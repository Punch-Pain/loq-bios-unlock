#!/usr/bin/env python3
"""
Static RE of SetupUtilityApp_pe32.efi
Analyzes: strings, GUID references, entry point disassembly, hang hypothesis.
"""
import struct
import sys
import os

def read_pe(path):
    with open(path, 'rb') as f:
        return f.read()

def get_pe_info(data):
    """Parse PE32+ header to find sections, entry point."""
    e_lfanew = struct.unpack_from('<I', data, 0x3C)[0]
    if data[e_lfanew:e_lfanew+4] != b'PE\x00\x00':
        return None
    
    coff = e_lfanew + 4
    machine = struct.unpack_from('<H', data, coff)[0]
    num_sections = struct.unpack_from('<H', data, coff + 2)[0]
    opt_hdr_size = struct.unpack_from('<H', data, coff + 16)[0]
    characteristics = struct.unpack_from('<H', data, coff + 18)[0]
    
    opt = coff + 20
    magic = struct.unpack_from('<H', data, opt)[0]
    if magic == 0x20B:  # PE32+
        entry_rva = struct.unpack_from('<I', data, opt + 16)[0]
        image_base = struct.unpack_from('<Q', data, opt + 24)[0]
        section_off = opt + opt_hdr_size
    else:
        entry_rva = struct.unpack_from('<I', data, opt + 16)[0]
        image_base = struct.unpack_from('<I', data, opt + 28)[0]
        section_off = opt + opt_hdr_size
    
    sections = []
    for i in range(num_sections):
        soff = section_off + i * 40
        name = data[soff:soff+8].rstrip(b'\x00').decode('ascii', errors='replace')
        vsize = struct.unpack_from('<I', data, soff + 8)[0]
        vaddr = struct.unpack_from('<I', data, soff + 12)[0]
        rawsize = struct.unpack_from('<I', data, soff + 16)[0]
        rawptr = struct.unpack_from('<I', data, soff + 20)[0]
        chars = struct.unpack_from('<I', data, soff + 36)[0]
        sections.append({
            'name': name, 'vaddr': vaddr, 'vsize': vsize,
            'rawptr': rawptr, 'rawsize': rawsize, 'chars': chars
        })
    
    return {
        'machine': hex(machine),
        'entry_rva': entry_rva,
        'image_base': image_base,
        'sections': sections,
        'num_sections': num_sections
    }

def extract_strings(data, min_len=4):
    """Extract ASCII strings from binary data."""
    strings = []
    current = b''
    start = 0
    for i, b in enumerate(data):
        if 0x20 <= b < 0x7f:
            if not current:
                start = i
            current += bytes([b])
        else:
            if len(current) >= min_len:
                strings.append((start, current.decode('ascii')))
            current = b''
    if len(current) >= min_len:
        strings.append((start, current.decode('ascii')))
    return strings

def extract_guids(data):
    """Find potential EFI_GUID-like 16-byte patterns."""
    guids = []
    # EFI GUID format: Data1(4) Data2(2) Data3(2) Data4(8)
    known_guids = {
        'EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9': 'Setup / VarStore GUID',
        'A04A27F4-DF00-4D42-B552-39511302113D': 'SystemConfig / AdvanceConfig',
        '72C5E28C-7783-43A1-8767-FAD73FCCAFA4': 'SaSetup',
        'B08F97FF-E6E8-4193-A997-5E9E9B0ADB32': 'CpuSetup',
        '4570B7F1-ADE8-4943-8DC3-406472842384': 'PchSetup',
        'AAF8E719-48F8-4099-A6F7-645FBD694C3D': 'SiSetup',
        '5432122D-D034-49D2-A6DE-65A829EB4C74': 'MeSetup',
        'C6D4769E-7F48-4D2A-98E9-87ADCCF35CCC': 'Advanced FormSet GUID',
        '732871A6-5F92-C646-90B4-A40F86A0917B': 'Power FormSet GUID',
    }
    
    # Well-known UEFI GUIDs
    well_known = {
        '387477C1-69C7-11D2-8E39-00A0C969723B': 'EFI_PEIFileInfo GUID',
        '0F99B5E2-1FFF-4F86-94B2-98D223A6C9A4': 'EFI loaded Image Protocol',
        '5B1B31A1-9562-11D2-8E3F-00A0C969723B': 'EFI_SIMPLE_TEXT_INPUT_PROTOCOL',
        '387477C2-69C7-11D2-8E39-00A0C969723B': 'EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL',
        '49152ECC-6F73-4EFA-8090-9A4D01CF20C1': 'EFI_HII_DATABASE_PROTOCOL',
        'B9D4C364-6050-4DE1-B6CC-3400608AE5C0': 'EFI_HII_CONFIG_ROUTING_PROTOCOL',
        '6441F818-6362-4E44-B570-7DBA519C56A2': 'EFI_FORM_BROWSER2_PROTOCOL',
        '964E5B21-6459-11D2-8E39-00A0C969723B': 'EFI_PCI_IO_PROTOCOL',
        '09576E91-6D3F-11D2-8E39-00A0C969723B': 'EFI_DEVICE_PATH_PROTOCOL',
        'CB3EE4D5-7CE5-470D-9660-12B19B4CA1F5': 'EFIGraphicsOutputProtocol',
        '5B1B31A1-9562-11D2-8E3F-00A0C969723B': 'EFI_SIMPLE_TEXT_INPUT_PROTOCOL',
        'EF9F1806-FCDB-4C37-83E6-F490D6A88EAD': 'Insyde H2O specific',
    }
    
    for i in range(len(data) - 15):
        d1 = struct.unpack_from('<I', data, i)[0]
        d2 = struct.unpack_from('<H', data, i + 4)[0]
        d3 = struct.unpack_from('<H', data, i + 6)[0]
        d4 = data[i + 8:i + 16]
        
        # Basic GUID plausibility: d4 bytes shouldn't all be 0xFF or all 0x00
        if d4 == b'\xff' * 8 or d4 == b'\x00' * 8:
            continue
        
        guid_str = f'{d1:08X}-{d2:04X}-{d3:04X}-{"-".join(f"{b:02X}{a:02X}" for a, b in zip(d4[::2], d4[1::2]))}'
        
        if guid_str in known_guids:
            guids.append((i, guid_str, known_guids[guid_str]))
        elif guid_str in well_known:
            guids.append((i, guid_str, well_known[guid_str]))
    
    return guids

def disassemble_entry(data, pe_info):
    """Disassemble from entry point. Uses Python built-in byte analysis if capstone unavailable."""
    try:
        from capstone import Cs, CS_ARCH_X86, CS_MODE_64
        has_capstone = True
    except ImportError:
        has_capstone = False
    
    entry_rva = pe_info['entry_rva']
    img_base = pe_info['image_base']
    
    # Find which section contains entry_rva
    entry_section = None
    for sec in pe_info['sections']:
        if sec['vaddr'] <= entry_rva < sec['vaddr'] + sec['vsize']:
            entry_section = sec
            break
    
    if not entry_section:
        return f"Entry RVA {hex(entry_rva)} not found in any section"
    
    # Calculate file offset of entry point
    raw_offset = entry_section['rawptr'] + (entry_rva - entry_section['vaddr'])
    entry_va = img_base + entry_rva
    
    result = []
    result.append(f"Entry point: VA {hex(entry_va)}, RVA {hex(entry_rva)}, file offset {hex(raw_offset)}")
    result.append(f"Entry section: {entry_section['name']} ({hex(entry_section['vaddr'])}-{hex(entry_section['vaddr']+entry_section['vsize'])})")
    
    # Extract code bytes (enough for thorough analysis)
    code_start = raw_offset
    code_end = min(raw_offset + 0x800, len(data))
    code = data[code_start:code_end]
    
    if has_capstone:
        md = Cs(CS_ARCH_X86, CS_MODE_64)
        md.detail = True
        count = 0
        for insn in md.disasm(code, entry_va):
            result.append(f"  {hex(insn.address)}: {insn.mnemonic}\t{insn.op_str}")
            count += 1
            if count >= 200:
                break
    else:
        # Manual pattern analysis
        result.append("  (capstone not available - manual pattern analysis)")
        
        # Scan for key patterns
        # CALL [rip+offset] - common for indirect calls (LocateProtocol etc)
        call_rel_pattern = bytes([0xFF, 0x15])  # call qword [rip+disp32]
        # JMP [rip+offset]
        jmp_rel_pattern = bytes([0xFF, 0x25])
        # INT3
        int3 = bytes([0xCC])
        # RET
        ret = bytes([0xC3])
        # PUSH rbp / MOV rbp,rsp (function prologue)
        push_rbp_mov = bytes([0x55, 0x48, 0x89, 0xE5])
        push_rbp_mov2 = bytes([0x55, 0x48, 0x8B, 0xEC])
        
        # Search for patterns
        i = 0
        while i < len(code) - 1:
            # Call [rip+disp32]
            if code[i:i+2] == call_rel_pattern and i + 6 <= len(code):
                disp = struct.unpack_from('<i', code, i + 2)[0]
                target = entry_va + i + 6 + disp
                result.append(f"  {hex(entry_va + i)}: call [rip+{hex(disp)}] -> {hex(target)}")
                i += 6
                continue
            # Call rel32
            if code[i] == 0xE8 and i + 5 <= len(code):
                disp = struct.unpack_from('<i', code, i + 1)[0]
                target = entry_va + i + 5 + disp
                result.append(f"  {hex(entry_va + i)}: call {hex(target)}")
                i += 5
                continue
            # JMP rel32
            if code[i] == 0xE9 and i + 5 <= len(code):
                disp = struct.unpack_from('<i', code, i + 1)[0]
                target = entry_va + i + 5 + disp
                result.append(f"  {hex(entry_va + i)}: jmp {hex(target)}")
                i += 5
                continue
            # JMP [rip+disp32]
            if code[i:i+2] == jmp_rel_pattern and i + 6 <= len(code):
                disp = struct.unpack_from('<i', code, i + 2)[0]
                target = entry_va + i + 6 + disp
                result.append(f"  {hex(entry_va + i)}: jmp [rip+{hex(disp)}] -> {hex(target)}")
                i += 6
                continue
            # RET
            if code[i] == 0xC3:
                result.append(f"  {hex(entry_va + i)}: ret")
                i += 1
                continue
            # INT3
            if code[i] == 0xCC:
                result.append(f"  {hex(entry_va + i)}: int3")
                i += 1
                continue
            # PUSH rbp
            if code[i] == 0x55:
                result.append(f"  {hex(entry_va + i)}: push rbp")
                i += 1
                continue
            # MOV rbp, rsp
            if code[i:i+4] == b'\x48\x89\xec' or code[i:i+4] == b'\x48\x8b\xec':
                result.append(f"  {hex(entry_va + i)}: mov rbp, rsp")
                i += 4
                continue
            i += 1
    
    return '\n'.join(result)

def analyze_startup_code(data, pe_info):
    """Analyze the startup/boot path code for UEFI application behavior."""
    sections = pe_info['sections']
    result = []
    
    # Find .text section
    text_section = None
    for sec in sections:
        if sec['name'] == '.text' or sec['chars'] & 0x20:
            text_section = sec
            break
    
    if not text_section:
        result.append("No .text section found")
        return '\n'.join(result)
    
    # Check for key UEFI patterns in the binary
    patterns_to_check = [
        (b'BootCurrent', 'BootCurrent variable reference'),
        (b'OsIndications', 'OsIndications variable reference'),
        (b'LoadOptions', 'LoadOptions reference'),
        (b'BootOptions', 'BootOptions reference'),
        (b'StartImage', 'StartImage call'),
        (b'LoadImage', 'LoadImage call'),
        (b'Exit', 'Exit call'),
        (b'ConnectController', 'ConnectController call'),
        (b'DisconnectController', 'DisconnectController call'),
        (b'LocateProtocol', 'LocateProtocol call'),
        (b'HII', 'HII reference'),
        (b'FormBrowser', 'FormBrowser reference'),
        (b'SetVariable', 'SetVariable call'),
        (b'GetVariable', 'GetVariable call'),
        (b'WaitForEvent', 'WaitForEvent call'),
        (b'InstallProtocol', 'InstallProtocol call'),
        (b'ReinstallProtocolInterface', 'ReinstallProtocolInterface call'),
        (b'gRT', 'Runtime Services table reference'),
        (b'gBS', 'Boot Services table reference'),
    ]
    
    result.append("=== Pattern scan in full binary ===")
    for pattern, desc in patterns_to_check:
        offsets = []
        start = 0
        while True:
            pos = data.find(pattern, start)
            if pos == -1:
                break
            offsets.append(hex(pos))
            start = pos + 1
            if len(offsets) >= 5:
                break
        if offsets:
            result.append(f"  [{desc}] at: {', '.join(offsets)}")
    
    return '\n'.join(result)

def main():
    path = r"D:\SetupUtilityApp_pe32.efi"
    data = read_pe(path)
    
    result = []
    result.append(f"=== SetupUtilityApp_pe32.efi Static Analysis ===")
    result.append(f"File size: {len(data)} bytes")
    result.append(f"First bytes: {data[:16].hex(' ')}")
    result.append("")
    
    # PE Info
    pe_info = get_pe_info(data)
    if pe_info:
        result.append("=== PE32+ Header ===")
        result.append(f"Machine: {pe_info['machine']}")
        result.append(f"Entry RVA: {hex(pe_info['entry_rva'])}")
        result.append(f"Image Base: {hex(pe_info['image_base'])}")
        result.append(f"Sections ({pe_info['num_sections']}):")
        for sec in pe_info['sections']:
            chars = []
            if sec['chars'] & 0x20: chars.append('CODE')
            if sec['chars'] & 0x40: chars.append('IDATA')
            if sec['chars'] & 0x80: chars.append('UDATA')
            if sec['chars'] & 0x20000000: chars.append('EXEC')
            if sec['chars'] & 0x40000000: chars.append('READ')
            if sec['chars'] & 0x80000000: chars.append('WRITE')
            result.append(f"  {sec['name']:8s} VA={hex(sec['vaddr']):>10s} VSize={hex(sec['vsize']):>8s} Raw={hex(sec['rawptr']):>8s} Chars={','.join(chars)}")
        result.append("")
    
    # Strings
    result.append("=== ASCII Strings ===")
    strings = extract_strings(data)
    for offset, s in strings[:100]:
        result.append(f"  {hex(offset):>6s}: {s[:120]}")
    result.append(f"  ... total strings found: {len(strings)}")
    result.append("")
    
    # GUIDs
    result.append("=== GUID-like patterns ===")
    guids = extract_guids(data)
    for offset, guid, desc in guids:
        result.append(f"  {hex(offset):>6s}: {guid} = {desc}")
    result.append(f"  ... total GUIDs found: {len(guids)}")
    result.append("")
    
    # Pattern analysis
    result.append("=== UEFI Boot Path Pattern Analysis ===")
    result.append(analyze_startup_code(data, pe_info))
    result.append("")
    
    # Disassembly
    result.append("=== Entry Point Disassembly ===")
    result.append(disassemble_entry(data, pe_info))
    result.append("")
    
    # Write output
    out_path = r"D:\tools\SetupUtilityApp_RE.txt"
    with open(out_path, 'w') as f:
        f.write('\n'.join(result))
    
    # Also print to console
    print('\n'.join(result))
    print(f"\n=== Output written to {out_path} ===")

if __name__ == '__main__':
    main()
