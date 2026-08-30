import struct, os

with open(r'D:\File_DXE_driver_SetupUtility_SetupUtility.ffs', 'rb') as f:
    data = f.read()

# Form package offsets from the list output
packages = [
    (0xDDB44, 0x1F3, 0),
    (0xDEEB4, 0x691, 1),
    (0xE0584, 0x1CF, 2),
    (0xE1794, 0x248, 3),
    (0xE2A14, 0x21D, 4),
    (0xE3C64, 0x85, 5),
    (0xE4D24, 0x2DBF3, 6),
    (0x1139A4, 0x1BD, 7),
    (0x114B94, 0x16C, 8),
    (0x115D34, 0x484, 9),
    (0x142654, 0x217, 10),
    (0x1438A4, 0xBD0, 11),
    (0x1454A4, 0xCC7, 12),
    (0x1471C4, 0x1DC, 13),
]

str_pkgs = [
    (0x5BD64, 0x7D3AD, 'en-US', 0),
    (0x134DA4, 0xA187, 'en-US', 2),
]

# Check the big form package at 0xE4D24
off = 0xE4D24
print(f'Form package #6 at 0x{off:X}:')
hdr_len = struct.unpack('<I', data[off:off+4])[0]
hdr_type = struct.unpack('<H', data[off+4:off+6])[0]
hdr_hsize = struct.unpack('<H', data[off+6:off+8])[0]
print(f'  Length: {hdr_len}')
print(f'  Type: {hdr_type}')
print(f'  Header size: {hdr_hsize}')
g = data[off+8:off+24]
guid_str = '%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X%02X%02X' % struct.unpack('<IHH8B', g)
print(f'  FormSet GUID: {guid_str}')
print(f'  First 64 bytes: {data[off:off+64].hex()}')

# Extract each form package
for idx, (foff, flen, fnum) in enumerate(packages):
    pkg_data = data[foff:foff+flen]
    out_path = f'D:\\tools\\form_pkg_{fnum}.bin'
    with open(out_path, 'wb') as pf:
        pf.write(pkg_data)

# Extract string packages
for soff, slen, lang, snum in str_pkgs:
    pkg_data = data[soff:soff+slen]
    out_path = f'D:\\tools\\str_pkg_{snum}.bin'
    with open(out_path, 'wb') as pf:
        pf.write(pkg_data)

# Try to scan the ENTIRE FFS for form-set GUIDs
print('\nScanning entire FFS for SREP GUIDs...')
guids_to_find = [
    ('Advanced', '9E76D4C6-487F-2A4D-98E9-87ADCCF35CCC'),
    ('Power', '732871A6-5F92-C646-90B4-A40F86A0917B'),
    ('1AB0E0C1', '1AB0E0C1-7E60-754B-B8BB-0631ECFAACF2'),
]
for name, guid_str in guids_to_find:
    parts = guid_str.split('-')
    a = int(parts[0], 16)
    b = int(parts[1], 16)
    c = int(parts[2], 16)
    d = bytes.fromhex(parts[3])
    e = bytes.fromhex(parts[4])
    guid_bin = struct.pack('<IHH', a, b, c) + d + e
    idx = data.find(guid_bin)
    if idx >= 0:
        print(f'  {name} ({guid_str}) found at FFS offset 0x{idx:08X}')
    else:
        print(f'  {name} ({guid_str}) NOT found')

# Also search for EFI_HII_FORM_PACKAGE signature: type=0x0002 at offset 0 within form package header
# EFI_HII_FORM_PACKAGE_HDR: Length(4) + Type(0x0002)(2) + ...
print('\nSearching for HII form package headers (type=0x0002)...')
for i in range(len(data) - 8):
    if struct.unpack('<H', data[i+4:i+6])[0] == 0x0002:
        pkg_len = struct.unpack('<I', data[i:i+4])[0]
        if 0x10 < pkg_len < 0x100000:
            print(f'  HII form package at 0x{i:08X}, length={pkg_len} (0x{pkg_len:X})')

print(f'\nExtracted {len(packages)} form packages and {len(str_pkgs)} string packages')
