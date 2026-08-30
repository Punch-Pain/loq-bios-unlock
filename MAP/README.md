# BIOS Setup IFR Read-Only Investigation — Deliverables

**Machine:** Lenovo LOQ Essential 15IRX11 (Type 83SC) · i5-13450HX · NVIDIA RTX 5050 · BIOS SECN22WW
**Goal:** Map the Insyde H2O Setup tree to find settings that starve the dGPU under combined
CPU+GPU load (GPU-only is fine).
**Mode:** Strictly read-only. No SPI write, no flash, no setting changes. CFG Lock & Overclocking
Lock noted as Enabled (cross-reference only).

## Pipeline (how the data was obtained)
1. Vendor BIOS image `secn22ww.exe` (13.76 MB, matches running SECN22WW) downloaded from
   download.lenovo.com; 7-Zip extracted → `signed_SE.ROM` (21,262,952 B).
2. `signed_SE.ROM` whole-image IFRExtractor found only tiny AbtSetup; main Setup is LZMA-packed.
3. UEFIExtract failed (Error 35) on the nested LZMA GUID volume
   (`EE4E5898-3914-4259-9D6E-DC7BD79403CF`); decompressed manually: located the LZMA GUID, parsed
   the GUID_DEFINED section, LZMA-decompressed (FORMAT_ALONE) → `lzma_g4_c0_s4642141.bin`
   (27,865,088 B, contains "Advanced" + "PL4" = main DXE volume).
4. IFRExtractor-RS on that volume → the canonical full Setup tree
   `lzma_g4_c0_s4642141.bin.28.78.en-US.uefi.ifr.txt` (FormSet `C6D4769E…`, 166 forms,
   4,418 leaf controls). This is the primary source for everything below.

## Files in this folder
| File | What it is |
|------|------------|
| `raw_ifr_Advanced_FormSet.txt` | Raw extracted IFR of the full Advanced/Setup tree (the authoritative reference). 1.8 MB. |
| `structured_map.md` | Full hierarchical map: FormSet → Form → leaf control (type, VarStore, offset, QID, options, help). 788 KB. |
| `power_flags.md` | Every leaf control whose prompt/help matches power/thermal/GPU keywords (673 entries). |
| `focused_power_settings.md` | High-signal subset of the above (103 entries): Platform PLx, Psys/Pmax, PL3/PL4, EC Turbo, Response Mode, Graphics IMON, C-States. |
| `HYPOTHESIS.md` | Ranked 3–6 hypotheses + safe/risky split + read-only verification steps. **Start here.** |

## Other Setup FormSets present in the volume (not the power tree)
`Main` (C1E0B01A), `Power` (A6712873), `BIOS Setup`/`Configuration` (C31B2733 / F500784D),
`Exit` (B6936426), plus Device Manager / RST / MEBx / HTTP-Boot / Driver-Health driver forms.
The power-arbitration settings relevant to the dGPU symptom all live in the `Advanced` FormSet
(forms 0x100F, 0x1111, 0x13B7, 0x102A).

## Quick read-order
1. `HYPOTHESIS.md` — the answer.
2. `focused_power_settings.md` — the exact knobs + IFR help text.
3. `structured_map.md` / `raw_ifr_Advanced_FormSet.txt` — drill down.
