<# extract_new_pattern.ps1
   Search H2OFormBrowserDxe PE32 section for form-set GUIDs + isShown flags.
   Outputs exact 20-byte SREP patterns (16-byte GUID + 4-byte flag) for each match.

   Usage:
     .\extract_new_pattern.ps1
     .\extract_new_pattern.ps1 -Bin "D:\Section_PE32_image_H2OFormBrowserDxe_H2OFormBrowserDxe.sct"
#>
param(
  [string]$Bin = "D:\Section_PE32_image_H2OFormBrowserDxe_H2OFormBrowserDxe.sct"
)

if (-not (Test-Path $Bin)) {
  Write-Host "ERROR: File not found: $Bin"
  exit 1
}

$data = [System.IO.File]::ReadAllBytes($Bin)
Write-Host "Loaded $Bin ($($data.Length) bytes)"
Write-Host ""

# --- Known GUIDs from SREP config (little-endian byte order for searching) ---
$knownGuids = @{
  "9E76D4C6-487F-2A4D-98E9-87ADCCF35CCC" = "Advanced"
  "732871A6-5F92-C646-90B4-A40F86A0917B" = "Power/Thermal"
  "1AB0E0C1-7E60-754B-B8BB-0631ECFAACF2" = "FormSet 1AB0E0C1"
  "59B963B8-C60E-3340-99C1-8FD89F040222" = "FormSet 59B963B8"
  "E33545B0-0430-4649-9EB7-149428983053" = "FormSet E33545B0"
  "49D592C3-EB27-464F-8A11-9F5DF55A9C8B" = "FormSet 49D592C3"
}

function Convert-GuidToLeBytes($g) {
  $g = $g.Replace('{','').Replace('}','').Replace('-','')
  $A = $g.Substring(0,8); $B = $g.Substring(8,4); $C = $g.Substring(12,4); $DE = $g.Substring(16,16)
  $le = $A.Substring(6,2)+$A.Substring(4,2)+$A.Substring(2,2)+$A.Substring(0,2) +
        $B.Substring(2,2)+$B.Substring(0,2) +
        $C.Substring(2,2)+$C.Substring(0,2) + $DE
  $bytes = @()
  for ($i=0; $i -lt 32; $i+=2) { $bytes += [convert]::ToByte($le.Substring($i,2),16) }
  return ,([byte[]]$bytes)
}

function FindBytes($hay, $needle, $start=0) {
  for ($i=$start; $i -le $hay.Length-$needle.Length; $i++) {
    $ok=$true
    for ($j=0; $j -lt $needle.Length; $j++) { if ($hay[$i+$j] -ne $needle[$j]) { $ok=$false; break } }
    if ($ok) { return $i }
  }
  return -1
}

function Format-Hex($bytes) {
  return ($bytes | ForEach-Object { $_.ToString('x2') }) -join ''
}

# --- Search each GUID ---
$results = @()
foreach ($entry in $knownGuids.GetEnumerator()) {
  $guidStr = $entry.Key
  $label = $entry.Value
  $guidBytes = Convert-GuidToLeBytes $guidStr
  $offset = 0
  $foundCount = 0

  while ($true) {
    $offset = FindBytes $data $guidBytes $offset
    if ($offset -lt 0) { break }
    $foundCount++

    # Dump 32 bytes: 16 GUID + 4 flag + 12 context
    $endOffset = [Math]::Min($offset + 32, $data.Length)
    $context = $data[$offset..($endOffset-1)]
    $hex32 = Format-Hex $context

    # Parse the 4 flag bytes (offset+16 .. offset+19)
    $flagBytes = $data[($offset+16)..($offset+19)]
    $flagHex = Format-Hex $flagBytes
    $isShown = ($flagBytes[0] -ne 0)

    # Build the 20-byte SREP pattern (16 GUID + 4 flag)
    $pattern20 = Format-Hex $guidBytes + $flagHex

    Write-Host ("{0} [{1}] at offset 0x{2:X}" -f $label, $(if($isShown){"SHOWN"}else{"HIDDEN"}), $offset)
    Write-Host "  Full 32-byte context: $hex32"
    Write-Host "  Flag bytes:           $flagHex"
    Write-Host "  20-byte SREP pattern: $pattern20"
    if ($isShown) {
      $patched = Format-Hex $guidBytes + "00000000"
      $unpatched = $pattern20
      Write-Host "  To HIDE (patch):  $patched -> $pattern20"
    } else {
      $unpatched = Format-Hex $guidBytes + "01000000"
      Write-Host "  To SHOW (patch):  $pattern20 -> $unpatched"
    }
    Write-Host ""

    $results += [PSCustomObject]@{
      Label = $label
      Guid = $guidStr
      Offset = "0x{0:X}" -f $offset
      Shown = $isShown
      Pattern20 = $pattern20
      Context32 = $hex32
    }

    $offset += 16  # advance past this GUID match
  }

  if ($foundCount -eq 0) {
    Write-Host ("{0} [{1}]: NOT FOUND in binary" -f $label, $guidStr)
    Write-Host ""
  }
}

# --- Also scan for any GUID-like structures we don't know about ---
Write-Host "=== Scanning for unknown GUIDs with isShown=00000000 (hidden forms) ==="
Write-Host ""

# Scan for 16 bytes followed by 00000000 where first 4 bytes look like a GUID pattern
# (byte 6 and 8 of first group are version/variant indicators for real GUIDs)
$count = 0
for ($i=0; $i -le $data.Length-20; $i++) {
  # Check if bytes 16-19 are 00000000 (hidden flag)
  if ($data[$i+16] -ne 0 -or $data[$i+17] -ne 0 -or $data[$i+18] -ne 0 -or $data[$i+19] -ne 0) { continue }

  # Check GUID version nibble (byte 6 of GUID = data[$i+6], high nibble should be 4)
  $verByte = $data[$i+6]
  if (($verByte -band 0xF0) -ne 0x40) { continue }

  # Check variant bits (byte 8 of GUID = data[$i+8], high 2 bits should be 10)
  $varByte = $data[$i+8]
  if (($varByte -band 0xC0) -ne 0x80) { continue }

  # Skip if it matches a known GUID
  $isKnown = $false
  foreach ($entry in $knownGuids.GetEnumerator()) {
    $kb = Convert-GuidToLeBytes $entry.Key
    $match = $true
    for ($k=0; $k -lt 16; $k++) { if ($data[$i+$k] -ne $kb[$k]) { $match=$false; break } }
    if ($match) { $isKnown=$true; break }
  }
  if ($isKnown) { continue }

  $context = $data[$i..($i+31)]
  $hex32 = Format-Hex $context
  Write-Host ("Unknown GUID at 0x{0:X}: {1}" -f $i, $hex32)
  $count++
  if ($count -ge 20) { Write-Host "... (stopped after 20)"; break }
}

if ($count -eq 0) {
  Write-Host "No unknown hidden GUIDs found."
}

# --- Summary ---
Write-Host ""
Write-Host "=== SUMMARY ==="
foreach ($r in $results) {
  $status = if($r.Shown){"SHOWN"}else{"HIDDEN"}
  Write-Host ("{0,-25} {1}  {2}  {3}" -f $r.Label, $r.Offset, $status, $r.Pattern20)
}
