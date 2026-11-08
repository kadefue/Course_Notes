#!/usr/bin/env python3
"""
build_outline.py
Generates the comprehensive Course Outline & Syllabus document for:
BIT 111: MICROCOMPUTERS AND APPLICATIONS
Department of Informatics and Information Technology (DIIT),
Sokoine University of Agriculture (SUA).
Saved in Notes/BIT_111_Course_Outline.pdf.
"""

import os
import sys

LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from compendium_base import (
    get_custom_stylesheet, create_custom_table, render_pdf,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_BG_LIGHT, COLOR_BORDER
)

def build_course_outline():
    styles = get_custom_stylesheet()
    story = []

    # Title Block Table
    header_data = [
        [Paragraph("SOKOINE UNIVERSITY OF AGRICULTURE", styles['CoverUniv'])],
        [Paragraph("School of Engineering and Technology / College of Natural and Applied Sciences", styles['CoverDept'])],
        [Paragraph("Department of Informatics and Information Technology (DIIT)", styles['CoverDept'])],
        [Spacer(1, 3)],
        [Paragraph("BIT 111: MICROCOMPUTERS AND APPLICATIONS", styles['CourseCode'])],
        [Paragraph("OFFICIAL COURSE SYLLABUS & LEARNING CONTRACT", styles['CourseTitle'])],
        [Paragraph(
            "<b>Course Instructor:</b> Madam Bertha Msuliche Lebalwa (MSc)<br/>"
            "<b>Course Status:</b> Core / Elective Undergraduate | <b>Credit Rating:</b> 12 Credits | <b>Total Notional Hours:</b> 120 Hours<br/>"
            "<b>Hours Distribution:</b> 15h Lectures, 30h Seminars/Tutorials, 15h Assignments, 15h Independent Study, 45h Practical Laboratory",
            styles['MetaBox']
        )]
    ]
    tbl = Table(header_data, colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_LIGHT),
        ('BOX', (0, 0), (-1, -1), 1.2, COLOR_PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 10))

    # 1. Course Aim & Rationale
    story.append(Paragraph("1. Course Aim & Strategic Rationale", styles['SecH1']))
    story.append(Paragraph(
        "<b>BIT 111: Microcomputers and Applications</b> is designed to empower undergraduate students across various engineering, "
        "agricultural, applied sciences, and environmental disciplines with foundational knowledge and applied practical competence "
        "in modern microcomputer systems. In an era increasingly driven by Agriculture 4.0, data-driven farm enterprise management, "
        "smart sensors, and automated information processing, microcomputers serve as the ubiquitous tool for computational analysis, "
        "scientific documentation, electronic telemetry, and institutional workflow automation. This course establishes both the physical "
        "hardware foundations of personal computing and the hands-on proficiency required to operate operating systems, conduct advanced "
        "word processing, build dynamic quantitative spreadsheets, browse securely, and defend digital assets against cyber threats.",
        styles['DocBody']
    ))

    # 2. Course Expected Learning Outcomes (CELOs)
    story.append(Paragraph("2. Course Expected Learning Outcomes (CELOs)", styles['SecH1']))
    story.append(Paragraph(
        "Upon successful completion of BIT 111, each student will be able to:",
        styles['DocBody']
    ))
    outcomes = [
        "1. <b>Identify and describe</b> the principal hardware components of a modern microcomputer system and explain their physical and logical interconnects.",
        "2. <b>Utilize modern and legacy operating systems</b> (including command-line DOS and graphical Windows/Linux environments) to manage processes, files, directories, and peripheral devices.",
        "3. <b>Configure and apply personal computer (PC) security controls</b>, including power-on passwords, BIOS/UEFI setup parameters, Secure Boot, TPM encryption, and multi-factor operating system login policies.",
        "4. <b>Demonstrate advanced proficiency in word processing</b> application software (Microsoft Word / LibreOffice Writer) to produce professional academic reports, automate multi-level styling, implement mail merges, and manage citations.",
        "5. <b>Construct dynamic computational spreadsheet models</b> (Microsoft Excel / LibreOffice Calc) applying mathematical, statistical, lookup, and financial functions, conditional formatting, pivot tables, and analytical visualizations for agricultural and scientific decision-making.",
        "6. <b>Apply computer application software and security countermeasures</b> (including 3-2-1 backup strategies, anti-malware scanners, and email protocol netiquette) to resolve authentic real-world data management challenges."
    ]
    for o in outcomes:
        story.append(Paragraph(o, styles['DocBullet']))
        story.append(Spacer(1, 2))

    # 3. Detailed Course Content Breakdown
    story.append(Spacer(1, 4))
    story.append(Paragraph("3. Course Structure & Syllabus Modules", styles['SecH1']))

    syllabus_headers = ["Topic #", "Curriculum Topic Title", "Detailed Syllabus Subtopics & Practical Competencies", "Notional Hours"]
    syllabus_rows = [
        ["Topic 1", "Introduction to Computers",
         "1.1 Computer Generations (1st to 5th+ Gen: vacuum tubes, transistors, ICs, microprocessors, AI/quantum);<br/>"
         "1.2 History & Pioneers (Abacus, Babbage, Lovelace, ENIAC, von Neumann, microcomputer revolution);<br/>"
         "1.3 Computer Classifications (Size: micro, mini, mainframe, supercomputer; Technology: analog, digital, hybrid; Purpose & network roles).",
         "15 Hours"],
        ["Topic 2", "Main Components of a Microcomputer",
         "2.1 Devices & Logical Configurations (CPU: ALU, CU, Registers, Cache; Bus architecture: Data, Address, Control; System RAM DDR4/DDR5, ROM/UEFI, NVMe SSD, HDD; Input/Output devices, Motherboard chipsets);<br/>"
         "2.2 Comparative Architecture (Micro vs Mainframe, Workstations vs Micro, Minicomputers vs Microcomputers).",
         "20 Hours"],
        ["Topic 3", "PC Security Controls",
         "3.1 Hardware & Power-on Security (Hard disk ATA passwords, Power-On Password, Chassis intrusion);<br/>"
         "3.2 Firmware & System Setup Security (BIOS/UEFI Supervisor & User passwords, Secure Boot, TPM 2.0, BitLocker / LUKS drive encryption);<br/>"
         "3.3 OS Login & Access Controls (Windows Hello, PINs, Passwords, User Account Control, Least Privilege).",
         "15 Hours"],
        ["Topic 4", "Functions & Types of Operating Systems",
         "4.1 Evolution & OS Categories (Single/Multi-user, Multitasking, RTOS, Batch; MS-DOS, UNIX/Linux, Windows);<br/>"
         "4.2 Disk Operating System (DOS Architecture, COMMAND.COM, Internal vs External commands, batch automation);<br/>"
         "4.3 Graphical Operating Systems (Kernel architecture, Memory management, Paging, NTFS/ext4, Admin tools).",
         "20 Hours"],
        ["Topic 5", "Microcomputer Applications: Word, Excel, Web & Email",
         "5.1 Word Processing (Templates, Styles, Multi-level numbering, Automated Table of Contents, Tables, Mail Merge);<br/>"
         "5.2 Spreadsheet Modeling (Relative, Absolute, Mixed cell references, Formulas: SUM, AVERAGE, IF, VLOOKUP/XLOOKUP, Charts, Pivot Tables);<br/>"
         "5.3 Web Browsing & Email (HTTP/HTTPS, DNS, Web browsers, SMTP, IMAP, POP3, Netiquette, Spam filtering).",
         "30 Hours"],
        ["Topic 6", "Data Security & Malware Defense",
         "6.1 Physical Protection & Environmental Controls (UPS, Surge protectors, 3-2-1 Backup rule, Disaster recovery);<br/>"
         "6.2 Logical Access Control & Cryptography (Authentication vs Authorization, ACLs, Symmetric AES vs Asymmetric RSA);<br/>"
         "6.3 Malware Mitigation (Viruses, Worms, Trojans, Ransomware, Spyware, Rootkits, Anti-malware scanners).",
         "20 Hours"]
    ]
    story.append(create_custom_table(syllabus_headers, syllabus_rows, [0.8*inch, 1.8*inch, 3.7*inch, 0.9*inch]))

    # 4. Teaching and Learning Methodology
    story.append(Spacer(1, 4))
    story.append(Paragraph("4. Teaching and Learning Methodology", styles['SecH1']))
    story.append(Paragraph(
        "<b>i. Interactive Lectures & Multimedia Presentations:</b> Interactive face-to-face lectures and conceptual demonstrations covering computer hardware architecture, operating system design principles, and cybersecurity foundations.<br/>"
        "<b>ii. Hands-on Laboratory Practical Sessions:</b> Intensive bench sessions in the university computer laboratory: exploring BIOS/UEFI setup screens, executing command-line DOS batch utilities, configuring drive security, building multi-page formatted technical reports in Word, creating complex agricultural data models in Excel, and configuring anti-malware software.<br/>"
        "<b>iii. Practical Demonstrations & Problem-Solving:</b> Live demonstration of formula auditing, spreadsheet error troubleshooting, mail merge configuration, and network email client setup.<br/>"
        "<b>iv. Self-Directed Takehome Homework Assignments:</b> Six comprehensive tiered assignments reinforcing conceptual understanding, quantitative calculations, command syntax, and real-world enterprise scenarios.",
        styles['DocBody']
    ))

    # 5. Assessment Methods & Grading Policy
    story.append(Spacer(1, 4))
    story.append(Paragraph("5. Assessment Methods & Grading Policy", styles['SecH1']))
    story.append(Paragraph(
        "Assessment for <b>BIT 111: Microcomputers and Applications</b> consists of <b>Continuous Assessment (60%)</b> "
        "and a comprehensive <b>University Examination (40%)</b>. Practical hands-on competence in Word, Excel, DOS, "
        "and system security is heavily weighted to ensure true technical operational proficiency.<br/>"
        "<i>Note: Specific weighting allocations may be adjusted by the course instructor in accordance with departmental guidelines.</i>",
        styles['DocBody']
    ))

    grade_headers = ["Assessment Component", "Scope / Description", "Weighting (%)", "Delivery Mode / Deliverable"]
    grade_rows = [
        ["Two Takehome Assignments", "Selected from the 6 Course Topic Homeworks", "5%", "Individual analytical and practical submissions (2.5% each)"],
        ["Two Theory Tests", "Theory Test 1 (Topics 1–3) & Theory Test 2 (Topics 4–6)", "15%", "Closed-book written engineering theory examinations (7.5% each)"],
        ["Practical Laboratory Report", "Formal logbook of laboratory practical sessions (Word, Excel, DOS, Security)", "10%", "Submitted laboratory logbook with verified output screenshots and analysis"],
        ["Practical Test", "Hands-on examination in the Computer Lab (Word Processing, Excel Modeling & DOS)", "30%", "Timed hands-on laboratory examination testing live application proficiency"],
        ["Continuous Assessment (CA) Subtotal", "Assignments (5%) + Theory Tests (15%) + Lab Report (10%) + Practical Test (30%)", "60%", "Total In-Semester Continuous Assessment Score"],
        ["University Examination (UE)", "Comprehensive Final Examination covering Topics 1 through 6", "40%", "Formal 3-hour theoretical and applied university examination"],
        ["Total Final Grade", "Continuous Assessment (60%) + University Examination (40%)", "100%", "SUA Grading Scale: A (70%+), B+ (60-69%), B (50-59%), C (40-49%), D (35-39%), E (0-34%)"]
    ]
    story.append(create_custom_table(grade_headers, grade_rows, [1.8*inch, 2.3*inch, 0.9*inch, 2.2*inch]))

    # 6. Prescribed Textbooks & Reading List
    story.append(Spacer(1, 6))
    story.append(Paragraph("6. Prescribed Textbooks & Reference Literature", styles['SecH1']))
    refs = [
        "1. Shelly, G. A., & Vermaat, M. E. (2018). <i>Discovering Computers: Digital Technology, Data, and Devices</i> (16th ed.). Cengage Learning.",
        "2. Parhami, B. (2005). <i>Computer Architecture: From Microprocessors to Supercomputers</i>. Oxford University Press.",
        "3. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). <i>Operating System Concepts</i> (10th ed.). John Wiley & Sons.",
        "4. Walkenbach, J. (2019). <i>Microsoft Excel 2019 Bible: The Comprehensive Tutorial Resource</i>. Wiley.",
        "5. Stallings, W. (2021). <i>Computer Organization and Architecture: Designing for Performance</i> (11th ed.). Pearson.",
        "6. Young, M. L., Barrows, A., & Stockman, J. C. (2010). <i>Access 2010 ALL-IN-ONE For Dummies</i>. Wiley Publishing Inc.",
        "7. Tanenbaum, A. S., & Bos, H. (2015). <i>Modern Operating Systems</i> (4th ed.). Pearson Education.",
        "8. Forouzan, B. A. (2013). <i>Data Communications and Networking</i> (5th ed.). McGraw-Hill Education.",
        "9. Castellan, N. J. (1988). Comments on applications of microcomputers in teaching. <i>Behavior Research Methods, Instruments, & Computers</i>, 20(2), 193-196."
    ]
    for r in refs:
        story.append(Paragraph(r, styles['DocBullet']))
        story.append(Spacer(1, 1.5))

    render_pdf("BIT_111_Course_Outline.pdf", story, doc_title="BIT 111: Course Outline & Syllabus")

if __name__ == "__main__":
    build_course_outline()
