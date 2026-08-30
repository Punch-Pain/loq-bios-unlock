import struct

# The SREP patterns are NOT standard LE GUIDs. They use a specific byte order.
# Let's search using the EXACT hex strings from the SREP config.

patterns = {
    "59B963B8C60E334099C18FD89F040222": "59B963B8",
    "E33545B0043046499EB7149428983053": "E33545B0",
    "732871A65F92C64690B4A40F86A0917B": "Power/Thermal",
    "9E76D4C6487F2A4D98E987ADCCF35CCC": "Advanced",
    "49D592C3EB27464F8A119F5DF55A9C8B": "49D592C3",
    "1AB0E0C17E60754BB8BB0631ECFAACF2": "1AB0E0C1",
}

with open(r'D:\Section_PE32_image_H2OFormBrowserDxe_H2OFormBrowserDxe.sct', 'rb') as f:
    data = f.read()

print(f"File: H2OFormBrowserDxe.sct ({len(data)} bytes)")
print(f"Searching for GUID + 00000000 (hidden) patterns...\n")

for hex_guid, name in patterns.items():
    hidden_pattern = bytes.fromhex(hex_guid + "00000000")
    shown_pattern = bytes.fromhex(hex_guid + "01000000")
    
    h_off = data.find(hidden_pattern)
    s_off = data.find(shown_pattern)
    
    if h_off >= 0:
        print(f"  {name:20s} HIDDEN  at 0x{h_off:05X} — CAN be patched to shown")
    elif s_off >= 0:
        print(f"  {name:20s} SHOWN   at 0x{s_off:05X} — already unhidden in static binary")
    else:
        # Check if the GUID alone exists (without flag bytes following)
        guid_only = bytes.fromhex(hex_guid)
        g_off = data.find(guid_only)
        if g_off >= 0:
            trailing = data[g_off+16:g_off+20]
            print(f"  {name:20s} GUID at 0x{g_off:05X} — trailing: {trailing.hex(' ')} (unexpected flag)")
        else:
            print(f"  {name:20s} NOT FOUND at all in binary")

print()
print("=" * 70)
print("SECOND: Search ALL form-set GUIDs from IFR data (14 form packages)")
print("using the IFR file to extract every GUID, then search the binary")
print("=" * 70)

# Extract ALL GUIDs from the IFR text file
import re
ifr_path = r'D:\tools\SetupUtility_pe32.efi.6.0.en-US.uefi.ifr.txt'
with open(ifr_path, 'r', errors='replace') as f:
    ifr_text = f.read()

# Find all FormSet GUIDs (they appear in "FormId" and "FormSet" lines)
guid_re = re.compile(r'([0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})')
all_guids = set(guid_re.findall(ifr_text))

# Also extract from "FormSet GUID:" lines
formset_re = re.compile(r'FormSet\s+GUID:\s*([0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})', re.IGNORECASE)
formset_guids = formset_re.findall(ifr_text)

print(f"Total unique GUIDs in IFR: {len(all_guids)}")
print(f"FormSet GUIDs explicitly: {len(formset_guids)}")
for fg in formset_guids:
    print(f"  FormSet: {fg}")

# Convert GUID string to the byte order used in the SREP config / H2OFormBrowserDxe
def ifr_guid_to_bytes(gs):
    """Convert standard GUID string to the byte order found in H2OFormBrowserDxe binary"""
    gs = gs.replace('-','')
    # Standard GUID wire format: D1(LE) D2(LE) D3(LE) D4(BE) D5(BE)
    # But H2OFormBrowserDxe stores: D1(LE) D2(LE) D3(LE) D4(BE) D5(BE)
    # Which is exactly what make_cfg.ps1 produces
    a = gs[0:8]; b = gs[8:12]; c = gs[12:16]; de = gs[16:32]
    le = a[6:8]+a[4:6]+a[2:4]+a[0:2] + b[2:4]+b[0:2] + c[2:4]+c[0:2] + de
    return bytes.fromhex(le)

print(f"\nSearching for ALL IFR form-set GUIDs in H2OFormBrowserDxe.sct...")
print("(Searching for GUID + 00000000 = hidden, GUID + 01000000 = shown)")
print()

found_shown = []
found_hidden = []
not_found = []

for gs in all_guids:
    gb = ifr_guid_to_bytes(gs)
    hidden = gb + bytes.fromhex("00000000")
    shown = gb + bytes.fromhex("01000000")
    
    h_off = data.find(hidden)
    s_off = data.find(shown)
    
    if h_off >= 0:
        found_hidden.append((gs, h_off, "HIDDEN"))
    elif s_off >= 0:
        found_shown.append((gs, s_off, "SHOWN"))
    else:
        not_found.append(gs)

print(f"RESULTS: {len(found_hidden)} hidden, {len(found_shown)} shown, {len(not_found)} not found")
print()

if found_hidden:
    print("--- HIDDEN (can be patched to show) ---")
    for gs, off, state in sorted(found_hidden, key=lambda x: x[1]):
        # Check if it matches a known SREP pattern
        known = "SREP" if gs.replace('-','').upper() in [p.upper() for p in patterns] else "extra"
        print(f"  [{known}] {gs} at 0x{off:05X}")

if found_shown:
    print("\n--- ALREADY SHOWN (no patch needed) ---")
    for gs, off, state in sorted(found_shown, key=lambda x: x[1]):
        known = "SREP" if gs.replace('-','').upper() in [p.upper() for p in patterns] else "extra"
        print(f"  [{known}] {gs} at 0x{off:05X}")

if not_found:
    print(f"\n--- NOT FOUND: {len(not_found)} GUIDs (compressed or shifted) ---")
