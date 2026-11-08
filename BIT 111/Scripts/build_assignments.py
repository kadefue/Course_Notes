#!/usr/bin/env python3
"""
build_assignments.py
Generates the 6 comprehensive takehome homework assignments for:
BIT 111: MICROCOMPUTERS AND APPLICATIONS
Department of Informatics and Information Technology (DIIT),
Sokoine University of Agriculture (SUA), Morogoro, Tanzania.

Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Assessment note: the course assessment scheme is subject to confirmation by the instructor.

Each assignment is a multi-page academic document with:
- Part A: Theoretical and foundational concepts (25 marks)
- Part B: Conceptual and technical applications (35 marks)
- Part C: Applied agricultural and enterprise scenarios (40 marks)
Total: 100 Marks per Assignment.
"""

import os
import sys

LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak, HRFlowable
from compendium_base import (
    NumberedCanvas, get_custom_stylesheet,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_WHITE, COLOR_TEXT, COLOR_SUA_GREEN
)

ASSIGNMENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Assignment"))
os.makedirs(ASSIGNMENT_DIR, exist_ok=True)

def render_assignment_pdf(filename, story):
    out_path = os.path.join(ASSIGNMENT_DIR, filename)
    doc = SimpleDocTemplate(
        out_path,
        pagesize=letter,
        leftMargin=46,
        rightMargin=46,
        topMargin=50,
        bottomMargin=46
    )
    doc.build(story, canvasmaker=lambda *args, **kwargs: NumberedCanvas(*args, doc_title="BIT 111 Takehome Assignment", **kwargs))
    print(f"[Success] Generated {out_path} ({os.path.getsize(out_path)} bytes)")
    return out_path

def create_assignment_header(asn_num, topic_num, title, topics_covered, due_info):
    styles = get_custom_stylesheet()
    header_data = [
        [Paragraph("SOKOINE UNIVERSITY OF AGRICULTURE", styles['CoverUniv'])],
        [Paragraph("School of Engineering and Technology / College of Natural and Applied Sciences", styles['CoverDept'])],
        [Paragraph("Department of Informatics and Information Technology (DIIT)", styles['CoverDept'])],
        [Spacer(1, 4)],
        [Paragraph("BIT 111: MICROCOMPUTERS AND APPLICATIONS", styles['CourseCode'])],
        [Paragraph(f"TAKEHOME HOMEWORK ASSIGNMENT {asn_num} (TOPIC {topic_num})", styles['CourseTitle'])],
        [Paragraph(f"<b>Theme:</b> {title.upper()}", styles['CalloutTitle'])],
        [Paragraph(
            f"<b>Course Instructor:</b> Madam Bertha Msuliche Lebalwa (MSc)<br/>"
            f"<b>Curriculum Coverage:</b> {topics_covered}<br/>"
            f"<b>Assessment Weight:</b> Coursework Component (Official Scheme: Assignments 5%, Tests 15%, Practical Report 10%, Practical Test 30%, UE 40% - subject to instructor review)<br/>"
            f"<b>Submission Deadline:</b> {due_info} | <b>Total Allocation:</b> 100 Marks",
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
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    return tbl

def create_instructions_box():
    styles = get_custom_stylesheet()
    text = (
        "<b>INSTRUCTIONS TO CANDIDATES:</b><br/>"
        "1. This assignment must be solved individually. Plagiarism, peer copying, or unreferenced AI generation will result in an automatic score of zero and disciplinary reporting under SUA Examination Regulations.<br/>"
        "2. Answer <b>ALL questions</b> in Sections A, B, and C. Allocate your effort according to the mark allocations shown in brackets.<br/>"
        "3. Support your explanations with clear examples, labeled diagrams, or command syntax where requested.<br/>"
        "4. Use spreadsheet formulas only where requested in the spreadsheet assignment; no other numerical calculations are required.<br/>"
        "5. Submit your completed work as a clean, stapled technical report or upload the single consolidated PDF to the SUA Virtual Learning Environment (Moodle) before the deadline."
    )
    tbl = Table([[Paragraph(text, styles['CalloutText'])]], colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#fef2f2")),
        ('BOX', (0, 0), (-1, -1), 1.0, colors.HexColor("#dc2626")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    return tbl

# -------------------------------------------------------------
# ASSIGNMENT 1: INTRODUCTION TO COMPUTERS
# -------------------------------------------------------------
def build_assignment_1():
    styles = get_custom_stylesheet()
    story = []
    story.append(create_assignment_header(
        1, 1, "Introduction to Computers, Generations, Pioneers & Classification",
        "Subtopic 1.1 (Computer Generations), Subtopic 1.2 (History & Pioneers), Subtopic 1.3 (Classifications)",
        "End of Week 2 by 17:00 EAT"
    ))
    story.append(Spacer(1, 8))
    story.append(create_instructions_box())
    story.append(Spacer(1, 10))

    # Section A
    story.append(Paragraph("SECTION A: FOUNDATIONAL & HISTORICAL CONCEPTS [25 MARKS]", styles['SecH1']))
    story.append(Paragraph("Answer all five questions in this section. Concise, technically accurate answers are required.", styles['DocBody']))
    
    q_a = [
        ("Question 1 [5 Marks]",
         "Differentiate clearly between <i>data</i> and <i>information</i> within an agricultural enterprise context. "
         "Illustrate your answer by outlining the four stages of the Information Processing Cycle (IPOS) as applied to an automated grain moisture monitoring station at SUA Mazimbu Farm."),
        ("Question 2 [5 Marks]",
         "Compare First-Generation and Second-Generation computers across the following specific dimensions: "
         "(a) Primary active switching electronics, (b) Primary internal memory technology, (c) Typical physical power and cooling requirements, and (d) Primary programming paradigm. Provide one canonical machine example for each generation."),
        ("Question 3 [5 Marks]",
         "Analyze the historical contribution of Charles Babbage and Augusta Ada Lovelace. Why is the Analytical Engine universally recognized as the theoretical prototype of modern general-purpose digital computers, and what conceptual breakthrough did Lovelace contribute regarding algorithmic execution?"),
        ("Question 4 [5 Marks]",
         "Explain the fundamental architecture proposed by John von Neumann in his 1945 EDVAC report. "
         "What is the 'stored-program concept', and what physical phenomenon constitutes the 'Von Neumann Bottleneck' in contemporary microcomputer processing?"),
        ("Question 5 [5 Marks]",
         "Distinguish between <i>Analog</i>, <i>Digital</i>, and <i>Hybrid</i> computing systems based on how they represent and process information. Provide an example of a hybrid computer in agricultural engineering.")
    ]
    for q_title, q_body in q_a:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    # Section B
    story.append(Paragraph("SECTION B: COMPUTER CONCEPTS & APPLICATIONS [35 MARKS]", styles['SecH1']))
    
    q_b = [
        ("Question 6 [10 Marks]",
         "Describe how a processor, memory, storage, and operating-system software work together when a student opens and edits a document. [10 Marks]"),
        ("Question 7 [10 Marks]",
         "Compare general-purpose, special-purpose, and embedded computers. Give an appropriate example from agriculture, animal science, tourism, engineering, or food science for each type. [10 Marks]"),
        ("Question 8 [8 Marks]",
         "Explain the stored-program concept and describe one way it changed the design and use of computers. [8 Marks]"),
        ("Question 9 [7 Marks]",
         "Choose a suitable computer type for an agricultural extension team working both in an office and in the field. Explain your choice using portability, connectivity, software needs, and data protection. [7 Marks]")
    ]
    for q_title, q_body in q_b:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    # Section C
    story.append(Paragraph("SECTION C: APPLIED ENTERPRISE & INFRASTRUCTURE DESIGN [40 MARKS]", styles['SecH1']))
    
    q_c = [
        ("Question 10 [15 Marks]",
         "The SUA School of Engineering and Technology intends to procure new computer infrastructure for two distinct facilities: (Facility 1) A Computer-Aided Design (CAD) and drone aerial photogrammetry laboratory for precision farming; (Facility 2) An automated field weather telemetry network spanning 12 outlying experimental agricultural stations in Morogoro Rural.<br/>"
         "(a) Specify and justify the optimal computer classification (e.g., Workstation vs Desktop PC vs Single-Board Computer vs Embedded Microcontroller) for each facility. [5 Marks]<br/>"
         "(b) Produce a comparative specification matrix evaluating both choices across: Processor class, memory capacity and ECC requirements, graphics accelerator, thermal/environmental tolerance, power source, and operating system. [6 Marks]<br/>"
         "(c) Outline the network role (Client, Peer, or Dedicated Server) each machine plays in the overall enterprise data collection pipeline. [4 Marks]"),
        ("Question 11 [15 Marks]",
         "Contrast the architectural paradigms of Supercomputers, Enterprise Mainframes, and Microcomputer Clusters.<br/>"
         "(a) Discuss why a commercial banking transaction processing system (such as CRDB or NMB in Tanzania) relies on IBM z16 Mainframes with 99.999% ('five nines') availability rather than high-performance supercomputers. [6 Marks]<br/>"
         "(b) Contrast the concepts of <i>Reliability, Availability, and Serviceability (RAS)</i> with <i>Peak Floating-Point Operations Per Second (FLOPS)</i>. [5 Marks]<br/>"
         "(c) Explain how a cluster of commodity microcomputers (Beowulf cluster) running Linux can economically perform agricultural genomics and climate forecasting previously restricted to monolithic supercomputers. [4 Marks]"),
        ("Question 12 [10 Marks]",
         "Terminal Diagnostics & Operating Environment Analysis:<br/>"
         "A systems technician at SUA is auditing a microcomputer laboratory running Ubuntu Linux.<br/>"
         "(a) Provide the exact terminal commands required to display: (i) Detailed CPU architecture and cache topology, (ii) Total and available RAM in human-readable megabytes/gigabytes, (iii) Motherboard BIOS/firmware vendor and version, and (iv) Storage block device hierarchy. [5 Marks]<br/>"
         "(b) Explain what the processor model, core, and thread entries in `lscpu` describe, and why an operating system may report more logical processors than physical processor packages. [5 Marks]")
    ]
    for q_title, q_body in q_c:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    render_assignment_pdf("BIT_111_Assignment_1.pdf", story)

# -------------------------------------------------------------
# ASSIGNMENT 2: MAIN COMPONENTS OF A MICROCOMPUTER
# -------------------------------------------------------------
def build_assignment_2():
    styles = get_custom_stylesheet()
    story = []
    story.append(create_assignment_header(
        2, 2, "Microcomputer Components, Subsystems & Architectural Comparisons",
        "Subtopic 2.1 (Devices & Logical Configurations: CPU, Memory, Bus, I/O, Storage), Subtopic 2.2 (Comparative Aspects)",
        "End of Week 4 by 17:00 EAT"
    ))
    story.append(Spacer(1, 8))
    story.append(create_instructions_box())
    story.append(Spacer(1, 10))

    story.append(Paragraph("SECTION A: FOUNDATIONAL ARCHITECTURAL CONCEPTS [25 MARKS]", styles['SecH1']))
    q_a = [
        ("Question 1 [5 Marks]",
         "Detail the functional role of the four internal CPU components: (a) Arithmetic Logic Unit (ALU), (b) Control Unit (CU), (c) Program Counter (PC), and (d) Instruction Register (IR). Describe how they collaborate during instruction decoding."),
        ("Question 2 [5 Marks]",
         "Differentiate between Static RAM (SRAM) and Dynamic RAM (DRAM) at the transistor/circuit level. Explain why SRAM is utilized exclusively for processor cache hierarchies (L1, L2, L3) while DRAM is utilized for main system memory."),
        ("Question 3 [5 Marks]",
         "Explain the mechanical architecture of a Hard Disk Drive (HDD). Define the components that govern total average data access time: Seek Time, Rotational Latency, and Transfer Time. How does a Solid-State Drive (SSD) eliminate two of these components?"),
        ("Question 4 [5 Marks]",
         "Define the three functional sub-buses comprising the system bus: (a) Data Bus, (b) Address Bus, and (c) Control Bus. Specify which of these buses are unidirectional and which are bidirectional, providing rigorous architectural reasons."),
        ("Question 5 [5 Marks]",
         "Compare CISC (Complex Instruction Set Computer) and RISC (Reduced Instruction Set Computer) design philosophies. Explain how modern microprocessors (such as Intel Core x86-64 and Apple M-Series ARM) incorporate elements of both philosophies.")
    ]
    for q_title, q_body in q_a:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION B: HARDWARE CONCEPTS & COMPARISONS [35 MARKS]", styles['SecH1']))
    q_b = [
        ("Question 6 [10 Marks]",
         "Describe the fetch, decode, and execute stages of the processor instruction cycle. Explain how the control unit, arithmetic logic unit, and registers contribute. [10 Marks]"),
        ("Question 7 [10 Marks]",
         "Compare RAM, ROM, cache, and secondary storage by purpose, volatility, and typical use. Give one example of when each is relevant to a student or researcher. [10 Marks]"),
        ("Question 8 [8 Marks]",
         "Explain the difference between a hard disk drive and a solid-state drive. Discuss durability, moving parts, and suitable uses without performing capacity or speed calculations. [8 Marks]"),
        ("Question 9 [7 Marks]",
         "Describe the purpose of the address, data, and control buses. Explain how an input device and an output device communicate with a computer system. [7 Marks]")
    ]
    for q_title, q_body in q_b:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION C: SYSTEM COMPARISONS & APPLIED INTEGRATION [40 MARKS]", styles['SecH1']))
    q_c = [
        ("Question 10 [15 Marks]",
         "Workstations versus Standard Commercial Microcomputers:<br/>"
         "The Department of Soil and Geological Sciences at SUA requires a high-performance computer for running 3D digital elevation models (DEM) and hyperspectral soil GIS simulations.<br/>"
         "(a) Contrast an engineering workstation with an ordinary consumer desktop PC across: Processor architecture (e.g., AMD Threadripper/Intel Xeon vs Core i5), Memory architecture (ECC vs non-ECC), GPU capabilities (Nvidia RTX Ada Generation vs consumer GeForce), and Storage interfaces. [7 Marks]<br/>"
         "(b) What is Error-Correcting Code (ECC) memory? Explain the physical Hamming code mechanism that enables single-bit error correction and double-bit error detection (SEC-DED). Why is this critical for long-running scientific simulations? [5 Marks]<br/>"
         "(c) Recommend a workstation or a standard desktop for this research task. Justify your choice using software needs, reliability, support, and expected use. [3 Marks]"),
        ("Question 11 [15 Marks]",
         "Comparative Analysis: Microcomputers vs Mainframes and Minicomputers:<br/>"
         "(a) Construct an exhaustive comparison matrix evaluating Microcomputers, Minicomputers (Midrange systems), and Mainframes across: Typical user concurrency, I/O processor subsystem architecture, operating system complexity, physical footprints, and fault-tolerant hardware redundancy. [8 Marks]<br/>"
         "(b) Trace the historical paradigm shift that led to the decline of traditional minicomputers (e.g., DEC PDP and VAX) in favor of networked microcomputer client-server architectures in university and enterprise environments. [4 Marks]<br/>"
         "(c) Explain the concept of 'Symmetric Multiprocessing' (SMP) and how modern multi-socket microcomputer servers achieve processing capabilities that rival historic enterprise mainframes. [3 Marks]"),
        ("Question 12 [10 Marks]",
         "Peripheral Interface & Agricultural Sensor Integration:<br/>"
         "An engineering student at SUA is designing an automated greenhouse control unit based on an embedded microcomputer (Raspberry Pi 4B) connected to soil moisture sensors, temperature probes, and irrigation solenoid relays.<br/>"
         "(a) Differentiate between Analog-to-Digital Conversion (ADC) and Digital I/O (GPIO). Why does the microcomputer require an external ADC (such as the ADS1115) to read analog resistive soil sensors? [4 Marks]<br/>"
         "(b) Contrast the I2C, SPI, and UART serial communication protocols in terms of wiring complexity, general communication speed, and multi-device addressing. Recommend a suitable protocol for connecting identical environmental sensors. [6 Marks]")
    ]
    for q_title, q_body in q_c:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    render_assignment_pdf("BIT_111_Assignment_2.pdf", story)

# -------------------------------------------------------------
# ASSIGNMENT 3: PERSONAL COMPUTER SECURITY CONTROLS
# -------------------------------------------------------------
def build_assignment_3():
    styles = get_custom_stylesheet()
    story = []
    story.append(create_assignment_header(
        3, 3, "Personal Computer (PC) Security Controls, Firmware, TPM & Access Models",
        "Subtopic 3.1 (Hard Disk & Power-On Passwords), Subtopic 3.2 (BIOS/UEFI & Secure Boot/TPM), Subtopic 3.3 (Login Passwords & Access Controls)",
        "End of Week 6 by 17:00 EAT"
    ))
    story.append(Spacer(1, 8))
    story.append(create_instructions_box())
    story.append(Spacer(1, 10))

    story.append(Paragraph("SECTION A: FOUNDATIONAL SECURITY ARCHITECTURE [25 MARKS]", styles['SecH1']))
    q_a = [
        ("Question 1 [5 Marks]",
         "Differentiate between an ATA Storage Security Password (hard disk password) and an Operating System Login Password. If a physical hard disk is extracted from a stolen laptop and connected via a USB enclosure to an external forensic computer, explain precisely which password protects the data and why."),
        ("Question 2 [5 Marks]",
         "Contrast the legacy BIOS (Basic Input/Output System) with the modern UEFI (Unified Extensible Firmware Interface) architecture. Focus on: (a) Execution mode (16-bit real mode vs 32/64-bit protected mode), (b) Partition table support (MBR vs GPT), and (c) Secure firmware verification mechanisms."),
        ("Question 3 [5 Marks]",
         "Explain the role and architecture of the Trusted Platform Module (TPM 2.0). Define the Endorsement Key (EK), Storage Root Key (SRK), and Platform Configuration Registers (PCRs). What is 'Measured Boot'?"),
        ("Question 4 [5 Marks]",
         "Describe the three fundamental factors of authentication: Something you know, Something you have, and Something you are. Give two microcomputer examples of each factor. What is Multi-Factor Authentication (MFA), and why does it drastically reduce account takeover risk?"),
        ("Question 5 [5 Marks]",
         "Differentiate between Discretionary Access Control (DAC) and Mandatory Access Control (MAC). Illustrate how standard Linux POSIX permissions represent DAC, whereas SELinux enforces MAC.")
    ]
    for q_title, q_body in q_a:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION B: SECURITY CONCEPTS & PRACTICES [35 MARKS]", styles['SecH1']))
    q_b = [
        ("Question 6 [10 Marks]",
         "Explain why long, unique passwords and multi-factor authentication help protect university accounts. Describe how a password manager can support safe password use. [10 Marks]"),
        ("Question 7 [10 Marks]",
         "Describe how full-disk encryption protects information on a lost or stolen laptop. Explain the roles of the user account and trusted hardware at a conceptual level. [10 Marks]"),
        ("Question 8 [8 Marks]",
         "Explain the purpose of Secure Boot and describe how it helps ensure that a computer starts trusted system software. [8 Marks]"),
        ("Question 9 [7 Marks]",
         "Compare secure erasure, cryptographic erasure, and physical destruction as ways to handle storage media that is no longer needed. [7 Marks]")
    ]
    for q_title, q_body in q_b:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION C: APPLIED ENTERPRISE SECURITY SCENARIOS [40 MARKS]", styles['SecH1']))
    q_c = [
        ("Question 10 [15 Marks]",
         "Enterprise PC Security Hardening at SUA Administration:<br/>"
         "The SUA Examination Directorate manages 30 microcomputers containing highly confidential university examination papers, grading sheets, and student transcripts.<br/>"
         "(a) Design a comprehensive multi-layered security hardening policy covering: (i) Physical chassis lock and port blocking, (ii) BIOS/UEFI supervisor passwords and boot order locking, (iii) TPM-backed Full Disk Encryption with BitLocker/LUKS, and (iv) Operating system user account privileges. [8 Marks]<br/>"
         "(b) Detail the configuration of Windows Group Policy Objects (GPO) or Linux PAM rules to enforce: 14-character minimum password length, account lockout after 5 failed attempts, automated screen lock after 5 minutes of inactivity, and disabling USB mass storage write access. [4 Marks]<br/>"
         "(c) Outline an incident response protocol if one of the examination laptops is reported stolen from an academic office. [3 Marks]"),
        ("Question 11 [15 Marks]",
         "Linux Access Control & Sudoers Security Engineering:<br/>"
         "A shared departmental research server at SUA DIIT hosts 40 student users and 4 research staff.<br/>"
         "(a) Explain the permission groups (Owner, Group, Others) and the purpose of the sticky bit. Describe how an administrator can support shared work while preventing users from deleting one another's files. [6 Marks]<br/>"
         "(b) Write the exact Linux commands to: (i) Create a group called `agric_research`, (ii) Add users `bertha` and `baraka` to the group, (iii) Set ownership and permissions on `/opt/crop_data` to ensure group collaboration with sticky bit protection. [5 Marks]<br/>"
         "(c) Explain why granting `ALL=(ALL:ALL) ALL` in `/etc/sudoers` violates the Principle of Least Privilege. Show how to restrict a user to running only `/usr/bin/systemctl restart apache2` without a password prompt. [4 Marks]"),
        ("Question 12 [10 Marks]",
         "Biometric Security Evaluation in Field Microcomputers:<br/>"
         "SUA Agricultural Extension Officers utilize ruggedized field tablets equipped with fingerprint scanners and facial recognition cameras to register smallholder farmers across Morogoro.<br/>"
         "(a) Define False Acceptance Rate (FAR) and False Rejection Rate (FRR). Explain the trade-off between FAR and FRR when calibrating biometric sensor sensitivity. [4 Marks]<br/>"
         "(b) What is the Crossover Error Rate (CER) / Equal Error Rate (EER), and why is it used as the benchmark for biometric device comparison? [3 Marks]<br/>"
         "(c) How can biometric authentication be vulnerable to 'presentation attacks' (spoofing with silicone fingers or photographs), and what hardware liveness detection techniques exist to mitigate this vulnerability? [3 Marks]")
    ]
    for q_title, q_body in q_c:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    render_assignment_pdf("BIT_111_Assignment_3.pdf", story)

# -------------------------------------------------------------
# ASSIGNMENT 4: FUNCTIONS AND TYPES OF OPERATING SYSTEMS
# -------------------------------------------------------------
def build_assignment_4():
    styles = get_custom_stylesheet()
    story = []
    story.append(create_assignment_header(
        4, 4, "Functions & Types of Operating Systems, DOS Commands & Process Management",
        "Subtopic 4.1 (OS Evolution & Categories), Subtopic 4.2 (DOS Internal & External Commands), Subtopic 4.3 (Windows/Linux System Management)",
        "End of Week 8 by 17:00 EAT"
    ))
    story.append(Spacer(1, 8))
    story.append(create_instructions_box())
    story.append(Spacer(1, 10))

    story.append(Paragraph("SECTION A: FOUNDATIONAL OS THEORIES [25 MARKS]", styles['SecH1']))
    q_a = [
        ("Question 1 [5 Marks]",
         "Explain the primary objectives of an Operating System as: (a) An Extended Machine (Abstraction Layer), and (b) A Resource Arbiter. Contrast how user applications interact with hardware directly versus through system call interfaces."),
        ("Question 2 [5 Marks]",
         "Differentiate between Monolithic Kernels, Microkernels, and Hybrid Kernels. Discuss the trade-offs regarding execution performance, fault isolation, and memory footprint. Name one real-world operating system utilizing each kernel architecture."),
        ("Question 3 [5 Marks]",
         "Describe the 5-state process lifecycle (New, Ready, Running, Waiting/Blocked, Terminated). Draw or trace the state transitions that occur when: (a) A running process requests a disk read, and (b) The disk controller signals an interrupt that the data has been loaded into memory."),
        ("Question 4 [5 Marks]",
         "Define Virtual Memory and Demand Paging. What is a Page Fault? Explain the architectural function of the Memory Management Unit (MMU) and the Translation Lookaside Buffer (TLB) during address translation."),
        ("Question 5 [5 Marks]",
         "Differentiate between Real-Time Operating Systems (RTOS) and General-Purpose Operating Systems (GPOS). Distinguish between 'Hard Real-Time' and 'Soft Real-Time' constraints using an automated agricultural combine harvester as an illustrative example.")
    ]
    for q_title, q_body in q_a:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION B: OPERATING-SYSTEM CONCEPTS & COMMANDS [35 MARKS]", styles['SecH1']))
    q_b = [
        ("Question 6 [12 Marks]",
         "Explain what a process is and describe how the operating system creates, runs, pauses, and ends processes. Compare First-Come, First-Served and Round Robin scheduling conceptually, including one advantage and limitation of each. [12 Marks]"),
        ("Question 7 [11 Marks]",
         "MS-DOS Command Architecture and Batch Scripting:<br/>"
         "(a) Explain the fundamental difference between an Internal DOS Command and an External DOS Command in terms of memory residency and file execution. [3 Marks]<br/>"
         "(b) Classify each of the following DOS commands as Internal or External: `DIR`, `FORMAT`, `CHKDSK`, `COPY`, `XCOPY`, `MD`, `ATTRIB`, `DEL`. [4 Marks]<br/>"
         "(c) Write an automated MS-DOS batch script (`BACKUP_AGRIC.BAT`) that performs the following sequence:<br/>"
         "    1. Clears the screen and checks if the directory `D:\\SUA_DATA\\2026` exists.<br/>"
         "    2. If it exists, creates a timestamped backup directory `E:\\ARCHIVE_2026`.<br/>"
         "    3. Uses `XCOPY` with switches to copy all files and subdirectories (including empty ones) and verify data integrity.<br/>"
         "    4. Sets the archive attribute of all source files to read-only using `ATTRIB`.<br/>"
         "    5. Outputs a success message to a log file `E:\\backup.log`. [4 Marks]"),
        ("Question 8 [12 Marks]",
         "Linux Process Management and Shell Pipeline Diagnostics:<br/>"
         "A bioinformatics pipeline at SUA running under Ubuntu is consuming excessive CPU resources.<br/>"
         "(a) Provide the exact Linux terminal pipeline to: Find the top 5 memory-consuming processes, display their PID, User, %MEM, and Command, and output the result to `/var/log/heavy_processes.txt`. [4 Marks]<br/>"
         "(b) Explain the difference between `kill -15 (SIGTERM)` and `kill -9 (SIGKILL)`. Why should a systems administrator always attempt `SIGTERM` before executing `SIGKILL`? [4 Marks]<br/>"
         "(c) Explain the concept of process 'Niceness' in Linux. What command adjusts the priority of a running process with PID 4120 to run with lower priority so it does not degrade interactive terminal responsiveness? [4 Marks]")
    ]
    for q_title, q_body in q_b:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION C: APPLIED FILE SYSTEMS & ENTERPRISE ADMIN [40 MARKS]", styles['SecH1']))
    q_c = [
        ("Question 9 [15 Marks]",
         "Enterprise File Systems Comparison: FAT32 vs NTFS vs ext4:<br/>"
         "(a) Construct a technical comparison matrix evaluating FAT32, NTFS, and Linux ext4 across: Maximum single file size, Maximum volume size, Journaling support, File-level access control permissions (ACLs), File-level encryption, and Compression capabilities. [8 Marks]<br/>"
         "(b) Explain why a file system's maximum single-file size can matter even when a storage device has free space. Describe how choosing a suitable file system can avoid this problem. [4 Marks]<br/>"
         "(c) What is a 'Journaling File System'? Trace the three-step sequence of journal commit, file system update, and checkpointing, explaining how journaling prevents file corruption during an abrupt power outage. [3 Marks]"),
        ("Question 10 [15 Marks]",
         "System Management and Troubleshooting: Windows Administrative Utilities:<br/>"
         "An IT specialist at SUA is resolving multiple client workstation issues.<br/>"
         "(a) Detail the specific administrative utility (Device Manager, Task Manager, Event Viewer, Disk Management, Services MMC, or Windows Registry) required to resolve each of the following scenarios: [6 Marks]<br/>"
         "    - Scenario 1: A newly installed PCIe network adapter displays a yellow exclamation mark and fails to obtain an IP address.<br/>"
         "    - Scenario 2: A computer boots to a black screen after an unverified driver installation; the technician needs to inspect system error logs and bugcheck codes.<br/>"
         "    - Scenario 3: An unpartitioned 2 TB secondary SATA SSD needs to be initialized with GPT and formatted as an NTFS drive labeled 'Data'.<br/>"
         "(b) Explain the architecture of the Windows Registry. Differentiate between `HKEY_LOCAL_MACHINE` (HKLM) and `HKEY_CURRENT_USER` (HKCU). Why can incorrect registry editing cause operating system boot failure? [5 Marks]<br/>"
         "(c) Write PowerShell cmdlets to: (i) List all stopped services that have their startup type set to Automatic, and (ii) Forcefully start the `Spooler` service. [4 Marks]"),
        ("Question 11 [10 Marks]",
         "Virtualization & Containerization within Academic Computing:<br/>"
         "(a) Differentiate between Type-1 (Bare-Metal) Hypervisors (e.g., VMware ESXi, Proxmox VE) and Type-2 (Hosted) Hypervisors (e.g., VirtualBox, VMware Workstation). Explain which is preferred for university server datacenters and why. [4 Marks]<br/>"
         "(b) Compare a Virtual Machine (VM) with a Docker Container in terms of operating system kernel sharing, boot time, resource overhead, and isolation boundaries. [4 Marks]<br/>"
         "(c) Explain how containerization allows agricultural researchers at SUA to package Python machine learning models with exact library dependencies for repeatable field deployment. [2 Marks]")
    ]
    for q_title, q_body in q_c:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    render_assignment_pdf("BIT_111_Assignment_4.pdf", story)

# -------------------------------------------------------------
# ASSIGNMENT 5: MICROCOMPUTER APPLICATIONS
# -------------------------------------------------------------
def build_assignment_5():
    styles = get_custom_stylesheet()
    story = []
    story.append(create_assignment_header(
        5, 5, "Microcomputer Applications: Word Processing, Simple Spreadsheets & Internet Protocols",
        "Subtopic 5.1 (Word Processors & Formatting), Subtopic 5.2 (Spreadsheets & Simple Formulas), Subtopic 5.3 (Web Browsing & Email Protocols)",
        "End of Week 10 by 17:00 EAT"
    ))
    story.append(Spacer(1, 8))
    story.append(create_instructions_box())
    story.append(Spacer(1, 10))

    story.append(Paragraph("SECTION A: FOUNDATIONAL SOFTWARE CONCEPTS [25 MARKS]", styles['SecH1']))
    q_a = [
        ("Question 1 [5 Marks]",
         "In word processing systems (e.g., Microsoft Word, LibreOffice Writer), differentiate between a 'Section Break (Next Page)' and a simple 'Page Break'. Describe a specific scenario in compiling an academic undergraduate thesis where a Section Break is mandatory."),
        ("Question 2 [5 Marks]",
         "Explain the mechanical architecture of Mail Merge. Identify the three principal components involved in any mail merge pipeline and explain how conditional fields (`IF...THEN...ELSE`) enable dynamic document customization."),
        ("Question 3 [5 Marks]",
         "In a spreadsheet, explain how a cell reference such as `B2` identifies a value by its column and row. Describe why a formula can refer to a cell rather than repeat a value."),
        ("Question 4 [5 Marks]",
         "Explain the difference between typing a value directly into a cell and using a simple formula that refers to other cells. Give one classroom example of when a formula is useful."),
        ("Question 5 [5 Marks]",
         "Contrast the two primary electronic mail retrieval protocols: POP3 (Post Office Protocol v3) and IMAP4 (Internet Message Access Protocol v4). Under what operational conditions is IMAP4 strictly required for university staff and students?")
    ]
    for q_title, q_body in q_a:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION B: SIMPLE SPREADSHEET FORMULAS & PROTOCOLS [35 MARKS]", styles['SecH1']))
    q_b = [
        ("Question 6 [15 Marks]",
         "A farm records daily milk yields in cells B2 through B6. Write spreadsheet formulas to add the yields with `SUM`, find their mean with `AVERAGE`, and calculate the value in a row by multiplying quantity in cell C2 by price in cell D2. Explain what each formula does. [15 Marks]"),
        ("Question 7 [10 Marks]",
         "A forestry class records seedling counts in one column and planted counts in another. Explain how to enter a simple addition formula and use `SUM` to find a column total. State how copying a formula to another row changes its cell references. [10 Marks]"),
        ("Question 8 [10 Marks]",
         "Web Protocols & HTTP/HTTPS Security Cycle:<br/>"
         "(a) Dissect the components of the Uniform Resource Locator (URL): `https://www.sua.ac.tz:443/academics/courses?dept=diit&term=2#syllabus`. Identify: Protocol/Scheme, Fully Qualified Domain Name (FQDN), Port, Path, Query String, and Anchor/Fragment. [4 Marks]<br/>"
         "(b) Explain the HTTP Request-Response cycle. Differentiate between the HTTP `GET` and `POST` methods regarding parameter transmission and security. [3 Marks]<br/>"
         "(c) Interpret the following HTTP response status codes: 200 OK, 301 Moved Permanently, 401 Unauthorized, 404 Not Found, 500 Internal Server Error, and 503 Service Unavailable. [3 Marks]")
    ]
    for q_title, q_body in q_b:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION C: APPLIED DOCUMENT & ENTERPRISE ARCHITECTURE [40 MARKS]", styles['SecH1']))
    q_c = [
        ("Question 9 [15 Marks]",
         "Academic Document Engineering & Master Dissertation Compilation:<br/>"
         "A postgraduate student at SUA is formatting a 120-page dissertation in Microsoft Word / LibreOffice Writer requiring strict university formatting standards:<br/>"
         "- Preliminary pages (Title, Declaration, Abstract, Table of Contents) must use Roman numerals (i, ii, iii, iv) centered at the bottom.<br/>"
         "- Chapter 1 onwards must begin with Arabic numeral '1' at the top-right corner.<br/>"
         "- Chapter 4 contains a wide 8-column agricultural field trial table that must be displayed in Landscape orientation, while preceding and succeeding pages remain Portrait.<br/>"
         "(a) Provide step-by-step technical instructions detailing how to insert Section Breaks, unlink headers and footers ('Link to Previous'), configure page numbering formats, and isolate page orientation for Chapter 4 without corrupting the rest of the document. [8 Marks]<br/>"
         "(b) Explain how the automated Table of Contents (TOC) and Table of Figures are constructed using Heading Styles (Heading 1, Heading 2) and Caption tags. Why should a professional academic document never contain manually typed tables of contents? [4 Marks]<br/>"
         "(c) Explain the utility of the 'Track Changes' feature and document compare tools in collaborative academic review between students and thesis supervisors. [3 Marks]"),
        ("Question 10 [15 Marks]",
         "Electronic Mail Infrastructure & Anti-Spoofing Architecture:<br/>"
         "The SUA ICT Directorate operates the university mail server domain `@sua.ac.tz`. Recently, fraudulent emails claiming to be from the Vice Chancellor's office were received by students.<br/>"
         "(a) Trace the complete path of an email sent via SMTP from `instructor@sua.ac.tz` to `student@gmail.com`. Detail the interactions between Mail User Agent (MUA), Mail Submission Agent (MSA), Mail Transfer Agent (MTA), and Mail Delivery Agent (MDA). [6 Marks]<br/>"
         "(b) Explain how the three foundational email authentication protocols protect against domain spoofing and phishing: [6 Marks]<br/>"
         "    1. SPF (Sender Policy Framework): How DNS TXT records specify authorized sending mail servers.<br/>"
         "    2. DKIM (DomainKeys Identified Mail): How public-key digital signatures in message headers verify message integrity.<br/>"
         "    3. DMARC (Domain-based Message Authentication, Reporting, and Conformance): How policy enforcement and reporting align SPF and DKIM results.<br/>"
         "(c) Construct a valid DNS TXT record for SPF that authorizes the mail server with IP `196.216.180.15` to send email for `sua.ac.tz` and instructs receiving servers to hard-fail (`-all`) all other sources. [3 Marks]"),
        ("Question 11 [10 Marks]",
         "A class records seedling types and quantities in a spreadsheet.<br/>"
         "(a) Describe how to label columns and enter one record per row. [3 Marks]<br/>"
         "(b) Explain how to sort the records by seedling type and make a simple chart to compare categories. [4 Marks]<br/>"
         "(c) Write a simple `SUM` formula for adding the quantities in cells B2 through B6. [3 Marks]")
    ]
    for q_title, q_body in q_c:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    render_assignment_pdf("BIT_111_Assignment_5.pdf", story)

# -------------------------------------------------------------
# ASSIGNMENT 6: DATA SECURITY AND MALWARE DEFENSE
# -------------------------------------------------------------
def build_assignment_6():
    styles = get_custom_stylesheet()
    story = []
    story.append(create_assignment_header(
        6, 6, "Data Security, Applied Cryptography, Environmental Protection & Malware Defense",
        "Subtopic 6.1 (Physical & Environmental Protection), Subtopic 6.2 (Unauthorized Access & Cryptography), Subtopic 6.3 (Malware Classifications & Defense)",
        "End of Week 12 by 17:00 EAT"
    ))
    story.append(Spacer(1, 8))
    story.append(create_instructions_box())
    story.append(Spacer(1, 10))

    story.append(Paragraph("SECTION A: FOUNDATIONAL SECURITY THEORIES [25 MARKS]", styles['SecH1']))
    q_a = [
        ("Question 1 [5 Marks]",
         "Explain the CIA Triad (Confidentiality, Integrity, Availability) within the context of a University Academic Information System (such as the SUA SUASIS student records system). Provide one realistic operational threat that specifically compromises each of the three pillars."),
        ("Question 2 [5 Marks]",
         "Differentiate between Symmetric and Asymmetric Cryptography across the following dimensions: (a) Key architecture, (b) Computational processing overhead, (c) Key distribution challenge, and (d) Primary operational use cases. Give one standardized cipher algorithm for each."),
        ("Question 3 [5 Marks]",
         "Describe the properties of a Cryptographic Hash Function: (a) Deterministic output, (b) Pre-image resistance (one-way), (c) Second pre-image resistance, (d) Collision resistance, and (e) The Avalanche Effect. Why are MD5 and SHA-1 no longer accepted for cryptographic integrity verification?"),
        ("Question 4 [5 Marks]",
         "Differentiate between a Computer Virus, a Computer Worm, and a Trojan Horse. Focus on their respective mechanisms of infection, replication, and human interaction requirements."),
        ("Question 5 [5 Marks]",
         "Explain the 3-2-1 Backup Strategy. Why does this rule specifically mandate that at least one copy of data be stored in an offsite or air-gapped physical location?")
    ]
    for q_title, q_body in q_a:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION B: SECURITY CONCEPTS & RESPONSE [35 MARKS]", styles['SecH1']))
    q_b = [
        ("Question 6 [12 Marks]",
         "Explain the purpose of an uninterruptible power supply (UPS) for a computer. Compare standby, line-interactive, and online UPS designs by describing how each responds to power interruptions or irregular supply. [12 Marks]"),
        ("Question 7 [11 Marks]",
         "Compare full, differential, and incremental backups in terms of what they copy and the general steps needed to restore files. Explain why an organization should keep an offline or offsite backup. [11 Marks]"),
        ("Question 8 [12 Marks]",
         "Applied Cryptographic Protocol Analysis: Hybrid Encryption & Digital Signatures:<br/>"
         "(a) Explain how TLS/HTTPS implements 'Hybrid Cryptography' combining asymmetric RSA/ECC and symmetric AES-GCM during a secure web session. Why is asymmetric encryption used during handshake negotiation but discarded in favor of symmetric encryption for bulk payload data transmission? [5 Marks]<br/>"
         "(b) A SUA professor digitally signs a final exam PDF using their private key. Trace the step-by-step mathematical verification process executed by the Examination Officer's software using the professor's public key. How does this prove both Authenticity and Non-Repudiation? [4 Marks]<br/>"
         "(c) What is a Certificate Authority (CA), and what security catastrophe occurs if a root CA's private signing key is compromised? [3 Marks]")
    ]
    for q_title, q_body in q_b:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 8))
    story.append(Paragraph("SECTION C: APPLIED MALWARE ANALYSIS & INCIDENT RESPONSE [40 MARKS]", styles['SecH1']))
    q_c = [
        ("Question 9 [15 Marks]",
         "Ransomware Anatomy and Defense-in-Depth Architecture:<br/>"
         "In May 2017, the WannaCry ransomware infected over 200,000 computers across 150 countries within hours, paralyzing critical hospital and enterprise networks.<br/>"
         "(a) Analyze the propagation mechanism of WannaCry. How did it combine the EternalBlue exploit (targeting Microsoft SMBv1 vulnerability CVE-2017-0144) with worm-like autonomous network scanning to spread across microcomputers without human interaction? [6 Marks]<br/>"
         "(b) Explain the technical encryption process executed by ransomware once inside a host machine (e.g., generation of local AES keys, encryption of user document extensions, and encryption of AES keys with the attacker's public RSA key). Why is it mathematically impossible to recover encrypted files without the attacker's private key in properly implemented ransomware? [5 Marks]<br/>"
         "(c) Formulate a robust Defense-in-Depth strategy for SUA computer laboratories to prevent ransomware infections, addressing network segmentation, automated patch management, Endpoint Detection and Response (EDR), and immutable offline backups. [4 Marks]"),
        ("Question 10 [15 Marks]",
         "Modern Anti-Malware Detection Methodologies:<br/>"
         "(a) Differentiate between Signature-Based Detection, Heuristic Analysis, and Behavioral Monitoring in modern anti-malware engines. Explain why signature-based detection fails against Zero-Day exploits and Polymorphic/Metamorphic malware. [6 Marks]<br/>"
         "(b) What is a 'Sandbox' in anti-malware analysis? Describe how an Endpoint Detection and Response (EDR) agent detonates an unknown email executable attachment within an isolated virtual machine to detect malicious API calls and process injection. [5 Marks]<br/>"
         "(c) Explain the concept of 'Living-off-the-Land' (LotL) attacks. Why are sophisticated adversaries increasingly utilizing native operating system binaries (such as PowerShell, WMI, and `certutil.exe`) rather than compiling custom malware executables? [4 Marks]"),
        ("Question 11 [10 Marks]",
         "NIST Incident Response Lifecycle Execution:<br/>"
         "A laboratory technician at SUA detects that 15 desktop microcomputers in the Solomon Mahlangu Campus (SMC) computer lab are exhibiting anomalous high outbound network traffic to an unknown external IP address in Eastern Europe, and their fans are running at 100% speed.<br/>"
         "(a) Classify this security incident (e.g., Botnet Command-and-Control / Cryptojacking). [2 Marks]<br/>"
         "(b) Outline the tactical response steps according to the four phases of the NIST SP 800-61 Computer Security Incident Handling Guide: [8 Marks]<br/>"
         "    1. Containment: Immediate actions to isolate compromised hosts without destroying volatile memory forensic evidence.<br/>"
         "    2. Eradication: Identifying malware persistence mechanisms (scheduled tasks, registry run keys, services) and removing malicious artifacts.<br/>"
         "    3. Recovery: Re-imaging systems from known clean gold masters, restoring data from verified backups, and testing network connectivity.<br/>"
         "    4. Post-Incident Activity: Documenting root cause analysis and implementing preventative firewall controls.")
    ]
    for q_title, q_body in q_c:
        story.append(Paragraph(f"<b>{q_title}:</b> {q_body}", styles['DocBody']))
        story.append(Spacer(1, 4))

    render_assignment_pdf("BIT_111_Assignment_6.pdf", story)

def build_all_assignments():
    print("=" * 60)
    print("BUILDING 6 TAKEHOME HOMEWORK ASSIGNMENTS FOR BIT 111")
    print("=" * 60)
    build_assignment_1()
    build_assignment_2()
    build_assignment_3()
    build_assignment_4()
    build_assignment_5()
    build_assignment_6()
    print("=" * 60)
    print("ALL 6 ASSIGNMENTS GENERATED SUCCESSFULLY IN BIT 111/Assignment/")
    print("=" * 60)

if __name__ == "__main__":
    build_all_assignments()
