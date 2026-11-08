#!/usr/bin/env python3
"""
build_compedia_topic1.py
Comprehensive Academic Lecture Compendium for:
BIT 111: MICROCOMPUTERS AND APPLICATIONS
TOPIC 1: INTRODUCTION TO COMPUTERS
Department of Informatics and Information Technology (DIIT),
Sokoine University of Agriculture (SUA).

Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Curriculum Coverage:
- Subtopic 1.1: Evolution of Computers and Computer Generations (1st to 5th)
- Subtopic 1.2: History of Computing & Visionary Pioneers (From Abacus to Microprocessors)
- Subtopic 1.3: Multi-Dimensional Computer Classifications (By Size, Technology, Purpose, Role)
- Theoretical Hardware Physics, Register Transfer Notation, Instruction Execution Cycle
- Performance Modeling: CPU Equation, IPC, MIPS, FLOPS, Amdahl's Law, Power Wall
- Laboratory Practical Workshop: Linux Terminal Telemetry, Sysbench & Python Performance Modeling
- Case Studies: Smart Agriculture at SUA Mazimbu Farm & Precision Farming Telemetry
- Comprehensive Problem Set: 40 Multi-Part Self-Assessment Questions
- Exhaustive Solutions: Full Distractor Analysis for MCQs, Complete Step-by-Step Mathematical Derivations,
  Model Essays, and Production-Grade Enterprise Engineering Blueprints.

Target: Strictly >= 35 Pages (Targeting 37 - 42 Pages).
"""

import os
import sys

LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, HRFlowable
from reportlab.lib import colors
from compendium_base import (
    get_custom_stylesheet, create_custom_table, create_callout_box, create_example_box,
    create_code_box, create_figure_box, render_pdf,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_SUA_GREEN, COLOR_WHITE, COLOR_TEXT
)

def generate_topic_1_story():
    styles = get_custom_stylesheet()
    story = []

    # =========================================================
    # COVER / HEADER TITLE BLOCK
    # =========================================================
    header_data = [
        [Paragraph("SOKOINE UNIVERSITY OF AGRICULTURE", styles['CoverUniv'])],
        [Paragraph("School of Engineering and Technology / College of Natural and Applied Sciences", styles['CoverDept'])],
        [Paragraph("Department of Informatics and Information Technology (DIIT)", styles['CoverDept'])],
        [Spacer(1, 4)],
        [Paragraph("BIT 111: MICROCOMPUTERS AND APPLICATIONS", styles['CourseCode'])],
        [Paragraph("TOPIC 1: INTRODUCTION TO COMPUTERS — COMPREHENSIVE LECTURE COMPENDIUM", styles['CourseTitle'])],
        [Paragraph(
            "<b>Course Instructor:</b> Madam Bertha Msuliche Lebalwa (MSc)<br/>"
            "<b>Department:</b> Informatics and Information Technology (DIIT), SUA Morogoro<br/>"
            "<b>Target Audience:</b> First-Year Undergraduate Degree Students at Sokoine University of Agriculture<br/>"
            "<b>Curriculum Modules:</b> Computer Generations (1.1) | History & Pioneers (1.2) | Computer Classifications (1.3)<br/>"
            "<b>Assessment Weighting:</b> Continuous Assessment 60% (Assignments 5%, Tests 15%, Practical Report 10%, Practical Test 30%), UE 40%*<br/>"
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

    # Pedagogical Callout Box
    story.append(create_callout_box(
        "TOPIC 1 CURRICULUM OVERVIEW & STRATEGIC LEARNING OBJECTIVES",
        "This compendium establishes the physical, logical, mathematical, and historical foundations of electronic digital computing. "
        "By completing this module, undergraduate students at Sokoine University of Agriculture will be able to:<br/>"
        "1. Define the fundamental nature of computation, information processing, and the IPOS operational cycle.<br/>"
        "2. Trace the historical evolution of calculating machinery from mechanical aids to modern multi-core microprocessors.<br/>"
        "3. Evaluate the Von Neumann architectural paradigm, register transfer notation, and the instruction execution cycle.<br/>"
        "4. Differentiate the five technological computer generations by active electronic components, memory, and languages.<br/>"
        "5. Systematically classify computer systems across scale, underlying technology, operational purpose, and network roles.<br/>"
        "6. Calculate quantitative performance metrics including clock frequency, IPC, MIPS, FLOPS, and apply Amdahl's Law.<br/>"
        "7. Execute terminal-based hardware diagnostics and apply microcomputer tools to authentic agricultural and enterprise scenarios."
    ))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 1: THE NATURE OF DATA, INFORMATION & COMPUTATION
    # =========================================================
    story.append(Paragraph("1. THE NATURE OF DATA, INFORMATION, AND COMPUTATION", styles['SecH1']))
    story.append(Paragraph(
        "At the foundational level of informatics and computer engineering lies the distinction between raw observation and structured meaning. "
        "Electronic digital computers do not natively operate upon human concepts, agricultural harvests, or economic decisions; they operate upon discrete electrical voltage potentials representing binary digits (bits). "
        "Understanding how physical phenomena are transformed into mathematical abstractions is essential for every computing professional.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>1.1 Data vs Information vs Knowledge</b><br/>"
        "• <b>Data:</b> Raw, unorganized, uninterpreted symbols, figures, signals, or characters gathered through observation or measurement. "
        "Data lacks context, intentionality, and standalone utility. For instance, the sequence of numbers <code>[28.4, 62.1, 1013.2, 0.0]</code> represents data; without metadata and schema, it cannot inform action. "
        "Data may be qualitative (descriptive labels such as crop variety names, soil color classifications) or quantitative (numerical measurements of grain moisture content, ambient temperature, tractor speed). In microcomputers, data is physically encoded as high and low voltage states across silicon memory cells.<br/>"
        "• <b>Information:</b> Data that has been processed, structured, organized, contextualized, and presented within an analytical framework so that it becomes meaningful, intelligible, and actionable. "
        "When the previous sequence is interpreted as: <i>'At SUA Mazimbu Meteorological Station on 12 October 2026 at 14:00 EAT: Air Temperature = 28.4°C, Relative Humidity = 62.1%, Barometric Pressure = 1013.2 hPa, Precipitation = 0.0 mm'</i>, it constitutes information. "
        "Information reduces uncertainty, resolves ambiguities, and reveals operational conditions within physical systems.<br/>"
        "• <b>Knowledge:</b> The synthesis of information, contextual understanding, predictive rules, empirical experience, and cognitive models that enables effective decision-making. "
        "For example, knowing that combining an air temperature of 28.4°C with 62.1% relative humidity in maize cultivation creates optimal conditions for the sporulation of <i>Exserohilum turcicum</i> (Northern Corn Leaf Blight) allows agricultural extension officers to dispatch preventative fungicide advisories.<br/>"
        "• <b>Metadata:</b> Data describing other data, providing essential contextual attributes such as spatial coordinates (GPS latitude/longitude), sampling frequency, sensor serial identifiers, unit dimensions, and timestamps.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>1.2 The Information Processing Cycle (IPOS)</b><br/>"
        "Every digital microcomputer, from a humble microcontroller managing drip irrigation to a multi-socket enterprise server at the SUA Directorate of Information and Communication Technology (DICT), executes the universal Information Processing Cycle:",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "1. <b>Input:</b> The systematic acquisition and ingestion of external data and instructions into the computer's internal digital representation. Input is mediated by input transducers and peripheral interfaces (keyboards, optical mice, touch digitizers, barcode readers, and analog-to-digital converters connected to environmental probes). In microcomputers, input signals trigger bus interrupts or populate direct memory access (DMA) buffers.<br/>"
        "2. <b>Processing:</b> The manipulation, arithmetic calculation, logical evaluation, and algorithmic transformation of binary data executed by the Central Processing Unit (CPU). Under the direction of stored program instructions, the Arithmetic Logic Unit (ALU) performs operations such as addition, bitwise shifting, and magnitude comparison, altering internal register states.<br/>"
        "3. <b>Output:</b> The translation and conveyance of internally processed binary results into forms comprehensible to human operators or actuatable by mechanical machinery. Output channels include visual display units (LCD/OLED monitors rendering rasterized graphics), impact and non-impact printers, audio digital-to-analog converters, and electromechanical relay actuators that open irrigation valves.<br/>"
        "4. <b>Storage:</b> The non-volatile retention of digital code, datasets, operating system files, and user records for future retrieval. Primary memory (RAM) is volatile and loses state upon power removal; secondary and tertiary storage subsystems (Solid-State Drives, Hard Disk Drives, optical media, and cloud repositories) preserve data across power cycles.<br/>"
        "5. <b>Communication (The Contemporary Fifth Dimension):</b> In modern distributed environments, standalone IPOS is insufficient. Microcomputers continuously transmit telemetry, synchronize databases, and receive software payloads over serial buses, Local Area Networks (Ethernet, Wi-Fi), and Low-Power Wide-Area Networks (LoRaWAN, cellular NB-IoT).",
        styles['DocBody']
    ))
    story.append(Spacer(1, 8))

    # =========================================================
    # SECTION 2: THE VON NEUMANN ARCHITECTURAL PARADIGM
    # =========================================================
    story.append(Paragraph("2. THE VON NEUMANN ARCHITECTURAL PARADIGM", styles['SecH1']))
    story.append(Paragraph(
        "Prior to 1945, calculating machines were special-purpose instruments whose operational sequence was dictated by fixed mechanical gearing or physical electrical wiring. "
        "Reprogramming the ENIAC to solve a different artillery trajectory required a team of operators to physically re-route hundreds of cables and re-set thousands of multi-pole switches over several days. "
        "In June 1945, mathematician and physicist John von Neumann authored the landmark document <i>'First Draft of a Report on the EDVAC'</i> (Electronic Discrete Variable Automatic Computer), articulating the theoretical architecture that remains the foundation of virtually all modern microcomputers.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>2.1 The Stored-Program Concept</b><br/>"
        "The core innovation of the Von Neumann architecture is the <b>stored-program concept</b>: program instructions (the operational codes instructing the CPU what actions to perform) and program data (the numeric values and strings operated upon) reside together in the same physically unified, addressable, read-write electronic memory space. "
        "Because instructions are encoded as binary numbers identical in format to data, a program can be loaded from secondary storage into RAM dynamically, modified during runtime, and replaced by a completely different program without altering a single physical wire. "
        "This single conceptual breakthrough transformed computers from rigid calculating appliances into universal, Turing-complete information processing engines.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>2.2 The Five Architectural Subsystems</b><br/>"
        "The classical Von Neumann model partitions the computing machine into five fundamental functional units:<br/>"
        "• <b>Control Unit (CU):</b> The coordinator and conductor of the microcomputer. The CU fetches instructions sequentially from memory, decodes their operational bit patterns, and emits micro-control electrical signals across internal buses to coordinate the ALU, registers, and memory.<br/>"
        "• <b>Arithmetic Logic Unit (ALU):</b> The computational core executing elementary binary arithmetic (addition, subtraction, multiplication, division) and Boolean logic (AND, OR, NOT, XOR, bit shifts).<br/>"
        "• <b>Memory Subsystem:</b> A linear, indexed sequence of addressable storage cells capable of holding both machine instructions and operands. In byte-addressable architectures, each 8-bit memory cell is uniquely mapped to a numerical physical address.<br/>"
        "• <b>Input Subsystem:</b> The hardware interface through which external data enters the computer's internal registers from peripheral transducers.<br/>"
        "• <b>Output Subsystem:</b> The hardware interface delivering internal computational states to external peripheral actuators and human-readable interfaces.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 6))

    # Embed Figure 1.2
    story.append(create_figure_box(
        "fig1_2_von_neumann_architecture.png",
        "The Classical Von Neumann Architecture: CPU, Shared Primary Memory, and the Tri-Bus Interconnect.",
        width=5.8 * inch, height=2.8 * inch
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>2.3 Register Transfer Notation & The Instruction Execution Cycle</b><br/>"
        "At the hardware level, instruction execution proceeds in a rigorous micro-operational sequence known as the <b>Fetch-Decode-Execute Cycle</b>. "
        "This sequence is formally described using Register Transfer Notation (RTN):<br/>"
        "1. <b>Fetch Micro-operations:</b><br/>"
        "   • <code>MAR ← [PC]</code>: The address currently contained in the Program Counter (PC) is transferred onto the internal bus and latched into the Memory Address Register (MAR).<br/>"
        "   • <code>Control Line ← READ</code>: The Control Unit asserts the memory read control signal, placing the memory subsystem into output mode.<br/>"
        "   • <code>MDR ← [Memory at MAR]</code>: Primary memory places the contents of the addressed location onto the Data Bus, which is latched into the Memory Data Register (MDR).<br/>"
        "   • <code>IR ← [MDR]</code>: The instruction word in MDR is transferred to the Instruction Register (IR).<br/>"
        "   • <code>PC ← [PC] + 1</code>: The Program Counter is incremented to point to the next contiguous instruction address.<br/>"
        "2. <b>Decode Micro-operations:</b><br/>"
        "   • The Control Unit decodes the opcode bits in the IR, resolving the required addressing mode (direct, indirect, register, immediate) and operand memory addresses.<br/>"
        "3. <b>Execute Micro-operations:</b><br/>"
        "   • The ALU performs the specified operation (e.g., adding an operand from memory to the Accumulator register). Status flags (Zero, Carry, Sign, Overflow) are updated.<br/>"
        "4. <b>Interrupt Check:</b><br/>"
        "   • The Control Unit evaluates whether external hardware interrupt lines (timer interrupts, keyboard interrupts, network packet notifications) are asserted. If asserted, the CPU saves its register state to the stack and jumps to the Interrupt Service Routine (ISR).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>2.4 The Von Neumann Bottleneck and Architectural Counter-Measures</b><br/>"
        "While the unified memory model provided unprecedented flexibility, it introduced a severe architectural vulnerability known as the <b>Von Neumann Bottleneck</b>. "
        "Because a single shared physical bus is utilized to fetch instructions and to transfer data operands between the CPU and memory, throughput is inherently constrained. "
        "The CPU cannot read an instruction and read/write data simultaneously; memory access must be strictly serialized. "
        "Over the decades, semiconductor fabrication advancements caused CPU processing speeds to scale dramatically (from kilohertz to multi-gigahertz), whereas DRAM memory latency improved at a substantially slower rate (the 'Memory Wall'). "
        "Consequently, modern high-frequency microprocessors spend a significant proportion of their operational cycles idling ('memory stalls') waiting for operands to arrive from main RAM.<br/>"
        "Modern computer engineering mitigates this bottleneck through several architectural strategies:<br/>"
        "1. <b>Multi-Level Cache Hierarchies (L1, L2, L3):</b> Small, ultra-fast static RAM (SRAM) buffers placed directly on the CPU silicon die to store recently accessed instructions and data.<br/>"
        "2. <b>Pipelining and Branch Prediction:</b> Overlapping instruction execution stages and speculative pre-fetching of anticipated code paths.<br/>"
        "3. <b>Modified Harvard Architecture in Caches:</b> Modern microprocessors implement a 'Modified Harvard' architecture: while external main memory is unified (Von Neumann), on-die Level-1 cache is physically split into a dedicated L1 Instruction Cache (L1i) and a dedicated L1 Data Cache (L1d), allowing simultaneous instruction fetch and operand transfer.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 8))

    # =========================================================
    # SECTION 3: THE FIVE COMPUTER GENERATIONS
    # =========================================================
    story.append(Paragraph("3. EVOLUTION OF COMPUTERS: THE FIVE GENERATIONS", styles['SecH1']))
    story.append(Paragraph(
        "The technological history of modern electronic digital computing is categorized into five distinct generations. "
        "Each generation is demarcated by a fundamental paradigm shift in the underlying <b>active switching electronics</b>, which in turn revolutionized physical scale, operational reliability, power consumption, memory capacity, and programming abstractions.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 4))

    # Embed Figure 1.1
    story.append(create_figure_box(
        "fig1_1_computer_generations.png",
        "The Chronological Progression of the Five Computer Generations (1940 to Present and Beyond).",
        width=5.8 * inch, height=2.8 * inch
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>3.1 First Generation (1940 – 1956): The Thermionic Valve Era</b><br/>"
        "• <b>Primary Switching Device:</b> The Vacuum Tube (Thermionic Valve). A sealed glass envelope containing an anode, cathode, and control grid operating in a vacuum. By modulating the grid voltage, the flow of thermionically emitted electrons between cathode and anode is switched on or off, functioning as a binary gate.<br/>"
        "• <b>Physical Characteristics & Limitations:</b> Vacuum tubes were physically massive (several centimeters tall), generated enormous thermal dissipation, and required substantial electrical filament power. Filaments burned out frequently; the mean time between failures (MTBF) of first-generation computers was measured in mere hours. Cooling required massive industrial refrigeration units.<br/>"
        "• <b>Internal Memory Technologies:</b> Mercury Acoustic Delay Lines (where ultrasonic pulses traveled through tubes of liquid mercury and were refreshed cyclically), Williams-Kilburn Electrostatic Tubes (storing charge on CRT phosphor screens), and rotating magnetic drums.<br/>"
        "• <b>Storage & I/O:</b> Punched cards (utilizing the 80-column Hollerith card format) and punched paper tape.<br/>"
        "• <b>Programming Paradigm:</b> Raw Machine Language (binary opcodes and addresses wired manually or punched into cards). No operating systems existed; a single user booked physical machine time and toggled front-panel console switches.<br/>"
        "• <b>Landmark Computers:</b> ENIAC (1945, 17,468 tubes, 30 tons, 150 kW), EDVAC (1949, first stored-program implementation), UNIVAC I (1951, first commercially manufactured computer sold to the US Census Bureau).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>3.2 Second Generation (1956 – 1963): The Solid-State Transistor Era</b><br/>"
        "• <b>Primary Switching Device:</b> The Bipolar Junction Transistor (BJT). Invented in December 1947 at Bell Telephone Laboratories by John Bardeen, Walter Brattain, and William Shockley. Transistors utilize solid semiconductor materials (germanium, later silicon) with doped p-n junctions to switch and amplify current.<br/>"
        "• <b>Engineering Advantages:</b> Transistors required no vacuum envelope, had no fragile heating filaments, consumed approximately 1/1000th the electrical power of vacuum tubes, generated negligible heat, and were physically smaller by two orders of magnitude. System reliability and MTBF increased from hours to hundreds of hours.<br/>"
        "• <b>Internal Memory Technology:</b> Magnetic Ferrite Core Memory. Tiny toroidal rings of ferromagnetic ceramic strung on wire matrices; each core was magnetized clockwise or counter-clockwise to store a non-volatile binary 1 or 0.<br/>"
        "• <b>Secondary Storage:</b> High-speed magnetic tape reels and the first commercial magnetic disk drives (e.g., the IBM 350 Disk Storage Unit on the RAMAC 305 system in 1956, featuring fifty 24-inch platters storing 5 MB).<br/>"
        "• <b>Software Evolution:</b> Emergence of symbolic <b>Assembly Language</b> (using mnemonic codes such as <code>MOV</code>, <code>ADD</code>, <code>JMP</code> instead of binary) and early <b>High-Level Programming Languages</b>. FORTRAN (Formula Translation, 1957) revolutionized scientific computation, while COBOL (Common Business-Oriented Language, 1959) standardized commercial data processing. Rudimentary batch processing monitors emerged.<br/>"
        "• <b>Landmark Computers:</b> IBM 7090, IBM 1401 (widely deployed business system), DEC PDP-1 (which hosted the first computer video game, <i>Spacewar!</i>).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>3.3 Third Generation (1964 – 1971): The Integrated Circuit (IC) Era</b><br/>"
        "• <b>Primary Switching Device:</b> The Monolithic Integrated Circuit (IC). Invented independently by Jack Kilby of Texas Instruments (hybrid microcircuit on germanium, 1958) and Robert Noyce of Fairchild Semiconductor (planar integrated circuit on silicon, 1959). Multiple transistors, diodes, resistors, and capacitors were fabricated simultaneously on a single silicon substrate.<br/>"
        "• <b>Scale of Integration:</b> Small-Scale Integration (SSI: 10 to 100 transistors per die) and Medium-Scale Integration (MSI: 100 to 1,000 transistors per die). This eliminated the 'tyranny of numbers' — the physical impossibility of manually soldering millions of discrete wiring interconnections without catastrophic connection faults.<br/>"
        "• <b>Operating Systems & Time-Sharing:</b> True multiprogramming operating systems emerged (e.g., IBM OS/360). <b>Time-Sharing</b> allowed dozens of simultaneous users to access a central processor concurrently via interactive Video Display Terminals (VDTs) equipped with cathode ray tubes and keyboards, displacing batch punched card submissions.<br/>"
        "• <b>Standardization:</b> Introduction of the standard 8-bit byte and ASCII (American Standard Code for Information Interchange) character encoding.<br/>"
        "• <b>Landmark Computers:</b> IBM System/360 family (the landmark mainframe platform establishing upward software compatibility), DEC PDP-8 (the world's first mass-market minicomputer, priced under $20,000).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>3.4 Fourth Generation (1971 – Present): The Microprocessor & VLSI Era</b><br/>"
        "• <b>Primary Switching Device:</b> The Silicon Microprocessor. Enabled by Large-Scale Integration (LSI: 1,000 to 10,000 transistors) and Very Large-Scale Integration (VLSI: 100,000 to millions of transistors on a single silicon die). In 1971, Intel engineers Marcian 'Ted' Hoff, Federico Faggin, and Stan Mazor designed the <b>Intel 4004</b> — a complete 4-bit central processing unit integrated onto a single microchip containing 2,300 transistors.<br/>"
        "• <b>Primary Memory:</b> Solid-state semiconductor Dynamic Random-Access Memory (DRAM) displaced magnetic core memory, offering nanosecond access times and high density.<br/>"
        "• <b>The Personal Computer (PC) Revolution:</b> Computing power shifted from centralized corporate glass-room datacenters directly onto individual office desks and into private homes. Landmark microcomputers included the MITS Altair 8800 (1975), Apple II (1977), and the IBM 5150 Personal Computer (1981) powered by the Intel 8088 CPU and Microsoft MS-DOS.<br/>"
        "• <b>Human-Computer Interfaces:</b> Graphical User Interfaces (GUIs) featuring overlapping windows, icons, drop-down menus, and mouse pointers (WIMP paradigm) popularized by the Xerox Alto, Apple Macintosh (1984), and Microsoft Windows.<br/>"
        "• <b>Storage & Networks:</b> 5.25\" and 3.5\" floppy diskettes, high-density magnetic hard drives, CD-ROMs, local area networks (Ethernet), and the explosive proliferation of the global Internet.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>3.5 Fifth Generation (Present & Emerging): ULSI, Artificial Intelligence & Quantum Systems</b><br/>"
        "• <b>Primary Hardware Paradigm:</b> Ultra Large-Scale Integration (ULSI: billions of transistors fabricated using extreme ultraviolet photolithography at 3-nanometer and 2-nanometer gate geometries). Pervasive multi-core and many-core processor architectures.<br/>"
        "• <b>Heterogeneous Computing Accelerators:</b> Integration of specialized silicon execution blocks alongside CPU cores, including Graphics Processing Units (GPUs for massively parallel SIMD computing), Neural Processing Units (NPUs), and Tensor Processing Units (TPUs) dedicated to deep learning matrix multiplications.<br/>"
        "• <b>Artificial Intelligence & Autonomous Systems:</b> Fifth-generation computing emphasizes artificial neural networks, natural language processing, computer vision, voice recognition, and real-time autonomous robotics (e.g., self-guided agricultural combine harvesters).<br/>"
        "• <b>Distributed Cloud & Edge Computing:</b> Computing resources abstracted into globally elastic serverless cloud datacenters interconnected by multi-terabit fiber backbones, paired with edge-computing microcomputers processing telemetry on site.<br/>"
        "• <b>Frontier Paradigms:</b> Quantum Computing (manipulating quantum bits or qubits exhibiting superposition and entanglement to execute complex optimization and cryptographic computations exponentially faster than classical Turing machines).",
        styles['DocBody']
    ))
    story.append(Spacer(1, 8))

    # Reference Table 1.1: Generations Comparison
    story.append(Paragraph("<b>Table 1.1: Systematic Comparison of the Five Computer Generations</b>", styles['SecH3']))
    gen_headers = ["Generation", "Active Device", "Primary Memory", "Secondary Storage", "Programming Languages", "Typical Speed", "Seminal Machines"]
    gen_rows = [
        ["1st (1940–56)", "Vacuum Tubes", "Mercury Delay Lines, Drum", "Punched Cards, Paper Tape", "Machine Language", "10–40 KIPS", "ENIAC, EDVAC, UNIVAC I"],
        ["2nd (1956–63)", "BJT Transistors", "Magnetic Ferrite Core", "Magnetic Tape, Early Disk", "Assembly, FORTRAN, COBOL", "100–500 KIPS", "IBM 7090, IBM 1401, PDP-1"],
        ["3rd (1964–71)", "Integrated Circuits (SSI/MSI)", "Magnetic Core / Early Semis", "Magnetic Disk Packs (DASD)", "BASIC, Pascal, C, PL/I", "1–10 MIPS", "IBM System/360, PDP-8"],
        ["4th (1971–Pres)", "VLSI Microprocessor", "Semiconductor DRAM", "Floppy, HDD, SSD, Optical", "OOP (Java, C++), Python, SQL", "100–100,000 MIPS", "Apple II, IBM PC, Pentium"],
        ["5th (Emerging)", "ULSI, NPUs, Qubits", "High-Bandwidth 3D DRAM", "NVMe SSD, Distributed Cloud", "AI Frameworks, Declarative", "TFLOPS to EFLOPS", "Multi-core CPUs, H100, TPU"]
    ]
    story.append(create_custom_table(gen_headers, gen_rows, col_widths=[0.9*inch, 1.1*inch, 1.1*inch, 1.1*inch, 1.2*inch, 0.8*inch, 1.0*inch]))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 4: HISTORICAL TIMELINE & VISIONARY PIONEERS
    # =========================================================
    story.append(Paragraph("4. HISTORICAL FOUNDATIONS & VISIONARY PIONEERS", styles['SecH1']))
    story.append(Paragraph(
        "The contemporary microcomputer is not the creation of a single inventor or company; it is the cumulative intellectual achievement of centuries of mathematics, mechanical engineering, and physical discoveries. "
        "Understanding these historical pioneers provides critical insight into the conceptual roots of modern computer science.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>4.1 Mechanical Calculating Precursors</b><br/>"
        "• <b>The Abacus (c. 2500 BCE, Mesopotamia and Asia):</b> The earliest recorded calculating instrument, utilizing beads sliding on parallel rods to perform positional decimal arithmetic. It established the concept of representing numerical values through physical spatial states.<br/>"
        "• <b>Napier's Bones (1617, John Napier):</b> A set of graduated ivory rods carved with multiplication tables based on lattice multiplication. Napier also invented logarithms, reducing complex multiplication and division to basic addition and subtraction.<br/>"
        "• <b>The Slide Rule (1622, William Oughtred):</b> An analog calculating device utilizing logarithmic scales sliding past each other. It served as the primary calculating instrument for scientists, agricultural surveyors, and engineers for over three centuries until the advent of electronic pocket calculators in the 1970s.<br/>"
        "• <b>The Pascaline (1642, Blaise Pascal):</b> The first operational mechanical adding machine, built by Pascal at age 19 to assist his father, a French tax collector. It used a series of ten-toothed geared wheels with an innovative gravity-assisted carry mechanism (the <i>sautoir</i>) to perform direct addition and subtraction.<br/>"
        "• <b>The Stepped Reckoner (1673, Gottfried Wilhelm Leibniz):</b> A mechanical digital calculator featuring the stepped drum (Leibniz wheel) mechanism. It was the first machine capable of direct multiplication and division. Leibniz also published <i>'Explication de l'Arithmétique Binaire'</i> (1703), formally establishing the binary number system (base-2) and demonstrating that all mathematical logic could be computed using binary 0 and 1.<br/>"
        "• <b>The Jacquard Loom (1804, Joseph Marie Jacquard):</b> A mechanical loom utilizing a sequence of stiff pasteboard punched cards to automate the weaving of intricate textile tapestries. The presence or absence of a hole in a card determined whether a warp thread was raised or lowered. This was the first operational realization of <b>stored digital programming</b>.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>4.2 The Visionary Architect and the First Programmer</b><br/>"
        "• <b>Charles Babbage (1791–1871) — The Father of Computing:</b> British mathematician and mechanical engineer who recognized that printed mathematical navigation and astronomical tables contained dangerous human calculation errors. He conceived two revolutionary mechanical calculating engines:<br/>"
        "    - <i>The Difference Engine (1822):</i> A specialized mechanical calculator designed to tabulate polynomial functions automatically using the mathematical method of finite differences. A working model was constructed by the Science Museum of London in 1991, proving Babbage's design fully functional.<br/>"
        "    - <i>The Analytical Engine (1837):</i> Babbage's masterpiece — the conceptual prototype of the modern general-purpose digital computer. It incorporated all fundamental components of modern computer architecture: the <b>Store</b> (memory holding 1,000 numbers of 50 decimal digits each), the <b>Mill</b> (arithmetic processing unit executing operations), punched card input (inspired by Jacquard), and sequential control flow with conditional branching.<br/>"
        "• <b>Augusta Ada Lovelace (1815–1852) — The World's First Computer Programmer:</b> English mathematician and daughter of Lord Byron. While translating Luigi Menabrea's French lecture notes on Babbage's Analytical Engine, Lovelace appended extensive annotations (the famous 'Notes'). In Note G, she authored an algorithm to calculate Bernoulli numbers, recognized as the world's first published computer program. Lovelace foresaw that computers were not merely number crunchers: she argued that if physical entities (such as musical notes, language, or agricultural attributes) could be expressed symbolically, the Analytical Engine could compose symphonies, manipulate graphics, and execute complex logical workflows.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>4.3 Electromechanical Census Tabulation and Theoretical Foundations</b><br/>"
        "• <b>Herman Hollerith (1860–1929):</b> American engineer who developed an electromechanical punched card tabulating system for the 1890 US Census. Census data was punched into standardized 80-column paper cards. When pressed into a mercury-filled well, metal pins passed through holes, completing electrical circuits that incremented mechanical counting dials. The 1890 census was completed in under three years (saving $5 million) compared to eight years for the 1880 census. In 1896, Hollerith founded the Tabulating Machine Company, which in 1924 merged and was renamed <b>International Business Machines (IBM)</b>.<br/>"
        "• <b>Alan Mathison Turing (1912–1954):</b> British logician, mathematician, and the father of theoretical computer science and artificial intelligence. In his 1936 paper <i>'On Computable Numbers, with an Application to the Entscheidungsproblem'</i>, Turing introduced the <b>Universal Turing Machine (UTM)</b> — an abstract mathematical model of an infinite tape and read/write head that established the theoretical boundaries of what is mathematically computable. During World War II at Bletchley Park, Turing designed the electromechanical 'Bombe', breaking Nazi military Enigma ciphers. In 1950, he published <i>'Computing Machinery and Intelligence'</i>, formulating the Turing Test to evaluate artificial intelligence.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>4.4 Pioneers of the Electronic and Microprocessor Era</b><br/>"
        "• <b>John Vincent Atanasoff & Clifford Berry (1939–1942):</b> Built the Atanasoff-Berry Computer (ABC) at Iowa State University, the first electronic digital calculating device utilizing binary arithmetic, regenerative capacitor memory, and vacuum tube switching.<br/>"
        "• <b>John Mauchly & J. Presper Eckert (1943–1946):</b> Designed and constructed the ENIAC at the Moore School of Electrical Engineering, University of Pennsylvania, to compute military firing tables. Later they designed EDVAC and founded the Eckert-Mauchly Computer Corporation, building UNIVAC I.<br/>"
        "• <b>John von Neumann (1903–1957):</b> Formulated the unified stored-program architecture, formalizing the relationship between memory, arithmetic processing, control sequencing, and bus interconnects.<br/>"
        "• <b>Jack Kilby & Robert Noyce (1958/1959):</b> Co-inventors of the Integrated Circuit. Noyce co-founded Fairchild Semiconductor and Intel Corporation.<br/>"
        "• <b>Gordon Moore (1929–2023):</b> Intel co-founder who formulated <b>Moore's Law</b> in 1965, observing that the number of transistors on a microchip doubles approximately every 18 to 24 months with a corresponding decrease in cost per transistor.<br/>"
        "• <b>Steve Jobs & Steve Wozniak (1976):</b> Founded Apple Computer in a Los Altos garage. Wozniak engineered the Apple I and Apple II single-board microcomputers, while Jobs championed the consumer GUI, laser typography, and the graphical desktop metaphor in the Macintosh.<br/>"
        "• <b>Bill Gates & Paul Allen (1975):</b> Founded Microsoft, licensing Altair BASIC and acquiring 86-DOS from Seattle Computer Products, which was re-engineered as MS-DOS for the IBM PC platform.<br/>"
        "• <b>Dennis Ritchie & Ken Thompson (1969–1972):</b> Created the UNIX operating system and the C programming language at AT&T Bell Labs, establishing the foundation of contemporary operating system software and POSIX standards.<br/>"
        "• <b>Tim Berners-Lee (1989):</b> British computer scientist at CERN who invented the World Wide Web, creating HTML, HTTP, URLs, and the first web browser/server, transforming interconnected computer networks into a globally accessible hypermedia repository.<br/>"
        "• <b>Linus Torvalds (1991):</b> Finnish computer science student who authored the open-source <b>Linux</b> kernel, establishing the foundational operating system powering global cloud servers, supercomputers, Android smartphones, and enterprise research clusters.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 8))

    # =========================================================
    # SECTION 5: MULTI-DIMENSIONAL COMPUTER CLASSIFICATIONS
    # =========================================================
    story.append(Paragraph("5. MULTI-DIMENSIONAL CLASSIFICATION OF COMPUTERS", styles['SecH1']))
    story.append(Paragraph(
        "Computer systems can be classified across multiple orthogonal operational and architectural dimensions: "
        "(1) Physical Size, Scale, and Processing Power; (2) Underlying Technology and Signal Representation; (3) Operational Purpose; and (4) Network Roles.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 4))

    # Embed Figure 1.3
    story.append(create_figure_box(
        "fig1_3_computer_classifications.png",
        "Multi-Dimensional Taxonomy: Scale, Signal Technology, and Operational Purpose.",
        width=5.8 * inch, height=2.8 * inch
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>5.1 Classification by Physical Size and Processing Power</b><br/>"
        "• <b>Supercomputers:</b> The apex of computational capability. Designed for maximum floating-point throughput (FLOPS). Modern frontier supercomputers (e.g., Frontier at Oak Ridge National Laboratory) exceed 1 ExaFLOPS (10<sup>18</sup> calculations per second). They feature hundreds of thousands of multi-core CPU and GPU nodes interconnected via ultra-low-latency networks (InfiniBand at 400 Gbps), consuming 15 to 25 Megawatts of electrical power and utilizing direct liquid immersion cooling. Applied in global climate forecasting, aerodynamic simulations, quantum molecular modeling, and national crop genomic sequencing.<br/>"
        "• <b>Mainframe Computers:</b> Massive multi-user enterprise servers engineered not for peak floating-point speed, but for unmatched <b>Reliability, Availability, and Serviceability (RAS)</b> and massive concurrent I/O throughput. Mainframes feature dedicated hardware channel processors that offload storage and network interrupts from central compute cores. They achieve 'five nines' (99.999%) availability (less than 5 minutes downtime per year) through hardware lockstepping, dynamic error correction, and hot-swappable components. Mainframes run core transactional workloads: nationwide banking clearing (e.g., CRDB Bank and NMB Bank in Tanzania), automated airline ticketing, and tax revenue accounting (e.g., IBM z16 running z/OS).<br/>"
        "• <b>Minicomputers (Midrange Computers):</b> Historically filled the niche between single-user microcomputers and massive mainframes from the 1960s to 1980s (e.g., DEC VAX-11/780, IBM AS/400). Typically supported 20 to 100 simultaneous users sharing compute time via dumb terminals for university departments or manufacturing plants. Largely superseded today by commodity rack-mounted multi-socket microcomputer servers.<br/>"
        "• <b>Microcomputers (Personal Computers):</b> Any computing system whose Central Processing Unit is built as a single integrated microprocessor. Microcomputers represent the most pervasive computing platform on earth, spanning desktops, laptops, tablets, and smartphones.<br/>"
        "    - <i>Engineering Workstations:</i> High-performance microcomputers equipped with multi-core enterprise CPUs (Intel Xeon, AMD Threadripper), Error-Correcting Code (ECC) memory, and workstation-class graphics accelerators (Nvidia RTX A-series) with ISV-certified drivers for CAD, 3D GIS photogrammetry, and statistical modeling.<br/>"
        "    - <i>Desktop Microcomputers:</i> Traditional modular computers housed in desktop or tower chassis; offer high upgradeability, full PCIe expansion slots, and cost-effective performance.<br/>"
        "    - <i>Mobile Laptops and Tablets:</i> Portable microcomputers integrating flat-panel displays, rechargeable batteries, and low-power mobile microprocessors (TDP 15–45W).<br/>"
        "• <b>Embedded Computers & Microcontrollers:</b> Dedicated computing engines integrated directly into larger physical machines, appliances, or vehicles. A <b>Microcontroller Unit (MCU)</b> integrates the CPU, flash ROM firmware, SRAM, timers, and analog/digital peripheral interfaces onto a single silicon chip. They operate under tight resource constraints (clock speeds of 16–240 MHz, RAM of 2 KB to 512 KB), prioritizing low electrical power (milliwatts) and extreme environmental tolerance. Examples include engine electronic control units (ECUs), automated tractor guidance autosteer systems, drone flight controllers, and solar irrigation telemetry nodes.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>5.2 Classification by Underlying Technology and Signal Representation</b><br/>"
        "• <b>Analog Computers:</b> Process continuous physical variables (voltage, current, hydraulic pressure, mechanical shaft rotation) without converting them into discrete numerical values. Mathematical operations (integration, differentiation, addition) are performed directly through analog circuit laws (Ohm's law, Kirchhoff's laws, operational amplifiers). Analog computers execute operations instantaneously and in parallel, but suffer from limited precision (typically 3 to 4 significant digits) and calibration drift due to thermal variations.<br/>"
        "• <b>Digital Computers:</b> Process discrete, quantized binary signals (binary digits 0 and 1, represented physically by low and high voltage thresholds, e.g., 0V and +3.3V). All alphanumeric data, images, sounds, and mathematical operations are abstracted into binary words. Digital computers provide arbitrary mathematical precision, perfect reproducibility, high noise immunity, and immense programmability.<br/>"
        "• <b>Hybrid Computers:</b> Combine the continuous real-time processing speed of analog circuitry with the high precision, logical decision-making, and digital memory of a microcomputer. The analog subsystem models rapid dynamic physical processes (such as flight dynamics or fluid kinetics), while the digital subsystem handles supervisory control, data logging, and parameter optimization. Critical in flight simulators, hospital ICU patient telemetry, and precision agricultural chemical spray injection systems.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>5.3 Classification by Operational Purpose</b><br/>"
        "• <b>General-Purpose Computers:</b> Designed to execute an arbitrary variety of software applications under the control of a versatile operating system. The same physical hardware can compile a Python program, run an agricultural finite element simulation, compose an academic dissertation, stream multimedia, and browse the web.<br/>"
        "• <b>Special-Purpose (Dedicated) Computers:</b> Engineered and hardwired to perform a single invariant task or narrow set of tasks with optimal efficiency. Their programming is typically burned permanently into ROM/Flash firmware. Examples include Automated Teller Machine (ATM) controllers, digital microwave timers, automotive anti-lock braking (ABS) controllers, and digital agricultural moisture meters.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>5.4 Classification by Network Role and Architecture</b><br/>"
        "• <b>Clients:</b> End-user microcomputers that request computational services, files, database records, or web applications across a network. Clients host user-facing software (web browsers, thin client shells).<br/>"
        "• <b>Servers:</b> High-capacity computing nodes configured to listen for and fulfill incoming requests from client nodes across local or wide-area networks. Categorized by functional workload: Web Servers (HTTP/HTTPS), File Servers (NFS, SMB), Database Servers (PostgreSQL, MySQL), Mail Servers (SMTP, IMAP), and Directory Servers (Active Directory, LDAP).<br/>"
        "• <b>Peer-to-Peer (P2P) Nodes:</b> Nodes in a decentralized network architecture where every microcomputer possesses equivalent privileges and responsibilities, acting simultaneously as both client and server (e.g., BitTorrent file distribution, blockchain validation nodes).",
        styles['DocBody']
    ))
    story.append(Spacer(1, 8))

    # Reference Table 1.2: Computer Scale Specifications
    story.append(Paragraph("<b>Table 1.2: Hardware Specifications Across Computer Scales</b>", styles['SecH3']))
    scale_headers = ["Category", "Typical Processor", "Memory (RAM)", "Operating System", "Power Draw", "Target Domain"]
    scale_rows = [
        ["Supercomputer", "100,000+ Cores (Xeon/EPYC/H100)", "Petabytes (HBM/DRAM)", "Custom Enterprise Linux", "10–25 MW", "Global Climate, Genomic Sequencing"],
        ["Mainframe", "Multi-socket Telum / z16", "Terabytes to Petabytes", "IBM z/OS, Linux on Z", "10–50 kW", "High-Volume Banking & Airline Trans."],
        ["Workstation", "Intel Xeon, AMD Threadripper", "64 GB to 1 TB ECC", "Windows Pro / Ubuntu LTS", "400–1200 W", "CAD Engineering, 3D GIS Photogram."],
        ["Desktop PC", "Intel Core i5/i7, AMD Ryzen", "8 GB to 64 GB Non-ECC", "Windows 11, macOS, Linux", "65–350 W", "Enterprise Admin, Student Labs"],
        ["Embedded MCU", "ARM Cortex-M, ESP32, AVR", "2 KB to 512 KB SRAM", "Bare-metal, FreeRTOS", "0.01–2 W", "Tractor Autosteer, Field Telemetry"]
    ]
    story.append(create_custom_table(scale_headers, scale_rows, col_widths=[1.1*inch, 1.4*inch, 1.1*inch, 1.2*inch, 0.8*inch, 1.6*inch]))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 6: QUANTITATIVE PERFORMANCE METRICS & AMDAHL'S LAW
    # =========================================================
    story.append(Paragraph("6. QUANTITATIVE PERFORMANCE MODELING & ARCHITECTURAL LIMITS", styles['SecH1']))
    story.append(Paragraph(
        "Evaluating microcomputer performance requires rigorous mathematical metrics rather than intuitive assumptions. "
        "Historically, marketing departments relied on clock frequency alone (the 'Megahertz Myth') to persuade consumers that higher clock rates guaranteed faster performance. "
        "In computer architecture, true execution time is governed by the fundamental <b>CPU Performance Equation</b>.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>6.1 The Fundamental CPU Performance Equation</b><br/>"
        "The CPU execution time required to complete a given software workload is derived from three interdependent variables:<br/>"
        "• <b>Instruction Count (IC):</b> The total number of machine code instructions executed during program execution. Governed by the algorithm, high-level language compiler optimization, and the processor's Instruction Set Architecture (ISA).<br/>"
        "• <b>Clock Cycles Per Instruction (CPI):</b> The average number of clock cycles required to execute an individual instruction. Governed by the processor micro-architecture, pipeline depth, and memory cache hit rates.<br/>"
        "• <b>Clock Cycle Time (T):</b> The duration of a single oscillating clock pulse generated by the quartz crystal oscillator. Clock cycle time is the mathematical reciprocal of clock frequency: <code>T = 1 / f</code>.<br/>"
        "The total CPU execution time is given by:",
        styles['DocBody']
    ))
    story.append(create_code_box(
        "CPU_Time = Instruction_Count * CPI * Clock_Cycle_Time\n"
        "CPU_Time = (Instruction_Count * CPI) / Clock_Frequency\n"
        "\n"
        "Instructions_Per_Cycle (IPC) = 1 / CPI\n"
        "MIPS = Clock_Frequency / (CPI * 10^6) = Instruction_Count / (CPU_Time * 10^6)",
        caption="Mathematical CPU Execution Time and Throughput Equations"
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>6.2 The Power Wall and Dennard Scaling Breakdown</b><br/>"
        "From 1974 to the mid-2000s, <b>Dennard Scaling</b> observed that as transistor dimensions shrunk by factor <code>k</code>, power density remained constant because operational voltage could be reduced proportionally. "
        "This allowed CPU designers to increase clock frequencies dramatically (from 4.77 MHz in the 1981 IBM PC to 3.8 GHz in 2004). "
        "However, around 2005, Dennard scaling collapsed due to quantum tunneling leakage current: operational voltage could not be dropped below ~1.0V without causing signal instability. "
        "The dynamic power consumption of a CMOS digital circuit is modeled by:",
        styles['DocBody']
    ))
    story.append(create_code_box(
        "Power_Dynamic = Capacitive_Load * (Voltage^2) * Clock_Frequency\n"
        "P = C * V^2 * f",
        caption="CMOS Dynamic Power Dissipation Formula"
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Because power scales linearly with frequency and quadratically with voltage, pushing clock speeds past 4 GHz resulted in unsustainable thermal dissipation (the <b>Power Wall</b>), where microchips generated more heat per unit area than a nuclear reactor core. "
        "Consequently, the semiconductor industry shifted the entire paradigm from scaling clock frequency to <b>multi-core parallelism</b>: placing 2, 4, 8, 16, or more energy-efficient processor cores on a single silicon die running at conservative clock rates.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>6.3 Amdahl's Law and Theoretical Parallel Limits</b><br/>"
        "While multi-core processors solved the Power Wall, they exposed the fundamental limit of parallel software scaling, articulated by computer architect Gene Amdahl in 1967. "
        "<b>Amdahl's Law</b> calculates the theoretical maximum speedup <code>S</code> of a computer program when executed across <code>N</code> parallel processor cores:",
        styles['DocBody']
    ))
    story.append(create_code_box(
        "Speedup S(N) = 1 / [ (1 - p) + (p / N) ]\n"
        "\n"
        "Where:\n"
        "  p = Proportion of the program execution time that can be perfectly parallelized (0 <= p <= 1)\n"
        "  (1 - p) = Inherently sequential (serial) fraction of the program\n"
        "  N = Number of parallel processing cores / execution units\n"
        "\n"
        "Asymptotic Limit (as N -> infinity):\n"
        "  S_max = 1 / (1 - p)",
        caption="Amdahl's Law Speedup Formulation"
    ))
    story.append(Spacer(1, 6))

    # Worked Example 1.1: Amdahl's Law
    story.append(create_example_box(
        "Amdahl's Law Speedup in Crop Yield Simulation",
        "A crop disease simulation program running at the SUA Department of Informatics currently takes 100 seconds to execute on a single CPU core. "
        "Profiling reveals that 80% of the runtime (80 seconds) consists of an image matrix filter that can be parallelized across multiple cores, while the remaining 20% (20 seconds) consists of sequential file I/O operations.<br/>"
        "1. Calculate the theoretical speedup and execution time on a quad-core (4-core) CPU.<br/>"
        "2. Calculate the theoretical speedup on an 8-core CPU.<br/>"
        "3. Calculate the absolute maximum speedup achievable even if an infinite number of CPU cores (N → ∞) are deployed.",
        "<b>Step-by-Step Derivation:</b><br/>"
        "Given: Parallelizable fraction <code>p = 0.80</code>; Sequential fraction <code>(1 - p) = 0.20</code>.<br/>"
        "<b>1. For N = 4 cores:</b><br/>"
        "   <code>S(4) = 1 / [ 0.20 + (0.80 / 4) ] = 1 / [ 0.20 + 0.20 ] = 1 / 0.40 = 2.50x</code>.<br/>"
        "   Execution Time = 100s / 2.50 = <b>40.0 seconds</b>.<br/>"
        "<b>2. For N = 8 cores:</b><br/>"
        "   <code>S(8) = 1 / [ 0.20 + (0.80 / 8) ] = 1 / [ 0.20 + 0.10 ] = 1 / 0.30 = 3.33x</code>.<br/>"
        "   Execution Time = 100s / 3.33 = <b>30.0 seconds</b>.<br/>"
        "<b>3. Asymptotic Limit (N → ∞):</b><br/>"
        "   <code>S_max = 1 / (1 - p) = 1 / 0.20 = 5.00x</code>.<br/>"
        "   Minimum Execution Time = 100s / 5.00 = <b>20.0 seconds</b>.<br/>"
        "<b>Architectural Insight:</b> Regardless of whether the university invests in an 8-core, 64-core, or 10,000-core supercomputer, the simulation program can NEVER execute in less than 20 seconds unless the sequential I/O algorithm itself is re-engineered!"
    ))
    story.append(Spacer(1, 8))

    # Worked Example 1.2: CPU Time & MIPS
    story.append(create_example_box(
        "CPU Execution Time and Compiler Optimization",
        "A benchmark remote sensing program at SUA executes 2.0 × 10<sup>10</sup> machine instructions on a 3.2 GHz workstation processor with an average CPI of 1.4.<br/>"
        "(a) Calculate the total CPU execution time in seconds.<br/>"
        "(b) Calculate the processor's effective MIPS rating.<br/>"
        "(c) A new optimizing compiler reduces instruction count by 25% but increases average CPI to 1.5 due to additional memory loads. Determine the new CPU execution time and percentage performance improvement.",
        "<b>Solution:</b><br/>"
        "(a) <code>CPU_Time = (Instruction_Count * CPI) / Clock_Frequency</code><br/>"
        "    <code>CPU_Time = (2.0 * 10^10 * 1.4) / (3.2 * 10^9) = 2.8 * 10^10 / 3.2 * 10^9 = 8.75 seconds</code>.<br/>"
        "(b) <code>MIPS = Clock_Frequency / (CPI * 10^6) = (3.2 * 10^9) / (1.4 * 10^6) = 2,285.71 MIPS</code>.<br/>"
        "(c) New Instruction Count = <code>2.0 * 10^10 * (1 - 0.25) = 1.5 * 10^10</code> instructions.<br/>"
        "    New CPI = <code>1.5</code>.<br/>"
        "    <code>New_CPU_Time = (1.5 * 10^10 * 1.5) / (3.2 * 10^9) = 2.25 * 10^10 / 3.2 * 10^9 = 7.03125 seconds</code>.<br/>"
        "    <code>Speedup = 8.75 / 7.03125 = 1.244 (24.4% faster)</code>."
    ))
    story.append(Spacer(1, 8))

    # =========================================================
    # SECTION 7: TERMINAL DIAGNOSTICS & SYSTEM BENCHMARKING
    # =========================================================
    story.append(Paragraph("7. TERMINAL HARDWARE DIAGNOSTICS & TELEMETRY", styles['SecH1']))
    story.append(Paragraph(
        "Modern informatics professionals must possess practical command-line fluency to inspect microcomputer hardware, verify processor topologies, examine memory hierarchies, and diagnose system bus bottlenecks. "
        "In enterprise server and research environments running GNU/Linux, terminal utilities query kernel pseudo-filesystems (<code>/proc</code> and <code>/sys</code>) directly.",
        styles['DocBody']
    ))
    story.append(create_code_box(
        "# 1. Display CPU architecture, cache sizes, and hardware virtualization flags\n"
        "$ lscpu\n"
        "\n"
        "# 2. Inspect physical memory capacity, allocated swap, and available RAM in human-readable units\n"
        "$ free -h\n"
        "\n"
        "# 3. Enumerate block storage devices, partitions, mount points, and drive models\n"
        "$ lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT,MODEL\n"
        "\n"
        "# 4. Query PCI and PCIe expansion bus controllers (GPU, NVMe, Network)\n"
        "$ lspci -tv\n"
        "\n"
        "# 5. Display motherboard BIOS/UEFI firmware metadata via DMI table decoder (requires root)\n"
        "$ sudo dmidecode -t bios -t baseboard",
        caption="Essential Linux Terminal Commands for Hardware Auditing"
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>Interpreting <code>lscpu</code> Output:</b><br/>"
        "When auditing a server in the SUA computer lab, <code>lscpu</code> reports:<br/>"
        "• <code>Thread(s) per core: 2</code>: Indicates Simultaneous Multithreading (Intel Hyper-Threading), where each physical core presents two logical execution contexts to the OS scheduler.<br/>"
        "• <code>Core(s) per socket: 8</code> and <code>Socket(s): 1</code>: Total physical cores = <code>8 * 1 = 8</code>. Total logical processors = <code>8 * 2 = 16</code>.<br/>"
        "• <code>L1d cache: 256 KiB</code> (8 instances of 32 KiB dedicated data cache per core).<br/>"
        "• <code>L3 cache: 16 MiB</code>: Unified cache shared dynamically across all 8 cores on the silicon die.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 8))

    # =========================================================
    # SECTION 8: CASE STUDY - SMART AGRICULTURE AT SUA
    # =========================================================
    story.append(Paragraph("8. APPLIED CASE STUDY: MICROCOMPUTERS IN SMART AGRICULTURE", styles['SecH1']))
    story.append(Paragraph(
        "At Sokoine University of Agriculture, microcomputer systems are deployed across field stations to transform traditional agrarian practices into data-driven precision farming. "
        "Consider the automated microclimate and irrigation telemetry network deployed at the SUA Mazimbu Experimental Farm:",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "• <b>Tier 1 - Field Embedded Microcontrollers:</b> Battery/solar-powered ESP32 and ARM Cortex-M microcontrollers deployed across 12 field sectors. Each node reads capacitive soil moisture sensors and digital thermistors via an I2C bus. Nodes spend 98% of their lifecycle in microampere deep-sleep mode, waking every 15 minutes to take readings, package telemetry into compact binary packets, and broadcast them over LoRaWAN (868 MHz) across a 5 km radius.<br/>"
        "• <b>Tier 2 - Edge Microcomputer Gateway:</b> A ruggedized single-board microcomputer (Raspberry Pi 4B) located at the farm manager's office receives LoRaWAN packets, validates payload checksums, and logs readings to a local SQLite database. If soil matric potential drops below -35 kPa, the gateway's GPIO pins actuate a solid-state relay, opening the 24V solenoid valve on the drip irrigation mainline.<br/>"
        "• <b>Tier 3 - Central Enterprise Server:</b> The gateway relays aggregated hourly datasets via a 4G cellular modem to the central MySQL server at the DIIT server room. Department researchers run Python automated scripts using Pandas and Matplotlib to model soil water depletion curves, dispatching automated SMS advisory bulletins to Morogoro smallholder farmers.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 9: LABORATORY PRACTICAL WORKSHOP & SIMULATION
    # =========================================================
    story.append(Paragraph("9. LABORATORY PRACTICAL WORKSHOP & PERFORMANCE PROFILING", styles['SecH1']))
    story.append(Paragraph(
        "This laboratory section provides undergraduate students with practical exercises in hardware profiling, CPU performance benchmarking, and parallel scalability modeling. "
        "All exercises are executed using standard GNU/Linux terminal tools and Python.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Lab Exercise 1.1: Auditing Hardware Micro-Architecture via Terminal</b><br/>"
        "Objective: Interrogate system pseudo-filesystems to extract hardware topologies.<br/>"
        "1. Open the bash shell and view the raw processor descriptor file:<br/>"
        "   <code>cat /proc/cpuinfo | grep 'model name' | head -n 1</code><br/>"
        "2. Determine physical core count versus logical thread count:<br/>"
        "   <code>echo \"Physical Sockets: $(grep 'physical id' /proc/cpuinfo | sort -u | wc -l)\"</code><br/>"
        "   <code>echo \"Physical Cores: $(grep 'cpu cores' /proc/cpuinfo | head -n 1 | awk '{print $4}')\"</code><br/>"
        "   <code>echo \"Logical Processors: $(grep -c 'processor' /proc/cpuinfo)\"</code><br/>"
        "3. Inspect hardware cache line sizes and cache associativity:<br/>"
        "   <code>cat /sys/devices/system/cpu/cpu0/cache/index0/size</code> (L1 Data Cache size)<br/>"
        "   <code>cat /sys/devices/system/cpu/cpu0/cache/index0/coherency_line_size</code> (Standard 64-byte cache line)<br/>"
        "4. Enumerate PCI Express lanes and peripheral bus bandwidth:<br/>"
        "   <code>sudo lspci -vv -s $(lspci | grep -i 'vga\\|3d' | awk '{print $1}') | grep -i 'LnkCap'</code>",
        styles['DocBody']
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<b>Lab Exercise 1.2: CPU Computational Benchmarking with Sysbench</b><br/>"
        "Objective: Measure raw CPU prime-number calculation performance across single-thread and multi-thread configurations to empirically verify Amdahl's Law.<br/>"
        "1. Execute single-threaded prime number computation up to 20,000:<br/>"
        "   <code>sysbench cpu --cpu-max-prime=20000 --threads=1 run</code><br/>"
        "   Record the execution time <code>T_1</code> and total events processed per second.<br/>"
        "2. Execute the identical workload across 2, 4, and 8 parallel threads:<br/>"
        "   <code>sysbench cpu --cpu-max-prime=20000 --threads=2 run</code><br/>"
        "   <code>sysbench cpu --cpu-max-prime=20000 --threads=4 run</code><br/>"
        "   <code>sysbench cpu --cpu-max-prime=20000 --threads=8 run</code><br/>"
        "3. Tabulate the empirical speedup <code>S(N) = T_1 / T_N</code> and compare against theoretical linear scaling.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<b>Lab Exercise 1.3: Python Amdahl's Law Numerical Simulator</b><br/>"
        "Students are required to execute the following Python simulation script to model parallel scalability curves across varying parallel proportions (p = 0.50, 0.75, 0.90, 0.99):",
        styles['DocBody']
    ))
    story.append(create_code_box(
        "import numpy as np\n"
        "\n"
        "def amdahl_speedup(p, cores):\n"
        "    \"\"\"Calculates Amdahl's Law theoretical speedup.\"\"\"\n"
        "    return 1.0 / ((1.0 - p) + (p / cores))\n"
        "\n"
        "cores_array = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])\n"
        "parallel_fractions = [0.50, 0.75, 0.90, 0.95, 0.99]\n"
        "\n"
        "print(f\"{'Cores':>6} | \" + \" | \".join([f\"p={p:.2f}\" for p in parallel_fractions]))\n"
        "print(\"-\" * 55)\n"
        "for c in cores_array:\n"
        "    row = [f\"{amdahl_speedup(p, c):7.2f}x\" for p in parallel_fractions]\n"
        "    print(f\"{c:6d} | \" + \" | \".join(row))\n"
        "\n"
        "# Asymptotic limits:\n"
        "print(\"-\" * 55)\n"
        "limit_row = [f\"{1.0/(1.0-p):7.2f}x\" for p in parallel_fractions]\n"
        "print(f\"{'Limit':>6} | \" + \" | \".join(limit_row))",
        caption="Python Simulation: Amdahl's Law Scalability Across Cores and Parallel Fractions"
    ))
    story.append(Spacer(1, 8))

    # =========================================================
    # SECTION 10: TOPIC 1 COMPREHENSIVE SELF-ASSESSMENT
    # =========================================================
    story.append(Paragraph("10. COMPREHENSIVE TOPIC 1 SELF-ASSESSMENT QUESTIONS", styles['SecH1']))
    story.append(Paragraph(
        "The following 40 questions evaluate your mastery of Topic 1 across theoretical foundations, quantitative derivations, system comparisons, and practical agricultural designs. "
        "Complete step-by-step solutions are provided in Section 11.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 4))

    # Questions 1-15: Multiple Choice / Objective
    story.append(Paragraph("<b>Part A: Multiple Choice and Conceptual Review (Questions 1 to 15)</b>", styles['SecH2']))
    q_mc = [
        "1. Which active electronic component characterized First-Generation computing machinery? (A) Transistors (B) Vacuum Tubes (C) Integrated Circuits (D) Microprocessors.",
        "2. The primary technological reason why magnetic ferrite core memory displaced acoustic delay lines was: (A) Lower manufacturing cost (B) Complete non-volatility and random-access capability (C) Smaller electrical voltage requirements (D) Optical transmission speed.",
        "3. Charles Babbage's Analytical Engine incorporated a memory component known as the: (A) Mill (B) Accumulator (C) Store (D) Drum.",
        "4. Augusta Ada Lovelace is recognized in computer history for: (A) Inventing the vacuum tube (B) Authoring Note G containing the first published computer algorithm (C) Designing the ENIAC (D) Founding IBM.",
        "5. The fundamental innovation of the Stored-Program Concept formulated by John von Neumann is: (A) Storing data exclusively on magnetic tape (B) Storing both instructions and data in the same unified addressable memory space (C) Completely eliminating CPU registers (D) Separating program code onto read-only optical disks.",
        "6. In the Information Processing Cycle (IPOS), the conversion of raw sensor voltage into digital units by an ADC belongs to which phase? (A) Processing (B) Output (C) Storage (D) Input.",
        "7. A computing system that processes continuous physical phenomena directly without binary quantization is classified as: (A) A Digital Computer (B) An Analog Computer (C) A Hybrid Computer (D) An Embedded Microcomputer.",
        "8. Mainframe computers prioritize which architectural characteristic above all others? (A) Maximum Peak Floating-Point FLOPS (B) Reliability, Availability, and Serviceability (RAS) with massive I/O throughput (C) Minimum physical form factor (D) Direct battery-powered field operation.",
        "9. Herman Hollerith's tabulating machine automated the 1890 US Census utilizing what medium? (A) Magnetic tape (B) Punched cards (C) Williams tubes (D) Paper magnetic disks.",
        "10. Which computer pioneer proved the mathematical limits of mechanical computation through the Universal Turing Machine? (A) John Mauchly (B) Alan Turing (C) Gordon Moore (D) Jack Kilby.",
        "11. Moore's Law empirically predicts that: (A) Processor clock speed doubles every 6 months (B) Transistor density on microchips doubles roughly every 18 to 24 months (C) Hard drive capacity quadruples annually (D) Computer software execution time halves each year.",
        "12. The physical constraint where high clock frequencies cause excessive dynamic power dissipation and overheating is known as: (A) The Memory Wall (B) The Power Wall (C) The Von Neumann Bottleneck (D) Belady's Anomaly.",
        "13. In Amdahl's Law, if 100% of a program's execution time is strictly sequential (p = 0), what is the maximum achievable speedup on an 8-core CPU? (A) 8.0x (B) 4.0x (C) 1.0x (No speedup) (D) 0.5x.",
        "14. What is the total number of physical memory bytes addressable by a 32-bit address bus in a byte-addressable microcomputer? (A) 2 GiB (B) 4 GiB (C) 8 GiB (D) 16 GiB.",
        "15. An enterprise server running Linux has 2 physical CPU sockets, each housing an 8-core processor with 2 threads per core. How many logical CPUs does the kernel scheduler see? (A) 16 (B) 24 (C) 32 (D) 64."
    ]
    for q in q_mc:
        story.append(Paragraph(q, styles['DocBody']))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 6))
    # Questions 16-25: Quantitative
    story.append(Paragraph("<b>Part B: Quantitative Calculations and Performance Modeling (Questions 16 to 25)</b>", styles['SecH2']))
    q_quant = [
        "16. A workstation at the SUA Remote Sensing Laboratory executes an agricultural classification algorithm requiring 3.6 × 10<sup>10</sup> machine instructions. The processor operates at a clock frequency of 3.0 GHz with an average CPI of 1.25. Calculate the total CPU execution time in seconds.",
        "17. For the workstation in Question 16, compute the effective MIPS (Million Instructions Per Second) rating of the processor under this workload.",
        "18. A crop simulation program takes 120 seconds to execute on a single core. Profiling reveals that 75% of the execution time can be parallelized across multi-core processors, while the remaining 25% consists of strictly serial database writing. Using Amdahl's Law, calculate the theoretical speedup and new execution time on a 6-core processor.",
        "19. For the simulation program in Question 18, calculate the theoretical asymptotic maximum speedup possible on an infinite number of processor cores (N → ∞).",
        "20. A CMOS microcomputer processor operates at an internal voltage of 1.2V and a clock frequency of 2.5 GHz, drawing 45W of dynamic power. If the operational voltage is reduced by 15% (to 1.02V) while the clock frequency is increased to 3.0 GHz, calculate the new dynamic power consumption assuming capacitive load remains constant.",
        "21. A microprocessor features a 36-bit physical address bus. If each unique address references an individual 8-bit byte, calculate the maximum physical RAM capacity supported by the hardware in exact Gibibytes (GiB).",
        "22. A high-performance computing cluster node features a dual-channel memory bus operating at 3,200 MT/s (MegaTransfers per second). If each memory channel is 64 bits wide, calculate the theoretical peak memory bus bandwidth in Gigabytes per second (GB/s).",
        "23. An image processing loop on a 4.0 GHz CPU consists of 4.8 × 10<sup>9</sup> instructions. If 60% of the instructions take 1 cycle, 30% take 2 cycles, and 10% take 5 cycles, calculate: (a) The average CPI, and (b) The total CPU runtime in seconds.",
        "24. A system architect at SUA is deciding between Processor X (Clock = 4.0 GHz, Average CPI = 1.6) and Processor Y (Clock = 3.2 GHz, Average CPI = 1.1) to run an identical compiled binary. Determine which processor is faster and calculate the percentage performance difference.",
        "25. A parallel genomics program achieves a speedup of 3.2x when executed on a 4-core machine. Using Amdahl's Law, determine the parallel fraction <code>p</code> of the codebase."
    ]
    for q in q_quant:
        story.append(Paragraph(q, styles['DocBody']))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 6))
    # Questions 26-35: Analytical / Essay
    story.append(Paragraph("<b>Part C: Comparative and Theoretical Analysis (Questions 26 to 35)</b>", styles['SecH2']))
    q_essay = [
        "26. Explain the technical differences between First-Generation vacuum tubes and Second-Generation transistors regarding switching physics, power requirements, heat dissipation, and MTBF.",
        "27. Detail the mechanical architecture of Charles Babbage's Analytical Engine, describing the specific functional roles of the 'Store' and the 'Mill'.",
        "28. What constitutes the 'Von Neumann Bottleneck' in contemporary microcomputer design? Detail three specific hardware techniques implemented in modern CPUs to mitigate its performance impact.",
        "29. Contrast the fundamental architectural design goals of Enterprise Mainframes with High-Performance Supercomputers. Why do banks in Tanzania rely on mainframes rather than supercomputers for processing mobile banking transactions?",
        "30. Differentiate between Analog and Digital computing systems across signal representation, mathematical precision, execution parallelism, and environmental noise sensitivity.",
        "31. Explain why Gordon Moore's empirical observation (Moore's Law) drove exponential economic and technical growth across the global electronics industry for five decades.",
        "32. Define an Embedded Computer. Explain how the hardware architecture and operational constraints of a microcontroller unit (MCU) differ from a general-purpose desktop microcomputer.",
        "33. Trace the evolution of primary internal memory from acoustic mercury delay lines and magnetic ferrite core to modern semiconductor dynamic RAM (DRAM).",
        "34. Explain the concept of the 'Megahertz Myth'. Why is comparing clock frequencies across different processor microarchitectures fundamentally misleading?",
        "35. Describe the historical significance of the Intel 4004 microprocessor and explain how it initiated the Fourth Generation of computing."
    ]
    for q in q_essay:
        story.append(Paragraph(q, styles['DocBody']))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 6))
    # Questions 36-40: Applied Scenarios
    story.append(Paragraph("<b>Part D: Applied Enterprise and Agricultural Engineering Scenarios (Questions 36 to 40)</b>", styles['SecH2']))
    q_applied = [
        "36. The SUA Department of Crop Science intends to establish an automated drone photogrammetry station to process high-resolution multispectral crop imagery. Formulate a comprehensive hardware specification for an engineering workstation, detailing CPU class, ECC RAM capacity, GPU requirements, storage configuration, and power supply.",
        "37. Design an autonomous environmental telemetry and irrigation control unit for an outlying experimental vineyard in Kilosa. Specify the computing class, sensor interfaces (analog vs digital), power subsystem, and communication protocol.",
        "38. A systems technician at the SUA Solomon Mahlangu Campus (SMC) computer laboratory is auditing desktop workstations running Ubuntu Linux. Provide the exact terminal commands required to display: (a) CPU model and cache sizes, (b) Total and available RAM, (c) Block storage devices and partition layout, and (d) Motherboard BIOS firmware version.",
        "39. Contrast the operational paradigms of Client-Server and Peer-to-Peer network architectures in the context of distributing 50 GB satellite weather datasets to 200 undergraduate student laptops at SUA.",
        "40. Explain how a hybrid computing architecture could be engineered to control precision variable-rate pesticide spraying on an autonomous farm tractor, differentiating the roles of the analog sensor circuitry and digital microcomputer."
    ]
    for q in q_applied:
        story.append(Paragraph(q, styles['DocBody']))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 10))

    # =========================================================
    # SECTION 11: COMPLETE STEP-BY-STEP SOLUTIONS
    # =========================================================
    story.append(Paragraph("11. EXHAUSTIVE SOLUTIONS AND MARKING SCHEME FOR QUESTIONS 1 TO 40", styles['SecH1']))
    story.append(Paragraph(
        "This section provides rigorous, step-by-step academic solutions, mathematical proofs, architectural justifications, full distractor rationales, and marking guidelines for all 40 self-assessment questions.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 4))

    # Solutions Part A
    story.append(Paragraph("<b>Solutions to Part A: Objective Questions with Comprehensive Distractor Rationale (1 to 15)</b>", styles['SecH2']))
    sol_mc = [
        "<b>Question 1: Correct Answer is (B) — Vacuum Tubes.</b><br/>"
        "• <i>Correct Option Rationale:</i> First-generation computers (1940–1956) utilized thermionic vacuum tubes as their active electronic switching gates. In a vacuum tube, thermionic emission releases electrons from a heated cathode filament across a vacuum to an anode plate, gated by grid voltage.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [Transistors] is incorrect because discrete transistors were invented at Bell Labs in late 1947 and define the Second Generation (1956–1963).<br/>"
        "  - Option (C) [Integrated Circuits] is incorrect because ICs were invented in 1958/1959 and define the Third Generation (1964–1971).<br/>"
        "  - Option (D) [Microprocessors] is incorrect because microprocessors originated with the Intel 4004 in 1971 and define the Fourth Generation.",

        "<b>Question 2: Correct Answer is (B) — Complete non-volatility and random-access capability.</b><br/>"
        "• <i>Correct Option Rationale:</i> Magnetic ferrite core memory utilized tiny ferromagnetic ceramic toroids that maintained magnetic polarity indefinitely without electrical power (non-volatility) and allowed any address to be accessed in uniform time (~1 μs), eliminating mechanical or acoustic latency.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) is incorrect because early core memory was extremely labor-intensive, requiring manual weaving under microscopes, making it initially expensive.<br/>"
        "  - Option (C) is incorrect because core memory required relatively high coincident-current pulses to switch magnetic domains.<br/>"
        "  - Option (D) is incorrect because core memory relies entirely on electromagnetic flux switching, not optical photons.",

        "<b>Question 3: Correct Answer is (C) — The Store.</b><br/>"
        "• <i>Correct Option Rationale:</i> In Charles Babbage's Analytical Engine (1837), the memory unit holding stored numbers was termed the <i>'Store'</i> (capable of holding 1,000 numbers of 50 decimal digits each), while the calculating engine executing arithmetic was termed the <i>'Mill'</i>.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [The Mill] is incorrect because the Mill was the processing unit (analogous to the CPU/ALU), not memory.<br/>"
        "  - Option (B) [Accumulator] is incorrect because the accumulator is a specific internal register in electronic CPUs.<br/>"
        "  - Option (D) [Drum] is incorrect because magnetic drums were first-generation electronic memory devices developed in the 1940s.",

        "<b>Question 4: Correct Answer is (B) — Authoring Note G containing the first published computer algorithm.</b><br/>"
        "• <i>Correct Option Rationale:</i> Augusta Ada Lovelace appended extensive annotations to Menabrea's paper on the Analytical Engine; Note G contained the algorithm for computing Bernoulli numbers, universally recognized as the world's first computer program.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) is incorrect because the thermionic vacuum tube was invented by John Ambrose Fleming (diode, 1904) and Lee de Forest (triode, 1906).<br/>"
        "  - Option (C) is incorrect because ENIAC was designed by John Mauchly and J. Presper Eckert in the 1940s.<br/>"
        "  - Option (D) is incorrect because IBM was evolved from Herman Hollerith's Tabulating Machine Company.",

        "<b>Question 5: Correct Answer is (B) — Storing both instructions and data in the same unified addressable memory space.</b><br/>"
        "• <i>Correct Option Rationale:</i> The Stored-Program Concept dictates that operational machine instructions and operand data are stored together in the same addressable, read-write memory space, allowing dynamic program modification, dynamic loading, and eliminating manual hardware rewiring.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) is incorrect because magnetic tape is a sequential secondary storage medium, not the primary stored-program space.<br/>"
        "  - Option (C) is incorrect because Von Neumann processors rely heavily on internal CPU registers (PC, IR, MAR, MDR, Accumulator).<br/>"
        "  - Option (D) is incorrect because separating instructions into read-only memory describes the Harvard architecture, not the unified Von Neumann concept.",

        "<b>Question 6: Correct Answer is (D) — Input.</b><br/>"
        "• <i>Correct Option Rationale:</i> An Analog-to-Digital Converter (ADC) functions as an input transducer converting continuous external physical voltages into internal binary data words.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [Processing] is incorrect because processing refers to arithmetic or logical transformations carried out by the ALU after digital ingestion.<br/>"
        "  - Option (B) [Output] is incorrect because output delivers internal binary results to the external world (e.g., via a DAC or display).<br/>"
        "  - Option (C) [Storage] is incorrect because storage preserves data in non-volatile media.",

        "<b>Question 7: Correct Answer is (B) — An Analog Computer.</b><br/>"
        "• <i>Correct Option Rationale:</i> Analog computers represent and process continuous physical variables (voltage, mechanical rotation) without binary quantization.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [Digital Computer] is incorrect because digital computers operate exclusively on discrete binary states.<br/>"
        "  - Option (C) [Hybrid Computer] is incorrect because hybrid computers contain both analog and discrete digital subcomponents.<br/>"
        "  - Option (D) [Embedded Microcomputer] is incorrect because microcontrollers are digital processing engines.",

        "<b>Question 8: Correct Answer is (B) — Reliability, Availability, and Serviceability (RAS) with massive I/O throughput.</b><br/>"
        "• <i>Correct Option Rationale:</i> Enterprise mainframes are engineered specifically for Reliability, Availability, and Serviceability (RAS) and massive concurrent I/O channel throughput rather than raw floating-point peak speed.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [FLOPS] is incorrect because peak floating-point throughput is the design goal of supercomputers.<br/>"
        "  - Option (C) is incorrect because mainframes are massive multi-cabinet rack installations.<br/>"
        "  - Option (D) is incorrect because mainframes draw tens of kilowatts of multi-phase industrial AC power.",

        "<b>Question 9: Correct Answer is (B) — Punched cards.</b><br/>"
        "• <i>Correct Option Rationale:</i> Herman Hollerith utilized standardized 80-column punched paper cards sensed by electromechanical spring-loaded pins dipping into mercury cups to automate the 1890 US Census.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [Magnetic tape] is incorrect because magnetic tape was developed for audio in Germany in the 1930s and adapted for computers in 1951 on the UNIVAC I.<br/>"
        "  - Option (C) [Williams tubes] is incorrect because electrostatic CRT storage was developed in 1947.<br/>"
        "  - Option (D) [Paper magnetic disks] is incorrect because magnetic disks appeared with the IBM RAMAC in 1956.",

        "<b>Question 10: Correct Answer is (B) — Alan Turing.</b><br/>"
        "• <i>Correct Option Rationale:</i> Alan Turing formulated the Universal Turing Machine (UTM) in his 1936 paper, mathematically defining the theoretical limits of algorithmic computability.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [John Mauchly] is incorrect because Mauchly was an electrical engineer and co-designer of ENIAC/EDVAC.<br/>"
        "  - Option (C) [Gordon Moore] is incorrect because Moore is known for his empirical observation on semiconductor scaling.<br/>"
        "  - Option (D) [Jack Kilby] is incorrect because Kilby co-invented the integrated circuit.",

        "<b>Question 11: Correct Answer is (B) — Transistor density on microchips doubles roughly every 18 to 24 months.</b><br/>"
        "• <i>Correct Option Rationale:</i> Moore's Law observes that the number of transistors packed onto an integrated circuit doubles approximately every 18 to 24 months with falling per-transistor cost.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) is incorrect because clock speed scaling collapsed in the mid-2000s due to the Power Wall.<br/>"
        "  - Option (C) is incorrect because hard drive areal density scaling is governed by Kryder's Law.<br/>"
        "  - Option (D) is incorrect because software execution time does not automatically halve without parallel algorithm redesign.",

        "<b>Question 12: Correct Answer is (B) — The Power Wall.</b><br/>"
        "• <i>Correct Option Rationale:</i> The Power Wall refers to the physical threshold where excessive dynamic CMOS power dissipation (P = C · V<sup>2</sup> · f) prevents further clock frequency scaling due to cooling limits.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [The Memory Wall] refers to the increasing latency disparity between ultra-fast CPUs and slower DRAM.<br/>"
        "  - Option (C) [Von Neumann Bottleneck] refers to shared bus throughput limits between CPU and memory.<br/>"
        "  - Option (D) [Belady's Anomaly] refers to the FIFO page replacement anomaly where adding page frames increases page faults.",

        "<b>Question 13: Correct Answer is (C) — 1.0x (No speedup).</b><br/>"
        "• <i>Correct Option Rationale:</i> If a program is entirely sequential (p = 0), Amdahl's Law yields S = 1 / [(1 - 0) + 0/8] = 1 / 1 = 1.0x (zero performance speedup regardless of core count).<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [8.0x] would occur only if the code were 100% perfectly parallelizable (p = 1.0).<br/>"
        "  - Option (B) [4.0x] would occur if parallel fraction were p = 0.857.<br/>"
        "  - Option (D) [0.5x] would represent a 50% performance regression.",

        "<b>Question 14: Correct Answer is (B) — 4 GiB.</b><br/>"
        "• <i>Correct Option Rationale:</i> A 32-bit address bus can uniquely address 2<sup>32</sup> distinct bytes = 4,294,967,296 bytes = exactly 4.0 GiB.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [2 GiB] corresponds to a 31-bit address bus.<br/>"
        "  - Option (C) [8 GiB] corresponds to a 33-bit address bus.<br/>"
        "  - Option (D) [16 GiB] corresponds to a 34-bit address bus.",

        "<b>Question 15: Correct Answer is (C) — 32.</b><br/>"
        "• <i>Correct Option Rationale:</i> Total logical processors = (2 sockets) × (8 cores per socket) × (2 threads per core) = 32 logical execution threads.<br/>"
        "• <i>Distractor Analysis:</i><br/>"
        "  - Option (A) [16] is the total physical core count without hyper-threading.<br/>"
        "  - Option (B) [24] is an arithmetic error.<br/>"
        "  - Option (D) [64] would occur if there were 4 sockets or 4 threads per core."
    ]
    for s in sol_mc:
        story.append(Paragraph(s, styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 6))
    # Solutions Part B
    story.append(Paragraph("<b>Solutions to Part B: Quantitative Problems with Complete Algebraic Proofs (16 to 25)</b>", styles['SecH2']))
    
    sol_quant = [
        "<b>Question 16 Solution:</b><br/>"
        "• <i>Underlying Formula:</i> <code>CPU_Time = (Instruction_Count * CPI) / Clock_Frequency</code><br/>"
        "• <i>Variable Declarations:</i><br/>"
        "  - Instruction Count (IC) = 3.6 × 10<sup>10</sup> instructions<br/>"
        "  - Average Cycles Per Instruction (CPI) = 1.25 clock cycles/instruction<br/>"
        "  - Clock Frequency (f) = 3.0 GHz = 3.0 × 10<sup>9</sup> cycles/second<br/>"
        "• <i>Step 1: Calculate Total Clock Cycles:</i><br/>"
        "  <code>Total Cycles = IC * CPI = (3.6 * 10^10 instructions) * (1.25 cycles/instruction) = 4.5 * 10^10 cycles</code>.<br/>"
        "• <i>Step 2: Calculate CPU Execution Time:</i><br/>"
        "  <code>CPU_Time = (4.5 * 10^10 cycles) / (3.0 * 10^9 cycles/second) = 15.0 seconds</code>.<br/>"
        "• <b>Final Answer:</b> Total CPU execution time is <b>15.0 seconds</b>.",

        "<b>Question 17 Solution:</b><br/>"
        "• <i>Underlying Formula:</i> <code>MIPS = Clock_Frequency / (CPI * 10^6)</code> OR <code>MIPS = Instruction_Count / (CPU_Time * 10^6)</code><br/>"
        "• <i>Evaluation via Method 1 (Clock Rate & CPI):</i><br/>"
        "  <code>MIPS = (3.0 * 10^9 cycles/s) / (1.25 cycles/instr * 10^6) = 3,000 / 1.25 = 2,400 MIPS</code>.<br/>"
        "• <i>Evaluation via Method 2 (Instruction Count & CPU Time):</i><br/>"
        "  <code>MIPS = (3.6 * 10^10 instructions) / (15.0 seconds * 10^6) = 36,000 / 15.0 = 2,400 MIPS</code>.<br/>"
        "• <b>Final Answer:</b> The effective processor throughput is <b>2,400 MIPS</b>.",

        "<b>Question 18 Solution:</b><br/>"
        "• <i>Underlying Formula:</i> Amdahl's Law <code>Speedup S(N) = 1 / [ (1 - p) + (p / N) ]</code><br/>"
        "• <i>Variable Declarations:</i><br/>"
        "  - Baseline single-core execution time <code>T_1 = 120 seconds</code>.<br/>"
        "  - Parallelizable fraction <code>p = 0.75</code>.<br/>"
        "  - Serial fraction <code>(1 - p) = 0.25</code>.<br/>"
        "  - Core count <code>N = 6</code>.<br/>"
        "• <i>Step 1: Compute Speedup Factor:</i><br/>"
        "  <code>S(6) = 1 / [ 0.25 + (0.75 / 6) ] = 1 / [ 0.25 + 0.125 ] = 1 / 0.375 = 2.6667x</code>.<br/>"
        "• <i>Step 2: Compute New Execution Time:</i><br/>"
        "  <code>T(6) = T_1 / S(6) = 120s / 2.6667 = 45.0 seconds</code>.<br/>"
        "  (Verification: Serial Time = 120 * 0.25 = 30s. Parallel Time on 6 cores = (120 * 0.75) / 6 = 90 / 6 = 15s. Total = 30 + 15 = 45.0s).<br/>"
        "• <b>Final Answer:</b> Theoretical speedup is <b>2.67x</b>; new execution time is <b>45.0 seconds</b>.",

        "<b>Question 19 Solution:</b><br/>"
        "• <i>Underlying Formula:</i> Asymptotic Amdahl Limit as <code>N → ∞</code>: <code>S_max = 1 / (1 - p)</code><br/>"
        "• <i>Calculation:</i><br/>"
        "  Given sequential fraction <code>(1 - p) = 0.25</code>.<br/>"
        "  <code>S_max = 1 / 0.25 = 4.00x</code>.<br/>"
        "• <i>Minimum Execution Time:</i><br/>"
        "  <code>T_min = T_1 / S_max = 120s / 4.0 = 30.0 seconds</code>.<br/>"
        "• <b>Final Answer:</b> The theoretical maximum speedup on an infinite number of cores is strictly bounded at <b>4.00x</b>, and the runtime cannot drop below <b>30.0 seconds</b>.",

        "<b>Question 20 Solution:</b><br/>"
        "• <i>Underlying Formula:</i> CMOS Dynamic Power <code>P = C * V^2 * f</code><br/>"
        "• <i>Baseline State:</i> <code>P_1 = C * (V_1)^2 * f_1 = 45 W</code>, where <code>V_1 = 1.2V</code>, <code>f_1 = 2.5 GHz</code>.<br/>"
        "• <i>New State:</i> Voltage reduced by 15% → <code>V_2 = 1.2 * (1 - 0.15) = 1.02V</code>. Frequency increased → <code>f_2 = 3.0 GHz</code>.<br/>"
        "• <i>Ratio Derivation:</i><br/>"
        "  <code>P_2 / P_1 = [ C * (V_2)^2 * f_2 ] / [ C * (V_1)^2 * f_1 ] = (V_2 / V_1)^2 * (f_2 / f_1)</code><br/>"
        "  <code>(V_2 / V_1) = 1.02 / 1.2 = 0.85</code>. Therefore, <code>(V_2 / V_1)^2 = (0.85)^2 = 0.7225</code>.<br/>"
        "  <code>(f_2 / f_1) = 3.0 / 2.5 = 1.20</code>.<br/>"
        "  <code>P_2 = 45 W * 0.7225 * 1.20 = 45 * 0.8670 = 39.015 Watts</code>.<br/>"
        "• <b>Final Answer:</b> New dynamic power dissipation is <b>39.02 Watts</b> (a net power reduction of 13.3% despite a 20% frequency increase!).",

        "<b>Question 21 Solution:</b><br/>"
        "• <i>Underlying Formula:</i> Total Addressable Bytes = 2<sup>n</sup> bytes, where <code>n</code> is address bus width.<br/>"
        "• <i>Given:</i> <code>n = 36 bits</code>.<br/>"
        "  <code>Total Bytes = 2^36 bytes</code>.<br/>"
        "• <i>Conversion to Binary Gibibytes (GiB):</i><br/>"
        "  <code>1 GiB = 2^30 bytes</code>.<br/>"
        "  <code>Capacity = 2^36 / 2^30 = 2^(36 - 30) = 2^6 = 64 GiB</code>.<br/>"
        "• <b>Final Answer:</b> The processor hardware can directly address a maximum physical RAM capacity of <b>64 GiB</b>.",

        "<b>Question 22 Solution:</b><br/>"
        "• <i>Underlying Formula:</i> <code>Bandwidth (GB/s) = (Transfer_Rate * Total_Data_Bus_Width_in_Bytes) / 10^9</code><br/>"
        "• <i>Given:</i><br/>"
        "  - Transfer Rate = 3,200 MT/s = 3.2 × 10<sup>9</sup> transfers/second.<br/>"
        "  - Dual-Channel configuration with 64 bits per channel → Total Data Bus Width = 2 × 64 = 128 bits = 16 bytes.<br/>"
        "• <i>Calculation:</i><br/>"
        "  <code>Bandwidth = (3.2 * 10^9 transfers/s * 16 bytes/transfer) = 51.2 * 10^9 bytes/s = 51.2 GB/s</code>.<br/>"
        "• <b>Final Answer:</b> Theoretical peak memory bus bandwidth is <b>51.2 GB/s</b>.",

        "<b>Question 23 Solution:</b><br/>"
        "• <i>Part (a): Average CPI Calculation:</i><br/>"
        "  <code>Average CPI = ∑ (Frequency_i * Cycles_i) = (0.60 * 1) + (0.30 * 2) + (0.10 * 5) = 0.60 + 0.60 + 0.50 = 1.70</code>.<br/>"
        "• <i>Part (b): Total CPU Execution Time:</i><br/>"
        "  <code>Total Clock Cycles = IC * CPI = (4.8 * 10^9 instructions) * 1.70 cycles/instr = 8.16 * 10^9 cycles</code>.<br/>"
        "  <code>CPU_Time = Total Cycles / Clock_Frequency = (8.16 * 10^9 cycles) / (4.0 * 10^9 cycles/second) = 2.04 seconds</code>.<br/>"
        "• <b>Final Answer:</b> Average CPI is <b>1.70</b>; total CPU execution time is <b>2.04 seconds</b>.",

        "<b>Question 24 Solution:</b><br/>"
        "• <i>Underlying Equation:</i> <code>CPU_Time = (IC * CPI) / Clock_Frequency</code><br/>"
        "• <i>Processor X Evaluation:</i><br/>"
        "  <code>Time_X = (IC * 1.6) / (4.0 * 10^9) = 0.40 * 10^-9 * IC seconds</code>.<br/>"
        "• <i>Processor Y Evaluation:</i><br/>"
        "  <code>Time_Y = (IC * 1.1) / (3.2 * 10^9) = 0.34375 * 10^-9 * IC seconds</code>.<br/>"
        "• <i>Comparison & Speedup:</i><br/>"
        "  Because <code>Time_Y < Time_X</code>, <b>Processor Y is faster</b>.<br/>"
        "  <code>Speedup = Time_X / Time_Y = 0.40 / 0.34375 = 1.1636 (16.36% faster)</code>.<br/>"
        "• <b>Final Answer:</b> <b>Processor Y is 16.36% faster</b> than Processor X. This is a classic demonstration of the 'Megahertz Myth' — higher IPC (lower CPI) outweighs raw clock frequency.",

        "<b>Question 25 Solution:</b><br/>"
        "• <i>Underlying Formula:</i> <code>S(N) = 1 / [ (1 - p) + (p / N) ]</code><br/>"
        "• <i>Given:</i> <code>S = 3.2</code>, <code>N = 4</code>.<br/>"
        "  <code>3.2 = 1 / [ (1 - p) + (p / 4) ]</code>.<br/>"
        "• <i>Algebraic Inversion:</i><br/>"
        "  <code>(1 - p) + 0.25p = 1 / 3.2 = 0.3125</code>.<br/>"
        "  <code>1 - 0.75p = 0.3125</code>.<br/>"
        "  <code>0.75p = 1 - 0.3125 = 0.6875</code>.<br/>"
        "  <code>p = 0.6875 / 0.75 = 0.91667 (91.67%)</code>.<br/>"
        "• <b>Final Answer:</b> The parallelizable proportion <code>p</code> of the codebase constitutes exactly <b>91.67%</b>."
    ]
    for s in sol_quant:
        story.append(Paragraph(s, styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 6))
    # Solutions Part C
    story.append(Paragraph("<b>Solutions to Part C: Analytical Model Essays (26 to 35)</b>", styles['SecH2']))
    
    sol_essay = [
        "<b>Question 26 Model Answer:</b><br/>"
        "The technological transition from First-Generation thermionic vacuum tubes to Second-Generation solid-state transistors represents one of the most critical paradigm shifts in engineering history.<br/>"
        "1. <b>Physical Switching Mechanism:</b> Vacuum tubes operate on thermionic emission within an evacuated glass bulb. A tungsten filament must be heated to extreme temperatures (>1000°C) to boil electrons off a cathode, which are attracted across a vacuum gap to an anode plate, gated by a control grid. Transistors, by contrast, are solid-state semiconductor devices fabricated from silicon or germanium. They control current flow through the movement of electrons and holes across microscopic p-n junctions without requiring physical vacuums, mechanical heating, or electron boiling.<br/>"
        "2. <b>Electrical Power Consumption:</b> Vacuum tubes require continuous electrical current solely to heat the filament (consuming 2 to 10 Watts per tube) in addition to high plate voltages (100–300V DC). Transistors require no filament heating and operate at low operational voltages (typically 1.5–5V DC), consuming milliwatts—a reduction in electrical power demand exceeding 99.9%.<br/>"
        "3. <b>Thermal Dissipation & Cooling:</b> The enormous electrical power of thousands of vacuum tubes converted into intense thermal heat. The ENIAC dissipated 150 kW of heat, necessitating dedicated industrial refrigeration plants. Transistors emit negligible heat, enabling dense circuit packaging.<br/>"
        "4. <b>Reliability & MTBF:</b> Vacuum tube filaments suffered mechanical fatigue, cathode poisoning, and thermal burnout, resulting in system Mean Time Between Failures (MTBF) measured in mere hours. In contrast, transistors contain no moving parts or consumable filaments, offering MTBFs exceeding tens of thousands of operating hours and establishing reliable commercial computing.",

        "<b>Question 27 Model Answer:</b><br/>"
        "Charles Babbage's Analytical Engine (1837) represents the theoretical prototype of the modern general-purpose digital computer, anticipating the Von Neumann architecture by over a century.<br/>"
        "1. <b>The Store (Memory Subsystem):</b> The Store functioned as the passive memory unit. It consisted of a large mechanical bank of vertical steel axes containing stacked toothed brass wheels. Each wheel was engraved with digits 0 through 9, implementing decimal positional notation. The Store was engineered to hold 1,000 numerical variables, each consisting of 50 decimal digits, retaining intermediate operands and results without processing them.<br/>"
        "2. <b>The Mill (Arithmetic Processing Unit):</b> The Mill was the computational engine, analogous to the modern CPU's ALU. It consisted of complex mechanical gear trains, barrel controllers, and intermeshing racks that physically engaged to perform addition, subtraction, multiplication, and division. Operands were mechanically fetched from the Store, latched into the Mill, operated upon, and the resulting numbers were transferred back to designated columns in the Store.<br/>"
        "3. <b>Control Sequencing:</b> Operations were directed by punched cards (Operation Cards specifying the arithmetic function, and Variable Cards specifying which Store columns were read/written). The machine included conditional branching ('backing the cards') if a mechanical lever detected an arithmetic zero or sign reversal.",

        "<b>Question 28 Model Answer:</b><br/>"
        "The <b>Von Neumann Bottleneck</b> describes the fundamental throughput limit imposed by sharing a single physical bus system for both instruction fetching and operand data transfer between the central processor and main primary memory.<br/>"
        "1. <b>Physical Nature of the Bottleneck:</b> Because the CPU must use the same address and data buses to fetch an instruction and subsequently read or write memory data operands, these operations must be strictly serialized in time. Over decades, microprocessor clock speeds scaled by orders of magnitude while DRAM memory latency improved at a sluggish pace (the 'Memory Wall'). As a result, multi-gigahertz processors spend a significant fraction of clock cycles stalled, waiting for memory buses to deliver data.<br/>"
        "2. <b>Hardware Mitigation 1 — Multi-Level On-Die Caches (L1, L2, L3):</b> Modern CPUs integrate high-speed Static RAM (SRAM) cache hierarchies directly onto the processor silicon die. Caches exploit spatial and temporal locality, intercepting over 95% of memory references in 1 to 15 nanoseconds, shielding the CPU core from off-chip DRAM latency.<br/>"
        "3. <b>Hardware Mitigation 2 — Split L1 Caches (Modified Harvard):</b> While external system memory remains unified (Von Neumann), on-die Level-1 cache is physically split into a dedicated L1 Instruction Cache (L1i) and a dedicated L1 Data Cache (L1d), allowing simultaneous instruction fetching and data reading.<br/>"
        "4. <b>Hardware Mitigation 3 — Branch Prediction & Speculative Execution:</b> Sophisticated hardware branch predictors analyze execution history, pre-fetching anticipated instructions from memory and speculatively executing code paths ahead of time.",

        "<b>Question 29 Model Answer:</b><br/>"
        "Enterprise Mainframes and High-Performance Supercomputers represent two fundamentally distinct engineering philosophies optimized for diametrically opposed computational workloads.<br/>"
        "1. <b>Supercomputer Design Philosophy:</b> Supercomputers maximize peak <b>Floating-Point Operations Per Second (FLOPS)</b> on massive, compute-bound, scientific mathematical workloads (e.g., climate modeling, aerodynamic simulations, molecular docking). They deploy hundreds of thousands of tightly coupled CPU and GPU cores operating in parallel on a single massive computational grid via message-passing interfaces (MPI).<br/>"
        "2. <b>Mainframe Design Philosophy:</b> Mainframes are engineered for <b>Reliability, Availability, and Serviceability (RAS)</b> and massive concurrent transactional throughput. Mainframes are designed to process billions of independent, small, I/O-heavy transactions (e.g., database queries, credit card authorizations, ledger balance updates) with guaranteed ACID (Atomicity, Consistency, Isolation, Durability) integrity and 'five nines' (99.999%) uptime.<br/>"
        "3. <b>Why Banks in Tanzania Choose Mainframes:</b> Commercial banks such as CRDB, NMB, and NBC process millions of simultaneous mobile money (M-Pesa, Airtel Money) and ATM transactions. These workloads require zero arithmetic complexity, but demand absolute data integrity and massive I/O bandwidth. Mainframes deploy specialized hardware <b>Channel Processors (System Assist Processors)</b> that handle all storage and network interrupts independently from central compute cores. A supercomputer would collapse under this I/O interrupt volume, whereas an IBM z16 mainframe handles it seamlessly with zero unplanned downtime.",

        "<b>Question 30 Model Answer:</b><br/>"
        "Analog and Digital computers represent two completely divergent paradigms of information processing and physical signal representation.<br/>"
        "1. <b>Signal Representation:</b> Analog computers represent information as continuous physical quantities (continuous electrical voltages, currents, shaft angles, or hydraulic pressures). Digital computers represent information as discrete, quantized binary states (binary digits 0 and 1, physically implemented as low and high voltage thresholds).<br/>"
        "2. <b>Mathematical Precision:</b> Analog precision is strictly bounded by electrical component tolerances, thermal drift, resistor noise, and amplifier saturation, typically yielding only 3 to 4 significant digits (0.1% to 0.01% precision). Digital computers provide arbitrary mathematical precision governed by binary word length (64-bit IEEE 754 floating-point provides ~16 decimal digits of precision; arbitrary-precision software libraries can compute to millions of digits).<br/>"
        "3. <b>Execution Parallelism:</b> Analog computers are inherently parallel: differential equations are solved instantaneously as voltages propagate through operational amplifier circuits. Digital computers execute operations sequentially or through pipelined clock cycles.<br/>"
        "4. <b>Noise Sensitivity & Reproducibility:</b> Analog circuits are vulnerable to electromagnetic interference (EMI) and temperature drift, leading to non-reproducible results. Digital circuits possess immense noise immunity because voltage signals within wide margins are cleanly restored to binary 1 or 0, guaranteeing 100% reproducible execution.",

        "<b>Question 31 Model Answer:</b><br/>"
        "In 1965, Gordon Moore, co-founder of Fairchild Semiconductor and Intel, published an empirical observation in <i>Electronics</i> magazine that became known as <b>Moore's Law</b>.<br/>"
        "1. <b>Core Formulation:</b> Moore observed that the number of transistors that could be economically fabricated onto an integrated circuit doubled approximately every 12 months (revised in 1975 to every 18 to 24 months), while the manufacturing cost per transistor decreased exponentially.<br/>"
        "2. <b>Economic & Technological Driver:</b> Moore's Law was not a natural physical law, but an industrial roadmap and economic imperative. Semiconductor manufacturers recognized that if they did not shrink transistor gate geometries and double density every two years, their competitors would, rendering their product lines obsolete.<br/>"
        "3. <b>Virtuous Cycle of Innovation:</b> Each semiconductor shrink delivered four concurrent benefits: (a) Doubled computational density on the same die area, (b) Faster transistor switching frequencies due to shorter electron transit paths, (c) Lower dynamic power consumption per switching event, and (d) Falling unit costs. This virtuous cycle democratized computing, transforming multi-million-dollar government mainframes into multi-gigahertz smartphones affordable to rural farming communities in Tanzania.",

        "<b>Question 32 Model Answer:</b><br/>"
        "An <b>Embedded Computer</b> is a specialized computing system designed to perform dedicated, real-time control functions within a larger mechanical or electrical host machine (e.g., automobile ABS, solar inverters, drone autosteer).<br/>"
        "1. <b>Architectural Integration:</b> A Microcontroller Unit (MCU) integrates the CPU, non-volatile flash ROM firmware, SRAM primary memory, system timers, Analog-to-Digital Converters (ADCs), and digital I/O interfaces onto a single monolithic silicon chip. Desktop microcomputers utilize modular architectures with separate CPU sockets, motherboard chipsets, DIMM RAM slots, storage drives, and expansion cards.<br/>"
        "2. <b>Resource Allocations:</b> MCUs operate with modest resources (clock speeds of 16 to 240 MHz, SRAM of 2 KB to 512 KB, flash storage of 32 KB to 4 MB). Desktop microcomputers feature multi-gigahertz multi-core processors, 8 to 64 GB of DRAM, and terabytes of solid-state storage.<br/>"
        "3. <b>Power Consumption & Environmental Tolerance:</b> MCUs consume milliwatts or microwatts, operating for years on compact battery packs or solar harvesters across extreme temperature ranges (-40°C to +85°C). Desktop PCs draw 65 to 500 Watts of AC power and require controlled indoor environments.<br/>"
        "4. <b>Software Architecture:</b> MCUs run bare-metal infinite polling loops (<code>setup()</code> and <code>loop()</code>) or lightweight Real-Time Operating Systems (FreeRTOS) with sub-microsecond interrupt latencies. Desktops run general-purpose preemptive operating systems (Windows, Linux).",

        "<b>Question 33 Model Answer:</b><br/>"
        "The historical evolution of primary computer memory reflects an unceasing engineering struggle to balance capacity, access latency, non-volatility, physical size, and manufacturing cost.<br/>"
        "1. <b>Acoustic Mercury Delay Lines (1st Generation):</b> Developed in the 1940s (used in EDVAC). Electrical data pulses were converted by piezoelectric quartz crystals into ultrasonic acoustic waves traveling through 1.5-meter steel tubes filled with liquid mercury. At the far end, another crystal picked up the pulses, amplified them, and recirculated them. Memory was strictly sequential and acoustic latency was enormous (~1 millisecond).<br/>"
        "2. <b>Magnetic Ferrite Core Memory (2nd & 3rd Generations):</b> Invented by An Wang and Jay Forrester in the early 1950s. Tiny toroidal rings of ferromagnetic ceramic were strung onto orthogonal copper wire grids (X and Y drive lines, Sense, Inhibit). Passing half-currents through intersecting wires selected a specific core, switching its magnetic polarity clockwise (1) or counter-clockwise (0). Core memory provided true random access, 1-microsecond access times, and absolute non-volatility, dominating computing for two decades.<br/>"
        "3. <b>Semiconductor Dynamic RAM (4th & 5th Generations):</b> Invented by Robert Dennard at IBM in 1968 and commercialized as the Intel 1103 (1970). DRAM stores binary bits as electrical charges on microscopic MOS capacitors, switched by a single MOSFET transistor (the 1T-1C cell). DRAM delivers gigabytes of storage on fingernail-sized silicon chips with access times under 15 nanoseconds, completely displacing magnetic core memory.",

        "<b>Question 34 Model Answer:</b><br/>"
        "The <b>'Megahertz Myth'</b> is the common misconception that microprocessor clock frequency alone determines computational execution speed.<br/>"
        "1. <b>Deconstructing the Myth via the CPU Equation:</b> True execution time is governed by the CPU performance equation: <code>CPU_Time = (Instruction Count * CPI) / Clock_Frequency</code>. Clock frequency merely defines how many clock ticks occur per second; it does NOT define how much productive work is accomplished per clock tick.<br/>"
        "2. <b>Microarchitectural Efficiency (IPC):</b> Instructions Per Cycle (IPC = 1 / CPI) measures microarchitectural efficiency. A processor with wider superscalar execution units, deeper out-of-order execution windows, superior branch prediction, and massive on-die cache hierarchies can achieve an IPC of 2.5 instructions per cycle. In contrast, an inefficient, deeply pipelined processor may achieve an IPC of only 0.8.<br/>"
        "3. <b>Historical Proof (Intel Pentium 4 vs AMD Athlon):</b> In the early 2000s, Intel's Pentium 4 featured an ultra-deep 31-stage pipeline ('NetBurst') operating at 3.6 GHz, but suffered high CPI due to frequent pipeline flushes on branch mispredictions. AMD's Athlon 64 operating at only 2.2 GHz easily outperformed the 3.6 GHz Pentium 4 in real-world benchmarks because it retired more instructions per cycle.",

        "<b>Question 35 Model Answer:</b><br/>"
        "The <b>Intel 4004</b>, introduced in November 1971, is universally recognized as the catalyst for the Fourth Generation of computing.<br/>"
        "1. <b>Genesis of the Microprocessor:</b> In 1969, Japanese calculator manufacturer Busicom commissioned Intel to design 12 custom integrated circuits for their 141-PF printing calculator. Intel engineer Marcian 'Ted' Hoff recognized that designing 12 specialized chips was inefficient. Hoff, Federico Faggin, and Stan Mazor proposed an audacious alternative: a single, general-purpose central processing unit integrated onto a single silicon chip whose functions were determined by software stored in external ROM.<br/>"
        "2. <b>Technical Specifications:</b> Fabricated using 10-micrometer pMOS silicon gate technology, the 4004 packed 2,300 transistors onto a die measuring 12 mm<sup>2</sup>. It was a 4-bit CPU operating at a clock frequency of 740 kHz, executing up to 92,000 instructions per second.<br/>"
        "3. <b>Historical & Industrial Impact:</b> The Intel 4004 delivered computational power equivalent to the 30-ton ENIAC (1945) on a silicon chip the size of a fingernail. It proved that a complete, universal CPU could be mass-produced on silicon dies, decentralizing computing from corporate mainframe enclaves and directly launching the personal computer, embedded systems, and mobile revolutions."
    ]
    for s in sol_essay:
        story.append(Paragraph(s, styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 6))
    # Solutions Part D
    story.append(Paragraph("<b>Solutions to Part D: Applied Enterprise & Agricultural Engineering Designs (36 to 40)</b>", styles['SecH2']))
    
    sol_applied = [
        "<b>Question 36 Implementation Blueprint:</b><br/>"
        "• <b>Objective:</b> High-throughput photogrammetric workstation for processing 500+ multispectral aerial drone TIFF images into 3D Digital Surface Models (DSM) and NDVI orthomosaics.<br/>"
        "• <b>Processor (CPU):</b> AMD Ryzen Threadripper PRO 5965WX (24 physical cores, 48 threads, 3.8 GHz base clock, 4.5 GHz boost, 128 MB L3 cache, 128 PCIe 4.0 lanes). Massive multi-threading accelerates dense point-cloud bundle adjustment in Agisoft Metashape and Pix4D.<br/>"
        "• <b>Primary Memory (RAM):</b> 128 GB (4 × 32 GB) Quad-Channel DDR4-3200 Registered ECC (Error-Correcting Code) RAM. Photogrammetry builds massive spatial matrices in RAM; ECC memory is mandatory to eliminate silent bit-flips caused by cosmic rays that crash 8-hour rendering runs.<br/>"
        "• <b>Graphics Accelerator (GPU):</b> Nvidia RTX A4500 (20 GB GDDR6 with ECC, 7,168 CUDA cores, 224 Tensor cores). High VRAM capacity prevents out-of-memory errors during high-resolution texture mesh generation.<br/>"
        "• <b>Storage Subsystem:</b><br/>"
        "    - System Drive: 1 TB NVMe PCIe 4.0 M.2 SSD (7,000 MB/s sequential read) hosting Ubuntu 24.04 LTS and photogrammetry binaries.<br/>"
        "    - Scratch / Cache Drive: 2 TB NVMe PCIe 4.0 M.2 SSD dedicated exclusively to temporary image feature matching cache files.<br/>"
        "    - Archive Array: Two 8 TB Enterprise SATA HDDs configured in RAID 1 (Mirroring) for redundant local storage of completed GIS orthomosaics.<br/>"
        "• <b>Power & Environmental Protection:</b> 1,000W 80-Plus Platinum Certified Power Supply connected to a 1,500 VA / 900W Line-Interactive Uninterruptible Power Supply (UPS) with AVR to safeguard against Morogoro utility grid power fluctuations.",

        "<b>Question 37 Implementation Blueprint:</b><br/>"
        "• <b>Objective:</b> Autonomous, solar-powered environmental telemetry and precision drip irrigation controller deployed in rural Kilosa.<br/>"
        "• <b>Computing Core:</b> ESP32-WROOM-32 Microcontroller Unit (Tensilica Xtensa Dual-Core 32-bit LX6 @ 240 MHz, 520 KB SRAM, 4 MB SPI Flash). Deep-sleep current draw is only 15 μA.<br/>"
        "• <b>Sensor Interfacing Architecture:</b><br/>"
        "    - Analog Subsystem: Three capacitive soil moisture sensors interfaced through an external Texas Instruments ADS1115 16-bit Analog-to-Digital Converter (ADC) communicating over I2C (address 0x48). The 16-bit ADC delivers 65,536 discrete voltage quantization steps, vastly superior to the ESP32's noisy internal ADC.<br/>"
        "    - Digital Subsystem: SHT31 digital temperature and relative humidity sensor (I2C address 0x44) and waterproof DS18B20 digital soil temperature probes (1-Wire protocol on GPIO 4).<br/>"
        "• <b>Actuation Mechanism:</b> 12V DC Latching Solenoid Valve driven by an optocoupled dual N-channel MOSFET H-bridge circuit. Latching solenoids require an electrical pulse of only 50 ms to open or close, consuming zero power in steady state.<br/>"
        "• <b>Power Subsystem:</b> 20W Monocrystalline solar panel, MPPT charge controller, and a 3.2V 6,000 mAh LiFePO4 (Lithium Iron Phosphate) battery pack capable of sustaining 2,000+ thermal charge cycles.<br/>"
        "• <b>Communication:</b> Semtech SX1262 LoRa transceiver operating on 868 MHz transmitting telemetry packets every 30 minutes to a base station 8 km away, requiring zero cellular SIM subscription fees.",

        "<b>Question 38 Implementation Blueprint:</b><br/>"
        "The SMC computer laboratory technician executes the following standard Linux terminal commands to audit workstation hardware without opening physical chassis cases:<br/>"
        "1. <b>CPU Architecture & Cache Topology:</b><br/>"
        "   <code>lscpu</code><br/>"
        "   (Extracts architecture, model name, core counts, thread counts, virtualization support, and L1d, L1i, L2, L3 cache sizes).<br/>"
        "2. <b>System Memory & Available Swap:</b><br/>"
        "   <code>free -h</code> OR <code>cat /proc/meminfo | head -n 5</code><br/>"
        "   (Displays total physical RAM, currently used RAM, cached RAM, and available capacity in human-readable mebibytes/gibibytes).<br/>"
        "3. <b>Storage Block Devices & Partition Hierarchy:</b><br/>"
        "   <code>lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT,MODEL</code><br/>"
        "   (Lists all physical NVMe/SATA drives, partition boundaries, filesystem types such as ext4/NTFS, and mount points).<br/>"
        "4. <b>Motherboard BIOS/UEFI Firmware Version:</b><br/>"
        "   <code>sudo dmidecode -t bios -t baseboard</code><br/>"
        "   (Queries the Desktop Management Interface (DMI) / SMBIOS tables to display the motherboard manufacturer, board serial number, BIOS vendor, and firmware release date).",

        "<b>Question 39 Implementation Blueprint:</b><br/>"
        "• <b>Operational Scenario:</b> Distributing a 50 GB high-resolution satellite weather dataset to 200 undergraduate student laptops in a single computer lab at SUA.<br/>"
        "• <b>Client-Server Architecture Breakdown:</b><br/>"
        "    - Single departmental web server hosts the 50 GB file on an Apache/Nginx HTTP server.<br/>"
        "    - When 200 students simultaneously initiate downloads, the server's single 1 Gbps network interface card is overwhelmed.<br/>"
        "    - Bandwidth per student drops to: <code>1,000 Mbps / 200 = 5.0 Mbps (~625 KB/s)</code>.<br/>"
        "    - Total transfer time per student: <code>(50,000 MB) / (0.625 MB/s) = 80,000 seconds ≈ 22.2 hours</code>.<br/>"
        "    - Disk I/O thrashing and TCP connection saturation frequently crash the server.<br/>"
        "• <b>Peer-to-Peer (BitTorrent) Architecture Breakdown:</b><br/>"
        "    - The instructor generates a `.torrent` metadata file dividing the 50 GB dataset into 25,000 pieces (2 MB each) and seeds it to the first 5 machines.<br/>"
        "    - As student laptops download pieces, they immediately upload ('seed') those completed pieces to neighboring laptops across the campus Wi-Fi and switch fabric.<br/>"
        "    - Total upload capacity scales linearly with each participating peer (200 peers × 50 Mbps local Wi-Fi = 10,000 Mbps aggregate swarm bandwidth).<br/>"
        "    - The entire laboratory completes the 50 GB distribution in under 35 minutes, completely relieving the central server.",

        "<b>Question 40 Implementation Blueprint:</b><br/>"
        "• <b>Objective:</b> Engineering a Hybrid Computing Architecture for real-time Variable-Rate Technology (VRT) pesticide spraying on an autonomous farm tractor.<br/>"
        "• <b>Analog Subsystem (Microsecond Closed-Loop Control):</b><br/>"
        "    - Deployed directly at the 24-meter tractor sprayer boom.<br/>"
        "    - Pressure transducers and ultrasonic canopy height sensors generate continuous voltage signals (0–5V).<br/>"
        "    - Analog operational amplifier circuits (op-amps) and passive RC filter networks perform real-time noise filtering and differential amplification.<br/>"
        "    - Analog comparator circuits provide instantaneous (sub-microsecond) hardware shutoff if boom hydraulic pressure exceeds safety thresholds, preventing line ruptures without waiting for CPU polling loops.<br/>"
        "• <b>Digital Microcomputer Subsystem (Algorithmic & Supervisory Intelligence):</b><br/>"
        "    - An in-cab ruggedized x86-64 microcomputer running embedded Linux and Robot Operating System (ROS).<br/>"
        "    - Reads digitized sensor streams via CAN bus (Controller Area Network - ISO 11783 / ISOBUS).<br/>"
        "    - Cross-references real-time RTK-GPS coordinates with a high-resolution GIS prescription weed map.<br/>"
        "    - An integrated Neural Processing Unit (NPU) runs a YOLO deep learning vision model processing camera feeds to classify weed species in real time.<br/>"
        "    - Digital outputs modulate pulse-width modulation (PWM) solenoid nozzle drivers at 10 Hz, varying droplet volume per square meter while logging compliance records to NVMe storage."
    ]
    for s in sol_applied:
        story.append(Paragraph(s, styles['DocBody']))
        story.append(Spacer(1, 4))

    # Compile the document
    out_pdf = render_pdf("BIT_111_Topic_1_Compendium.pdf", story, doc_title="BIT 111 Topic 1 Compendium")
    return out_pdf

if __name__ == "__main__":
    generate_topic_1_story()
