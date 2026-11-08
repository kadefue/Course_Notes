#!/usr/bin/env python3
"""
slides_topics_1_to_3.py
High-density lecture slide definitions for Topics 1, 2, and 3.
BIT 111: MICROCOMPUTERS AND APPLICATIONS
Sokoine University of Agriculture (SUA).
Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Each topic features strictly >= 30 slides (34-35 slides per topic).
"""

def get_topic_1_slides():
    return [
        {
            "type": "bullet",
            "title": "Topic 1: Lecture Outline & Learning Roadmap",
            "sub_title": "Foundational Computing Principles (Curriculum Coverage: 1.1, 1.2, 1.3)",
            "bullets": [
                "• Section 1.1: Evolution & The Five Computer Generations",
                "    - Active switching electronics: Vacuum tubes to ULSI & Quantum gates",
                "    - Architectural shifts, primary memory evolution & programming paradigms",
                "• Section 1.2: History of Computing & Visionary Pioneers",
                "    - Mechanical precursors: Abacus, Pascaline, Leibniz Reckoner, Jacquard",
                "    - Babbage's Difference/Analytical Engine & Ada Lovelace's algorithms",
                "    - Turing's computability, Hollerith's punch cards, and the Microprocessor explosion",
                "• Section 1.3: Multi-Dimensional Computer Classifications",
                "    - Physical size & processing power: Supercomputers, Mainframes, Micros, Embedded",
                "    - Signal technology: Analog, Digital, and Hybrid paradigms",
                "    - Operational purpose & Network roles: General vs Dedicated; Clients vs Servers",
                "• Conceptual factors that influence computer performance"
            ],
            "callout": {
                "title": "PEDAGOGICAL GOAL",
                "body": "Understand the historical development, main parts, and everyday uses of computers, establishing a foundation for further study."
            }
        },
        {
            "type": "bullet",
            "title": "Topic 1: Intended Learning Outcomes (ILOs)",
            "sub_title": "Core Competencies for SUA Undergraduate Students",
            "bullets": [
                "• Define data, information, and the Information Processing Cycle (IPOS).",
                "• Contrast the physical components, speed, memory, and programming of all 5 computer generations.",
                "• Explain John von Neumann's stored-program architecture and the 'Von Neumann Bottleneck'.",
                "• Identify seminal computing pioneers and their engineering contributions to modern IT.",
                "• Systematically classify any computer by size, signal technology, purpose, and network role.",
                "• Describe, without calculations, how processor design, memory, and software affect performance.",
                "• Formulate appropriate microcomputer infrastructure choices for agricultural and enterprise applications."
            ]
        },
        {
            "type": "bullet",
            "title": "Fundamental Concepts: Data vs Information",
            "sub_title": "The Raw Substrate versus The Contextualized Output",
            "bullets": [
                "• Data: Raw, unorganized, uninterpreted facts, symbols, or observations without inherent meaning.",
                "    - Examples: `23.4`, `1014`, `12/04/2026`, `MWZ-042`",
                "• Information: Data that has been processed, structured, contextualized, and organized to be meaningful.",
                "    - Example: 'Soil moisture at Mazimbu Block C dropped to 23.4% on 12/04/2026, triggering automated drip irrigation.'",
                "• Knowledge: Applied information combined with experience, rules, and actionable insight.",
                "• Metadata: 'Data about data' that defines properties, data types, timestamps, and provenance."
            ],
            "callout": {
                "title": "AGRICULTURAL CONTEXT",
                "body": "In SUA research trials, raw weather sensor logs are useless until processed into degree-day heat metrics to predict crop maturity."
            }
        },
        {
            "type": "bullet",
            "title": "The Information Processing Cycle (IPOS)",
            "sub_title": "The Universal Operational Cycle of Electronic Computers",
            "bullets": [
                "• Input: Acceptance of external data and instructions into binary form via input transducers (keyboards, mice, optical sensors, ADC).",
                "• Processing: Arithmetic manipulation and logical evaluation executed by the CPU according to stored software instructions.",
                "• Output: Transformation of internal binary results into human-comprehensible or machine-actuatable forms (displays, printers, solenoids).",
                "• Storage: Non-volatile persistence of programs and data on secondary storage media (SSDs, HDDs, flash memory) for future retrieval.",
                "• Communication (Modern 5th Element): Transmission of data and telemetry across local buses and network interfaces (Ethernet, Wi-Fi, LoRaWAN)."
            ]
        },
        {
            "type": "bullet",
            "title": "First Generation Computers (1940 – 1956)",
            "sub_title": "The Thermionic Valve Era: Massive Scale, Heat, and Hardwiring",
            "bullets": [
                "• Active Electronics: Vacuum Tubes (Thermionic Valves) acting as binary switches and amplifiers.",
                "• Internal Memory: Mercury Delay Lines, Williams-Kilburn Tubes, and early Magnetic Drums.",
                "• Input / Output Media: Punched cards (80-column Hollerith format) and paper tape.",
                "• Programming Paradigm: Raw Machine Language (binary 0s and 1s) and manual plugboard wiring.",
                "• Operational Characteristics: Enormous electrical power consumption (150+ kW), severe heat generation, and frequent tube blowouts (MTBF < 2 hours).",
                "• Landmark Systems: ENIAC (1945), EDVAC (1949), UNIVAC I (1951 - first commercial computer)."
            ]
        },
        {
            "type": "bullet",
            "title": "Second Generation Computers (1956 – 1963)",
            "sub_title": "The Solid-State Revolution: Discrete Transistors & Ferrite Core",
            "bullets": [
                "• Active Electronics: Discrete Bipolar Junction Transistors (invented at Bell Labs in 1947).",
                "• Transistor Advantages: 1/1000th the size of tubes, fraction of the power, instant-on, no fragile filament to burn out.",
                "• Internal Memory: Magnetic Ferrite Core Memory (coincident-current toroidal rings, non-volatile).",
                "• Secondary Storage: Magnetic tape drives and early commercial magnetic disk drives (IBM RAMAC 305, 1956).",
                "• Software Evolution: Emergence of Assembly Language and early High-Level Languages (FORTRAN for science, COBOL for business).",
                "• Landmark Systems: IBM 7090, IBM 1401, DEC PDP-1 (precursor to minicomputers)."
            ]
        },
        {
            "type": "bullet",
            "title": "Third Generation Computers (1964 – 1971)",
            "sub_title": "The Monolithic Integrated Circuit (IC) & Time-Sharing",
            "bullets": [
                "• Active Electronics: Small-Scale Integration (SSI: < 100 transistors) and Medium-Scale Integration (MSI: 100–1,000 transistors) on silicon planar chips.",
                "• Circuit Innovation: Invented independently by Jack Kilby (Texas Instruments) and Robert Noyce (Fairchild Semiconductor).",
                "• Operating System Revolution: Multi-programming and Time-Sharing Operating Systems (OS/360, MULTICS, early UNIX).",
                "• Interactive Terminals: Video display terminals (VDTs) replaced punched cards, allowing real-time interactive debugging.",
                "• Standardization: Introduction of the 8-bit byte and ASCII character encoding standard.",
                "• Landmark Systems: IBM System/360 family (upward-compatible architecture), DEC PDP-8 (first mass-market minicomputer)."
            ]
        },
        {
            "type": "bullet",
            "title": "Fourth Generation Computers (1971 – Present)",
            "sub_title": "Microprocessors, LSI/VLSI, and the Personal Computer Revolution",
            "bullets": [
                "• Active Electronics: Large-Scale (LSI: 10<sup>3</sup>–10<sup>4</sup>) and Very Large-Scale Integration (VLSI: 10<sup>4</sup>–10<sup>7</sup> transistors per die).",
                "• The Microprocessor: Complete CPU on a single silicon chip (Intel 4004 in 1971; Intel 8080/8086).",
                "• Primary Memory: Semiconductor DRAM (Dynamic RAM) displacing magnetic core.",
                "• Personal Computing Emergence: Altair 8800 (1975), Apple II (1977), IBM 5150 PC (1981).",
                "• Graphical User Interfaces (GUI): Desktop metaphor, WIMP (Windows, Icons, Menus, Pointer) popularized by Apple Macintosh (1984) and Microsoft Windows.",
                "• Secondary Storage: 5.25\" and 3.5\" floppy disks, high-capacity HDDs, optical CD-ROMs, and early flash memory."
            ]
        },
        {
            "type": "bullet",
            "title": "Fifth Generation Computers (Present & Future)",
            "sub_title": "Ultra-Large Scale Integration, Multi-Core, AI & Quantum Systems",
            "bullets": [
                "• Active Electronics: Ultra Large-Scale Integration (ULSI) with tens of billions of transistors (3nm / 2nm lithography).",
                "• Architectural Paradigms: Massively parallel computing, heterogeneous computing (CPU + GPU + NPU / TPU).",
                "• Artificial Intelligence & Deep Learning: Neural network inference accelerators integrated directly on silicon dies.",
                "• Natural Interaction: Natural language processing, computer vision, voice recognition, adaptive bio-sensing.",
                "• Distributed Cloud Computing: Elastic serverless architectures and edge-computing micro-nodes.",
                "• Frontier Computing: Quantum computers (qubits, superposition, entanglement) solving cryptanalytic and molecular simulations."
            ]
        },
        {
            "type": "table",
            "title": "Comparative Matrix: The Five Computer Generations",
            "headers": ["Generation", "Active Device", "Primary Memory", "Programming Level", "Relative Capability", "Key Landmark"],
            "rows": [
                ["1st (1940-56)", "Vacuum Tubes", "Mercury Delay / Drums", "Machine Language", "Limited; very large systems", "ENIAC, UNIVAC I"],
                ["2nd (1956-63)", "Transistors", "Magnetic Core", "Assembly / FORTRAN", "Smaller and more reliable", "IBM 7090, PDP-1"],
                ["3rd (1964-71)", "Integrated Circuits (SSI/MSI)", "Magnetic Core / Semis", "High-Level (COBOL, C)", "More compact and versatile", "IBM System/360"],
                ["4th (1971-Pres)", "VLSI Microprocessor", "Semiconductor DRAM", "4GL, OOP, Web, Scripting", "Personal and portable systems", "IBM PC, Apple Mac"],
                ["5th (Present+)", "ULSI / Multi-Core / NPUs", "3D NAND / HBM / Quantum", "AI, Python, Declarative", "Connected, specialized systems", "Multi-core, TPU, Rigetti"]
            ],
            "col_widths": [1.8, 2.2, 2.2, 2.2, 1.8, 2.1]
        },
        {
            "type": "bullet",
            "title": "The Stored-Program Concept & Von Neumann Model",
            "sub_title": "First Draft of a Report on the EDVAC (John von Neumann, 1945)",
            "bullets": [
                "• Core Innovation: Both program instructions and operative data reside together in the same shared, addressable read-write memory space.",
                "• Eliminates Hardwiring: Changing a computer program no longer requires physical rewiring or resetting patch cords.",
                "• Five Architectural Subsystems:",
                "    1. Arithmetic Logic Unit (ALU): Executes arithmetic operations (+, -, *, /) and logical tests (AND, OR, NOT).",
                "    2. Control Unit (CU): Fetches, decodes, and orchestrates the micro-operations of each instruction.",
                "    3. Memory Subsystem: Linear array of addressable storage cells holding instructions and operands.",
                "    4. Input Subsystem: Channels accepting external signals into internal binary registers.",
                "    5. Output Subsystem: Channels presenting internal results to external devices."
            ]
        },
        {
            "type": "figure",
            "title": "Von Neumann Architecture & Shared Bus Pipeline",
            "img": "fig1_2_von_neumann_architecture.png",
            "caption": "The classical Von Neumann model illustrating ALU, Control Unit, Registers, and System Bus interface.",
            "bullets": [
                "• Unified Memory: Single physical bus path for instruction fetching and data reading/writing.",
                "• The Von Neumann Bottleneck: CPU processing speed far outpaces memory bus bandwidth; CPU is frequently stalled waiting for memory operands.",
                "• Modern Mitigations: Multi-level SRAM cache hierarchies (L1, L2, L3), instruction pre-fetching, branch prediction, and pipelining.",
                "• Harvard Architecture Contrast: Implements physically separate buses for instructions and data (common in DSPs and ARM Cortex microcontrollers)."
            ]
        },
        {
            "type": "bullet",
            "title": "Early History: Mechanical Aids to Automated Looms",
            "sub_title": "From Manual Bead Computation to Programmable Cards",
            "bullets": [
                "• The Abacus (c. 2500 BCE): First mechanical aid for positional arithmetic.",
                "• Napier's Bones (1617, John Napier): Logarithmic calculation rods enabling rapid multiplication.",
                "• The Slide Rule (1622, William Oughtred): Analog calculating device dominant until electronic pocket calculators (1970s).",
                "• The Pascaline (1642, Blaise Pascal): First gear-driven mechanical calculating machine (addition and subtraction).",
                "• Leibniz Stepped Reckoner (1673, Gottfried Wilhelm Leibniz): Stepped gear mechanism capable of direct multiplication and division; formulated binary arithmetic.",
                "• Jacquard Loom (1804, Joseph Marie Jacquard): Used punched cards to automate complex textile weaving patterns — first programmable automation device."
            ]
        },
        {
            "type": "bullet",
            "title": "Pioneers: Charles Babbage & Augusta Ada Lovelace",
            "sub_title": "The Grandfathers and Grandmothers of Universal Computation",
            "bullets": [
                "• Charles Babbage (1791–1871): 'Father of Computing'.",
                "    - Difference Engine (1822): Mechanical polynomial evaluator designed to eliminate human error in mathematical tables.",
                "    - Analytical Engine (1837): The true mechanical general-purpose computer design featuring a 'Store' (Memory), a 'Mill' (CPU), punched card input, and sequential control flow with conditional branching.",
                "• Augusta Ada Lovelace (1815–1852): 'World's First Computer Programmer'.",
                "    - Translated Menabrea's paper on the Analytical Engine and added extensive 'Notes'.",
                "    - Created Note G: An algorithm for generating Bernoulli numbers, widely recognized as an early published computer program.",
                "    - Articulated the visionary concept that machines could manipulate any symbols (including music and graphics), not just numbers."
            ]
        },
        {
            "type": "bullet",
            "title": "Pioneers: Herman Hollerith & Alan Turing",
            "sub_title": "Electromechanical Census Tabulation and Theoretical Foundations",
            "bullets": [
                "• Herman Hollerith (1860–1929):",
                "    - Developed electromechanical punched card tabulating machines for the 1890 US Census, completing in 3 years what took 8 years prior.",
                "    - Founded the Tabulating Machine Company in 1896, which later merged into IBM (International Business Machines) in 1924.",
                "• Alan Mathison Turing (1912–1954):",
                "    - Published 1936 paper introducing the Universal Turing Machine (UTM), establishing the mathematical limits of what can be computed.",
                "    - Led cryptanalysis at Bletchley Park during WWII, designing the electromechanical 'Bombe' to break Enigma enciphered traffic.",
                "    - Formulated the Turing Test (1950) as an operational criterion for artificial machine intelligence."
            ]
        },
        {
            "type": "bullet",
            "title": "Pioneers: Atanasoff, Mauchly, Eckert & von Neumann",
            "sub_title": "The Transition to High-Speed Electronic Digital Machinery",
            "bullets": [
                "• John Vincent Atanasoff & Clifford Berry (1939–1942):",
                "    - Built the Atanasoff-Berry Computer (ABC) at Iowa State: First electronic digital computer utilizing binary arithmetic, regenerative capacitor memory, and vacuum tubes.",
                "• John Mauchly & J. Presper Eckert (1943–1946):",
                "    - Designed and constructed the ENIAC (Electronic Numerical Integrator and Computer) at University of Pennsylvania for ballistic trajectory calculations.",
                "    - Contained 17,468 vacuum tubes, weighed 30 tons, and performed 5,000 additions per second.",
                "• John von Neumann (1903–1957):",
                "    - Collaborated with Eckert and Mauchly on the EDVAC project, formally documenting the stored-program concept that became the blueprint for 20th-century computing."
            ]
        },
        {
            "type": "bullet",
            "title": "Semiconductor Pioneers & The Silicon Microprocessor",
            "sub_title": "From Discrete Transistors to Desktop Supercomputing",
            "bullets": [
                "• Bardeen, Brattain & Shockley (1947): Invented the point-contact and junction transistor at Bell Telephone Laboratories (Nobel Prize 1956).",
                "• Jack Kilby (1958) & Robert Noyce (1959): Independently created the integrated circuit, solving the 'tyranny of numbers' in circuit interconnections.",
                "• Gordon Moore (1965): Formulated 'Moore's Law' — transistor density on microchips doubles roughly every 18 to 24 months with falling unit costs.",
                "• Marcian 'Ted' Hoff, Federico Faggin & Stan Mazor (1971): Designed the Intel 4004 (2,300 transistors, 4-bit, 740 kHz), the first commercially sold monolithic single-chip microprocessor."
            ]
        },
        {
            "type": "bullet",
            "title": "Pioneers of the Personal Computer Revolution",
            "sub_title": "Democratizing Computing: Garage Innovators to Global Giants",
            "bullets": [
                "• Steve Wozniak & Steve Jobs (1976):",
                "    - Wozniak engineered the Apple I and Apple II, the first mass-produced personal computer with color graphics and integrated case.",
                "    - Jobs championed intuitive design, laser typography, and the graphical user interface on the Macintosh (1984).",
                "• Bill Gates & Paul Allen (1975):",
                "    - Founded Microsoft, writing Altair BASIC and licensing MS-DOS to IBM for the landmark IBM 5150 PC, standardizing the personal computer platform.",
                "• Tim Berners-Lee (1989):",
                "    - Invented the World Wide Web at CERN, defining HTML, HTTP, and URLs, transforming computers from calculating nodes into a global information web.",
                "• Linus Torvalds (1991):",
                "    - Created the Linux kernel, launching the open-source revolution powering global cloud servers, supercomputers, and Android devices."
            ]
        },
        {
            "type": "figure",
            "title": "Multi-Dimensional Classification of Computer Systems",
            "img": "fig1_3_computer_classifications.png",
            "caption": "Taxonomy of computer systems classified by Physical Size, Signal Technology, and Operational Purpose.",
            "bullets": [
                "• Classification by Scale & Power: Supercomputers, Mainframes, Minicomputers, Microcomputers, and Embedded Microcontrollers.",
                "• Classification by Underlying Technology: Analog (continuous voltage), Digital (discrete binary states), and Hybrid (mixed-signal).",
                "• Classification by Purpose: General-Purpose (multipurpose operating systems) vs Dedicated/Special-Purpose (firmware-locked tasks).",
                "• Classification by Network Hierarchy: Enterprise Servers, Workstations, Interactive Clients, and Autonomous Edge Nodes."
            ]
        },
        {
            "type": "bullet",
            "title": "Classification by Size: Supercomputers",
            "sub_title": "Extreme Parallelism & High-Performance Computing (HPC)",
            "bullets": [
                "• Primary Metric: Extreme Floating-Point Operations Per Second (FLOPS). Modern frontier systems exceed 1 ExaFLOPS (10<sup>18</sup> FLOPS).",
                "• Physical Architecture: Hundreds of thousands of multi-core CPU and GPU nodes interconnected by ultra-low-latency networks (e.g., InfiniBand 400 Gbps).",
                "• Thermal & Power Constraints: Consumes 10 to 30 Megawatts of power, requiring liquid immersion or closed-loop water cooling.",
                "• Dominant Applications: Global climate modeling, quantum chemistry simulations, nuclear stockpile stewardship, agricultural genomics, and massive AI training.",
                "• Global Benchmark: The TOP500 list (updated bi-annually using the High-Performance Linpack benchmark)."
            ]
        },
        {
            "type": "bullet",
            "title": "Classification by Size: Mainframe Computers",
            "sub_title": "The Bedrock of High-Volume Enterprise Transaction Processing",
            "bullets": [
                "• Primary Philosophy: Unrivaled Reliability, Availability, and Serviceability (RAS) rather than raw floating-point peak speed.",
                "• Key Attributes: Massive I/O bandwidth, independent specialized channel processors, hardware fault tolerance, and hot-swappable components.",
                "• Operational Uptime: 'Five Nines' (99.999%) availability, equating to less than 5 minutes of unplanned downtime per calendar year.",
                "• Virtualization: Hardware partitioning (LPARs) running thousands of isolated operating system instances simultaneously.",
                "• Enterprise Role: Core banking (CRDB, NMB in Tanzania), national airline reservations, tax revenue processing, credit card clearing.",
                "• Exemplar: IBM z16 running IBM z/OS and Linux on IBM Z."
            ]
        },
        {
            "type": "bullet",
            "title": "Classification by Size: Minicomputers & Microcomputers",
            "sub_title": "Midrange Departmental Systems to Personal Desktop Workstations",
            "bullets": [
                "• Minicomputers (Midrange Computers):",
                "    - Historical role: Bridged the gap between monolithic mainframes and early microcomputers (1960s–1980s).",
                "    - Exemplars: DEC PDP-11, VAX-11/780, IBM AS/400 (now IBM i).",
                "    - Evolution: Largely superseded today by commodity rack-mounted multi-socket microcomputer servers.",
                "• Microcomputers (Personal Computers):",
                "    - Core Definition: Any computer whose central processing unit is a single microprocessor.",
                "    - Form Factors: Desktop towers, all-in-one PCs, laptops, convertibles, tablets, smartphones.",
                "    - Workstations: High-end microcomputers equipped with multi-core Xeon/Threadripper processors, ECC memory, and workstation GPUs for scientific CAD/GIS."
            ]
        },
        {
            "type": "bullet",
            "title": "Classification: Embedded Computers & Microcontrollers",
            "sub_title": "Invisible Intelligence Powering Modern Machinery and IoT",
            "bullets": [
                "• Embedded System: A dedicated computer system designed to perform one or a few dedicated functions, often with real-time computing constraints.",
                "• Physical Integration: Microcontroller Unit (MCU) integrating CPU, RAM, ROM/Flash, ADC, and I/O peripherals onto a single microchip.",
                "• Constraints: Low power consumption (milliwatts), compact footprint, harsh environmental tolerance, minimal memory (KB to MB).",
                "• Agricultural Engineering Applications:",
                "    - GPS-guided autonomous tractor autosteer units.",
                "    - Drip irrigation automated solenoid valve controllers.",
                "    - Silo temperature and grain moisture telemetry sensors.",
                "    - Exemplars: Arduino (ATmega328P), ESP32 (Wi-Fi/BLE), Raspberry Pi Pico (RP2040), STM32."
            ]
        },
        {
            "type": "bullet",
            "title": "Classification by Technology: Signal Representation",
            "sub_title": "Analog vs Digital vs Hybrid Computing Paradigms",
            "bullets": [
                "• Analog Computers:",
                "    - Process continuous physical variables (voltages, pressures, shaft rotations) without binary quantization.",
                "    - Inherently parallel and instantaneous differential equation solvers; limited precision and prone to thermal drift.",
                "• Digital Computers:",
                "    - Process discrete binary electrical states (0 and 1, low and high voltage).",
                "    - High mathematical precision, perfect reproducibility, arbitrary programmability, and non-volatile storage.",
                "• Hybrid Computers:",
                "    - Combine the real-time speed of analog processors with the precision, logic, and storage of digital microcomputers.",
                "    - Critical in flight simulators, ICU patient telemetry, and precision agricultural chemical blending systems."
            ]
        },
        {
            "type": "bullet",
            "title": "Classification by Purpose & Network Roles",
            "sub_title": "Operational Scope and Client-Server Distributed Architecture",
            "bullets": [
                "• Classification by Purpose:",
                "    - General-Purpose Computers: Designed to execute a wide variety of software applications (word processing, spreadsheets, games, coding).",
                "    - Special-Purpose / Dedicated Computers: Engineered to perform a single invariant task with hardwired or ROM-based logic (ATM controllers, automotive ECUs).",
                "• Classification by Network Hierarchy:",
                "    - Client: End-user microcomputer requesting services, data, or web pages across the network.",
                "    - Server: High-capacity centralized microcomputer or cluster dedicated to serving resources (Web, File, Database, Mail, DNS).",
                "    - Peer-to-Peer (P2P): Decentralized node acting simultaneously as both client and server."
            ]
        },
        {
            "type": "bullet",
            "title": "Factors That Influence Computer Performance",
            "sub_title": "A qualitative introduction for first-year students",
            "bullets": [
                "• Processor design and the number of tasks it can handle at once influence responsiveness.",
                "• Available memory affects how many programs and data files can be active together.",
                "• Storage type affects how quickly files and applications open.",
                "• Software design and unnecessary background programs can affect the user's experience.",
                "• A single specification does not determine overall performance; consider the intended task and the complete system."
            ]
        },
        {
            "type": "bullet",
            "title": "Choosing a Computer for Its Intended Work",
            "sub_title": "Comparing needs across SUA disciplines",
            "bullets": [
                "• Agricultural researchers may prioritize reliable data handling and compatibility with field equipment.",
                "• Veterinary and animal-science teams may need dependable access to records, images, and office applications.",
                "• Tourism and extension staff may prioritize portability, connectivity, and battery life.",
                "• Engineering, aquaculture, forestry, and food-science teams should match the device to their specialist software and data.",
                "• Compare whole-system needs rather than relying on one advertised specification."
            ]
        },
        {
            "type": "bullet",
            "title": "Computer Selection Case Study",
            "sub_title": "A conceptual example from agricultural research",
            "bullets": [
                "• A research team collects crop images in the field and reviews them at the university.",
                "• Field staff need portable devices that can capture and safely transfer image files.",
                "• Researchers reviewing large image collections may need a desktop with suitable memory and graphics capability.",
                "• The team should also consider software compatibility, backup, maintenance, and cost.",
                "• Explain which factors matter most for each role; no performance calculations are required."
            ]
        },
        {
            "type": "bullet",
            "title": "Microcomputer Applications in Smart Agriculture",
            "sub_title": "Field Case Studies from Sokoine University of Agriculture",
            "bullets": [
                "• SUA Mazimbu & Solomon Mahlangu Experimental Farms:",
                "    - Drip Irrigation Automation: Microcontrollers monitor soil conditions and control water solenoids.",
                "    - Drone Photogrammetry: Rugged microcomputer workstations process multispectral aerial imagery into NDVI crop stress maps.",
                "    - Dairy Cattle Telemetry: RFID transponders read cow collars at automated feeding stations, logging milk yield into central MySQL databases.",
                "    - Weather Telemetry Nodes: Solar-powered single-board computers transmit temperature, humidity, and rainfall data over cellular networks to DIIT servers.",
                "• Agricultural Extension Dispatches: Tablet microcomputers utilized by extension agents to identify pest infestations via computer vision models."
            ]
        },
        {
            "type": "bullet",
            "title": "Hardware Diagnostics via Linux Terminal",
            "sub_title": "Inspecting System Architecture & Microcomputer Peripherals",
            "bullets": [
                "• Essential Hardware Inspection Commands in Ubuntu Linux:",
                "    - `lscpu`: Displays comprehensive CPU architecture, cores, threads, sockets, virtualization, and cache sizes (L1d, L1i, L2, L3).",
                "    - `free -h`: Displays total, used, free, and available system RAM in human-readable mebibytes/gibibytes.",
                "    - `lsblk`: Displays block storage devices, partitions, mount points, and drive types (NVMe vs SATA).",
                "    - `lspci`: Lists all PCI/PCIe peripheral buses and connected controllers (GPU, Ethernet, NVMe).",
                "    - `lsusb`: Enumerates all Universal Serial Bus devices, hubs, and agricultural serial interfaces.",
                "    - `dmidecode -t bios`: Queries motherboard SMBIOS tables for firmware vendor, version, and release date."
            ]
        },
        {
            "type": "bullet",
            "title": "Topic 1: Key Takeaways & Synthesis Matrix",
            "sub_title": "Summary of Core Concepts for Examination Mastery",
            "bullets": [
                "• Five Generations: Defined by active electronics (Tubes → Transistors → ICs → VLSI Microprocessors → ULSI/AI/Quantum).",
                "• Von Neumann Model: Unified memory for data and instructions; performance constrained by the Von Neumann Bottleneck.",
                "• Pioneers: Babbage (hardware architecture), Lovelace (software algorithm), Turing (computability), von Neumann (stored program), Noyce/Kilby (IC), Hoff (microprocessor).",
                "• Classifications: Scale (Super > Mainframe > Mini > Micro > Embedded), Signal (Digital vs Analog vs Hybrid), Role (Client vs Server).",
                "• Performance depends on the processor, memory, storage, software, and the task being performed."
            ]
        },
        {
            "type": "bullet",
            "title": "Review Quiz & Knowledge Check",
            "sub_title": "Self-Testing Key Technical Concepts",
            "bullets": [
                "1. Why is the stored-program concept considered the most revolutionary breakthrough in computer design history?",
                "2. Contrast the physical reasons why magnetic ferrite core memory displaced vacuum delay lines in 2nd generation computers.",
                "3. Name two system characteristics that can affect how responsive a computer feels, and explain why one specification alone is not enough.",
                "4. Why can a program fail to benefit from a computer with multiple processor cores?",
                "5. What computer classification is optimal for an automated solar-powered irrigation valve controller in Kilosa?"
            ]
        },
        {
            "type": "bullet",
            "title": "Reading Assignments & Homework Notice",
            "sub_title": "Preparation for Next Lecture & Continuous Assessment",
            "bullets": [
                "• Required Readings:",
                "    - Smith, J. L., Wang, S., & Mortati, J. - Information Systems for Business and Beyond (2019), Chapter 1. https://opentextbook.site/informationsystems2019/",
                "    - Vermaat et al. - Discovering Computers: Digital Technology, Data, and Devices (16th ed.). Cengage. https://faculty.cengage.com/works/9781337285100",
                "• Homework Assignment 1 Notice:",
                "    - Available on SUA Moodle / Assignment directory: `BIT_111_Assignment_1.pdf`.",
                "    - Total Allocation: 100 Marks (Covers computer concepts and applied design).",
                "    - Submission Deadline: End of Week 2 by 17:00 EAT.",
                "• Next Lecture Preview: Topic 2 — Main Components of a Microcomputer (CPU, Buses, Memory, I/O)."
            ]
        }
    ]

# -------------------------------------------------------------
# TOPIC 2 SLIDES DATA
# -------------------------------------------------------------
def get_topic_2_slides():
    return [
        {
            "type": "bullet",
            "title": "Topic 2: Lecture Outline & Learning Roadmap",
            "sub_title": "Microcomputer Architecture, Subsystems & Comparisons (Coverage: 2.1, 2.2)",
            "bullets": [
                "• Section 2.1: Microcomputer Devices & Logical Configurations",
                "    - Central Processing Unit (CPU): Control Unit, ALU, Internal Registers, Fetch-Decode-Execute",
                "    - Primary Memory: ROM (PROM, EPROM, Flash) vs RAM (SRAM, DRAM, DDR4/DDR5 architectures)",
                "    - System Bus Topology: Data, Address, and Control buses; Expansion buses (PCIe, SATA, USB)",
                "    - Input & Output Subsystems: Human-interface peripherals, agricultural transducers, displays, printers",
                "    - Secondary & Tertiary Storage: Magnetic HDDs, Solid-State Drives (NAND flash), and Optical media",
                "• Section 2.2: Comparative Aspects of Computer Categories",
                "    - Microcomputers vs Enterprise Mainframes: Fault tolerance, RAS, and I/O channels",
                "    - Engineering Workstations vs Standard Microcomputers: ECC RAM, multi-socket CPUs, and pro GPUs",
                "    - Historical Minicomputers vs Modern Microcomputer Clusters and Cloud Nodes"
            ],
            "callout": {
                "title": "TOPIC OBJECTIVE",
                "body": "Describe the main parts of a microcomputer and how they work together to support common tasks."
            }
        },
        {
            "type": "bullet",
            "title": "Topic 2: Intended Learning Outcomes (ILOs)",
            "sub_title": "Core Competencies for Engineering & Informatics Students",
            "bullets": [
                "• Detail the internal micro-architecture of the CPU, including CU, ALU, and dedicated registers.",
                "• Trace the step-by-step micro-operations of the Fetch-Decode-Execute instruction cycle.",
                "• Evaluate the memory hierarchy in terms of access latency, capacity, and cost per bit.",
                "• Explain conceptually how address buses and data buses support communication between computer components.",
                "• Contrast HDD mechanical physics (seek time, latency) with SSD semiconductor NAND flash architecture.",
                "• Differentiate between Engineering Workstations, Consumer PCs, Mainframes, and Minicomputers.",
                "• Integrate agricultural sensor interfaces (ADC, I2C, SPI) into microcomputer data collection pipelines."
            ]
        },
        {
            "type": "figure",
            "title": "Microcomputer Hardware Block Diagram",
            "img": "fig2_1_microcomputer_hardware_block.png",
            "caption": "Functional block diagram showing CPU, System Buses, Memory, Storage, and I/O Subsystems.",
            "bullets": [
                "• Central Processing Unit (CPU): Executes instructions and orchestrates system timing.",
                "• System Bus: The tri-bus interconnect (Address, Data, Control) linking all primary subsystems.",
                "• Northbridge / System Agent: Connects high-speed devices (RAM, PCIe graphics) to the CPU.",
                "• Southbridge / PCH (Platform Controller Hub): Connects slower I/O buses (SATA, USB, Audio, Ethernet, BIOS)."
            ]
        },
        {
            "type": "bullet",
            "title": "The Central Processing Unit (CPU): Core Subsystems",
            "sub_title": "The Computational Engine of the Microcomputer",
            "bullets": [
                "• Arithmetic Logic Unit (ALU): Executes binary arithmetic (+, -, *, /) and bitwise Boolean logic (AND, OR, XOR, NOT, shifts).",
                "• Control Unit (CU): Decodes instructions, generates sequential micro-control signals, and manages clock synchrony.",
                "• Internal Register File: High-speed, on-die storage cells operating at processor clock speed:",
                "    - Program Counter (PC): Holds the memory address of the next instruction to fetch.",
                "    - Memory Address Register (MAR): Holds the physical memory address currently being accessed.",
                "    - Memory Data Register (MDR): Buffers data read from or written to memory.",
                "    - Instruction Register (IR): Holds the operational code (opcode) currently being decoded.",
                "    - Accumulator / General-Purpose Registers: Holds intermediate arithmetic operands and results.",
                "    - Flags / Status Register: Indicates condition codes (Zero, Carry, Overflow, Sign, Interrupt enable)."
            ]
        },
        {
            "type": "bullet",
            "title": "The Instruction Cycle: Fetch, Decode, Execute",
            "sub_title": "The Heartbeat of Microcomputer Processing",
            "bullets": [
                "• 1. Fetch Phase:",
                "    - `MAR ← [PC]`: Address in PC is placed onto the address bus.",
                "    - `Memory Read`: Control unit asserts read signal; memory places instruction onto data bus.",
                "    - `MDR ← Data Bus`: Instruction loaded into MDR.",
                "    - `IR ← [MDR]`: Instruction transferred to Instruction Register.",
                "    - `PC ← [PC] + 1`: Program counter incremented to point to the next instruction.",
                "• 2. Decode Phase: Control unit decodes opcode in IR, determines required operands and addressing modes.",
                "• 3. Execute Phase: ALU performs required operation; results written back to registers or main memory.",
                "• 4. Interrupt Check: Processor verifies if external hardware interrupts (timer, I/O) are asserted."
            ]
        },
        {
            "type": "figure",
            "title": "The Computer Memory Hierarchy",
            "img": "fig2_2_memory_hierarchy_pyramid.png",
            "caption": "The Memory Hierarchy Pyramid balancing speed, capacity, and cost per bit.",
            "bullets": [
                "• Trade-off Principle: As you descend the pyramid, capacity increases, cost per bit decreases, but access latency increases exponentially.",
                "• Level 0 - CPU Registers: < 1 KB, < 0.5 ns latency (direct silicon gates).",
                "• Level 1 - L1 Cache: 32–64 KB per core, 1 ns latency (on-die SRAM).",
                "• Level 2 - L2 Cache: 512 KB–1 MB per core, 3–5 ns latency.",
                "• Level 3 - L3 Cache: 16–96 MB shared, 10–15 ns latency.",
                "• Level 4 - Main Memory (DRAM): 16–128 GB, 50–70 ns latency.",
                "• Level 5 - Non-Volatile Storage (NVMe SSD / HDD): 1–10 TB, 10 μs (SSD) to 10 ms (HDD)."
            ]
        },
        {
            "type": "bullet",
            "title": "Primary Memory: ROM Technologies",
            "sub_title": "Non-Volatile Semiconductor Firmware Storage",
            "bullets": [
                "• Read-Only Memory (ROM): Non-volatile primary storage retaining code even when power is removed.",
                "• Evolution of ROM Devices:",
                "    - Mask ROM: Programmed during silicon fabrication; permanently unalterable.",
                "    - PROM (Programmable ROM): Field-programmable once using fusible links blown by high voltage.",
                "    - EPROM (Erasable PROM): Erased by exposing quartz window to intense ultraviolet (UV) light for 20 minutes.",
                "    - EEPROM (Electrically Erasable PROM): Byte-erasable electrically in-circuit; limited write cycles.",
                "    - Flash ROM (NOR Flash): Block-erasable high-speed firmware storage powering modern UEFI BIOS chips."
            ]
        },
        {
            "type": "bullet",
            "title": "Primary Memory: RAM Technologies (SRAM vs DRAM)",
            "sub_title": "Static vs Dynamic Volatile Random-Access Memory",
            "bullets": [
                "• Static RAM (SRAM):",
                "    - Storage Element: 6-transistor (6T) flip-flop circuit.",
                "    - Attributes: Fast (1–5 ns), does not require refresh cycles, low density, high power, very expensive.",
                "    - Application: Exclusively utilized for on-die CPU cache hierarchies (L1, L2, L3).",
                "• Dynamic RAM (DRAM):",
                "    - Storage Element: 1 transistor and 1 tiny capacitor (1T-1C cell).",
                "    - Attributes: High storage density, inexpensive, but capacitor charge leaks within milliseconds.",
                "    - Refresh Circuitry: Requires periodic refresh cycles (every 64 ms) to restore charge, introducing latency.",
                "    - Application: Main system memory (DIMM modules)."
            ]
        },
        {
            "type": "bullet",
            "title": "Modern Synchronous DRAM Evolution: DDR4 to DDR5",
            "sub_title": "Double Data Rate Architecture and Architectural Enhancements",
            "bullets": [
                "• Double Data Rate (DDR) Principle: Transfers data on both the rising and falling edges of the clock signal.",
                "• DDR4 SDRAM:",
                "    - Clock Speeds: 2133 to 3200 MT/s; Voltage: 1.2V.",
                "    - Channel Architecture: Single 64-bit data bus per module.",
                "• DDR5 SDRAM:",
                "    - Clock Speeds: 4800 to 8400+ MT/s; Voltage: 1.1V.",
                "    - Channel Architecture: Two independent 32-bit subchannels per DIMM, improving memory access concurrency.",
                "    - On-Die ECC: Internal error correction on the DRAM die for enhanced cell reliability at extreme densities.",
                "    - On-Module PMIC: Power Management Integrated Circuit moved from motherboard to the memory module."
            ]
        },
        {
            "type": "bullet",
            "title": "System Bus Architecture: Tri-Bus Fundamentals",
            "sub_title": "The Shared Highway for Data, Addresses, and Control",
            "bullets": [
                "• Definition: A set of shared parallel or serialized electrical conductors transmitting signals between components.",
                "• 1. Data Bus:",
                "    - Function: Carries actual data words and instruction operands between CPU, memory, and I/O devices.",
                "    - Directionality: Bidirectional (data flows to and from the CPU).",
                "    - Width: Typically 64 bits in modern microcomputers.",
                "• 2. Address Bus:",
                "    - Function: Carries the physical memory address or I/O port identifier being selected.",
                "    - Directionality: Unidirectional (CPU asserts addresses; memory responds).",
                "    - Address buses identify locations that the processor or another component needs to access.",
                "• 3. Control Bus:",
                "    - Function: Transmits operational timing and status signals (Memory Read/Write, I/O Read/Write, Clock, Reset, Interrupt Requests)."
            ]
        },
        {
            "type": "bullet",
            "title": "Address and Data Bus Concepts",
            "sub_title": "How computer components locate and exchange information",
            "bullets": [
                "• The address bus identifies the location that the processor or another component needs to access.",
                "• The data bus carries instructions or data between the processor, memory, and other components.",
                "• The control bus carries signals that coordinate activities such as reading, writing, and responding to an interrupt.",
                "• Bus width and design affect the amount of information a system can address or transfer, but this course treats the relationship conceptually.",
                "• Describe the purpose of each bus; numerical capacity and bandwidth calculations are outside this topic."
            ]
        },
        {
            "type": "bullet",
            "title": "Expansion Bus Architecture: PCI to PCI Express (PCIe)",
            "sub_title": "The Paradigm Shift from Shared Parallel to Point-to-Point Serial",
            "bullets": [
                "• Legacy PCI (Parallel): Shared parallel bus (32-bit, 33 MHz = 133 MB/s); suffered from clock skew across traces.",
                "• PCI Express (PCIe) Architecture:",
                "    - Point-to-Point Serial switched fabric connecting each device directly to the root complex.",
                "    - Scalable Lane Architecture: Uses dedicated differential signaling pairs (x1, x4, x8, x16 lanes).",
                "• PCIe Generation Bandwidths (per lane, each direction):",
                "    - PCIe 3.0: 8.0 GT/s (~985 MB/s per lane; x16 slot = 15.75 GB/s).",
                "    - PCIe 4.0: 16.0 GT/s (~1.97 GB/s per lane; x16 slot = 31.51 GB/s).",
                "    - PCIe 5.0: 32.0 GT/s (~3.94 GB/s per lane; x16 slot = 63.02 GB/s).",
                "• Applications: High-end graphics cards (x16), NVMe solid-state storage (x4), 10GbE network adapters (x4)."
            ]
        },
        {
            "type": "bullet",
            "title": "Secondary Storage: Magnetic Hard Disk Drives (HDD)",
            "sub_title": "Electromechanical Platters, Cylinders, and Physics of Access",
            "bullets": [
                "• Mechanical Architecture: Rigid rotating aluminum/glass platters coated with magnetic thin film, spinning on a central spindle (5400, 7200, 10000, 15000 RPM).",
                "• Read/Write Heads: Aerodynamic flying heads floating nanometers above platters on an actuator arm.",
                "• Formatting Geometry: Tracks (concentric rings), Sectors (standard 512 bytes or 4,096-byte Advanced Format), Cylinders (aligned tracks across all platters).",
                "• Total Data Access Time Components:",
                "    - 1. Seek Time (T<sub>seek</sub>): Time for actuator arm to move to target cylinder (avg 4–9 ms).",
                "    - 2. Rotational Latency (T<sub>rot</sub>): Time for target sector to rotate under head (avg = 1/2 revolution; 4.17 ms at 7200 RPM).",
                "    - 3. Transfer Time (T<sub>trans</sub>): Time to read/write sequential data bits (governed by track density).",
                "    - Average Access Time = T<sub>seek</sub> + T<sub>rot</sub> + Overhead ≈ 10 to 15 ms."
            ]
        },
        {
            "type": "bullet",
            "title": "Secondary Storage: Solid-State Drives (SSD)",
            "sub_title": "Semiconductor Flash Storage, NAND Physics, and Flash Controllers",
            "bullets": [
                "• Core Architecture: Silicon NAND flash memory chips managed by an intelligent multi-core Flash Controller.",
                "• Zero Moving Parts: Complete elimination of seek time and rotational latency; access time < 0.05 ms.",
                "• NAND Flash Cell Technologies:",
                "    - SLC (Single-Level Cell): 1 bit/cell; highest endurance (100,000 P/E cycles), fastest, highest cost.",
                "    - MLC (Multi-Level Cell): 2 bits/cell; 3,000–10,000 P/E cycles.",
                "    - TLC (Triple-Level Cell): 3 bits/cell; 1,000–3,000 P/E cycles; dominant consumer standard.",
                "    - QLC (Quad-Level Cell): 4 bits/cell; ~1,000 P/E cycles; high capacity, lower endurance.",
                "• Flash Management Imperatives: Wear-Leveling (distributing writes evenly across cells) and TRIM command (notifying drive of deleted LBAs to enable background block garbage collection)."
            ]
        },
        {
            "type": "table",
            "title": "Comparative Analysis: Storage Interfaces & Technologies",
            "headers": ["Metric", "Magnetic HDD (SATA)", "SATA SSD (2.5\")", "NVMe SSD (PCIe 4.0)", "Magnetic Tape (LTO-9)"],
            "rows": [
                ["Storage Medium", "Magnetic Platters", "NAND Flash", "3D NAND Flash", "Magnetic Barium Ferrite Tape"],
                ["Sequential Read", "150 - 260 MB/s", "500 - 560 MB/s", "5,000 - 7,400 MB/s", "400 MB/s (native)"],
                ["Random IOPS", "75 - 150 IOPS", "50,000 - 90,000 IOPS", "500,000 - 1,000,000 IOPS", "N/A (Sequential Only)"],
                ["Access Latency", "10 - 15 ms", "50 - 100 μs", "10 - 20 μs", "Seconds to Minutes"],
                ["Vulnerability", "Mechanical Shock", "Cell Wear (P/E)", "Thermal Throttling", "Physical Misplacement"],
                ["Primary Role", "Bulk Secondary / NAS", "Budget Upgrades", "OS Boot & Pro Compute", "Cold Deep Archival"]
            ],
            "col_widths": [2.0, 2.5, 2.5, 2.5, 2.8]
        },
        {
            "type": "bullet",
            "title": "Input Subsystems: Transducers to Digital Interface",
            "sub_title": "Human Input Devices & Agricultural Sensors",
            "bullets": [
                "• Keyboards: Switch matrix scanned by dedicated microcontroller; debounce circuitry generates make/break scan codes.",
                "• Optical Mice: LED/laser illuminates surface; CMOS optical sensor captures thousands of surface images/sec, calculating relative movement vectors.",
                "• Agricultural Sensors & Transducers:",
                "    - Thermistors & RTDs: Temperature-dependent resistance measuring grain silo thermal gradients.",
                "    - Capacitive Soil Moisture Probes: Measures dielectric permittivity of soil water content.",
                "• Analog-to-Digital Converter (ADC): Quantizes continuous analog voltages (0–5V) into discrete binary words (e.g., 10-bit ADC provides 1,024 discrete levels).",
                "• Communication Protocols: I2C (Inter-Integrated Circuit - 2 wire), SPI (Serial Peripheral Interface - 4 wire), UART (Asynchronous Serial)."
            ]
        },
        {
            "type": "bullet",
            "title": "Output Subsystems: Displays and Printing Technologies",
            "sub_title": "Visual Telemetry, Rasterization, and Hardcopy Reproduction",
            "bullets": [
                "• Display Technologies:",
                "    - LCD (Liquid Crystal Display) with LED Backlight: In-Plane Switching (IPS) panels offering superior color accuracy and 178° viewing angles for GIS/CAD.",
                "    - OLED (Organic LED): Self-emissive pixels offering infinite contrast ratio, true blacks, and rapid response times.",
                "    - Key Metrics: Native resolution (Full HD 1080p, 4K UHD), aspect ratio (16:9, 16:10), refresh rate (60 Hz, 144 Hz).",
                "• Printing Technologies:",
                "    - Dot-Matrix (Impact): Uses print pins striking an ink ribbon; indispensable for multi-part carbon copy financial invoices at SUA bursar.",
                "    - Inkjet: Piezoelectric or thermal nozzles spraying microscopic picoliter droplets; high-resolution photographic rendering.",
                "    - Laser (Electrophotographic): Laser discharges photosensitive drum, attracting toner powder transferred and fused to paper via heated rollers."
            ]
        },
        {
            "type": "bullet",
            "title": "Microcomputers vs Enterprise Mainframes",
            "sub_title": "Contrasting Architectural Paradigms and Throughput Philosophy",
            "bullets": [
                "• Processing Philosophy:",
                "    - Microcomputer: Optimized for low-latency interactive processing, single-user responsiveness, and high single-thread clock speed.",
                "    - Mainframe: Engineered for massive concurrent throughput, processing billions of independent transactional records per second.",
                "• I/O Channel Offloading:",
                "    - Microcomputer: CPU actively participates in managing bus interrupts and storage transfers (DMA helps, but CPU coordinates).",
                "    - Mainframe: Employs hundreds of dedicated Channel Processors (System Assist Processors) that handle all I/O independently from main compute engines.",
                "• Redundancy & Fault Tolerance: Mainframes feature dual lockstep execution, redundant power/cooling, and dynamic processor sparing."
            ]
        },
        {
            "type": "bullet",
            "title": "Engineering Workstations vs Standard Microcomputers",
            "sub_title": "Mission-Critical Precision Computing versus Consumer Utility",
            "bullets": [
                "• Processor Architecture: Consumer PCs utilize Intel Core i5/i7 or AMD Ryzen; Workstations deploy Intel Xeon or AMD Threadripper with higher PCIe lane counts.",
                "• Memory Integrity (ECC RAM):",
                "    - Standard PCs: Non-ECC RAM; silent bit-flips caused by cosmic radiation can corrupt simulation data or cause system crashes.",
                "    - Workstations: Error-Correcting Code (ECC) memory detects and corrects single-bit errors automatically, halting on multi-bit errors.",
                "• Graphics Accelerators: Consumer GPUs (Nvidia GeForce) prioritize gaming frame rates; Professional GPUs (Nvidia RTX A-Series) feature ISV-certified drivers for AutoCAD, ArcGIS, and SolidWorks with double-precision floating-point accuracy.",
                "• Mean Time Between Failures (MTBF): Workstation components are binned and rated for continuous 24/7/365 full-load computational workloads."
            ]
        },
        {
            "type": "bullet",
            "title": "Minicomputers vs Modern Microcomputer Clusters",
            "sub_title": "The Evolution from Midrange Hardware to Distributed Micro-Nodes",
            "bullets": [
                "• The Minicomputer Era (1965–1985): Multi-user systems (DEC PDP-11, VAX) sharing compute power via serial 'dumb terminals' across university departments.",
                "• The Downsizing Revolution: Microprocessors became so powerful and inexpensive that client-server microcomputer networks replaced monolithic minicomputers.",
                "• Modern Microcomputer Clusters (Beowulf Clusters):",
                "    - Network of commodity microcomputer nodes interconnected via high-speed gigabit switches running Linux.",
                "    - Delivers supercomputing throughput at a fraction of minicomputer or mainframe acquisition costs.",
                "    - Applied extensively in agricultural genomics, crop disease prediction, and remote sensing imagery processing at SUA."
            ]
        },
        {
            "type": "bullet",
            "title": "Hard Disk Drives and Solid-State Drives",
            "sub_title": "A qualitative comparison of secondary storage",
            "bullets": [
                "• Hard disk drives store data on rotating magnetic platters and use moving read/write heads.",
                "• Solid-state drives store data electronically and have no moving mechanical parts.",
                "• SSDs generally open files and applications more quickly, while HDDs are commonly used for economical bulk storage.",
                "• Consider portability, durability, capacity needs, cost, and backup when choosing a storage device.",
                "• Compare the two device types using their design and appropriate uses; no timing calculations are required."
            ]
        },
        {
            "type": "bullet",
            "title": "Agricultural IoT Hardware Design Case Study",
            "sub_title": "Autonomous Soil & Microclimate Station at SUA Mazimbu Farm",
            "bullets": [
                "• Environmental Challenge: Tropical field deployment, high humidity, erratic cellular coverage, no grid AC power.",
                "• System Architecture:",
                "    - Embedded Microcomputer: ESP32 dual-core microcontroller (240 MHz, ultra-low-power deep sleep mode).",
                "    - Sensor Bus (I2C): SHT31 air temperature/humidity sensor + BH1750 solar lux transducer.",
                "    - Analog Sensor Subsystem: Capacitive soil moisture probes interfaced via ADS1115 16-bit external ADC.",
                "    - Power Subsystem: 20W Monocrystalline solar panel + MPPT charge controller + 18650 LiFePO4 battery pack.",
                "    - Telemetry Subsystem: LoRaWAN 868 MHz transmitter beaming packets 5 km to the DIIT gateway receiver."
            ]
        },
        {
            "type": "bullet",
            "title": "Instruction Pipeline Architecture & Pipeline Hazards",
            "sub_title": "Overlapping Instruction Phases to Maximize Throughput",
            "bullets": [
                "• Pipelining Principle: Divides instruction execution into sequential stages (Fetch, Decode, Execute, Memory, Write-back), allowing multiple instructions to execute concurrently across different stages.",
                "• Pipeline Hazards (Factors causing pipeline stalls / bubbles):",
                "    - 1. Structural Hazard: Hardware resource conflict (e.g., single memory port simultaneously accessed by Fetch and Memory stages).",
                "    - 2. Data Hazard (Read-After-Write - RAW): Instruction depends on the computational result of an uncompleted prior instruction; mitigated via data forwarding/bypassing.",
                "    - 3. Control Hazard (Branch Hazard): Pipelining branch instructions before condition outcome is evaluated; mitigated via Branch Prediction (static vs 2-bit dynamic branch history tables) and Speculative Execution."
            ]
        },
        {
            "type": "bullet",
            "title": "Microprocessor Packaging & Socket Standards",
            "sub_title": "LGA, PGA, and BGA Thermal and Interconnect Engineering",
            "bullets": [
                "• Pin Grid Array (PGA): Pins located on the bottom of the processor package that mate with socket holes (e.g., legacy AMD AM4); pins fragile and vulnerable to bending.",
                "• Land Grid Array (LGA): Pins located inside the motherboard socket; processor package features flat gold contact pads (e.g., Intel LGA1700, AMD AM5); reduces risk of damaged CPU pins.",
                "• Ball Grid Array (BGA): Processor permanently soldered to motherboard using microscopic solder balls; ubiquitous in ultra-thin laptops, tablets, and smartphones; non-upgradeable.",
                "• Thermal Interface Materials (TIM) & Heat Spreaders: Integrated Heat Spreader (IHS), thermal paste, and finned heatsinks with copper heatpipes dissipating heat to prevent thermal throttling."
            ]
        },
        {
            "type": "bullet",
            "title": "Storage Protocols: SATA AHCI vs NVMe Architecture",
            "sub_title": "From Spinning Disk Legacy to Silicon-Optimized Queuing",
            "bullets": [
                "• Advanced Host Controller Interface (AHCI):",
                "    - Designed in the 1990s specifically for high-latency rotating magnetic hard drives.",
                "    - Bottlenecks: Single command queue with maximum depth of 32 commands; high software interrupt overhead (over 20,000 CPU cycles per I/O).",
                "• Non-Volatile Memory Express (NVMe):",
                "    - Architected from the ground up for low-latency solid-state NAND flash directly over PCIe lanes.",
                "    - Unrivaled Scalability: Up to 64,000 independent command queues, each capable of holding 64,000 commands.",
                "    - Multi-Core Parallelism: Each CPU core gets its own dedicated submission and completion queue pair, completely eliminating lock contention."
            ]
        },
        {
            "type": "bullet",
            "title": "Peripheral Bus Evolution: USB 2.0 to USB4 & Thunderbolt",
            "sub_title": "The Universal Interconnect: Bandwidth Scaling and Power Delivery",
            "bullets": [
                "• USB 2.0 (HighSpeed, 2000): 480 Mbps half-duplex; 4-wire interface; maximum 2.5W power delivery (5V @ 500mA).",
                "• USB 3.2 Gen 1 (SuperSpeed): 5 Gbps full-duplex with dedicated transmitter and receiver differential pairs.",
                "• USB 3.2 Gen 2x2: 20 Gbps using dual-lane Type-C cabling.",
                "• USB4 & Thunderbolt 4 / 5 Architecture:",
                "    - 40 Gbps to 80 Gbps bidirectional bandwidth.",
                "    - Protocol Tunneling: Simultaneously tunnels PCIe data, DisplayPort 2.1 video streams, and USB packets over a single reversible Type-C cable.",
                "    - USB Power Delivery (USB-PD 3.1): Up to 240 Watts (48V @ 5A), powering high-performance laptops and charging field agricultural equipment."
            ]
        },
        {
            "type": "bullet",
            "title": "Display Standards: DisplayPort vs HDMI vs Analog VGA",
            "sub_title": "Digital Packetized Video Streams and Color Depth",
            "bullets": [
                "• Analog Legacy: VGA (15-pin D-sub) transmitting continuous analog RGB voltages; prone to signal attenuation and EMI ghosting.",
                "• HDMI (High-Definition Multimedia Interface):",
                "    - Consumer audio/video standard; HDMI 2.1 supports up to 48 Gbps (Fixed Rate Link), enabling 4K @ 120 Hz and 8K @ 60 Hz.",
                "• DisplayPort (VESA DP 2.1):",
                "    - Professional computing standard; packetized micro-packet architecture (similar to PCIe and Ethernet); DP 2.1 supports up to 80 Gbps (UHBR 20).",
                "    - Multi-Stream Transport (MST): Allows daisy-chaining multiple independent monitors from a single physical port.",
                "• Color Precision: 8-bit color (16.7 million colors) vs 10-bit HDR (1.07 billion colors) for precision GIS satellite analysis."
            ]
        },
        {
            "type": "bullet",
            "title": "Motherboard Form Factors & Power Delivery (VRM)",
            "sub_title": "Chassis Geometry and Clean Multi-Phase DC Power",
            "bullets": [
                "• Motherboard Form Factors:",
                "    - ATX (Standard): 305 × 244 mm; up to 7 expansion slots, 4 RAM DIMMs; used in departmental servers and workstations.",
                "    - Micro-ATX (mATX): 244 × 244 mm; 4 expansion slots; cost-effective balance for computer lab desktops.",
                "    - Mini-ITX: 170 × 170 mm; 1 expansion slot; used in compact industrial PCs and automated tractor cab telemetry units.",
                "• Voltage Regulator Module (VRM):",
                "    - Step-down buck converter stepping down 12V DC from ATX power supply to ~1.0–1.3V required by modern CPU cores.",
                "    - Multi-Phase Architecture: Uses multiple parallel phases (PWM controller, MOSFETs, chokes, solid capacitors) to deliver clean, ripple-free current exceeding 150 Amps without overheating."
            ]
        },
        {
            "type": "bullet",
            "title": "Hardware Accelerators: NPUs & Systolic Arrays",
            "sub_title": "Dedicated Silicon for On-Device Machine Learning and AI",
            "bullets": [
                "• Neural Processing Unit (NPU) / Tensor Processing Unit (TPU):",
                "    - Specialized silicon execution blocks designed specifically for low-precision tensor operations (INT8, FP16, BF16).",
                "• Systolic Array Architecture: 2D grid of processing elements where data flows synchronously through cells, multiplying and accumulating without constantly reading/writing back to main memory registers.",
                "• Extreme Energy Efficiency: Delivers 10 to 45 TOPS (Trillions of Operations Per Second) at just 3 to 10 Watts.",
                "• Agricultural Application: Real-time computer vision on battery-powered edge drones at SUA, classifying crop disease lesions and weed species instantly in the field without cloud connectivity."
            ]
        },
        {
            "type": "bullet",
            "title": "Firmware Diagnostics: POST, Beep Codes & Diagnostic LEDs",
            "sub_title": "Troubleshooting Microcomputer Hardware Boot Failures",
            "bullets": [
                "• Power-On Self-Test (POST): Sequence of firmware diagnostic routines executed immediately upon applying electrical power.",
                "• Subsystem Verification Sequence:",
                "    1. CPU registers and ALU sanity check.",
                "    2. BIOS ROM checksum verification.",
                "    3. System timer and DMA controller initialization.",
                "    4. Primary DRAM detection and read/write parity verification.",
                "    5. Video display controller initialization and VRAM detection.",
                "• Diagnostic Signaling:",
                "    - Beep Codes: Internal piezo speaker signals failure before video is initialized (e.g., 1 long 2 short = video card failure).",
                "    - Motherboard Q-LEDs: Discrete LEDs (CPU, DRAM, VGA, BOOT) indicating which subsystem halted the boot process.",
                "    - Seven-Segment POST Code Displays: Displays hexadecimal status codes (e.g., code `00` = CPU failure; code `55` = Memory not installed)."
            ]
        },
        {
            "type": "bullet",
            "title": "Topic 2: Key Takeaways & Synthesis Matrix",
            "sub_title": "Essential Hardware Principles for Technical Mastery",
            "bullets": [
                "• CPU Architecture: CU orchestrates; ALU computes; registers provide ultra-fast operand buffering.",
                "• Instruction Pipeline: Fetch (PC to MAR, memory to MDR, MDR to IR, PC increment) → Decode → Execute.",
                "• Memory Hierarchy: L1/L2/L3 SRAM Cache (fastest, costly) → DRAM System Memory → NVMe/SATA SSD → Magnetic HDD.",
                "• Bus Physics: Address Bus determines maximum memory capacity (2<sup>n</sup>); Data Bus width determines word size.",
                "• Workstation Differentiators: ECC memory prevents silent corruption; ISV workstation GPUs guarantee geometric precision.",
                "• Storage Mechanics: HDDs bounded by mechanical physics (seek + rotation); SSDs bounded by NAND flash controllers and bus protocol."
            ]
        },
        {
            "type": "bullet",
            "title": "Review Quiz & Knowledge Check",
            "sub_title": "Self-Testing Key Architectural Principles",
            "bullets": [
                "1. If a microprocessor has a 36-bit address bus, what is the maximum physical RAM it can directly address? (Ans: 64 GiB).",
                "2. Why does Dynamic RAM require periodic electrical refresh cycles, whereas Static RAM does not?",
                "3. Explain the function of the Program Counter (PC) during the instruction fetch phase.",
                "4. What happens when an NVMe SSD experiences severe thermal throttling during sustained sequential writes?",
                "5. Why is ECC memory mandatory for scientific GIS servers but considered unnecessary for consumer gaming laptops?"
            ]
        },
        {
            "type": "bullet",
            "title": "Reading Assignments & Homework Notice",
            "sub_title": "Preparation for Next Lecture & Continuous Assessment",
            "bullets": [
                "• Required Readings:",
                "    - Smith, J. L., Wang, S., & Mortati, J. - Information Systems for Business and Beyond (2019), Chapter 2: Hardware. https://opentextbook.site/informationsystems2019/chapter/chapter-2-hardware-information-systems-introduction/",
                "    - Vermaat et al. - Discovering Computers: Digital Technology, Data, and Devices (16th ed.). Cengage. https://faculty.cengage.com/works/9781337285100",
                "• Homework Assignment 2 Notice:",
                "    - Available on SUA Moodle / Assignment directory: `BIT_111_Assignment_2.pdf`.",
                "    - Total Allocation: 100 Marks (Covers hardware concepts, storage, and workstation selection).",
                "    - Submission Deadline: End of Week 4 by 17:00 EAT.",
                "• Next Lecture Preview: Topic 3 — Personal Computer (PC) Security Controls (Firmware, TPM, BitLocker, Access Models)."
            ]
        }
    ]

# -------------------------------------------------------------
# TOPIC 3 SLIDES DATA
# -------------------------------------------------------------
def get_topic_3_slides():
    return [
        {
            "type": "bullet",
            "title": "Topic 3: Lecture Outline & Learning Roadmap",
            "sub_title": "Personal Computer Security Controls, Firmware & Access Models (Coverage: 3.1, 3.2, 3.3)",
            "bullets": [
                "• Section 3.1: Hard Disk & Storage-Level Security Controls",
                "    - ATA security feature set: User vs Master passwords; Self-Encrypting Drives (SED / Opal)",
                "    - Whole Disk Encryption (WDE): BitLocker, LUKS, FileVault; Key management hierarchies",
                "    - Data sanitization standards: NIST SP 800-88 Rev. 2 (Clear, Purge, Destroy); cryptographic erase",
                "• Section 3.2: BIOS & UEFI Firmware Security Controls",
                "    - Legacy BIOS limitations vs UEFI architecture (GPT, 64-bit mode, modular drivers)",
                "    - Firmware password hierarchy: Supervisor vs User/Power-On passwords",
                "    - UEFI Secure Boot Architecture: PK, KEK, db, dbx; The cryptographic chain of trust",
                "    - Trusted Platform Module (TPM 2.0): EK, SRK, PCR registers, Measured Boot & Attestation",
                "• Section 3.3: Operating System Login Passwords & User Access Controls",
                "    - Authentication factors: Something you know, have, and are (Biometrics FAR/FRR)",
                "    - Password safety, secure storage, and hashing concepts",
                "    - Access Control Models: Discretionary (DAC - POSIX), Mandatory (MAC - SELinux), and RBAC"
            ],
            "callout": {
                "title": "SECURITY PRINCIPLE",
                "body": "Security is a system of defense-in-depth: protecting hardware, firmware, storage encryption, and OS access privileges in cohesive layers."
            }
        },
        {
            "type": "bullet",
            "title": "Topic 3: Intended Learning Outcomes (ILOs)",
            "sub_title": "Core Security Competencies for Undergraduate Students",
            "bullets": [
                "• Differentiate between storage-level ATA passwords, Whole Disk Encryption, and OS login passwords.",
                "• Analyze UEFI Secure Boot key hierarchies (PK, KEK, db, dbx) and explain the verified boot chain.",
                "• Explain the cryptographic role of TPM 2.0 in Measured Boot and BitLocker volume key sealing.",
                "• Recommend password and account-protection practices for personal and university devices.",
                "• Describe appropriate NIST SP 800-88 media-sanitization choices at a conceptual level.",
                "• Apply Discretionary (DAC) and Mandatory (MAC) access control models in Windows and Linux environments.",
                "• Design a hardened microcomputer workstation deployment for confidential university examinations."
            ]
        },
        {
            "type": "figure",
            "title": "Multi-Layered Personal Computer Security Stack",
            "img": "fig3_1_pc_security_layers.png",
            "caption": "The multi-layered PC security defense model from physical chassis to application access controls.",
            "bullets": [
                "• Layer 1 - Physical & Storage Security: Chassis locks, Kensington cables, ATA disk locks, Full Disk Encryption.",
                "• Layer 2 - Firmware & Hardware Root of Trust: UEFI Supervisor passwords, Secure Boot, TPM 2.0 PCR sealing.",
                "• Layer 3 - Operating System Security: Kernel integrity, secure login, PAM authentication, Least Privilege access.",
                "• Layer 4 - Access Control & Encryption: Discretionary Access Control (POSIX permissions), MAC, encrypted filesystems."
            ]
        },
        {
            "type": "bullet",
            "title": "Storage Security: ATA Security Feature Set",
            "sub_title": "Drive-Level Firmware Locking and Self-Encrypting Drives",
            "bullets": [
                "• ATA Storage Security Commands: Built into drive controller firmware (independent of operating system).",
                "• Password Hierarchy:",
                "    - User Password: Required to unlock drive for normal read/write operations at system boot.",
                "    - Master Password: Set by system administrators; allows drive unlocking or secure data erasure.",
                "• Security Modes: High Security (User password can be cleared by Master password) vs Maximum Security (User password cannot be cleared; drive must be Secure Erased).",
                "• Critical Vulnerability: Standard ATA passwords transmit password hashes in plaintext across the SATA/NVMe bus; vulnerable to hardware bus sniffing.",
                "• Self-Encrypting Drives (SED): Opal standard; drive hardware automatically encrypts all written data using internal AES engine; passwords unlock decryption key."
            ]
        },
        {
            "type": "bullet",
            "title": "Whole Disk Encryption (WDE): BitLocker & LUKS",
            "sub_title": "Logical Sector-Level Cryptography Protecting Data at Rest",
            "bullets": [
                "• The Physical Theft Threat: If a laptop is stolen, an attacker can extract the drive and mount it in another PC, completely bypassing Windows/Linux login passwords.",
                "• Whole Disk Encryption Architecture:",
                "    - Encrypts every single sector on the storage volume (operating system files, swap files, user documents).",
                "    - Uses high-speed hardware-accelerated AES-XTS (128 or 256 bits).",
                "• Microsoft BitLocker Key Architecture:",
                "    - Full Volume Encryption Key (FVEK): Encrypts actual disk sectors.",
                "    - Volume Master Key (VMK): Encrypts the FVEK; sealed inside the TPM chip.",
                "    - TPM Unsealing: TPM releases VMK only if Platform Configuration Registers (PCRs) match authorized hardware state.",
                "• Linux dm-crypt / LUKS: Linux Unified Key Setup providing multi-keyslot encryption for root filesystems."
            ]
        },
        {
            "type": "bullet",
            "title": "Data Sanitization Standards (NIST SP 800-88 Rev. 2)",
            "sub_title": "Clear, Purge, and Destroy: Preventing Post-Decommissioning Leakage",
            "bullets": [
                "• The Residual Data Threat: Simple OS file deletion or formatting merely clears filesystem metadata; raw data remains recoverable.",
                "• NIST SP 800-88 Rev. 2 Categories:",
                "    - 1. Clear: Overwriting storage spaces with logical data patterns via standard read/write commands (e.g., single-pass overwrite for HDDs).",
                "    - 2. Purge: Applying physical or cryptographic techniques that make data recovery impossible even with laboratory equipment (ATA Secure Erase, Cryptographic Erase).",
                "    - 3. Destroy: Physical destruction of media (degaussing for magnetic media, shredding, incineration, chemical disintegration).",
                "• The SSD Overwrite Problem: Traditional multi-pass overwrites (DoD 5220.22-M) fail on SSDs due to wear-leveling spare blocks. Cryptographic Erase (destroying encryption key) is the recognized modern standard."
            ]
        },
        {
            "type": "bullet",
            "title": "Firmware Security: Legacy BIOS vs Modern UEFI",
            "sub_title": "The Evolution from 16-bit Real Mode to 64-bit Modular Architecture",
            "bullets": [
                "• Legacy BIOS (Basic Input/Output System):",
                "    - 16-bit real mode execution; limited to 1 MB addressable memory space.",
                "    - Master Boot Record (MBR) partition table: Maximum 2.0 TB drive capacity, max 4 primary partitions.",
                "    - No built-in cryptographic signature verification; highly vulnerable to bootkits (malicious MBR overwrites).",
                "• UEFI (Unified Extensible Firmware Interface):",
                "    - 32-bit or 64-bit protected mode; direct access to full system RAM.",
                "    - GUID Partition Table (GPT): Up to 9.4 Zettabytes volume capacity, 128 primary partitions.",
                "    - Modular architecture with network stack, graphical setup interface, and UEFI Secure Boot."
            ]
        },
        {
            "type": "bullet",
            "title": "Firmware Password Controls & Physical Tampering",
            "sub_title": "Supervisor Passwords, Boot Order Locking & CMOS Physics",
            "bullets": [
                "• BIOS/UEFI Supervisor (Administrator) Password:",
                "    - Restricts unauthorized access to firmware setup utility; prevents tampering with boot sequence, virtualization, or Secure Boot settings.",
                "• User / Power-On Password:",
                "    - Demands authentication before the firmware initiates hardware POST or boots the operating system.",
                "• Physical Tampering Defenses:",
                "    - Legacy desktop PCs could be bypassed by removing the CR2032 coin-cell battery or shorting the CMOS clear jumper.",
                "    - Modern enterprise laptops store firmware hashes and passwords in non-volatile flash / security chips resistant to battery removal.",
                "    - Chassis Intrusion Switches: Motherboard sensor logs an alert if the physical computer chassis has been opened."
            ]
        },
        {
            "type": "bullet",
            "title": "UEFI Secure Boot Architecture & Key Hierarchy",
            "sub_title": "Establishing an Unbroken Cryptographic Chain of Trust",
            "bullets": [
                "• Core Objective: Guarantees that only cryptographically signed and authenticated bootloaders, drivers, and OS kernels can execute at boot time.",
                "• Secure Boot Key Hierarchy:",
                "    - 1. Platform Key (PK): Root of trust held by OEM/hardware manufacturer; controls access to KEK.",
                "    - 2. Key Exchange Key (KEK): Authorizes updates to signature databases (db / dbx). Held by Microsoft and OS vendors.",
                "    - 3. Allowed Signature Database (db): Contains trusted certificates, SHA-256 hashes of authorized bootloaders and EFI binaries.",
                "    - 4. Forbidden Signature Database (dbx): Revocation list containing compromised binaries and revoked signing keys.",
                "• The 'Shim' Bootloader: Lightweight bootloader signed by Microsoft 3rd Party UEFI CA that verifies the GRUB2 bootloader and Linux kernel."
            ]
        },
        {
            "type": "bullet",
            "title": "The Trusted Platform Module (TPM 2.0)",
            "sub_title": "Hardware Root of Trust, Cryptographic Co-Processor & Measured Boot",
            "bullets": [
                "• Definition: Dedicated tamper-resistant cryptographic microchip (discrete dTPM or firmware fTPM) soldered to the motherboard.",
                "• Core Cryptographic Engines: Hardware True Random Number Generator (TRNG), RSA-2048 and ECC key generation, SHA-256 hashing engine.",
                "• Internal Key Infrastructure:",
                "    - Endorsement Key (EK): Permanently burnt into silicon during manufacturing; unique device identifier.",
                "    - Storage Root Key (SRK): Master key protecting user cryptographic keys.",
                "• Platform Configuration Registers (PCRs 0–23):",
                "    - Measured Boot: Each boot component (UEFI code, hardware configuration, bootloader, kernel) hashes the subsequent stage and extends PCRs.",
                "    - Key Sealing: Data is sealed against specific PCR values; if firmware or bootloader is altered, PCRs will not match, and TPM refuses to unseal encryption keys."
            ]
        },
        {
            "type": "bullet",
            "title": "Authentication Principles & Multi-Factor Models",
            "sub_title": "Something You Know, Have, and Are",
            "bullets": [
                "• Authentication: The formal process of verifying an entity's claimed identity.",
                "• The Three Classical Factors:",
                "    - 1. Knowledge Factor (Something you know): Passwords, passphrases, PIN numbers, security questions.",
                "    - 2. Possession Factor (Something you have): Hardware security keys (YubiKey / FIDO2), smartcards, TOTP authenticator app tokens.",
                "    - 3. Inherence Factor (Something you are): Biometrics — fingerprints, facial geometry, iris patterns, retinal scans.",
                "• Multi-Factor Authentication (MFA):",
                "    - Requires presentation of two or more *different* authentication categories.",
                "    - Presenting a password and a PIN is NOT MFA (both are knowledge factors).",
                "    - Combining a password (Knowledge) with a FIDO2 token (Possession) provides genuine MFA, eliminating >99% of automated credential theft attacks."
            ]
        },
        {
            "type": "bullet",
            "title": "Creating and Protecting Strong Passwords",
            "sub_title": "Practical account-security habits",
            "bullets": [
                "• Use a long, unique passphrase for each important account.",
                "• Avoid names, birthdays, common phrases, and passwords reused across services.",
                "• Use a reputable password manager to create and store unique credentials.",
                "• Enable multi-factor authentication when it is available.",
                "• Never share passwords in messages or store them in an unprotected document."
            ]
        },
        {
            "type": "bullet",
            "title": "Cryptographic Password Hashing in Operating Systems",
            "sub_title": "From Insecure MD5 to Salted, Slow-Key Derivation (Argon2id)",
            "bullets": [
                "• Password Storage Imperative: Operating systems NEVER store user passwords in plaintext; only cryptographic hashes are stored.",
                "• The Role of Salt: A unique random string (e.g., 16 bytes) appended to password before hashing; defeats precomputed Rainbow Table attacks.",
                "• Linux `/etc/shadow` Architecture: `$id$salt$hashed_value`:",
                "    - `$1$`: MD5 (legacy, broken); `$5$`: SHA-256; `$6$`: SHA-512; `$y$`: yescrypt.",
                "• Modern Slow Key Derivation Functions:",
                "    - bcrypt, PBKDF2, scrypt, and Argon2id (Password Hashing Competition winner).",
                "    - Memory-hard and computationally parameterized: Forces GPU cracking rigs to allocate large RAM blocks per guess, neutralizing brute-force parallelization."
            ]
        },
        {
            "type": "bullet",
            "title": "Access Control Models: Discretionary vs Mandatory",
            "sub_title": "DAC, MAC, and Role-Based Access Control (RBAC)",
            "bullets": [
                "• Discretionary Access Control (DAC):",
                "    - Resource owner has full discretion to grant or revoke access permissions to other users.",
                "    - Standard model in Windows NTFS permissions and Linux POSIX permissions (`chmod`, `chown`).",
                "    - Limitation: Vulnerable to Trojan horses executing with owner privileges.",
                "• Mandatory Access Control (MAC):",
                "    - Central security policy enforced by operating system kernel based on security clearances and object sensitivity labels.",
                "    - Users/owners CANNOT override policy (e.g., SELinux - Security-Enhanced Linux, AppArmor).",
                "• Role-Based Access Control (RBAC):",
                "    - Permissions assigned to organizational roles (e.g., 'SUA Exam Officer', 'Lecturer', 'Student'), and users assigned to roles."
            ]
        },
        {
            "type": "bullet",
            "title": "Linux Permissions Architecture & Hardening",
            "sub_title": "Octal Representation, Special Bits, and Sudoers Governance",
            "bullets": [
                "• Permission Triplet: Owner (u), Group (g), Others (o) across Read (r=4), Write (w=2), Execute (x=1):",
                "    - `chmod 755 file.sh` → `rwxr-xr-x` (Owner can read/write/exec; others read/exec).",
                "    - `chmod 640 data.db` → `rw-r-----` (Owner can read/write; group can read; others denied).",
                "• Special Permission Bits:",
                "    - SetUID (4000): Process runs with file owner privileges (e.g., `/usr/bin/passwd`).",
                "    - SetGID (2000): Files created inherit directory's group ownership.",
                "    - Sticky Bit (1000): Only file owner can delete file within directory (e.g., `/tmp`, `chmod 1777 /tmp`).",
                "• Principle of Least Privilege: Administrative tasks executed via `sudo` with exact binary paths logged in `/etc/sudoers`."
            ]
        },
        {
            "type": "bullet",
            "title": "Biometric Authentication: Technical Metrics",
            "sub_title": "Balancing Security and Usability in Field Systems",
            "bullets": [
                "• Biometric Matching Engine: Compares captured live sample with enrolled mathematical template.",
                "• False Acceptance Rate (FAR): Probability that the biometric system incorrectly authorizes an unauthorized imposter (Type II Error - Security failure).",
                "• False Rejection Rate (FRR): Probability that the system incorrectly rejects an authentic registered user (Type I Error - Usability failure).",
                "• Crossover Error Rate (CER) / Equal Error Rate (EER): The operating threshold where FAR equals FRR. Lower CER indicates superior sensor accuracy.",
                "• Liveness Detection: Capacitive pulse sensing, infrared vein detection, and thermal imaging preventing presentation attacks (silicone molds, photographs)."
            ]
        },
        {
            "type": "bullet",
            "title": "Password Hashing Defenses: Salt and Pepper Architecture",
            "sub_title": "Mitigating Offline Dictionary and Rainbow Table Attacks",
            "bullets": [
                "• The Rainbow Table Threat: Precomputed lookup tables containing trillions of pre-hashed passwords, enabling instant hash inversion.",
                "• Cryptographic Salt:",
                "    - A unique, cryptographically random string (minimum 16 bytes / 128 bits) generated per user and stored alongside the password hash in the database.",
                "    - Eliminates Rainbow Tables: Attackers must recompute tables specifically for each individual user's salt.",
                "    - Disguises identical passwords: Two users with the exact same password produce completely distinct hashes.",
                "• Cryptographic Pepper:",
                "    - A secret server-side key concatenated with the password before hashing, stored in an isolated Hardware Security Module (HSM) or environment variable away from the database.",
                "    - If the user database is dumped, hashes cannot be cracked without the secret pepper."
            ]
        },
        {
            "type": "bullet",
            "title": "Slow Key Derivation Functions: Argon2id, bcrypt & PBKDF2",
            "sub_title": "Memory-Hard Functions That Neutralize GPU/ASIC Cracking",
            "bullets": [
                "• Why SHA-256 and MD5 Fail for Passwords: Fast general-purpose hashing functions allow specialized GPU clusters to test over 100 billion guesses per second.",
                "• Adaptive Slow Hashing Functions:",
                "    - Parameterized Work Factor: Work factor (cost / iterations) can be increased over time as hardware advances without invalidating existing passwords.",
                "    - bcrypt (Niels Provos & David Mazières): Based on Blowfish key schedule; incorporates 128-bit salt and configurable cost factor 2<sup>cost</sup>.",
                "    - PBKDF2 (Password-Based Key Derivation Function 2): Applies HMAC pseudorandom function repeatedly (typically 600,000+ iterations for SHA-256).",
                "    - Argon2id: Winner of the Password Hashing Competition; memory-hard algorithm that forces cracker hardware to allocate large RAM blocks per guess, making massive GPU parallelization economically and physically impossible."
            ]
        },
        {
            "type": "bullet",
            "title": "Windows Security: SAM Database & LSASS Process",
            "sub_title": "Local Account Storage, Password Hashes, and Memory Security",
            "bullets": [
                "• Security Account Manager (SAM):",
                "    - Registry hive stored in `C:\\Windows\\System32\\config\\SAM` storing local user accounts and NTLM password hashes.",
                "    - Locked exclusively by the kernel during OS runtime; cannot be opened or copied by standard user processes.",
                "    - Protected with Syskey / System startup key encryption.",
                "• Local Security Authority Subsystem Service (`lsass.exe`):",
                "    - Core Windows process enforcing security policies, verifying user credentials, and handling Kerberos and NTLM authentication tickets.",
                "    - Credential Dumping Threat: Attackers utilizing tools like Mimikatz inject into `lsass.exe` memory to dump plaintext passwords and Kerberos tickets.",
                "    - Modern Mitigation: Windows Credential Guard runs LSASS in an isolated virtualized container (VBS - Virtualization-Based Security) inaccessible to the host OS kernel."
            ]
        },
        {
            "type": "bullet",
            "title": "Windows User Account Control (UAC) & Integrity Levels",
            "sub_title": "Enforcing Least Privilege in Desktop Client Environments",
            "bullets": [
                "• User Account Control (UAC): Prevents unauthorized system modifications by running administrative accounts with standard user privileges by default.",
                "• Dual Access Tokens: When an administrator logs on, Windows issues two security tokens: a filtered standard user token and a full administrator token.",
                "• UAC Elevation Prompt: Switches to the Secure Desktop (isolated from malware hooks), requesting explicit human consent or credential entry.",
                "• Windows Mandatory Integrity Levels (MIC):",
                "    - Untrusted / Low: Sandboxed web browser processes (Edge, Chrome tabs).",
                "    - Medium: Standard interactive user applications and documents.",
                "    - High: Elevated administrative processes.",
                "    - System: Operating system kernel and critical drivers.",
                "    - Rule: A process at a lower integrity level CANNOT write to or inject code into an object at a higher integrity level."
            ]
        },
        {
            "type": "bullet",
            "title": "Enterprise Authentication: Kerberos Protocol",
            "sub_title": "Ticket-Based Single Sign-On in Active Directory Domains",
            "bullets": [
                "• Kerberos (RFC 4120): The default network authentication protocol in Windows Active Directory and enterprise Linux domains.",
                "• Key Distribution Center (KDC): Runs on Domain Controller, consisting of Authentication Server (AS) and Ticket-Granting Server (TGS).",
                "• Step-by-Step Ticket Exchange Sequence:",
                "    1. AS-REQ / AS-REP: User authenticates; KDC returns a Ticket-Granting Ticket (TGT) encrypted with KDC secret key.",
                "    2. TGS-REQ / TGS-REP: User presents TGT to request access to a specific service (e.g., SUA file share); KDC issues a Service Ticket.",
                "    3. AP-REQ: User presents Service Ticket to target server; server verifies ticket without ever seeing the user's password.",
                "• Advantages: Passwords are NEVER transmitted across the network; mutual authentication prevents server spoofing; tickets expire automatically."
            ]
        },
        {
            "type": "bullet",
            "title": "Role-Based Access Control (RBAC) Architecture",
            "sub_title": "Enterprise Permission Management for University Systems",
            "bullets": [
                "• Core Philosophy: Access permissions are assigned to organizational job roles rather than directly to individual user accounts.",
                "• Three Core Rules:",
                "    - 1. Role Assignment: A subject can execute a transaction only if assigned an authorized role.",
                "    - 2. Role Authorization: A subject's active role must be authorized for that subject.",
                "    - 3. Permission Authorization: A subject can execute a transaction only if the transaction is authorized for the subject's active role.",
                "• Role Hierarchy in SUA Academic Systems:",
                "    - `Student`: Read own grades, submit assignments, browse course materials.",
                "    - `Lecturer`: Enter/edit continuous assessment marks for assigned courses, upload compendia.",
                "    - `Head of Department (HOD)`: Approve marks, assign course teaching allocations.",
                "    - `Examination Officer`: Decrypt examination master files, lock final semester results."
            ]
        },
        {
            "type": "bullet",
            "title": "Linux Pluggable Authentication Modules (PAM)",
            "sub_title": "Modular Framework Decoupling Applications from Authentication",
            "bullets": [
                "• PAM Architecture: Provides a centralized API allowing system programs (`login`, `sshd`, `sudo`, `su`) to authenticate users via pluggable shared libraries without modifying application source code.",
                "• Four Management Groups in `/etc/pam.d/`:",
                "    - `auth`: Verifies user identity (checks password, biometrics, or hardware token).",
                "    - `account`: Enforces account restrictions (password expiration, login hour limits, access bans).",
                "    - `password`: Updates user authentication credentials (enforcing complexity rules via `pam_pwquality`).",
                "    - `session`: Manages user environment setup and teardown (mounting home directories, logging login audit records).",
                "• Control Flags: `required` (must succeed, continues through stack), `requisite` (must succeed, fails immediately), `sufficient` (success grants access if no prior required failed), `optional`."
            ]
        },
        {
            "type": "bullet",
            "title": "Physical Port Security & DMA Attack Mitigations",
            "sub_title": "Hardening External Expansion Buses Against Hardware Exploits",
            "bullets": [
                "• Physical USB Threats: BadUSB (microcontroller simulating human keyboard typing keystrokes at 1,000 WPM), Rubber Ducky, USB killer devices injecting high-voltage discharge into data lines.",
                "• Direct Memory Access (DMA) Attacks:",
                "    - High-speed expansion interfaces (Thunderbolt, PCIe, FireWire) possess direct access to system DRAM without CPU mediation.",
                "    - Threat: An attacker connects a PCIe hardware sniffer to read encryption keys directly out of RAM within seconds.",
                "• Hardware Defense - Kernel DMA Protection & IOMMU:",
                "    - Input-Output Memory Management Unit (IOMMU - Intel VT-d / AMD-Vi): Remaps device memory accesses through dedicated page tables.",
                "    - Blocks unauthorized DMA: High-speed peripherals cannot access unallocated system memory or kernel regions, neutralizing physical Thunderbolt snooping attacks."
            ]
        },
        {
            "type": "bullet",
            "title": "Remote Attestation via TPM 2.0",
            "sub_title": "Cryptographic Verification of System Integrity Across Networks",
            "bullets": [
                "• The Integrity Challenge: How can a centralized university management server know that a remote field laptop at SUA Mazimbu has not been compromised by a rootkit?",
                "• Remote Attestation Sequence:",
                "    1. Remote laptop boots: Firmware, bootloader, kernel, and security drivers are measured and hashes extended into TPM PCRs.",
                "    2. Central Attestation Server generates a cryptographic Nonce (random challenge string) to prevent replay attacks.",
                "    3. Laptop TPM quotes PCR contents: Combines PCR hashes with the nonce and digitally signs the payload using its private Attestation Identity Key (AIK).",
                "    4. Server verifies the AIK signature using the laptop's public certificate and compares PCR values against a database of known-good 'Gold Masters'.",
                "    5. Access Decision: If PCRs match, network access is granted; if unauthorized code was executed, access is quarantined immediately."
            ]
        },
        {
            "type": "bullet",
            "title": "Secure Boot Key Revocation: Managing the dbx",
            "sub_title": "Responding to Vulnerable Bootloaders and Stolen Certificates",
            "bullets": [
                "• The Vulnerability Window: If a legitimate signed bootloader is found to have a security flaw (e.g., 'BootHole' CVE-2020-10713 in GRUB2), attackers can use that vulnerable binary to bypass Secure Boot.",
                "• Forbidden Signatures Database (`dbx`):",
                "    - A cryptographically signed blocklist embedded in UEFI NVRAM containing SHA-256 hashes of compromised EFI executables and revoked vendor signing keys.",
                "    - If an EFI binary's hash is listed in `dbx`, UEFI firmware halts execution immediately, even if the file is signed with a valid key in `db`.",
                "• Update Distribution: `dbx` updates are signed with the vendor's KEK and delivered through operating system security updates (Windows Update / Linux `fwupd`)."
            ]
        },
        {
            "type": "bullet",
            "title": "Enterprise Key Escrow: Managing BitLocker Recovery Keys",
            "sub_title": "Preventing Catastrophic Lockout in Corporate Deployments",
            "bullets": [
                "• The Recovery Dilemma: If motherboard hardware is replaced, firmware is updated, or TPM state is cleared, BitLocker locks the drive and demands the 48-digit numerical Recovery Key.",
                "• Enterprise Key Escrow Architecture:",
                "    - In an enterprise environment (SUA administration), recovery keys must NEVER be left to individual end-users to record on paper.",
                "    - Active Directory Domain Services (AD DS): BitLocker policies configured via GPO automatically back up the 48-digit recovery password and TPM owner information into AD computer objects.",
                "    - Cloud Escrow (Microsoft Intune / Entra ID): Recovery keys vaulted securely in encrypted cloud directories accessible only to authorized IT administrators via multi-factor authentication.",
                "    - Self-Service Portals: Allows authenticated users to look up their specific device recovery key following identity verification."
            ]
        },
        {
            "type": "bullet",
            "title": "Physical Media Destruction: Degaussing & Disintegration",
            "sub_title": "NIST SP 800-88 Rev. 2 'Destroy' guidance for end-of-life assets",
            "bullets": [
                "• When Logical Sanitization is Insufficient: Decommissioning drives containing classified national research, examination master keys, or personal health records.",
                "• Degaussing (Magnetic Media Only):",
                "    - Subjecting magnetic HDDs or tapes to an intense magnetic pulse (measured in Oersteds / Gauss, typically > 10,000 Gauss).",
                "    - Eliminates magnetic domain alignments permanently and destroys factory servo tracks, rendering the drive completely inoperable and unreadable.",
                "    - WARNING: Degaussing has ZERO effect on Solid-State Drives (NAND flash stores charge, not magnetic polarity!).",
                "• Disintegration & Shredding (SSD & Media Universal):",
                "    - Physical mechanical shredders grinding drive electronics down into microscopic fragments (NIST specifies particle size ≤ 2 mm for SSD chips).",
                "    - Ensures that no single silicon NAND die remains intact."
            ]
        },
        {
            "type": "bullet",
            "title": "Topic 3: Key Takeaways & Synthesis Matrix",
            "sub_title": "Summary of PC Security Controls for Examination Mastery",
            "bullets": [
                "• Storage Security: ATA passwords protect hardware controllers; WDE (BitLocker/LUKS) protects logical data at rest via TPM key sealing.",
                "• UEFI vs BIOS: UEFI provides 64-bit protected execution, GPT partition table (>2TB), and cryptographic Secure Boot.",
                "• Secure Boot Chain: Platform Key (PK) → Key Exchange Key (KEK) → Allowed Database (db) authenticates bootloader and kernel.",
                "• TPM 2.0: Hardware Root of Trust providing Platform Configuration Registers (PCRs) for Measured Boot and cryptographic unsealing.",
                "• Password Security: Use long, unique passwords and enable multi-factor authentication."
                "• Access Control: DAC grants discretionary owner control; MAC (SELinux) enforces kernel-level mandatory labels; RBAC maps to job roles."
            ]
        },
        {
            "type": "bullet",
            "title": "Review Quiz & Knowledge Check",
            "sub_title": "Self-Testing Key Security Principles",
            "bullets": [
                "1. If a laptop with an unencrypted drive and a Windows login password is stolen, how can an attacker read the files?",
                "2. What is the fundamental function of the Forbidden Signatures Database (dbx) in UEFI Secure Boot?",
                "3. Name two practices that make an account harder to access without authorization.",
                "4. Differentiate between Discretionary Access Control (DAC) and Mandatory Access Control (MAC).",
                "5. Why does modern SSD data sanitization rely on Cryptographic Erase rather than multi-pass magnetic overwriting?"
            ]
        },
        {
            "type": "bullet",
            "title": "Reading Assignments & Homework Notice",
            "sub_title": "Preparation for Next Lecture & Continuous Assessment",
            "bullets": [
                "• Required Readings:",
                "    - National Institute of Standards and Technology. (2024). The NIST Cybersecurity Framework (CSF) 2.0. https://doi.org/10.6028/NIST.CSWP.29",
                "    - Chandramouli, R., & Hibbard, E. (2025). Guidelines for Media Sanitization (NIST SP 800-88 Rev. 2). https://doi.org/10.6028/NIST.SP.800-88r2",
                "• Homework Assignment 3 Notice:",
                "    - Available on SUA Moodle / Assignment directory: `BIT_111_Assignment_3.pdf`.",
                "    - Total Allocation: 100 Marks (Covers storage security, account protection, and exam-lab hardening).",
                "    - Submission Deadline: End of Week 6 by 17:00 EAT.",
                "• Next Lecture Preview: Topic 4 — Functions and Types of Operating Systems (DOS, Linux, Windows, Scheduling)."
            ]
        }
    ]
