# Focused Power / Thermal / GPU-relevant Settings (high-signal subset)
Extracted from Advanced FormSet (28.78). 103 entries shown out of 673 flagged.

## Form 0x100A: ACPI Settings  ->  **CS PL1 Limit** (oneof)
- VarStore: Setup @ offset 0x39 | QuestionId 0x60 | size 8
- options: 
- help: Limit PL1 (Power Limit 1) while in Connected Standby

## Form 0x100A: ACPI Settings  ->  **CS PL1 Value** (numeric)
- VarStore: Setup @ offset 0x3A | QuestionId 0x61 | size 16
- min 0xBB8 max 0x4E20
- help: PL1 value is in milliwatts with 125 step value

## Form 0x100F: CPU - Power Management Control  ->  **Intel(R) Turbo Boost Max Technology 3.0** (oneof)
- VarStore: CpuSetup @ offset 0xC | QuestionId 0x1409 | size 8
- options: 
- help: Enable/Disable Intel(R) Turbo Boost Max Technology 3.0 support. Disabling will report the maximum ratio of the slowest core in _CPC object.

## Form 0x100F: CPU - Power Management Control  ->  **Turbo Mode** (oneof)
- VarStore: CpuSetup @ offset 0x16 | QuestionId 0x1579 | size 8
- options: 
- help: Enable/Disable processor Turbo Mode (requires EMTTM enabled too). AUTO means enabled.

## Form 0x100F: CPU - Power Management Control  ->  **Platform PL1 Enable** (oneof)
- VarStore: CpuSetup @ offset 0x31 | QuestionId 0xAD | size 8
- options: 
- help: Enable/Disable Platform Power Limit 1 programming. If this option is enabled, it activates the PL1 value to be used by the processor to limit the average power of given time window.

## Form 0x100F: CPU - Power Management Control  ->  **Platform PL1 Power** (numeric)
- VarStore: CpuSetup @ offset 0x32 | QuestionId 0xAE | size 32
- min 0x0 max 0x3E7F83
- help: Platform Power Limit 1 Power in Milli Watts/Percent. BIOS will round to the nearest 1/8W when programming. Any value can be programmed between Max and Min Power Limits (specified by PACKAGE_POWER_SKU_MSR). For example, if 12.50W, enter 12500, if 12%, enter 12000, if 50%, enter 50000. This setting will act as the new PL1 value for the Package RAPL algorithm.

## Form 0x100F: CPU - Power Management Control  ->  **Platform PL1 Time Window** (oneof)
- VarStore: CpuSetup @ offset 0x36 | QuestionId 0xAF | size 8
- options: 
- help: Platform Power Limit 1 Time Window value in seconds. The value may vary from 0 to 128. 0 = default values. Indicates the time window over which Platform Processor Base Power (TDP) value should be maintained.

## Form 0x100F: CPU - Power Management Control  ->  **Platform PL2 Enable** (oneof)
- VarStore: CpuSetup @ offset 0x37 | QuestionId 0xB0 | size 8
- options: 
- help: Enable/Disable Platform Power Limit 2 programming. If this option is disabled, BIOS will program the default values for Platform Power Limit 2.

## Form 0x100F: CPU - Power Management Control  ->  **Platform PL2 Power** (numeric)
- VarStore: CpuSetup @ offset 0x38 | QuestionId 0xB1 | size 32
- min 0x0 max 0x3E7F83
- help: Platform Power Limit 2 Power in Milli Watts / Milli Percent. BIOS will round to the nearest 1/8W or 1/8% when programming. Any value can be programmed between Max and Min Power Limits (specified by PACKAGE_POWER_SKU_MSR) or PMAX value in %. For example if 12%, enter 12000, if 50%, enter 50000. If the value is '0', will default to PACKAGE_POWER_SKU_MSR if Psys is in Watts. Recommended value is 97000 if Psys is in %. This setting will act as the new PL2 value for the Package RAPL algorithm.

## Form 0x100F: CPU - Power Management Control  ->  **Power Limit 4 Override** (oneof)
- VarStore: CpuSetup @ offset 0x2A | QuestionId 0xB3 | size 8
- options: 
- help: Enable/Disable Power Limit 4 override. If this option is disabled, BIOS will leave the default values for Power Limit 4.

## Form 0x100F: CPU - Power Management Control  ->  **Power Limit 4** (numeric)
- VarStore: CpuSetup @ offset 0x2B | QuestionId 0xB4 | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 4 in Milli Watts. BIOS will round to the nearest 1/8W when programming. For 12.50W, enter 12500. If the value is 0, BIOS leaves default value

## Form 0x100F: CPU - Power Management Control  ->  **Power Limit 4 Lock** (oneof)
- VarStore: CpuSetup @ offset 0x2F | QuestionId 0xB5 | size 8
- options: 
- help: Power Limit 4 MSR 601h Lock. When enabled PL4 configurations are locked during OS. When disabled PL4 configuration can be changed during OS.

## Form 0x100F: CPU - Power Management Control  ->  **Package C-State Demotion** (oneof)
- VarStore: CpuSetup @ offset 0x40 | QuestionId 0xB9 | size 8
- options: 
- help: Package C-State Demotion

## Form 0x100F: CPU - Power Management Control  ->  **Package C-State Un-demotion** (oneof)
- VarStore: CpuSetup @ offset 0x41 | QuestionId 0xBA | size 8
- options: 
- help: Package C-State Un-demotion

## Form 0x100F: CPU - Power Management Control  ->  **Package C State Limit** (oneof)
- VarStore: CpuSetup @ offset 0x4B | QuestionId 0xBD | size 8
- options: 
- help: Maximum Package C State Limit Setting. Cpu Default: Leaves to Factory default value.Auto: Initializes to deepest available Package C State Limit.

## Form 0x100F: CPU - Power Management Control  ->  **EC Turbo Control Mode** (oneof)
- VarStore: CpuSetup @ offset 0xC7 | QuestionId 0xCC | size 8
- options: 
- help: Enable/Disable EC Turbo Control mode

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Numcore0** (numeric)
- VarStore: CpuSetup @ offset 0xE6 | QuestionId 0x10A1 | size 8
- min 0x0 max 0xFF
- help: Performance-core Turbo Ratio Limit Numcore0 defines the core range, the turbo ratio is defined in Turbo Ratio Limit Ratio0. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Numcore1** (numeric)
- VarStore: CpuSetup @ offset 0xE7 | QuestionId 0x10A2 | size 8
- min 0x0 max 0xFF
- help: Performance-core Turbo Ratio Limit Numcore1 defines the core range, the turbo ratio is defined in Turbo Ratio Limit Ratio1. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Numcore2** (numeric)
- VarStore: CpuSetup @ offset 0xE8 | QuestionId 0x10A3 | size 8
- min 0x0 max 0xFF
- help: Performance-core Turbo Ratio Limit Numcore2 defines the core range, the turbo ratio is defined in Turbo Ratio Limit Ratio2. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Numcore3** (numeric)
- VarStore: CpuSetup @ offset 0xE9 | QuestionId 0x10A4 | size 8
- min 0x0 max 0xFF
- help: Performance-core Turbo Ratio Limit Numcore3 defines the core range, the turbo ratio is defined in Turbo Ratio Limit Ratio3. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Numcore4** (numeric)
- VarStore: CpuSetup @ offset 0xEA | QuestionId 0x10A5 | size 8
- min 0x0 max 0xFF
- help: Performance-core Turbo Ratio Limit Numcore4 defines the core range, the turbo ratio is defined in Turbo Ratio Limit Ratio4. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Numcore5** (numeric)
- VarStore: CpuSetup @ offset 0xEB | QuestionId 0x10A6 | size 8
- min 0x0 max 0xFF
- help: Performance-core Turbo Ratio Limit Numcore5 defines the core range, the turbo ratio is defined in Turbo Ratio Limit Ratio5. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Numcore6** (numeric)
- VarStore: CpuSetup @ offset 0xEC | QuestionId 0x10A7 | size 8
- min 0x0 max 0xFF
- help: Performance-core Turbo Ratio Limit Numcore6 defines the core range, the turbo ratio is defined in Turbo Ratio Limit Ratio6. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Numcore7** (numeric)
- VarStore: CpuSetup @ offset 0xED | QuestionId 0x10A8 | size 8
- min 0x0 max 0xFF
- help: Performance-core Turbo Ratio Limit Numcore7 defines the core range, the turbo ratio is defined in Turbo Ratio Limit Ratio7. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Ratio0** (numeric)
- VarStore: CpuSetup @ offset 0xD6 | QuestionId 0x10A9 | size 8
- min 0x0 max 0x78
- help: Performance-core Turbo Ratio Limit Ratio0 defines the turbo ratio (max is 85 in normal mode and 120 in core extension mode), the core range is defined in Turbo Ratio Limit Numcore0.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Ratio1** (numeric)
- VarStore: CpuSetup @ offset 0xD7 | QuestionId 0x10AA | size 8
- min 0x0 max 0x78
- help: Performance-core Turbo Ratio Limit Ratio1 defines the turbo ratio (max is 85 in normal mode and 120 in core extension mode), the core range is defined in Turbo Ratio Limit Numcore1.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Ratio2** (numeric)
- VarStore: CpuSetup @ offset 0xD8 | QuestionId 0x10AB | size 8
- min 0x0 max 0x78
- help: Performance-core Turbo Ratio Limit Ratio2 defines the turbo ratio (max is 85 in normal mode and 120 in core extension mode), the core range is defined in Turbo Ratio Limit Numcore2.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Ratio3** (numeric)
- VarStore: CpuSetup @ offset 0xD9 | QuestionId 0x10AC | size 8
- min 0x0 max 0x78
- help: Performance-core Turbo Ratio Limit Ratio3 defines the turbo ratio (max is 85 in normal mode and 120 in core extension mode), the core range is defined in Turbo Ratio Limit Numcore3.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Ratio4** (numeric)
- VarStore: CpuSetup @ offset 0xDA | QuestionId 0x10AD | size 8
- min 0x0 max 0x78
- help: Performance-core Turbo Ratio Limit Ratio4 defines the turbo ratio (max is 85 in normal mode and 120 in core extension mode), the core range is defined in Turbo Ratio Limit Numcore4.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Ratio5** (numeric)
- VarStore: CpuSetup @ offset 0xDB | QuestionId 0x10AE | size 8
- min 0x0 max 0x78
- help: Performance-core Turbo Ratio Limit Ratio5 defines the turbo ratio (max is 85 in normal mode and 120 in core extension mode), the core range is defined in Turbo Ratio Limit Numcore5.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Ratio6** (numeric)
- VarStore: CpuSetup @ offset 0xDC | QuestionId 0x10AF | size 8
- min 0x0 max 0x78
- help: Performance-core Turbo Ratio Limit Ratio6 defines the turbo ratio (max is 85 in normal mode and 120 in core extension mode), the core range is defined in Turbo Ratio Limit Numcore6.

## Form 0x1015: Turbo Ratio Limit Options  ->  **P-core Turbo Ratio Limit Ratio7** (numeric)
- VarStore: CpuSetup @ offset 0xDD | QuestionId 0x10B0 | size 8
- min 0x0 max 0x78
- help: Performance-core Turbo Ratio Limit Ratio7 defines the turbo ratio (max is 85 in normal mode and 120 in core extension mode), the core range is defined in Turbo Ratio Limit Numcore7.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Numcore0** (numeric)
- VarStore: CpuSetup @ offset 0x106 | QuestionId 0x10B1 | size 8
- min 0x0 max 0xFF
- help: Efficient-core Turbo Ratio Limit Numcore0 defines the core range, the turbo ratio is defined in E-core Turbo Ratio Limit Ratio0. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Numcore1** (numeric)
- VarStore: CpuSetup @ offset 0x107 | QuestionId 0x10B2 | size 8
- min 0x0 max 0xFF
- help: Efficient-core Turbo Ratio Limit Numcore1 defines the core range, the turbo ratio is defined in E-core Turbo Ratio Limit Ratio1. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Numcore2** (numeric)
- VarStore: CpuSetup @ offset 0x108 | QuestionId 0x10B3 | size 8
- min 0x0 max 0xFF
- help: Efficient-core Turbo Ratio Limit Numcore2 defines the core range, the turbo ratio is defined in E-core Turbo Ratio Limit Ratio2. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Numcore3** (numeric)
- VarStore: CpuSetup @ offset 0x109 | QuestionId 0x10B4 | size 8
- min 0x0 max 0xFF
- help: Efficient-core Turbo Ratio Limit Numcore3 defines the core range, the turbo ratio is defined in E-core Turbo Ratio Limit Ratio3. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Numcore4** (numeric)
- VarStore: CpuSetup @ offset 0x10A | QuestionId 0x10B5 | size 8
- min 0x0 max 0xFF
- help: Efficient-core Turbo Ratio Limit Numcore4 defines the core range, the turbo ratio is defined in E-core Turbo Ratio Limit Ratio4. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Numcore5** (numeric)
- VarStore: CpuSetup @ offset 0x10B | QuestionId 0x10B6 | size 8
- min 0x0 max 0xFF
- help: Efficient-core Turbo Ratio Limit Numcore5 defines the core range, the turbo ratio is defined in E-core Turbo Ratio Limit Ratio5. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Numcore6** (numeric)
- VarStore: CpuSetup @ offset 0x10C | QuestionId 0x10B7 | size 8
- min 0x0 max 0xFF
- help: Efficient-core Turbo Ratio Limit Numcore6 defines the core range, the turbo ratio is defined in E-core Turbo Ratio Limit Ratio6. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Numcore7** (numeric)
- VarStore: CpuSetup @ offset 0x10D | QuestionId 0x10B8 | size 8
- min 0x0 max 0xFF
- help: Efficient-core Turbo Ratio Limit Numcore7 defines the core range, the turbo ratio is defined in E-core Turbo Ratio Limit Ratio7. If value is zero, this entry is ignored.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Ratio0** (numeric)
- VarStore: CpuSetup @ offset 0xF6 | QuestionId 0x10B9 | size 8
- min 0x0 max 0x55
- help: Efficient-core Turbo Ratio Limit Ratio0 defines the turbo ratio (max is 85 irrespective of the core extension mode), the core range is defined in E-core Turbo Ratio Limit Numcore0.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Ratio1** (numeric)
- VarStore: CpuSetup @ offset 0xF7 | QuestionId 0x10BA | size 8
- min 0x0 max 0x55
- help: Efficient-core Turbo Ratio Limit Ratio1 defines the turbo ratio (max is 85 irrespective of the core extension mode), the core range is defined in E-core Turbo Ratio Limit Numcore1.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Ratio2** (numeric)
- VarStore: CpuSetup @ offset 0xF8 | QuestionId 0x10BB | size 8
- min 0x0 max 0x55
- help: Efficient-core Turbo Ratio Limit Ratio2 defines the turbo ratio (max is 85 irrespective of the core extension mode), the core range is defined in E-core Turbo Ratio Limit Numcore2.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Ratio3** (numeric)
- VarStore: CpuSetup @ offset 0xF9 | QuestionId 0x10BC | size 8
- min 0x0 max 0x55
- help: Efficient-core Turbo Ratio Limit Ratio3 defines the turbo ratio (max is 85 irrespective of the core extension mode), the core range is defined in E-core Turbo Ratio Limit Numcore3.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Ratio4** (numeric)
- VarStore: CpuSetup @ offset 0xFA | QuestionId 0x10BD | size 8
- min 0x0 max 0x55
- help: Efficient-core Turbo Ratio Limit Ratio4 defines the turbo ratio (max is 85 irrespective of the core extension mode), the core range is defined in E-core Turbo Ratio Limit Numcore4.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Ratio5** (numeric)
- VarStore: CpuSetup @ offset 0xFB | QuestionId 0x10BE | size 8
- min 0x0 max 0x55
- help: Efficient-core Turbo Ratio Limit Ratio5 defines the turbo ratio (max is 85 irrespective of the core extension mode), the core range is defined in E-core Turbo Ratio Limit Numcore5.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Ratio6** (numeric)
- VarStore: CpuSetup @ offset 0xFC | QuestionId 0x10BF | size 8
- min 0x0 max 0x55
- help: Efficient-core Turbo Ratio Limit Ratio6 defines the turbo ratio (max is 85 irrespective of the core extension mode), the core range is defined in E-core Turbo Ratio Limit Numcore6.

## Form 0x1015: Turbo Ratio Limit Options  ->  **E-core Turbo Ratio Limit Ratio7** (numeric)
- VarStore: CpuSetup @ offset 0xFD | QuestionId 0x10C0 | size 8
- min 0x0 max 0x55
- help: Efficient-core Turbo Ratio Limit Ratio7 defines the turbo ratio (max is 85 irrespective of the core extension mode), the core range is defined in E-core Turbo Ratio Limit Numcore7.

## Form 0x1011:   View/Configure Turbo Options  ->  **Package Power Limit MSR Lock** (oneof)
- VarStore: CpuSetup @ offset 0x30 | QuestionId 0x112 | size 8
- options: 
- help: Enable/Disable locking of Package Power Limit settings. When enabled, PACKAGE_POWER_LIMIT MSR will be locked and a reset will be required to unlock the register.

## Form 0x1011:   View/Configure Turbo Options  ->  **Power Limit 1 Override** (oneof)
- VarStore: CpuSetup @ offset 0x1B | QuestionId 0x113 | size 8
- options: 
- help: Enable/Disable Power Limit 1 override. If this option is disabled, BIOS will program the default values for Power Limit 1 and Power Limit 1 Time Window.

## Form 0x1011:   View/Configure Turbo Options  ->  **Power Limit 1** (numeric)
- VarStore: CpuSetup @ offset 0x17 | QuestionId 0x114 | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 1 in Milli Watts. BIOS will round to the nearest 1/8W when programming. 0 = no custom override. For 12.50W, enter 12500. Overclocking SKU: Value must be between Max and Min Power Limits (specified by PACKAGE_POWER_SKU_MSR). Other SKUs: This value must be between Min Power Limit and Processor Base Power (TDP) Limit. If value is 0, BIOS will program Processor Base Power (TDP) value.

## Form 0x1011:   View/Configure Turbo Options  ->  **Power Limit 1 Time Window** (oneof)
- VarStore: CpuSetup @ offset 0x1C | QuestionId 0x115 | size 8
- options: 
- help: Power Limit 1 Time Window value in seconds. The value may vary from 0 to 128. 0 = default value. Defines time window which Processor Base Power (TDP) value should be maintained.

## Form 0x1011:   View/Configure Turbo Options  ->  **Power Limit 2 Override** (oneof)
- VarStore: CpuSetup @ offset 0x1D | QuestionId 0x116 | size 8
- options: 
- help: Enable/Disable Power Limit 2 override. If this option is disabled, BIOS will program the default values for Power Limit 2.

## Form 0x1011:   View/Configure Turbo Options  ->  **Power Limit 2** (numeric)
- VarStore: CpuSetup @ offset 0x1E | QuestionId 0x117 | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 2 value in Milli Watts. BIOS will round to the nearest 1/8W when programming. If the value is 0, BIOS will program this value as 1.25*Processor Base Power (TDP). For 12.50W, enter 12500. Processor applies control policies such that the package power does not exceed this limit.

## Form 0x1011:   View/Configure Turbo Options  ->  **Energy Efficient Turbo** (oneof)
- VarStore: CpuSetup @ offset 0x1D5 | QuestionId 0x118 | size 8
- options: 
- help: Enable/Disable Energy Efficient Turbo Feature. This feature will opportunistically lower the turbo frequency to increase efficiency. Recommended only to disable in overclocking situations where turbo frequency must remain constant. Otherwise, leave enabled.

## Form 0x13B7: CPU VR Settings  ->  **PSYS Slope** (numeric)
- VarStore: CpuSetup @ offset 0x127 | QuestionId 0x119 | size 8
- min 0x0 max 0xC8
- help: PSYS Slope defined in 1/100 increments. Range is 0-200. For a 1.25 slope, enter 125. 0 = AUTO. Uses BIOS VR mailbox command 0x9.

## Form 0x13B7: CPU VR Settings  ->  **PSYS Offset** (numeric)
- VarStore: CpuSetup @ offset 0x128 | QuestionId 0x11A | size 16
- min 0x0 max 0xF9FF
- help: PSYS Offset defined in 1/1000 increments. Range is 0-63999. For an offset of 25.348, enter 25348. PSYS Uses BIOS VR mailbox command 0x4.

## Form 0x13B7: CPU VR Settings  ->  **PSYS Prefix** (oneof)
- VarStore: CpuSetup @ offset 0x12A | QuestionId 0x11B | size 8
- options: 
- help: Sets the offset value as positive or negative.

## Form 0x13B7: CPU VR Settings  ->  **PSYS PMax Power** (numeric)
- VarStore: CpuSetup @ offset 0x12B | QuestionId 0x11C | size 16
- min 0x0 max 0x1FFF
- help: Psys Pmax power, defined in 1/8 Watt or 1/8 Percent increments. For Watts, range is 0-8191 (ex. For 125W, enter 1000). For ATX12VO Percent, Range is 0-1600 (ex. For recommended value of 200%, enter 1600). Uses BIOS VR mailbox command 0xB.

## Form 0x13B7: CPU VR Settings  ->  **VccIn Aux IMON Slope** (numeric)
- VarStore: CpuSetup @ offset 0x2EA | QuestionId 0x121 | size 16
- min 0x0 max 0xC8
- help: VccIN Aux IMON Slope defined in 1/100 increments. Range is 0-200. For a 1.25 slope, enter 125. 0 = AUTO. Uses BIOS VR mailbox command 0x18.

## Form 0x13B7: CPU VR Settings  ->  **VccIN Aux IMON Offset** (numeric)
- VarStore: CpuSetup @ offset 0x2EC | QuestionId 0x122 | size 16
- min 0x0 max 0xF9FF
- help: VccIN Aux IMON Offset defined in 1/1000 increments. Range is 0-63999. For an offset of 25.348, enter 25348. IMON Uses BIOS VR mailbox command 0x18.

## Form 0x13B7: CPU VR Settings  ->  **VccIN Aux IMON Prefix** (oneof)
- VarStore: CpuSetup @ offset 0x2EE | QuestionId 0x123 | size 8
- options: 
- help: Sets the offset value as positive or negative.

## Form 0x13B7: CPU VR Settings  ->  **Vsys/Psys Critical** (oneof)
- VarStore: CpuSetup @ offset 0x2EF | QuestionId 0x124 | size 8
- options: 
- help: Vsys/Psys Critical Enable or disable

## Form 0x13B7: CPU VR Settings  ->  **Vsys/Psys Full Scale** (numeric)
- VarStore: CpuSetup @ offset 0x38D | QuestionId 0x125 | size 32
- min 0x0 max 0x3E418
- help: Input Vsys or Psys Full-Scale and Critical Threshold to program Vsys/Psys Critical (0x4A) register. Critical Limit Trigger = (Critical Threshold/Full-Scale) * 0xFF. Input for Vsys is in Milli-Volts. For Psys either in Milli-Watts or Milli-Percent. For ATX12VO systems, recommended value is 200000.

## Form 0x13B7: CPU VR Settings  ->  **Vsys/Psys Critical Threshold** (numeric)
- VarStore: CpuSetup @ offset 0x391 | QuestionId 0x126 | size 32
- min 0x0 max 0x3E418
- help: Input Vsys or Psys Full-Scale and Critical Threshold to program Vsys/Psys Critical (0x4A) register. Critical Limit Trigger = (Critical Threshold/Full-Scale) * 0xFF. Input for Vsys is in Milli-Volts. For Psys either in Milli-Watts or Milli-Percent. For ATX12VO systems, recommended value is 120000.

## Form 0x13B7: CPU VR Settings  ->  **Vsys/Psys Full Scale** (numeric)
- VarStore: CpuSetup @ offset 0x385 | QuestionId 0x127 | size 32
- min 0x0 max 0x3E418
- help: Input Vsys or Psys Full-Scale and Critical Threshold to program Vsys/Psys Critical (0x4A) register. Critical Limit Trigger = (Critical Threshold/Full-Scale) * 0xFF. Input for Vsys is in Milli-Volts. For Psys either in Milli-Watts or Milli-Percent. For ATX12VO systems, recommended value is 200000.

## Form 0x13B7: CPU VR Settings  ->  **Vsys/Psys Critical Threshold** (numeric)
- VarStore: CpuSetup @ offset 0x389 | QuestionId 0x128 | size 32
- min 0x0 max 0x3E418
- help: Input Vsys or Psys Full-Scale and Critical Threshold to program Vsys/Psys Critical (0x4A) register. Critical Limit Trigger = (Critical Threshold/Full-Scale) * 0xFF. Input for Vsys is in Milli-Volts. For Psys either in Milli-Watts or Milli-Percent. For ATX12VO systems, recommended value is 120000.

## Form 0x13B9: Core/IA VR Settings  ->  **IMON Slope** (numeric)
- VarStore: CpuSetup @ offset 0x16E | QuestionId 0x143 | size 16
- min 0x0 max 0xC8
- help: IMON Slope defined in 1/100 increments. Range is 0-200. For a 1.25 slope, enter 125. 0 = AUTO. Uses BIOS VR mailbox command 0x4.

## Form 0x13B9: Core/IA VR Settings  ->  **IMON Offset** (numeric)
- VarStore: CpuSetup @ offset 0x178 | QuestionId 0x144 | size 16
- min 0x0 max 0xF9FF
- help: IMON Offset defined in 1/1000 increments. Range is 0-63999. For an offset of 25.348, enter 25348. IMON Uses BIOS VR mailbox command 0x4.

## Form 0x13B9: Core/IA VR Settings  ->  **IMON Prefix** (oneof)
- VarStore: CpuSetup @ offset 0x182 | QuestionId 0x145 | size 8
- options: 
- help: Sets the offset value as positive or negative.

## Form 0x13BC: GT VR Settings  ->  **IMON Slope** (numeric)
- VarStore: CpuSetup @ offset 0x170 | QuestionId 0x156 | size 16
- min 0x0 max 0xC8
- help: IMON Slope defined in 1/100 increments. Range is 0-200. For a 1.25 slope, enter 125. 0 = AUTO. Uses BIOS VR mailbox command 0x4.

## Form 0x13BC: GT VR Settings  ->  **IMON Offset** (numeric)
- VarStore: CpuSetup @ offset 0x17A | QuestionId 0x157 | size 16
- min 0x0 max 0xF9FF
- help: IMON Offset defined in 1/1000 increments. Range is 0-63999. For an offset of 25.348, enter 25348. IMON Uses BIOS VR mailbox command 0x4.

## Form 0x13BC: GT VR Settings  ->  **IMON Prefix** (oneof)
- VarStore: CpuSetup @ offset 0x183 | QuestionId 0x158 | size 8
- options: 
- help: Sets the offset value as positive or negative.

## Form 0x13B8: SA VR Settings  ->  **IMON Slope** (numeric)
- VarStore: CpuSetup @ offset 0x172 | QuestionId 0x168 | size 16
- min 0x0 max 0xC8
- help: IMON Slope defined in 1/100 increments. Range is 0-200. For a 1.25 slope, enter 125. 0 = AUTO. Uses BIOS VR mailbox command 0x4.

## Form 0x13B8: SA VR Settings  ->  **IMON Offset** (numeric)
- VarStore: CpuSetup @ offset 0x17C | QuestionId 0x169 | size 16
- min 0x0 max 0xF9FF
- help: IMON Offset defined in 1/1000 increments. Range is 0-63999. For an offset of 25.348, enter 25348. IMON Uses BIOS VR mailbox command 0x4.

## Form 0x13B8: SA VR Settings  ->  **IMON Prefix** (oneof)
- VarStore: CpuSetup @ offset 0x184 | QuestionId 0x16A | size 8
- options: 
- help: Sets the offset value as positive or negative.

## Form 0x1111: Power Limit 3 Settings  ->  **Power Limit 3 Override** (oneof)
- VarStore: CpuSetup @ offset 0x22 | QuestionId 0x173 | size 8
- options: 
- help: Enable/DisablePower Limit 3 override. If this option is disabled, BIOS will leave the hardware default values for Power Limit 3 and Power Limit 3 Time Window.

## Form 0x1111: Power Limit 3 Settings  ->  **Power Limit 3** (numeric)
- VarStore: CpuSetup @ offset 0x23 | QuestionId 0x174 | size 32
- min 0x0 max 0x3E7F83
- help: Platform Power Limit 3 Power in Milli Watts / Milli Percent. BIOS will round to the nearest 1/8W or 1/8% when programming. For example if 12%, enter 12000, if 50%, enter 50000.  For all SKUs, limit must be less than Psys Pmax value (either in Watts or %). XE SKU: Any value up through Psys Pmax can be programmed. Overclocking SKU: value must be between Max and Min Power Limits (specified by PACKAGE_POWER_SKU_MSR). Other SKUs: This value must be between Min Power Limit and Processor Base Power (TDP). If the value is '0', will default to hardware default value. Recommended value is 100000 if Psys is in %.

## Form 0x1111: Power Limit 3 Settings  ->  **Power Limit 3 Time Window** (oneof)
- VarStore: CpuSetup @ offset 0x27 | QuestionId 0x175 | size 8
- options: 
- help: Power Limit 3 Time Window value in Milli seconds. The value may vary from 3 to 64(max). Indicates the time window over which Power Limit 3 value should be maintained. If the value is 0, BIOS leaves the hardware default value. For ATX12VO PSU systems, recommended value is 40.

## Form 0x1111: Power Limit 3 Settings  ->  **Power Limit 3 Duty Cycle** (numeric)
- VarStore: CpuSetup @ offset 0x28 | QuestionId 0x176 | size 8
- min 0x0 max 0x64
- help: Specify the duty cycle in percentage that the CPU is required to maintain over the configured time window. Range is 0-100. For ATX12VO PSU systems, recommended value is 25.

## Form 0x1111: Power Limit 3 Settings  ->  **Response Mode** (oneof)
- VarStore: CpuSetup @ offset 0x383 | QuestionId 0x177 | size 8
- options: 
- help: Use Response Mode to adjust Psys_PL3 power reduction behavior. Battery-enabled systems use Gradual power reduction.

## Form 0x1111: Power Limit 3 Settings  ->  **Power Limit 3 Lock** (oneof)
- VarStore: CpuSetup @ offset 0x29 | QuestionId 0x178 | size 8
- options: 
- help: Power Limit 3 MSR 615h Lock. When enabled PL3 configurations are locked during OS. When disabled PL3 configuration can be changed during OS.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 1** (numeric)
- VarStore: CpuSetup @ offset 0x5B | QuestionId 0x17D | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 1 in Milli Watts. BIOS will round to the nearest 1/8W when programming. 0 = no custom override. For 12.50W, enter 12500. Overclocking SKU: Value must be between Max and Min Power Limits (specified by PACKAGE_POWER_SKU_MSR). Other SKUs: This value must be between Min Power Limit and Processor Base Power (TDP) Limit.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 2** (numeric)
- VarStore: CpuSetup @ offset 0x5F | QuestionId 0x17E | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 2 value in Milli Watts. BIOS will round to the nearest 1/8W when programming. 0 = no custom override. For 12.50W, enter 12500. Processor applies control policies such that the package power does not exceed this limit.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 1 Time Window** (oneof)
- VarStore: CpuSetup @ offset 0x63 | QuestionId 0x17F | size 8
- options: 
- help: Power Limit 1 Time Window value in seconds. The value may vary from 0 to 128. 0 = default value. Defines time window which Processor Base Power (TDP) value should be maintained.

## Form 0x10E9:   Config TDP Configurations  ->  **ConfigTDP Turbo Activation Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x64 | QuestionId 0x180 | size 8
- min 0x0 max 0xFF
- help: Custom value for Turbo Activation Ratio. Needs to be configured with valid values from LFM to Max Turbo. 0 means don't use custom value.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 1** (numeric)
- VarStore: CpuSetup @ offset 0x65 | QuestionId 0x181 | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 1 in Milli Watts. BIOS will round to the nearest 1/8W when programming. 0 = no custom override. For 12.50W, enter 12500. Overclocking SKU: Value must be between Max and Min Power Limits (specified by PACKAGE_POWER_SKU_MSR). Other SKUs: This value must be between Min Power Limit and Processor Base Power (TDP) Limit.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 2** (numeric)
- VarStore: CpuSetup @ offset 0x69 | QuestionId 0x182 | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 2 value in Milli Watts. BIOS will round to the nearest 1/8W when programming. 0 = no custom override. For 12.50W, enter 12500. Processor applies control policies such that the package power does not exceed this limit.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 1 Time Window** (oneof)
- VarStore: CpuSetup @ offset 0x6D | QuestionId 0x183 | size 8
- options: 
- help: Power Limit 1 Time Window value in seconds. The value may vary from 0 to 128. 0 = default value. Defines time window which Processor Base Power (TDP) value should be maintained.

## Form 0x10E9:   Config TDP Configurations  ->  **ConfigTDP Turbo Activation Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x6E | QuestionId 0x184 | size 8
- min 0x0 max 0xFF
- help: Custom value for Turbo Activation Ratio. Needs to be configured with valid values from LFM to Max Turbo. 0 means don't use custom value.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 1** (numeric)
- VarStore: CpuSetup @ offset 0x6F | QuestionId 0x185 | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 1 in Milli Watts. BIOS will round to the nearest 1/8W when programming. 0 = no custom override. For 12.50W, enter 12500. Overclocking SKU: Value must be between Max and Min Power Limits (specified by PACKAGE_POWER_SKU_MSR). Other SKUs: This value must be between Min Power Limit and Processor Base Power (TDP) Limit.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 2** (numeric)
- VarStore: CpuSetup @ offset 0x73 | QuestionId 0x186 | size 32
- min 0x0 max 0x3E7F83
- help: Power Limit 2 value in Milli Watts. BIOS will round to the nearest 1/8W when programming. 0 = no custom override. For 12.50W, enter 12500. Processor applies control policies such that the package power does not exceed this limit.

## Form 0x10E9:   Config TDP Configurations  ->  **Power Limit 1 Time Window** (oneof)
- VarStore: CpuSetup @ offset 0x77 | QuestionId 0x187 | size 8
- options: 
- help: Power Limit 1 Time Window value in seconds. The value may vary from 0 to 128. 0 = default value. Defines time window which Processor Base Power (TDP) value should be maintained.

## Form 0x10E9:   Config TDP Configurations  ->  **ConfigTDP Turbo Activation Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x78 | QuestionId 0x188 | size 8
- min 0x0 max 0xFF
- help: Custom value for Turbo Activation Ratio. Needs to be configured with valid values from LFM to Max Turbo. 0 means don't use custom value.

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR Power Limit 2400 Chain A** (numeric)
- VarStore: Setup @ offset 0xBAA | QuestionId 0x2C4 | size 8
- min 0x0 max 0xFF
- help: Bluetooth SAR power restriction for the Lower Band (LB) - 2400MHz frequency Chain A. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x1016: E-core L2 Configurations  ->  **E-core L2 Extra Turbo Voltage** (numeric)
- VarStore: CpuSetup @ offset 0x2B5 | QuestionId 0x35D | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while Efficient-core L2 is operating in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range 0-2000 mV

## Form 0x1101: Ring  ->  **Ring Extra Turbo Voltage** (numeric)
- VarStore: CpuSetup @ offset 0x1EF | QuestionId 0x363 | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while ring is operating in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range 0-2000 mV

## Form 0x101B: GT  ->  **GT Extra Turbo Voltage** (numeric)
- VarStore: SaSetup @ offset 0x269 | QuestionId 0x388 | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while GT is operating in turbo mode. Unit is in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV

## Form 0x101B: GT  ->  **GT Extra Turbo Voltage** (numeric)
- VarStore: SaSetup @ offset 0x272 | QuestionId 0x38E | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while GT is operating in turbo mode. Unit is in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV

## Form 0x1102: Uncore  ->  **Uncore Extra Turbo Voltage** (numeric)
- VarStore: CpuSetup @ offset 0x2E1 | QuestionId 0x393 | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while SA Uncore is operating in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range 0-2000 mV

## Form 0x102A: Graphics Configuration  ->  **Graphics Turbo IMON Current** (numeric)
- VarStore: SaSetup @ offset 0xB8 | QuestionId 0x487 | size 8
- min 0xE max 0x1F
- help: Graphics turbo IMON current values supported (14-31)

## Form 0x102E: GT - Power Management Control  ->  **Disable Turbo GT frequency** (oneof)
- VarStore: SaSetup @ offset 0x40 | QuestionId 0x4FF | size 8
- options: 
- help: Enabled: Disables Turbo GT frequency. Disabled: GT frequency is not limited

## Form 0x10E4: Memory Training Algorithms  ->  **Post Package Repair Training** (oneof)
- VarStore: SaSetup @ offset 0x47F | QuestionId 0x534 | size 8
- options: 
- help: Post Package Repair Training

