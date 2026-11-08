#!/usr/bin/env python3
"""
compendium_base.py
Shared styling, typography, page layouts, and PDF generation pipeline for:
BIT 111: Microcomputers and Applications
Department of Informatics and Information Technology (DIIT),
School of Engineering and Technology / College of Natural and Applied Sciences,
Sokoine University of Agriculture (SUA), Morogoro, Tanzania.

Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Official SUA Brand Palette: SUA Green (#008836), Forest Green (#005a24), Charcoal, Gold Accent.
TrueType Fonts: DejaVuSans (eliminates all square symbol artifacts).
"""

import os
import sys

# Inject local python libs if present
LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph as _RLParagraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage

# -------------------------------------------------------------
# SCIENTIFIC & TECHNICAL NOTATION RECTIFIER
# -------------------------------------------------------------
def rectify_technical_text(text):
    """Formats technical terminology, superscripts, subscripts, units, and symbols."""
    if not isinstance(text, str):
        return text

    parts = re.split(r'(<[^>]+>)', text)
    rectified = []
    for part in parts:
        if part.startswith('<') and part.endswith('>'):
            rectified.append(part)
            continue
        p = part
        # Superscripts for powers (e.g., 2^10 -> 2<sup>10</sup>, 10^6 -> 10<sup>6</sup>)
        p = re.sub(r'(\b\d+)\^([0-9A-Za-z\+\-]+)', r'\1<sup>\2</sup>', p)
        # Subscripts for bases (e.g., 1010_2 -> 1010<sub>2</sub>, FF_16 -> FF<sub>16</sub>)
        p = re.sub(r'(\b[0-9A-Fa-f]+)_([0-9]+)\b', r'\1<sub>\2</sub>', p)
        # Symbols
        p = p.replace(' >= ', ' ≥ ').replace(' <= ', ' ≤ ').replace(' != ', ' ≠ ')
        p = p.replace(' -> ', ' → ').replace(' <- ', ' ← ').replace(' <-> ', ' ↔ ')
        p = p.replace(' * ', ' · ')
        rectified.append(p)
    return ''.join(rectified)

def ScientificParagraph(text, *args, **kwargs):
    if isinstance(text, str):
        text = rectify_technical_text(text)
    return _RLParagraph(text, *args, **kwargs)

Paragraph = ScientificParagraph

# -------------------------------------------------------------
# FONT REGISTRATION (DEJAVUSANS)
# -------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
FONT_NORMAL = "DejaVuSans"
FONT_BOLD = "DejaVuSans-Bold"
FONT_OBLIQUE = "DejaVuSans-Oblique"
FONT_BOLDOBLIQUE = "DejaVuSans-BoldOblique"

if os.path.exists(os.path.join(FONT_DIR, "DejaVuSans.ttf")):
    pdfmetrics.registerFont(TTFont(FONT_NORMAL, os.path.join(FONT_DIR, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_OBLIQUE, os.path.join(FONT_DIR, "DejaVuSans-Oblique.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_BOLDOBLIQUE, os.path.join(FONT_DIR, "DejaVuSans-BoldOblique.ttf")))
else:
    FONT_NORMAL = "Helvetica"
    FONT_BOLD = "Helvetica-Bold"
    FONT_OBLIQUE = "Helvetica-Oblique"
    FONT_BOLDOBLIQUE = "Helvetica-BoldOblique"

# -------------------------------------------------------------
# SUA COLOR PALETTE
# -------------------------------------------------------------
COLOR_SUA_GREEN = colors.HexColor("#008836")      # Official SUA Logo Green
COLOR_SUA_DARKGREEN = colors.HexColor("#005a24")  # Deep Forest Green
COLOR_BLACK = colors.HexColor("#000000")          # Pure Black
COLOR_TEXT = colors.HexColor("#111827")           # Dark Charcoal body text
COLOR_MUTED = colors.HexColor("#4b5563")          # Slate gray
COLOR_BG_LIGHT = colors.HexColor("#f8faf8")       # Crisp off-white
COLOR_CALLOUT_BG = colors.HexColor("#f0fdf4")     # Very light green tint
COLOR_CALLOUT_BORDER = colors.HexColor("#008836") # Green border
COLOR_EX_BG = colors.HexColor("#f9fafb")          # Neutral gray background
COLOR_EX_BORDER = colors.HexColor("#008836")      # Green border
COLOR_BORDER = colors.HexColor("#d1d5db")         # Clean gray border
COLOR_WHITE = colors.HexColor("#ffffff")
COLOR_CODE_BG = colors.HexColor("#1e293b")        # Dark slate for code
COLOR_CODE_TEXT = colors.HexColor("#f8fafc")      # White/light text
COLOR_WARN_BG = colors.HexColor("#fffbeb")        # Amber warn
COLOR_WARN_BORDER = colors.HexColor("#f59e0b")

# Aliases
COLOR_PRIMARY = COLOR_SUA_GREEN
COLOR_SECONDARY = COLOR_SUA_DARKGREEN
COLOR_ACCENT = COLOR_SUA_GREEN

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Figures"))
SUA_LOGO_PATH = os.path.join(FIGURES_DIR, "SUA.png")
if not os.path.exists(SUA_LOGO_PATH):
    SUA_LOGO_PATH = "/home/kadefue/Course_Notes/SUA.png"

# -------------------------------------------------------------
# TWO-PASS NUMBERED CANVAS WITH SUA LOGO
# -------------------------------------------------------------
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.doc_title = kwargs.get('doc_title', 'BIT 111: Microcomputers and Applications')

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_decorations(self, total_pages):
        self.saveState()
        page_num = self._pageNumber

        # Header on page 2+
        if page_num > 1:
            if os.path.exists(SUA_LOGO_PATH):
                self.drawImage(SUA_LOGO_PATH, 46, 11 * inch - 46, width=24, height=24, mask='auto', preserveAspectRatio=True)

            self.setFont(FONT_BOLD, 8)
            self.setFillColor(COLOR_SUA_GREEN)
            self.drawString(76, 11 * inch - 36, "SOKOINE UNIVERSITY OF AGRICULTURE")
            self.setFont(FONT_NORMAL, 7.2)
            self.setFillColor(COLOR_TEXT)
            self.drawString(76, 11 * inch - 46, "Dept. of Informatics & IT | BIT 111: Microcomputers and Applications")

            self.setFont(FONT_NORMAL, 7.2)
            self.setFillColor(COLOR_MUTED)
            self.drawRightString(8.5 * inch - 46, 11 * inch - 36, "Lecture Compendium")

            # Header rule
            self.setStrokeColor(COLOR_SUA_GREEN)
            self.setLineWidth(1.0)
            self.line(46, 11 * inch - 50, 8.5 * inch - 46, 11 * inch - 50)

        # Footer on all pages
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.75)
        self.line(46, 42, 8.5 * inch - 46, 42)

        self.setFont(FONT_NORMAL, 7.2)
        self.setFillColor(COLOR_MUTED)
        self.drawString(46, 30, "BIT 111 Microcomputers and Applications | Instructor: Madam Bertha Msuliche Lebalwa (MSc) - SUA Morogoro")
        self.drawRightString(8.5 * inch - 46, 30, f"Page {page_num} of {total_pages}")

        self.restoreState()

# -------------------------------------------------------------
# TYPOGRAPHICAL STYLESHEET
# -------------------------------------------------------------
def get_custom_stylesheet():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'CoverUniv',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=12,
        leading=15,
        alignment=TA_CENTER,
        textColor=COLOR_SUA_GREEN
    ))

    styles.add(ParagraphStyle(
        'CoverDept',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=9.5,
        leading=13,
        alignment=TA_CENTER,
        textColor=COLOR_BLACK
    ))

    styles.add(ParagraphStyle(
        'CourseCode',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        textColor=COLOR_SUA_GREEN
    ))

    styles.add(ParagraphStyle(
        'CourseTitle',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=12.5,
        leading=16,
        alignment=TA_CENTER,
        textColor=COLOR_BLACK
    ))

    styles.add(ParagraphStyle(
        'MetaBox',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=8.5,
        leading=12,
        alignment=TA_CENTER,
        textColor=COLOR_TEXT
    ))

    styles.add(ParagraphStyle(
        'SecH1',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=13.5,
        leading=17,
        spaceBefore=14,
        spaceAfter=6,
        textColor=COLOR_SUA_GREEN,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'SecH2',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=11.5,
        leading=15,
        spaceBefore=10,
        spaceAfter=4,
        textColor=COLOR_SUA_DARKGREEN,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'SecH3',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=10.0,
        leading=13.5,
        spaceBefore=8,
        spaceAfter=3,
        textColor=COLOR_TEXT,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=10.0,
        leading=14.8,
        spaceBefore=4,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        textColor=COLOR_TEXT
    ))

    styles.add(ParagraphStyle(
        'DocBodyBold',
        parent=styles['DocBody'],
        fontName=FONT_BOLD
    ))

    styles.add(ParagraphStyle(
        'DocBullet',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=9.8,
        leading=14.2,
        spaceBefore=3,
        spaceAfter=4,
        leftIndent=16,
        textColor=COLOR_TEXT
    ))

    styles.add(ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=9.0,
        leading=12.5,
        alignment=TA_CENTER,
        textColor=COLOR_WHITE
    ))

    styles.add(ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=9.0,
        leading=12.5,
        textColor=COLOR_TEXT
    ))

    styles.add(ParagraphStyle(
        'TblCellBold',
        parent=styles['TblCell'],
        fontName=FONT_BOLD
    ))

    styles.add(ParagraphStyle(
        'CalloutTitle',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=9.8,
        leading=13.5,
        textColor=COLOR_SUA_DARKGREEN
    ))

    styles.add(ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=9.2,
        leading=13.5,
        alignment=TA_JUSTIFY,
        textColor=COLOR_TEXT
    ))

    styles.add(ParagraphStyle(
        'CodeText',
        parent=styles['Normal'],
        fontName="Courier",
        fontSize=8.0,
        leading=10.5,
        textColor=COLOR_CODE_TEXT
    ))

    styles.add(ParagraphStyle(
        'FigCaption',
        parent=styles['Normal'],
        fontName=FONT_OBLIQUE,
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=COLOR_MUTED
    ))

    return styles

# -------------------------------------------------------------
# TABLE, CALLOUT & BOX HELPERS
# -------------------------------------------------------------
def create_custom_table(headers, rows, col_widths=None):
    """Creates an SUA Green styled reference table."""
    styles = get_custom_stylesheet()
    hdr_cells = [Paragraph(h, styles['TblHdr']) for h in headers]
    data = [hdr_cells]

    for row in rows:
        row_cells = []
        for c in row:
            if isinstance(c, str):
                row_cells.append(Paragraph(c, styles['TblCell']))
            else:
                row_cells.append(c)
        data.append(row_cells)

    tbl = Table(data, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_SUA_GREEN),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_WHITE, COLOR_BG_LIGHT]),
    ]))
    return tbl

def create_callout_box(title, text, *args, kind="info", box_type=None, **kwargs):
    """Creates a highlighted callout box (Green for info/takeaway/sua, Amber for warning)."""
    styles = get_custom_stylesheet()
    if box_type:
        kind = "info" if box_type in ("info", "sua", "note") else "warning"
    bg = COLOR_CALLOUT_BG if kind == "info" else COLOR_WARN_BG
    border = COLOR_CALLOUT_BORDER if kind == "info" else COLOR_WARN_BORDER

    content = [
        Paragraph(f"<b>{title}</b>", styles['CalloutTitle']),
        Spacer(1, 2),
        Paragraph(text, styles['CalloutText'])
    ]
    tbl = Table([[content]], colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('BOX', (0, 0), (-1, -1), 1.0, border),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    return tbl

def create_example_box(title, problem_text, solution_text):
    """Creates a structured Worked Example & Application Scenario box."""
    styles = get_custom_stylesheet()
    content = [
        Paragraph(f"<b>WORKED EXAMPLE / PRACTICAL SCENARIO: {title}</b>", styles['CalloutTitle']),
        Spacer(1, 3),
        Paragraph(f"<b>Scenario / Problem Statement:</b><br/>{problem_text}", styles['DocBody']),
        Spacer(1, 3),
        Paragraph(f"<b>Technical Solution & Analysis:</b><br/>{solution_text}", styles['DocBody'])
    ]
    tbl = Table([[content]], colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_EX_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, COLOR_EX_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    return tbl

def create_code_box(code_str, caption=None):
    """Creates a dark terminal / syntax highlighted code box."""
    styles = get_custom_stylesheet()
    elements = []
    if caption:
        elements.append(Paragraph(f"<b>Command Syntax / Script: {caption}</b>", styles['CalloutTitle']))
        elements.append(Spacer(1, 2))

    # Replace newlines with <br/> for ReportLab Paragraph
    formatted_code = "<font face='Courier' size='7.5' color='#38bdf8'>" + code_str.replace("\n", "<br/>&nbsp;&nbsp;") + "</font>"
    elements.append(Paragraph(formatted_code, styles['DocBody']))

    tbl = Table([[elements]], colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_CODE_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor("#0f172a")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    return tbl

def create_figure_box(img_filename, caption, width=5.5*inch, height=2.6*inch):
    """Safely loads an image from Figures/ and wraps with an academic caption."""
    styles = get_custom_stylesheet()
    img_path = os.path.join(FIGURES_DIR, img_filename)
    if not os.path.exists(img_path):
        # Fallback to placeholder table if image not yet generated
        tbl = Table([[Paragraph(f"<b>[Figure: {caption}]</b><br/>(Refer to course media directory: {img_filename})", styles['FigCaption'])]], colWidths=[width])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_LIGHT),
            ('BOX', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        return KeepTogether([tbl, Spacer(1, 4)])

    elements = [
        Image(img_path, width=width, height=height),
        Spacer(1, 2),
        Paragraph(f"<b>Figure:</b> {caption}", styles['FigCaption']),
        Spacer(1, 4)
    ]
    return KeepTogether(elements)

# -------------------------------------------------------------
# BUILD PDF ORCHESTRATOR
# -------------------------------------------------------------
def render_pdf(filename, story, doc_title="BIT 111: Microcomputers and Applications"):
    """Compiles the complete document to Notes/ using NumberedCanvas."""
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Notes"))
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename)

    doc = SimpleDocTemplate(
        out_path,
        pagesize=letter,
        leftMargin=46,
        rightMargin=46,
        topMargin=54,
        bottomMargin=46
    )
    doc.build(story, canvasmaker=lambda *args, **kwargs: NumberedCanvas(*args, doc_title=doc_title, **kwargs))
    print(f"[Success] Generated {out_path} ({os.path.getsize(out_path)} bytes)")
    return out_path
