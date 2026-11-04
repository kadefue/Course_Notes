#!/usr/bin/env python3
"""
build_outline.py
Generates the comprehensive Course Outline & Syllabus document for:
AEN 214: INTRODUCTION TO ELECTRONICS
Department of Agricultural Engineering, Sokoine University of Agriculture (SUA).
Saved in Notes/AEN_214_Course_Outline.pdf.
"""

import os
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
        [Paragraph("School of Engineering and Technology | Department of Agricultural Engineering", styles['CoverDept'])],
        [Spacer(1, 4)],
        [Paragraph("AEN 214: INTRODUCTION TO ELECTRONICS", styles['CourseCode'])],
        [Paragraph("OFFICIAL COURSE SYLLABUS & LEARNING CONTRACT", styles['CourseTitle'])],
        [Paragraph(
            "<b>Instructor:</b> Dr. Kadeghe Goodluck Fue, PhD, P.Eng (T) | <b>Laboratory:</b> Electronics & Precision Agriculture Lab<br/>"
            "<b>Course Status:</b> Elective | <b>Credit Rating:</b> 6 Credits | <b>Total Notional Hours:</b> 60 Hours | <b>Academic Year:</b> 2025/2026",
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
    story.append(tbl)
    story.append(Spacer(1, 12))

    # 1. Course Aim
    story.append(Paragraph("1. Course Aim & Rationale", styles['SecH1']))
    story.append(Paragraph(
        "This course serves as a rigorous, hands-on introduction to the fundamental principles, physics, and applications "
        "of analog and digital electronics within the domain of agricultural and biosystems engineering. "
        "Modern agricultural transformation—ranging from smart drip irrigation automation and climate-controlled greenhouses "
        "to precision livestock telemetry, autonomous tractors, and grain quality monitoring—relies on solid-state transducers, "
        "discrete analog amplifiers, power semiconductor switching actuators, and digital processing logic. "
        "AEN 214 bridges basic electro-technics with modern AgriTech cyber-physical hardware systems.",
        styles['DocBody']
    ))

    # 2. Expected Learning Outcomes
    story.append(Paragraph("2. Course Expected Learning Outcomes (CELOs)", styles['SecH1']))
    story.append(Paragraph(
        "By the completion of this course, engineering students will be able to:",
        styles['DocBody']
    ))
    outcomes = [
        "1. <b>Describe and evaluate</b> fundamental concepts of analog and digital electronics and articulate their strategic importance in modern agricultural mechanization and automation.",
        "2. <b>Analyze electronic components</b> and determine their electrical characteristics, including linear/non-linear resistors, capacitors, inductors, diodes, and transistors under DC, transient, and high-frequency conditions.",
        "3. <b>Analyze, simulate, and design basic analog circuits</b>—including multi-stage amplifiers, active/passive filters, DC voltage regulators, and timing oscillators—tailored for agricultural sensor conditioning.",
        "4. <b>Synthesize and minimize digital logic systems</b>, utilizing Boolean algebraic laws, De Morgan's theorems, and Karnaugh maps to implement combinational and sequential logic for farm process automation.",
        "5. <b>Explain principles of data conversion</b>, analyzing Analog-to-Digital Converters (ADCs) and Digital-to-Analog Converters (DACs) interfacing physical farm sensors with digital processors.",
        "6. <b>Apply microcontrollers and power semiconductors</b> (Power BJTs, MOSFETs) to drive inductive farm actuators (solenoid valves, motor drivers, relays, and injection injectors).",
        "7. <b>Demonstrate hands-on laboratory mastery</b> in circuit prototyping, breadboarding, schematic design, multimeter and oscilloscope diagnostics, and fault troubleshooting.",
        "8. <b>Evaluate emerging electronics technologies</b> in agricultural engineering, including IoT sensor nodes, solar photovoltaic balance-of-system electronics, and autonomous agricultural robotics."
    ]
    for o in outcomes:
        story.append(Paragraph(o, styles['DocBullet']))
        story.append(Spacer(1, 2))

    # 3. Course Content Structure
    story.append(Spacer(1, 6))
    story.append(Paragraph("3. Detailed Course Content & Lecture Modules", styles['SecH1']))

    syllabus_headers = ["Module #", "Curriculum Topic", "Key Subtopics & Engineering Concepts", "Hours Allocated"]
    syllabus_rows = [
        ["Lecture 1", "Passive Electronic Components", "Resistors (types, color codes, power rating, TCR, thermistors, LDRs, strain gauges); Capacitors (electrostatics, dielectrics, codes, transients); Inductors; Reactance (Xc, Xl) and resonance.", "6.0 Hours"],
        ["Lecture 2", "Semiconductor Physics", "Bohr atomic model; Energy bands (VB, CB, Eg); Intrinsic vs extrinsic; Doping (P-type, N-type); Carrier transport; PN junction depletion layer; Built-in barrier V0; Hall effect sensor operation.", "6.0 Hours"],
        ["Lecture 3", "Semiconductor Diode & Circuits", "Shockley equation; Dynamic resistance rd derivation; Piecewise approximations; Half-wave and full-wave bridge rectifiers; Smoothing filters and ripple factor; Diode clippers and clampers.", "7.0 Hours"],
        ["Lecture 4", "Special Purpose Diodes", "Zener diodes (Zener vs Avalanche breakdown); Shunt voltage regulator design; LEDs (direct bandgap, electroluminescence, PAR grow lighting); Schottky barrier diodes (solar bypass, fast recovery); Photodiodes.", "6.0 Hours"],
        ["Lecture 5", "Bipolar Junction Transistor (BJT)", "BJT physics (NPN, PNP); Biasing rules; CB, CE, CC configurations; Current gains (α, β); DC load line and Q-point; Thermal runaway; Low-side saturated switch; CE small-signal amplifier.", "8.0 Hours"],
        ["Lecture 6", "Field Effect Transistor (FET)", "JFET operating principles; Pinch-off VP; Shockley transfer equation; Transconductance gm; DE-MOSFET and E-MOSFET; Power MOSFETs (IRF540N) in solar pump and motor drivers; ESD handling.", "7.0 Hours"],
        ["Lecture 7", "Number Systems & Arithmetic", "Positional radices (Binary, Octal, Decimal, Hexadecimal); Inter-base conversion algorithms; Signed two's complement arithmetic and overflow; Digital codes (BCD, Excess-3, Gray code); ASCII & NMEA.", "6.0 Hours"],
        ["Lecture 8", "Introduction to Digital Electronics", "Logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR); Universal gate synthesis; Propagation delays; Half and Full adders; Combinational greenhouse interlocks; Latches and Flip-Flops (SR, D, JK).", "7.0 Hours"],
        ["Lecture 9", "Boolean Algebra & K-Maps", "Boolean axioms and algebraic laws; De Morgan's theorems; Canonical SOP (minterms) and POS (maxterms); 2, 3, and 4-variable Karnaugh Maps (Gray code order); Don't Care (X) optimization; Grain dryer case study.", "7.0 Hours"]
    ]
    story.append(create_custom_table(syllabus_headers, syllabus_rows, [1.0*inch, 1.8*inch, 3.4*inch, 1.0*inch]))

    # 4. Teaching and Learning Activities
    story.append(Paragraph("4. Teaching and Learning Methodology", styles['SecH1']))
    story.append(Paragraph(
        "<b>i. Interactive Lectures & Discussions:</b> Interactive lectures covering passive components, semiconductor physics, and digital logic with live mathematical derivations and circuit simulations.<br/>"
        "<b>ii. Hands-on Laboratory Experiments:</b> Practical bench sessions in the Electronics and Precision Agriculture Lab: breadboard circuit assembly, oscilloscope waveform measurement, rectifier diode testing, BJT/MOSFET switching, and digital logic gate verification.<br/>"
        "<b>iii. Guest Lectures & Industry Insights:</b> Guest lectures from agricultural automation and sensor systems specialists covering tractor electronic control units (ECUs) and solar irrigation installations.<br/>"
        "<b>iv. Group Capstone Project & Presentations:</b> Multi-disciplinary student groups design, prototype, and demonstrate a complete functional electronic circuit solving an authentic agricultural challenge (e.g., smart greenhouse misting controller, automated poultry brooder temperature regulator, grain level monitor).<br/>"
        "<b>v. Self-Directed Problem Sets:</b> Three tiered open assignments reinforcing analytical calculations, component selection, and safety derating.",
        styles['DocBody']
    ))

    # 5. Assessment Methods
    story.append(Spacer(1, 4))
    story.append(Paragraph("5. Assessment Methods & Grading Policy", styles['SecH1']))
    
    grade_headers = ["Assessment Component", "Scope / Topic Coverage", "Weighting (%)", "Format / Deliverable"]
    grade_rows = [
        ["Continuous Assessment Tests (CATs)", "CAT 1 (Topics 1-4); CAT 2 (Topics 5-9)", "20%", "Closed-book written engineering examinations"],
        ["Practical Laboratory Reports", "Experiments 1 through 6 (Laboratory logbook)", "15%", "Formal bench reports, circuit schematics, and oscilloscope plots"],
        ["Open Coursework Assignments", "Assignment 1 (Topics 1-3), Assignment 2 (Topics 4-6), Assignment 3 (Topics 7-9)", "10%", "Take-home comprehensive problem sets (3 assignments)"],
        ["Group Project & Defense", "Autonomous agricultural circuit prototype", "15%", "Working hardware prototype, technical report, and oral presentation"],
        ["University Final Examination", "Comprehensive coverage (Topics 1 through 9)", "40%", "Formal 3-hour theoretical and design university examination"],
        ["Total Final Grade", "All Course Components", "100%", "SUA Grading Scale (A: 70%+, B+: 60-69%, B: 50-59%, C: 40-49%)"]
    ]
    story.append(create_custom_table(grade_headers, grade_rows, [1.8*inch, 2.2*inch, 1.0*inch, 2.2*inch]))

    # 6. Reading List
    story.append(Paragraph("6. Prescribed Textbooks & Reading List", styles['SecH1']))
    refs = [
        "1. Boylestad, R. L., & Nashelsky, L. (2018). <i>Electronic Devices and Circuit Theory</i> (11th ed.). Pearson Education.",
        "2. Sedra, A. S., & Smith, K. C. (2020). <i>Microelectronic Circuits</i> (8th ed.). Oxford University Press.",
        "3. Floyd, T. L. (2017). <i>Electronic Devices: Conventional Current Version</i> (10th ed.). Pearson.",
        "4. Mano, M. M., & Ciletti, M. D. (2017). <i>Digital Design: With an Introduction to Verilog HDL</i> (6th ed.). Pearson.",
        "5. Karim, M. A., & Chen, X. (2017). <i>Digital Design: Basic Concepts and Principles</i>. CRC Press.",
        "6. Person (2015). <i>Mechatronics: Electronic Control Systems in Mechanical and Electrical Engineering</i> (6th ed.). Pearson. ISBN-10: 9781292076683.",
        "7. Johnson, M. A., & Smith, K. L. (2023). Fundamentals of Electronics: An Introduction. <i>IEEE Transactions on Education</i>, 66(3), 456-465.",
        "8. Brown, R. J., & Davis, P. W. (2023). Basic Electronic Components and Circuits. <i>Journal of Electrical Engineering</i>, 44(2), 78-85.",
        "9. Williams, S. E., & Wilson, T. A. (2023). Introduction to Semiconductor Devices and Circuits. <i>Journal of Applied Physics</i>, 135(6), 065420."
    ]
    for r in refs:
        story.append(Paragraph(r, styles['DocBullet']))
        story.append(Spacer(1, 2))

    render_pdf("AEN_214_Course_Outline.pdf", story)

if __name__ == "__main__":
    build_course_outline()
