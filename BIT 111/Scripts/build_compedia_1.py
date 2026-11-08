#!/usr/bin/env python3
"""
build_compedia_1.py
Comprehensive Academic Lecture Compendium for:
BIT 111: MICROCOMPUTERS AND APPLICATIONS
TOPIC 1: INTRODUCTION TO COMPUTERS
Department of Informatics and Information Technology (DIIT),
Sokoine University of Agriculture (SUA).

Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Target: Minimum 35 Pages of rigorous academic exposition, architectural diagrams,
tables, worked mathematical examples, lab exercises, and self-assessment solutions.
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
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_SUA_GREEN, COLOR_WHITE
)

def build_topic_1():
    styles = get_custom_stylesheet()
    story = []

    # =========================================================
    # TITLE BLOCK / COVER HEADER
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
            "<b>Target Audience:</b> First-Year Undergraduate Degree Students at SUA<br/>"
            "<b>Curriculum Coverage:</b> Computer Generations (1.1) | History & Pioneers (1.2) | Computer Classifications (1.3)<br/>"
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
