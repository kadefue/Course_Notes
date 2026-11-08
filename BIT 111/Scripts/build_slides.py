#!/usr/bin/env python3
"""
build_slides.py
Generates comprehensive, professional 16:9 widescreen PowerPoint (.pptx) presentations
and converts them to PDF for all 6 topics of:
BIT 111: MICROCOMPUTERS AND APPLICATIONS
Department of Informatics and Information Technology (DIIT),
Sokoine University of Agriculture (SUA), Morogoro, Tanzania.

Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Requirements: Strictly >= 30 slides per topic (32-35 slides per deck).
Converts PPTX to PDF via LibreOffice headless.
"""

import os
import sys
import subprocess
import json

LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image as PILImage

LECTURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Lectures"))
FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Figures"))
INTERNET_FIGURES_DIR = os.path.join(FIGURES_DIR, "Internet")
ATTRIBUTIONS_FILE = os.path.join(INTERNET_FIGURES_DIR, "attributions.json")
os.makedirs(LECTURES_DIR, exist_ok=True)

# Official SUA Brand Colors
SUA_GREEN = RGBColor(0, 136, 54)        # #008836 Official SUA Logo Green
SUA_DARKGREEN = RGBColor(0, 90, 36)     # #005a24 Forest Green
SUA_LIGHT_BG = RGBColor(248, 250, 248)  # #f8faf8 Crisp light off-white
COLOR_TEXT = RGBColor(17, 24, 39)       # #111827 Charcoal Dark Body
COLOR_MUTED = RGBColor(75, 85, 99)      # #4b5563 Medium Slate Gray
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_CARD_BG = RGBColor(240, 253, 244) # #f0fdf4 Very light green tint
COLOR_BORDER = RGBColor(209, 213, 219)  # #d1d5db Light gray border
COLOR_ACCENT = RGBColor(16, 185, 129)   # Accent green

SUA_LOGO_PATH = os.path.join(FIGURES_DIR, "SUA.png")
if not os.path.exists(SUA_LOGO_PATH):
    SUA_LOGO_PATH = "/home/kadefue/Course_Notes/SUA.png"

def init_presentation():
    """Initializes 16:9 widescreen presentation."""
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_header(slide, title_text, category_text="BIT 111: MICROCOMPUTERS AND APPLICATIONS"):
    """Adds standard SUA Green header banner, course subtitle, slide title, and SUA logo."""
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = SUA_GREEN
    banner.line.color.rgb = SUA_DARKGREEN
    banner.line.width = Pt(1.5)

    if os.path.exists(SUA_LOGO_PATH):
        try:
            slide.shapes.add_picture(SUA_LOGO_PATH, Inches(0.4), Inches(0.12), height=Inches(0.85))
        except Exception:
            pass

    tx_box = slide.shapes.add_textbox(Inches(1.4), Inches(0.08), Inches(11.5), Inches(0.95))
    tf = tx_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_sub = tf.paragraphs[0]
    p_sub.text = category_text.upper() + " | SOKOINE UNIVERSITY OF AGRICULTURE"
    p_sub.font.size = Pt(10.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = RGBColor(220, 252, 231)

    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.size = Pt(20)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE

def add_footer(slide, current_idx, total_slides):
    """Adds standard bottom footer."""
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(6.9), Inches(12.333), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_BORDER
    line.line.fill.background()

    tx_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.95), Inches(12.333), Inches(0.4))
    tf = tx_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.text = f"BIT 111: Microcomputers and Applications | Instructor: Madam Bertha Msuliche Lebalwa (MSc) - SUA Morogoro"
    p.font.size = Pt(9.5)
    p.font.color.rgb = COLOR_MUTED

    p2 = tf.add_paragraph()
    p2.text = f"Slide {current_idx} of {total_slides}"
    p2.font.size = Pt(9.5)
    p2.font.bold = True
    p2.font.color.rgb = SUA_GREEN
    p2.alignment = PP_ALIGN.RIGHT
    tx_box.top = Inches(6.95)

def make_title_slide(prs, topic_num, title, subtopics, total_slides):
    """Generates the official title slide."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SUA_LIGHT_BG
    bg.line.fill.background()

    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(2.2))
    banner.fill.solid()
    banner.fill.fore_color.rgb = SUA_GREEN
    banner.line.color.rgb = SUA_DARKGREEN
    banner.line.width = Pt(2.0)

    if os.path.exists(SUA_LOGO_PATH):
        try:
            slide.shapes.add_picture(SUA_LOGO_PATH, Inches(0.8), Inches(0.35), height=Inches(1.5))
        except Exception:
            pass

    tbox = slide.shapes.add_textbox(Inches(2.5), Inches(0.3), Inches(10.2), Inches(1.6))
    tf = tbox.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "SOKOINE UNIVERSITY OF AGRICULTURE"
    p0.font.size = Pt(15)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(220, 252, 231)

    p1 = tf.add_paragraph()
    p1.text = "Department of Informatics and Information Technology (DIIT)"
    p1.font.size = Pt(12)
    p1.font.color.rgb = COLOR_WHITE

    p2 = tf.add_paragraph()
    p2.text = "BIT 111: MICROCOMPUTERS AND APPLICATIONS"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_WHITE

    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(2.6), Inches(11.333), Inches(3.8))
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_WHITE
    card.line.color.rgb = SUA_GREEN
    card.line.width = Pt(1.5)

    cbox = slide.shapes.add_textbox(Inches(1.3), Inches(2.8), Inches(10.7), Inches(3.4))
    ctf = cbox.text_frame
    ctf.word_wrap = True

    cp1 = ctf.paragraphs[0]
    cp1.text = f"TOPIC {topic_num}: {title.upper()}"
    cp1.font.size = Pt(24)
    cp1.font.bold = True
    cp1.font.color.rgb = SUA_GREEN

    cp2 = ctf.add_paragraph()
    cp2.text = "Official Undergraduate Lecture Slide Deck (Academic Year 2026/2027)"
    cp2.font.size = Pt(13)
    cp2.font.color.rgb = COLOR_MUTED

    ctf.add_paragraph()

    cp3 = ctf.add_paragraph()
    cp3.text = f"• Curriculum Coverage: {subtopics}"
    cp3.font.size = Pt(12.5)
    cp3.font.color.rgb = COLOR_TEXT

    cp4 = ctf.add_paragraph()
    cp4.text = f"• Course Instructor: Madam Bertha Msuliche Lebalwa (MSc)"
    cp4.font.size = Pt(13)
    cp4.font.bold = True
    cp4.font.color.rgb = SUA_DARKGREEN

    cp5 = ctf.add_paragraph()
    cp5.text = "• Assessment Structure: 2 Assignments (5%), 2 Tests (15%), Practical Report (10%), Practical Test (30%), UE (40%)*"
    cp5.font.size = Pt(11.5)
    cp5.font.color.rgb = COLOR_TEXT

    cp6 = ctf.add_paragraph()
    cp6.text = "*Assessment weightings are subject to adjustment by the course instructor."
    cp6.font.size = Pt(10)
    cp6.font.italic = True
    cp6.font.color.rgb = COLOR_MUTED

    add_footer(slide, 1, total_slides)

def make_bullet_slide(prs, title, bullets, current_idx, total_slides, sub_title=None, callout=None):
    """Standard content slide with bullet points and optional callout card."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, title)

    left_w = Inches(12.333) if not callout else Inches(8.3)

    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.3), left_w, Inches(5.4))
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_WHITE
    card.line.color.rgb = COLOR_BORDER
    card.line.width = Pt(1)

    tbox = slide.shapes.add_textbox(Inches(0.7), Inches(1.4), left_w - Inches(0.4), Inches(5.1))
    tf = tbox.text_frame
    tf.word_wrap = True

    first = True
    if sub_title:
        p = tf.paragraphs[0]
        p.text = sub_title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = SUA_GREEN
        first = False

    for b in bullets:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()

        is_sub = b.startswith("    - ") or b.startswith("      * ")
        p.text = b
        p.font.size = Pt(11.5 if is_sub else 13)
        p.space_after = Pt(4 if is_sub else 8)
        p.font.color.rgb = COLOR_TEXT
        if b.startswith("• <b>") or b.startswith("• **"):
            p.font.bold = True

    if callout:
        ccard = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.0), Inches(1.3), Inches(3.833), Inches(5.4))
        ccard.fill.solid()
        ccard.fill.fore_color.rgb = COLOR_CARD_BG
        ccard.line.color.rgb = SUA_GREEN
        ccard.line.width = Pt(1.2)

        ctbox = slide.shapes.add_textbox(Inches(9.2), Inches(1.5), Inches(3.433), Inches(5.0))
        ctf = ctbox.text_frame
        ctf.word_wrap = True

        cp0 = ctf.paragraphs[0]
        cp0.text = callout.get("title", "KEY TAKEAWAY").upper()
        cp0.font.size = Pt(13)
        cp0.font.bold = True
        cp0.font.color.rgb = SUA_DARKGREEN

        cp1 = ctf.add_paragraph()
        cp1.text = callout.get("body", "")
        cp1.font.size = Pt(11)
        cp1.font.color.rgb = COLOR_TEXT
        cp1.space_before = Pt(8)

    add_footer(slide, current_idx, total_slides)

def make_figure_slide(prs, title, img_filename, caption, bullets, current_idx, total_slides):
    """Slide with an embedded architectural diagram and explanatory points."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, title)

    # Left: Image container
    img_path = os.path.join(FIGURES_DIR, img_filename)
    if os.path.exists(img_path):
        try:
            slide.shapes.add_picture(img_path, Inches(0.6), Inches(1.4), width=Inches(6.4))
        except Exception:
            pass

    # Image caption box
    cap_box = slide.shapes.add_textbox(Inches(0.6), Inches(5.8), Inches(6.4), Inches(0.9))
    ctf = cap_box.text_frame
    ctf.word_wrap = True
    cp = ctf.paragraphs[0]
    cp.text = f"Figure: {caption}"
    cp.font.size = Pt(10.5)
    cp.font.italic = True
    cp.font.color.rgb = COLOR_MUTED
    cp.alignment = PP_ALIGN.CENTER

    # Right: Analysis Card
    rcard = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(1.3), Inches(5.6), Inches(5.4))
    rcard.fill.solid()
    rcard.fill.fore_color.rgb = COLOR_WHITE
    rcard.line.color.rgb = SUA_GREEN
    rcard.line.width = Pt(1.2)

    rtbox = slide.shapes.add_textbox(Inches(7.4), Inches(1.5), Inches(5.2), Inches(5.0))
    rtf = rtbox.text_frame
    rtf.word_wrap = True

    rp0 = rtf.paragraphs[0]
    rp0.text = "ARCHITECTURAL ANALYSIS & PRINCIPLES"
    rp0.font.size = Pt(14)
    rp0.font.bold = True
    rp0.font.color.rgb = SUA_GREEN

    for b in bullets:
        p = rtf.add_paragraph()
        p.text = b
        p.font.size = Pt(11.5)
        p.space_after = Pt(6)
        p.font.color.rgb = COLOR_TEXT

    add_footer(slide, current_idx, total_slides)

def make_table_slide(prs, title, headers, rows, current_idx, total_slides, col_widths=None):
    """Slide containing a structured data comparison table."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, title)

    num_rows = len(rows) + 1
    num_cols = len(headers)

    t_shape = slide.shapes.add_table(num_rows, num_cols, Inches(0.5), Inches(1.4), Inches(12.333), Inches(5.2))
    table = t_shape.table

    if col_widths and len(col_widths) == num_cols:
        for idx, w in enumerate(col_widths):
            table.columns[idx].width = Inches(w)

    # Style Header
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = SUA_GREEN
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE
        p.alignment = PP_ALIGN.CENTER

    # Rows
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 0 else COLOR_CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = str(val)
            p.font.size = Pt(10)
            p.font.color.rgb = COLOR_TEXT
            if c_idx == 0:
                p.font.bold = True

    add_footer(slide, current_idx, total_slides)

def make_internet_figure_slide(prs, topic_num, figure, current_idx, total_slides):
    """Adds an online image with creator, license, and source attribution."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, f"Topic {topic_num}: {figure['title']}")

    image_path = os.path.join(INTERNET_FIGURES_DIR, figure["filename"])
    with PILImage.open(image_path) as source_image:
        image_width, image_height = source_image.size
    max_width, max_height = 6.7, 4.9
    scale = min(max_width / image_width, max_height / image_height)
    width, height = image_width * scale, image_height * scale
    x = 0.5 + (max_width - width) / 2
    y = 1.35 + (max_height - height) / 2
    slide.shapes.add_picture(
        image_path,
        Inches(x),
        Inches(y),
        width=Inches(width),
        height=Inches(height),
    )

    panel = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(7.5),
        Inches(1.35),
        Inches(5.3),
        Inches(5.2),
    )
    panel.fill.solid()
    panel.fill.fore_color.rgb = COLOR_WHITE
    panel.line.color.rgb = SUA_GREEN
    panel.line.width = Pt(1.2)

    textbox = slide.shapes.add_textbox(
        Inches(7.75), Inches(1.6), Inches(4.8), Inches(4.7)
    )
    frame = textbox.text_frame
    frame.word_wrap = True
    frame.clear()

    title = frame.paragraphs[0]
    title.text = "IMAGE NOTES"
    title.font.size = Pt(15)
    title.font.bold = True
    title.font.color.rgb = SUA_GREEN

    details = [
        (
            "Description",
            (figure.get("description") or figure["title"])[:260],
        ),
        ("Creator", figure.get("creator", "Creator not credited on file page")),
        ("License", figure["license"]),
    ]
    for label, value in details:
        paragraph = frame.add_paragraph()
        paragraph.text = f"{label}: {value}"
        paragraph.font.size = Pt(11)
        paragraph.font.color.rgb = COLOR_TEXT
        paragraph.space_before = Pt(12)

    source = frame.add_paragraph()
    source.text = "Source: Wikimedia Commons file page"
    source.font.size = Pt(11)
    source.font.color.rgb = SUA_DARKGREEN
    source.runs[0].hyperlink.address = figure["source_url"]

    license_url = figure.get("license_url")
    if license_url:
        license_paragraph = frame.add_paragraph()
        license_paragraph.text = "License details"
        license_paragraph.font.size = Pt(11)
        license_paragraph.font.color.rgb = SUA_DARKGREEN
        license_paragraph.runs[0].hyperlink.address = license_url

    add_footer(slide, current_idx, total_slides)

def build_topic_slides(topic_num, topic_title, subtopics_str, slides_data):
    """Assembles and saves a >=30 slide deck for a topic."""
    if not os.path.isfile(ATTRIBUTIONS_FILE):
        raise FileNotFoundError(
            "Internet figure attributions are missing. Run "
            "Scripts/prepare_internet_figures.py first."
        )
    with open(ATTRIBUTIONS_FILE, encoding="utf-8") as file:
        figures = json.load(file).get(str(topic_num), [])
    if len(figures) < 8:
        raise RuntimeError(f"Topic {topic_num} has fewer than eight licensed figures.")
    for figure in figures[:8]:
        if not os.path.isfile(os.path.join(INTERNET_FIGURES_DIR, figure["filename"])):
            raise FileNotFoundError(f"Missing internet figure: {figure['filename']}")

    prs = init_presentation()
    total_slides = len(slides_data) + 1 + 8

    # Slide 1: Title
    make_title_slide(prs, topic_num, topic_title, subtopics_str, total_slides)

    # Slides 2..N
    for idx, s in enumerate(slides_data, start=2):
        stype = s.get("type", "bullet")
        if stype == "bullet":
            make_bullet_slide(
                prs, s["title"], s["bullets"], idx, total_slides,
                sub_title=s.get("sub_title"), callout=s.get("callout")
            )
        elif stype == "figure":
            make_figure_slide(
                prs, s["title"], s["img"], s["caption"], s["bullets"],
                idx, total_slides
            )
        elif stype == "table":
            make_table_slide(
                prs, s["title"], s["headers"], s["rows"], idx, total_slides,
                col_widths=s.get("col_widths")
            )

    first_figure_slide = len(slides_data) + 2
    for idx, figure in enumerate(figures[:8], start=first_figure_slide):
        make_internet_figure_slide(prs, topic_num, figure, idx, total_slides)

    if len(prs.slides) < 30:
        raise RuntimeError(f"Topic {topic_num} deck has fewer than 30 slides.")
    pptx_path = os.path.join(LECTURES_DIR, f"BIT_111_Topic_{topic_num}.pptx")
    prs.save(pptx_path)
    print(f"[Success] Saved PPTX: {pptx_path} ({len(prs.slides)} slides)")

    # Headless conversion to PDF
    try:
        cmd = [
            "libreoffice", "-env:UserInstallation=file:///tmp/LibreOffice_Conversion",
            "--headless", "--convert-to", "pdf",
            "--outdir", LECTURES_DIR, pptx_path
        ]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        pdf_path = os.path.join(LECTURES_DIR, f"BIT_111_Topic_{topic_num}.pdf")
        if os.path.exists(pdf_path):
            print(f"[Success] Converted to PDF: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    except Exception as e:
        print(f"[Warning] LibreOffice PDF conversion failed: {e}")

    return pptx_path

def build_all_slides():
    from slides_topics_1_to_3 import get_topic_1_slides, get_topic_2_slides, get_topic_3_slides
    from slides_topics_4_to_6 import get_topic_4_slides, get_topic_5_slides, get_topic_6_slides

    print("=" * 60)
    print("BUILDING 6 16:9 PRESENTATION SLIDE DECKS FOR BIT 111")
    print("=" * 60)

    # Topic 1
    t1_slides = get_topic_1_slides()
    build_topic_slides(
        1, "Introduction to Computers",
        "Generations (1.1) | History & Pioneers (1.2) | Classifications (1.3)",
        t1_slides
    )

    # Topic 2
    t2_slides = get_topic_2_slides()
    build_topic_slides(
        2, "Main Components of a Microcomputer",
        "Devices & Configurations (2.1) | Comparative Aspects (2.2)",
        t2_slides
    )

    # Topic 3
    t3_slides = get_topic_3_slides()
    build_topic_slides(
        3, "Personal Computer (PC) Security Controls",
        "Hard Disk Passwords (3.1) | BIOS/UEFI & TPM (3.2) | Access Controls (3.3)",
        t3_slides
    )

    # Topic 4
    t4_slides = get_topic_4_slides()
    build_topic_slides(
        4, "Functions and Types of Operating Systems",
        "OS Evolution & Categories (4.1) | DOS Commands (4.2) | GUI Management (4.3)",
        t4_slides
    )

    # Topic 5
    t5_slides = get_topic_5_slides()
    build_topic_slides(
        5, "Microcomputer Applications",
        "Word Processors (5.1) | Spreadsheets (5.2) | Web & Email Protocols (5.3)",
        t5_slides
    )

    # Topic 6
    t6_slides = get_topic_6_slides()
    build_topic_slides(
        6, "Data Security and Malware Defense",
        "Physical Protection (6.1) | Unauthorized Access & Crypto (6.2) | Malware Defense (6.3)",
        t6_slides
    )

    print("=" * 60)
    print("ALL 6 SLIDE DECKS GENERATED AND CONVERTED TO PDF")
    print("=" * 60)

if __name__ == "__main__":
    build_all_slides()
