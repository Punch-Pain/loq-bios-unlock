import struct

# Check SREP loader PE32 subsystem
with open(r'D:\EFI\Boot\BOOTX64_SREP.efi', 'rb') as f:
    data = f.read()

mz = struct.unpack_from('<H', data, 0)[0]
pe_off = struct.unpack_from('<I', data, 0x3C)[0]
machine = struct.unpack_from('<H', data, pe_off + 4)[0]
subsystem = struct.unpack_from('<H', data, pe_off + 24 + 68)[0]
num_sections = struct.unpack_from('<H', data, pe_off + 6)[0]
opt_hdr_size = struct.unpack_from('<H', data, pe_off + 20)[0]
entry_rva = struct.unpack_from('<I', data, pe_off + 24 + 16)[0]
image_size = struct.unpack_from('<I', data, pe_off + 24 + 56)[0]

subsys_name = {1: "Native", 2: "Windows GUI", 3: "Windows CUI", 10: "EFI Application", 11: "EFI Boot Service Driver", 12: "EFI Runtime Driver", 13: "EFI ROM"}

print(f"SREP Loader (BOOTX64_SREP.efi):")
print(f"  Size: {len(data)} bytes")
print(f"  Machine: 0x{machine:X} ({'x86_64' if machine==0x8664 else 'x86' if machine==0x14c else 'unknown'})")
print(f"  Subsystem: {subsystem} ({subsys_name.get(subsystem, 'UNKNOWN')})")
print(f"  Entry RVA: 0x{entry_rva:X}")
print(f"  Image Size: 0x{image_size:X}")
print(f"  Sections: {num_sections}")

# Also check sections
sec_off = pe_off + 24 + opt_hdr_size
for i in range(num_sections):
    sec = sec_off + i * 40
    name = data[sec:sec+8].rstrip(b'\x00').decode('ascii', errors='replace')
    vsize = struct.unpack_from('<I', data, sec + 8)[0]
    vaddr = struct.unpack_from('<I', data, sec + 12)[0]
    rawsize = struct.unpack_from('<I', data, sec + 16)[0]
    rawoff = struct.unpack_from('<I', data, sec + 20)[0]
    print(f"  Section {i}: \"{name}\" VA=0x{vaddr:X} Raw=0x{rawoff:X}+0x{rawsize:X}")

# Search for ASCII strings in SREP
print(f"\nSearching for ASCII strings in SREP:")
for term in [b"Loaded", b"Patching", b"No Patter", b"Found at", b"Op ", b"Pattern", b"LoadFromFV", b"LoadFromFS", b"Exec", b"Loaded Image", b"driver", b"bcfg"]:
    idx = data.find(term)
    if idx >= 0:
        # get surrounding string
        start = max(0, idx - 20)
        end = min(len(data), idx + 40)
        ctx = data[start:end]
        # find printable range
        printable = b''
        for b in ctx:
            if 32 <= b < 127:
                printable += bytes([b])
            else:
                if len(printable) >= 4:
                    break
                printable = b''
        print(f"  \"{term.decode()}\" at 0x{idx:X}")

# Now search for the 3 missing GUIDs in SetupUtility DXE
def guid_to_le(gs):
    gs = gs.replace('-','')
    a = gs[0:8]; b = gs[8:12]; c = gs[12:16]; de = gs[16:32]
    le = a[6:8]+a[4:6]+a[2:4]+a[0:2] + b[2:4]+b[0:2] + c[2:4]+c[0:2] + de
    return bytes.fromhex(le)

missing_guids = [
    "DBA6A7E3-BB57-4BE7-8AF8-D578DB7E5687",
    "A6E38A2F-EA46-484E-ADC8-CE0187E4CCE2",
    "41939F65-0F74-457E-9D28-C64F957B4D28",
]

with open(r'D:\tools\SetupUtility_pe32.efi', 'rb') as f:
    drv = f.read()

print(f"\n--- 3 Missing GUIDs (stub-only, not in SetupUtility DXE) ---")
for gs in missing_guids:
    gb = guid_to_le(gs)
    idx = drv.find(gb)
    if idx >= 0:
        print(f"  FOUND in SetupUtility DXE at 0x{idx:X}: {gs}")
    else:
        # Also search in H2OFormBrowserDxe
        with open(r'D:\Section_PE32_image_H2OFormBrowserDxe_H2OFormBrowserDxe.sct', 'rb') as f:
            h2o = f.read()
        idx2 = h2o.find(gb)
        if idx2 >= 0:
            print(f"  FOUND in H2OFormBrowserDxe at 0x{idx2:X}: {gs}")
        else:
            print(f"  NOT FOUND in either module: {gs}")

# Also look up the first GUID in common databases
print(f"\n--- GUID lookup ---")
# DBA6A7E3-BB57-4BE7-8AF8-D578DB7E5687 - search web for identification
# A6E38A2F-EA46-484E-ADC8-CE0187E4CCE2
# 41939F65-0F74-457E-9D28-C64F957B4D28
# These appear in .data+0x000, .data+0x1B0, .data+0x20C of SetupUtilityApp
