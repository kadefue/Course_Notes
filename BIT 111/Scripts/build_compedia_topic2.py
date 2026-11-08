#!/usr/bin/env python3
"""
build_compedia_topic2.py
Comprehensive Academic Compendium for:
BIT 111: Microcomputers and Applications
Topic 2: Main Components of a Microcomputer

Department of Informatics and Information Technology (DIIT),
School of Engineering and Technology / College of Natural and Applied Sciences,
Sokoine University of Agriculture (SUA), Morogoro, Tanzania.

Course Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Target Audience: First-Year Undergraduate Students across all SUA degree programs.
"""

import os
import sys

LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

SCRIPTS_DIR = "/home/kadefue/Course_Notes/BIT 111/Scripts"
if os.path.exists(SCRIPTS_DIR) and SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from compendium_base import (
    get_custom_stylesheet, create_callout_box, create_custom_table,
    NumberedCanvas, SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Image, KeepTogether, PageBreak, HRFlowable, letter, inch,
    COLOR_PRIMARY, COLOR_SUA_GREEN, COLOR_SUA_DARKGREEN, COLOR_TEXT,
    COLOR_BORDER, COLOR_BG_LIGHT, COLOR_WHITE, COLOR_MUTED
)

def generate_topic_2_story():
    styles = get_custom_stylesheet()
    story = []

    # Cover / Header Title Block
    header_data = [
        [Paragraph("SOKOINE UNIVERSITY OF AGRICULTURE", styles['CoverUniv'])],
        [Paragraph("School of Engineering and Technology / College of Natural and Applied Sciences", styles['CoverDept'])],
        [Paragraph("Department of Informatics and Information Technology (DIIT)", styles['CoverDept'])],
        [Spacer(1, 4)],
        [Paragraph("BIT 111: MICROCOMPUTERS AND APPLICATIONS", styles['CourseCode'])],
        [Paragraph("TOPIC 2: MAIN COMPONENTS OF A MICROCOMPUTER — LECTURE COMPENDIUM", styles['CourseTitle'])],
        [Paragraph(
            "<b>Course Instructor:</b> Madam Bertha Msuliche Lebalwa (MSc)<br/>"
            "<b>Department:</b> Informatics and Information Technology (DIIT), SUA Morogoro<br/>"
            "<b>Target Audience:</b> First-Year Undergraduate Students across all SUA Degree Programs<br/>"
            "<b>Disciplines Covered:</b> Agriculture, Agronomy, Animal Science, Veterinary Medicine, Wildlife Management, Tourism, Agricultural Engineering, Extension, Aquaculture, Forestry, Wood Science, Food Science, Consumer Studies<br/>"
            "<b>Curriculum Modules:</b> Input Devices (2.1) | Output Devices (2.2) | Central Processing Unit (2.3) | Memory Systems (2.4) | Comparative Aspects (2.5)<br/>"
            "<b>Official Assessment Scheme:</b> Two Assignments (5%), Two Theory Tests (15%), Practical Report (10%), Practical Test (30%), University Examination (40%)*<br/>"
            "<i>*Note: Assessment weightings are subject to adjustment by the course instructor.</i><br/>"
            "<b>Standard Academic Reference Edition</b> — Academic Year 2026/2027",
            styles['MetaBox']
        )]
    ]
    tbl = Table(header_data, colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_LIGHT),
        ('BOX', (0, 0), (-1, -1), 1.2, COLOR_PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 10))

    story.append(create_callout_box(
        "TOPIC ORIENTATION: DEMYSTIFYING THE PHYSICAL HARDWARE ENGINE",
        "Topic 2 explores the physical, tangible anatomy of the microcomputer system unit and its peripheral ecosystem. "
        "As first-year undergraduate scholars, you will look past the external casing of personal computers to understand how silicon microprocessors, volatile memory banks, high-capacity secondary storage drives, motherboards, expansion buses, and sensory input/output transducers collaborate to execute scientific and professional tasks. "
        "In strict alignment with university introductory guidelines, our study is 100% conceptual and architectural: you will master how hardware subsystems operate, interact, and fail without being subjected to engineering circuit equations, timing formulas, or clock cycle calculations.",
        styles,
        box_type='sua'
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>TOPIC 2 LEARNING OUTCOMES (BLOOM'S TAXONOMY ALIGNED)</b>", styles['SecH2']))
    story.append(Paragraph(
        "Upon thorough completion of Topic 2, first-year scholars will be able to:<br/>"
        "• <b>Identify & Locate:</b> Identify and describe the functional purpose of every major component inside the microcomputer system unit, including the CPU socket, RAM slots, PCIe expansion slots, power supply unit, and motherboard chipset.<br/>"
        "• <b>Explain CPU Architecture:</b> Explain the distinct roles of the Control Unit (CU), Arithmetic Logic Unit (ALU), internal registers, on-die cache hierarchies (L1/L2/L3), system clock concept, and multi-core processors without mathematical calculations.<br/>"
        "• <b>Distinguish Memory Tiers:</b> Differentiate between volatile primary memory (RAM: DRAM vs. SRAM, DDR evolution) and non-volatile memory (ROM: PROM, EPROM, EEPROM, flash UEFI/BIOS), as well as CMOS memory and its battery backup.<br/>"
        "• <b>Analyze Secondary Storage:</b> Compare magnetic storage (HDD platters, tracks, sectors), solid-state storage (NAND flash, SSDs, SATA vs. NVMe), and optical/removable media in terms of physical durability, access speed, and reliability.<br/>"
        "• <b>Classify I/O Devices:</b> Categorize input devices (keyboards, mice, scanners, RFID transponders, agricultural probes) and output devices (displays, printers, audio, actuators) based on physical operation and academic utility.<br/>"
        "• <b>Conduct Comparative Hardware Appraisals:</b> Evaluate architectural distinctions among microcomputers, technical workstations, departmental servers, and mainframes, as well as desktop vs. laptop design trade-offs.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 12))

    # =========================================================
    # SECTION 1: SYSTEM UNIT & MOTHERBOARD ARCHITECTURE
    # =========================================================
    story.append(Paragraph("1. THE SYSTEM UNIT AND MOTHERBOARD ARCHITECTURE", styles['SecH1']))
    story.append(Paragraph(
        "The <b>system unit</b> (often termed the chassis, case, or cabinet) is the primary physical enclosure that houses the critical electronic hardware components responsible for computing, memory, storage, and peripheral communication. In desktop systems, the system unit is an independent tower or desktop box; in laptops, tablets, and smartphones, the system unit is integrated into the same physical body as the display screen, keyboard, and battery.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "At the structural and electrical heart of the system unit lies the <b>motherboard</b> (also called the mainboard or system board). The motherboard is a multi-layered printed circuit board (PCB) that acts as the grand central nervous system of the computer. It provides physical mounting sockets, electrical power distribution traces, and high-speed communication bus pathways that interconnect the Central Processing Unit, primary RAM memory modules, secondary storage drives, graphics expansion cards, and external peripheral ports.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Core Motherboard Anatomy and Subsystems</b>", styles['SecH2']))
    story.append(Paragraph(
        "Every modern microcomputer motherboard integrates several essential structural and electronic subsystems:<br/>"
        "• <b>CPU Socket:</b> The specialized physical receptacle designed to hold the microprocessor chip securely. Desktop motherboards feature zero-insertion-force (ZIF) or land grid array (LGA) sockets with locking lever arms that secure the CPU pins against gold contacts, facilitating thermal transfer to an overhead heatsink and cooling fan.<br/>"
        "• <b>Memory Slots (DIMM / SO-DIMM):</b> Elongated sockets equipped with spring-loaded side clips that accept dual in-line memory modules (DIMMs) of Dynamic RAM. Desktop motherboards typically feature two to four DIMM slots supporting multi-channel memory configurations, whereas compact laptops utilize miniaturized SO-DIMM slots or have RAM chips soldered directly onto the board.<br/>"
        "• <b>Motherboard Chipset:</b> The integrated circuit architecture that manages data flow between the CPU, memory, high-speed graphics interfaces, and lower-speed peripheral buses. In modern systems, high-speed memory and PCIe lanes connect directly to the CPU silicon, while a secondary 'Platform Controller Hub' (PCH) chip coordinates SATA storage drives, USB ports, onboard audio, and Ethernet controllers.<br/>"
        "• <b>Expansion Slots (PCIe):</b> Peripheral Component Interconnect Express (PCIe) slots allow users to expand the system's capabilities by inserting specialized add-in cards. PCIe slots vary in physical length and lane bandwidth (PCIe x1 for sound or network cards, PCIe x4 for NVMe SSD carrier cards, and PCIe x16 for high-performance graphics processing units).<br/>"
        "• <b>Power Supply Connectors:</b> Standardized keyed multi-pin electrical sockets (such as the 24-pin ATX main power connector and 8-pin auxiliary CPU power connector) that deliver clean, regulated direct-current (DC) voltages from the Power Supply Unit (PSU) to energize the board's electronic circuits.<br/>"
        "• <b>Internal Storage Connectors:</b> Serial ATA (SATA) ports connecting traditional mechanical hard drives and 2.5-inch SSDs, along with ultra-compact <b>M.2 slots</b> that accept high-speed NVMe solid-state storage sticks mounted directly flat against the motherboard surface.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Table 2.1: Common Motherboard Form Factors and Operational Attributes</b>", styles['SecH3']))
    t1_data = [
        [
            Paragraph("Motherboard Form Factor", styles['TblHdr']),
            Paragraph("Physical Dimensions", styles['TblHdr']),
            Paragraph("RAM & PCIe Expansion Capacity", styles['TblHdr']),
            Paragraph("Typical Deployment Environment at SUA", styles['TblHdr'])
        ],
        [
            Paragraph("<b>Standard ATX</b>", styles['TblCellBold']),
            Paragraph("305 mm x 244 mm (Full-sized desktop)", styles['TblCell']),
            Paragraph("4 to 8 RAM slots; up to 7 PCIe expansion slots; maximum upgradeability", styles['TblCell']),
            Paragraph("Technical GIS workstations in Department of Forestry; institutional departmental research servers.", styles['TblCell'])
        ],
        [
            Paragraph("<b>Micro-ATX (mATX)</b>", styles['TblCellBold']),
            Paragraph("244 mm x 244 mm (Square compact)", styles['TblCell']),
            Paragraph("2 to 4 RAM slots; 2 to 4 PCIe slots; balanced footprint and cost", styles['TblCell']),
            Paragraph("DIIT undergraduate instructional computer laboratories; administrative office desktop towers.", styles['TblCell'])
        ],
        [
            Paragraph("<b>Mini-ITX</b>", styles['TblCellBold']),
            Paragraph("170 mm x 170 mm (Ultra-compact)", styles['TblCell']),
            Paragraph("2 SO-DIMM/DIMM slots; single PCIe x16 slot; space-constrained", styles['TblCell']),
            Paragraph("Space-saving reception desk PCs; portable field station computing units; laboratory instrument controllers.", styles['TblCell'])
        ],
        [
            Paragraph("<b>Proprietary Mobile / SBC</b>", styles['TblCellBold']),
            Paragraph("Custom irregular layout / credit-card size", styles['TblCell']),
            Paragraph("RAM soldered on-board; zero PCIe slots; fixed internal hardware", styles['TblCell']),
            Paragraph("Student laptops and tablets; solar-powered weather stations; Raspberry Pi automated irrigation nodes.", styles['TblCell'])
        ]
    ]
    t1_table = Table(t1_data, colWidths=[1.6 * inch, 1.6 * inch, 2.0 * inch, 2.0 * inch])
    t1_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SUA_GREEN),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_WHITE, COLOR_BG_LIGHT]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t1_table)
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 2: CENTRAL PROCESSING UNIT IN DEPTH
    # =========================================================
    story.append(Paragraph("2. THE CENTRAL PROCESSING UNIT (CPU) IN DEPTH", styles['SecH1']))
    story.append(Paragraph(
        "The <b>Central Processing Unit (CPU)</b> is the primary microelectronic semiconductor engine responsible for interpreting software instructions, executing logical decisions, performing mathematical calculations, and orchestrating the operational timing of the entire computer. In modern microcomputers, the CPU is fabricated as a single monolithic microprocessor chip containing hundreds of millions, or billions, of microscopic transistors etched onto a silicon wafer.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Architectural Subsystems of the Microprocessor</b>", styles['SecH2']))
    story.append(Paragraph(
        "A modern microprocessor silicon die is partitioned into several distinct, highly coordinated functional functional blocks:<br/>"
        "1. <b>Control Unit (CU):</b> The executive supervisor of the chip. The CU coordinates instruction fetching from memory, decodes binary operation codes, manages the sequencing of internal execution stages, and issues synchronized electrical control signals that instruct the ALU, registers, and memory controllers on how to respond.<br/>"
        "2. <b>Arithmetic Logic Unit (ALU):</b> The computational powerhouse that executes two primary categories of operations: (a) <i>Arithmetic computations</i> (fundamental addition, subtraction, multiplication, and division), and (b) <i>Logical evaluations</i> (comparisons such as testing whether a milk somatic cell count exceeds a disease threshold, as well as Boolean operations like AND, OR, NOT).<br/>"
        "3. <b>Internal Processor Registers:</b> Extremely fast, microscopic temporary storage cells built directly into the processor silicon right beside the execution circuits. Registers provide instant, zero-wait-state access to immediate operands and operational flags. Essential registers include:<br/>"
        "   • <i>Program Counter (PC):</i> Holds the primary memory address of the next sequential program instruction to be fetched.<br/>"
        "   • <i>Instruction Register (IR):</i> Stores the binary bit pattern of the instruction currently undergoing decoding and execution.<br/>"
        "   • <i>Memory Address Register (MAR):</i> Holds the physical RAM memory address that the CPU desires to read from or write to.<br/>"
        "   • <i>Memory Buffer Register (MBR / MDR):</i> Holds the actual data byte retrieved from RAM or about to be written into RAM.<br/>"
        "   • <i>Accumulator (AC):</i> Holds intermediate mathematical or logical results produced by the ALU.<br/>"
        "   • <i>Status / Flags Register:</i> Contains individual binary condition bits that record operational outcomes (e.g., zero result, arithmetic overflow, sign flag, parity).",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>The System Clock and Frequency Concept (Without Equations)</b>", styles['SecH2']))
    story.append(Paragraph(
        "Every digital microcomputer incorporates an internal <b>system clock</b>—a microscopic quartz crystal oscillator circuit located on the motherboard or integrated into the CPU chipset. When an electrical voltage is applied to the quartz crystal, it vibrates at an extraordinarily steady, precise physical frequency, generating continuous electronic square-wave voltage pulses.<br/>"
        "Conceptually, the system clock acts like the steady, rhythmic beat of a conductor's baton or an orchestra metronome. Every microscopic micro-operation within the CPU—fetching an instruction byte, latching a register, or gating an ALU calculation—must be synchronized to occur during these discrete clock ticks. Clock speed is measured in <b>Gigahertz (GHz)</b>, a unit used to describe the frequency of those pulses.<br/>"
        "<i>Introductory Conceptual Principle:</i> First-year students should note that while higher clock frequency allows a processor to execute more operational steps per second, clock speed alone does not determine overall computer performance. Architectural efficiency—such as how many instructions a CPU can complete per clock cycle, the size of on-chip cache memory, and the number of physical cores—plays an equally decisive role.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Multi-Core Processor Architecture</b>", styles['SecH2']))
    story.append(Paragraph(
        "In earlier decades, processor manufacturers increased computing performance primarily by engineering microprocessors to run at higher and higher clock frequencies. However, in the mid-2000s, engineers encountered physical thermal and electrical limits: running silicon chips beyond 3.8 to 4.0 GHz caused excessive electrical leakage and generated extreme thermal heat that could not be cooled reliably with conventional air heatsinks.<br/>"
        "To continue expanding computational power, the industry pivoted to <b>multi-core architectures</b>. Instead of building a single colossal CPU core running at blistering clock speeds, engineers placed two, four, eight, or more complete, independent physical CPU execution cores onto the very same piece of silicon (or inside a single multi-chip processor package).<br/>"
        "• <i>Dual-Core:</i> Contains two independent physical execution cores.<br/>"
        "• <i>Quad-Core:</i> Contains four independent physical cores, standard in modern student laptops.<br/>"
        "• <i>Octa-Core:</i> Contains eight physical execution cores, common in high-performance laptops and smartphones.<br/>"
        "• <i>Many-Core (16 to 64+ cores):</i> Deployed in technical workstations and servers (e.g., AMD Threadripper, Intel Xeon).<br/>"
        "<i>Conceptual Benefit:</i> A multi-core processor can execute several independent software programs or computational threads simultaneously in true physical parallel. For example, a student's laptop can run an antivirus background scan on Core 1, stream an agricultural lecture video on Core 2, download a scientific journal article on Core 3, and format a word-processing document on Core 4 without system stutter or slowdown.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>On-Chip Cache Memory Hierarchy (L1, L2, L3)</b>", styles['SecH2']))
    story.append(Paragraph(
        "Fetching data from main primary memory (RAM) across external motherboard buses is a comparatively slow operation that forces the fast CPU to wait in idle cycles. To solve this dilemma, microprocessors incorporate a multi-tiered hierarchy of <b>cache memory</b>—microscopic banks of ultra-fast Static RAM (SRAM) integrated directly onto the CPU die right beside the execution units:<br/>"
        "• <b>Level 1 Cache (L1):</b> The smallest, fastest, and most immediate cache tier, built directly into each individual processor core. L1 cache is typically partitioned into two dedicated segments: an <i>L1 Instruction Cache</i> and an <i>L1 Data Cache</i> (each 32 to 64 KB per core). It operates at the full physical clock speed of the processor core with zero wait states.<br/>"
        "• <b>Level 2 Cache (L2):</b> A slightly larger, fast cache bank (typically 512 KB to 2 MB per core) dedicated to each core, holding instructions and data that overflow from L1.<br/>"
        "• <b>Level 3 Cache (L3):</b> A substantial, shared cache pool (ranging from 8 MB to 64 MB or more) shared collectively by all cores on the processor die. When a core needs an instruction or piece of data, it checks L1 first; if not found (a 'cache miss'), it checks L2, then L3. Only if the data is absent from all three cache tiers does the CPU incur the performance penalty of reaching out across external buses to main RAM.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 3: PRIMARY STORAGE SUBSYSTEMS (RAM & ROM)
    # =========================================================
    story.append(Paragraph("3. PRIMARY STORAGE SUBSYSTEMS: RAM, ROM, AND CMOS", styles['SecH1']))
    story.append(Paragraph(
        "<b>Primary storage</b> (also referred to as main memory or internal memory) represents the high-speed electronic storage tier directly addressable and accessible by the Central Processing Unit. Primary storage is divided into two fundamentally distinct technological categories: volatile <b>Random Access Memory (RAM)</b> and non-volatile <b>Read-Only Memory (ROM)</b>.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Random Access Memory (RAM)</b>", styles['SecH2']))
    story.append(Paragraph(
        "RAM is the active computational workspace of the computer. Whenever you launch an operating system, open a web browser, or edit an agricultural spreadsheet, the program instructions and data files are copied from slow secondary storage into RAM so the CPU can access them at nanosecond speeds. RAM is termed 'Random Access' because any individual memory cell can be accessed directly in the exact same amount of time, regardless of its physical position on the chip.<br/>"
        "• <b>Dynamic RAM (DRAM):</b> The technology utilized for standard system main memory. Each DRAM memory cell consists of a single microscopic transistor and capacitor. Because capacitors leak electrical charge within milliseconds, DRAM must be continuously refreshed with electrical recharge pulses hundreds of times per second. DRAM provides high storage density at low manufacturing cost.<br/>"
        "• <b>Static RAM (SRAM):</b> Constructed from flip-flop circuits consisting of four to six transistors per bit. SRAM does not leak charge and requires no continuous refresh cycles. It is significantly faster than DRAM but is physically larger, more complex, and vastly more expensive. It is used exclusively for on-chip CPU cache memory (L1, L2, L3).<br/>"
        "• <b>The Synchronous Dynamic RAM (DDR) Evolution:</b> System RAM has evolved through successive generations of Double Data Rate (DDR) technology, which transfers data on both the rising and falling edges of the clock signal. Generations have progressed from original DDR to DDR2, DDR3, DDR4, and contemporary <b>DDR5</b>, with each generation doubling data transfer bandwidth while lowering operational operating voltage (from 2.5V down to 1.1V), conserving laptop battery life.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Read-Only Memory (ROM) and Motherboard Firmware</b>", styles['SecH2']))
    story.append(Paragraph(
        "Unlike volatile RAM, <b>Read-Only Memory (ROM)</b> is strictly <i>non-volatile</i>; its contents are permanently burned or flashed into the silicon circuitry and remain intact even when electrical power is disconnected. ROM stores foundational system startup firmware:<br/>"
        "• <b>BIOS (Basic Input/Output System):</b> The traditional legacy firmware interface that executes the Power-On Self-Test (POST) and initializes fundamental keyboard, display, and storage hardware.<br/>"
        "• <b>UEFI (Unified Extensible Firmware Interface):</b> The modern firmware specification that supersedes legacy BIOS. UEFI supports large storage drives (over 2 Terabytes via GUID Partition Tables), graphical mouse-driven setup menus, faster boot times, and <i>Secure Boot</i> (which cryptographically verifies operating system signatures to prevent boot-sector rootkits).<br/>"
        "• <i>Evolutionary Types of ROM:</i> Historically, ROM progressed from factory-masked ROM (unalterable) to <b>PROM</b> (Programmable ROM, writable once by a technician), <b>EPROM</b> (Erasable Programmable ROM, erasable under ultraviolet light), and modern <b>EEPROM / Flash Memory</b> (Electrically Erasable Programmable ROM), which allows firmware to be updated ('flashed') electronically via software without removing chips from the motherboard.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>CMOS RAM and the Real-Time Clock (RTC)</b>", styles['SecH2']))
    story.append(Paragraph(
        "Modern motherboards feature a tiny bank of volatile memory known as <b>CMOS RAM</b> (Complementary Metal-Oxide Semiconductor), which stores user-configured firmware settings—such as hardware boot priority order, processor virtualization settings, and security passwords. Adjacent to CMOS is the <b>Real-Time Clock (RTC)</b> chip, an electronic clock that maintains accurate wall-clock date and time even when the computer is completely unplugged from wall power.<br/>"
        "To prevent CMOS settings and the RTC from losing data during power-off, the motherboard incorporates a small coin-shaped 3-volt lithium battery (typically a <b>CR2032 battery</b>). If this battery expires after several years of service, the computer will reset its system date to a default historical year (e.g., January 1, 2000) and display a 'CMOS Checksum Error' during startup.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 4: SECONDARY STORAGE SUBSYSTEMS
    # =========================================================
    story.append(Paragraph("4. SECONDARY STORAGE SUBSYSTEMS", styles['SecH1']))
    story.append(Paragraph(
        "Because primary memory (RAM) is volatile and relatively expensive per gigabyte, computers require <b>secondary storage</b> to retain software operating systems, installed applications, research databases, student documents, and multimedia permanently. Secondary storage is non-volatile, possesses vast storage capacity, and preserves digital files indefinitely without electrical current.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>1. Magnetic Storage: Hard Disk Drives (HDD)</b>", styles['SecH2']))
    story.append(Paragraph(
        "A <b>Hard Disk Drive (HDD)</b> is an electro-mechanical storage device that records digital data magnetically on high-speed rotating metallic or glass platters coated with a microscopic magnetic layer. Within the sealed drive enclosure, platters spin continuously at standardized rotational speeds—typically 5,400 or 7,200 revolutions per minute (RPM) in consumer systems, and 10,000 to 15,000 RPM in enterprise enterprise servers.<br/>"
        "• <i>Physical Organization:</i> The surface of each platter is formatted into concentric circular rings called <b>tracks</b>, which are segmented into smaller pie-shaped sectors (conventionally storing 512 bytes or modern 4,096-byte Advanced Format sectors). Vertically aligned tracks across all platter surfaces form a <b>cylinder</b>.<br/>"
        "• <i>Read/Write Heads:</i> Electromagnetic heads mounted on a movable actuator arm glide on an aerodynamic air cushion mere nanometers above the spinning platter surface, magnetizing microscopic domains to record binary 1s and 0s, or detecting magnetic fields to read data.<br/>"
        "• <i>Mechanical Vulnerability:</i> Because HDDs rely on high-precision moving parts, they are vulnerable to physical shock. If a running laptop is dropped, the heads can physically strike the platter surface (a catastrophic 'head crash'), permanently gouging the magnetic coating and destroying stored data.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>2. Solid-State Storage: Solid-State Drives (SSD)</b>", styles['SecH2']))
    story.append(Paragraph(
        "A <b>Solid-State Drive (SSD)</b> is a high-speed non-volatile secondary storage device constructed entirely from semiconductor <b>NAND flash memory</b> chips and an onboard micro-controller, with zero moving mechanical parts.<br/>"
        "• <i>Architectural Superiority:</i> Because there are no spinning platters or movable actuator arms, SSDs provide near-instantaneous access speeds, silent operation, minimal heat generation, lower electrical power draw, and total physical immunity to mechanical drops and vibrations.<br/>"
        "• <i>SATA SSDs vs. NVMe M.2 SSDs:</i> Early SSDs utilized the legacy SATA interface (limited to roughly 550 MB/s throughput due to older hard disk cabling protocols). Modern microcomputers utilize <b>NVMe (Non-Volatile Memory Express) SSDs</b> mounted in ultra-compact M.2 slots directly on the motherboard. NVMe drives communicate over high-speed PCI Express lanes, delivering data transfer throughputs exceeding 3,500 to 7,000 MB/s—accelerating operating system boot times from 45 seconds down to under 8 seconds.<br/>"
        "• <i>Wear Leveling:</i> NAND flash memory cells can withstand a finite number of write/erase cycles before degrading. Modern SSD controllers implement sophisticated <i>wear-leveling algorithms</i> that distribute new data writes evenly across all physical flash memory blocks, ensuring SSD lifespans exceeding a decade of typical university and scientific use.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>3. Optical and Removable Storage Media</b>", styles['SecH2']))
    story.append(Paragraph(
        "• <b>Optical Storage (CD, DVD, Blu-ray):</b> Discs that store binary data physically as microscopic microscopic indentations (<b>pits</b>) and flat reflective spaces (<b>lands</b>) molded into a polycarbonate plastic disc layer. An optical drive's laser beam shines against the disc, detecting binary states based on the light reflection detected by a photodiode. While largely superseded by USB flash drives, optical discs remain valuable for long-term historical archives and distribution of educational media.<br/>"
        "• <b>USB Flash Drives & SD Cards:</b> Portable, pocket-sized flash storage devices connecting via USB ports or camera memory slots. They represent the primary medium undergraduate students use to transport assignments, course notes, and presentation slide decks between campus laboratories and personal dormitories.<br/>"
        "• <b>Cloud Storage Services:</b> Remote, off-site secondary storage repositories hosted in commercial enterprise data centers (e.g., Google Drive, Microsoft OneDrive, Dropbox) accessed across the Internet, enabling collaborative sharing and offsite backup protection.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 5: INPUT DEVICES AND SENSORY TRANSDUCERS
    # =========================================================
    story.append(Paragraph("5. INPUT DEVICES AND SENSORY TRANSDUCERS", styles['SecH1']))
    story.append(Paragraph(
        "An <b>input device</b> is any hardware peripheral or electronic transducer that captures physical actions, mechanical movements, optical patterns, audio waves, or biological/environmental signals from the physical world and converts them into digital binary representations (zeros and ones) that the computer system can interpret and process.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Primary Categories of Input Peripherals</b>", styles['SecH2']))
    story.append(Paragraph(
        "1. <b>Keyboards:</b> The primary alphanumeric text entry peripheral. Most international keyboards utilize the standardized <b>QWERTY</b> layout (named after the first six letters on the top alphabetic row). Modern keyboards employ either low-cost <i>membrane switches</i> (where keypresses push a conductive rubber dome against a printed circuit sheet) or high-durability <i>mechanical switches</i> (featuring individual spring-loaded physical mechanical contacts favored for heavy typing durability).<br/>"
        "2. <b>Pointing Devices:</b> Peripherals that control the motion of a visual on-screen pointer or cursor within a Graphical User Interface:<br/>"
        "   • <i>Optical Mouse:</i> Emits a tiny LED or laser light downward against a desk surface; an internal microscopic camera captures thousands of surface images per second, tracking movement via optical digital signal processing.<br/>"
        "   • <i>Touchpad (Trackpad):</i> A flat, touch-sensitive capacitive surface integrated into laptops that tracks the electrical properties of the user's fingertips, supporting multi-touch gestures (pinching to zoom, two-finger scrolling).<br/>"
        "   • <i>Touchscreen Displays:</i> Combines visual output with direct capacitive touch input, enabling intuitive direct manipulation on smartphones, tablets, and field computers.<br/>"
        "3. <b>Optical Scanners and Barcode / QR Readers:</b> Devices that capture physical optical information:<br/>"
        "   • <i>Flatbed Optical Scanners:</i> Use an array of Charge-Coupled Devices (CCD) and a bright moving light bar to capture high-resolution digital images of paper documents, botanical leaf specimens, or soil survey maps.<br/>"
        "   • <i>Optical Character Recognition (OCR):</i> Software algorithms that analyze scanned raster images and convert photographed printed text into editable, searchable digital word-processing documents.<br/>"
        "   • <i>Barcode and QR Code Readers:</i> Optical scanners that decode 1D linear bars or 2D Quick Response matrix patterns, universally deployed in agricultural seed warehouses, supermarket retail checkouts, and laboratory specimen tracking.<br/>"
        "4. <b>Radio-Frequency Identification (RFID) and Biometric Readers:</b><br/>"
        "   • <i>RFID Transceivers:</i> Wireless readers that emit radio-frequency electromagnetic fields to power and query passive transponder chips embedded within animal ear tags (at the SUA Magadu Dairy Farm), library books (at SNAL), or automated campus gate passes.<br/>"
        "   • <i>Biometric Sensors:</i> Hardware scanners that measure unique physical biological traits—such as optical or capacitive fingerprint scanners, facial geometry cameras, and retinal scanners—used for tamper-proof student exam attendance and secure computer login authentication.<br/>"
        "5. <b>Specialized Agricultural and Environmental Sensor Probes:</b> In precision farming and natural sciences, input devices extend beyond human peripherals to electronic transducers: soil volumetric moisture sensors, multi-spectral drone cameras, dissolved oxygen electrodes in fish ponds, and ultrasonic tree height hypsometers in forestry research.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 6: OUTPUT DEVICES AND VISUAL DISPLAYS
    # =========================================================
    story.append(Paragraph("6. OUTPUT DEVICES AND VISUAL DISPLAYS", styles['SecH1']))
    story.append(Paragraph(
        "An <b>output device</b> is any hardware component that translates digital binary data processed by the computer into human-perceptible formats—such as visual text and images on a screen, ink on physical paper, audible sound waves—or converts data into physical electrical control signals that drive mechanical actuators.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Visual Display Technologies</b>", styles['SecH2']))
    story.append(Paragraph(
        "The visual display monitor is the most fundamental output device for human interaction. Screen images are formed by millions of microscopic picture elements called <b>pixels</b>, arranged in a rectangular grid:<br/>"
        "• <b>Liquid Crystal Displays (LCD) with LED Backlighting:</b> Modern flat-panel monitors pass electrical current through liquid crystal molecules that twist and untwist to block or permit light passing from an array of bright, energy-efficient Light-Emitting Diodes (LEDs) positioned behind or along the edges of the panel. LED-backlit LCDs offer exceptional brightness, slim profiles, and low power consumption.<br/>"
        "• <b>Organic Light-Emitting Diode (OLED) Displays:</b> Premium display panels where every individual pixel is an organic semiconductor compound that emits its own light when electrified. Because OLED pixels can be switched off completely, they deliver true infinite black levels, extraordinary contrast ratios, and vibrant color accuracy favored for professional photography and satellite imagery review.<br/>"
        "• <b>Display Metrics:</b> (a) <i>Resolution:</i> The number of horizontal and vertical pixels (e.g., Full HD: 1920 x 1080 pixels; 4K UHD: 3840 x 2160 pixels); (b) <i>Aspect Ratio:</i> The proportional relationship between screen width and height (standard widescreen is 16:9); (c) <i>Refresh Rate:</i> The frequency (measured in Hertz, Hz) with which the screen image is redrawn per second (standard office monitors refresh at 60 Hz).",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Printers and Hard-Copy Output Peripherals</b>", styles['SecH2']))
    story.append(Paragraph(
        "Printers generate permanent, physical hard-copy records on paper media. Printers are broadly divided into two foundational technological families:<br/>"
        "• <b>Impact Printers (Dot-Matrix):</b> Print by physically striking an inked ribbon against paper using an array of tiny mechanical pins or hammers. While noisy and producing low-resolution text, dot-matrix printers remain indispensable in agricultural produce buying centers, grain silos, and warehouse dispatch docks because their physical impact can print through multi-part carbon-copy multipart forms.<br/>"
        "• <b>Non-Impact Printers:</b> Form images without physical pins striking paper:<br/>"
        "  1. <i>Inkjet Printers:</i> Spray microscopic droplets of liquid ink from microscopic nozzles onto paper with extraordinary precision. Inkjets produce vibrant, photographic color prints at low initial purchase cost, making them ideal for small offices and student dormitories; however, liquid ink cartridges are expensive per page, and ink can smudge if exposed to water.<br/>"
        "  2. <i>Laser Printers:</i> Utilize an electrostatic xerographic process: a laser beam draws an electrostatic latent image onto a rotating photosensitive drum; negatively charged powdered plastic toner clings to the drum's exposed areas; the drum rolls toner onto paper, and heated ceramic fuser rollers permanently melt and press the plastic toner into the paper fibers. Laser printers are the workhorses of university computer labs and administrative offices, delivering sharp, waterproof black text at blistering speeds and very low operating cost per page.<br/>"
        "  3. <i>Wide-Format Plotters:</i> Specialized large-format printers that utilize rolls of heavy paper (up to 44 or 60 inches wide) to output massive architectural blueprints, topographic catchment maps for forestry, and student scientific conference posters.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Audio Output and Physical Actuators</b>", styles['SecH2']))
    story.append(Paragraph(
        "• <b>Audio Output:</b> Built-in stereo speakers, headphones, and audio jacks driven by an onboard sound card that converts digital audio bitstreams into analog electrical currents that vibrate speaker cones, providing acoustic feedback, lecture multimedia playback, and system error alerts.<br/>"
        "• <b>Physical Actuators:</b> In automated agricultural engineering and smart biology labs, output extends to electromechanical actuators. Digital output voltages trigger electronic relays that switch on high-voltage electrical water pumps, open automated greenhouse ventilation louvers, trigger motorized livestock feed augers, or activate cold-chain compressor cooling units.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 7: EXPANSION BUSES, PORTS, AND CONNECTIVITY
    # =========================================================
    story.append(Paragraph("7. EXPANSION BUSES, PORTS, AND MOTHERBOARD CONNECTIVITY", styles['SecH1']))
    story.append(Paragraph(
        "The ability of a microcomputer to adapt to specialized research, engineering, and laboratory applications depends upon its <b>expansion buses</b> and standardized external <b>ports</b>.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Peripheral Component Interconnect Express (PCIe)</b>", styles['SecH2']))
    story.append(Paragraph(
        "PCIe is the reigning high-speed serial expansion bus architecture on modern motherboards. Rather than using older, slow parallel buses where data lines suffered electrical interference, PCIe transmits data serially across dedicated point-to-point connections called <b>lanes</b>. Expansion slots are scaled by the number of lanes: PCIe x1 (single lane for Wi-Fi or sound cards), PCIe x4 (four lanes for high-speed NVMe SSD carrier cards), and PCIe x16 (sixteen lanes dedicated to high-bandwidth graphics processing units). PCIe generations (Gen 3, Gen 4, Gen 5) double data throughput per lane with each successive evolutionary step.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Standardized External Ports and Interfacing Standards</b>", styles['SecH2']))
    story.append(Paragraph(
        "• <b>USB Standard:</b> Universal Serial Bus enables hot-swappable, plug-and-play peripheral connectivity. USB Type-A remains standard for legacy peripherals, while modern USB Type-C provides a reversible, high-speed interface capable of transmitting data, digital video, and DC charging power simultaneously.<br/>"
        "• <b>High-Definition Multimedia Interface (HDMI):</b> Carries uncompressed digital audio and high-resolution video across a single cable to monitors and classroom digital projectors.<br/>"
        "• <b>DisplayPort (DP):</b> The preferred digital video standard on high-end desktop workstations, supporting multiple daisy-chained high-resolution monitors.<br/>"
        "• <b>RJ-45 Ethernet:</b> Connects the workstation to the campus local area network (LAN) via Cat6 twisted-pair copper cabling, providing robust Gigabit data transfer immune to Wi-Fi signal interference.<br/>"
        "• <b>Legacy Serial (RS-232) and Parallel Ports:</b> While phased out of consumer laptops, RS-232 serial ports remain critically important in agricultural laboratories for interfacing with legacy scientific instruments, autoclave data loggers, and automated weather station telemetry modems.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 8: COMPARATIVE HARDWARE ASPECTS
    # =========================================================
    story.append(Paragraph("8. COMPARATIVE HARDWARE ARCHITECTURAL ASPECTS", styles['SecH1']))
    story.append(Paragraph(
        "To make informed procurement and operational decisions in their scientific and professional careers, first-year scholars must comprehend how microcomputers compare architecturally to other computing classes and evaluate internal hardware trade-offs.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Table 2.2: Comprehensive Matrix of Comparative Hardware Aspects</b>", styles['SecH3']))
    t2_data = [
        [
            Paragraph("Comparative Dimension", styles['TblHdr']),
            Paragraph("Standard Microcomputer (PC)", styles['TblHdr']),
            Paragraph("Technical Workstation", styles['TblHdr']),
            Paragraph("Minicomputer / Server", styles['TblHdr']),
            Paragraph("Enterprise Mainframe", styles['TblHdr'])
        ],
        [
            Paragraph("<b>Processor Architecture</b>", styles['TblCellBold']),
            Paragraph("Single consumer-grade CPU (4 to 8 cores, e.g., Core i5/i7, Ryzen 5/7)", styles['TblCell']),
            Paragraph("High-end multi-core CPU (12 to 64 cores, e.g., Xeon, Threadripper)", styles['TblCell']),
            Paragraph("Multi-socket server CPUs (dual/quad Xeon or EPYC processors)", styles['TblCell']),
            Paragraph("Dozens of specialized processor books with dedicated I/O coprocessors", styles['TblCell'])
        ],
        [
            Paragraph("<b>Memory Subsystem</b>", styles['TblCellBold']),
            Paragraph("8 to 32 GB standard non-ECC DDR4/DDR5 RAM", styles['TblCell']),
            Paragraph("32 to 256 GB Error-Correcting Code (ECC) RAM", styles['TblCell']),
            Paragraph("64 GB to 1 TB+ Registered ECC RAM with multi-channel support", styles['TblCell']),
            Paragraph("Multiple Terabytes of fully redundant, self-healing memory arrays", styles['TblCell'])
        ],
        [
            Paragraph("<b>Graphics Hardware</b>", styles['TblCellBold']),
            Paragraph("Integrated CPU graphics or consumer gaming GPU", styles['TblCell']),
            Paragraph("Dedicated professional GPU (e.g., NVIDIA RTX Workstation) with certified drivers", styles['TblCell']),
            Paragraph("Basic headless onboard video for server console administration", styles['TblCell']),
            Paragraph("Specialized display channels; no consumer 3D gaming hardware", styles['TblCell'])
        ],
        [
            Paragraph("<b>Storage & Fault Tolerance</b>", styles['TblCellBold']),
            Paragraph("Single M.2 NVMe SSD or SATA HDD; no hardware redundancy", styles['TblCell']),
            Paragraph("Dual or quad NVMe SSDs in RAID-0/1; high-capacity scratch disks", styles['TblCell']),
            Paragraph("Hot-swappable SAS/SATA drives in hardware RAID-5/6/10 arrays", styles['TblCell']),
            Paragraph("Massive external fiber-channel storage area networks (SAN) with zero data loss", styles['TblCell'])
        ],
        [
            Paragraph("<b>Cooling & Power</b>", styles['TblCellBold']),
            Paragraph("Single 300–650W power supply; standard air cooling fans", styles['TblCell']),
            Paragraph("High-wattage 850–1200W gold-rated PSU; heavy heatsinks or liquid cooling", styles['TblCell']),
            Paragraph("Dual redundant hot-swappable 800W power supplies; high-CFM server fans", styles['TblCell']),
            Paragraph("Dedicated facility power substations; chilled water liquid heat exchangers", styles['TblCell'])
        ],
        [
            Paragraph("<b>Operational Role at SUA</b>", styles['TblCellBold']),
            Paragraph("Undergraduate BIT 111 labs, student report typing, library catalog searches.", styles['TblCell']),
            Paragraph("3D GIS mapping in Forestry; structural CAD in Agricultural Engineering.", styles['TblCell']),
            Paragraph("Departmental research databases, SUASIS local nodes, campus web servers.", styles['TblCell']),
            Paragraph("National banking networks, national census, central university registrar databases.", styles['TblCell'])
        ]
    ]
    t2_table = Table(t2_data, colWidths=[1.3 * inch, 1.4 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
    t2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SUA_DARKGREEN),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_WHITE, COLOR_BG_LIGHT]),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t2_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Desktop vs. Laptop Internal Architectural Trade-Offs</b>", styles['SecH2']))
    story.append(Paragraph(
        "• <b>Thermal Dissipation and Throttling:</b> Desktop chassis provide generous internal physical volume, allowing massive copper heatsinks and multiple high-flow chassis fans to exhaust hot air. Laptops have ultra-compact enclosures with tiny micro-blowers and heatpipes. Under sustained heavy computational loads (such as rendering GIS maps), laptop processors become thermally constrained and automatically execute <i>thermal throttling</i> (lowering clock frequencies temporarily to prevent physical silicon melting), reducing computational performance.<br/>"
        "• <b>Hardware Upgradeability:</b> Desktop towers allow straightforward component upgrades—users can swap the CPU, add more RAM sticks, install larger storage drives, or upgrade PCIe graphics cards easily. In modern ultrabooks, the CPU, RAM chips, and Wi-Fi modules are often soldered permanently onto the motherboard, rendering post-purchase upgrades impossible.<br/>"
        "• <b>Power Source:</b> Desktops require continuous, uninterrupted AC wall power; a sudden power blackout shuts the system down instantly. Laptops incorporate integrated lithium-ion batteries that act like a built-in Uninterruptible Power Supply (UPS), allowing uninterrupted academic work during campus power cuts.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 12))

    # =========================================================
    # SECTION 9: CROSS-DISCIPLINARY APPLIED CASE STUDIES
    # =========================================================
    story.append(Paragraph("9. CROSS-DISCIPLINARY APPLIED CASE STUDIES AT SOKOINE UNIVERSITY OF AGRICULTURE", styles['SecH1']))
    story.append(Paragraph(
        "To comprehend how microcomputer hardware components interact in real-world professional environments, first-year scholars must examine how specific processors, storage media, and peripheral devices are deployed across diverse departments at Sokoine University of Agriculture:",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 1: Agronomy & Precision Horticulture — High-Throughput Phenotyping Systems</b>", styles['SecH2']))
    story.append(Paragraph(
        "In modern crop breeding trials conducted at the SUA Department of Crop Science and Horticulture, agronomists evaluate hundreds of indigenous drought-resistant bean varieties. Rather than relying solely on manual field measurements, researchers utilize automated digital imaging chambers. High-resolution multi-spectral optical cameras (input devices) capture thousands of raw photographs of bean plant canopies at distinct growth stages. The multi-gigabyte image datasets are transferred across high-speed USB 3.1 ports into a desktop microcomputer equipped with a multi-core processor (8 cores) and 32 GB of high-speed DDR4 RAM.<br/>"
        "Because image processing algorithms (calculating Normalized Difference Vegetation Index - NDVI) are computationally demanding, the multi-core CPU and high-speed RAM allow the software to process multiple image tiles in parallel without running out of memory. The processed vegetation indices and canopy biomass estimates are stored permanently on an ultra-fast M.2 NVMe SSD. Using this hardware setup, agronomists can screen 500 bean varieties in an afternoon—a task that previously took weeks of destructive physical plant harvesting.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 2: Animal Science & Dairy Technology — Automated Concentrate Feeding Dispensers</b>", styles['SecH2']))
    story.append(Paragraph(
        "At the SUA Magadu Dairy Farm, maximizing individual cow milk production while controlling costly feed concentrate expenses requires precision nutritional management. High-producing dairy cows require supplemental grain pellets, whereas low-producing cows become obese and develop reproductive disorders if overfed.<br/>"
        "The dairy unit implemented computerized feeding stations. When a cow approaches the concentrate feeder, a high-frequency RFID antenna (input device) energizes the transponder chip in the cow's ear tag, reading its unique electronic ID. An onboard industrial microcomputer queries the herd database stored in local flash memory (secondary storage). If the cow is entitled to feed, the microcomputer's digital output lines trigger an electronic relay switch, energizing an electric motorized auger (actuator output) that dispenses exactly 500 grams of pelleted concentrate into the feed bowl. The cow's remaining daily allowance is updated in non-volatile memory immediately, preventing dominant cows from overeating.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 3: Veterinary Medicine — Digital Radiography Workstations at the Animal Hospital</b>", styles['SecH2']))
    story.append(Paragraph(
        "The SUA Veterinary Teaching Hospital recently phased out manual chemical film processing in favor of direct digital radiography (DR) for diagnosing orthopedic fractures, gastrointestinal foreign bodies, and pulmonary pathologies in animal patients. In conventional film radiography, developing chemical darkroom tanks caused delays, chemical hazards, and frequent over/under-exposure errors requiring repeated radiation exposure.<br/>"
        "In the digital radiography suite, an X-ray detector panel containing an array of amorphous silicon photodetectors (input device) captures X-ray photons passing through the patient and converts them into high-resolution 16-bit digital DICOM images in under 3 seconds. The raw image is transmitted over a Gigabit Ethernet cable (RJ-45) to a specialized medical imaging workstation. This workstation incorporates a high-end multi-core CPU, 64 GB of ECC RAM, and a specialized medical-grade high-contrast grayscale LED monitor (output device). Veterinary radiologists adjust image brightness, zoom into bone trabeculae, measure cardiac vertebral heart scores digitally, and archive the patient radiograph permanently to a mirrored NAS storage server.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 4: Wildlife Management & Ecotourism — Acoustic Bat and Bird Telemetry Loggers</b>", styles['SecH2']))
    story.append(Paragraph(
        "In the dense miombo woodlands of the Mikumi ecosystem, researchers from the SUA College of Forestry, Wildlife and Tourism monitor nocturnal bat species and elusive forest birds to assess ecological health. Many insectivorous bats navigate and hunt using ultrasonic echolocation calls (ranging from 20 kHz to over 120 kHz) that are completely inaudible to human ears.<br/>"
        "Researchers mount autonomous acoustic recording microcomputers to tree trunks. High-frequency ultrasonic microphones (input devices) capture acoustic pressure waves, which an internal analog-to-digital converter (ADC) samples at 384,000 samples per second. A low-power microprocessor executes digital filters in real time, saving continuous ultrasonic spectrograms to high-endurance SD flash cards (secondary storage). The device operates on four rechargeable lithium-ion cells for 3 weeks continuously. Back at the university, wildlife students load the audio files into sound-analysis software, visually identifying bat species by the unique frequency sweeps of their echolocation pulses.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 5: Agricultural Engineering — Tractor Implement Telemetry and Fuel Optimization</b>", styles['SecH2']))
    story.append(Paragraph(
        "Heavy agricultural mechanization in large-scale cereal farming (such as wheat and maize schemes in Arusha and Kilombero) represents a massive operational expenditure, with tractor diesel fuel comprising over 35% of total tillage costs. Operating heavy disc plows with improper tire pressure or incorrect hitch geometry results in excessive wheel slippage, soil compaction, and severe fuel waste.<br/>"
        "Engineers at the SUA Department of Agricultural Engineering installed an instrumented telemetry microcomputer on a research tractor. Wheel rotation sensors, a radar forward-speed sensor, and an in-line fuel flow transducer (input devices) feed real-time signals across a Controller Area Network (CAN bus) to an onboard ruggedized cabin computer. The computer's multi-core processor compares theoretical wheel speed against actual ground radar speed to calculate instantaneous wheel slip. A high-brightness anti-glare LCD display monitor (output device) provides live visual guidance to the tractor operator: if wheel slip exceeds the optimal 12% range, the screen displays a warning prompt advising the driver to downshift gears and reduce tillage depth, reducing overall fuel consumption by 18%.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 6: Agricultural Extension — Portable Video Projectors for Rural Farmer Field Schools</b>", styles['SecH2']))
    story.append(Paragraph(
        "Agricultural extension officers conducting Farmer Field Schools in off-grid rural villages face immense communication challenges when explaining microscopic agronomic concepts—such as how fungal spores spread on maize cobs or the proper technique for grafting citrus fruit saplings. Traditional black-and-white paper leaflets are easily discarded and ineffective for illiterate or visually impaired farmers.<br/>"
        "Extension officers travel equipped with lightweight laptop microcomputers and battery-powered portable LED pico-projectors (output devices). The laptop stores short, professionally produced instructional video documentaries in Swahili on its fast internal SSD (secondary storage). Extension officers connect the projector to the laptop's HDMI port and project vivid, full-color instructional videos onto a hanging white bedsheet against a village schoolhouse wall. The visual presentation engages farmers dynamically, facilitating immediate group discussions and dramatically accelerating the adoption of sustainable farming techniques.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 7: Aquaculture — Automated Fish Feeding Cannons in Concrete Culture Tanks</b>", styles['SecH2']))
    story.append(Paragraph(
        "In intensive aquaculture raceways at the SUA Fisheries Unit, commercial African sharptooth catfish (<i>Clarias gariepinus</i>) must be fed small quantities of high-protein pelleted feed at frequent, precise intervals throughout the day and night to maximize growth and prevent territorial fighting and cannibalism. Manual hand feeding by farm workers is labor-intensive, irregular, and impossible to maintain reliably during midnight hours.<br/>"
        "The aquaculture station deployed automated feeding cannons mounted above each culture tank. An embedded microcomputer controls the system. At pre-programmed intervals stored in EEPROM firmware, the microcomputer activates an air blower motor and opens a solenoid valve (actuator outputs) for exactly 15 seconds, propelling 250 grams of floating feed pellets across the water surface in a broad, uniform pattern. The microcomputer logs each feeding event to an internal flash memory card, ensuring that nutritional regimens are adhered to precisely.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 8: Forestry & Wood Science — Ultrasonic Timber Flaw Detectors</b>", styles['SecH2']))
    story.append(Paragraph(
        "In the timber processing industry, determining the internal structural soundness and detecting hidden internal rot pockets or cracks inside valuable hardwood logs (e.g., East African Blackwood - <i>Dalbergia melanoxylon</i>) prior to sawmill conversion is essential to prevent costly saw blade damage and maximize merchantable lumber yield.<br/>"
        "Researchers in the SUA Department of Wood Science and Technology employ portable ultrasonic non-destructive testing (NDT) microcomputers. Two piezoelectric acoustic transducers (input/output devices) are clamped to opposite sides of a timber log. The transmitting transducer injects a high-frequency mechanical sound pulse into the wood fibers; the receiving transducer captures the transmitted wave on the other side. The microcomputer's high-speed processor measures the acoustic time-of-flight in microseconds. Because sound travels significantly slower through decayed or hollow wood than through sound, dense timber, the computer calculates stress wave velocity and displays a 2D cross-sectional density map on its color LCD screen, allowing sawmill operators to position saw cuts precisely.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 9: Food Science & Human Nutrition — Texture Analyzers in Post-Harvest Storage Trials</b>", styles['SecH2']))
    story.append(Paragraph(
        "Undergraduate researchers in Food Science investigate the post-harvest storage stability and textural deterioration of new cassava varieties stored in rustic sawdust evaporative cooling chambers. Evaluating cassava root firmness manually by thumb pressure is subjective and scientifically unpublishable.<br/>"
        "The food quality laboratory utilizes an automated electronic Texture Analyzer interfaced with a laboratory desktop microcomputer. A stainless-steel mechanical penetration probe descends into the cassava flesh at a controlled rate of 1 mm per second. A high-precision strain-gauge load cell (input transducer) measures resistive puncture force in Newtons every millisecond. The data stream is transmitted across a USB cable into the microcomputer, where software plots real-time force-distance deformation curves on the monitor (output). The peak rupture force (bio-yield point) is recorded in a spreadsheet on the hard disk, providing empirical, objective proof of post-harvest preservation quality.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Case Study 10: Family & Consumer Studies — Barcode Scanners in Consumer Food Purchasing Audits</b>", styles['SecH2']))
    story.append(Paragraph(
        "In consumer economics research conducted by the Department of Family and Consumer Studies, students evaluate urban household food consumption, packaged food labeling compliance, and ultra-processed food purchasing trends across supermarkets in Morogoro and Dar es Salaam.<br/>"
        "Students conduct audits equipped with handheld laser barcode scanners (input devices) connected to portable laptops. When a student scans the standardized 13-digit EAN-13 barcode on a package of fortified maize flour or imported cooking oil, the scanner decodes the black-and-white optical bars into a binary number string, entering it directly into an active inventory database. The laptop matches the barcode against an electronic product catalog, automatically retrieving manufacturer details, nutritional labeling claims, and retail pricing. This eliminates hours of manual typing and prevents recording errors, enabling rigorous consumer expenditure analysis.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 12))

    # =========================================================
    # SECTION 10: PRACTICAL LABORATORY GUIDE: INSIDE THE SYSTEM UNIT
    # =========================================================
    story.append(Paragraph("10. PRACTICAL LABORATORY GUIDE: EXPLORING THE SYSTEM UNIT", styles['SecH1']))
    story.append(Paragraph(
        "In your second practical laboratory session in the DIIT computer laboratories, you will conduct a structured, hands-on physical exploration of the microcomputer system unit. Developing confidence in identifying internal hardware components, understanding safety precautions, and performing basic maintenance are vital practical skills for all university students.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Laboratory Safety Protocols and Anti-Static Protection</b>", styles['SecH2']))
    story.append(Paragraph(
        "Before opening any physical computer chassis, you must observe these strict safety protocols:<br/>"
        "• <b>Electrical Isolation:</b> Always perform a complete graceful software shutdown, turn off the physical rocker switch on the Power Supply Unit (PSU), and disconnect the AC mains power cord from the wall outlet. Press and hold the chassis power button for 5 seconds while unplugged to discharge residual electrical energy stored in high-voltage capacitors.<br/>"
        "• <b>Electrostatic Discharge (ESD) Hazards:</b> The human body naturally accumulates static electricity through friction (walking across synthetic carpets, wearing woolen clothing). A static shock of merely 100 volts—completely imperceptible to human touch—is sufficient to melt microscopic conductive pathways inside a CPU or puncture fragile oxide layers in RAM chips.<br/>"
        "• <b>ESD Mitigation:</b> Always wear an <b>anti-static wrist strap</b> clipped to an unpainted metal section of the computer chassis, or frequently touch the bare metal chassis frame with your bare hands before touching sensitive internal printed circuit boards. Always handle RAM sticks and expansion cards by their non-conductive fiberglass edges—never touch gold contact pins or exposed silicon chips.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Visual Identification Walkthrough Inside the Chassis</b>", styles['SecH2']))
    story.append(Paragraph(
        "Once the side panel of the desktop tower is removed, locate each of the following components:<br/>"
        "1. <b>The Power Supply Unit (PSU):</b> The large metal box located at the top or bottom rear of the case, bearing an electrical safety label specifying input AC voltage (230V) and total wattage output (e.g., 450W). Observe the multicolored bundled wiring harness (24-pin ATX, 8-pin CPU, SATA power cables).<br/>"
        "2. <b>The CPU Cooler & Socket:</b> The large aluminum finned heatsink and electric cooling fan mounted near the center of the motherboard. Beneath this cooler sits the microprocessor, clamped inside its metal socket with a microscopic layer of thermal paste bridging the surfaces.<br/>"
        "3. <b>The RAM Slots (DIMMs):</b> Long vertical slots situated adjacent to the CPU socket. Observe the small plastic retention latches on both ends. Notice how a DDR4 memory stick has a single off-center physical notch (key) on its gold edge connector that prevents it from being inserted backward.<br/>"
        "4. <b>PCI Express Expansion Slots:</b> Horizontal expansion slots on the lower half of the motherboard. Identify the long PCIe x16 slot (housing the graphics card) and the shorter PCIe x1 slots.<br/>"
        "5. <b>Storage Drives and M.2 Slots:</b> Identify the mechanical 3.5-inch hard drive mounted in the forward drive cage connected via thin SATA data cables, or locate the ultra-compact M.2 NVMe SSD stick screwed directly flat onto the motherboard surface.<br/>"
        "6. <b>The CMOS Battery:</b> The shiny, coin-shaped CR2032 3V lithium battery that powers the motherboard's Real-Time Clock.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Step-by-Step Procedure: Installing a RAM Module</b>", styles['SecH2']))
    story.append(Paragraph(
        "1. Power off the system completely and disconnect the AC power cord.<br/>"
        "2. Put on an anti-static wrist strap clipped to the metal chassis frame.<br/>"
        "3. Locate an empty DIMM memory slot on the motherboard.<br/>"
        "4. Push down gently on the plastic locking clips at both ends of the memory slot until they click outward into the open position.<br/>"
        "5. Take the new RAM stick, holding it strictly by its top fiberglass corners. Inspect the gold contact edge and align the physical notch on the RAM stick with the matching plastic key inside the memory slot.<br/>"
        "6. Insert the RAM stick vertically into the slot. Apply firm, even downward pressure simultaneously with both thumbs on the top two corners of the module.<br/>"
        "7. As the module seats fully into the socket, the plastic retention clips will automatically swing inward and snap shut with an audible click. Verify that both clips are completely locked into the notches of the memory stick.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 12))

    # =========================================================
    # SECTION 11: TOPIC 2 COMPREHENSIVE ACADEMIC GLOSSARY
    # =========================================================
    story.append(Paragraph("11. TOPIC 2 COMPREHENSIVE ACADEMIC GLOSSARY", styles['SecH1']))
    story.append(Paragraph(
        "This glossary provides formal definitions for fifty foundational hardware terms introduced in Topic 2:",
        styles['DocBody']
    ))
    story.append(Spacer(1, 4))

    glossary_terms_t2 = [
        ("Actuator", "A mechanical or electronic device (such as an electric motor, pneumatic valve, or relay) that converts digital computer output signals into physical mechanical movement or control."),
        ("Amorphous Silicon", "A non-crystalline semiconductor material utilized in flat-panel digital radiography X-ray detectors that converts X-ray photons into electronic digital imagery."),
        ("Anti-Static Wrist Strap", "A safety grounding device worn on the human wrist that safely bleeds off static electricity to the chassis, preventing electrostatic discharge (ESD) damage to sensitive computer chips."),
        ("Aspect Ratio", "The proportional mathematical relationship between the horizontal width and vertical height of a visual display monitor (e.g., standard widescreen displays have an aspect ratio of 16:9)."),
        ("ATX (Advanced Technology Extended)", "A standardized specification governing the physical dimensions, mounting hole locations, power connectors, and layout of desktop computer motherboards and power supplies."),
        ("Barcode Reader", "An optical input scanner that utilizes a laser beam or light sensor to decode 1D parallel lines or 2D QR codes into digital alphanumeric character strings."),
        ("Biometrics", "The measurement and statistical analysis of unique physiological human characteristics (fingerprints, facial geometry, iris patterns) used for identity authentication."),
        ("Blu-ray Disc", "A high-capacity optical disc storage format that utilizes a short-wavelength blue-violet laser (405 nm) to read and write microscopic pits, storing up to 25 to 50 GB per disc."),
        ("Cache Memory", "A small, ultra-fast tier of static RAM (SRAM) integrated directly onto the CPU die (L1, L2, L3) that stores frequently accessed instructions and data to minimize latency."),
        ("Chipset", "The integrated circuit architecture on the motherboard that coordinates data communication between the CPU, memory, PCIe expansion slots, and peripheral storage controllers."),
        ("Clock Frequency", "The speed at which a computer's system clock generates synchronization pulses, measured in Gigahertz (GHz), where one GHz equals one billion electrical ticks per second."),
        ("CMOS RAM", "A tiny bank of battery-backed volatile memory on the motherboard that stores user-configured firmware parameters, boot device priorities, and system passwords."),
        ("CR2032 Battery", "A 3-volt coin-cell lithium battery mounted on the motherboard that provides continuous trickle power to the CMOS RAM and Real-Time Clock when AC power is unplugged."),
        ("Cylinder", "A logical structural unit in a hard disk drive consisting of the collection of all circular tracks located at the exact same radial position across all spinning platter surfaces."),
        ("DDR SDRAM", "Double Data Rate Synchronous Dynamic RAM; memory technology that transfers data on both the rising and falling edges of each clock pulse, doubling data throughput."),
        ("DIMM", "Dual In-Line Memory Module; a standardized rectangular printed circuit board containing DRAM chips with independent electrical contacts on both sides, inserted into motherboard memory slots."),
        ("DisplayPort (DP)", "A high-bandwidth digital display interface capable of carrying multi-stream digital video and audio from microcomputer graphics cards to professional monitors."),
        ("Dot-Matrix Printer", "An impact printer that creates characters and graphics by physically striking an inked fabric ribbon against paper using a matrix of tiny metal pins."),
        ("DRAM (Dynamic RAM)", "Memory technology where each memory bit is stored as a capacitive electrical charge; requires continuous periodic refresh pulses to prevent data loss."),
        ("ECC RAM", "Error-Correcting Code RAM; specialized memory incorporating internal parity circuitry that automatically detects and corrects single-bit memory errors in workstations and servers."),
        ("EEPROM", "Electrically Erasable Programmable Read-Only Memory; non-volatile memory that can be erased and reprogrammed electronically via software, utilized for motherboard firmware chips."),
        ("Electrostatic Discharge (ESD)", "The sudden, momentary flow of electrical current between two objects caused by contact or static friction, capable of permanently destroying microscopic microchip circuitry."),
        ("Expansion Slot", "A physical socket on the motherboard (primarily PCIe) engineered to receive add-in expansion cards (such as graphics, sound, or network cards) to expand system capabilities."),
        ("Flash Memory", "A non-volatile solid-state storage medium based on EEPROM technology that can be erased and reprogrammed in multi-megabyte blocks, used in SSDs and USB flash drives."),
        ("Gigahertz (GHz)", "A physical unit of alternating frequency equal to one billion cycles per second; used to denote the operational clock speed of computer microprocessors."),
        ("Hard Disk Drive (HDD)", "An electro-mechanical secondary storage device that records digital data magnetically on high-speed rotating metallic platters using movable electromagnetic read/write heads."),
        ("HDMI", "High-Definition Multimedia Interface; a widely adopted audio-video standard that transmits uncompressed digital high-definition video and multi-channel audio across a single cable."),
        ("Heatsink", "A passive aluminum or copper thermal dissipation block featuring dense arrays of cooling fins, mounted atop hot computer chips to absorb and radiate heat into the air."),
        ("Inkjet Printer", "A non-impact printer that creates text and images by precisely propelling microscopic droplets of liquid ink from tiny nozzle apertures onto paper fibers."),
        ("Laser Printer", "A high-speed non-impact printer that utilizes an electrostatic xerographic drum, laser beam, and heated fuser rollers to permanently melt powdered plastic toner onto paper."),
        ("Liquid Crystal Display (LCD)", "A flat-panel display technology that controls the passage of light through liquid crystal molecules positioned between polarizing filters and an LED backlight."),
        ("M.2 Slot", "An ultra-compact, high-speed motherboard connector specification that accepts thin solid-state storage sticks and wireless modules mounted flat against the board surface."),
        ("Mechanical Keyboard", "A keyboard constructed with individual physical mechanical spring-loaded switches beneath every keycap, providing tactile feedback and superior typing longevity."),
        ("Membrane Keyboard", "A keyboard constructed from flexible plastic sheets with conductive circuit traces separated by a rubber dome layer; quiet and low-cost but offers mushy tactile feedback."),
        ("Motherboard", "The primary printed circuit board of a microcomputer that structurally houses and electrically interconnects the CPU, RAM, storage, expansion cards, and external ports."),
        ("Multi-Core Processor", "A single semiconductor microprocessor package that integrates two or more complete, independent physical CPU execution cores onto a single silicon chip."),
        ("NAND Flash", "The specific solid-state non-volatile memory cell architecture utilized in SSDs and USB drives that retains stored electrical charges inside floating-gate or charge-trap transistors."),
        ("NVMe", "Non-Volatile Memory Express; an optimized high-speed communications protocol engineered specifically for solid-state storage communicating directly over PCI Express lanes."),
        ("OLED Display", "Organic Light-Emitting Diode; a display technology where each individual pixel emits its own light, delivering true infinite contrast ratios and wide viewing angles."),
        ("Optical Mouse", "A pointing device that uses an internal LED or laser diode and an optical digital signal processor to track movement by photographing micro-textures on a desk surface."),
        ("PCIe", "Peripheral Component Interconnect Express; a high-speed serial expansion bus standard utilizing point-to-point differential signaling lanes (x1, x4, x16) on the motherboard."),
        ("Pixel", "Picture element; the smallest individual controllable point of color in a raster display monitor or digital photograph, arranged in a two-dimensional rectangular grid."),
        ("QWERTY", "The standard international alphanumeric keyboard layout, named for the first six alphabetic characters appearing on the top letter row, originally designed in 1873."),
        ("RAM", "Random Access Memory; the fast, volatile primary electronic workspace of a computer directly accessible by the CPU to hold the operating system, running applications, and data."),
        ("Real-Time Clock (RTC)", "An electronic battery-backed clock integrated into the motherboard chipset that continuously maintains accurate calendar date and wall-clock time."),
        ("Refresh Rate", "The frequency, measured in Hertz (Hz), with which a visual display screen completely redraws its visual image per second (typically 60 Hz to 144 Hz)."),
        ("RFID", "Radio-Frequency Identification; wireless technology utilizing electromagnetic radio waves to query and retrieve unique digital identifiers from transponders embedded in livestock tags or cards."),
        ("ROM", "Read-Only Memory; non-volatile semiconductor memory whose contents are permanently retained during power-off, utilized to store foundational startup firmware."),
        ("Solid-State Drive (SSD)", "A high-speed secondary data storage device constructed entirely from solid-state NAND flash memory chips and a controller, possessing zero moving mechanical components."),
        ("Thermal Throttling", "A hardware protective mechanism where a microprocessor automatically reduces its operational clock frequency to decrease electrical power draw and prevent overheating.")
    ]

    for term, definition in glossary_terms_t2:
        story.append(Paragraph(f"• <b>{term}:</b> {definition}", styles['DocBullet']))

    story.append(Spacer(1, 12))

    # =========================================================
    # SECTION 12: AUTHENTIC ACADEMIC LITERATURE & REFERENCES
    # =========================================================
    story.append(Paragraph("12. RECOMMENDED READINGS AND AUTHENTIC REFERENCES", styles['SecH1']))
    story.append(Paragraph(
        "The following genuine introductory references provide additional reading on computer systems and hardware:",
        styles['DocBody']
    ))
    story.append(Spacer(1, 4))

    references_t2 = [
        ("Smith, J. L., Wang, S., &amp; Mortati, J. (2019).", "<i>Information Systems for Business and Beyond</i>. Open textbook. <a href='https://opentextbook.site/informationsystems2019/chapter/chapter-2-hardware-information-systems-introduction/'>Chapter 2: Hardware</a>."),
        ("Vermaat, M. E., Sebok, S. L., Freund, S. M., Campbell, J. T., &amp; Frydenberg, M. (2018).", "<i>Discovering Computers: Digital Technology, Data, and Devices</i> (16th ed.). Cengage Learning. <a href='https://faculty.cengage.com/works/9781337285100'>Publisher catalog</a>."),
    ]

    for author, citation in references_t2:
        story.append(Paragraph(f"• <b>{author}</b> {citation}", styles['DocBullet']))

    story.append(Spacer(1, 14))

    # =========================================================
    # SECTION 13: TOPIC 2 SELF-ASSESSMENT QUESTIONS
    # =========================================================
    story.append(Paragraph("13. TOPIC 2 SELF-ASSESSMENT QUESTIONS", styles['SecH1']))
    story.append(Paragraph(
        "This self-assessment bank presents <b>forty comprehensive, rigorously developed questions</b> covering all conceptual dimensions of Topic 2. First-year scholars should attempt every question independently before consulting the model solutions in Section 14.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    # Part A: MCQs
    story.append(Paragraph("<b>Part A: Multiple Choice Questions (Questions 1 to 15)</b>", styles['SecH2']))
    story.append(Spacer(1, 4))

    mcqs_t2 = [
        ("1. What physical electronic component is mounted directly into the motherboard CPU socket?",
         ["A. The primary mechanical hard disk drive",
          "B. The microprocessor silicon chip (Central Processing Unit)",
          "C. The coin-shaped CR2032 lithium CMOS battery",
          "D. The PCIe optical disc reader"]),
        ("2. Which CPU subcomponent is specifically responsible for executing arithmetic operations (addition, subtraction) and logical evaluations (comparisons)?",
         ["A. Control Unit (CU)",
          "B. Arithmetic Logic Unit (ALU)",
          "C. Program Counter (PC)",
          "D. Platform Controller Hub (PCH)"]),
        ("3. Why did microprocessor manufacturers shift from increasing clock frequencies (above 3.8 GHz) to building multi-core processors in the mid-2000s?",
         ["A. Because software developers refused to write programs in English.",
          "B. Extreme thermal heat generation and electrical power leakage made cooling single cores at higher frequencies physically unsustainable.",
          "C. Because international copyright laws banned clock speeds exceeding 4.0 GHz.",
          "D. Because computer monitors could not display text faster than 3 GHz."]),
        ("4. Which tier of on-chip cache memory is built directly inside each individual CPU core and operates at the full physical clock speed of the processor?",
         ["A. Level 3 (L3) Cache",
          "B. Level 1 (L1) Cache",
          "C. CMOS RAM",
          "D. Virtual Paging File"]),
        ("5. What is the fundamental technological distinction between DRAM (Dynamic RAM) and SRAM (Static RAM)?",
         ["A. DRAM is non-volatile, whereas SRAM loses data when power is turned off.",
          "B. DRAM stores bits as capacitive charges requiring continuous refresh cycles, whereas SRAM uses transistor flip-flops and requires no refreshing.",
          "C. DRAM is integrated directly inside the CPU registers, whereas SRAM is mounted on external SATA cables.",
          "D. DRAM can only store text, whereas SRAM can only store graphics."]),
        ("6. What is the primary function of the coin-shaped CR2032 3V lithium battery found on a microcomputer motherboard?",
         ["A. To power the cooling fan during severe processor overheating.",
          "B. To maintain electrical trickle power to the CMOS RAM and Real-Time Clock (RTC) when the system is unplugged.",
          "C. To charge the laptop's main secondary storage SSD.",
          "D. To provide backup power to the display monitor during blackouts."]),
        ("7. Why are Solid-State Drives (SSDs) inherently more physically durable than traditional Hard Disk Drives (HDDs)?",
         ["A. SSDs are manufactured from tempered plate glass.",
          "B. SSDs construct data storage purely from solid-state NAND flash silicon chips with zero moving mechanical parts.",
          "C. SSDs are shielded with heavy electromagnetic lead casings.",
          "D. SSDs rotate at 15,000 RPM inside a vacuum chamber."]),
        ("8. Which secondary storage interface communicates directly over high-speed PCI Express lanes, delivering throughput speeds significantly faster than legacy SATA cables?",
         ["A. Optical Blu-ray IDE",
          "B. Non-Volatile Memory Express (NVMe) M.2",
          "C. Floppy Disk Interface",
          "D. RS-232 Serial Port"]),
        ("9. In hard disk drive geometry, what term describes the circular ring tracks located at the exact same radial position across all spinning platter surfaces?",
         ["A. Cluster",
          "B. Sector",
          "C. Cylinder",
          "D. Platter Spindle"]),
        ("10. Which input peripheral is specifically designed to decode optical patterns of parallel lines or 2D matrices into digital strings for warehouse and seed inventory tracking?",
         ["A. Capacitive Trackpad",
          "B. Barcode and QR Code Reader",
          "C. Piezoelectric Ultrasound Probe",
          "D. Cathode-Ray Tube Scanner"]),
        ("11. An agricultural produce buying dock in Kilombero requires an output printer capable of striking through multi-part carbon-copy receipts for truck drivers. Which printer technology is strictly required?",
         ["A. Thermal Dye-Sublimation Printer",
          "B. Non-Impact Color Inkjet Printer",
          "C. Impact Dot-Matrix Printer",
          "D. Electrostatic Laser Printer"]),
        ("12. What electrostatic printing technology utilizes a rotating photosensitive drum, a laser beam, and heated fuser rollers to melt powdered plastic toner onto paper?",
         ["A. Wide-Format Pen Plotter",
          "B. Laser Printer",
          "C. Piezoelectric Inkjet Printer",
          "D. Continuous-Tone Impact Printer"]),
        ("13. Why are technical workstations in the SUA Department of Forestry equipped with Error-Correcting Code (ECC) RAM rather than standard consumer desktop RAM?",
         ["A. ECC RAM doubles the frame rate of 3D computer video games.",
          "B. ECC RAM incorporates parity circuitry that detects and corrects single-bit memory corruptions in real time during long-running scientific simulations.",
          "C. ECC RAM eliminates the need for an operating system.",
          "D. ECC RAM can function with zero electrical power."]),
        ("14. What occurs when a laptop microcomputer is subjected to sustained heavy computational processing in a hot tropical environment without adequate ventilation?",
         ["A. The CPU permanently reverses the polarity of its data bus.",
          "B. Thermal throttling engages, causing the processor to automatically lower its clock frequency to prevent physical overheating.",
          "C. The secondary storage SSD automatically reformats its partitions.",
          "D. The liquid crystal display permanently freezes its pixels."]),
        ("15. What safety hazard is eliminated by wearing an anti-static wrist strap clipped to the metal chassis when servicing internal computer hardware?",
         ["A. High-voltage 230V AC electrocution from the wall outlet.",
          "B. Electrostatic Discharge (ESD) from human fingertips that can destroy microscopic silicon circuitry.",
          "C. Overheating of the power supply unit fan.",
          "D. Accidental deletion of files from the cloud."])
    ]

    for q_text, opts in mcqs_t2:
        story.append(Paragraph(f"<b>{q_text}</b>", styles['DocBodyBold']))
        for opt in opts:
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;{opt}", styles['DocBody']))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 8))

    # Part B: Conceptual Short Answer
    story.append(Paragraph("<b>Part B: Conceptual Short-Answer Questions (Questions 16 to 25)</b>", styles['SecH2']))
    story.append(Spacer(1, 4))

    saqs_t2 = [
        "16. Explain the conceptual function of the motherboard chipset, distinguishing between components that connect directly to the CPU versus those managed through the Platform Controller Hub (PCH).",
        "17. Define the concept of the microcomputer 'system clock' and explain why comparing processor performance strictly by Gigahertz (GHz) across different CPU architectures can be misleading.",
        "18. Describe the hierarchy of CPU cache memory (L1, L2, L3) and explain what occurs during a 'cache hit' versus a 'cache miss'.",
        "19. Contrast the operational characteristics of volatile Dynamic RAM (DRAM) with non-volatile Flash Memory used in Solid-State Drives.",
        "20. Explain what 'wear leveling' is in modern SSD architecture and why it is essential for the long-term reliability of solid-state storage.",
        "21. Describe the mechanical read/write process in a Hard Disk Drive (HDD) and explain the physical cause and catastrophic consequence of a 'head crash'.",
        "22. Distinguish between an Impact Printer (dot-matrix) and a Non-Impact Printer (laser) in terms of image formation, printing noise, operational cost, and specific institutional use cases at SUA.",
        "23. What is the fundamental difference between legacy BIOS and modern UEFI firmware? List three distinct operational advantages provided by UEFI.",
        "24. Explain why Electrostatic Discharge (ESD) represents such a severe threat to computer microchips during laboratory servicing, and outline two standard precautions to prevent ESD damage.",
        "25. Describe how an optical mouse detects physical movement across a desk surface and explain how optical scanning differs fundamentally from mechanical ball mice."
    ]

    for q in saqs_t2:
        story.append(Paragraph(f"<b>{q}</b>", styles['DocBullet']))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 8))

    # Part C: Comparative Discussion
    story.append(Paragraph("<b>Part C: Comparative Analysis and Discussion Questions (Questions 26 to 35)</b>", styles['SecH2']))
    story.append(Spacer(1, 4))

    cdqs_t2 = [
        "26. Construct a comprehensive comparative analysis between a Hard Disk Drive (HDD) and a Solid-State Drive (SSD) across the parameters of physical data storage mechanism, access latency, operational noise, power consumption, mechanical shock resistance, and longevity.",
        "27. Compare and contrast standard consumer desktop microcomputers with specialized Technical Workstations. In your discussion, address the processor architecture, memory specifications (ECC), graphics acceleration, storage redundancy, and concrete scientific use cases at Sokoine University of Agriculture.",
        "28. Examine the physical and architectural differences between desktop tower motherboards (ATX/mATX) and mobile laptop motherboards. How do physical space constraints impact cooling, upgradeability, component soldering, and thermal throttling?",
        "29. Discuss the historical progression of Double Data Rate (DDR) memory from original DDR through DDR5. What architectural changes permitted bandwidth expansion while simultaneously reducing electrical operating voltages?",
        "30. Contrast the visual display technologies of LED-backlit LCD monitors and Organic Light-Emitting Diode (OLED) displays. Discuss their differences in backlighting, contrast ratios, black levels, power consumption, and suitability for reviewing GIS satellite maps versus general text processing.",
        "31. Compare the communication standards of USB Type-A, USB Type-C, and HDMI. Why is USB Type-C considered a revolutionary convergence connector in modern personal computing?",
        "32. Detail how sensory input transducers and electronic output actuators interact within an automated microcomputer feedback loop in an agricultural greenhouse at the SUA Department of Horticulture.",
        "33. Discuss the comparative advantages and operational trade-offs of Inkjet Printers versus Laser Printers in a university department managing student exam printing, research color photographs, and daily administrative memos.",
        "34. Explain the physical construction and data encoding principles of optical storage media (CD, DVD, Blu-ray), highlighting the role of laser wavelengths, microscopic pits, and reflective lands.",
        "35. Critically assess the role of Radio-Frequency Identification (RFID) technology versus optical Barcode scanning in modern livestock herd management and agricultural supply chain traceability in Tanzania."
    ]

    for q in cdqs_t2:
        story.append(Paragraph(f"<b>{q}</b>", styles['DocBullet']))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 8))

    # Part D: Applied Case Studies
    story.append(Paragraph("<b>Part D: Cross-Disciplinary Applied Case Studies (Questions 36 to 40)</b>", styles['SecH2']))
    story.append(Spacer(1, 4))

    cases_t2 = [
        "36. <b>Forestry & GIS Workstation Hardware Specification:</b> The SUA College of Forestry, Wildlife and Tourism requires a technical workstation to process multi-spectral drone photography and 3D GIS satellite maps of the Uluguru Nature Reserve. Formulate an optimal hardware component specification: select the CPU class and core count, RAM type and capacity, primary and secondary storage configuration, graphics accelerator, and display monitor, justifying each component choice conceptually.",
        "37. <b>Dairy Parlor Automation Hardware Failure Diagnosis:</b> At the SUA Magadu Dairy Farm, the automated concentrate feeding station suddenly stops dispensing grain to cows when they enter the milking stall. As the student hardware technician, develop a systematic physical troubleshooting procedure to isolate whether the failure is in the input transducer (RFID reader), processing controller, or output actuator (relay/motor).",
        "38. <b>Veterinary Clinic Mobile Hardware Selection:</b> Clinicians at the SUA Veterinary Teaching Hospital need new mobile computing devices to record patient diagnostics in the animal wards and during rural ambulatory field visits. Evaluate the trade-offs between standard consumer laptops, 2-in-1 touchscreen convertibles, and military-grade ruggedized tablets, recommending the optimal form factor for veterinary clinical environments.",
        "39. <b>University Laboratory Printer Deployment Strategy:</b> The Department of Informatics and Information Technology (DIIT) must deploy printing solutions across three distinct environments: (a) high-volume student term paper printing in the computer lab (10,000 pages/month), (b) high-resolution color botanical photograph printing for researchers, and (c) warehouse carbon-copy receipt dispatch. Recommend the precise printer technology for each environment and justify your selections.",
        "40. <b>Computer Lab Memory Upgrade Proposal:</b> The DIIT undergraduate computer laboratory currently operates 60 desktop towers equipped with 4 GB of DDR4 RAM and mechanical hard disk drives (HDDs), resulting in sluggish performance when first-year students launch multiple applications simultaneously. Propose a cost-effective hardware upgrade plan (RAM capacity and SSD replacement) and explain the conceptual performance improvements students will experience."
    ]

    for c in cases_t2:
        story.append(Paragraph(c, styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 14))

    # =========================================================
    # SECTION 14: SOLUTIONS AND MODEL ANSWERS
    # =========================================================
    story.append(Paragraph("14. COMPREHENSIVE SOLUTIONS AND MODEL ANSWERS", styles['SecH1']))
    story.append(Paragraph(
        "This section provides fully developed, academically rigorous model solutions and conceptual rationales for all forty self-assessment questions in Topic 2:",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    # Solutions to Part A: MCQs
    story.append(Paragraph("<b>Solutions to Part A: Multiple Choice Questions (1 to 15)</b>", styles['SecH2']))
    story.append(Spacer(1, 4))

    mcq_solutions_t2 = [
        ("Question 1: Component Mounted in CPU Socket",
         "Correct Answer: B. The microprocessor silicon chip (Central Processing Unit).",
         "Conceptual Rationale: The CPU socket is the central physical zero-insertion-force (ZIF) or land grid array (LGA) receptacle on the motherboard designed specifically to seat and lock the microprocessor chip, providing hundreds of gold pin contacts for power and data buses. Hard drives (A) mount in chassis drive bays; the CR2032 battery (C) mounts in a coin socket; optical drives (D) connect via SATA or external ports."),

        ("Question 2: CPU Subcomponent Executing Math and Logic",
         "Correct Answer: B. Arithmetic Logic Unit (ALU).",
         "Conceptual Rationale: The Arithmetic Logic Unit is the dedicated digital electronic circuit within the processor that executes all fundamental arithmetic calculations (addition, subtraction, multiplication, division) and logical comparisons (equal-to, greater-than, Boolean logic). The Control Unit (A) directs instruction flow; the Program Counter (C) holds memory addresses; the PCH (D) coordinates peripheral motherboard buses."),

        ("Question 3: Why Manufacturers Shifted to Multi-Core Processors",
         "Correct Answer: B. Extreme thermal heat generation and electrical power leakage made cooling single cores at higher frequencies physically unsustainable.",
         "Conceptual Rationale: When clock frequencies approached 4.0 GHz in the mid-2000s, processors encountered the physical 'Power Wall': electrical current leakage increased dramatically and thermal heat output escalated exponentially, exceeding the cooling capacity of standard heatsinks. Engineers pivoted to multi-core architectures, placing multiple independent execution cores on the same chip running at moderate, energy-efficient clock frequencies to expand total throughput in parallel. Options A, C, and D are fabricated distractions."),

        ("Question 4: Fastest On-Chip Cache Tier Built Into Each Core",
         "Correct Answer: B. Level 1 (L1) Cache.",
         "Conceptual Rationale: Level 1 cache is the smallest, fastest memory tier, integrated directly inside each individual CPU core silicon. It operates at the full physical clock frequency of the core with zero wait states. L3 cache (A) is a larger, shared pool positioned further from the core execution circuits. CMOS RAM (C) is a slow battery-backed memory on the motherboard. Virtual paging files (D) reside on slow secondary storage."),

        ("Question 5: Fundamental Distinction Between DRAM and SRAM",
         "Correct Answer: B. DRAM stores bits as capacitive charges requiring continuous refresh cycles, whereas SRAM uses transistor flip-flops and requires no refreshing.",
         "Conceptual Rationale: Dynamic RAM (DRAM) memory cells consist of one transistor and one microscopic capacitor; because capacitors leak charge within milliseconds, DRAM must be refreshed with electrical pulses hundreds of times per second. Static RAM (SRAM) uses multi-transistor flip-flop circuits that retain state without refreshing. SRAM is vastly faster but larger and more expensive, used for on-chip CPU caches, while DRAM forms main system memory. Option A is incorrect because both DRAM and SRAM are volatile."),

        ("Question 6: Function of the Motherboard CR2032 Lithium Battery",
         "Correct Answer: B. To maintain electrical trickle power to the CMOS RAM and Real-Time Clock (RTC) when the system is unplugged.",
         "Conceptual Rationale: When a computer is unplugged from AC wall power, the 3V lithium CR2032 coin battery supplies continuous low-wattage current to preserve user-configured firmware parameters in CMOS RAM and keep the quartz-crystal Real-Time Clock (RTC) ticking accurately. Options A, C, and D are physically impossible given the tiny milliampere-hour capacity of a coin-cell battery."),

        ("Question 7: Why Solid-State Drives Are Physically More Durable Than HDDs",
         "Correct Answer: B. SSDs construct data storage purely from solid-state NAND flash silicon chips with zero moving mechanical parts.",
         "Conceptual Rationale: Hard Disk Drives rely on spinning magnetic platters (5,400 to 7,200 RPM) and delicate actuator arms floating nanometers above the surface, making them highly vulnerable to mechanical drops. SSDs have zero moving physical parts, storing data electronically in solid-state NAND flash silicon chips, rendering them completely immune to physical shocks, drops, and rotational vibrations. Options A, C, and D describe fictitious engineering attributes."),

        ("Question 8: Interface Communicating Directly Over PCIe Lanes",
         "Correct Answer: B. Non-Volatile Memory Express (NVMe) M.2.",
         "Conceptual Rationale: NVMe is an optimized storage communications protocol designed specifically for flash memory, connecting directly over high-speed PCI Express (PCIe) lanes. This bypasses legacy SATA controller bottlenecks, delivering bandwidth speeds of 3,500 to 7,000 MB/s compared to SATA's 550 MB/s ceiling. Options A, C, and D are older, slow legacy interfaces."),

        ("Question 9: Concentric Circular Tracks Across All Platter Surfaces",
         "Correct Answer: C. Cylinder.",
         "Conceptual Rationale: In hard disk drive geometry, a cylinder is the logical vertical collection of all concentric circular tracks located at the exact same radial distance from the spindle across all spinning platter surfaces. A sector (B) is a smaller arc subdivision of a single track; a cluster (A) is a logical operating system allocation unit grouping multiple sectors."),

        ("Question 10: Input Peripheral for 1D Bars and 2D QR Codes",
         "Correct Answer: B. Barcode and QR Code Reader.",
         "Conceptual Rationale: Barcode and QR code readers are optical input devices that illuminate and capture light reflections from dark bars and white spaces, translating optical patterns into digital binary text strings for automated inventory tracking. Options A, C, and D serve entirely different human-pointing or scientific sensing functions."),

        ("Question 11: Printer Required for Multi-Part Carbon-Copy Receipts",
         "Correct Answer: C. Impact Dot-Matrix Printer.",
         "Conceptual Rationale: Multi-part carbon-copy forms require physical mechanical impact to press through carbon paper layers to duplicate text on underlying sheets. Only impact dot-matrix printers physically strike pins against an inked ribbon with sufficient mechanical force. Non-impact printers (inkjet, laser, dye-sublimation) deposit ink or toner onto the surface without striking, making them physically incapable of producing carbon copies."),

        ("Question 12: Electrostatic Printing Process with Drum, Laser, and Fuser",
         "Correct Answer: B. Laser Printer.",
         "Conceptual Rationale: Laser printers operate on the electrophotographic (xerographic) principle: a laser beam draws an electrostatic charge pattern on a rotating photosensitive drum; charged plastic toner powder adheres to the drum; toner transfers to paper, and heated fuser rollers melt and press the plastic toner permanently into the paper fibers. Options A, C, and D utilize entirely different liquid ink, pen, or impact mechanisms."),

        ("Question 13: Purpose of ECC RAM in Technical Workstations",
         "Correct Answer: B. ECC RAM incorporates parity circuitry that detects and corrects single-bit memory corruptions in real time during long-running scientific simulations.",
         "Conceptual Rationale: Workstations running multi-day GIS terrain modeling or statistical analyses cannot tolerate system crashes caused by random single-bit memory flips (caused by cosmic rays or electrical noise). Error-Correcting Code (ECC) RAM contains dedicated extra parity bits and internal logic that automatically detects and corrects single-bit errors on the fly without interrupting calculations. Options A, C, and D are false claims."),

        ("Question 14: Consequence of Sustained Heavy Load in Hot Environments",
         "Correct Answer: B. Thermal throttling engages, causing the processor to automatically lower its clock frequency to prevent physical overheating.",
         "Conceptual Rationale: When CPU temperatures exceed safety thresholds (typically 90–100 °C) due to ambient tropical heat and compact laptop cooling limitations, internal thermal sensors trigger 'thermal throttling'. The CPU automatically reduces its operational clock frequency and voltage to decrease heat generation, temporarily sacrificing processing speed to prevent permanent silicon damage. Options A, C, and D describe impossible physical reactions."),

        ("Question 15: Safety Hazard Eliminated by Anti-Static Wrist Strap",
         "Correct Answer: B. Electrostatic Discharge (ESD) from human fingertips that can destroy microscopic silicon circuitry.",
         "Conceptual Rationale: The human body accumulates static electricity that can discharge in microscopic sparks of hundreds or thousands of volts. While harmless to humans, these discharges instantly vaporize microscopic conductive traces inside CPUs and RAM. An anti-static wrist strap provides a safe, high-resistance path to chassis ground that bleeds off static charges continuously. Option A is false because power cords must already be unplugged before servicing.")
    ]

    for q_title, ans_line, rationale in mcq_solutions_t2:
        story.append(Paragraph(f"<b>{q_title}</b>", styles['DocBodyBold']))
        story.append(Paragraph(f"<font color='{COLOR_SUA_DARKGREEN}'><b>{ans_line}</b></font>", styles['DocBody']))
        story.append(Paragraph(f"<i>Conceptual Rationale:</i> {rationale}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    return story
