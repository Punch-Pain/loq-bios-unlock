import struct

# The image loaded is 35FE0 bytes at 6E706000
# Compare with known module sizes
print("=== Image Size Comparison ===")
print(f"SREP loaded image: 0x35FE0 = {0x35FE0} bytes")

# H2OFormBrowserDxe PE32 section
with open(r'D:\Section_PE32_image_H2OFormBrowserDxe_H2OFormBrowserDxe.sct', 'rb') as f:
    h2o = f.read()
print(f"H2OFormBrowserDxe.sct: 0x{len(h2o):X} = {len(h2o)} bytes")

# H2OFormBrowserDxe FFS
with open(r'D:\File_DXE_driver_H2OFormBrowserDxe_H2OFormBrowserDxe.ffs', 'rb') as f:
    h2o_ffs = f.read()
print(f"H2OFormBrowserDxe.ffs: 0x{len(h2o_ffs):X} = {len(h2o_ffs)} bytes")

# Search for 1AB0E0C1 pattern in H2OFormBrowserDxe binary
def guid_to_le(gs):
    gs = gs.replace('-','')
    a = gs[0:8]; b = gs[8:12]; c = gs[12:16]; de = gs[16:32]
    le = a[6:8]+a[4:6]+a[2:4]+a[0:2] + b[2:4]+b[0:2] + c[2:4]+c[0:2] + de
    return bytes.fromhex(le)

# Pattern: 16-byte GUID + 4 bytes (00000000 = hidden)
targets = {
    "1AB0E0C1-7E60-754B-B8BB-0631ECFAACF2": "1AB0E0C1",
    "9E76D4C6-487F-2A4D-98E9-87ADCCF35CCC": "Advanced",
    "732871A6-5F92-C646-90B4-A40F86A0917B": "Power",
    "59B963B8-C60E-3340-99C1-8FD89F040222": "59B963B8",
    "E33545B0-0430-4649-9EB7-149428983053": "E33545B0",
    "49D592C3-EB27-464F-8A11-9F5DF55A9C8B": "49D592C3",
}

print(f"\n=== Searching all 6 patterns in H2OFormBrowserDxe.sct ===")
for gs, name in targets.items():
    gb = guid_to_le(gs)
    hidden = gb + b'\x00\x00\x00\x00'
    shown = gb + b'\x01\x00\x00\x00'
    
    h_off = h2o.find(hidden)
    s_off = h2o.find(shown)
    
    if h_off >= 0:
        print(f"  {name}: HIDDEN at 0x{h_off:X} (pattern matches!)")
    elif s_off >= 0:
        print(f"  {name}: SHOWN at 0x{s_off:X} (already unhidden)")
    else:
        # Try just the 16-byte GUID
        g_off = h2o.find(gb)
        if g_off >= 0:
            # Check what follows
            trailing = h2o[g_off+16:g_off+20]
            print(f"  {name}: GUID found at 0x{g_off:X}, trailing bytes: {trailing.hex(' ')}")
        else:
            print(f"  {name}: NOT FOUND in binary at all")

# Now search in H2OFormBrowserDxe FFS (full FFS with section headers)
print(f"\n=== Searching in H2OFormBrowserDxe FFS ===")
for gs, name in targets.items():
    gb = guid_to_le(gs)
    hidden = gb + b'\x00\x00\x00\x00'
    idx = h2o_ffs.find(hidden)
    if idx >= 0:
        print(f"  {name}: HIDDEN at 0x{idx:X} in FFS!")
    else:
        g_off = h2o_ffs.find(gb)
        if g_off >= 0:
            trailing = h2o_ffs[g_off+16:g_off+20]
            print(f"  {name}: GUID at 0x{g_off:X}, trailing: {trailing.hex(' ')}")
        else:
            print(f"  {name}: NOT FOUND in FFS")

# Now the key question: search the FULL signed_SE.ROM for these patterns
print(f"\n=== Searching in signed_SE.ROM (compressed modules) ===")
with open(r'D:\tools\signed_SE.ROM', 'rb') as f:
    # Only read first 4MB for speed
    rom_head = f.read(4*1024*1024)
print(f"Read first {len(rom_head)} bytes of ROM")

for gs, name in targets.items():
    gb = guid_to_le(gs)
    hidden = gb + b'\x00\x00\x00\x00'
    idx = rom_head.find(hidden)
    if idx >= 0:
        print(f"  {name}: HIDDEN at ROM offset 0x{idx:X}")
    else:
        g_off = rom_head.find(gb)
        if g_off >= 0:
            trailing = rom_head[g_off+16:g_off+20]
            print(f"  {name}: GUID at ROM 0x{g_off:X}, trailing: {trailing.hex(' ')}")
        else:
            print(f"  {name}: NOT FOUND in ROM head")

# The critical finding: 1AB0E0C1 was found at 324B4 in the LOADED image
# But the loaded image is 35FE0 bytes - same as H2OFormBrowserDxe.sct (357FC)
# Let's check what's at offset 324B4 in H2OFormBrowserDxe.sct
print(f"\n=== What's at offset 0x324B4 in H2OFormBrowserDxe.sct? ===")
if 0x324B4 < len(h2o):
    ctx = h2o[0x324B4:0x324B4+32]
    print(f"  Bytes: {ctx.hex(' ')}")
    # Check if any GUID+flag pattern is here
    for gs, name in targets.items():
        gb = guid_to_le(gs)
        for delta in range(-16, 17):
            check_off = 0x324B4 + delta
            if 0 <= check_off and check_off + 20 <= len(h2o):
                if h2o[check_off:check_off+16] == gb:
                    flag = h2o[check_off+16:check_off+20]
                    print(f"  ** {name} GUID found at 0x{check_off:X}! Flag: {flag.hex(' ')}")

# Check the ACTUAL offset from the first boot log (m0028) where Advanced was found at 324C8
print(f"\n=== What's at offset 0x324C8 in H2OFormBrowserDxe.sct? (first boot found Advanced here) ===")
if 0x324C8 < len(h2o):
    ctx = h2o[0x324C8:0x324C8+32]
    print(f"  Bytes: {ctx.hex(' ')}")
    adv_gb = guid_to_le("9E76D4C6-487F-2A4D-98E9-87ADCCF35CCC")
    if h2o[0x324C8:0x324C8+16] == adv_gb:
        flag = h2o[0x324C8+16:0x324C8+20]
        print(f"  ** Advanced GUID IS here! Flag: {flag.hex(' ')}")
    else:
        print(f"  NOT the Advanced GUID at this offset")
        # Check nearby
        for delta in range(-32, 33):
            check_off = 0x324C8 + delta
            if 0 <= check_off and check_off + 16 <= len(h2o):
                if h2o[check_off:check_off+16] == adv_gb:
                    flag = h2o[check_off+16:check_off+20]
                    print(f"  ** Advanced GUID found nearby at 0x{check_off:X}! Flag: {flag.hex(' ')}")
