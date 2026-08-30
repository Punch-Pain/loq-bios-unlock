import sys

with open(r'D:\Section_PE32_image_H2OFormBrowserDxe_H2OFormBrowserDxe.sct', 'rb') as f:
    data = f.read()

# Check what's at .sct 0x324B4 (raw)
print('At .sct 0x324B4 (raw):')
print(data[0x324B4:0x324C4].hex(' '))

# Check what's at loaded offset 0x324B4 = .sct 0x324B8
print('At .sct 0x324B8 (= loaded 0x324B4):')
print(data[0x324B8:0x324C8].hex(' '))

# Check: where does 85 C0 74 appear in the file?
pattern = bytes([0x85, 0xC0, 0x74])
idx = 0
matches = []
while True:
    pos = data.find(pattern, idx)
    if pos == -1:
        break
    matches.append(pos)
    idx = pos + 1

print()
print(f'85 C0 74 appears at {len(matches)} locations:')
for m in matches:
    ctx = data[max(0, m-2):m+5]
    print(f'  .sct 0x{m:06X} (= loaded 0x{m-4:06X}): {ctx.hex(" ")}')
