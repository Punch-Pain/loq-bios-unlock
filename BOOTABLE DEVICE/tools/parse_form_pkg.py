import struct

with open(r'D:\tools\SetupUtility_pe32.efi', 'rb') as f:
    data = f.read()

# Form package #6: offset 0xE4B44, length 0x2DBF3
off = 0xE4B44
length = 0x2DBF3
pkg = data[off:off+length]

# EFI_HII_FORM_PACKAGE_HDR: Length(4) + Type(2) + ...
# Type should be 0x0002 for HII_FORM_PACKAGE
pkg_len = struct.unpack('<I', pkg[0:4])[0]
pkg_type = struct.unpack('<H', pkg[4:6])[0]
pkg_hsize = struct.unpack('<H', pkg[6:8])[0]
print(f'Form package header: len={pkg_len} type=0x{pkg_type:04X} hsize={pkg_hsize}')

# The form-set GUID should be at offset 8 (after header)
g = pkg[8:24]
guid_str = '%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X%02X%02X' % struct.unpack('<IHH8B', g)
print(f'FormSet GUID: {guid_str}')
print(f'FormSet GUID raw: {g.hex()}')

# Scan for all form-set GUIDs in this package
print('\nScanning for all form-set GUIDs in form package #6...')
i = 0
while i < len(pkg) - 16:
    # Look for EFI_IFR_FORM_SET opcodes (opcode 0x0E, length varies)
    if pkg[i] == 0x0E:
        if i + 17 < len(pkg):
            opcode_len = pkg[i+1]
            if opcode_len >= 16 and opcode_len <= 255:
                form_guid = pkg[i+5:i+21]
                try:
                    fs = '%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X%02X%02X' % struct.unpack('<IHH8B', form_guid)
                    print(f'  FormSet at 0x{off+i:08X} (rel 0x{i:06X}): GUID={fs}')
                    i += opcode_len
                    continue
                except:
                    pass
    i += 1

# Also look for the form-set GUIDs from SREP config
print('\nSearching for SREP form-set GUIDs in form data...')
guids = [
    ('Advanced', '9E76D4C6-487F-2A4D-98E9-87ADCCF35CCC'),
    ('Power', '732871A6-5F92-C646-90B4-A40F86A0917B'),
    ('1AB0E0C1', '1AB0E0C1-7E60-754B-B8BB-0631ECFAACF2'),
]
for name, guid_str in guids:
    parts = guid_str.split('-')
    a = int(parts[0], 16)
    b = int(parts[1], 16)
    c = int(parts[2], 16)
    d = bytes.fromhex(parts[3])
    e = bytes.fromhex(parts[4])
    guid_bin = struct.pack('<IHH', a, b, c) + d + e
    idx = pkg.find(guid_bin)
    if idx >= 0:
        print(f'  {name} ({guid_str}) found at package offset 0x{idx:06X} (file offset 0x{off+idx:08X})')
    else:
        print(f'  {name} ({guid_str}) NOT found')

# Count opcodes
print('\nIFR opcode distribution:')
from collections import Counter
opcodes = Counter()
i = 0
while i < len(pkg):
    op = pkg[i]
    opcodes[op] += 1
    if i + 1 < len(pkg):
        op_len = pkg[i+1]
        if op_len > 0:
            i += op_len
        else:
            i += 1
    else:
        break

# Show top opcodes with names
opcode_names = {
    0x0E: 'FormSet', 0x0F: 'Form', 0x10: 'End', 0x11: 'SubTitle',
    0x12: 'String', 0x14: 'Goto', 0x05: 'QuestionId1',
    0x2C: 'SuppressIf', 0x2D: 'GrayOutIf', 0x2E: 'DisableIf',
    0x17: 'CheckBox', 0x18: 'Numeric', 0x19: 'Password',
    0x1A: 'OneOf', 0x1B: 'OrderedList', 0x1C: 'TimeStamp',
    0x1D: 'Guid', 0x5B: 'Guid', 0x02: 'Ref',
}
print(f'Total opcodes: {sum(opcodes.values())}')
for op, count in opcodes.most_common(20):
    name = opcode_names.get(op, f'Unknown')
    print(f'  0x{op:02X} ({name}): {count}')
