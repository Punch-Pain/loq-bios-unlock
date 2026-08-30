param([string]$OutputDir = "C:\Abdalrhman\Devlopment\BIOS\osdump")

$code = @'
using System;
using System.Runtime.InteropServices;
using System.Security.Principal;

public class UefiVar {
  [DllImport("kernel32.dll", SetLastError=true, CharSet=CharSet.Unicode)]
  public static extern uint GetFirmwareEnvironmentVariable(
      string lpName, string lpGuid, byte[] pBuffer, uint nSize);

  [DllImport("advapi32.dll", SetLastError=true)]
  public static extern bool OpenProcessToken(IntPtr ProcessHandle,
      uint DesiredAccess, out IntPtr TokenHandle);

  [DllImport("advapi32.dll", SetLastError=true)]
  public static extern bool LookupPrivilegeValue(string lpSystemName,
      string lpName, out LUID lpLuid);

  [DllImport("advapi32.dll", SetLastError=true)]
  public static extern bool AdjustTokenPrivileges(IntPtr TokenHandle,
      bool DisableAllPrivileges, ref TOKEN_PRIVILEGES NewState,
      uint BufferLength, IntPtr PreviousState, IntPtr ReturnLength);

  [DllImport("kernel32.dll")]
  public static extern IntPtr GetCurrentProcess();

  public const uint TOKEN_ADJUST_PRIVILEGES = 0x0020;
  public const uint TOKEN_QUERY = 0x0008;
  public const uint SE_PRIVILEGE_ENABLED = 0x00000002;

  [StructLayout(LayoutKind.Sequential)]
  public struct LUID {
    public uint LowPart;
    public int HighPart;
  }

  [StructLayout(LayoutKind.Sequential)]
  public struct LUID_AND_ATTRIBUTES {
    public LUID Luid;
    public uint Attributes;
  }

  [StructLayout(LayoutKind.Sequential)]
  public struct TOKEN_PRIVILEGES {
    public uint PrivilegeCount;
    public LUID_AND_ATTRIBUTES Privileges;
  }

  public static bool EnableSeSystemEnvironment() {
    IntPtr hToken;
    if (!OpenProcessToken(GetCurrentProcess(),
        TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, out hToken))
      return false;
    LUID luid;
    if (!LookupPrivilegeValue(null, "SeSystemEnvironmentPrivilege", out luid))
      return false;
    TOKEN_PRIVILEGES tp = new TOKEN_PRIVILEGES();
    tp.PrivilegeCount = 1;
    tp.Privileges.Luid = luid;
    tp.Privileges.Attributes = SE_PRIVILEGE_ENABLED;
    return AdjustTokenPrivileges(hToken, false, ref tp, 0, IntPtr.Zero, IntPtr.Zero);
  }
}
'@

Add-Type -TypeDefinition $code -ErrorAction SilentlyContinue
[UefiVar]::EnableSeSystemEnvironment() | Out-Null

$out = $OutputDir
New-Item -ItemType Directory -Force -Path $out | Out-Null

$vars = @(
  @("Setup","{ec87d643-eba4-4bb5-a1e5-3f3e36b20da9}"),
  @("SetupCpuFeatures","{ec87d643-eba4-4bb5-a1e5-3f3e36b20da9}"),
  @("SystemConfig","{a04a27f4-df00-4d42-b552-39511302113d}"),
  @("AdvanceConfig","{a04a27f4-df00-4d42-b552-39511302113d}"),
  @("SaSetup","{72c5e28c-7783-43a1-8767-fad73fccafa4}"),
  @("CpuSetup","{b08f97ff-e6e8-4193-a997-5e9e9b0adb32}"),
  @("PchSetup","{4570b7f1-ade8-4943-8dc3-406472842384}"),
  @("MeSetup","{5432122d-d034-49d2-a6de-65a829eb4c74}")
)

$results = @()
foreach ($v in $vars) {
  $buf = New-Object byte[] 16384
  $len = [int][UefiVar]::GetFirmwareEnvironmentVariable($v[0], $v[1], $buf, 16384)
  if ($len -gt 0) {
    [IO.File]::WriteAllBytes("$out\$($v[0]).bin", $buf[0..($len-1)])
    $results += "$($v[0]): $len bytes OK"
  } else {
    $e = [Runtime.InteropServices.Marshal]::GetLastWin32Error()
    $results += "$($v[0]): NOT ACCESSIBLE (Win32 $e)"
  }
}
$results | Out-File "$out\results.txt"
