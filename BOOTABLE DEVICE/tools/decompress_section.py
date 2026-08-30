import struct, lzma, zlib

with open(r'D:\File_DXE_driver_SetupUtility_SetupUtility.ffs', 'rb') as f:
    data = f.read()

# FFS header: 24 bytes
# First section: VERSION at 0x18, size 0xB8
# Second section: GUID_DEFINED at 0xD0, size 0x10C  
# Third section: COMPRESSION at 0x1DC, size 0x154044
sec_start = 0x1DC
sec_size = 0x154044
sec_type = data[sec_start + 3]
print(f'Section at 0x{sec_start:X}: size=0x{sec_size:X}, type=0x{sec_type:02X}')

# Section body starts at sec_start + 4 (3 bytes size + 1 byte type)
body_start = sec_start + 4
# Compression header: UncompressedLength (4 bytes) + CompressionType (1 byte)
uncomp_len = struct.unpack('<I', data[body_start:body_start+4])[0]
comp_type = data[body_start + 4]
print(f'Uncompressed length: {uncomp_len} (0x{uncomp_len:X})')
print(f'Compression type: {comp_type}')

comp_data_start = body_start + 5
comp_data = data[comp_data_start:comp_data_start + sec_size - 9]  # sec_size - 4 header - 5 comp header
print(f'Compressed data: {len(comp_data)} bytes')
print(f'First 32 bytes: {comp_data[:32].hex()}')

# Compression type in UEFI PI spec:
# 0 = EFI_CUSTOMIZED_COMPRESSION (or not compressed in some impls)
# 1 = EFI_STANDARD_COMPRESSION (Tiano)
# 2 = ?

# Try various decompression methods
methods = [
    ('LZMA alone', lambda d: lzma.decompress(d, format=lzma.FORMAT_ALONE)),
    ('LZMA2 raw', lambda d: lzma.decompress(d, format=lzma.FORMAT_RAW, filters=[{'id': lzma.FILTER_LZMA2}])),
    ('Zlib raw -15', lambda d: zlib.decompress(d, -15)),
    ('Zlib default', lambda d: zlib.decompress(d)),
    ('Zlib wbits=15', lambda d: zlib.decompress(d, 15)),
    ('Zlib wbits=9', lambda d: zlib.decompress(d, 9)),
    ('Zlib wbits=31', lambda d: zlib.decompress(d, 31)),
    ('Zlib wbits=47', lambda d: zlib.decompress(d, 47)),
]

# Also try skipping first few bytes
for skip in [0, 1, 2, 4, 8]:
    test_data = comp_data[skip:]
    for name, func in methods:
        try:
            result = func(test_data)
            if len(result) > 100:
                print(f'\nSUCCESS: {name} (skip={skip}): {len(result)} bytes')
                print(f'First 16: {result[:16].hex()}')
                # Check for MZ or PE
                if result[:2] == b'MZ':
                    print('Starts with MZ!')
                # Save it
                out_path = f'D:\\tools\\SetupUtility_decomp.bin'
                with open(out_path, 'wb') as out:
                    out.write(result)
                print(f'Saved to {out_path}')
                # Now try to find form-set GUIDs in decompressed data
                import re
                # Search for known GUIDs
                guids = [
                    ('Advanced', bytes.fromhex('C6D4769E7F484D2A98E987ADCCF35CCC')),
                    ('Power', bytes.fromhex('A6712873925F46C690B4A40F86A0917B')),
                    ('1AB0E0C1', bytes.fromhex('C1E0AB1E607E4B75B8BB0631ECFAACF2')),
                ]
                for gname, gbin in guids:
                    gidx = result.find(gbin)
                    if gidx >= 0:
                        print(f'  {gname} GUID found at offset 0x{gidx:X}')
                break
        except Exception as e:
            pass
    else:
        continue
    break
else:
    print('\nAll decompression methods failed')
    
    # Try Tiano decompression with header parsing
    # Tiano compressed data format:
    # Often starts with specific signature bytes
    # Check for Tiano/EFI signature
    if comp_data[:4] == b'\x00\x00\x00\x00':
        print('Data starts with 4 zero bytes - might need to skip header')
        # Try skipping various amounts of zeros
        for nz in range(1, min(64, len(comp_data))):
            if comp_data[nz] != 0:
                print(f'Non-zero byte at offset {nz}: 0x{comp_data[nz]:02X}')
                break
