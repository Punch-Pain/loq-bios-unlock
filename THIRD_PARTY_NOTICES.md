# Third-Party Notices

This repository (`Punch-Pain/loq-bios-unlock`) contains, in addition to original
documentation, several **third-party tools, EFI drivers and firmware artifacts**
that are redistributed here for reproducibility of the BIOS-unlock procedure
described in the README.

**Important:** The GPL-3.0 `LICENSE` in this repository applies only to the
original content of this project (documentation, notes, configuration files and
mapping data written by the author). It does **not** re-license, and does not
take precedence over, the licenses of the third-party components listed below.
Each component remains under its own copyright and license terms. When a
component ships with its own license file, that file is included in the tree
and referenced here.

---

## 1. Open-source software included in this repository

### CHIPSEC

- **Path:** `BOOTABLE DEVICE/tools/chipsec/` (vendored checkout, ~155 MB) and
  `BOOTABLE DEVICE/tools/chipsec.zip`
- **Source:** https://github.com/intel/chipsec (Secure Hardware & Firmware research
  framework by Intel)
- **License:** GNU General Public License v2.0
- **License text:** included at `BOOTABLE DEVICE/tools/chipsec/LICENSE` and
  `BOOTABLE DEVICE/tools/chipsec/COPYING` (Debian copyright summary also present at
  `BOOTABLE DEVICE/tools/chipsec/debian/copyright`)

CHIPSEC is used in this project to inspect platform security configuration on the
author's own hardware. It is a large Python/C project; its full source tree is
vendored here unchanged.

### 7-Zip command line version (7za)

- **Path:** `BOOTABLE DEVICE/tools/7za/7za.exe`, `BOOTABLE DEVICE/tools/7za920.zip`
- **Version:** 7-Zip Command line version 9.20 (2010)
- **Copyright:** (C) 1999-2010 Igor Pavlov
- **License:** GNU LGPL
- **License text:** included at `BOOTABLE DEVICE/tools/7za/license.txt` and
  `BOOTABLE DEVICE/tools/7za/readme.txt`

### UEFITool NE (New Engine)

- **Path:** `BOOTABLE DEVICE/tools/UEFITool_NE/UEFITool.exe`
- **Source:** https://github.com/LongSoft/UEFITool (`new_engine` branch builds)
- **Copyright:** Nikolaj Schlej (LongSoft)
- **License:** BSD 2-Clause

### UEFIExtract NE

- **Path:** `BOOTABLE DEVICE/tools/UEFIExtract_NE/UEFIExtract.exe`
- **Source:** https://github.com/LongSoft/UEFITool (UEFIExtract component)
- **Copyright:** Nikolaj Schlej (LongSoft)
- **License:** BSD 2-Clause

The binaries above were obtained from the upstream project's release artifacts.
Their license text is not bundled with the binaries; the standard BSD 2-Clause
text is reproduced at the bottom of this file.

### IFRExtractor RS

- **Path:** `BOOTABLE DEVICE/tools/ifrextract-rs/ifrextractor.exe`
- **Source:** https://github.com/LongSoft/ifrextractor-rs
- **Copyright:** Nikolaj Schlej (LongSoft)
- **License:** BSD 2-Clause (see reproduction of the license text at the bottom
  of this file)

### Universal IFR Extractor

- **Path:** `BOOTABLE DEVICE/tools/ifrextract/ifrextract.exe`
- **Source:** https://github.com/donovan6000/Universal-IFR-Extractor
- **Copyright:** Donovan6000
- **License:** GNU General Public License v3.0 (the full license text is available
  at the upstream repository as `COPYING`)

### UEFI Shell

- **Path:** `BOOTABLE DEVICE/EFI/Boot/BOOTX64_SHELL.efi` (also referenced as
  `BOOTX64_SHELL.efi` in the README/UNLOCK_README instructions)
- **Source:** TianoCore / edk2 UEFI Shell distribution (Shell v2.x binaries)
- **Copyright:** Intel Corporation and TianoCore contributors
- **License:** BSD 2-Clause Patent (the edk2 "BSD+Patent" license)

*Note:* the binary was obtained as part of a pre-built tool package rather than
directly from an edk2 release, so its exact upstream build is presumed rather
than documented. The edk2 license permits redistribution with attribution.

---

## 2. Software redistributed without an explicit license

The following components are freely shared by their authors but ship **without a
license file or explicit redistribution terms**. They are redistributed here as
they were received, solely to keep the unlock procedure reproducible. If you are
an author of one of these components and want it removed from this repository,
open an issue and it will be removed promptly.

### SmokelessRuntimeEFIPatcher (SREP)

- **Path:** `BOOTABLE DEVICE/EFI/Boot/BOOTX64.efi` (SREP loader used by this
  procedure; a copy exists as `BOOTABLE DEVICE/EFI/Boot/BOOTX64_SREP.efi`)
- **Source:** SmokelessRuntimeEFIPatcher by James (SmokelessCPU); the original
  repository is no longer maintained. Community mirrors exist, e.g.
  https://github.com/hboyd2003/SmokelessRuntimeEFIPatcher and
  https://github.com/barlowhaydnb/SmokelessRuntimeEFIPatcher
- **Version:** 0.1.4c
- **License:** none provided by the author. The project is distributed as
  freeware through its official threads and mirrors; no license text ships with
  the binary or its sources in any known mirror.

The `SREP_Config.cfg` / `SREP_Config_G_WORKING.cfg` files in this repository are
original configuration files written for this project (not part of upstream SREP).

### UMAF (Smokeless UMAF / Universal AMD Form Browser)

- **Path:** `BOOTABLE DEVICE/EFI/Boot/BOOTX64_UMAF.efi` and
  `BOOTABLE DEVICE/downloads/UMAF_BETA.zip` (also `BOOTABLE DEVICE/umaf/`)
- **Source:** https://github.com/DavidS95/Smokeless_UMAF (backup repository of the
  original tool by xef)
- **License:** none provided in the distribution. The upstream README states the
  tool is shared "as a backup of the original project" for use at one's own risk.

*Note:* UMAF targets AMD form-browser menus and is **not required** for the
Lenovo LOQ unlock described in this repository (the README marks it as "not
needed"); it is present only as an archive of the working USB contents.

---

## 3. Lenovo firmware and extracted firmware artifacts

The following files originate from **Lenovo's firmware images** and are included
strictly for reproducibility and documentation of reverse-engineering work on
the author's own Lenovo LOQ Essential 15IRX11 (Type 83SC) machine:

- `BOOTABLE DEVICE/tools/secn22ww.exe` — the official Lenovo BIOS update package
  for SECN22WW, downloaded from Lenovo's support site
- `BOOTABLE DEVICE/tools/signed_SE.ROM` — the firmware image extracted from the
  package above
- `BOOTABLE DEVICE/tools/SetupUtility_pe32.efi` and
  `BOOTABLE DEVICE/tools/SetupUtilityApp_original.sct.bak` /
  `SetupUtilityApp_pe32.bin` — the BIOS Setup Utility module (and its thin
  wrapper) extracted from the firmware image with UEFITool
- `BOOTABLE DEVICE/tools/SetupUtility_pe32.efi.*.uefi.ifr.txt`,
  `BOOTABLE DEVICE/tools/Setup.ifr.txt`, `SetupUtilityApp_RE.txt` — IFR dumps and
  reverse-engineering notes derived from those modules (some are original work,
  but they are inseparable descriptions of Lenovo's proprietary setup code)

These artifacts are **(c) Lenovo** (and their respective OEM/IBV vendors) and are
not covered by any open-source license. They are redistributed here under the
fair-use/customary-practice norms of the firmware-research community, for
interoperability and educational purposes only. They must not be used to flash
hardware other than your own, and Lenovo remains the sole rights holder. If
requested by Lenovo, these artifacts will be removed from the repository.

---

## 4. Incidental files (not third-party software)

- `BOOTABLE DEVICE/System Volume Information/WPSettings.dat` — a Windows
  artifact created when the USB stick was formatted; included accidentally as
  part of the drive image and kept only for completeness of the archive.
- `BOOTABLE DEVICE/tools/__MACOSX/` — Finder metadata folder from a macOS zip
  extraction; contains no software.

These carry no license obligations but will be dropped when the repository is
slimmed down to the minimal file set described in the README.

---

## 5. BSD 2-Clause license text (for the binaries above)

The following license text applies to the UEFITool NE, UEFIExtract NE and
IFRExtractor RS binaries redistributed in this repository:

```
Copyright (c) Nikolaj Schlej (LongSoft)

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

## 6. Acknowledgements

Thanks to the authors and maintainers of CHIPSEC, 7-Zip, UEFITool/UEFIExtract,
the IFR extractors, the edk2/UEFI Shell project, SmokelessRuntimeEFIPatcher and
UMAF. Tools like these are what make community firmware research possible. This
project would not exist without them.
