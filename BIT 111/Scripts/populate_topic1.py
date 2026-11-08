import os
import sys

output_file = "/home/kadefue/Course_Notes/BIT 111/Scripts/build_compedia_topic1.py"

with open(output_file, "w", encoding="utf-8") as f:
    f.write('''#!/usr/bin/env python3
"""
build_compedia_topic1.py
Comprehensive Academic Compendium for:
BIT 111: Microcomputers and Applications
Topic 1: Introduction to Microcomputers

Department of Informatics and Information Technology (DIIT),
School of Engineering and Technology / College of Natural and Applied Sciences,
Sokoine University of Agriculture (SUA), Morogoro, Tanzania.

Course Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Level: First-Year Undergraduate Degree Programs across SUA:
Agronomy, Animal Science, Veterinary Medicine, Tourism, Engineering, Extension,
Aquaculture, Wood Science, Food Science, Consumer Studies.

PEDAGOGICAL DESIGN PRINCIPLES:
- Introductory, conceptual, intuitive approach for first-year undergraduates.
- STRICTLY ZERO CALCULATIONS (No clock equations, CPI, Amdahl's Law, or binary math).
- Broadly inclusive across all 10 SUA academic and professional disciplines.
- Authentic, genuine academic literature citations only.
- Strict page-budget requirement: >= 35 pages of high-density academic material.
"""

import os
import sys

# Inject local python libs if present
LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

SCRIPTS_DIR = "/home/kadefue/Course_Notes/BIT 111/Scripts"
if os.path.exists(SCRIPTS_DIR) and SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from compendium_base import (
    get_custom_stylesheet, create_callout_box, create_styled_table,
    NumberedCanvas, SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Image, KeepTogether, PageBreak, HRFlowable, letter, inch,
    COLOR_PRIMARY, COLOR_SUA_GREEN, COLOR_SUA_DARKGREEN, COLOR_TEXT,
    COLOR_BORDER, COLOR_BG_LIGHT, COLOR_WHITE, COLOR_MUTED
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
        [Paragraph("TOPIC 1: INTRODUCTION TO COMPUTERS — LECTURE COMPENDIUM", styles['CourseTitle'])],
        [Paragraph(
            "<b>Course Instructor:</b> Madam Bertha Msuliche Lebalwa (MSc)<br/>"
            "<b>Department:</b> Informatics and Information Technology (DIIT), SUA Morogoro<br/>"
            "<b>Target Audience:</b> First-Year Undergraduate Students across all SUA Degree Programs<br/>"
            "<b>Disciplines Covered:</b> Agriculture, Agronomy, Animal Science, Veterinary Medicine, Wildlife Management, Tourism, Agricultural Engineering, Extension, Aquaculture, Forestry, Wood Science, Food Science, Consumer Studies<br/>"
            "<b>Curriculum Modules:</b> Computer Generations (1.1) | History & Pioneers (1.2) | Computer Classifications (1.3)<br/>"
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

    # Pedagogical Callout Box
    story.append(create_callout_box(
        "COURSE ORIENTATION & PEDAGOGICAL PHILOSOPHY FOR FIRST-YEAR UNDERGRADUATES",
        "Welcome to BIT 111: Microcomputers and Applications at Sokoine University of Agriculture (SUA). "
        "As an introductory, foundational course designed for students entering their university journey across diverse fields—from agronomy and animal sciences to veterinary medicine, wildlife tourism, engineering, community extension, aquaculture, forestry, food science, and consumer studies—this course assumes no prior background in computer science or programming. "
        "Our educational approach is strictly conceptual and intuitive. You will not be burdened with engineering mathematics, complex circuit formulas, or hardware clock equations. Instead, you will acquire a clear, rigorous, and practical understanding of how personal computers work, how data transforms into actionable intelligence, how computing technology evolved over five distinct generations, and how modern microcomputers empower researchers and professionals to solve real-world challenges across Tanzania and East Africa.",
        styles,
        box_type='sua'
    ))
    story.append(Spacer(1, 10))

    # Learning Outcomes Block
    story.append(Paragraph("<b>TOPIC 1 LEARNING OUTCOMES (BLOOM'S TAXONOMY ALIGNED)</b>", styles['SecH2']))
    story.append(Paragraph(
        "Upon thorough study of this compendium and active participation in laboratory sessions, first-year students will be able to:<br/>"
        "• <b>Remember & Define:</b> Accurately define a computer, microcomputer, data, information, hardware, software, user, and communication within the Information Processing Cycle (IPOS+C).<br/>"
        "• <b>Understand & Explain:</b> Describe the conceptual architecture of the Von Neumann model (Control Unit, ALU, Registers, Primary Memory, and System Buses) and narrate the step-by-step Fetch-Decode-Execute machine cycle.<br/>"
        "• <b>Trace Historical Evolution:</b> Characterize the five distinct computer generations in terms of their core electronic technology (vacuum tubes, transistors, integrated circuits, microprocessors, and artificial intelligence) and identify pivotal contributions by computing pioneers.<br/>"
        "• <b>Classify & Distinguish:</b> Differentiate among computing classes (microcomputers, workstations, minicomputers/servers, mainframes, supercomputers, and embedded systems) based on processing capability, user concurrency, physical scale, and typical application domains.<br/>"
        "• <b>Apply Cross-Disciplinary Solutions:</b> Analyze how microcomputers solve domain-specific problems across all SUA academic disciplines, including agricultural yield tracking, veterinary clinical records, wildlife ecotourism management, forestry GIS inventories, food quality testing, and rural extension.<br/>"
        "• <b>Demonstrate Laboratory Competence:</b> Adhere to computer laboratory safety and ergonomic standards, recognize external ports and connections, inspect system hardware specifications, and practice proper boot/shutdown hygiene.",
        styles['DocBody']
    ))
    story.append(Spacer(1, 12))

    return story
''')
print("Base header written.")
