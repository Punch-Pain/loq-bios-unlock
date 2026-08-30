Lenovo LOQ Essential 15IRX11 (SECN22WW) — Advanced BIOS Unlock
================================================================
Method: SREP (Smokeless Runtime EFI Patcher) driver + Config G
Status: WORKING — Advanced tab visible in native F2 BIOS setup
Machine: Lenovo LOQ Essential 15IRX11 (model_secn)
BIOS:    SECN22WW
SREP:    0.1.4c


================================================================
HOW TO REPRODUCE (step by step)
================================================================

PREREQUISITES
-------------
- A FAT32-formatted USB drive (any size, 1GB+ is fine)
- This repository cloned or downloaded
- A Windows PC to prepare the USB

STEP 1: PREPARE THE USB
------------------------
On your Windows PC, format a USB drive as FAT32 (Quick Format is fine).

Then copy these 3 files from this repo to the USB:

  From:  BOOTABLE DEVICE\EFI\Boot\BOOTX64.efi
  To:    USB:\EFI\Boot\BOOTX64.efi

  From:  BOOTABLE DEVICE\EFI\Boot\BOOTX64_SHELL.efi
  To:    USB:\EFI\Boot\BOOTX64_SHELL.efi

  From:  BOOTABLE DEVICE\SREP_Config.cfg
  To:    USB:\SREP_Config.cfg

The USB should now look like:

  USB:\
    SREP_Config.cfg                          (660 bytes)
    EFI\
      Boot\
        BOOTX64.efi                          (16,704 bytes)
        BOOTX64_SHELL.efi                    (1,137,728 bytes)

That is ALL you need. Three files. Nothing else.

STEP 2: BOOT FROM USB
---------------------
1. Plug the USB into the LOQ 15IRX11.
2. Power on and immediately spam F12 to enter the Boot Menu.
3. Select your USB drive from the boot list.
4. The system will boot into the SREP driver, which patches the BIOS
   form-set visibility flags in memory, then hands off to Windows.

STEP 3: VERIFY UNLOCK
---------------------
After Windows boots:
1. Restart the computer.
2. Spam F2 during POST to enter BIOS Setup.
3. The "Advanced" tab should now be visible in the BIOS menu.

If it is there, you are done. The unlock is active.

STEP 4: MAKE IT PERSIST WITHOUT USB (one-time setup)
----------------------------------------------------
After confirming the unlock works with USB plugged in, you can
register SREP as a DXE driver on the internal EFI System Partition
(ESP) so you no longer need the USB.

4a. From Windows, open PowerShell as Administrator and run:

      mountvol S: /s

    This mounts the internal ESP as drive S:. Then copy the files:

      mkdir S:\EFI\SREP
      copy "BOOTABLE DEVICE\EFI\Boot\BOOTX64.efi" S:\EFI\SREP\BOOTX64.efi
      copy "BOOTABLE DEVICE\SREP_Config.cfg" S:\SREP_Config.cfg
      copy "BOOTABLE DEVICE\SREP_Config.cfg" S:\EFI\SREP\SREP_Config.cfg

    Then unmount:

      mountvol S: /d

4b. Now you need to register the driver from UEFI Shell:

    - Plug the USB back in (it has the UEFI Shell on it).
    - Reboot, spam F12, select USB from boot menu.
    - When the UEFI Shell loads, type:

        map -r

    - Find the fsX: that maps to your internal ESP (look for the
      one containing \EFI\SREP\). Usually fs1: or fs2:.
    - Run:

        bcfg driver add 0 fsX:\EFI\SREP\BOOTX64.efi "SREP-Patch"

      (Replace X with the actual number)

    - Verify with:

        bcfg driver dump

    - Type exit, remove USB, reboot.

4c. After this, SREP runs automatically from the internal ESP at
    every boot. You no longer need the USB. Press F2 at POST and
    the Advanced tab is there.


================================================================
QUICK REFERENCE (if you already know what you are doing)
================================================================

USB files needed:
  EFI\Boot\BOOTX64.efi        (SREP loader)
  EFI\Boot\BOOTX64_SHELL.efi  (UEFI Shell for F12)
  SREP_Config.cfg              (Config G — the working config)

Boot from USB → patches applied → Advanced visible in F2 BIOS.

ESP persistence:
  mountvol S: /s
  mkdir S:\EFI\SREP
  copy BOOTX64.efi S:\EFI\SREP\
  copy SREP_Config.cfg S:\EFI\SREP\
  copy SREP_Config.cfg S:\
  mountvol S: /d
  # Then from UEFI Shell:
  bcfg driver add 0 fsX:\EFI\SREP\BOOTX64.efi "SREP-Patch"


================================================================
RECOVERY (undo everything)
================================================================

Option 1 — Instant:  Unplug USB → reboot → Advanced hidden.
                      (Your NVRAM settings are still saved, just invisible.)

Option 2 — Shell:    Boot USB → F12 → Shell →
                      bcfg driver rm 0

Option 3 — ESP:      Boot USB → Shell →
                      mountvol S: /s
                      cd S:\EFI\SREP
                      del BOOTX64.efi
                      del SREP_Config.cfg
                      cd ..
                      rmdir SREP
                      bcfg driver rm 0

Option 4 — Nuclear:  Enter F2 → Load Defaults → Save & Exit.
                      (Clears all NVRAM settings, SREP stays registered
                       if driver entry still exists.)


================================================================
TECHNICAL DETAILS
================================================================

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

Repo Contents (this repository)
-------------------------------
BOOTABLE DEVICE\
  EFI\Boot\BOOTX64.efi            SREP loader (the file you need)
  EFI\Boot\BOOTX64_SHELL.efi      UEFI Shell v2.2 (for F12 boot)
  EFI\Boot\BOOTX64_SREP.efi       SREP loader backup
  EFI\Boot\BOOTX64_UMAF.efi       UMAF loader (not needed)
  SREP_Config.cfg                  Config G (the working config)
  SREP_Config_G_WORKING.cfg       Backup of working config
  UNLOCK_README.txt                This file
  logs\                            Boot logs + NVRAM dumps
  tools\                           Analysis tools, ROM, scripts
  umaf\                            UMAF payload (not needed)

tools\ contains:
  signed_SE.ROM                    Official BIOS image (keep for
                                  future BIOS updates — re-extract
                                  H2OFormBrowserDxe to find new
                                  patterns if Lenovo changes them)
  secn22ww.exe                     Original BIOS update executable
  make_cfg.ps1                     SREP config generator
  *.py                             Analysis scripts for pattern
                                  extraction from new ROMs
  ifrextract-rs\ifrextractor.exe   IFR extraction tool

MAP\ contains:
  raw_ifr_Advanced_FormSet.txt     Full IFR dump of Advanced menu
  structured_map.md                Human-readable form-set map
  focused_power_settings.md        Power/thermal setting offsets
  power_flags.md                   Complete variable reference
  HYPOTHESIS.md                    Reverse engineering notes

Generated: 2026-08-30
Machine:   Lenovo LOQ Essential 15IRX11 (model_secn)
BIOS:      SECN22WW
SREP:      0.1.4c
