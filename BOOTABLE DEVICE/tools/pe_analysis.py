import struct
import sys

with open(r'D:\SetupUtilityApp_pe32.efi', 'rb') as f:
    data = f.read()

pe_off = struct.unpack('<I', data[60:64])[0]
print(f'PE offset: {pe_off}')
sig = data[pe_off:pe_off+4]
print(f'PE signature: {sig}')

coff = pe_off + 4
machine = struct.unpack('<H', data[coff:coff+2])[0]
num_sections = struct.unpack('<H', data[coff+2:coff+4])[0]
opt_hdr_size = struct.unpack('<H', data[coff+16:coff+18])[0]
print(f'Machine: 0x{machine:04X} (0xEF00 = EFI)')
print(f'Number of sections: {num_sections}')
print(f'Optional header size: {opt_hdr_size}')

opt = coff + 20
magic = struct.unpack('<H', data[opt:opt+2])[0]
print(f'Optional header magic: 0x{magic:04X} (0x20B=PE32+, 0x10B=PE32)')

subsystem = struct.unpack('<H', data[opt+68:opt+70])[0] if magic == 0x20B else struct.unpack('<H', data[opt+68:opt+70])[0]
print(f'Subsystem: {subsystem} (10=EFI_APPLICATION, 11=EFI_BOOT_SERVICE_DRIVER, 12=EFI_RUNTIME_DRIVER)')

image_size = struct.unpack('<I', data[opt+56:opt+60])[0]
print(f'Image size from header: 0x{image_size:X} ({image_size} bytes)')

entry = struct.unpack('<I', data[opt+16:opt+20])[0] if magic == 0x10B else struct.unpack('<I', data[opt+16:opt+20])[0]
print(f'Entry point RVA: 0x{entry:08X}')

sec_start = opt + opt_hdr_size
print(f'\nSection headers start at offset: {sec_start}')
for i in range(num_sections):
    off = sec_start + i * 40
    if off + 40 > len(data):
        print(f'  Section {i}: TRUNCATED')
        continue
    name = data[off:off+8].rstrip(b'\x00').decode('ascii', errors='replace')
    vsize = struct.unpack('<I', data[off+8:off+12])[0]
    vaddr = struct.unpack('<I', data[off+12:off+16])[0]
    raw_size = struct.unpack('<I', data[off+16:off+20])[0]
    raw_ptr = struct.unpack('<I', data[off+20:off+24])[0]
    chars = struct.unpack('<I', data[off+36:off+40])[0]
    print(f'  Section {i}: "{name}" VA=0x{vaddr:08X} VSize=0x{vsize:X} Raw=0x{raw_ptr:X} RawSize=0x{raw_size:X} Chars=0x{chars:08X}')
    # Dump first 16 bytes of each section
    if raw_ptr > 0 and raw_size > 0 and raw_ptr + min(raw_size, 16) <= len(data):
        print(f'    First bytes: {data[raw_ptr:raw_ptr+16].hex()}')

# Search for HII form package signatures (7B 00 for EFI_HII_FORM_PACKAGE_HDR)
print('\nSearching for HII form package signatures...')
for i in range(len(data) - 4):
    if data[i] == 0x7B and data[i+1] == 0x00 and data[i+2] == 0x00 and data[i+3] == 0x00:
        pkg_len = struct.unpack('<I', data[i:i+4])[0]
        if 0x10 < pkg_len < 0x100000:
            print(f'  Possible HII form package at 0x{i:08X}, length={pkg_len} (0x{pkg_len:X})')
            # Check for known form-set GUID nearby
            if i + 28 < len(data):
                guid_bytes = data[i+4:i+20]
                guid_str = '%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X%02X%02X' % struct.unpack('<IHH8B', guid_bytes)
                print(f'    Form-set GUID: {guid_str}')

# Also search for SuppressIf opcodes (0x2C) and GrayOutIf (0x2D) and SuppressIf/GrayOutIf/DisableIf
print('\nSearching for EFI_IFR_SUPPRESS_IF (0x2C) opcodes...')
count = 0
for i in range(len(data)):
    if data[i] == 0x2C:
        count += 1
        if count <= 5:
            print(f'  SuppressIf at 0x{i:08X}, next bytes: {data[i:i+8].hex()}')
print(f'  Total SuppressIf opcodes found: {count}')

# Search for form-set GUID pattern
print('\nSearching for known SREP form-set GUIDs...')
guids = [
    ('Advanced', '9E76D4C6-487F-2A4D-98E9-87ADCCF35CCC'),
    ('Power', '732871A6-5F92-C646-90B4-A40F86A0917B'),
    ('1AB0E0C1', '1AB0E0C1-7E60-754B-B8BB-0631ECFAACF2'),
]
for name, guid_str in guids:
    parts = guid_str.split('-')
    # GUID binary format: first 3 parts LE, next 2 parts BE
    a = int(parts[0], 16)
    b = int(parts[1], 16)
    c = int(parts[2], 16)
    d = bytes.fromhex(parts[3])
    e = bytes.fromhex(parts[4])
    guid_bin = struct.pack('<IHH', a, b, c) + d + e
    idx = data.find(guid_bin)
    if idx >= 0:
        print(f'  {name} ({guid_str}) found at offset 0x{idx:08X}')
    else:
        print(f'  {name} ({guid_str}) NOT found')
