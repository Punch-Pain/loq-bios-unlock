import struct, os, subprocess

with open(r'D:\File_DXE_driver_SetupUtility_SetupUtility.ffs', 'rb') as f:
    data = f.read()

# The ifrextractor list found form packages at these offsets in the FFS file
# But the extraction failed - the offsets might be WRONG because the section is compressed
# Let me try to find the REAL form packages by scanning the raw FFS data

# The string packages are NOT compressed (they have valid offsets and data)
# Let me verify the en-US string package
str_off = 0x5BD64
str_len = 0x7D3AD
str_data = data[str_off:str_off+str_len]
print(f'String package en-US at 0x{str_off:X}: {len(str_data)} bytes')
print(f'First 32: {str_data[:32].hex()}')

# HII_STRING_PACKAGE header: Length(4) + Type(2) + HeaderSize(2) + ...
str_type = struct.unpack('<H', str_data[4:6])[0]
print(f'String package type: 0x{str_type:04X} (should be 0x0002 for HII_STRING_PACKAGE)')

# Now let me try a different approach: 
# The SetupUtility module has a GUID_DEFINED section (type 0x19) at offset 0xD0
# Let me parse that - it might contain the actual data
guid_sec_off = 0xD0
guid_sec_size = struct.unpack('<I', data[guid_sec_off:guid_sec_off+3] + b'\x00')[0]
guid_sec_type = data[guid_sec_off+3]
print(f'\nGUID_DEFINED section at 0x{guid_sec_off:X}: size=0x{guid_sec_size:X}, type=0x{guid_sec_type:02X}')

# GUID-defined section body: DefinitionOffset(4) + Guid(16) + DataOffset(4) + Attributes(4) + ...
body = data[guid_sec_off+4:guid_sec_off+guid_sec_size]
def_offset = struct.unpack('<I', body[0:4])[0]
guid = body[4:20]
data_offset = struct.unpack('<I', body[20:24])[0]
attrs = struct.unpack('<I', body[24:28])[0]
print(f'Definition offset: 0x{def_offset:X}')
print(f'GUID: {guid.hex()}')
print(f'Data offset: 0x{data_offset:X}')
print(f'Attributes: 0x{attrs:08X}')

# Maybe this GUID-defined section wraps the compressed PE32 section
# Try to extract the PE32 from the entire FFS by looking for MZ patterns
# The PE32 should be somewhere in the FFS file

# Actually, let me look at this from a different angle
# The SetupUtility FFS file has sections:
# 0x18: VERSION (0xB8 bytes) 
# 0xD0: GUID_DEFINED (0x10C bytes) 
# 0x1DC: ??? (0x154044 bytes) - This is the bulk of the file
# After this: more sections

# What if 0x1DC isn't a compressed section but a data section?
# Let me look at the section header more carefully
print(f'\nSection at 0x1DC:')
sec_body = data[0x1DC+4:0x1DC+0x154044]
# Skip zero padding
nz_off = 0
for i in range(min(1024, len(sec_body))):
    if sec_body[i] != 0:
        nz_off = i
        break
print(f'First non-zero byte at offset 0x{nz_off:X} within section body')
print(f'Bytes at first non-zero: {sec_body[nz_off:nz_off+32].hex()}')

# Check if maybe this is LZMA2 or Tiano data with a header
# Tiano compressed data usually starts with specific patterns
# Let me check for EFI_TIANO_COMPRESSED header
if sec_body[nz_off:nz_off+4] == b'\x00\x00\x00\x00':
    # Might be a sub-header
    for skip in range(nz_off, min(nz_off+256, len(sec_body))):
        if sec_body[skip] != 0:
            print(f'Non-zero at skip={skip}: {sec_body[skip:skip+16].hex()}')
            break
