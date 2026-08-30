import sys

with open(r'D:\SREP_Config_diag_F_PatchAndExit.cfg', 'rb') as f1:
    f1_data = f1.read()
with open(r'D:\SREP_Config_20260830_002244.cfg.bak', 'rb') as f2:
    f2_data = f2.read()

print(f'Config F: {len(f1_data)} bytes')
print(f'Original: {len(f2_data)} bytes')
print(f'First 4 bytes F:    {f1_data[:4].hex()}')
print(f'First 4 bytes Orig: {f2_data[:4].hex()}')
print(f'Last 4 bytes F:     {f1_data[-4:].hex()}')
print(f'Last 4 bytes Orig:  {f2_data[-4:].hex()}')

bom = bytes([0xEF, 0xBB, 0xBF])
print(f'F starts with BOM:    {f1_data[:3] == bom}')
print(f'Orig starts with BOM: {f2_data[:3] == bom}')

f1_crlf = f1_data.count(b'\r\n')
f1_lf = f1_data.count(b'\n') - f1_crlf
f2_crlf = f2_data.count(b'\r\n')
f2_lf = f2_data.count(b'\n') - f2_crlf
print(f'F:  {f1_crlf} CRLF, {f1_lf} bare LF')
print(f'Orig: {f2_crlf} CRLF, {f2_lf} bare LF')

newline_bytes = (b'\n', b'\r')
print(f'F ends with newline:    {f1_data[-1:] in newline_bytes}')
print(f'Orig ends with newline: {f2_data[-1:] in newline_bytes}')

if f1_data == f2_data:
    print('\nFILES ARE IDENTICAL (byte-for-byte)')
else:
    print('\nFILES ARE DIFFERENT')
    diffs = []
    for i in range(min(len(f1_data), len(f2_data))):
        if f1_data[i] != f2_data[i]:
            diffs.append(i)
    print(f'Total differing bytes: {len(diffs)} (first 30 shown)')
    for i in diffs[:30]:
        s = max(0, i - 12)
        e1 = min(len(f1_data), i + 12)
        e2 = min(len(f2_data), i + 12)
        print(f'  Byte {i}: F={f1_data[i]:02X} Orig={f2_data[i]:02X}')
        print(f'    F  [{s:04X}]: {f1_data[s:e1].hex(" ")}')
        print(f'    Orig[{s:04X}]: {f2_data[s:e2].hex(" ")}')
    if len(f1_data) != len(f2_data):
        shorter = min(len(f1_data), len(f2_data))
        print(f'\nTail after shorter ends (offset {shorter}):')
        longer = f1_data if len(f1_data) > len(f2_data) else f2_data
        label = 'F' if len(f1_data) > len(f2_data) else 'Orig'
        print(f'  {label}[{shorter}:{shorter+40}]: {longer[shorter:shorter+40].hex(" ")}')
