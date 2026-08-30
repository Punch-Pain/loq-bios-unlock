# Power / Thermal / GPU-relevant Settings (flagged from Advanced FormSet)

Total flagged leaf controls: 673

## Form 0x21: Boot Configuration  ->  **Numlock** (oneof)
- VarStore: SystemConfig @ offset 0x8 | QuestionId 0x17 | size 8
- options: 
- help: Selects Power-on state for Numlock

## Form 0x27: Chipset Configuration  ->  **Hg Slot** (oneof)
- VarStore: SystemConfig @ offset 0x1AC | QuestionId 0x28 | size 8
- options: 
- help: PEG or PCH Slot Slection for Hybrid Graphics

## Form 0x1006: Debug Settings  ->  **Serial Io Uart Debug Power Gating** (oneof)
- VarStore: PchSetup @ offset 0x786 | QuestionId 0x2D | size 8
- options: 
- help: For S0iX support with Kernel Debugger Enabled. BIOS needs to change DBG2 Port Sub Type as value of 0x14 (0x0014 Intel LPSS) Note: Requires OS support

## Form 0x1006: Debug Settings  ->  **Platform Debug Consent** (oneof)
- VarStore: SiSetup @ offset 0x1 | QuestionId 0x1007 | size 8
- options: 
- help: Enabled(All Probes+TraceHub) supports all probes with TraceHub enabled and blocks s0ix  Enabled(Low Power) Tracehub is powergated by default, s0ix is viable  Manual:user needs to configure Advanced Debug Settings manually, aimed at advanced users

## Form 0x1056: Advanced Debug Settings  ->  **USB Overcurrent Override for VISA** (oneof)
- VarStore: PchSetup @ offset 0xB | QuestionId 0x3F | size 8
- options: 
- help: This option overrides USB Over Current enablement state that USB OC will be disabled after enabling this option. Enable when VISA pin is muxed with USB OC

## Form 0x1056: Advanced Debug Settings  ->  **JTAG C10 Power Gate** (oneof)
- VarStore: CpuSetup @ offset 0x8 | QuestionId 0x43 | size 8
- options: 
- help: When Enabled, JTAG is power gated in C10 state. When Disabled, keeps the JTAG power up during C10 and deeper power states for debug purpose.

## Form 0x100A: ACPI Settings  ->  **Native PCIE Enable** (oneof)
- VarStore: Setup @ offset 0x11 | QuestionId 0x56 | size 8
- options: 
- help: Bit - PCIe Native * control  0 - ~ Hot Plug  1 - SHPC Native Hot Plug control  2 - ~ Power Management Events  3 - PCIe Advanced Error Reporting control  4 - PCIe Capability Structure control  5 - Latency Tolerance Reporting control

## Form 0x100A: ACPI Settings  ->  **Low Power S0 Idle Capability** (oneof)
- VarStore: Setup @ offset 0x1C | QuestionId 0x111D | size 8
- options: 
- help: This variable determines if we enable ACPI Lower Power S0 Idle Capability (Mutually exclusive with Smart connect). While this is enabled, it also disable 8254 timer for SLP_S0 support.

## Form 0x100A: ACPI Settings  ->  **PUIS Enable** (oneof)
- VarStore: Setup @ offset 0x84F | QuestionId 0x5C | size 8
- options: 
- help: Enable/Disable Power-Up In Standby (PUIS) feature set allows devices to be powered-up into the Standby power management state to minimize inrush current at power-up and to allow the host to sequence the spin-up of devices.

## Form 0x100A: ACPI Settings  ->  **EC Notification** (oneof)
- VarStore: Setup @ offset 0x31 | QuestionId 0x5D | size 8
- options: 
- help: Sends EC notification of Low Power S0 Idle State

## Form 0x100A: ACPI Settings  ->  **EC CS Debug Light** (oneof)
- VarStore: Setup @ offset 0x32 | QuestionId 0x1395 | size 8
- options: 
- help: When EC enters Low Power S0 Idle State, the CAPS LOCK light will be turned on

## Form 0x100A: ACPI Settings  ->  **EC Low Power Mode** (oneof)
- VarStore: Setup @ offset 0x33 | QuestionId 0x5E | size 8
- options: 
- help: This option controls whether EC will go to Low power mode during Low Power S0 Idle State

## Form 0x100A: ACPI Settings  ->  **CS PL1 Limit** (oneof)
- VarStore: Setup @ offset 0x39 | QuestionId 0x60 | size 8
- options: 
- help: Limit PL1 (Power Limit 1) while in Connected Standby

## Form 0x100A: ACPI Settings  ->  **CS PL1 Value** (numeric)
- VarStore: Setup @ offset 0x3A | QuestionId 0x61 | size 16
- min 0xBB8 max 0x4E20
- help: PL1 value is in milliwatts with 125 step value

## Form 0x100D: CPU Configuration  ->  **CPU Flex Ratio Settings** (numeric)
- VarStore: CpuSetup @ offset 0x1 | QuestionId 0x10E1 | size 8
- min 0x0 max 0x3F
- help: This value must be between Max Efficiency Ratio (LFM) and Maximum non-turbo ratio set by Hardware (HFM).

## Form 0x100D: CPU Configuration  ->  **Active Performance-cores** (oneof)
- VarStore: CpuSetup @ offset 0x6 | QuestionId 0x8D | size 8
- options: 
- help: Number of P-cores to enable in each processor package. Note: Number of Cores and E-cores are looked at together. When both are {0,0}, Pcode will enable all cores.

## Form 0x100D: CPU Configuration  ->  **Active Efficient-cores** (oneof)
- VarStore: CpuSetup @ offset 0x22F | QuestionId 0x8E | size 8
- options: 
- help: Number of E-cores to enable in each processor package. Note: Number of Cores and E-cores are looked at together. When both are {0,0}, Pcode will enable all cores.

## Form 0x100D: CPU Configuration  ->  **Intel Trusted Execution Technology** (oneof)
- VarStore: CpuSetup @ offset 0xC1 | QuestionId 0x1549 | size 8
- options: 
- help: Enables utilization of additional hardware capabilities provided by Intel (R) Trusted Execution Technology.  Changes require a full power cycle to take effect.

## Form 0x100D: CPU Configuration  ->  **FCLK Frequency for Early Power On** (oneof)
- VarStore: CpuSetup @ offset 0x126 | QuestionId 0x99 | size 8
- options: 
- help: FCLK frequency can take values of 400MHz, 800MHz  and 1GHz (1GHz not supported for ULT/ULX SKUs)

## Form 0x100F: CPU - Power Management Control  ->  **Race To Halt (RTH)** (oneof)
- VarStore: CpuSetup @ offset 0xA | QuestionId 0xA2 | size 8
- options: 
- help: Enable/Disable Race To Halt feature. RTH will dynamically increase CPU frequency in order to enter pkg C-State faster to reduce overall power. (RTH is controlled through MSR 1FC bit 20)

## Form 0x100F: CPU - Power Management Control  ->  **Intel(R) Turbo Boost Max Technology 3.0** (oneof)
- VarStore: CpuSetup @ offset 0xC | QuestionId 0x1409 | size 8
- options: 
- help: Enable/Disable Intel(R) Turbo Boost Max Technology 3.0 support. Disabling will report the maximum ratio of the slowest core in _CPC object.

## Form 0x100F: CPU - Power Management Control  ->  **HwP Lock** (oneof)
- VarStore: CpuSetup @ offset 0x228 | QuestionId 0xA8 | size 8
- options: 
- help: Enable/Disable HWP Lock support in Misc Power Management MSR.

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

## Form 0x100F: CPU - Power Management Control  ->  **Enhanced C-states** (oneof)
- VarStore: CpuSetup @ offset 0x15 | QuestionId 0xB6 | size 8
- options: 
- help: Enable/Disable C1E. When enabled, CPU will switch to minimum speed when all cores enter C-State.

## Form 0x100F: CPU - Power Management Control  ->  **C states** (oneof)
- VarStore: CpuSetup @ offset 0x14 | QuestionId 0x1406 | size 8
- options: 
- help: Enable/Disable CPU Power Management. Allows CPU to go to C states when it's not 100% utilized.

## Form 0x100F: CPU - Power Management Control  ->  **C-State Auto Demotion** (oneof)
- VarStore: CpuSetup @ offset 0x3E | QuestionId 0xB7 | size 8
- options: 
- help: Configure C-State Auto Demotion

## Form 0x100F: CPU - Power Management Control  ->  **C-State Un-demotion** (oneof)
- VarStore: CpuSetup @ offset 0x3F | QuestionId 0xB8 | size 8
- options: 
- help: Configure C-State Un-demotion

## Form 0x100F: CPU - Power Management Control  ->  **Package C-State Demotion** (oneof)
- VarStore: CpuSetup @ offset 0x40 | QuestionId 0xB9 | size 8
- options: 
- help: Package C-State Demotion

## Form 0x100F: CPU - Power Management Control  ->  **Package C-State Un-demotion** (oneof)
- VarStore: CpuSetup @ offset 0x41 | QuestionId 0xBA | size 8
- options: 
- help: Package C-State Un-demotion

## Form 0x100F: CPU - Power Management Control  ->  **CState Pre-Wake** (oneof)
- VarStore: CpuSetup @ offset 0x3D | QuestionId 0xBB | size 8
- options: 
- help: Disable - Sets bit 30 of POWER_CTL MSR(0x1FC) to 1 to disable the Cstate Pre-Wake

## Form 0x100F: CPU - Power Management Control  ->  **Package C State Limit** (oneof)
- VarStore: CpuSetup @ offset 0x4B | QuestionId 0xBD | size 8
- options: 
- help: Maximum Package C State Limit Setting. Cpu Default: Leaves to Factory default value.Auto: Initializes to deepest available Package C State Limit.

## Form 0x100F: CPU - Power Management Control  ->  **Thermal Monitor** (oneof)
- VarStore: CpuSetup @ offset 0x42 | QuestionId 0xC8 | size 8
- options: 
- help: Enable/Disable Thermal Monitor

## Form 0x100F: CPU - Power Management Control  ->  **EC Turbo Control Mode** (oneof)
- VarStore: CpuSetup @ offset 0xC7 | QuestionId 0xCC | size 8
- options: 
- help: Enable/Disable EC Turbo Control mode

## Form 0x100F: CPU - Power Management Control  ->  **EC Polling Period** (numeric)
- VarStore: CpuSetup @ offset 0xC9 | QuestionId 0xCE | size 8
- min 0x1 max 0xFF
- help: Count 1 to 255 for a range of 10ms to 2.55 seconds (1 count = 10ms)

## Form 0x100F: CPU - Power Management Control  ->  **EC Guard Band Value** (numeric)
- VarStore: CpuSetup @ offset 0xCA | QuestionId 0xCF | size 8
- min 0x0 max 0x14
- help: Count 1 to 20 for a range of 1 watt to 20 watts

## Form 0x100F: CPU - Power Management Control  ->  **EC Algorithm Selection** (numeric)
- VarStore: CpuSetup @ offset 0xCB | QuestionId 0xD0 | size 8
- min 0x1 max 0xA
- help: Count 1 to 10 for Algorithm Selection

## Form 0x100F: CPU - Power Management Control  ->  **EPG DIMM Idd3N** (numeric)
- VarStore: SaSetup @ offset 0x76 | QuestionId 0xD2 | size 16
- min 0x0 max 0x7D0
- help: Active standby current (Idd3N) in milliamps from datasheet. Must be calculated on a per DIMM basis.

## Form 0x100F: CPU - Power Management Control  ->  **EPG DIMM Idd3P** (numeric)
- VarStore: SaSetup @ offset 0x78 | QuestionId 0xD3 | size 16
- min 0x0 max 0x7D0
- help: Active power-down current (Idd3P) in milliamps from datasheet. Must be calculated on a per DIMM basis.

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

## Form 0x13B7: CPU VR Settings  ->  **Min Voltage Override** (oneof)
- VarStore: CpuSetup @ offset 0x207 | QuestionId 0x11D | size 8
- options: 
- help: Min Voltage Override. Enable to override minimum voltage for runtime and for C8.

## Form 0x13B7: CPU VR Settings  ->  **Min Voltage Runtime** (numeric)
- VarStore: CpuSetup @ offset 0x208 | QuestionId 0x11E | size 16
- min 0x0 max 0x7CF
- help: Min Voltage for Runtime. Range is 0 - 1999mV in 1/128 volt increments. Input is in mVolts.

## Form 0x13B7: CPU VR Settings  ->  **Min Voltage C8** (numeric)
- VarStore: CpuSetup @ offset 0x20A | QuestionId 0x11F | size 16
- min 0x0 max 0x7CF
- help: Min Voltage for Package C8. Range is 0 - 1999mV in 1/128 volt increments. Input is in mVolts.

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

## Form 0x13B7: CPU VR Settings  ->  **VR Power Delivery Design** (oneof)
- VarStore: CpuSetup @ offset 0x313 | QuestionId 0x10C2 | size 8
- options: 
- help: Specifies the ADL Desktop board design used for the VR settings override values. By default, BIOS will override the default Desktop VR settings based on the board design. A value of AUTO(0) will use the board ID to determine the board design. Any other value will override the board id logic to provide a custom VR Power Delivery Design value. This is intended primarily for validation.

## Form 0x13BA: Acoustic Noise Settings  ->  **Acoustic Noise Mitigation** (oneof)
- VarStore: CpuSetup @ offset 0x1FC | QuestionId 0x132 | size 8
- options: 
- help: Enabling this option will help mitigate acoustic noise on certain SKUs when the CPU is in deeper C state

## Form 0x13BA: Acoustic Noise Settings  ->  **Disable Fast PKG C State Ramp for IA Domain** (oneof)
- VarStore: CpuSetup @ offset 0x1FD | QuestionId 0x136 | size 8
- options: 
- help: This option needs to be configured to reduce acoustic noise during deeper C states. False: Don't disable Fast ramp during deeper C states; True: Disable Fast ramp during deeper C state

## Form 0x13BA: Acoustic Noise Settings  ->  **Slow Slew Rate for IA Domain** (oneof)
- VarStore: CpuSetup @ offset 0x202 | QuestionId 0x137 | size 8
- options: 
- help: Set VR IA Slow Slew Rate for Deep Package C State ramp time; Slow slew rate equals to Fast divided by number, the number is 2, 4, 8, 16 to slow down the slew rate to help minimize acoustic noise

## Form 0x13BA: Acoustic Noise Settings  ->  **Disable Fast PKG C State Ramp for GT Domain** (oneof)
- VarStore: CpuSetup @ offset 0x1FE | QuestionId 0x138 | size 8
- options: 
- help: This option needs to be configured to reduce acoustic noise during deeper C states. False: Don't disable Fast ramp during deeper C states; True: Disable Fast ramp during deeper C state

## Form 0x13BA: Acoustic Noise Settings  ->  **Slow Slew Rate for GT Domain** (oneof)
- VarStore: CpuSetup @ offset 0x203 | QuestionId 0x139 | size 8
- options: 
- help: Set VR GT Slow Slew Rate for Deep Package C State ramp time; Slow slew rate equals to Fast divided by number, the number is 2, 4, 8 to slow down the slew rate to help minimize acoustic noise; divide by 16 is disabled

## Form 0x13BA: Acoustic Noise Settings  ->  **Disable Fast PKG C State Ramp for SA Domain** (oneof)
- VarStore: CpuSetup @ offset 0x1FF | QuestionId 0x13A | size 8
- options: 
- help: This option needs to be configured to reduce acoustic noise during deeper C states. False: Don't disable Fast ramp during deeper C states; True: Disable Fast ramp during deeper C state

## Form 0x13B9: Core/IA VR Settings  ->  **VR Config Enable** (oneof)
- VarStore: CpuSetup @ offset 0x12D | QuestionId 0x13B | size 8
- options: 
- help: VR Config Enable

## Form 0x13B9: Core/IA VR Settings  ->  **PS Current Threshold1** (numeric)
- VarStore: CpuSetup @ offset 0x146 | QuestionId 0x13E | size 16
- min 0x0 max 0x200
- help: PS Current Threshold1, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13B9: Core/IA VR Settings  ->  **PS Current Threshold2** (numeric)
- VarStore: CpuSetup @ offset 0x150 | QuestionId 0x13F | size 16
- min 0x0 max 0x200
- help: PS Current Threshold2, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13B9: Core/IA VR Settings  ->  **PS Current Threshold3** (numeric)
- VarStore: CpuSetup @ offset 0x15A | QuestionId 0x140 | size 16
- min 0x0 max 0x200
- help: PS Current Threshold3, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13B9: Core/IA VR Settings  ->  **PS3 Enable** (oneof)
- VarStore: CpuSetup @ offset 0x164 | QuestionId 0x141 | size 8
- options: 
- help: PS3 Enable/Disable. 0 - Disabled, 1 - Enabled.Uses BIOS VR mailbox command 0x3.

## Form 0x13B9: Core/IA VR Settings  ->  **PS4 Enable** (oneof)
- VarStore: CpuSetup @ offset 0x169 | QuestionId 0x142 | size 8
- options: 
- help: PS4 Enable/Disable. 0 - Disabled, 1 - Enabled. Uses BIOS VR mailbox command 0x3

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

## Form 0x13B9: Core/IA VR Settings  ->  **VR Current Limit** (numeric)
- VarStore: CpuSetup @ offset 0x187 | QuestionId 0x146 | size 16
- min 0x0 max 0x800
- help: Voltage Regulator Current Limit (IccMax). This value represents the Maximum instantaneous current allowed at any given time. The value is represented in 1/4 A increments. A value of 400 = 100A. 0 means AUTO. Uses BIOS VR mailbox command 0x6.

## Form 0x13B9: Core/IA VR Settings  ->  **Core VR Fast Vmode** (oneof)
- VarStore: CpuSetup @ offset 0x379 | QuestionId 0x10C3 | size 8
- options: 
- help: Core VR Fast Vmode. Use to control Core Fast Vmode Enable/Disable. The value will only be effective by enabling the corresponding CEP..

## Form 0x13B9: Core/IA VR Settings  ->  **Fast Vmode Itrip ICC Limit** (numeric)
- VarStore: CpuSetup @ offset 0x32A | QuestionId 0x10C6 | size 16
- min 0x0 max 0x7F8
- help: Voltage Regulator Fast Vmode Itrip ICC Limit. A value of 400 = 100A. A value of 0 corresponds to feature disabled (no reactive protection). This value represents the current threshold where the VR would initiate reactive protection if Fast Vmode is enabled. The value is represented in 1/4 A increments. Uses BIOS VR mailbox command 0x25.

## Form 0x13B9: Core/IA VR Settings  ->  **Core CEP Enable** (oneof)
- VarStore: CpuSetup @ offset 0x396 | QuestionId 0x147 | size 8
- options: 
- help: Enable/Disable the IA Core CEP (Current Excursion Protection) Support. BIOS doesn't allow to enable FVM when CEP disabled

## Form 0x13B9: Core/IA VR Settings  ->  **VR Voltage Limit** (numeric)
- VarStore: CpuSetup @ offset 0x1BE | QuestionId 0x148 | size 16
- min 0x0 max 0x1F3F
- help: Voltage Limit (VMAX). This value represents the Maximum instantaneous voltage allowed at any given time. Range is 0 - 7999mV. Uses BIOS VR mailbox command 0x8.

## Form 0x13B9: Core/IA VR Settings  ->  **TDC Current Limit** (numeric)
- VarStore: CpuSetup @ offset 0x191 | QuestionId 0x14A | size 16
- min 0x0 max 0x7FFF
- help: TDC Current Limit, defined in 1/8A increments. Range 0-32767. For a TDC Current Limit of 125A, enter 1000. 0 = 0 Amps. Uses BIOS VR mailbox command 0x1A.

## Form 0x13B9: Core/IA VR Settings  ->  **TDC Time Window** (oneof)
- VarStore: CpuSetup @ offset 0x1A0 | QuestionId 0x14B | size 32
- options: 
- help: VR TDC Time Window, value in seconds. 1s is default. Range from 1s to 448s.

## Form 0x13B9: Core/IA VR Settings  ->  **IRMS** (oneof)
- VarStore: CpuSetup @ offset 0x1B9 | QuestionId 0x14D | size 8
- options: 
- help: Enable/Disable IRMS - Current root mean square

## Form 0x13BC: GT VR Settings  ->  **VR Config Enable** (oneof)
- VarStore: CpuSetup @ offset 0x12E | QuestionId 0x14E | size 8
- options: 
- help: VR Config Enable

## Form 0x13BC: GT VR Settings  ->  **PS Current Threshold1** (numeric)
- VarStore: CpuSetup @ offset 0x148 | QuestionId 0x151 | size 16
- min 0x0 max 0x200
- help: PS Current Threshold1, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13BC: GT VR Settings  ->  **PS Current Threshold2** (numeric)
- VarStore: CpuSetup @ offset 0x152 | QuestionId 0x152 | size 16
- min 0x0 max 0x200
- help: PS Current Threshold2, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13BC: GT VR Settings  ->  **PS Current Threshold3** (numeric)
- VarStore: CpuSetup @ offset 0x15C | QuestionId 0x153 | size 16
- min 0x0 max 0x200
- help: PS Current Threshold3, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13BC: GT VR Settings  ->  **PS3 Enable** (oneof)
- VarStore: CpuSetup @ offset 0x165 | QuestionId 0x154 | size 8
- options: 
- help: PS3 Enable/Disable. 0 - Disabled, 1 - Enabled.Uses BIOS VR mailbox command 0x3.

## Form 0x13BC: GT VR Settings  ->  **PS4 Enable** (oneof)
- VarStore: CpuSetup @ offset 0x16A | QuestionId 0x155 | size 8
- options: 
- help: PS4 Enable/Disable. 0 - Disabled, 1 - Enabled. Uses BIOS VR mailbox command 0x3

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

## Form 0x13BC: GT VR Settings  ->  **VR Current Limit** (numeric)
- VarStore: CpuSetup @ offset 0x189 | QuestionId 0x159 | size 16
- min 0x0 max 0x800
- help: Voltage Regulator Current Limit (IccMax). This value represents the Maximum instantaneous current allowed at any given time. The value is represented in 1/4 A increments. A value of 400 = 100A. 0 means AUTO. Uses BIOS VR mailbox command 0x6.

## Form 0x13BC: GT VR Settings  ->  **GT VR Fast Vmode** (oneof)
- VarStore: CpuSetup @ offset 0x37A | QuestionId 0x10C4 | size 8
- options: 
- help: GT VR Fast Vmode. Use to control GT Fast Vmode Enable/Disable.

## Form 0x13BC: GT VR Settings  ->  **Fast Vmode Itrip ICC Limit** (numeric)
- VarStore: CpuSetup @ offset 0x32C | QuestionId 0x10C7 | size 16
- min 0x0 max 0x7F8
- help: Voltage Regulator Fast Vmode Itrip ICC Limit. A value of 400 = 100A. A value of 0 corresponds to feature disabled (no reactive protection). This value represents the current threshold where the VR would initiate reactive protection if Fast Vmode is enabled. The value is represented in 1/4 A increments. Uses BIOS VR mailbox command 0x25.

## Form 0x13BC: GT VR Settings  ->  **GT CEP Enable** (oneof)
- VarStore: CpuSetup @ offset 0x397 | QuestionId 0x15A | size 8
- options: 
- help: Enable/Disable the GT CEP (Current Excursion Protection) Support. BIOS doesn't allow to enable FVM when CEP disabled

## Form 0x13BC: GT VR Settings  ->  **VR Voltage Limit** (numeric)
- VarStore: CpuSetup @ offset 0x1C0 | QuestionId 0x15B | size 16
- min 0x0 max 0x1F3F
- help: Voltage Limit (VMAX). This value represents the Maximum instantaneous voltage allowed at any given time. Range is 0 - 7999mV. Uses BIOS VR mailbox command 0x8.

## Form 0x13BC: GT VR Settings  ->  **TDC Current Limit** (numeric)
- VarStore: CpuSetup @ offset 0x193 | QuestionId 0x15D | size 16
- min 0x0 max 0x7FFF
- help: TDC Current Limit, defined in 1/8A increments. Range 0-32767. For a TDC Current Limit of 125A, enter 1000. 0 = 0 Amps. Uses BIOS VR mailbox command 0x1A.

## Form 0x13BC: GT VR Settings  ->  **TDC Time Window** (oneof)
- VarStore: CpuSetup @ offset 0x1A4 | QuestionId 0x15E | size 32
- options: 
- help: VR TDC Time Window, value in seconds. 1s is default. Range from 1s to 448s.

## Form 0x13B8: SA VR Settings  ->  **VR Config Enable** (oneof)
- VarStore: CpuSetup @ offset 0x12F | QuestionId 0x160 | size 8
- options: 
- help: VR Config Enable

## Form 0x13B8: SA VR Settings  ->  **PS Current Threshold1** (numeric)
- VarStore: CpuSetup @ offset 0x14A | QuestionId 0x163 | size 16
- min 0x0 max 0x200
- help: PS Current Threshold1, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13B8: SA VR Settings  ->  **PS Current Threshold2** (numeric)
- VarStore: CpuSetup @ offset 0x154 | QuestionId 0x164 | size 16
- min 0x0 max 0x200
- help: PS Current Threshold2, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13B8: SA VR Settings  ->  **PS Current Threshold3** (numeric)
- VarStore: CpuSetup @ offset 0x15E | QuestionId 0x165 | size 16
- min 0x0 max 0x200
- help: PS Current Threshold3, defined in 1/4 A increments. A value of 400 = 100A. Range 0-512, which translates to 0-128A. 0 = AUTO. Uses BIOS VR mailbox command 0x3.

## Form 0x13B8: SA VR Settings  ->  **PS3 Enable** (oneof)
- VarStore: CpuSetup @ offset 0x166 | QuestionId 0x166 | size 8
- options: 
- help: PS3 Enable/Disable. 0 - Disabled, 1 - Enabled.Uses BIOS VR mailbox command 0x3.

## Form 0x13B8: SA VR Settings  ->  **PS4 Enable** (oneof)
- VarStore: CpuSetup @ offset 0x16B | QuestionId 0x167 | size 8
- options: 
- help: PS4 Enable/Disable. 0 - Disabled, 1 - Enabled. Uses BIOS VR mailbox command 0x3

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

## Form 0x13B8: SA VR Settings  ->  **VR Current Limit** (numeric)
- VarStore: CpuSetup @ offset 0x18B | QuestionId 0x16B | size 16
- min 0x0 max 0x800
- help: Voltage Regulator Current Limit (IccMax). This value represents the Maximum instantaneous current allowed at any given time. The value is represented in 1/4 A increments. A value of 400 = 100A. 0 means AUTO. Uses BIOS VR mailbox command 0x6.

## Form 0x13B8: SA VR Settings  ->  **SA VR Fast Vmode** (oneof)
- VarStore: CpuSetup @ offset 0x37B | QuestionId 0x10C5 | size 8
- options: 
- help: SA VR Fast Vmode. Use to control SA Fast Vmode Enable/Disable.

## Form 0x13B8: SA VR Settings  ->  **Fast Vmode Itrip ICC Limit** (numeric)
- VarStore: CpuSetup @ offset 0x32E | QuestionId 0x10C8 | size 16
- min 0x0 max 0x7F8
- help: Voltage Regulator Fast Vmode Itrip ICC Limit. A value of 400 = 100A. A value of 0 corresponds to feature disabled (no reactive protection). This value represents the current threshold where the VR would initiate reactive protection if Fast Vmode is enabled. The value is represented in 1/4 A increments. Uses BIOS VR mailbox command 0x25.

## Form 0x13B8: SA VR Settings  ->  **VR Voltage Limit** (numeric)
- VarStore: CpuSetup @ offset 0x1C2 | QuestionId 0x16C | size 16
- min 0x0 max 0x1F3F
- help: Voltage Limit (VMAX). This value represents the Maximum instantaneous voltage allowed at any given time. Range is 0 - 7999mV. Uses BIOS VR mailbox command 0x8.

## Form 0x1483: RFI Settings  ->  **FIVR Spread Spectrum** (oneof)
- VarStore: CpuSetup @ offset 0x2F6 | QuestionId 0x171 | size 8
- options: 
- help: Enable or Disable the FIVR Spread Spectrum

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

## Form 0x10E9:   Config TDP Configurations  ->  **Enable Configurable TDP** (oneof)
- VarStore: CpuSetup @ offset 0x227 | QuestionId 0x179 | size 8
- options: 
- help: Applies Configurable Processor Base Power (cTDP) initialization settings based on non-cTDP or cTDP. Default is 1: Applies to cTDP; if 0 then applies non-cTDP and BIOS will bypass cTDP initialzation flow

## Form 0x10E9:   Config TDP Configurations  ->  **Configurable TDP Boot Mode** (oneof)
- VarStore: CpuSetup @ offset 0x44 | QuestionId 0x17A | size 8
- options: 
- help: Configurable Processor Base Power (cTDP) Mode as Nominal/Level/Leve2/Deactivate TDP selection. Deactivate option will set MSR to Nominal and MMIO to Zero.

## Form 0x10E9:   Config TDP Configurations  ->  **Configurable TDP Lock** (oneof)
- VarStore: CpuSetup @ offset 0x45 | QuestionId 0x17B | size 8
- options: 
- help: Configurable Processor Base Power (cTDP) Mode Lock sets the Lock bits on TURBO_ACTIVATION_RATIO and CONFIG_TDP_CONTROL.                 Note: When CTDP Lock is enabled Custom ConfigTDP Count will be forced to 1 and Custom ConfigTDP Boot Index will be forced to 0.

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

## Form 0x1012:   View/Configure CPU Lock Options  ->  **Overclocking Lock** (oneof)
- VarStore: CpuSetup @ offset 0x10E | QuestionId 0x18A | size 8
- options: 
- help: Enable/Disable Overclocking Lock (BIT 20) in FLEX_RATIO(194) MSR

## Form 0x13D2: Connectivity Configuration  ->  **BT Audio Offload** (oneof)
- VarStore: PchSetup @ offset 0x737 | QuestionId 0x146E | size 8
- options: 
- help: This is an option to Enable/Disable BT Audio Offload which enables audio input from BT device to the audio DSP and enables power efficient audio output to BT device.

## Form 0x13D2: Connectivity Configuration  ->  **DLVR RFI Mitigation** (oneof)
- VarStore: Setup @ offset 0xBA8 | QuestionId 0x190 | size 8
- options: 
- help: This is an option intended to Enable/Disable DLVR RFIM feature for Connectivity This option is only valid when global DLVR is enabled.

## Form 0x13D2: Connectivity Configuration  ->  **Default Power Limit** (numeric)
- VarStore: Setup @ offset 0x71B | QuestionId 0x1538 | size 16
- min 0x1 max 0xFFFF
- help: Power Limit in milli watts

## Form 0x13D2: Connectivity Configuration  ->  **Country Identifier** (numeric)
- VarStore: Setup @ offset 0x726 | QuestionId 0x1A6 | size 16
- min 0x1 max 0xFFFF
- help: Country identifier as defined in ISO/IEC 3166-1 Alpha 2 code

## Form 0x13D2: Connectivity Configuration  ->  **WiFi SAR** (oneof)
- VarStore: Setup @ offset 0x72B | QuestionId 0x1AB | size 8
- options: 
- help: Enable/Disable WiFi SAR Tx Power Limit; DISABLE - Device ignores WiFi SAR Configuration Table; ENABLE - Device uses WiFi SAR Configuration Table

## Form 0x13D2: Connectivity Configuration  ->  **SAR 2400 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x72C | QuestionId 0x1AC | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5180-5320 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x72D | QuestionId 0x1AD | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5340-5440 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x72E | QuestionId 0x1AE | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5460-5700 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x72F | QuestionId 0x1AF | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5720-5825 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x730 | QuestionId 0x1B0 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5845-6135 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x731 | QuestionId 0x1B1 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6155-6375 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x732 | QuestionId 0x1B2 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6395-6495 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x733 | QuestionId 0x1B3 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6515-6675 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x734 | QuestionId 0x1B4 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6695-6835 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x735 | QuestionId 0x1B5 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6855-7095 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0x9C2 | QuestionId 0x1B6 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 2400 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9C3 | QuestionId 0x1B7 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5180-5320 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9C4 | QuestionId 0x1B8 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5340-5440 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9C5 | QuestionId 0x1B9 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5460-5700 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9C6 | QuestionId 0x1BA | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5720-5825 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9C7 | QuestionId 0x1BB | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5845-6135 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9C8 | QuestionId 0x1BC | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6155-6375 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9C9 | QuestionId 0x1BD | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6395-6495 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9CA | QuestionId 0x1BE | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6515-6675 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9CB | QuestionId 0x1BF | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6695-6835 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9CC | QuestionId 0x1C0 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6855-7095 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0x9CD | QuestionId 0x1C1 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 2400 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA0B | QuestionId 0x1C2 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5180-5320 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA0C | QuestionId 0x1C3 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5340-5440 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA0D | QuestionId 0x1C4 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5460-5700 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA0E | QuestionId 0x1C5 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5720-5825 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA0F | QuestionId 0x1C6 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5845-6135 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA10 | QuestionId 0x1C7 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6155-6375 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA11 | QuestionId 0x1C8 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6395-6495 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA12 | QuestionId 0x1C9 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6515-6675 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA13 | QuestionId 0x1CA | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6695-6835 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA14 | QuestionId 0x1CB | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6855-7095 MHz Set1 Chain A** (numeric)
- VarStore: Setup @ offset 0xA15 | QuestionId 0x1CC | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 2400 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA16 | QuestionId 0x1CD | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5180-5320 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA17 | QuestionId 0x1CE | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5340-5440 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA18 | QuestionId 0x1CF | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5460-5700 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA19 | QuestionId 0x1D0 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5720-5825 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA1A | QuestionId 0x1D1 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5845-6135 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA1B | QuestionId 0x1D2 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6155-6375 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA1C | QuestionId 0x1D3 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6395-6495 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA1D | QuestionId 0x1D4 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6515-6675 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA1E | QuestionId 0x1D5 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6695-6835 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA1F | QuestionId 0x1D6 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6855-7095 MHz Set1 Chain B** (numeric)
- VarStore: Setup @ offset 0xA20 | QuestionId 0x1D7 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **WiFi Dynamic SAR** (oneof)
- VarStore: Setup @ offset 0x736 | QuestionId 0x1D8 | size 8
- options: 
- help: Enable/Disable WiFi Dynamic SAR Tx Power Limit which shell be set dynamically accorting to the Proximity Sensor

## Form 0x13D2: Connectivity Configuration  ->  **Extended SAR Range Sets** (oneof)
- VarStore: Setup @ offset 0x737 | QuestionId 0x1D9 | size 8
- options: 
- help: Defines the WiFi SAR Sets that can be used to set the power limts dynamically based on the Proximity Sensor,Set 1 is always present if WiFi SAR enabled and Set 2-3 are additinoal sets

## Form 0x13D2: Connectivity Configuration  ->  **SAR 2400 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x738 | QuestionId 0x1DA | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5180-5320 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x739 | QuestionId 0x1DB | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5340-5440 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x73A | QuestionId 0x1DC | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5460-5700 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x73B | QuestionId 0x1DD | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5720-5825 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x73C | QuestionId 0x1DE | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5845-6135 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x73D | QuestionId 0x1DF | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6155-6375 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x73E | QuestionId 0x1E0 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6395-6495 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x73F | QuestionId 0x1E1 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6515-6675 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x740 | QuestionId 0x1E2 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6695-6835 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x741 | QuestionId 0x1E3 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6855-7095 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0x9CE | QuestionId 0x1E4 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 2400 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9CF | QuestionId 0x1E5 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5180-5320 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D0 | QuestionId 0x1E6 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5340-5440 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D1 | QuestionId 0x1E7 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5460-5700 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D2 | QuestionId 0x1E8 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5720-5825 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D3 | QuestionId 0x1E9 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5845-6135 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D4 | QuestionId 0x1EA | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6155-6375 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D5 | QuestionId 0x1EB | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6395-6495 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D6 | QuestionId 0x1EC | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6515-6675 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D7 | QuestionId 0x1ED | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6695-6835 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D8 | QuestionId 0x1EE | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6855-7095 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0x9D9 | QuestionId 0x1EF | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 2400 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x742 | QuestionId 0x1F0 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5180-5320 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x743 | QuestionId 0x1F1 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5340-5440 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x744 | QuestionId 0x1F2 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5460-5700 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x745 | QuestionId 0x1F3 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5720-5825 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x746 | QuestionId 0x1F4 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5845-6135 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x747 | QuestionId 0x1F5 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6155-6375 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x748 | QuestionId 0x1F6 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6395-6495 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x749 | QuestionId 0x1F7 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6515-6675 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x74A | QuestionId 0x1F8 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6695-6835 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x74B | QuestionId 0x1F9 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6855-7095 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0x9DA | QuestionId 0x1FA | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 2400 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9DB | QuestionId 0x1FB | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5180-5320 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9DC | QuestionId 0x1FC | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5340-5440 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9DD | QuestionId 0x1FD | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5460-5700 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9DE | QuestionId 0x1FE | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5720-5825 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9DF | QuestionId 0x1FF | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5845-6135 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E0 | QuestionId 0x200 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6155-6375 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E1 | QuestionId 0x201 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6395-6495 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E2 | QuestionId 0x202 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6515-6675 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E3 | QuestionId 0x203 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6695-6835 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E4 | QuestionId 0x204 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6855-7095 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E5 | QuestionId 0x205 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 2400 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x74C | QuestionId 0x206 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5180-5320 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x74D | QuestionId 0x207 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5340-5440 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x74E | QuestionId 0x208 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5460-5700 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x74F | QuestionId 0x209 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5720-5825 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x750 | QuestionId 0x20A | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5845-6135 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x751 | QuestionId 0x20B | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6155-6375 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x752 | QuestionId 0x20C | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6395-6495 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x753 | QuestionId 0x20D | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6515-6675 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x754 | QuestionId 0x20E | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6695-6835 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x755 | QuestionId 0x20F | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6855-7095 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0x9E6 | QuestionId 0x210 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 2400 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E7 | QuestionId 0x211 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5180-5320 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E8 | QuestionId 0x212 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5340-5440 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9E9 | QuestionId 0x213 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5460-5700 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9EA | QuestionId 0x214 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5720-5825 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9EB | QuestionId 0x215 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5845-6135 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9EC | QuestionId 0x216 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6155-6375 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9ED | QuestionId 0x217 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6395-6495 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9EE | QuestionId 0x218 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6515-6675 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9EF | QuestionId 0x219 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6695-6835 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9F0 | QuestionId 0x21A | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6855-7095 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0x9F1 | QuestionId 0x21B | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 2400 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA21 | QuestionId 0x21C | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5180-5320 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA22 | QuestionId 0x21D | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5340-5440 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA23 | QuestionId 0x21E | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5460-5700 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA24 | QuestionId 0x21F | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5720-5825 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA25 | QuestionId 0x220 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5845-6135 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA26 | QuestionId 0x221 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6155-6375 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA27 | QuestionId 0x222 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6395-6495 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA28 | QuestionId 0x223 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6515-6675 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA29 | QuestionId 0x224 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6695-6835 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA2A | QuestionId 0x225 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6855-7095 MHz Set2 Chain A** (numeric)
- VarStore: Setup @ offset 0xA2B | QuestionId 0x226 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 2400 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA2C | QuestionId 0x227 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5180-5320 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA2D | QuestionId 0x228 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5340-5440 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA2E | QuestionId 0x229 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5460-5700 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA2F | QuestionId 0x22A | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5720-5825 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA30 | QuestionId 0x22B | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5845-6135 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA31 | QuestionId 0x22C | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6155-6375 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA32 | QuestionId 0x22D | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6395-6495 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA33 | QuestionId 0x22E | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6515-6675 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA34 | QuestionId 0x22F | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6695-6835 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA35 | QuestionId 0x230 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6855-7095 MHz Set2 Chain B** (numeric)
- VarStore: Setup @ offset 0xA36 | QuestionId 0x231 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 2400 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA37 | QuestionId 0x232 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5180-5320 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA38 | QuestionId 0x233 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5340-5440 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA39 | QuestionId 0x234 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5460-5700 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA3A | QuestionId 0x235 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi CDB SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5720-5825 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA3B | QuestionId 0x236 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5845-6135 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA3C | QuestionId 0x237 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6155-6375 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA3D | QuestionId 0x238 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6395-6495 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA3E | QuestionId 0x239 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6515-6675 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA3F | QuestionId 0x23A | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6695-6835 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA40 | QuestionId 0x23B | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6855-7095 MHz Set3 Chain A** (numeric)
- VarStore: Setup @ offset 0xA41 | QuestionId 0x23C | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 2400 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA42 | QuestionId 0x23D | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5180-5320 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA43 | QuestionId 0x23E | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5340-5440 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA44 | QuestionId 0x23F | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5460-5700 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA45 | QuestionId 0x240 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5720-5825 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA46 | QuestionId 0x241 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5845-6135 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA47 | QuestionId 0x242 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6155-6375 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA48 | QuestionId 0x243 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6395-6495 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA49 | QuestionId 0x244 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6515-6675 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA4A | QuestionId 0x245 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6695-6835 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA4B | QuestionId 0x246 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6855-7095 MHz Set3 Chain B** (numeric)
- VarStore: Setup @ offset 0xA4C | QuestionId 0x247 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 2400 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA4D | QuestionId 0x248 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5180-5320 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA4E | QuestionId 0x249 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5340-5440 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA4F | QuestionId 0x24A | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5460-5700 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA50 | QuestionId 0x24B | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5720-5825 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA51 | QuestionId 0x24C | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5845-6135 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA52 | QuestionId 0x24D | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6155-6375 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA53 | QuestionId 0x24E | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6395-6495 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA54 | QuestionId 0x24F | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6515-6675 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA55 | QuestionId 0x250 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6695-6835 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA56 | QuestionId 0x251 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6855-7095 MHz Set4 Chain A** (numeric)
- VarStore: Setup @ offset 0xA57 | QuestionId 0x252 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 2400 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA58 | QuestionId 0x253 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5180-5320 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA59 | QuestionId 0x254 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5340-5440 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA5A | QuestionId 0x255 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5460-5700 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA5B | QuestionId 0x256 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5720-5825 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA5C | QuestionId 0x257 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 5845-6135 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA5D | QuestionId 0x258 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6155-6375 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA5E | QuestionId 0x259 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6395-6495 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA5F | QuestionId 0x25A | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6515-6675 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA60 | QuestionId 0x25B | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6695-6835 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA61 | QuestionId 0x25C | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR CDB 6855-7095 MHz Set4 Chain B** (numeric)
- VarStore: Setup @ offset 0xA62 | QuestionId 0x25D | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **Antenna A Current Set** (oneof)
- VarStore: Setup @ offset 0x768 | QuestionId 0x25E | size 8
- options: 
- help: Current Set to be used 0 :Default OTP table 1-3 SAR Sets

## Form 0x13D2: Connectivity Configuration  ->  **Antenna B Current Set** (oneof)
- VarStore: Setup @ offset 0x769 | QuestionId 0x25F | size 8
- options: 
- help: Current Set to be used 0 :Default OTP table 1-3 SAR Sets

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5200 MHz Chain B Offset for Group 1** (numeric)
- VarStore: Setup @ offset 0x75B | QuestionId 0x266 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6000-7000 MHz Chain B Offset for Group 1** (numeric)
- VarStore: Setup @ offset 0xA04 | QuestionId 0x269 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6000-7000 MHz Chain B Offset for Group 2** (numeric)
- VarStore: Setup @ offset 0xA07 | QuestionId 0x272 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5200 MHz Chain B Offset for Group 3** (numeric)
- VarStore: Setup @ offset 0x767 | QuestionId 0x278 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6000-7000 MHz Chain B Offset for Group 3** (numeric)
- VarStore: Setup @ offset 0xA0A | QuestionId 0x27B | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5200 MHz Chain B Offset for Group 4** (numeric)
- VarStore: Setup @ offset 0xB3F | QuestionId 0x281 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6000-7000 MHz Chain B Offset for Group 4** (numeric)
- VarStore: Setup @ offset 0xB42 | QuestionId 0x284 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5200 MHz Chain B Offset for Group 5** (numeric)
- VarStore: Setup @ offset 0xB48 | QuestionId 0x28A | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6000-7000 MHz Chain B Offset for Group 5** (numeric)
- VarStore: Setup @ offset 0xB4B | QuestionId 0x28D | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5200 MHz Chain B Offset for Group 6** (numeric)
- VarStore: Setup @ offset 0xB51 | QuestionId 0x293 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6000-7000 MHz Chain B Offset for Group 6** (numeric)
- VarStore: Setup @ offset 0xB54 | QuestionId 0x296 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5200 MHz Chain B Offset for Group 7** (numeric)
- VarStore: Setup @ offset 0xB5A | QuestionId 0x29C | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6000-7000 MHz Chain B Offset for Group 7** (numeric)
- VarStore: Setup @ offset 0xB5D | QuestionId 0x29F | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 5200 MHz Chain B Offset for Group 8** (numeric)
- VarStore: Setup @ offset 0xB63 | QuestionId 0x2A5 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **SAR 6000-7000 MHz Chain B Offset for Group 8** (numeric)
- VarStore: Setup @ offset 0xB66 | QuestionId 0x2A8 | size 8
- min 0x0 max 0xFF
- help: Defines the WiFi SAR Tx Power Limit - 8bit unsigned with 5bit integer and 3bit fractional. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR** (oneof)
- VarStore: Setup @ offset 0x76A | QuestionId 0x2C2 | size 8
- options: 
- help: Define the mode of SAR control to be used.  Disabled: Tx power shall be mandated by device NVM  Enabled: Tx power shall be the minimum between BIOS SAR table and BT Device NVM (either Module or Platform)

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth Increased Power Mode** (oneof)
- VarStore: Setup @ offset 0xBA9 | QuestionId 0x2C3 | size 8
- options: 
- help: Defines Bluetooth Increased Power Mode. SAR Limitation feature enablement/disablement

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR Power Limit 2400 Chain A** (numeric)
- VarStore: Setup @ offset 0xBAA | QuestionId 0x2C4 | size 8
- min 0x0 max 0xFF
- help: Bluetooth SAR power restriction for the Lower Band (LB) - 2400MHz frequency Chain A. 0x00 = 0b00000000 = 0.125dB; 0xFF = 0b11111111 = 31.875dB. Each step is equivalent to 0.125dB

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR BR** (numeric)
- VarStore: Setup @ offset 0x76B | QuestionId 0x2C5 | size 8
- min 0x0 max 0xFF
- help: Defines the SAR power restriction for BR Modulation

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR EDR2** (numeric)
- VarStore: Setup @ offset 0x76C | QuestionId 0x2C6 | size 8
- min 0x0 max 0xFF
- help: Defines the SAR power restriction for EDR2 Modulation

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR EDR3** (numeric)
- VarStore: Setup @ offset 0x76D | QuestionId 0x2C7 | size 8
- min 0x0 max 0xFF
- help: Defines the SAR power restriction for EDR3 Modulation

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR LE** (numeric)
- VarStore: Setup @ offset 0x76E | QuestionId 0x2C8 | size 8
- min 0x0 max 0xFF
- help: Defines the SAR power restriction for LE Modulation

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR LE 2Mhz** (numeric)
- VarStore: Setup @ offset 0x76F | QuestionId 0x2C9 | size 8
- min 0x0 max 0xFF
- help: Defines the SAR power restriction for LE 2Mhz Modulation

## Form 0x13D2: Connectivity Configuration  ->  **Bluetooth SAR LE LR** (numeric)
- VarStore: Setup @ offset 0x770 | QuestionId 0x2CA | size 8
- min 0x0 max 0xFF
- help: Defines the SAR power restriction for LE LR Modulation

## Form 0x13D2: Connectivity Configuration  ->  **Wi-Fi Energy Detection Threshold** (numeric)
- VarStore: Setup @ offset 0xBA0 | QuestionId 0x2D4 | size 32
- min 0x0 max 0xFFFFFFFF
- help: Please input HEX value.  Bit value  '0' Use default EDT method  '1' Use new EDT method Bit0:1 - Reserved Bit2 - For ETSI Bit3:4 - Reserved Bit5 - For FCC Bit6:8 - Reserved Bit9 - For HB 5150-5350 Bit10 - For HB 5350-5470 Bit11 - For HB 5470-5725 Bit12 - For HB 5725-5945 Bit13 - For UHB 5945-6165 Bit14 - For UHB 6165-6405 Bit15 - For UHB 6405-6525 Bit16 - For UHB 6525-6705 Bit17 - For UHB 6705-6865 Bit18 - For UHB 6865-7105 Bit31:19 - Reserved

## Form 0x13D2: Connectivity Configuration  ->  **WTAS Selection** (numeric)
- VarStore: Setup @ offset 0xB6A | QuestionId 0x2D6 | size 32
- min 0x0 max 0xFFFFFFFF
- help: Please input HEX value.  Bit0 - Enable TAS feature.  '0' TAS Disabled [Default]  '1' TAS Enabled Bit1 - IEC Optimization, override NIC configuration (BIOSoverideTASrIEC),Allow override NIC defaults.  '0' No override, use device settings.  '1' Override IEC Optimization, effected over certified NIC. The Value will set by Bit #2. Bit2 - IEC Optimization Control Valve (BIOCenTrIC).This bit impact only incase that Bit #1 set to ‘1’ and the NIC is certified to support TAS over IEC.  '0' Disabled TAS IEC optimization regulatory averaging time  '1' Enabled TAS IEC optimization regulatory averaging time Bit31:3 - Reserved

## Form 0x153B: WWAN Configuration  ->  **WWAN Reset Workaround** (oneof)
- VarStore: Setup @ offset 0x84E | QuestionId 0x2EE | size 8
- options: 
- help: Enabling this workardound will result in BIOS asserting FULL_CARD_POWER_OFF#, PERST# and RESET# WWAN signals before the WWAN Device Power-On Sequence is executed. Disabling it has no impact.

## Form 0x1013: OverClocking Performance Menu  ->  **OverClocking Feature** (oneof)
- VarStore: CpuSetup @ offset 0x1D9 | QuestionId 0x1574 | size 8
- options: 
- help: Performance Menu for Processor and Memory.

## Form 0x1013: OverClocking Performance Menu  ->  **UnderVolt Protection** (oneof)
- VarStore: CpuSetup @ offset 0x381 | QuestionId 0x2F1 | size 8
- options: 
- help: When UnderVolt Protection is enabled, user will not be able to program under voltage in OS runtime. Recommended to keep it enabled by default. Enabled: Allow BIOS undervolting, but enable UnderVolt Protection in Runtime. Disabled: No UnderVolt Protection in Runtime.

## Form 0x1013: OverClocking Performance Menu  ->  **CPU BCLK OC Frequency** (numeric)
- VarStore: CpuSetup @ offset 0x2F7 | QuestionId 0x2F4 | size 32
- min 0x0 max 0xC350
- help: CPU BCLK Frequency in 10kHz increments. Specifies new CPU BCLK frequency to be applied. Frequency is rounded to nearest valid value. Allowed range is limited by the Max/Min supported frequencies. Changes are not applied until settings are saved and platform resets. Example: For 125.70MHz, enter 12570.

## Form 0x1013: OverClocking Performance Menu  ->  **BCLK Aware Adaptive Voltage** (oneof)
- VarStore: CpuSetup @ offset 0x20D | QuestionId 0x2F5 | size 8
- options: 
- help: BCLK Aware Adaptive Voltage enable/disable. When enabled, pcode will be aware of the BCLK frequency when calculating the CPU V/F curves. This is ideal for BCLK OC to avoid high voltage overrides. Uses OC Mailbox command 0x15.

## Form 0x1013: OverClocking Performance Menu  ->  **PVD Ratio Threshold** (numeric)
- VarStore: CpuSetup @ offset 0x1DC | QuestionId 0x2F6 | size 8
- min 0x0 max 0x28
- help: Select PVD Ratio Threshold Value from Range 1 to 40. 0 - Auto/HW default

## Form 0x1013: OverClocking Performance Menu  ->  **FLL Overclock Mode Enable** (oneof)
- VarStore: CpuSetup @ offset 0x352 | QuestionId 0x2F7 | size 8
- options: 
- help: Enable FLL Overclock Mode, Default is Disable

## Form 0x1013: OverClocking Performance Menu  ->  **FLL Overclock Mode Select** (numeric)
- VarStore: CpuSetup @ offset 0x353 | QuestionId 0x2F8 | size 8
- min 0x0 max 0x3
- help: Select FLL Mode Value from Range 1 to 3. 0x0 = no overclocking, 0x1 = ratio overclocking with nominal (0.5-1x) reference clock frequency, 0x2 = BCLK overclocking with elevated (1-3x) reference clock frequency, 0x3 = BCLK overclocking with extreme elevated (3-5x) reference clock frequency and ratio limited to 63

## Form 0x1014: Processor  ->  **Core Ratio Extension Mode** (oneof)
- VarStore: CpuSetup @ offset 0x1DA | QuestionId 0x305 | size 8
- options: 
- help: Enable / Disable Core Ratio Above 85 Extension Mode. Enable - Max Overclocking Ratio Limit as specified by OCMB 0x1 command is 120; Disable - Max Overclocking Ratio Limit as specified by OCMB 0x1 command is 85.

## Form 0x1014: Processor  ->  **Core Max OC Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x1DB | QuestionId 0x306 | size 8
- min 0x0 max 0x78
- help: Sets the maximum OC Ratio for the CPU Core. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range non-turbo max - 120 (Previously max turbo is 83).

## Form 0x1014: Processor  ->  **Core Max OC Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x1DB | QuestionId 0x307 | size 8
- min 0x0 max 0x55
- help: Sets the maximum OC Ratio for the CPU Core. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range non-turbo max - 85 (Previously max turbo is 83).

## Form 0x1014: Processor  ->  **Core 0 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2BC | QuestionId 0x309 | size 8
- min 0x0 max 0x78
- help: Override current maximum OC Ratio for the CPU Core 0.

## Form 0x1014: Processor  ->  **Core 1 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2BD | QuestionId 0x30A | size 8
- min 0x0 max 0x78
- help: Override current maximum OC Ratio for the CPU Core 1.

## Form 0x1014: Processor  ->  **Core 2 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2BE | QuestionId 0x30B | size 8
- min 0x0 max 0x78
- help: Override current maximum OC Ratio for the CPU Core 2.

## Form 0x1014: Processor  ->  **Core 3 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2BF | QuestionId 0x30C | size 8
- min 0x0 max 0x78
- help: Override current maximum OC Ratio for the CPU Core 3.

## Form 0x1014: Processor  ->  **Core 4 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2C0 | QuestionId 0x30D | size 8
- min 0x0 max 0x78
- help: Override current maximum OC Ratio for the CPU Core 4.

## Form 0x1014: Processor  ->  **Core 5 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2C1 | QuestionId 0x30E | size 8
- min 0x0 max 0x78
- help: Override current maximum OC Ratio for the CPU Core 5.

## Form 0x1014: Processor  ->  **Core 6 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2C2 | QuestionId 0x30F | size 8
- min 0x0 max 0x78
- help: Override current maximum OC Ratio for the CPU Core 6.

## Form 0x1014: Processor  ->  **Core 7 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2C3 | QuestionId 0x310 | size 8
- min 0x0 max 0x78
- help: Override current maximum OC Ratio for the CPU Core 7.

## Form 0x1014: Processor  ->  **Cluster 0 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2B7 | QuestionId 0x311 | size 8
- min 0x0 max 0x78
- help: Override Efficient-cores 0 - 3 Maximum OC Ratio, maximum value up to 120.Note. E-cores 0 - 3 are in the same Cluster and their max core ratio will be aligned.

## Form 0x1014: Processor  ->  **Cluster 1 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2B8 | QuestionId 0x312 | size 8
- min 0x0 max 0x78
- help: Override Efficient-cores 4 - 7 Maximum OC Ratio, maximum value up to 120.Note. E-cores 4 - 7 are in the same Cluster and their max core ratio will be aligned.

## Form 0x1014: Processor  ->  **Cluster 2 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2B9 | QuestionId 0x313 | size 8
- min 0x0 max 0x78
- help: Override Efficient-cores 8 - 11 Maximum OC Ratio, maximum value up to 120.Note. E-cores 8 - 11 are in the same Cluster and their max core ratio will be aligned.

## Form 0x1014: Processor  ->  **Cluster 3 Max Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x2BA | QuestionId 0x314 | size 8
- min 0x0 max 0x78
- help: Override Efficient-cores 12 - 15 Maximum OC Ratio, maximum value up to 120.Note. E-cores 12 - 15 are in the same Cluster and their max core ratio will be aligned.

## Form 0x1014: Processor  ->  **VF Offset Mode** (oneof)
- VarStore: CpuSetup @ offset 0x232 | QuestionId 0x315 | size 8
- options: 
- help: Selects between Legacy and Selection modes. Need Reset System after enabling OverClocking Feature to Initialize the default value. In Legacy Mode, setting a global offset for the entire VF curve. In Selection modes, setting a selected VF point.

## Form 0x1014: Processor  ->  **Core Voltage Mode** (oneof)
- VarStore: CpuSetup @ offset 0x1DD | QuestionId 0x316 | size 8
- options: 
- help: Selects between Adaptive and Override Voltage modes. In Override Mode the voltage selected will be applied over all operating frequencies. In Adaptive Mode the voltage is interpolated only in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11.

## Form 0x1014: Processor  ->  **P-core Voltage Override** (numeric)
- VarStore: CpuSetup @ offset 0x1DE | QuestionId 0x317 | size 16
- min 0x0 max 0x7D0
- help: Specifies the Override Voltage applied to the Performance-core domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV.

## Form 0x1014: Processor  ->  **P-core Voltage Target Override** (numeric)
- VarStore: CpuSetup @ offset 0x1E3 | QuestionId 0x318 | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while Performance-core is operating in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range 0-2000 mV

## Form 0x1014: Processor  ->  **P-core Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x1E0 | QuestionId 0x31A | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Global Performance-core domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **P-core 0 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x262 | QuestionId 0x31C | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Performance-core 0 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **P-core 1 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x264 | QuestionId 0x31E | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Performance-core 1 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **P-core 2 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x266 | QuestionId 0x320 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Performance-core 2 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **P-core 3 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x268 | QuestionId 0x322 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Performance-core 3 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **P-core 4 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x26A | QuestionId 0x324 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Performance-core 4 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **P-core 5 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x26C | QuestionId 0x326 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Performance-core 5 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **P-core 6 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x26E | QuestionId 0x328 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Performance-core 6 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **P-core 7 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x270 | QuestionId 0x32A | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Performance-core 7 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **Cluster 0 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x315 | QuestionId 0x32C | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Efficient-core Cluster 0 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **Cluster 1 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x317 | QuestionId 0x32E | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Efficient-core Cluster 1 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **Cluster 2 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x319 | QuestionId 0x330 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Efficient-core Cluster 2 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **Cluster 3 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x31B | QuestionId 0x332 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Efficient-core Cluster 3 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 1 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x234 | QuestionId 0x334 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 1. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x1. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 2 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x236 | QuestionId 0x336 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 2. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x2. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 3 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x238 | QuestionId 0x338 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 3. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x3. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 4 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x23A | QuestionId 0x33A | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 4. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x4. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 5 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x23C | QuestionId 0x33C | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 5. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x5. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 6 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x23E | QuestionId 0x33E | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 6. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x6. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 7 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x240 | QuestionId 0x340 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 7. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x7. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 8 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x242 | QuestionId 0x342 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 8. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x8. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 9 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x244 | QuestionId 0x344 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 9. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x9. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 10 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x246 | QuestionId 0x346 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 10. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xA. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 11 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x248 | QuestionId 0x348 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 11. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xB. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 12 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x24A | QuestionId 0x34A | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 12. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xC. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 13 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x24C | QuestionId 0x34C | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 13. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xD. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 14 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x24E | QuestionId 0x34E | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 14. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xE. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **VF Point 15 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x250 | QuestionId 0x350 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 15. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xF. Range -500 to 500 mV

## Form 0x1014: Processor  ->  **AVX2 Voltage Guardband Scale Factor** (numeric)
- VarStore: CpuSetup @ offset 0x225 | QuestionId 0x353 | size 8
- min 0x0 max 0xC8
- help: AVX2 Voltage Guardband Scale Factor. Controls the voltage guardband applied to AVX workloads. Range 0 - 200 in 1/100 units, where 125 = 1.25 scale factor. A default value of 100 applies the default voltage guardband scale factor of 1.0. A value > 100 will increase the votlage guardband, and < 100 will decrease the voltage guardband.

## Form 0x1014: Processor  ->  **Fast Throttle Threshold** (numeric)
- VarStore: CpuSetup @ offset 0x395 | QuestionId 0x13BB | size 8
- min 0x0 max 0x73
- help: Fast Throttle Threshold. Specified value for max allowed temperature when cores throttle. Support Fast Throttle Threshold in the range of 63 to 115 deg Celsius, set back to 0 for default if not in the range. 0 = Hardware Default.

## Form 0x1014: Processor  ->  **Thermal Velocity Boost** (oneof)
- VarStore: CpuSetup @ offset 0x2E3 | QuestionId 0x354 | size 8
- options: 
- help: This service controls Core frequency reduction caused by high package temperatures for processors that implement the Intel Thermal Velocity Boost (TVB) feature. It is required to be disabled for supporting overclocking at frequencies higher than the default max turbo frequency. Default is disabled. Uses Overclocking Mailbox command 0x18/0x19.

## Form 0x1014: Processor  ->  **Down Bins (delta) for Temperature Threshold 0** (numeric)
- VarStore: CpuSetup @ offset 0x34E | QuestionId 0x355 | size 8
- min 0x0 max 0xA
- help: When running above Temperature Threshold 0, the ratio will be clipped to (Max_Ratio-This Down Bins value)

## Form 0x1014: Processor  ->  **TVB Temperature Threshold 0 (degrees C)** (numeric)
- VarStore: CpuSetup @ offset 0x34F | QuestionId 0x356 | size 8
- min 0x0 max 0x64
- help: Running ABOVE this temperature will clip delta Down Bins for Threshold 0 from the resolved OC Ratio

## Form 0x1014: Processor  ->  **TVB Temperature Threshold 1 (degrees C)** (numeric)
- VarStore: CpuSetup @ offset 0x350 | QuestionId 0x357 | size 8
- min 0x0 max 0x64
- help: Running ABOVE this temperature will clip delta Down Bins for Threshold 1 from the resolved OC Ratio

## Form 0x1014: Processor  ->  **Down Bins (delta) for Temperature Threshold 1** (numeric)
- VarStore: CpuSetup @ offset 0x351 | QuestionId 0x358 | size 8
- min 0x0 max 0xA
- help: When running above Temperature Threshold 1, the ratio will be clipped to (Max_Ratio-This Down Bins value)

## Form 0x1014: Processor  ->  **TVB Voltage Optimizations** (oneof)
- VarStore: CpuSetup @ offset 0x2E4 | QuestionId 0x359 | size 8
- options: 
- help: This service controls thermal based voltage optimizations for processors that implement the Intel Thermal Velocity Boost (TVB) feature. Default is enabled. Uses Overclocking Mailbox command 0x18/0x19.

## Form 0x1014: Processor  ->  **Enhanced Thermal Velocity Boost** (oneof)
- VarStore: CpuSetup @ offset 0x378 | QuestionId 0x35A | size 8
- options: 
- help: If enabled the user will be clipped when the temperatures reach the default threshold on supported products.  Recommended to disable for overclocking.

## Form 0x1016: E-core L2 Configurations  ->  **E-core L2 Voltage Mode** (oneof)
- VarStore: CpuSetup @ offset 0x2AF | QuestionId 0x35B | size 8
- options: 
- help: Selects between Adaptive and Override Voltage modes. In Override Mode the voltage selected will be applied over all operating frequencies. In Adaptive Mode the voltage is interpolated only in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11.

## Form 0x1016: E-core L2 Configurations  ->  **E-core L2 Voltage Override** (numeric)
- VarStore: CpuSetup @ offset 0x2B0 | QuestionId 0x35C | size 16
- min 0x0 max 0x7D0
- help: Specifies the Override Voltage applied to the Efficient-core L2 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV.

## Form 0x1016: E-core L2 Configurations  ->  **E-core L2 Extra Turbo Voltage** (numeric)
- VarStore: CpuSetup @ offset 0x2B5 | QuestionId 0x35D | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while Efficient-core L2 is operating in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range 0-2000 mV

## Form 0x1016: E-core L2 Configurations  ->  **E-core L2 Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x2B2 | QuestionId 0x35E | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Efficient-core L2 domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **Ring Max OC Ratio** (numeric)
- VarStore: CpuSetup @ offset 0x1E7 | QuestionId 0x111C | size 8
- min 0x0 max 0x55
- help: Sets the maximum OC Ratio for the CPU Ring. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range non-turbo max - 85.

## Form 0x1101: Ring  ->  **VF Offset Mode** (oneof)
- VarStore: CpuSetup @ offset 0x27C | QuestionId 0x360 | size 8
- options: 
- help: Selects between Legacy and Selection modes. Need Reset System after enabling OverClocking Feature to Initialize the default value. In Legacy Mode, setting a global offset for the entire VF curve. In Selection modes, setting a selected VF point.

## Form 0x1101: Ring  ->  **Ring Voltage Mode** (oneof)
- VarStore: CpuSetup @ offset 0x1E9 | QuestionId 0x361 | size 8
- options: 
- help: Selects between Adaptive and Override Voltage modes. In Override Mode the voltage selected will be applied over all operating frequencies. In Adaptive Mode the voltage is interpolated only in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11.

## Form 0x1101: Ring  ->  **Ring Voltage Override** (numeric)
- VarStore: CpuSetup @ offset 0x1EA | QuestionId 0x362 | size 16
- min 0x0 max 0x7D0
- help: Specifies the Override Voltage applied to the Ring domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV.

## Form 0x1101: Ring  ->  **Ring Extra Turbo Voltage** (numeric)
- VarStore: CpuSetup @ offset 0x1EF | QuestionId 0x363 | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while ring is operating in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range 0-2000 mV

## Form 0x1101: Ring  ->  **Ring Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x1EC | QuestionId 0x364 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Ring domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 1 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x27E | QuestionId 0x366 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 1. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x1. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 2 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x280 | QuestionId 0x368 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 2. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x2. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 3 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x282 | QuestionId 0x36A | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 3. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x3. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 4 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x284 | QuestionId 0x36C | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 4. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x4. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 5 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x286 | QuestionId 0x36E | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 5. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x5. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 6 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x288 | QuestionId 0x370 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 6. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x6. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 7 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x28A | QuestionId 0x372 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 7. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x7. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 8 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x28C | QuestionId 0x374 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 8. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x8. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 9 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x28E | QuestionId 0x376 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 9. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0x9. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 10 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x290 | QuestionId 0x378 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 10. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xA. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 11 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x292 | QuestionId 0x37A | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 11. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xB. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 12 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x294 | QuestionId 0x37C | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 12. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xC. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 13 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x296 | QuestionId 0x37E | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 13. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xD. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 14 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x298 | QuestionId 0x380 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 14. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xE. Range -500 to 500 mV

## Form 0x1101: Ring  ->  **VF Point 15 Offset** (numeric)
- VarStore: CpuSetup @ offset 0x29A | QuestionId 0x382 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Selected VF Point 15. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11, Param1 0:Core 2:Ring, Param2 0xF. Range -500 to 500 mV

## Form 0x101B: GT  ->  **GT OverClocking Frequency** (numeric)
- VarStore: SaSetup @ offset 0x262 | QuestionId 0x385 | size 8
- min 0x0 max 0x2A
- help: Overclocked RP0 Frequency (MLC Clk) in multiples of 50 MHz

## Form 0x101B: GT  ->  **GT Voltage Mode** (oneof)
- VarStore: SaSetup @ offset 0x263 | QuestionId 0x386 | size 8
- options: 
- help: Selects between Adaptive and Override Voltage modes. In Override Mode the voltage selected will be applied over all operating frequencies. In Adaptive Mode the voltage is interpolated only in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11.

## Form 0x101B: GT  ->  **GT Voltage Override** (numeric)
- VarStore: SaSetup @ offset 0x267 | QuestionId 0x387 | size 16
- min 0x0 max 0x7D0
- help: Specifies the Override Voltage applied to the GT domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV

## Form 0x101B: GT  ->  **GT Extra Turbo Voltage** (numeric)
- VarStore: SaSetup @ offset 0x269 | QuestionId 0x388 | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while GT is operating in turbo mode. Unit is in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV

## Form 0x101B: GT  ->  **GT Voltage Offset** (numeric)
- VarStore: SaSetup @ offset 0x264 | QuestionId 0x389 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the GT domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -1000 to 1000 mV

## Form 0x101B: GT  ->  **GT OverClocking Frequency** (numeric)
- VarStore: SaSetup @ offset 0x26B | QuestionId 0x38B | size 8
- min 0x0 max 0x2A
- help: Overclocked RP0 Frequency (MLC Clk) in multiples of 50 MHz

## Form 0x101B: GT  ->  **GT Voltage Mode** (oneof)
- VarStore: SaSetup @ offset 0x26C | QuestionId 0x38C | size 8
- options: 
- help: Selects between Adaptive and Override Voltage modes. In Override Mode the voltage selected will be applied over all operating frequencies. In Adaptive Mode the voltage is interpolated only in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11.

## Form 0x101B: GT  ->  **GT Voltage Override** (numeric)
- VarStore: SaSetup @ offset 0x270 | QuestionId 0x38D | size 16
- min 0x0 max 0x7D0
- help: Specifies the Override Voltage applied to the GT domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV

## Form 0x101B: GT  ->  **GT Extra Turbo Voltage** (numeric)
- VarStore: SaSetup @ offset 0x272 | QuestionId 0x38E | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while GT is operating in turbo mode. Unit is in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV

## Form 0x101B: GT  ->  **GTU Voltage Offset** (numeric)
- VarStore: SaSetup @ offset 0x26D | QuestionId 0x38F | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the GT domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -1000 to 1000 mV

## Form 0x1102: Uncore  ->  **Uncore Voltage Mode** (oneof)
- VarStore: CpuSetup @ offset 0x2DE | QuestionId 0x391 | size 8
- options: 
- help: Selects between Adaptive and Override Voltage modes. In Override Mode the voltage selected will be applied over all operating frequencies. In Adaptive Mode the voltage is interpolated only in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11.

## Form 0x1102: Uncore  ->  **Uncore Voltage Override** (numeric)
- VarStore: CpuSetup @ offset 0x2DF | QuestionId 0x392 | size 16
- min 0x0 max 0x7D0
- help: Specifies the Override Voltage applied to the SA Uncore domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range 0-2000 mV.

## Form 0x1102: Uncore  ->  **Uncore Extra Turbo Voltage** (numeric)
- VarStore: CpuSetup @ offset 0x2E1 | QuestionId 0x393 | size 16
- min 0x0 max 0x7D0
- help: Specifies the extra turbo voltage applied while SA Uncore is operating in turbo mode. Uses Mailbox MSR 0x150, cmd 0x10, 0x11. Range 0-2000 mV

## Form 0x1102: Uncore  ->  **Uncore Voltage Offset** (numeric)
- VarStore: SaSetup @ offset 0x25F | QuestionId 0x394 | size 16
- min 0x0 max 0x3E8
- help: Specifies the Offset Voltage applied to the Uncore domain. This voltage is specified in millivolts. Uses Mailbox MSR 0x150, cmd 0x11. Range -1000 to 1000 mV

## Form 0x1103: Platform Voltage Overrides  ->  **Vcc1p8 Override Enable** (oneof)
- VarStore: CpuSetup @ offset 0x321 | QuestionId 0x396 | size 8
- options: 
- help: Overrides the Vcc1p8 voltage using SMBUS/PMBUS interface of VRM. Use the next option for exact voltage configuration

## Form 0x1103: Platform Voltage Overrides  ->  **Vcc1p8** (numeric)
- VarStore: CpuSetup @ offset 0x322 | QuestionId 0x397 | size 16
- min 0x320 max 0x9F6
- help: Range of Vcc1p8 voltage - Default is 1800 mV

## Form 0x1103: Platform Voltage Overrides  ->  **Vcc1p05 Override Enable** (oneof)
- VarStore: CpuSetup @ offset 0x324 | QuestionId 0x398 | size 8
- options: 
- help: Overrides the Vcc1p05 voltage using SMBUS/PMBUS interface of VRM. Use the next option for exact voltage configuration

## Form 0x1103: Platform Voltage Overrides  ->  **Vcc1p05** (numeric)
- VarStore: CpuSetup @ offset 0x325 | QuestionId 0x399 | size 16
- min 0x320 max 0x9F6
- help: Range of Vcc1p05 voltage - Default is 1050 mV

## Form 0x1103: Platform Voltage Overrides  ->  **VccDD2 Override Enable** (oneof)
- VarStore: CpuSetup @ offset 0x327 | QuestionId 0x39A | size 8
- options: 
- help: Overrides the VccDD2 voltage using SMBUS/PMBUS interface of VRM. Use the next option for exact voltage configuration

## Form 0x1103: Platform Voltage Overrides  ->  **VccDD2** (numeric)
- VarStore: CpuSetup @ offset 0x328 | QuestionId 0x39B | size 16
- min 0x320 max 0x9F6
- help: Range of VccDD2 voltage - Default is 1100 mV

## Form 0x1103: Platform Voltage Overrides  ->  **VCCIN AUX CPU Overrides Enable** (oneof)
- VarStore: CpuSetup @ offset 0x336 | QuestionId 0x39C | size 8
- options: 
- help: VCCIN AUX CPU Voltage Overrides from SMBUS/PMBUS interface of VRM. Use the next option for exact voltage configuration

## Form 0x1103: Platform Voltage Overrides  ->  **VCCIN AUX CPU** (numeric)
- VarStore: CpuSetup @ offset 0x337 | QuestionId 0x39D | size 16
- min 0x654 max 0x76C
- help: Voltage Range of VCCIN AUX CPU from 1620mV - 1900mV; Default is 1800 mV

## Form 0x1103: Platform Voltage Overrides  ->  **RichTek VccIA Control Overrides** (oneof)
- VarStore: CpuSetup @ offset 0x339 | QuestionId 0x39E | size 8
- options: 
- help: VccIA Voltage can be overrides from Richtek SMBUS/PMBUS VR. Use the next option for exact voltage configuration

## Form 0x1103: Platform Voltage Overrides  ->  **Fixed VID Mode** (oneof)
- VarStore: CpuSetup @ offset 0x33B | QuestionId 0x39F | size 8
- options: 
- help: Fixed VID Mode Enabled for the VccIA/VccGT Voltage rail Overrides from Richtek SMBUS/PMBUS VR. When Disabled, voltage rail will use IMVP from SVID BUS.

## Form 0x1103: Platform Voltage Overrides  ->  **VccIA (mV)** (numeric)
- VarStore: CpuSetup @ offset 0x33D | QuestionId 0x3A0 | size 16
- min 0xFA max 0x87A
- help: Voltage Range of RichTek VccIA from 250mV - 2170mV; Default is 1200 mV

## Form 0x1103: Platform Voltage Overrides  ->  **RichTek VccGT Control Overrides** (oneof)
- VarStore: CpuSetup @ offset 0x33A | QuestionId 0x3A1 | size 8
- options: 
- help: VccGT Voltage can be overrides from Richtek SMBUS/PMBUS VR. Use the next option for exact voltage configuration

## Form 0x1103: Platform Voltage Overrides  ->  **Fixed VID Mode** (oneof)
- VarStore: CpuSetup @ offset 0x33C | QuestionId 0x3A2 | size 8
- options: 
- help: Fixed VID Mode Enabled for the VccIA/VccGT Voltage rail Overrides from Richtek SMBUS/PMBUS VR. When Disabled, voltage rail will use IMVP from SVID BUS.

## Form 0x1103: Platform Voltage Overrides  ->  **VccGT (mV)** (numeric)
- VarStore: CpuSetup @ offset 0x33F | QuestionId 0x3A3 | size 16
- min 0xFA max 0x87A
- help: Voltage Range of RichTek VccGT from 250mV - 2170mV; Default is 1200 mV

## Form 0x1526: Voltage PLL Trim Controls  ->  **Core PLL Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x1F2 | QuestionId 0x3A4 | size 8
- min 0x0 max 0xF
- help: PLL Voltage Offset, Range 0-15. Units are in 17.5mV. Default is 0. This control can be used to increase the range of this domain frequency in extreme overclocking conditions.

## Form 0x1526: Voltage PLL Trim Controls  ->  **GT PLL Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x1F3 | QuestionId 0x3A5 | size 8
- min 0x0 max 0xF
- help: PLL Voltage Offset, Range 0-15. Units are in 17.5mV. Default is 0. This control can be used to increase the range of this domain frequency in extreme overclocking conditions.

## Form 0x1526: Voltage PLL Trim Controls  ->  **Ring PLL Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x1F4 | QuestionId 0x3A6 | size 8
- min 0x0 max 0xF
- help: PLL Voltage Offset, Range 0-15. Units are in 17.5mV. Default is 0. This control can be used to increase the range of this domain frequency in extreme overclocking conditions.

## Form 0x1526: Voltage PLL Trim Controls  ->  **System Agent PLL Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x1F5 | QuestionId 0x3A7 | size 8
- min 0x0 max 0xF
- help: PLL Voltage Offset, Range 0-15. Units are in 17.5mV. Default is 0. This control can be used to increase the range of this domain frequency in extreme overclocking conditions.

## Form 0x1526: Voltage PLL Trim Controls  ->  **Efficient-core PLL Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x1F6 | QuestionId 0x3A8 | size 8
- min 0x0 max 0xF
- help: PLL Voltage Offset, Range 0-15. Units are in 17.5mV. Default is 0. This control can be used to increase the range of this domain frequency in extreme overclocking conditions.

## Form 0x1526: Voltage PLL Trim Controls  ->  **Memory Controller PLL Voltage Offset** (numeric)
- VarStore: CpuSetup @ offset 0x1F7 | QuestionId 0x3A9 | size 8
- min 0x0 max 0xF
- help: PLL Voltage Offset, Range 0-15. Units are in 17.5mV. Default is 0. This control can be used to increase the range of this domain frequency in extreme overclocking conditions.

## Form 0x10DE: CEP Disable  ->  **IA CEP Enable** (oneof)
- VarStore: CpuSetup @ offset 0x334 | QuestionId 0x3AA | size 8
- options: 
- help: Enable/Disable IA CEP (Current Excursion Protection) Support. Uses pCode Mailbox Command 0x37, Sub-command 0x1. Set Data bit2 to 1.

## Form 0x10DE: CEP Disable  ->  **GT CEP Enable** (oneof)
- VarStore: CpuSetup @ offset 0x335 | QuestionId 0x3AB | size 8
- options: 
- help: Enable/Disable GT CEP (Current Excursion Protection) Support. Uses pCode Mailbox Command 0x37, Sub-command 0x1. Set Data bit3 to 1.

## Form 0x10EE: VR ICCMAX Current Override  ->  **IA ICC Max Current Limit Override** (numeric)
- VarStore: CpuSetup @ offset 0x347 | QuestionId 0x155A | size 16
- min 0x0 max 0x7FF
- help: IA Voltage Regulator Current Limit (Icc Max). This value represents the Maximum instantaneous current allowed at any given time. The value is represented in 1/4 A increments. A value of 400 = 100A. Range is 4 to 2047. Uses OC mailbox command 0x17

## Form 0x10EE: VR ICCMAX Current Override  ->  **IA ICC Unlimited Mode** (oneof)
- VarStore: CpuSetup @ offset 0x346 | QuestionId 0x3AC | size 8
- options: 
- help: Enable/Disable IA Unlimited ICCMAX. When Enabled, IA VR ICCMAX value is set to max ICC current 512A.

## Form 0x10EE: VR ICCMAX Current Override  ->  **GT ICC Max Current Limit Override** (numeric)
- VarStore: CpuSetup @ offset 0x34A | QuestionId 0x155B | size 16
- min 0x0 max 0x7FF
- help: GT Voltage Regulator Current Limit (Icc Max). This value represents the Maximum instantaneous current allowed at any given time. The value is represented in 1/4 A increments. A value of 400 = 100A. Range is 4 to 2047. Uses OC mailbox command 0x17

## Form 0x10EE: VR ICCMAX Current Override  ->  **GT ICC Unlimited Mode** (oneof)
- VarStore: CpuSetup @ offset 0x349 | QuestionId 0x3AD | size 8
- options: 
- help: Enable/Disable GT Unlimited ICCMAX. When Enabled, GT VR ICCMAX value is set to max ICC current 512A.

## Form 0x1028: Memory Configuration  ->  **Threshold For Switch Up** (numeric)
- VarStore: SaSetup @ offset 0x465 | QuestionId 0x41A | size 8
- min 0x1 max 0x32
- help: Duration In MS Of High Activity After Which SAGV Will Switch Up

## Form 0x1028: Memory Configuration  ->  **Threshold For Switch Down** (numeric)
- VarStore: SaSetup @ offset 0x466 | QuestionId 0x41B | size 8
- min 0x1 max 0x32
- help: Duration In MS Of Low Activity After Which SAGV Will Switch Down

## Form 0x1028: Memory Configuration  ->  **Power Down Mode** (oneof)
- VarStore: SaSetup @ offset 0x1A2 | QuestionId 0x140E | size 8
- options: 
- help: CKE Power Down Mode Control

## Form 0x1028: Memory Configuration  ->  **Training Tracing** (oneof)
- VarStore: SaSetup @ offset 0x191 | QuestionId 0x460 | size 8
- options: 
- help: Enables/Disables printing of the current trained state at every major training step.

## Form 0x1029: System Agent (SA) Configuration  ->  **Thermal Device (B0:D4:F0)** (oneof)
- VarStore: SaSetup @ offset 0x7C | QuestionId 0x475 | size 8
- options: 
- help: Enable/Disable SA Thermal Device. Always enabled for ICL A0 stepping.

## Form 0x101C: Memory Overclocking Menu  ->  **Memory profile** (oneof)
- VarStore: SaSetup @ offset 0x18D | QuestionId 0x112B | size 8
- options: 
- help: Select DIMM timing profile. The below values start with the currently running values and don't auto populate.

## Form 0x101C: Memory Overclocking Menu  ->  **OCSafeMode** (oneof)
- VarStore: SaSetup @ offset 0x478 | QuestionId 0x481 | size 8
- options: 
- help: OverClocking Safe Mode: When enabled, memory training uses less aggressive timing and algoes

## Form 0x101C: Memory Overclocking Menu  ->  **Memory Voltage** (numeric)
- VarStore: SaSetup @ offset 0x3 | QuestionId 0x484 | size 16
- min 0x0 max 0x7D0
- help: Memory Voltage Override (Vdd) at DRAM Side. 0 = no override

## Form 0x101C: Memory Overclocking Menu  ->  **Memory Voltage VDDQ** (numeric)
- VarStore: SaSetup @ offset 0x3F5 | QuestionId 0x485 | size 16
- min 0x0 max 0x7D0
- help: Memory Voltage Override (Vddq) at DRAM Side. 0 = no override

## Form 0x101C: Memory Overclocking Menu  ->  **Memory Voltage VPP** (numeric)
- VarStore: SaSetup @ offset 0x3F7 | QuestionId 0x486 | size 16
- min 0x0 max 0x8FC
- help: Memory Voltage Override (Vpp) at DRAM Side. 0 = no override

## Form 0x102A: Graphics Configuration  ->  **Graphics Turbo IMON Current** (numeric)
- VarStore: SaSetup @ offset 0xB8 | QuestionId 0x487 | size 8
- min 0xE max 0x1F
- help: Graphics turbo IMON current values supported (14-31)

## Form 0x102A: Graphics Configuration  ->  **Skip Scaning of External Gfx Card** (oneof)
- VarStore: SaSetup @ offset 0x256 | QuestionId 0x488 | size 8
- options: 
- help: If Enable, it will not scan for External Gfx Card on PEG and PCH PCIE Ports

## Form 0x102A: Graphics Configuration  ->  **Primary Display** (oneof)
- VarStore: SaSetup @ offset 0xB1 | QuestionId 0x489 | size 8
- options: 
- help: Select which of IGFX/PEG/PCI Graphics device should be Primary Display Or select HG for Hybrid Gfx.

## Form 0x102A: Graphics Configuration  ->  **HG Support** (oneof)
- VarStore: SaSetup @ offset 0x41B | QuestionId 0x48A | size 8
- options: 
- help: HG Support on PEG Port

## Form 0x102A: Graphics Configuration  ->  **Select PCIE Card** (oneof)
- VarStore: SaSetup @ offset 0xB2 | QuestionId 0x48B | size 8
- options: 
- help: Select the card used on the platform Auto       : Skip GPIO based Power Enable to dGPU Elk Creek 4: DGPU Power Enable = ActiveLow PEG Eval   : DGPU Power Enable = ActiveHigh

## Form 0x102A: Graphics Configuration  ->  **HG Delay After Power Enable** (numeric)
- VarStore: SaSetup @ offset 0xB3 | QuestionId 0x48C | size 16
- min 0x0 max 0x3E8
- help: Delay in milli-seconds after power enable

## Form 0x102A: Graphics Configuration  ->  **Primary Display** (oneof)
- VarStore: SaSetup @ offset 0xB1 | QuestionId 0x48E | size 8
- options: 
- help: Select which of IGFX/PEG/PCI Graphics device should be Primary Display Or select HG for Hybrid Gfx.

## Form 0x102E: GT - Power Management Control  ->  **Disable Turbo GT frequency** (oneof)
- VarStore: SaSetup @ offset 0x40 | QuestionId 0x4FF | size 8
- options: 
- help: Enabled: Disables Turbo GT frequency. Disabled: GT frequency is not limited

## Form 0x10E4: Memory Training Algorithms  ->  **Jedec Write Leveling** (oneof)
- VarStore: SaSetup @ offset 0x204 | QuestionId 0x505 | size 8
- options: 
- help: Jedec Write Leveling

## Form 0x10E4: Memory Training Algorithms  ->  **Write Voltage Centering 1D** (oneof)
- VarStore: SaSetup @ offset 0x208 | QuestionId 0x509 | size 8
- options: 

## Form 0x10E4: Memory Training Algorithms  ->  **Max RTT_WR** (oneof)
- VarStore: SaSetup @ offset 0x244 | QuestionId 0x50C | size 8
- options: 
- help: Caps the maximum RTT_WR in power training.

## Form 0x10E4: Memory Training Algorithms  ->  **Command Voltage Centering** (oneof)
- VarStore: SaSetup @ offset 0x213 | QuestionId 0x515 | size 8
- options: 
- help: Command Voltage Centering

## Form 0x10E4: Memory Training Algorithms  ->  **Write Voltage Centering 2D** (oneof)
- VarStore: SaSetup @ offset 0x214 | QuestionId 0x516 | size 8
- options: 
- help: Write Voltage Centering 2D

## Form 0x10E4: Memory Training Algorithms  ->  **Read Voltage Centering 2D** (oneof)
- VarStore: SaSetup @ offset 0x215 | QuestionId 0x517 | size 8
- options: 
- help: Read Voltage Centering 2D

## Form 0x10E4: Memory Training Algorithms  ->  **Read Voltage Centering 1D** (oneof)
- VarStore: SaSetup @ offset 0x248 | QuestionId 0x51D | size 8
- options: 
- help: Read Voltage Centering 1D

## Form 0x10E4: Memory Training Algorithms  ->  **Post Package Repair Training** (oneof)
- VarStore: SaSetup @ offset 0x47F | QuestionId 0x534 | size 8
- options: 
- help: Post Package Repair Training

## Form 0x10E4: Memory Training Algorithms  ->  **Margin Limit Check L2** (numeric)
- VarStore: SaSetup @ offset 0x3F1 | QuestionId 0x536 | size 16
- min 0x1 max 0x12C
- help: L2 check threshold is scale of L1 check. Ex. 200 is 2 x L1 Check

## Form 0x1048: Memory Thermal Configuration  ->  **Memory Thermal Management** (oneof)
- VarStore: SaSetup @ offset 0x22C | QuestionId 0x540 | size 8
- options: 
- help: Enable/Disable Memory Thermal Management.

## Form 0x10E8: Memory Power and Thermal Throttling  ->  **DDR PowerDown and idle counter** (oneof)
- VarStore: SaSetup @ offset 0x21F | QuestionId 0x545 | size 8
- options: 
- help: BIOS: BIOS is in control of DDR CKE mode and idle timer value. PCODE: pcode will manage the modes.

## Form 0x10E8: Memory Power and Thermal Throttling  ->  **For LPDDR Only: DDR PowerDown and idle counter** (oneof)
- VarStore: SaSetup @ offset 0x220 | QuestionId 0x546 | size 8
- options: 
- help: For LPDDR Only: BIOS: BIOS is in control of DDR CKE mode and idle timer value. PCODE: pcode will manage the modes.

## Form 0x10E8: Memory Power and Thermal Throttling  ->  **Allow Opp Ref Below Write Threhold** (oneof)
- VarStore: SaSetup @ offset 0x22A | QuestionId 0x54C | size 8
- options: 
- help: Allow opportunistic refreshes while we don't exit power down.

## Form 0x10E8: Memory Power and Thermal Throttling  ->  **Write Threshold** (numeric)
- VarStore: SaSetup @ offset 0x22B | QuestionId 0x54D | size 8
- min 0x0 max 0x3F
- help: Number of writes that can be accumulated while CKE is low before CKE is asserted.

## Form 0x8D: Link0 options  ->  **PMIC Position** (oneof)
- VarStore: Setup @ offset 0x207 | QuestionId 0x578 | size 8
- options: 
- help: PMIC Position Position 1 indicates the current module is placed on the left side of the CRD-G2 card Position 2 indicates the current module is placed on the right side of the CRD-G2 card

## Form 0x8D: Link0 options  ->  **Voltage Rail** (oneof)
- VarStore: Setup @ offset 0x208 | QuestionId 0x579 | size 8
- options: 
- help: Voltage Rail

## Form 0x8E: Link1 options  ->  **PMIC Position** (oneof)
- VarStore: Setup @ offset 0x28F | QuestionId 0x5A6 | size 8
- options: 
- help: PMIC Position Position 1 indicates the current module is placed on the left side of the CRD-G2 card Position 2 indicates the current module is placed on the right side of the CRD-G2 card

## Form 0x8E: Link1 options  ->  **Voltage Rail** (oneof)
- VarStore: Setup @ offset 0x290 | QuestionId 0x5A7 | size 8
- options: 
- help: Voltage Rail

## Form 0x8F: Link2 options  ->  **PMIC Position** (oneof)
- VarStore: Setup @ offset 0x317 | QuestionId 0x5D4 | size 8
- options: 
- help: PMIC Position Position 1 indicates the current module is placed on the left side of the CRD-G2 card Position 2 indicates the current module is placed on the right side of the CRD-G2 card

## Form 0x8F: Link2 options  ->  **Voltage Rail** (oneof)
- VarStore: Setup @ offset 0x318 | QuestionId 0x5D5 | size 8
- options: 
- help: Voltage Rail

## Form 0x90: Link3 options  ->  **PMIC Position** (oneof)
- VarStore: Setup @ offset 0x39F | QuestionId 0x602 | size 8
- options: 
- help: PMIC Position Position 1 indicates the current module is placed on the left side of the CRD-G2 card Position 2 indicates the current module is placed on the right side of the CRD-G2 card

## Form 0x90: Link3 options  ->  **Voltage Rail** (oneof)
- VarStore: Setup @ offset 0x3A0 | QuestionId 0x603 | size 8
- options: 
- help: Voltage Rail

## Form 0x91: Link4 options  ->  **PMIC Position** (oneof)
- VarStore: Setup @ offset 0x427 | QuestionId 0x630 | size 8
- options: 
- help: PMIC Position Position 1 indicates the current module is placed on the left side of the CRD-G2 card Position 2 indicates the current module is placed on the right side of the CRD-G2 card

## Form 0x91: Link4 options  ->  **Voltage Rail** (oneof)
- VarStore: Setup @ offset 0x428 | QuestionId 0x631 | size 8
- options: 
- help: Voltage Rail

## Form 0x92: Link5 options  ->  **PMIC Position** (oneof)
- VarStore: Setup @ offset 0x4AF | QuestionId 0x65E | size 8
- options: 
- help: PMIC Position Position 1 indicates the current module is placed on the left side of the CRD-G2 card Position 2 indicates the current module is placed on the right side of the CRD-G2 card

## Form 0x92: Link5 options  ->  **Voltage Rail** (oneof)
- VarStore: Setup @ offset 0x4B0 | QuestionId 0x65F | size 8
- options: 
- help: Voltage Rail

## Form 0x93: Control Logic options  ->  **WLED1 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0x6A | QuestionId 0x68B | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x93: Control Logic options  ->  **WLED1 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x6B | QuestionId 0x68C | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x93: Control Logic options  ->  **WLED2 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0x6C | QuestionId 0x68E | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x93: Control Logic options  ->  **WLED2 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x6D | QuestionId 0x68F | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x94: Control Logic options  ->  **WLED1 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0x9B | QuestionId 0x6B8 | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x94: Control Logic options  ->  **WLED1 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x9C | QuestionId 0x6B9 | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x94: Control Logic options  ->  **WLED2 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0x9D | QuestionId 0x6BB | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x94: Control Logic options  ->  **WLED2 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x9E | QuestionId 0x6BC | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x95: Control Logic options  ->  **WLED1 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0xCC | QuestionId 0x6E5 | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x95: Control Logic options  ->  **WLED1 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0xCD | QuestionId 0x6E6 | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x95: Control Logic options  ->  **WLED2 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0xCE | QuestionId 0x6E8 | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x95: Control Logic options  ->  **WLED2 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0xCF | QuestionId 0x6E9 | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x96: Control Logic options  ->  **WLED1 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0xFD | QuestionId 0x712 | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x96: Control Logic options  ->  **WLED1 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0xFE | QuestionId 0x713 | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x96: Control Logic options  ->  **WLED2 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0xFF | QuestionId 0x715 | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x96: Control Logic options  ->  **WLED2 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x100 | QuestionId 0x716 | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x97: Control Logic options  ->  **WLED1 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0x12E | QuestionId 0x73F | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x97: Control Logic options  ->  **WLED1 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x12F | QuestionId 0x740 | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x97: Control Logic options  ->  **WLED2 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0x130 | QuestionId 0x742 | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x97: Control Logic options  ->  **WLED2 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x131 | QuestionId 0x743 | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x98: Control Logic options  ->  **WLED1 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0x15F | QuestionId 0x76C | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x98: Control Logic options  ->  **WLED1 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x160 | QuestionId 0x76D | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x98: Control Logic options  ->  **WLED2 Flash Max Current** (numeric)
- VarStore: Setup @ offset 0x161 | QuestionId 0x76F | size 8
- min 0x0 max 0x1F
- help: WLED Flash Max Current Valid range is 0x00-0x1F 0x00 for HW default max current

## Form 0x98: Control Logic options  ->  **WLED2 Torch Max Current** (numeric)
- VarStore: Setup @ offset 0x162 | QuestionId 0x770 | size 8
- min 0x0 max 0x7
- help: WLED Torch Max Current Valid range is 0x00-0x07 0x00 for HW default max current

## Form 0x1582: PCI Express Root Port 1  ->  **PCI Express Power Gating** (oneof)
- VarStore: SaSetup @ offset 0x2A9 | QuestionId 0x802 | size 8
- options: 
- help: PCI Express Power Gating Enable/Disable for each root port.

## Form 0x1582: PCI Express Root Port 1  ->  **ASPM** (oneof)
- VarStore: SaSetup @ offset 0x379 | QuestionId 0x1586 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1583: PCI Express Root Port 2  ->  **PCI Express Power Gating** (oneof)
- VarStore: SaSetup @ offset 0x2AA | QuestionId 0x82B | size 8
- options: 
- help: PCI Express Power Gating Enable/Disable for each root port.

## Form 0x1583: PCI Express Root Port 2  ->  **ASPM** (oneof)
- VarStore: SaSetup @ offset 0x37A | QuestionId 0x1587 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1584: PCI Express Root Port 3  ->  **PCI Express Power Gating** (oneof)
- VarStore: SaSetup @ offset 0x2AB | QuestionId 0x854 | size 8
- options: 
- help: PCI Express Power Gating Enable/Disable for each root port.

## Form 0x1584: PCI Express Root Port 3  ->  **ASPM** (oneof)
- VarStore: SaSetup @ offset 0x37B | QuestionId 0x1588 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x102F: PCH-IO Configuration  ->  **SLP_LAN# Low on DC Power** (oneof)
- VarStore: PchSetup @ offset 0xD | QuestionId 0x890 | size 8
- options: 
- help: Enable/Disable SLP_LAN# Low on DC Power. Please notice this knob only applies to CNVd.

## Form 0x102F: PCH-IO Configuration  ->  **DeepSx Power Policies** (oneof)
- VarStore: PchSetup @ offset 0x4 | QuestionId 0x895 | size 8
- options: 
- help: configure the DeepSx Mode configuration.

## Form 0x102F: PCH-IO Configuration  ->  **PS_ON Enable** (oneof)
- VarStore: PchSetup @ offset 0x1E | QuestionId 0x896 | size 8
- options: 
- help: Enable or disable PS_ON ()support a new C10 state from the CPU on desktop SKUs that enables a lower power target that will be required by the California Energy Commission (CEC).

## Form 0x102F: PCH-IO Configuration  ->  **State After G3** (oneof)
- VarStore: PchSetup @ offset 0x20 | QuestionId 0x1094 | size 8
- options: 
- help: Specify what state to go to when power is re-applied after a power failure (G3 state).

## Form 0x102F: PCH-IO Configuration  ->  **Legacy IO Low Latency** (oneof)
- VarStore: PchSetup @ offset 0x76F | QuestionId 0x1416 | size 8
- options: 
- help: Set to enable low latency of legacy IO. Some systems require lower IO latency irrespective of power. This is a tradeoff between power and IO latency.

## Form 0x102F: PCH-IO Configuration  ->  **C10 Dynamic threshold adjustment** (oneof)
- VarStore: PchSetup @ offset 0x77D | QuestionId 0x8A7 | size 8
- options: 
- help: Enable/Disable C10 dynamic threshold adjustment

## Form 0x102F: PCH-IO Configuration  ->  **S0ix Auto Demotion** (oneof)
- VarStore: PchSetup @ offset 0x25 | QuestionId 0x8B3 | size 8
- options: 
- help: Enable/Disable Host Low Power Mode S0ix Auto-Demotion

## Form 0x1030: PCI Express Configuration  ->  **DMI Link ASPM Control** (oneof)
- VarStore: PchSetup @ offset 0x517 | QuestionId 0x1414 | size 8
- options: 
- help: The control of Active State Power Management of the DMI Link.

## Form 0x1031: USB Configuration  ->  **USB Overcurrent** (oneof)
- VarStore: PchSetup @ offset 0x43 | QuestionId 0x8DE | size 8
- options: 
- help: Select 'Disabled' for pin-based debug. If pin-based debug is enabled but USB overcurrent is not disabled, USB DbC does not work.

## Form 0x1031: USB Configuration  ->  **USB Overcurrent Lock** (oneof)
- VarStore: PchSetup @ offset 0x44 | QuestionId 0x8DF | size 8
- options: 
- help: Select 'Enabled' if Overcurrent functionality is used. Enabling this will make xHCI controller consume the Overcurrent mapping data

## Form 0x1031: USB Configuration  ->  **Enable HSII on xHCI** (oneof)
- VarStore: PchSetup @ offset 0x7F4 | QuestionId 0x8E1 | size 8
- options: 
- help: Enable/Disable HSII feature. It may lead to increased power consumption.

## Form 0x1032: SATA Configuration  ->  **Aggressive LPM Support** (oneof)
- VarStore: PchSetup @ offset 0x92 | QuestionId 0x900 | size 8
- options: 
- help: Enable PCH to aggressively enter link power state.

## Form 0x157C: PCI Express Root Port 1  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x11B | QuestionId 0x15E0 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1034: PCI Express Root Port 2  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x11C | QuestionId 0x15E1 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1035: PCI Express Root Port 3  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x11D | QuestionId 0x15E2 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1036: PCI Express Root Port 4  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x11E | QuestionId 0x15E3 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1037: PCI Express Root Port 5  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x11F | QuestionId 0x15E4 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1038: PCI Express Root Port 6  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x120 | QuestionId 0x15E5 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1039: PCI Express Root Port 7  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x121 | QuestionId 0x15E6 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x103A: PCI Express Root Port 8  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x122 | QuestionId 0x15E7 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x103B: PCI Express Root Port 9  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x123 | QuestionId 0x15E8 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13ED: PCI Express Root Port 10  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x124 | QuestionId 0x15E9 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13EE: PCI Express Root Port 11  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x125 | QuestionId 0x15EA | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13EF: PCI Express Root Port 12  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x126 | QuestionId 0x15EB | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F0: PCI Express Root Port 13  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x127 | QuestionId 0x15EC | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F1: PCI Express Root Port 14  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x128 | QuestionId 0x15ED | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F2: PCI Express Root Port 15  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x129 | QuestionId 0x15EE | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F3: PCI Express Root Port 16  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x12A | QuestionId 0x15EF | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F4: PCI Express Root Port 17  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x12B | QuestionId 0x15F0 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F5: PCI Express Root Port 18  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x12C | QuestionId 0x15F1 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F6: PCI Express Root Port 19  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x12D | QuestionId 0x15F2 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F7: PCI Express Root Port 20  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x12E | QuestionId 0x15F3 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x13F8: PCI Express Root Port 21  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x12F | QuestionId 0x15F4 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x157D: PCI Express Root Port 22  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x130 | QuestionId 0x15F5 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x157E: PCI Express Root Port 23  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x131 | QuestionId 0x15F6 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x157F: PCI Express Root Port 24  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x132 | QuestionId 0x15F7 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1587: PCI Express Root Port 25  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x133 | QuestionId 0x15F8 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1588: PCI Express Root Port 26  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x134 | QuestionId 0x15F9 | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x1589: PCI Express Root Port 27  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x135 | QuestionId 0x15FA | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x158A: PCI Express Root Port 28  ->  **ASPM** (oneof)
- VarStore: PchSetup @ offset 0x136 | QuestionId 0x15FB | size 8
- options: 
- help: PCI Express Active State Power Management settings.

## Form 0x152E: THC Configuration  ->  **HID Over SPI Limit Packet Size** (numeric)
- VarStore: PchSetup @ offset 0x7A4 | QuestionId 0xD0C | size 32
- min 0x0 max 0x1
- help: When set, limits SPI read & write packet size to 64B. Otherwise, THC uses Max Soc packet size for SPI Read and Write  0 - Max Soc Packet Size  1 - 64 Bytes

## Form 0x152E: THC Configuration  ->  **HID Over SPI Limit Packet Size** (numeric)
- VarStore: PchSetup @ offset 0x7A8 | QuestionId 0xD1C | size 32
- min 0x0 max 0x1
- help: When set, limits SPI read & write packet size to 64B. Otherwise, THC uses Max Soc packet size for SPI Read and Write  0 - Max Soc Packet Size  1 - 64 Bytes

## Form 0x103C: HD Audio Configuration  ->  **HDA Codec ALC245 Configuration** (oneof)
- VarStore: PchSetup @ offset 0x791 | QuestionId 0xD3C | size 8
- options: 
- help: Option for configuring DMIC connection to ALC245.

## Form 0x103F: HD Audio Advanced Configuration  ->  **Codec Sx Wake Capability** (oneof)
- VarStore: PchSetup @ offset 0x5A6 | QuestionId 0xD3E | size 8
- options: 
- help: Capability to detect wake initiated by a codec in Sx (eg by modem codec)

## Form 0x103F: HD Audio Advanced Configuration  ->  **HD Audio Link Frequency** (oneof)
- VarStore: PchSetup @ offset 0x5A3 | QuestionId 0xD40 | size 8
- options: 
- help: Selects HD Audio Link frequency. Applicable only if HDA codec supports selected frequency.

## Form 0x103F: HD Audio Advanced Configuration  ->  **ACX SSID 305610EC Codecs Topology** (oneof)
- VarStore: PchSetup @ offset 0x7FF | QuestionId 0xD4F | size 8
- options: 
- help: Codecs: ALC711-VD1, ALC714-VC1, 2x ALC316

## Form 0x1040: HD Audio DSP Features Configuration  ->  **I2S Es8326 24MHz** (oneof)
- VarStore: NhltEndpointsTableConfigurationVariable @ offset 0xB | QuestionId 0xD5A | size 8
- options: 
- help: Enables/Disables I2S Endpoint for Everest Codec 8326 and 8336 in NHLT ACPI table. XTAL: 24MHz.

## Form 0x1040: HD Audio DSP Features Configuration  ->  **I2S Codec Select** (oneof)
- VarStore: PchSetup @ offset 0x5B3 | QuestionId 0xD5B | size 8
- options: 
- help: Selects I2S Audio Codec support. Note: SerialIo UART0 must be disabled to enable external I2S codec (due to GPIO pin muxing).

## Form 0x1040: HD Audio DSP Features Configuration  ->  **I2S Codec Bus Number** (oneof)
- VarStore: PchSetup @ offset 0x5B4 | QuestionId 0xD5C | size 8
- options: 
- help: Selectcs Codec Bus from Serial IO I2C0/1/2/3/4/5

## Form 0x1040: HD Audio DSP Features Configuration  ->  **Voice Activity Detection** (oneof)
- VarStore: PchSetup @ offset 0x808 | QuestionId 0xD65 | size 8
- options: 
- help: Enables/Disables DSP Feature. Bitmask structure: [BIT0] - WoV [BIT1] - BT Sideband [BIT2] - Codec based VAD [BIT5] - BT Intel HFP [BIT6] - BT Intel A2DP [BIT7] - DSP based speech pre-processing disabled (for Intel WoV mode) [BIT8] - WoV Mode: Intel WoV / Windows Voice Activation for Cortana

## Form 0x7A: SerialIo Configuration  ->  **I2C0 Controller** (oneof)
- VarStore: PchSetup @ offset 0x705 | QuestionId 0xD83 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **I2C1 Controller** (oneof)
- VarStore: PchSetup @ offset 0x706 | QuestionId 0xD84 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **I2C2 Controller** (oneof)
- VarStore: PchSetup @ offset 0x707 | QuestionId 0xD85 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **I2C3 Controller** (oneof)
- VarStore: PchSetup @ offset 0x708 | QuestionId 0xD86 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **I2C6 Controller** (oneof)
- VarStore: PchSetup @ offset 0x70B | QuestionId 0xD89 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **I2C7 Controller** (oneof)
- VarStore: PchSetup @ offset 0x70C | QuestionId 0xD8A | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **SPI0 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6E0 | QuestionId 0xD8B | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **SPI1 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6E1 | QuestionId 0xD8C | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **SPI2 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6E2 | QuestionId 0xD8D | size 8
- options: 
- help: Enables/Disables SerialIo SPI2 Controller The following device depends from: Thermal Subsystem in PCI mode Otherwise SPI2 will not appear in the OS

## Form 0x7A: SerialIo Configuration  ->  **SPI3 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6E3 | QuestionId 0xD8E | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **SPI4 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6E4 | QuestionId 0xD8F | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **SPI5 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6E5 | QuestionId 0xD90 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **SPI6 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6E6 | QuestionId 0xD91 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **UART0 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6E9 | QuestionId 0xD92 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **UART1 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6EA | QuestionId 0xD93 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **UART2 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6EB | QuestionId 0xD94 | size 8
- options: 
- help: Set UART2 mode  - DBG used for BIOS log print and/or Kernel OS Debug   - COM - 16550 compatible serial port with Power Gating support

## Form 0x7A: SerialIo Configuration  ->  **UART3 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6EC | QuestionId 0xD95 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **UART4 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6ED | QuestionId 0xD96 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **UART5 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6EE | QuestionId 0xD97 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x7A: SerialIo Configuration  ->  **UART6 Controller** (oneof)
- VarStore: PchSetup @ offset 0x6EF | QuestionId 0xD98 | size 8
- options: 
- help: Enables/Disables SerialIo Controller If given device is Function 0 PSF disabling is skipped. PSF default will remain and device PCI CFG Space will still be visible. This is needed to allow PCI enumerator access functions above 0 in a multifunction device. The following devices depend on each other: I2C0 and I2C1,2,3 UART0 and UART1,SPI0,1 UART2 and I2C4,5   UART 0 (00:30:00) cannot be disabled when: 1. Child device is enabled like CNVi Bluetooth (\_SB.PC00.UA00.BTH0)  UART 0 (00:30:00) cannot be enabled when: 1. I2S Audio codec is enabled (\_SB.PC00.I2C0.HDAC)

## Form 0x84: Serial IO UART0 Settings  ->  **Power Gating** (oneof)
- VarStore: PchSetup @ offset 0x6FE | QuestionId 0xE37 | size 8
- options: 
- help: Disabled:  No _PS0 _PS3 support, device is left in D0, after initialization Enabled:  _PS0 _PS3 that supports getting device out of reset Auto:  _PS0 and _PS3 detection through ACPI if device was initialized prior to first PG. If it was used (DBG2) PG is disabled

## Form 0x85: Serial IO UART1 Settings  ->  **Power Gating** (oneof)
- VarStore: PchSetup @ offset 0x6FF | QuestionId 0xE3C | size 8
- options: 
- help: Disabled:  No _PS0 _PS3 support, device is left in D0, after initialization Enabled:  _PS0 _PS3 that supports getting device out of reset Auto:  _PS0 and _PS3 detection through ACPI if device was initialized prior to first PG. If it was used (DBG2) PG is disabled

## Form 0x8B: Serial IO UART2 Settings  ->  **Power Gating** (oneof)
- VarStore: PchSetup @ offset 0x700 | QuestionId 0xE41 | size 8
- options: 
- help: Disabled:  No _PS0 _PS3 support, device is left in D0, after initialization Enabled:  _PS0 _PS3 that supports getting device out of reset Auto:  _PS0 and _PS3 detection through ACPI if device was initialized prior to first PG. If it was used (DBG2) PG is disabled

## Form 0x13BE: Pch Thermal Throttling Control  ->  **Thermal Throttling Level** (oneof)
- VarStore: PchSetup @ offset 0x717 | QuestionId 0xE55 | size 8
- options: 
- help: Determine if use Intel suggested setting

## Form 0x13BE: Pch Thermal Throttling Control  ->  **DMI Thermal Setting** (oneof)
- VarStore: PchSetup @ offset 0x721 | QuestionId 0xE5C | size 8
- options: 
- help: Determine if use Intel suggested setting

## Form 0x13BE: Pch Thermal Throttling Control  ->  **Thermal Sensor 0 Width** (oneof)
- VarStore: PchSetup @ offset 0x722 | QuestionId 0xE5E | size 8
- options: 
- help: Determine the DMI Link Width when the output from the Thermal Sensor is T0

## Form 0x13BE: Pch Thermal Throttling Control  ->  **Thermal Sensor 1 Width** (oneof)
- VarStore: PchSetup @ offset 0x723 | QuestionId 0xE5F | size 8
- options: 
- help: Determine the DMI Link Width when the output from the Thermal Sensor is T1

## Form 0x13BE: Pch Thermal Throttling Control  ->  **Thermal Sensor 2 Width** (oneof)
- VarStore: PchSetup @ offset 0x724 | QuestionId 0xE60 | size 8
- options: 
- help: Determine the DMI Link Width when the output from the Thermal Sensor is T2

## Form 0x13BE: Pch Thermal Throttling Control  ->  **Thermal Sensor 3 Width** (oneof)
- VarStore: PchSetup @ offset 0x725 | QuestionId 0xE61 | size 8
- options: 
- help: Determine the DMI Link Width when the output from the Thermal Sensor is T3

## Form 0x13BE: Pch Thermal Throttling Control  ->  **SATA Thermal Setting** (oneof)
- VarStore: PchSetup @ offset 0x727 | QuestionId 0xE62 | size 8
- options: 
- help: Determine if use Intel suggested setting

## Form 0x13E1: FIVR Configuration  ->  **Off to High Current Mode** (numeric)
- VarStore: PchSetup @ offset 0x76B | QuestionId 0xE83 | size 16
- min 0x0 max 0x7FF
- help: Transition time in microseconds from Off (0V) to High Current Mode Voltage. This field has 1us resolution. 0 = Transition to 0V is disabled. The value must be greater than or equal to VccST board FET ramp time

## Form 0x1044: Anti-Rollback SVN Configuration  ->  **Set HW-Enforced Anti-Rollback for Current SVN** (oneof)
- VarStore: MeSetupStorage @ offset 0xB | QuestionId 0xEA9 | size 8
- options: 
- help: Enable hardware-enforced Anti-Rollback mechanism for current ARB-SVN value. FW with lower ARB-SVN will be blocked from execution. The value will be restored to disable after the command is sent.

## Form 0x1136: Local Platform Erase Configuration  ->  **SSD Erase Mode** (oneof)
- VarStore: LpeSetup @ offset 0x9 | QuestionId 0xEAA | size 8
- options: 
- help: Change LPE SSD Erase Action behavior: Simulated: Performs LPE SSD Erase flow without erasing SSD Real: Erase SSD. *** If SATA device is used, OEM could use SECURE_ERASE_HOOK_PROTOCOL to remove SATA power to skip G3 cycle. ***
