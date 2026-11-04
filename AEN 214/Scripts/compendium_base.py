#!/usr/bin/env python3
"""
compendium_base.py
Shared formatting, typography, styling, and structural components for
AEN 214: Introduction to Electronics lecture compendia and documents.
Department of Agricultural Engineering, Sokoine University of Agriculture (SUA).
Utilizes SUA Brand Colors: SUA Green (#008836), Black, and White.
Features DejaVuSans TrueType fonts for flawless mathematical/Greek symbol rendering (no black spots).
Embeds SUA.png logo on every page header.
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph as _RLParagraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage

# -------------------------------------------------------------
# RIGOROUS SCIENTIFIC FORMULA RECTIFIER
# -------------------------------------------------------------
def rectify_scientific_text(text):
    """
    Rigorously rectifies text to standard scientific notation:
    - Never uses raw '_' or '^' for subscript or superscript.
    - Uses HTML <sub>...</sub> and <sup>...</sup> for true sub/superscripts.
    - Italicizes mathematical variables (V, I, R, C, L, t, f, etc.).
    - Converts Greek symbol names to Unicode (π, μ, τ, β, α, γ, λ, θ, Ω, etc.).
    - Standardizes scientific multiplication (×, ·) and units.
    """
    if not isinstance(text, str):
        return text

    # Split by HTML tags to leave existing tags untouched
    parts = re.split(r'(<[^>]+>)', text)
    rectified_parts = []
    
    for part in parts:
        if part.startswith('<') and part.endswith('>'):
            rectified_parts.append(part)
            continue
            
        p = part

        # 1. Superscripts with ^
        p = re.sub(r'(\b[0-9A-Za-z\)]+)\^\{([^\}]+)\}', r'\1<sup>\2</sup>', p)
        p = re.sub(r'(\b[0-9A-Za-z\)]+)\^([\-0-9A-Za-z\+]+)', r'\1<sup>\2</sup>', p)

        # 2. Time-dependent / state variables with parentheses: v_C(t), i_L(t), v_L(t), i_C(t)
        p = re.sub(r'\b([VvIi])_([A-Za-z0-9]+)\(([t])\)', r'<i>\1</i><sub>\2</sub>(<i>\3</i>)', p)

        # 3. Complex subscripts with parentheses: V_CE(sat), R_DS(on), V_GS(th), V_BE(sat), I_C(sat), P_Z(max)
        p = re.sub(r'\b([VvRrIiPp])_([A-Za-z0-9]+)\(([A-Za-z0-9]+)\)', r'<i>\1</i><sub>\2(\3)</sub>', p)

        # 4. Standard variable subscripts:
        var_prefixes = ['V', 'v', 'I', 'i', 'R', 'r', 'C', 'c', 'L', 'X', 'Z', 'E', 'n', 'p', 'N', 'P', 'f', 't', 'g', 'm', 'M', 'S', 'G', 'B', 'F', 'Q', 'd', 'k', 'W', 'q', 'Y', 'U']
        for var in var_prefixes:
            pattern = r'(?<![A-Za-z0-9])(' + var + r')_([A-Za-z0-9]+)\b'
            p = re.sub(pattern, r'<i>\1</i><sub>\2</sub>', p)

        # 5. Greek letter subscripts
        p = re.sub(r'(?<![A-Za-z0-9])(tau|beta|alpha|theta|mu|eta|epsilon|gamma|lambda|sigma|rho|phi|Phi)_([A-Za-z0-9]+)\b', r'<i>\1</i><sub>\2</sub>', p)

        # 6. Clean Greek names to Unicode
        p = re.sub(r'\bmu\b', 'μ', p)
        p = re.sub(r'\btheta\b', 'θ', p)
        p = re.sub(r'\btau\b', 'τ', p)
        p = re.sub(r'\bbeta\b', 'β', p)
        p = re.sub(r'\balpha\b', 'α', p)
        p = re.sub(r'\bgamma\b', 'γ', p)
        p = re.sub(r'\blambda\b', 'λ', p)
        p = re.sub(r'\bpi\b', 'π', p)
        p = re.sub(r'\bOhm\b', 'Ω', p)
        p = re.sub(r'\bkOhm\b', 'kΩ', p)
        p = re.sub(r'\bMOhm\b', 'MΩ', p)
        p = re.sub(r'\bmicroFarad\b', 'μF', p)
        p = re.sub(r'\bmicroHenry\b', 'μH', p)
        p = re.sub(r'\bmicroA\b', 'μA', p)
        p = re.sub(r'\bmicroF\b', 'μF', p)
        p = re.sub(r'\bmicroH\b', 'μH', p)
        p = re.sub(r'\bmicro-mol\b', 'μmol', p)
        p = re.sub(r'\bmicrosecond\b', 'μs', p)
        p = re.sub(r'\bmicroseconds\b', 'μs', p)

        # 7. Differences (Delta X)
        p = re.sub(r'\bDelta\s+([A-Za-z])\b', r'Δ<i>\1</i>', p)

        # 8. Scientific multiplication & symbols
        p = re.sub(r'(\d+)\s+x\s+(10<sup>)', r'\1 × \2', p)
        p = p.replace(' * ', ' · ')
        p = p.replace(' >= ', ' ≥ ').replace(' <= ', ' ≤ ')

        rectified_parts.append(p)

    return ''.join(rectified_parts)

def ScientificParagraph(text, *args, **kwargs):
    if isinstance(text, str):
        text = rectify_scientific_text(text)
    return _RLParagraph(text, *args, **kwargs)

Paragraph = ScientificParagraph

# -------------------------------------------------------------
# FONT REGISTRATION (DEJAVUSANS PREVENTS ALL BLACK SPOTS / RECTANGLES)
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
    # Fallback to Helvetica if TrueType not available
    FONT_NORMAL = "Helvetica"
    FONT_BOLD = "Helvetica-Bold"
    FONT_OBLIQUE = "Helvetica-Oblique"
    FONT_BOLDOBLIQUE = "Helvetica-BoldOblique"

# -------------------------------------------------------------
# SUA COLOR PALETTE (GREEN, BLACK, WHITE)
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

# Aliases for compatibility
COLOR_PRIMARY = COLOR_SUA_GREEN
COLOR_SECONDARY = COLOR_SUA_DARKGREEN
COLOR_ACCENT = COLOR_SUA_GREEN
COLOR_DARK = COLOR_TEXT

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Figures"))
SUA_LOGO_PATH = os.path.join(FIGURES_DIR, "SUA.png")
if not os.path.exists(SUA_LOGO_PATH):
    SUA_LOGO_PATH = "/home/kadefue/Course_Notes/SUA.png"

# -------------------------------------------------------------
# NUMBERED CANVAS WITH SUA LOGO ON EVERY PAGE
# -------------------------------------------------------------
class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas that writes dynamic page numbers (Page X of Y),
    draws the SUA.png logo on every page header, and adds institutional rules.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.doc_title = kwargs.get('doc_title', 'AEN 214: Introduction to Electronics')

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
        
        # Draw SUA Logo on every page (top-left on page 2+, header block on page 1)
        if os.path.exists(SUA_LOGO_PATH):
            if page_num > 1:
                # Small running logo in header
                self.drawImage(SUA_LOGO_PATH, 46, 11 * inch - 46, width=24, height=24, mask='auto', preserveAspectRatio=True)
                
                # Header text
                self.setFont(FONT_BOLD, 8)
                self.setFillColor(COLOR_SUA_GREEN)
                self.drawString(76, 11 * inch - 36, "SOKOINE UNIVERSITY OF AGRICULTURE")
                self.setFont(FONT_NORMAL, 7.5)
                self.setFillColor(COLOR_TEXT)
                self.drawString(76, 11 * inch - 45, "Department of Agricultural Engineering | AEN 214: Introduction to Electronics")
                
                self.setFont(FONT_NORMAL, 7.5)
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
        
        self.setFont(FONT_NORMAL, 7.5)
        self.setFillColor(COLOR_MUTED)
        self.drawString(46, 30, "AEN 214 Introduction to Electronics | Electronics & Precision Agriculture Lab (EPAL) - SUA Morogoro")
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
        fontSize=17,
        leading=21,
        alignment=TA_CENTER,
        textColor=COLOR_SUA_DARKGREEN,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        'CourseTitle',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=13,
        leading=17,
        alignment=TA_CENTER,
        textColor=COLOR_BLACK,
        spaceAfter=8
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
        parent=styles['Heading1'],
        fontName=FONT_BOLD,
        fontSize=12,
        leading=15,
        textColor=COLOR_SUA_DARKGREEN,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'SecH2',
        parent=styles['Heading2'],
        fontName=FONT_BOLD,
        fontSize=10,
        leading=13,
        textColor=COLOR_SUA_GREEN,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'SecH3',
        parent=styles['Heading3'],
        fontName=FONT_BOLD,
        fontSize=9,
        leading=12,
        textColor=COLOR_BLACK,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=9.5,
        leading=14.0,
        textColor=COLOR_TEXT,
        alignment=TA_JUSTIFY,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        'DocBullet',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=9.5,
        leading=14.0,
        textColor=COLOR_TEXT,
        leftIndent=16,
        firstLineIndent=-11,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        'FormulaBox',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=9.5,
        leading=13.5,
        alignment=TA_CENTER,
        textColor=COLOR_SUA_DARKGREEN,
        spaceBefore=3,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        'FigCaption',
        parent=styles['Normal'],
        fontName=FONT_OBLIQUE,
        fontSize=8.0,
        leading=11.0,
        alignment=TA_CENTER,
        textColor=COLOR_MUTED,
        spaceBefore=4,
        spaceAfter=8
    ))

    styles.add(ParagraphStyle(
        'CalloutTitle',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=9.0,
        leading=12.5,
        textColor=COLOR_SUA_DARKGREEN,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        'CalloutContent',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=8.5,
        leading=12.5,
        textColor=COLOR_TEXT
    ))

    styles.add(ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName=FONT_BOLD,
        fontSize=8.5,
        leading=11.5,
        alignment=TA_CENTER,
        textColor=COLOR_WHITE
    ))

    styles.add(ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName=FONT_NORMAL,
        fontSize=8.0,
        leading=11.0,
        textColor=COLOR_TEXT
    ))

    return styles


# -------------------------------------------------------------
# FLOWABLE GENERATORS
# -------------------------------------------------------------
def create_banner_header(lecture_num, lecture_title, topics_list):
    """Generates the standardized university title block with SUA logo."""
    styles = get_custom_stylesheet()
    story = []

    # Check if logo exists
    logo_img = []
    if os.path.exists(SUA_LOGO_PATH):
        try:
            logo_img = [Image(SUA_LOGO_PATH, width=54, height=54)]
        except Exception:
            logo_img = []

    text_cells = [
        [Paragraph("SOKOINE UNIVERSITY OF AGRICULTURE", styles['CoverUniv'])],
        [Paragraph("School of Engineering and Technology | Department of Agricultural Engineering", styles['CoverDept'])],
        [Spacer(1, 3)],
        [Paragraph("AEN 214: INTRODUCTION TO ELECTRONICS", styles['CourseCode'])],
        [Paragraph(f"LECTURE COMPENDIUM {lecture_num}: {lecture_title.upper()}", styles['CourseTitle'])],
        [Paragraph("<b>Course Instructor:</b> Dr. Kadeghe Goodluck Fue, PhD, P.Eng (T) | <b>Lab:</b> Electronics & Precision Agriculture Lab (EPAL)<br/>"
                   "<b>Target Cohorts:</b> BSc Agricultural Engineering, BSc IWRE, BSc BPHE | <b>Academic Year:</b> 2025/2026", styles['MetaBox'])]
    ]

    if logo_img:
        banner_table = Table([[logo_img[0], Table(text_cells, colWidths=[6.2 * inch])]], colWidths=[0.9 * inch, 6.3 * inch])
        banner_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_LIGHT),
            ('BOX', (0, 0), (-1, -1), 1.2, COLOR_SUA_GREEN),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
    else:
        banner_table = Table(text_cells, colWidths=[7.2 * inch])
        banner_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_LIGHT),
            ('BOX', (0, 0), (-1, -1), 1.2, COLOR_SUA_GREEN),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ]))

    story.append(banner_table)
    story.append(Spacer(1, 8))

    # Topics covered badge
    topics_html = " &bull; ".join(topics_list)
    topic_bar = Table(
        [[Paragraph(f"<b>Key Curriculum Subtopics:</b> {topics_html}", styles['MetaBox'])]],
        colWidths=[7.2 * inch]
    )
    topic_bar.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_SUA_GREEN),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(topic_bar)
    story.append(Spacer(1, 10))

    return story


def create_callout(title, text, bg_color=COLOR_CALLOUT_BG, border_color=COLOR_CALLOUT_BORDER):
    """Creates a high-contrast educational callout box."""
    styles = get_custom_stylesheet()
    data = [
        [Paragraph(f"<b>{title.upper()}</b>", styles['CalloutTitle'])],
        [Paragraph(text, styles['CalloutContent'])]
    ]
    tbl = Table(data, colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_color),
        ('BOX', (0, 0), (-1, -1), 1.0, border_color),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return KeepTogether([tbl, Spacer(1, 7)])


def create_example(number, title, problem_text, steps):
    """Creates a step-by-step engineering example problem."""
    styles = get_custom_stylesheet()
    body_elements = [
        Paragraph(f"<b>WORKED ENGINEERING EXAMPLE {number}: {title}</b>", styles['CalloutTitle']),
        Spacer(1, 2),
        Paragraph(f"<b>Problem Statement:</b> {problem_text}", styles['CalloutContent']),
        Spacer(1, 3),
        Paragraph("<b>Step-by-Step Technical Derivation & Solution:</b>", styles['CalloutTitle']),
    ]
    for step in steps:
        body_elements.append(Paragraph(f"&bull; {step}", styles['CalloutContent']))
        body_elements.append(Spacer(1, 1.5))

    tbl = Table([[body_elements]], colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_EX_BG),
        ('BOX', (0, 0), (-1, -1), 1.0, COLOR_SUA_GREEN),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return KeepTogether([tbl, Spacer(1, 8)])


def create_figure(filename, caption, target_width=5.5 * inch, max_height=3.0 * inch):
    """Safely loads an image from Figures directory with proportional scaling and caption."""
    styles = get_custom_stylesheet()
    filepath = os.path.join(FIGURES_DIR, filename)
    if not os.path.exists(filepath):
        return Paragraph(f"<i>[Figure {filename} not found]</i>", styles['DocBody'])

    try:
        with PILImage.open(filepath) as im:
            orig_w, orig_h = im.size
            aspect = orig_h / orig_w
            w = target_width
            h = target_width * aspect
            if h > max_height:
                h = max_height
                w = max_height / aspect

        img = Image(filepath, width=w, height=h)
        cap = Paragraph(f"<b>Figure:</b> {caption}", styles['FigCaption'])
        return KeepTogether([img, cap, Spacer(1, 4)])
    except Exception as e:
        return Paragraph(f"<i>[Error embedding figure {filename}: {e}]</i>", styles['DocBody'])


def create_custom_table(headers, rows, col_widths=None):
    """Creates a styled reference table using SUA Green header."""
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
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLOR_WHITE, COLOR_BG_LIGHT]),
    ]))
    return tbl
def create_equation_box(formula_markup, eq_num=None):
    """Creates a high-visibility, centered scientific equation block with equation number."""
    styles = get_custom_stylesheet()
    formula_markup = rectify_scientific_text(formula_markup)
    if eq_num:
        content = [
            [Paragraph(f"<b>{formula_markup}</b>", styles['FormulaBox']),
             Paragraph(f"<b>({eq_num})</b>", styles['FormulaBox'])]
        ]
        tbl = Table(content, colWidths=[6.3 * inch, 0.9 * inch])
    else:
        content = [[Paragraph(f"<b>{formula_markup}</b>", styles['FormulaBox'])]]
        tbl = Table(content, colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_CALLOUT_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_SUA_GREEN),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    return KeepTogether([tbl, Spacer(1, 6)])


def create_formula_summary_table(formula_list):
    """
    Creates a styled scientific formula reference table.
    formula_list: list of [Law / Concept, Formula, Agricultural Engineering Context]
    """
    headers = ["Governing Physical / Circuit Law", "Standard Scientific Equation", "Agricultural Engineering Context"]
    rows = []
    for row in formula_list:
        rows.append([
            rectify_scientific_text(row[0]),
            rectify_scientific_text(row[1]),
            rectify_scientific_text(row[2])
        ])
    return create_custom_table(headers, rows, [2.2 * inch, 2.5 * inch, 2.5 * inch])


def render_pdf(filename, story):

    """Builds the final document with NumberedCanvas."""
    out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Notes", filename))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    doc = SimpleDocTemplate(
        out_path,
        pagesize=letter,
        leftMargin=46,
        rightMargin=46,
        topMargin=54,
        bottomMargin=46
    )
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[Success] Generated {out_path} ({os.path.getsize(out_path)} bytes)")
    return out_path
