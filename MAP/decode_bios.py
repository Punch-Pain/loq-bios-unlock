#!/usr/bin/env python3
"""
BIOS Settings Decoder — LOQ Essential 15IRX11 SECN22WW

Parses structured_map.md (IFR layout) + OS runtime dump .bin files.
Outputs: settings.csv, settings.md, settings.json

Usage:
  python decode_bios.py dump_dir [--output-dir dir]
  python decode_bios.py osdump
"""

import re
import struct
import csv
import json
import sys
import os
from pathlib import Path
from collections import OrderedDict

# VarStore GUID mapping (from IFR analysis)
VARGUID_MAP = {
    "Setup": "EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9",
    "SaSetup": "72C5E28C-7783-43A1-8767-FAD73FCCAFA4",
    "CpuSetup": "B08F97FF-E6E8-4193-A997-5E9E9B0ADB32",
    "MeSetup": "5432122D-D034-49D2-A6DE-65A829EB4C74",
    "PchSetup": "4570B7F1-ADE8-4943-8DC3-406472842384",
    "AdvanceConfig": "A04A27F4-DF00-4D42-B552-39511302113D",
    "SystemConfig": "A04A27F4-DF00-4D42-B552-39511302113D",
    "SetupCpuFeatures": "EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9",
    "SiSetup": "0FC50600-B162-4F49-B1B4-F0A86671276B",
    "PciBusSetup": "0FC50600-B162-4F49-B1B4-F0A86671276B",
    "MeSetupStorage": "5432122D-D034-49D2-A6DE-65A829EB4C74",
    "IccAdvancedSetupDataVar": "4669752B-1843-4591-8156-FEF38A4833F8",
}

# Expected varstore sizes from IFR
VARSIZES = {
    "Setup": 0xBAD,        # 2989
    "SaSetup": 0x578,      # 1400
    "CpuSetup": 0x3C1,     # 961
    "MeSetup": 0x36,       # 54
    "PchSetup": 0x80F,     # 2063
    "SetupCpuFeatures": 0x39,  # 57
    "AdvanceConfig": 0x8,   # 8 (boot-service-only)
    "SystemConfig": 0x4B0, # 1200 (boot-service-only)
}

# IFR opcode types
OPCODE_ONEOF = "OneOf"
OPCODE_NUMERIC = "Numeric"
OPCODE_CHECKBOX = "CheckBox"
OPCODE_TEXT = "Text"
OPCODE_REF = "Ref"
OPCODE_SUBTITLE = "Subtitle"
OPCODE_IMAGE = "Image"
OPCODE_LABEL = "Label"
OPCODE_KEY = "Key"
OPCODE_DEFAULT = "Default"
OPCODE_END = "End"
OPCODE_FORM = "Form"
OPCODE_FORM_SET = "FormSet"
OPCODE_SUPPRESS = "SuppressIf"
OPCODE_GRAYOUT = "GrayoutIf"
OPCODE_DISABLE = "DisableIf"
OPCODE_INVENTORY = "InconsistentIf"
OPCODE_QUESTION = "Question"


def parse_structured_map(map_path):
    """Parse structured_map.md into a list of IFR question entries."""
    with open(map_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entries = []
    current_form_id = None
    current_form_name = None
    current_form_path = []
    form_stack = []  # for nested forms

    varstore_re = re.compile(
        r'\[VarStore\s+(\w+)\s+@\s+(0x[0-9A-Fa-f]+),\s*QID\s+(0x[0-9A-Fa-f]+),\s*size\s+(\d+)\]'
    )
    numeric_re = re.compile(
        r'\[VarStore\s+(\w+)\s+@\s+(0x[0-9A-Fa-f]+),\s*QID\s+(0x[0-9A-Fa-f]+),\s*size\s+(\d+)\]\s+min\s+(0x[0-9A-Fa-f]+)\s+max\s+(0x[0-9A-Fa-f]+)'
    )
    form_re = re.compile(r'^## Form (0x[0-9A-Fa-f]+):\s+(.*)')
    form_ref_re = re.compile(r'\*\*(.+?)\*\*\s*->\s*Form\s+(0x[0-9A-Fa-f]+)')
    question_re = re.compile(r'^\s+-\s+\*\*(.+?)\*\*\s+\((\w+)\)')
    option_re = re.compile(r'^\s+-\s+options:\s*(.*)')

    for i, line in enumerate(lines):
        # Form header
        m = form_re.match(line)
        if m:
            form_id = m.group(1)
            form_name = m.group(2).strip()
            current_form_id = form_id
            current_form_name = form_name
            entries.append({
                'type': 'form',
                'form_id': form_id,
                'form_name': form_name,
                'line': i + 1
            })
            continue

        # Question with VarStore
        m = question_re.search(line)
        if m:
            question_name = m.group(1)
            question_type = m.group(2)

            # Check for VarStore on same line
            vm = varstore_re.search(line)
            if vm:
                varstore = vm.group(1)
                var_offset = int(vm.group(2), 16)
                qid = int(vm.group(3), 16)
                var_size = int(vm.group(4))

                # Check for numeric min/max
                nm = numeric_re.search(line)
                min_val = int(nm.group(5), 16) if nm else None
                max_val = int(nm.group(6), 16) if nm else None

                # Collect help text from next line
                help_text = ""
                if i + 1 < len(lines) and "help:" in lines[i + 1]:
                    help_text = lines[i + 1].strip().replace("- help: ", "")

                # Collect options from following lines
                options = []
                j = i + 1
                while j < len(lines) and j < i + 10:
                    om = option_re.match(lines[j])
                    if om:
                        opt_text = om.group(1).strip()
                        if opt_text and opt_text != "(no options listed)":
                            options = [o.strip() for o in opt_text.split(",")]
                        break
                    if question_re.search(lines[j]) or form_re.match(lines[j]):
                        break
                    j += 1

                entry = {
                    'type': question_type,
                    'form_id': current_form_id,
                    'form_name': current_form_name,
                    'name': question_name,
                    'varstore': varstore,
                    'var_offset': var_offset,
                    'var_size': var_size,
                    'qid': qid,
                    'min': min_val,
                    'max': max_val,
                    'options': options,
                    'help': help_text,
                    'line': i + 1
                }
                entries.append(entry)
            else:
                # Sub-form reference
                frm = form_ref_re.search(line)
                if frm:
                    entries.append({
                        'type': 'ref',
                        'form_id': current_form_id,
                        'form_name': current_form_name,
                        'name': frm.group(1),
                        'target_form': frm.group(2),
                        'line': i + 1
                    })

    return entries


def load_dump(dump_dir):
    """Load all .bin files from dump directory into a dict."""
    dumps = {}
    dump_path = Path(dump_dir)
    for bin_file in dump_path.glob("*.bin"):
        varstore_name = bin_file.stem
        data = bin_file.read_bytes()
        dumps[varstore_name] = data
        print(f"  Loaded {varstore_name}: {len(data)} bytes")
    return dumps


def read_field(data, offset, size_bits):
    """Read a field from binary data at given offset and size (in BITS).

    IFR stores size in bits: 8=1 byte, 16=2 bytes, 32=4 bytes, 64=8 bytes.
    """
    size_bytes = size_bits // 8
    if size_bytes < 1:
        size_bytes = 1
    if offset + size_bytes > len(data):
        return None
    raw = data[offset:offset + size_bytes]
    if size_bytes == 1:
        return raw[0]
    elif size_bytes == 2:
        return struct.unpack('<H', raw)[0]
    elif size_bytes == 4:
        return struct.unpack('<I', raw)[0]
    elif size_bytes == 8:
        return struct.unpack('<Q', raw)[0]
    else:
        return int.from_bytes(raw, 'little')


def decode_entry(entry, dumps):
    """Decode a single IFR question from dump data."""
    varstore = entry.get('varstore', '')
    offset = entry.get('var_offset', 0)
    size = entry.get('var_size', 8)

    if varstore not in dumps:
        return {
            'value': None,
            'raw_hex': None,
            'status': f'NO_DUMP ({varstore} not accessible)',
            'decoded': 'N/A'
        }

    data = dumps[varstore]
    value = read_field(data, offset, size)

    if value is None:
        return {
            'value': None,
            'raw_hex': None,
            'status': 'OUT_OF_RANGE',
            'decoded': 'N/A'
        }

    # Format raw hex
    size_bytes = size // 8
    if size_bytes <= 1:
        raw_hex = f"0x{value:02X}"
    elif size_bytes == 2:
        raw_hex = f"0x{value:04X}"
    elif size_bytes == 4:
        raw_hex = f"0x{value:08X}"
    else:
        raw_hex = f"0x{value:X}"

    # Decode based on type
    qtype = entry.get('type', '')
    decoded = raw_hex
    status = 'OK'

    if qtype == 'OneOf':
        # For OneOf, the value is an index or a direct value
        # Without option values in IFR text, we show raw
        decoded = f"{raw_hex} ({value})"
    elif qtype == 'Numeric':
        min_val = entry.get('min', 0)
        max_val = entry.get('max', 0xFFFF)
        # Apply unit hints from help text
        help_text = entry.get('help', '')
        name = entry.get('name', '')

        if 'milliwatts' in help_text.lower() or 'milli watts' in help_text.lower():
            decoded = f"{value} mW ({value/1000:.1f} W)"
        elif 'millivolts' in help_text.lower():
            decoded = f"{value} mV ({value/1000:.3f} V)"
        elif 'milliamps' in help_text.lower():
            decoded = f"{value} mA"
        elif 'mohms' in help_text.lower() or 'mOhm' in help_text.lower():
            decoded = f"{value/100:.2f} mOhm"
        elif 'seconds' in help_text.lower() or 'time window' in name.lower():
            decoded = f"{value} sec"
        elif 'micro tick' in help_text.lower():
            decoded = f"{value} µTicks"
        elif 'watts' in help_text.lower():
            decoded = f"{value} W"
        else:
            decoded = f"{value}"
    elif qtype == 'CheckBox':
        decoded = "Enabled" if value else "Disabled"

    return {
        'value': value,
        'raw_hex': raw_hex,
        'status': status,
        'decoded': decoded
    }


def generate_csv(results, output_path):
    """Write results to CSV."""
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Form', 'Name', 'Type', 'VarStore', 'Offset', 'Size',
            'QID', 'Value', 'Raw', 'Decoded', 'Status', 'Help'
        ])
        for r in results:
            if r.get('type') in ('form', 'ref'):
                continue
            writer.writerow([
                r.get('form_name', ''),
                r.get('name', ''),
                r.get('type', ''),
                r.get('varstore', ''),
                f"0x{r.get('var_offset', 0):X}",
                r.get('var_size', ''),
                f"0x{r.get('qid', 0):X}",
                r.get('decoded_value', {}).get('value', ''),
                r.get('decoded_value', {}).get('raw_hex', ''),
                r.get('decoded_value', {}).get('decoded', ''),
                r.get('decoded_value', {}).get('status', ''),
                r.get('help', '')[:120]
            ])
    print(f"  CSV written: {output_path}")


def generate_markdown(results, output_path):
    """Write results to Markdown."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# BIOS Settings Decode — LOQ Essential 15IRX11 SECN22WW\n\n")
        f.write("Generated from OS runtime dump (GetFirmwareEnvironmentVariable)\n\n")

        current_form = None
        for r in results:
            if r.get('type') == 'form':
                current_form = r
                f.write(f"\n## Form {r['form_id']}: {r['form_name']}\n\n")
                f.write("| Setting | Type | VarStore | Offset | Decoded | Raw | Status |\n")
                f.write("|---------|------|----------|--------|---------|-----|--------|\n")
                continue

            if r.get('type') in ('ref',):
                f.write(f"\n### → {r['name']} (→ Form {r.get('target_form', '?')})\n")
                continue

            if r.get('type') in ('form',):
                continue

            dv = r.get('decoded_value', {})
            f.write(f"| {r.get('name', '?')} | {r.get('type', '')} | {r.get('varstore', '')} | "
                    f"0x{r.get('var_offset', 0):X} | {dv.get('decoded', 'N/A')} | "
                    f"{dv.get('raw_hex', '?')} | {dv.get('status', '')} |\n")

    print(f"  Markdown written: {output_path}")


def generate_json(results, output_path):
    """Write results to JSON."""
    output = {
        'machine': 'Lenovo LOQ Essential 15IRX11',
        'bios': 'SECN22WW',
        'source': 'OS runtime dump (GetFirmwareEnvironmentVariable)',
        'varstores_dumped': [],
        'varstores_missing': [],
        'questions': []
    }

    dumped = set()
    for r in results:
        if r.get('type') not in ('form', 'ref') and r.get('varstore'):
            vs = r['varstore']
            if vs not in dumped:
                dumped.add(vs)
                dv = r.get('decoded_value', {})
                if 'NO_DUMP' in dv.get('status', ''):
                    output['varstores_missing'].append(vs)
                else:
                    output['varstores_dumped'].append(vs)

    for r in results:
        if r.get('type') in ('form', 'ref'):
            continue
        q = {
            'form': r.get('form_name', ''),
            'name': r.get('name', ''),
            'type': r.get('type', ''),
            'varstore': r.get('varstore', ''),
            'offset': r.get('var_offset', 0),
            'size': r.get('var_size', 0),
            'qid': r.get('qid', 0),
            'decoded': r.get('decoded_value', {}),
            'help': r.get('help', '')
        }
        output['questions'].append(q)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    print(f"  JSON written: {output_path}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description='BIOS Settings Decoder')
    parser.add_argument('dump_dir', help='Directory containing .bin dump files')
    parser.add_argument('--map', default=None, help='Path to structured_map.md')
    parser.add_argument('--output-dir', '-o', default=None, help='Output directory')
    args = parser.parse_args()

    # Find structured_map.md
    map_path = args.map
    if not map_path:
        # Search common locations
        candidates = [
            r"C:\Abdalrhman\Devlopment\BIOS\MAP\structured_map.md",
            os.path.join(os.path.dirname(__file__), '..', 'MAP', 'structured_map.md'),
            os.path.join(os.path.dirname(__file__), 'structured_map.md'),
        ]
        for c in candidates:
            if os.path.isfile(c):
                map_path = c
                break

    if not map_path or not os.path.isfile(map_path):
        print("ERROR: structured_map.md not found. Use --map to specify path.")
        sys.exit(1)

    output_dir = args.output_dir or args.dump_dir

    print(f"=== BIOS Settings Decoder ===")
    print(f"  IFR Map: {map_path}")
    print(f"  Dump dir: {args.dump_dir}")
    print(f"  Output dir: {output_dir}")

    # Step 1: Parse IFR map
    print(f"\n[1] Parsing IFR map...")
    entries = parse_structured_map(map_path)
    questions = [e for e in entries if e.get('type') not in ('form', 'ref')]
    forms = [e for e in entries if e.get('type') == 'form']
    print(f"  Found {len(forms)} forms, {len(questions)} questions with VarStore bindings")

    # Step 2: Load dump
    print(f"\n[2] Loading dump files...")
    dumps = load_dump(args.dump_dir)
    if not dumps:
        print("  ERROR: No .bin files found in dump directory")
        sys.exit(1)

    # Step 3: Decode
    print(f"\n[3] Decoding {len(questions)} questions...")
    results = []
    decoded_count = 0
    skipped_count = 0

    for entry in entries:
        if entry.get('type') in ('form', 'ref'):
            results.append(entry)
            continue

        dv = decode_entry(entry, dumps)
        entry['decoded_value'] = dv
        results.append(entry)

        if dv['status'] == 'OK':
            decoded_count += 1
        else:
            skipped_count += 1

    print(f"  Decoded: {decoded_count}, Skipped: {skipped_count}")

    # Step 4: Write outputs
    print(f"\n[4] Writing outputs...")
    os.makedirs(output_dir, exist_ok=True)

    csv_path = os.path.join(output_dir, "settings.csv")
    md_path = os.path.join(output_dir, "settings.md")
    json_path = os.path.join(output_dir, "settings.json")

    generate_csv(results, csv_path)
    generate_markdown(results, md_path)
    generate_json(results, json_path)

    print(f"\n=== Done ===")
    print(f"  {decoded_count} settings decoded from {len(dumps)} varstores")
    print(f"  Outputs in: {output_dir}")


if __name__ == '__main__':
    main()
