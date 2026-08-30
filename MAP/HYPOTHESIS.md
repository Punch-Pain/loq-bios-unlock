# dGPU-Under-Combined-Load Investigation — Hypothesis & Risk Map
**Target:** Lenovo LOQ Essential 15IRX11 (Type 83SC), i5-13450HX + NVIDIA RTX 5050 (dGPU),
Insyde H2O BIOS SECN22WW.
**Method:** Read-only. Source = official vendor BIOS image (`secn22ww.exe` → `signed_SE.ROM`),
LZMA volume decompressed, IFR extracted with IFRExtractor-RS v1.6.1. Main Setup tree =
`decompressed/lzma_g4_c0_s4642141.bin.28.78.en-US.uefi.ifr.txt` (FormSet `C6D4769E…`,
“Advanced”, 166 forms / 4,418 leaf controls).
**Constraint:** No settings were changed. CFG Lock & Overclocking Lock are Enabled (noted only).
SREP runtime-unlock of the Advanced menu is assumed to expose these items (cross-reference only).

## How to read the evidence
The RTX 5050 is a **discrete** GPU. It is **not** part of Intel RAPL/Psys accounting on the
CPU package. The CPU and dGPU share one **platform power budget (Psys)** fed through the
same rail/VR. The IFR exposes a separate “Platform PL1/PL2” knob that the help text ties
directly to the *Package RAPL algorithm*:

> *Platform Power Limit 2 Power … “Recommended value is 97000 if Psys is in %. This setting
> will act as the new PL2 value for the Package RAPL algorithm.”*
> (Form 0x100F “CPU – Power Management Control”, VarStore `CpuSetup`, off 0x38, QID 0xB1)

> *Platform Power Limit 1 Power … “This setting will act as the new PL1 value for the Package
> RAPL algorithm.”*
> (Form 0x100F, off 0x32, QID 0xAE)

Observed values: **Platform PL1 = 360 W, PL2 = 395 W, PL4 = 200 W**, set *independently* of the
CPU-package limits (PL1 55 W / PL2 130 W). The large “Platform” numbers are the platform/Psys
ceiling; the CPU package draws up to 130 W of it, leaving the remainder for the dGPU + rest.
This shared-budget topology is the root enabler of the symptom: GPU-only is fine because nothing
else competes for Psys; combined load makes the dGPU the marginal consumer that gets starved.

---

## Ranked hypotheses (most → least plausible)

### H1 — Platform/Psys power ceiling is the binding constraint under combined load  (HIGH)
Combined CPU+GPU load drives total platform power toward the Platform PL2 / Psys ceiling.
Because the dGPU ramps **after** the CPU has already claimed its turbo budget, and because the
dGPU has no RAPL priority in the Intel power algorithm, the residual Psys headroom left for the
dGPU is too small for it to climb to its max clock/power.
- **Evidence:** Platform PL1/PL2 are explicitly “new PL1/PL2 value for the Package RAPL
  algorithm” (Form 0x100F, off 0x32/0x38); values 360/395 W are far above the 55/130 W
  CPU-package limits, i.e. a distinct shared platform budget. Symptom is load-combination-
  specific, which is exactly what a shared-budget model predicts.
- **Test (read-only):** Log during a combined CPU+GPU stress: package/Psys power (HWiNFO
  “CPU Package Power” + a dGPU power readout), and the dGPU “Performance Limit” reasons
  (NVML/`nvidia-smi -q -d POWER`). If dGPU clocks cap while Psys ≈ Platform PL2, this is it.

### H2 — Psys_PL3 / Response Mode aggressive reduction clips the dGPU  (HIGH)
PL3 is a fast, secondary platform power limit used to yank power when Psys approaches PMax.
“Response Mode” selects how PL3 reduces power.
> *“Use Response Mode to adjust Psys_PL3 power reduction behavior. Battery-enabled systems use
> Gradual power reduction.”* (Form 0x1111 “Power Limit 3 Settings”, off 0x383, QID 0x177)
If Response Mode is set to a non-Gradual/aggressive profile, the moment combined load nears
Pmax the platform does a hard power cut that lands disproportionately on the dGPU (slowest to
react). GPU-only never reaches Pmax, so the cut never fires.
- **Evidence:** PL3 (off 0x23, QID 0x174) help: *“limit must be less than Psys Pmax value…
  Recommended value is 100000 if Psys is in %.”* Tight PL3 + aggressive Response Mode = dGPU
  clip under combined load.
- **Test (read-only):** Compare dGPU clock/power trace with CPU loaded vs idle; look for a
  step-down coincident with Psys crossing PL3, and note the Response Mode value.

### H3 — Psys PMax / Vsys-Psys Critical Threshold set conservatively for the adapter  (MEDIUM)
Psys PMax and the Vsys/Psys Critical + Full-Scale/Threshold values define the absolute
platform ceiling. The help references the VR mailbox and an adapter-derating hint:
> *“Psys Pmax power … For ATX12VO Percent recommended 200% enter 1600. Uses BIOS VR mailbox
> command 0xB.”* (Form 0x13B7 “CPU VR Settings”, off 0x12B, QID 0x11C)
If PMax/Critical are tuned for a smaller PSU or for ATX12VO 200% derating, the combined load
trips the critical threshold and the EC throttles the whole platform — dGPU included.
- **Test (read-only):** Identify the shipped AC adapter wattage vs the PMax threshold; check
  EC/throttling events in a combined-load log (HWiNFO “IA/GT/PL limits” + dGPU reasons).

### H4 — EC Turbo Control Mode rebalances budget away from the dGPU  (MEDIUM)
> *“Enable/Disable EC Turbo Control mode”* (Form 0x100F, off 0xC7, QID 0xCC)
With EC Turbo Control enabled, the embedded controller dynamically manages turbo/PL based on
platform thermals/power. A conservative EC policy can cap CPU turbo (good) but also pull the
platform ceiling down, shrinking dGPU headroom under combined load.
- **Test (read-only):** Toggle is gated by CFG/OC Lock state; observe whether EC-reported
  PL1/PL2 values change between idle and combined load (means EC is actively steering them).

### H5 — Graphics Turbo IMON Current mis-calibration  (LOW–MEDIUM)
> *“Graphics turbo IMON current values supported (14-31)”* (Form 0x102A “Graphics
> Configuration”, Numeric)
IMON (current monitor) calibration affects how the power algorithm *accounts* GPU/GT current.
A mis-set IMON offset can make the algorithm believe the GPU draws more than it does, causing
early clamping. Lower signal because it is a calibration, not a hard ceiling.
- **Test (read-only):** Compare reported vs measured dGPU current; an offset error shows as
  systematic over-accounting.

### H6 — Real dGPU limit lives in the VBIOS, not in Setup  (CONTEXT / LOW)
Lenovo ships a **separate** `loqeintel1501_vbiosupdate.exe` (RTX 5050 VBIOS) with its own
power/clock tables (TGP, board power, thermal). Setup cannot raise the dGPU beyond what the
VBIOS allows. If the VBIOS board-power limit is set tightly, combined-load thermal/power
headroom forces the dGPU down even when Psys has room.
- **Implication:** This is the most likely *actual fix path* (VBIOS update), and it is a
  flashing operation → out of scope for read-only and flagged RISKY below.

---

## Safe vs. understand-before-touch

### SAFE to experiment with later (standard Insyde knobs, reversible via “Load Setup Defaults”)
- Platform PL1/PL2 **Enable** + **Power** (Form 0x100F, off 0x31/0x32/0x37/0x38)
- Power Limit 3 **Override / Power / Time Window / Duty Cycle / Response Mode / Lock**
  (Form 0x1111, off 0x23/0x383/…)
- Power Limit 4 **Override / Power / Lock** (Form 0x100F, off 0x2A/0x2B/0x2F)
- EC Turbo Control Mode (Form 0x100F, off 0xC7)
- Graphics Turbo IMON Current (Form 0x102A)
- Package C-State Limit / Demotion (Form 0x100F)

### UNDERSTAND FULLY BEFORE TOUCHING (can brick / lock the machine / void warranty)
- **Firmware Configuration** OneOf (“Ignore Policy Update” / “Production” / “Test”) — Boot
  Guard / manufacturing state; wrong value can lock the platform.
- **CFG Lock** and **Overclocking Lock** (currently Enabled) — gating fuses; changing them
  alters security & unlock behavior.
- **PCH-FW / ME Configuration** (Form 0x103E) — Management Engine / SPI protections.
- **Secure Boot / Platform Keys / Audit Mode** (Security tree) — can soft-brick boot.
- **Debug Settings** (Form 0x1006) and **Platform Settings** (Form 0x1125) — low-level HW.
- **Flashing the dGPU VBIOS** (`loqeintel1501_vbiosupdate.exe`) — H6 fix path, but a failed
  flash bricks the GPU. Do not attempt under this read-only engagement.

---

## Recommended next (read-only) verification, before any change
1. Capture a combined-load log: HWiNFO sensors (CPU Package Power, Psys if exposed, IA/GT/PL
   limit reasons) + `nvidia-smi -q -d POWER,CLOCK` every 1 s, with and without CPU load.
2. Note the actual Platform PL1/PL2/PL3/PL4 and Response Mode/EC Turbo values present in NVRAM
   (read via the unlocked Setup or `chipsec`/`ru.efi` — NOT modified).
3. Cross-check adapter wattage against Psys PMax/Critical thresholds (Form 0x13B7).
4. If H1/H2 confirmed, the corrective knob is Platform PL / PL3 / Response Mode (SAFE group);
   if the VBIOS is the ceiling (H6), only a VBIOS update applies (RISKY group).

**No BIOS/Setup/VBIOS settings were modified during this analysis.**
