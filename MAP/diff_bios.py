#!/usr/bin/env python3
"""
BIOS Settings Differ — Compare two dump directories

Usage:
  python diff_bios.py <dir_a> <dir_b> [--output <file>]
  python diff_bios.py C:\osdump_before C:\osdump_after
"""

import struct
import csv
import sys
import os
from pathlib import Path

# Import decoder
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode_bios import parse_structured_map, load_dump, read_field


def diff_dirs(dir_a, dir_b, map_path=None):
    """Compare two dump directories and return differences."""
    # Find map
    if not map_path:
        candidates = [
            r"C:\Abdalrhman\Devlopment\BIOS\MAP\structured_map.md",
            os.path.join(os.path.dirname(__file__), '..', 'MAP', 'structured_map.md'),
        ]
        for c in candidates:
            if os.path.isfile(c):
                map_path = c
                break

    entries = parse_structured_map(map_path)
    questions = [e for e in entries if e.get('type') not in ('form', 'ref')]

    dumps_a = load_dump(dir_a)
    dumps_b = load_dump(dir_b)

    diffs = []
    for q in questions:
        vs = q.get('varstore', '')
        offset = q.get('var_offset', 0)
        size = q.get('var_size', 8)

        in_a = vs in dumps_a
        in_b = vs in dumps_b

        if not in_a and not in_b:
            continue

        val_a = read_field(dumps_a[vs], offset, size) if in_a else None
        val_b = read_field(dumps_b[vs], offset, size) if in_b else None

        if val_a != val_b:
            diffs.append({
                'form': q.get('form_name', ''),
                'name': q.get('name', ''),
                'type': q.get('type', ''),
                'varstore': vs,
                'offset': f"0x{offset:X}",
                'value_a': val_a,
                'value_b': val_b,
                'status_a': 'OK' if in_a else 'MISSING',
                'status_b': 'OK' if in_b else 'MISSING',
            })

    return diffs


def main():
    import argparse
    parser = argparse.ArgumentParser(description='BIOS Settings Differ')
    parser.add_argument('dir_a', help='First dump directory (baseline)')
    parser.add_argument('dir_b', help='Second dump directory (compare)')
    parser.add_argument('--output', '-o', default=None, help='Output file')
    parser.add_argument('--map', default=None, help='Path to structured_map.md')
    args = parser.parse_args()

    print(f"=== BIOS Settings Differ ===")
    print(f"  Baseline: {args.dir_a}")
    print(f"  Compare:  {args.dir_b}")

    diffs = diff_dirs(args.dir_a, args.dir_b, args.map)

    print(f"\n  Found {len(diffs)} differences\n")

    if not diffs:
        print("  No differences found.")
        return

    # Print table
    print(f"  {'Setting':<40} {'VarStore':<16} {'Offset':<10} {'Baseline':<12} {'Compare':<12}")
    print(f"  {'-'*40} {'-'*16} {'-'*10} {'-'*12} {'-'*12}")

    for d in diffs:
        a_str = f"0x{d['value_a']:X}" if d['value_a'] is not None else d['status_a']
        b_str = f"0x{d['value_b']:X}" if d['value_b'] is not None else d['status_b']
        print(f"  {d['name']:<40} {d['varstore']:<16} {d['offset']:<10} {a_str:<12} {b_str:<12}")

    # Write CSV if requested
    if args.output:
        with open(args.output, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Setting', 'Type', 'VarStore', 'Offset', 'Baseline', 'Compare'])
            for d in diffs:
                writer.writerow([
                    d['name'], d['type'], d['varstore'], d['offset'],
                    f"0x{d['value_a']:X}" if d['value_a'] is not None else d['status_a'],
                    f"0x{d['value_b']:X}" if d['value_b'] is not None else d['status_b']
                ])
        print(f"\n  CSV written: {args.output}")


if __name__ == '__main__':
    main()
