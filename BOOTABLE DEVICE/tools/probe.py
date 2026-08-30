import sys

rom = open(r"D:\tools\signed_SE.ROM","rb").read()
print("ROM size: 0x%X" % len(rom))

def find_all(needle):
    out=[]
    i=0
    while True:
        j=rom.find(needle, i)
        if j<0: break
        out.append(j); i=j+1
    return out

def hexstr(b): return " ".join("%02X"%x for x in b)

# Advanced form-set GUID, little-endian SREP form, plus isShown flag
adv = bytes.fromhex("9E76D4C6487F2A4D98E987ADCCF35CCC")
cands = {
 "Advanced (9E76D4C6...)": bytes.fromhex("9E76D4C6487F2A4D98E987ADCCF35CCC"),
 "Power    (732871A6...)": bytes.fromhex("732871A65F92C64690B4A40F86A0917B"),
 "1AB0E0C1...":           bytes.fromhex("1AB0E0C17E60754BB8BB0631ECFAACF2"),
}
for name,g in cands.items():
    print("\n=== %s ===" % name)
    occ = find_all(g)
    print("  GUID occurrences: %d" % len(occ))
    for off in occ:
        # show 16 pre + 16 post bytes
        pre = rom[off-16:off] if off>=16 else rom[:off]
        post = rom[off+16:off+16+8]
        print("  off=0x%X  pre[%s]  GUID  post[%s]" % (off, hexstr(pre), hexstr(post)))

# The hide code seen in SREP.log context (test r8,r8; jz)
hide = bytes.fromhex("4D85C074")
print("\n=== hide-code '4D 85 C0 74' (test/jz) occurrences: %d ===" % len(find_all(hide)))

# module names (UTF-16) presence
for nm in ["H2OFormBrowserDxe","SetupUtilityApp","Setup","SetupBrowser","UiApp","SetupUtility"]:
    u = nm.encode("utf-16-le")
    c = find_all(u)
    print("module name %-18s UTF-16 occurrences: %d  first=0x%X" % (nm, len(c), c[0] if c else -1))
