import struct, sys

# Read SetupUtilityApp_pe32.efi .data GUIDs
with open(r'D:\SetupUtilityApp_pe32.efi', 'rb') as f:
    app_data = f.read()

pe_off = struct.unpack_from('<I', app_data, 0x3C)[0]
num_sections = struct.unpack_from('<H', app_data, pe_off + 6)[0]
opt_hdr_size = struct.unpack_from('<H', app_data, pe_off + 20)[0]

app_guids = []
for i in range(num_sections):
    sec = pe_off + 24 + opt_hdr_size + i * 40
    name = app_data[sec:sec+8].rstrip(b'\x00').decode('ascii', errors='replace')
    if name == '.data':
        vaddr = struct.unpack_from('<I', app_data, sec + 12)[0]
        rawoff = struct.unpack_from('<I', app_data, sec + 20)[0]
        rawsize = struct.unpack_from('<I', app_data, sec + 16)[0]
        ddata = app_data[rawoff:rawoff+rawsize]
        for g in range(0, len(ddata) - 16, 4):
            d1 = struct.unpack_from('<I', ddata, g)[0]
            d2 = struct.unpack_from('<H', ddata, g+4)[0]
            d3 = struct.unpack_from('<H', ddata, g+6)[0]
            if (d3 >> 12) == 4 and (ddata[g+8] & 0xC0) == 0x80:
                guid_bytes = ddata[g:g+16]
                d4 = ddata[g+8:g+10]
                d5 = ddata[g+10:g+16]
                guid_str = f'{d1:08X}-{d2:04X}-{d3:04X}-{d4.hex().upper()}-{d5.hex().upper()}'
                app_guids.append((g, vaddr+g, guid_str, guid_bytes))
        break

print(f"SetupUtilityApp .data GUIDs: {len(app_guids)}")
for off, va, gs, gb in app_guids:
    print(f"  .data+0x{off:03X} (VA 0x{va:X}): {gs}")

# Read SetupUtility_pe32.efi (the 1.39MB DXE driver)
with open(r'D:\tools\SetupUtility_pe32.efi', 'rb') as f:
    drv_data = f.read()

print(f"\nSetupUtility_pe32.efi size: {len(drv_data)} bytes")

# For each app GUID, search in the driver
print("\n--- Searching app GUIDs in SetupUtility_pe32.efi ---")
for off, va, gs, gb in app_guids:
    # Search for the GUID bytes (LE order)
    idx = drv_data.find(gb)
    if idx >= 0:
        print(f"  FOUND {gs} at 0x{idx:X} in SetupUtility")
    else:
        # Try with known GUID names
        print(f"  NOT FOUND: {gs} (app .data+0x{off:03X})")

# Also search for known protocol GUIDs that the stub might use
# Common Insyde protocols
known_protocols = [
    "0F0B1735-87A0-4193-B266-538C38AF48CE",  # HII Class
    "FE3542FE-C1D3-4EF8-657C-8048606FF670",  # SetupUtility DXE
    "5B1B31A1-9562-11D2-8E3F-00A0C969723B",  # EFI_SIMPLE_TEXT_INPUT
    "A04A27F4-DF00-4D42-B552-39511302113D",  # SystemConfig/AdvanceConfig
    "C6D4769E-7F48-4D2A-98E9-87ADCCF35CCC",  # Advanced FormSet
    "EC87D643-EBA4-4BB5-A1E5-3F3E36B20DA9",  # Setup variable GUID
]

# Convert GUIDs to LE bytes for searching
def guid_to_le(gs):
    gs = gs.replace('-','')
    a = gs[0:8]; b = gs[8:12]; c = gs[12:16]; de = gs[16:32]
    le = a[6:8]+a[4:6]+a[2:4]+a[0:2] + b[2:4]+b[0:2] + c[2:4]+c[0:2] + de
    return bytes.fromhex(le)

print("\n--- Searching known protocol GUIDs in SetupUtility_pe32.efi ---")
for gs in known_protocols:
    gb = guid_to_le(gs)
    positions = []
    idx = 0
    while True:
        idx = drv_data.find(gb, idx)
        if idx == -1: break
        positions.append(idx)
        idx += 1
    if positions:
        pos_str = ", ".join(f"0x{p:X}" for p in positions[:5])
        extra = f" (+{len(positions)-5} more)" if len(positions) > 5 else ""
        print(f"  {gs}: {len(positions)} matches: {pos_str}{extra}")
    else:
        print(f"  {gs}: NOT FOUND")
