import struct, sys

with open(r'D:\SetupUtilityApp_pe32.efi', 'rb') as f:
    data = f.read()

print(f"File size: {len(data)} bytes")

# Search for UCS-2LE strings (variable names)
names = ['Setup', 'SystemConfig', 'AdvanceConfig', 'SetupCpuFeatures', 'CpuSetup',
         'PchSetup', 'SaSetup', 'MeSetup', 'BootOrder', 'PlatformLang', 'ConIn',
         'ConOut', 'ErrOut', 'Timeout', 'BootNext', 'SecureBoot', 'db', 'dbx',
         'KEK', 'PK', 'H2OFormBrowser', 'SetupUtility', 'FormBrowser',
         'HiiDatabase', 'HiiConfigAccess', 'ConfigAccess', 'FormBrowser2',
         'D3Cold', 'Bclk', 'Overclock', 'Performance', 'Thermal', 'Pch']
for name in names:
    ucs2 = name.encode('utf-16-le')
    offset = 0
    while True:
        idx = data.find(ucs2, offset)
        if idx == -1:
            break
        ctx = data[max(0,idx-4):idx+len(ucs2)+8]
        print(f'UCS-2 "{name}" at 0x{idx:X}')
        print(f'  hex: {ctx.hex(" ")}')
        offset = idx + 1

# Find PE32 sections
mz = struct.unpack_from('<H', data, 0)[0]
pe_off = struct.unpack_from('<I', data, 0x3C)[0]
num_sections = struct.unpack_from('<H', data, pe_off + 6)[0]
opt_hdr_size = struct.unpack_from('<H', data, pe_off + 20)[0]

print(f"\nPE32+ at 0x{pe_off:X}, {num_sections} sections")
for i in range(num_sections):
    sec = pe_off + 24 + opt_hdr_size + i * 40
    name = data[sec:sec+8].rstrip(b'\x00').decode('ascii', errors='replace')
    vsize = struct.unpack_from('<I', data, sec + 8)[0]
    vaddr = struct.unpack_from('<I', data, sec + 12)[0]
    rawsize = struct.unpack_from('<I', data, sec + 16)[0]
    rawoff = struct.unpack_from('<I', data, sec + 20)[0]
    chars = struct.unpack_from('<I', data, sec + 36)[0]
    print(f'  {i}: "{name}" VA=0x{vaddr:X} VSize=0x{vsize:X} Raw=0x{rawoff:X}+0x{rawsize:X} Chars=0x{chars:X}')

# Find .data section and extract GUIDs
for i in range(num_sections):
    sec = pe_off + 24 + opt_hdr_size + i * 40
    name = data[sec:sec+8].rstrip(b'\x00').decode('ascii', errors='replace')
    if name == '.data':
        vaddr = struct.unpack_from('<I', data, sec + 12)[0]
        rawoff = struct.unpack_from('<I', data, sec + 20)[0]
        rawsize = struct.unpack_from('<I', data, sec + 16)[0]
        print(f'\n.data: VA=0x{vaddr:X}, raw=0x{rawoff:X}, size=0x{rawsize:X}')
        ddata = data[rawoff:rawoff+rawsize]
        for g in range(0, len(ddata) - 16, 4):
            d1 = struct.unpack_from('<I', ddata, g)[0]
            d2 = struct.unpack_from('<H', ddata, g+4)[0]
            d3 = struct.unpack_from('<H', ddata, g+6)[0]
            if (d3 >> 12) == 4 and (ddata[g+8] & 0xC0) == 0x80:
                d4 = ddata[g+8:g+10]
                d5 = ddata[g+10:g+16]
                guid_str = f'{d1:08X}-{d2:04X}-{d3:04X}-{d4.hex().upper()}-{d5.hex().upper()}'
                print(f'  .data+0x{g:03X} (VA 0x{vaddr+g:X}): {guid_str}')
        break
