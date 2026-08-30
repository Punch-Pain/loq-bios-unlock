<# make_cfg.ps1 - generate a SECN22WW-specific SREP_Config.cfg
   Usage:
     .\make_cfg.ps1 -Bin D:\H2OFormBrowserDxe.bin -Ifr D:\Setup.ifr.txt -Out D:\SREP_Config.cfg
   Optional extra GUIDs (e.g. from other modules / community hints):
     .\make_cfg.ps1 -Bin D:\H2OFormBrowserDxe.bin -Ifr D:\Setup.ifr.txt -Out D:\SREP_Config.cfg -Guid "C6D4769E-7F48-4D2A-98E9-87ADCCF35CCC"
#>
param(
  [Parameter(Mandatory=$true)]  [string]$Bin,
  [Parameter(Mandatory=$false)] [string]$Ifr,
  [Parameter(Mandatory=$false)] [string]$Out = "D:\SREP_Config.cfg",
  [string[]]$Guid = @()
)

function Convert-GuidToSrepBytes($g) {
  $g = $g.Replace('{','').Replace('}','').Replace('-','')
  if ($g.Length -ne 32) { return $null }
  $A = $g.Substring(0,8);  $B = $g.Substring(8,4);  $C = $g.Substring(12,4); $DE = $g.Substring(16,16)
  $le = $A.Substring(6,2)+$A.Substring(4,2)+$A.Substring(2,2)+$A.Substring(0,2) + `
        $B.Substring(2,2)+$B.Substring(0,2) + `
        $C.Substring(2,2)+$C.Substring(0,2) + $DE
  $bytes = @()
  for ($i=0; $i -lt 32; $i+=2) { $bytes += [convert]::ToByte($le.Substring($i,2),16) }
  return $bytes
}

function FindBytes($haystack, $needle, $start=0) {
  for ($i=$start; $i -le $haystack.Length-$needle.Length; $i++) {
    $ok=$true
    for ($j=0; $j -lt $needle.Length; $j++) { if ($haystack[$i+$j] -ne $needle[$j]) { $ok=$false; break } }
    if ($ok) { return $i }
  }
  return -1
}

$data = [System.IO.File]::ReadAllBytes($Bin)
$guids = [System.Collections.Generic.List[string]]::new()
foreach ($x in $Guid) { $guids.Add($x) }
if ($Ifr -and (Test-Path $Ifr)) {
  $re = [regex]'(?i)\{?[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}\}?'
  foreach ($line in [System.IO.File]::ReadAllLines($Ifr)) {
    foreach ($m in $re.Matches($line)) { if (-not $guids.Contains($m.Value)) { $guids.Add($m.Value) } }
  }
}

$patches = [System.Collections.Generic.List[object]]::new()
foreach ($g in $guids) {
  $gb = Convert-GuidToSrepBytes $g
  if ($null -eq $gb) { Write-Host "skip bad GUID: $g"; continue }
  $hidden = $gb + @(0,0,0,0)
  $off = FindBytes $data $hidden
  if ($off -ge 0) {
    $shown = ($gb + @(1,0,0,0))
    $hiddenHex = ($hidden | ForEach-Object { $_.ToString('x2') }) -join ''
    $shownHex  = ($shown  | ForEach-Object { $_.ToString('x2') }) -join ''
    $patches.Add(@{guid=$g; off=$off; hidden=$hiddenHex; shown=$shownHex})
    Write-Host ("FOUND hidden form  GUID={0}  offset=0x{1:X}  -> reveal" -f $g, $off)
  } else {
    Write-Host ("not present as hidden form (already shown or not in H2OFormBrowserDxe): {0}" -f $g)
  }
}

if ($patches.Count -eq 0) {
  Write-Host "`nNo hidden form entries matched. The Advanced form-set GUID may not be in this IFR, or the form list uses a different layout. Try dumping SetupUtility/SetupBrowser too, or pass -Guid explicitly."
  exit 1
}

$sb = [System.Text.StringBuilder]::new()
[void]$sb.AppendLine("Op Loaded")
[void]$sb.AppendLine("H2OFormBrowserDxe")
foreach ($p in $patches) {
  [void]$sb.AppendLine("Op Patch")
  [void]$sb.AppendLine("Pattern")
  [void]$sb.AppendLine($p.hidden)
  [void]$sb.AppendLine($p.shown)
}
[void]$sb.AppendLine("Op End")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Op LoadFromFV")
[void]$sb.AppendLine("SetupUtilityApp")
[void]$sb.AppendLine("Op Exec")

Set-Content -Path $Out -Value $sb.ToString() -Encoding ASCII
Write-Host ("`nWrote {0} patch(es) -> {1}" -f $patches.Count, $Out)
