import struct

# Final verification: the table structure and exact byte patterns
with open(r'D:\Section_PE32_image_H2OFormBrowserDxe_H2OFormBrowserDxe.sct', 'rb') as f:
    data = f.read()

# The table is a series of [16-byte GUID][4-byte flag] pairs
# Let's parse it cleanly starting from the known Advanced GUID position
print("=== CONFIRMED TABLE STRUCTURE (H2OFormBrowserDxe.sct) ===")
print("Offset  Flag     GUID (hex)                              Name")
print("-" * 80)

# Parse from 0x323E0 onwards (before the first known GUID)
# We know: 1AB0E0C1 at 0x324B8, Advanced at 0x324CC, Power at 0x324F4
# Spacing: 0x324CC - 0x324B8 = 20 bytes (16 GUID + 4 flag) ✓
#          0x324F4 - 0x324E0 = 20 bytes (16 GUID + 4 flag) ✓

known = {
    0x324B8: "1AB0E0C1",
    0x324CC: "Advanced (C6D4769E)",
    0x324F4: "Power/Thermal (732871A6)",
}

# Scan for valid GUID+flag pairs starting from the area before the first known GUID
pos = 0x323F0
entries = []
while pos < 0x32560:
    guid = data[pos:pos+16]
    flag = struct.unpack_from('<I', data, pos+16)[0]
    if flag in (0, 1):
        name = known.get(pos, "")
        entries.append((pos, flag, guid.hex(), name))
        pos += 20
    else:
        pos += 1

for off, flag, ghex, name in entries:
    state = "SHOWN" if flag == 1 else "HIDDEN"
    marker = f"  <-- {name}" if name else ""
    print(f"0x{off:05X}  {flag:08X}  {ghex}  {state}{marker}")

print(f"\nTotal entries in this range: {len(entries)}")
print(f"HIDDEN: {sum(1 for _,f,_,_ in entries if f==0)}")
print(f"SHOWN:  {sum(1 for _,f,_,_ in entries if f==1)}")

# The SREP-loaded image has 4 fewer bytes at the start (35FE0 vs 35FE4)
# So offsets in loaded image = offsets in .sct - 4
print(f"\n=== OFFSET MAPPING (loaded image vs .sct) ===")
print(f".sct size: 0x{len(data):X} ({len(data)})")
print(f"Loaded image: 0x35FE0 (221152)")
print(f"Delta: {len(data) - 0x35FE0} bytes (loaded image = .sct minus first {len(data) - 0x35FE0} bytes)")
print()
print(f"If loaded image strips first {len(data) - 0x35FE0} bytes from .sct:")
for off, flag, ghex, name in entries:
    loaded_off = off - (len(data) - 0x35FE0)
    state = "SHOWN" if flag == 1 else "HIDDEN"
    print(f"  .sct 0x{off:05X} -> loaded 0x{loaded_off:05X}  {state}  {name or ghex[:16]}")

# Check the SREP log context bytes around 0x324B4
# The log showed "Found at 324B4" which is .sct offset 0x324B8 - 4 = 0x324B4
print(f"\n=== SREP LOG vs BINARY CORRELATION ===")
# In loaded image: 0x324B4 = 1AB0E0C1 GUID (at .sct 0x324B8)
# SREP searched loaded image for pattern: GUID(16) + 00000000(4) = 20 bytes
# At loaded 0x324B4: the 1AB0E0C1 GUID
# But SREP showed "Found at 324B4" after the secondary search, not the primary search
# Primary search: all 6 against loaded image -> No Patter Found
# Secondary: found 1AB0E0C1 at 324B4 -> Patched

# This means the primary search used a DIFFERENT byte order or format
# while the secondary search used the correct format
print("Primary search (Patching Image Size 35FE0): ALL 6 No Patter Found")
print("Secondary search: 1AB0E0C1 Found at 324B4 -> Patched")
print("Gap: 4 bytes (loaded image starts 4 bytes into .sct)")
print()
print("CONCLUSION: The primary search failed because SREP searched")
print("for patterns in a format that doesn't match the binary layout.")
print("The secondary search found the correct offset and patched.")
print()
print("For bcfg driver approach: SREP would need to find patterns in")
print("the DXE pool copy of H2OFormBrowserDxe, which may have yet")
print("another offset. The patterns 59B963B8, E33545B0, 49D592C3")
print("are NOT in this binary at all - they were restructured by Lenovo.")
