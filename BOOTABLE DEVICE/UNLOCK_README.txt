Lenovo LOQ Essential 15IRX11 (SECN22WW) — Advanced BIOS Unlock
================================================================
Method: SREP (Setup ROTEP Entry Point) driver + Config G
Status: WORKING — Advanced tab visible in native F2 BIOS setup

Mechanism
---------
SREP is a UEFI DXE application that runs before the BIOS setup UI.
It patches runtime flags in H2OFormBrowserDxe's form-set visibility
table, flipping "isShown" bytes from 0x00 (hidden) to 0x01 (shown)
for 6 Lenovo-hidden form sets including Advanced and Power/Thermal.

The patch is MEMORY-ONLY — no flash modification occurs. Each boot,
SREP re-applies the patches from scratch via the config file.

Config G = Original 6-pattern config MINUS "Op Exec". The
"Op LoadFromFV SetupUtilityApp" trigger is what causes SREP to load
H2OFormBrowserDxe into memory, making the form-set table available
for patching. Without it, SREP patches the wrong memory region.

What Persists
-------------
YES:  NVRAM settings you save in Advanced BIOS menus persist across
      reboots (stored in standard UEFI NVRAM variables: Setup,
      SetupCpuFeatures, PchSetup, etc.).

NO:   The Advanced menu visibility itself does NOT persist — it must
      be re-patched every boot by SREP running as a DXE driver.

RECOVERY (immediate)
--------------------
1. Unplug USB drive → boot → no SREP loaded → Advanced hidden.
   (NVRAM settings you saved are still there, just invisible.)

2. From UEFI Shell (F12 → USB Shell):
     bcfg driver rm 0
   This removes the SREP DXE driver entry. On next boot, SREP
   will not run. Advanced hidden.

3. Nuclear option — delete from ESP:
     fs0:\        (or whichever maps to internal ESP)
     cd EFI\SREP
     del BOOTX64.efi
     del SREP_Config.cfg
     cd ..
     rmdir SREP
   Then optionally: bcfg driver rm 0

4. BIOS defaults: Enter F2 → "Load Defaults" → Save & Exit.
   This clears NVRAM settings (Advanced menus stay visible if
   SREP driver is still registered).

USB Layout (working)
--------------------
D:\EFI\Boot\BOOTX64.efi          SREP loader (same as SREP.efi)
D:\EFI\Boot\BOOTX64_SREP.efi     SREP loader backup
D:\EFI\Boot\BOOTX64_SHELL.efi    UEFI Shell v2.2 (for F12)
D:\SREP_Config.cfg                Active config (Config G)
D:\SREP_Config_G_WORKING.cfg     Backup of working config
D:\archive\                       All diagnostic logs, old configs,
                                  analysis outputs (NOT deleted)
D:\tools\                         Analysis tools + ROM extraction
D:\umaf\                          UMAF payload (unused)
D:\UNLOCK_README.txt              This file

Config G Contents (SREP_Config.cfg)
------------------------------------
Op Loaded
H2OFormBrowserDxe
Op Patch
Pattern
59B963B8C60E334099C18FD89F04022200000000
59B963B8C60E334099C18FD89F04022201000000
Op Patch
Pattern
E33545B0043046499EB714942898305300000000
E33545B0043046499EB714942898305301000000
Op Patch
Pattern
732871A65F92C64690B4A40F86A0917B00000000
732871A65F92C64690B4A40F86A0917B01000000
Op Patch
Pattern
9E76D4C6487F2A4D98E987ADCCF35CCC00000000
9E76D4C6487F2A4D98E987ADCCF35CCC01000000
Op Patch
Pattern
49D592C3EB27464F8A119F5DF55A9C8B00000000
49D592C3EB27464F8A119F5DF55A9C8B01000000
Op Patch
Pattern
1AB0E0C17E60754BB8BB0631ECFAACF200000000
1AB0E0C17E60754BB8BB0631ECFAACF201000000
Op End

Op LoadFromFV
SetupUtilityApp

Internal ESP Files (for USB-free operation)
-------------------------------------------
S:\SREP_Config.cfg                Config G (USB root copy)
S:\EFI\SREP\BOOTX64.efi           SREP loader
S:\EFI\SREP\SREP_Config.cfg       Config G (ESP copy)
S:\EFI\Microsoft\                  Windows boot files (UNTOUCHED)

ESP/Shell Commands
------------------
# One-time setup (from UEFI Shell boot, F12 → USB):
mountvol S: /s                    # (from Windows, mount ESP)
# From UEFI Shell:
fs0:\                             # (or map -r; identify ESP fs#)
bcfg driver rm 0                  # remove old USB-based entry
bcfg driver add 0 fsX:\EFI\SREP\BOOTX64.efi "SREP-Patch"
# (replace X with the fs# that maps to the internal ESP)

# Verify:
bcfg driver dump                  # show all DXE driver entries

# Remove SREP completely:
bcfg driver rm 0
# Then from shell: fsX:\EFI\SREP\ → del + rmdir

# Re-add after removal:
bcfg driver add 0 fsX:\EFI\SREP\BOOTX64.efi "SREP-Patch"

Rollback (restore original BIOS menus)
--------------------------------------
Option A: Unplug USB + remove ESP files + bcfg driver rm 0
Option F2: Enter BIOS (F2) → Load Defaults → Save & Exit
Option SPI: Flash original SECN22WW via Lenovo recovery (not needed
           unless NVRAM is corrupted — SREP never touches flash)

Key NVRAM Variables (Advanced settings)
---------------------------------------
VarStoreId  Name              GUID                              Size
0x1         Setup             EC87D643-EBA4-4BB5-A1E5-...     0xBAD
0x1234      SystemConfig      A04A27F4-DF00-4D42-B552-...     0x4B0
0x1233      AdvanceConfig     A04A27F4-DF00-4D42-B552-...     0x8
0x100C      SetupCpuFeatures  EC87D643-EBA4-4BB5-A1E5-...     0x39
0x2         SaSetup           72C5E28C-7783-43A1-8767-...     0x578
0x3         CpuSetup          B08F97FF-E6E8-4193-A997-...     0x3C1
0x5         PchSetup          4570B7F1-ADE8-4943-8DC3-...     0x80F
0x4         MeSetup           5432122D-D034-49D2-A6DE-...     0x36

SuppressIf Gate: OverClocking Performance Menu is hidden when
SetupCpuFeatures[0x30] == 0x00. Set to 0x01 to show OC menu.

Files in D:\archive\ (for reference)
-------------------------------------
- logs\SREP_log_baseline.txt      First successful boot log
- logs\SREP_log_UMAF.txt          UMAF boot log
- logs\SREP_log_F.txt             Config F boot log
- logs\out_*.txt                  NVRAM dumps from shell
- configs\                        All old/diag config variants
- rom\                            ROM analysis output
- extracted\                      FFS/SCT extractions

Generated: 2026-08-30
Machine:   Lenovo LOQ Essential 15IRX11 (model_r3cn)
BIOS:      SECN22WW
SREP:      0.1.4c
