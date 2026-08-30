import struct

# The 3 MISSING SREP patterns: 59B963B8, E33545B0, 49D592C3
# These are NOT in H2OFormBrowserDxe.sct. Check if they're anywhere in the ROM.
# Also search the FULL ROM for ALL 6 patterns to understand the full picture.

missing_patterns = {
    "59B963B8C60E334099C18FD89F040222": "59B963B8",
    "E33545B0043046499EB7149428983053": "E33545B0",
    "49D592C3EB27464F8A119F5DF55A9C8B": "49D592C3",
}

all_patterns = {
    "59B963B8C60E334099C18FD89F040222": "59B963B8",
    "E33545B0043046499EB7149428983053": "E33545B0",
    "732871A65F92C64690B4A40F86A0917B": "Power/Thermal",
    "9E76D4C6487F2A4D98E987ADCCF35CCC": "Advanced",
    "49D592C3EB27464F8A119F5DF55A9C8B": "49D592C3",
    "1AB0E0C17E60754BB8BB0631ECFAACF2": "1AB0E0C1",
}

# Search the FULL ROM
print("=== Searching FULL signed_SE.ROM for all 6 SREP patterns ===")
with open(r'D:\tools\signed_SE.ROM', 'rb') as f:
    rom = f.read()
print(f"ROM size: {len(rom)} bytes ({len(rom)/1024/1024:.1f} MB)")

for hex_guid, name in all_patterns.items():
    hidden = bytes.fromhex(hex_guid + "00000000")
    shown = bytes.fromhex(hex_guid + "01000000")
    
    # Search for hidden
    positions = []
    idx = 0
    while True:
        idx = rom.find(hidden, idx)
        if idx == -1: break
        positions.append(idx)
        idx += 1
    
    # Search for shown
    shown_positions = []
    idx = 0
    while True:
        idx = rom.find(shown, idx)
        if idx == -1: break
        shown_positions.append(idx)
        idx += 1
    
    # Search for GUID alone (without flag)
    guid_only = bytes.fromhex(hex_guid)
    guid_positions = []
    idx = 0
    while True:
        idx = rom.find(guid_only, idx)
        if idx == -1: break
        guid_positions.append(idx)
        idx += 1
    
    if positions:
        print(f"  {name:20s}: {len(positions)} HIDDEN matches: {', '.join(f'0x{p:X}' for p in positions[:5])}")
    elif shown_positions:
        print(f"  {name:20s}: {len(shown_positions)} SHOWN matches (already unhidden): {', '.join(f'0x{p:X}' for p in shown_positions[:5])}")
    elif guid_positions:
        # Check trailing bytes
        for gp in guid_positions[:3]:
            trailing = rom[gp+16:gp+20]
            print(f"  {name:20s}: GUID at 0x{gp:X}, trailing: {trailing.hex(' ')}")
    else:
        print(f"  {name:20s}: NOT FOUND in entire ROM")

print()
print("=== Context around each H2OFormBrowserDxe pattern ===")
# Show the structure around each found pattern
h2o_patterns = {
    "1AB0E0C17E60754BB8BB0631ECFAACF2": ("1AB0E0C1", 0x324B8),
    "9E76D4C6487F2A4D98E987ADCCF35CCC": ("Advanced", 0x324CC),
    "732871A65F92C64690B4A40F86A0917B": ("Power/Thermal", 0x324F4),
}

with open(r'D:\Section_PE32_image_H2OFormBrowserDxe_H2OFormBrowserDxe.sct', 'rb') as f:
    h2o = f.read()

for hex_guid, (name, offset) in h2o_patterns.items():
    # Show 48 bytes starting 4 bytes before the GUID
    start = offset - 4
    ctx = h2o[start:start+64]
    print(f"\n  {name} at 0x{offset:05X}:")
    print(f"    Full context: {ctx.hex(' ')}")
    # Parse the structure
    prev_flag = struct.unpack_from('<I', h2o, offset-4)[0]
    guid_bytes = h2o[offset:offset+16]
    my_flag = struct.unpack_from('<I', h2o, offset+16)[0]
    next_guid = h2o[offset+20:offset+36]
    next_flag = struct.unpack_from('<I', h2o, offset+36)[0]
    print(f"    Prev flag: {prev_flag:08X} | This GUID: {guid_bytes.hex()} | This flag: {my_flag:08X} | Next GUID: {next_guid.hex()} | Next flag: {next_flag:08X}")

# Dump the FULL table structure: scan from 0x31900 to 0x32600
print("\n=== FULL GUID+FLAG TABLE SCAN (0x31900 to 0x32600) ===")
print("Looking for the isShown flag table structure...")
print()

# Look for the Advanced GUID (9E76D4C6) and dump the surrounding table
adv_guid = bytes.fromhex("9E76D4C6487F2A4D98E987ADCCF35CCC")
adv_pos = h2o.find(adv_guid)
if adv_pos >= 0:
    # The table should be a series of [16-byte GUID][4-byte flag] pairs
    # Scan backwards to find the start of the table
    # Look for a pattern that starts with a recognizable marker
    
    # Actually, let's look for the 4-byte marker that precedes the table
    # The first GUID at 0x3193C is 38237648-09CC-47C4-8B5F-B09F06890DF7
    # Let's scan from 0x31900 to find all GUID+flag pairs
    
    print(f"{'Offset':8s} {'Flag':10s} {'GUID':40s} {'State':8s} {'Next+8'}")
    print("-" * 80)
    
    # Scan for valid GUID+flag pairs
    pos = 0x31900
    while pos < 0x32600:
        # Check if there's a valid GUID here (4 bytes could be flag for previous)
        for trial in range(4):
            check_pos = pos + trial
            if check_pos + 20 > len(h2o):
                break
            potential_guid = h2o[check_pos:check_pos+16]
            potential_flag = struct.unpack_from('<I', h2o, check_pos+16)[0]
            
            # Check if this could be a GUID (look for known patterns)
            if potential_flag in (0, 1):
                # Check if the next 20 bytes also look like GUID+flag
                next_pos = check_pos + 20
                if next_pos + 20 <= len(h2o):
                    next_flag = struct.unpack_from('<I', h2o, next_pos+16)[0]
                    if next_flag in (0, 1):
                        # This looks like a GUID+flag pair
                        marker = " "
                        if potential_guid == adv_guid:
                            marker = "<-- ADVANCED"
                        elif potential_guid == bytes.fromhex("1AB0E0C17E60754BB8BB0631ECFAACF2"):
                            marker = "<-- 1AB0E0C1"
                        elif potential_guid == bytes.fromhex("732871A65F92C64690B4A40F86A0917B"):
                            marker = "<-- POWER"
                        
                        state = "SHOWN" if potential_flag == 1 else "HIDDEN"
                        print(f"0x{check_pos:05X}  {potential_flag:08X}   {potential_guid.hex()}  {state:8s} {marker}")
                        pos = check_pos + 20
                        break
        else:
            pos += 1
