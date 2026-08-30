import os

with open(r'D:\SREP_Config_20260830_002244.cfg.bak', 'rb') as f:
    data = f.read()

print(f'Original: {len(data)} bytes')
print(f'Original hex tail: {data[-20:].hex(" ")}')
print(f'Original last line repr: {data.splitlines()[-1]!r}')

# Remove only "Op Exec\n" at the end
# File ends with: ...Op End\n\nOp LoadFromFV\nSetupUtilityApp\nOp Exec\n
# We want:        ...Op End\n\nOp LoadFromFV\nSetupUtilityApp\n
# Strategy: find the byte position of the last "Op Exec" and cut it out

exec_marker = b'Op Exec'
last_pos = data.rfind(exec_marker)
print(f'"Op Exec" found at byte offset: {last_pos} (0x{last_pos:04X})')

# Verify what comes after "Op Exec"
after = data[last_pos + len(exec_marker):]
print(f'Bytes after "Op Exec": {after.hex(" ")} ({len(after)} bytes)')

# Config G = everything before "Op Exec" + trim trailing whitespace
config_g = data[:last_pos].rstrip(b'\r\n')
# Ensure trailing newline
config_g = config_g + b'\n'

with open(r'D:\SREP_Config_diag_G_LoadNoExec.cfg', 'wb') as f:
    f.write(config_g)

print(f'\nConfig G: {len(config_g)} bytes')
print(f'Config G hex tail: {config_g[-20:].hex(" ")}')
print(f'Config G last line repr: {config_g.splitlines()[-1]!r}')
print(f'Config G lines: {len(config_g.splitlines())}')

# Verify it matches the original minus "Op Exec\n"
expected = data[:last_pos].rstrip(b'\r\n') + b'\n'
if config_g == expected:
    print('VERIFIED: Config G = Original minus Op Exec')
else:
    print('MISMATCH!')
    for i in range(min(len(config_g), len(expected))):
        if config_g[i] != expected[i]:
            print(f'  First diff at byte {i}: G={config_g[i]:02X} Exp={expected[i]:02X}')
            break
