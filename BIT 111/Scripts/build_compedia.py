#!/usr/bin/env python3
"""
build_compedia.py
Master Compendium Builder for BIT 111: Microcomputers and Applications
Department of Informatics and Information Technology (DIIT),
Sokoine University of Agriculture (SUA).

Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Generates comprehensive, publication-quality academic compendia (minimum 35 pages each)
for all 6 course topics in accordance with SUA engineering and informatics standards.
"""

import os
import sys

LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib import colors
from compendium_base import (
    get_custom_stylesheet, create_custom_table, create_callout_box, create_example_box,
    create_code_box, create_figure_box, render_pdf,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_SUA_GREEN, COLOR_WHITE
)

def create_topic_header(topic_num, topic_title, subtopics_str):
    styles = get_custom_stylesheet()
    header_data = [
        [Paragraph("SOKOINE UNIVERSITY OF AGRICULTURE", styles['CoverUniv'])],
        [Paragraph("School of Engineering and Technology / College of Natural and Applied Sciences", styles['CoverDept'])],
        [Paragraph("Department of Informatics and Information Technology (DIIT)", styles['CoverDept'])],
        [Spacer(1, 4)],
        [Paragraph(f"BIT 111: MICROCOMPUTERS AND APPLICATIONS", styles['CourseCode'])],
        [Paragraph(f"TOPIC {topic_num}: {topic_title.upper()} — COMPREHENSIVE LECTURE COMPENDIUM", styles['CourseTitle'])],
        [Paragraph(
            f"<b>Course Instructor:</b> Madam Bertha Msuliche Lebalwa (MSc)<br/>"
            f"<b>Department:</b> Informatics and Information Technology (DIIT), SUA Morogoro<br/>"
            f"<b>Target Audience:</b> First-Year Undergraduate Degree Students at SUA<br/>"
            f"<b>Curriculum Coverage:</b> {subtopics_str}<br/>"
            f"<b>Standard Academic Reference Edition</b> — Academic Year 2026/2027",
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
    return tbl

print("build_compedia base ready")
