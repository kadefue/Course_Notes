#!/usr/bin/env python3
"""
build_slides.py
Generates comprehensive, professional 16:9 widescreen PowerPoint (.pptx) presentations
and converts them to PDF for all 9 lectures of:
AEN 214: INTRODUCTION TO ELECTRONICS
Department of Agricultural Engineering, Sokoine University of Agriculture (SUA).

Specifications:
- Strictly >= 25 slides per lecture (26 structured slides per lecture).
- Official SUA Brand Identity: SUA Green (#008836), Black/Charcoal, and White.
- Official SUA.png logo embedded on every slide header.
- Zero black spots: Standard unicode engineering symbols (Ω, μ, π, τ, ±, ², ³, °, α, β, γ, λ, √).
- Grounded in Tanzanian agricultural engineering scenarios.
- Integrated schematics and real hardware images from Figures/ directory.
- Automated headless conversion from PPTX to PDF via LibreOffice.
"""

import os
import sys
import subprocess
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

LECTURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Lectures"))
FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Figures"))
os.makedirs(LECTURES_DIR, exist_ok=True)

# SUA Brand Colors
SUA_GREEN = RGBColor(0, 136, 54)         # #008836 Official SUA Logo Green
SUA_DARKGREEN = RGBColor(0, 90, 36)      # #005a24 Dark Forest Green
SUA_LIGHT_BG = RGBColor(248, 250, 248)   # Crisp light background
COLOR_TEXT = RGBColor(17, 24, 39)        # Charcoal dark text
COLOR_MUTED = RGBColor(75, 85, 99)       # Medium slate gray
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_CARD_BG = RGBColor(240, 253, 244)  # Light green tint card
COLOR_BORDER = RGBColor(209, 213, 219)   # Light gray border

SUA_LOGO_PATH = os.path.join(FIGURES_DIR, "SUA.png")
if not os.path.exists(SUA_LOGO_PATH):
    SUA_LOGO_PATH = "/home/kadefue/Course_Notes/SUA.png"

def create_base_slide(prs):
    """Creates a blank 16:9 slide."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    return slide

def add_header(slide, title_text, category_text="AEN 214: INTRODUCTION TO ELECTRONICS"):
    """Adds standard SUA Green header banner, course subtitle, slide title, and SUA logo."""
    # Top banner background
    banner = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1)
    )
    banner.fill.solid()
    banner.fill.fore_color.rgb = SUA_GREEN
    banner.line.color.rgb = SUA_DARKGREEN
    banner.line.width = Pt(1.5)

    # Accent underline
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.1), Inches(13.333), Inches(0.04)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(0, 60, 20)
    line.line.fill.background()

    # Category Text
    tb_cat = slide.shapes.add_textbox(Inches(0.6), Inches(0.12), Inches(10.5), Inches(0.3))
    tf_cat = tb_cat.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = RGBColor(220, 252, 231) # Light green text

    # Title Text
    tb_title = slide.shapes.add_textbox(Inches(0.6), Inches(0.40), Inches(10.8), Inches(0.6))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(21)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE

    # SUA Logo
    if os.path.exists(SUA_LOGO_PATH):
        slide.shapes.add_picture(SUA_LOGO_PATH, Inches(12.0), Inches(0.12), height=Inches(0.85))

def add_footer(slide, current_slide, total_slides=26):
    """Adds standard footer bar with institutional metadata and slide number."""
    # Footer line
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(7.05), Inches(12.133), Inches(0.02)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_BORDER
    line.line.fill.background()

    # Left footer text
    tb_left = slide.shapes.add_textbox(Inches(0.6), Inches(7.08), Inches(9.0), Inches(0.35))
    tf_left = tb_left.text_frame
    p_l = tf_left.paragraphs[0]
    p_l.text = "Sokoine University of Agriculture | School of Engineering & Technology | Department of Agricultural Engineering"
    p_l.font.size = Pt(8.5)
    p_l.font.color.rgb = COLOR_MUTED

    # Right footer text (Slide number)
    tb_right = slide.shapes.add_textbox(Inches(10.5), Inches(7.08), Inches(2.2), Inches(0.35))
    tf_right = tb_right.text_frame
    p_r = tf_right.paragraphs[0]
    p_r.text = f"Slide {current_slide} of {total_slides}"
    p_r.alignment = PP_ALIGN.RIGHT
    p_r.font.size = Pt(9)
    p_r.font.bold = True
    p_r.font.color.rgb = SUA_GREEN

def add_title_slide(prs, lecture_num, title, subtitle, current_slide=1, total_slides=26):
    """Constructs the master title slide."""
    slide = create_base_slide(prs)

    # Background banner
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = SUA_LIGHT_BG
    bg.line.fill.background()

    # Header Card
    hdr_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(11.733), Inches(2.2))
    hdr_card.fill.solid()
    hdr_card.fill.fore_color.rgb = SUA_GREEN
    hdr_card.line.color.rgb = SUA_DARKGREEN
    hdr_card.line.width = Pt(2)

    # SUA Logo inside card
    if os.path.exists(SUA_LOGO_PATH):
        slide.shapes.add_picture(SUA_LOGO_PATH, Inches(1.1), Inches(0.85), height=Inches(1.7))

    tb_univ = slide.shapes.add_textbox(Inches(2.7), Inches(0.75), Inches(9.5), Inches(0.4))
    p_u = tb_univ.text_frame.paragraphs[0]
    p_u.text = "SOKOINE UNIVERSITY OF AGRICULTURE"
    p_u.font.size = Pt(17)
    p_u.font.bold = True
    p_u.font.color.rgb = COLOR_WHITE

    tb_dept = slide.shapes.add_textbox(Inches(2.7), Inches(1.15), Inches(9.5), Inches(0.35))
    p_d = tb_dept.text_frame.paragraphs[0]
    p_d.text = "School of Engineering and Technology | Department of Agricultural Engineering"
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = RGBColor(220, 252, 231)

    tb_code = slide.shapes.add_textbox(Inches(2.7), Inches(1.55), Inches(9.5), Inches(0.45))
    p_c = tb_code.text_frame.paragraphs[0]
    p_c.text = f"AEN 214: INTRODUCTION TO ELECTRONICS — LECTURE {lecture_num}"
    p_c.font.size = Pt(15)
    p_c.font.bold = True
    p_c.font.color.rgb = RGBColor(254, 240, 138) # Light yellow accent

    # Lecture Title & Subtitle Card
    title_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.0), Inches(11.733), Inches(2.5))
    title_card.fill.solid()
    title_card.fill.fore_color.rgb = COLOR_WHITE
    title_card.line.color.rgb = COLOR_BORDER
    title_card.line.width = Pt(1)

    tb_t = slide.shapes.add_textbox(Inches(1.2), Inches(3.2), Inches(11.0), Inches(1.0))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(28)
    p_t.font.bold = True
    p_t.font.color.rgb = SUA_DARKGREEN

    tb_sub = slide.shapes.add_textbox(Inches(1.2), Inches(4.3), Inches(11.0), Inches(0.8))
    tf_sub = tb_sub.text_frame
    tf_sub.word_wrap = True
    p_s = tf_sub.paragraphs[0]
    p_s.text = subtitle
    p_s.font.size = Pt(15)
    p_s.font.color.rgb = COLOR_MUTED

    # Instructor Card
    inst_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.7), Inches(11.733), Inches(1.0))
    inst_card.fill.solid()
    inst_card.fill.fore_color.rgb = COLOR_CARD_BG
    inst_card.line.color.rgb = SUA_GREEN
    inst_card.line.width = Pt(1)

    tb_inst = slide.shapes.add_textbox(Inches(1.2), Inches(5.75), Inches(11.0), Inches(0.8))
    tf_inst = tb_inst.text_frame
    p_i = tf_inst.paragraphs[0]
    p_i.text = "Course Instructor: Dr. Kadeghe Goodluck Fue, PhD, P.Eng (T)"
    p_i.font.size = Pt(12)
    p_i.font.bold = True
    p_i.font.color.rgb = COLOR_TEXT

    p_i2 = tf_inst.add_paragraph()
    p_i2.text = "Electronics & Precision Agriculture Laboratory | Academic Year 2025/2026 | Sokoine University of Agriculture"
    p_i2.font.size = Pt(10)
    p_i2.font.color.rgb = COLOR_MUTED

    add_footer(slide, current_slide, total_slides)
    return slide

def add_bullet_slide(prs, title, bullets, image_file=None, current_slide=2, total_slides=26):
    """Creates a structured content slide with bullet points and optional side figure."""
    slide = create_base_slide(prs)
    add_header(slide, title)

    has_img = False
    img_path = None
    if image_file:
        full_path = os.path.join(FIGURES_DIR, image_file)
        if os.path.exists(full_path):
            has_img = True
            img_path = full_path

    # Layout dimensions
    if has_img:
        text_width = Inches(7.2)
        img_left = Inches(8.1)
        img_top = Inches(1.4)
        img_width = Inches(4.6)
    else:
        text_width = Inches(12.133)

    # Card background for text
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.3), text_width, Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_WHITE
    card.line.color.rgb = COLOR_BORDER
    card.line.width = Pt(1)

    tb = slide.shapes.add_textbox(Inches(0.8), Inches(1.45), text_width - Inches(0.4), Inches(5.1))
    tf = tb.text_frame
    tf.word_wrap = True

    for i, bullet in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(10)
        p.font.size = Pt(14)
        p.font.color.rgb = COLOR_TEXT

        # Bold highlight prefix before colon if present
        if ":" in bullet:
            parts = bullet.split(":", 1)
            p.text = "• " + parts[0] + ":"
            p.font.bold = True
            p.font.color.rgb = SUA_DARKGREEN
            
            run = p.add_run()
            run.text = parts[1]
            run.font.bold = False
            run.font.color.rgb = COLOR_TEXT
        else:
            p.text = "• " + bullet

    if has_img:
        # Card border for image
        img_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, img_left - Inches(0.1), img_top - Inches(0.1), img_width + Inches(0.2), Inches(5.5))
        img_card.fill.solid()
        img_card.fill.fore_color.rgb = COLOR_WHITE
        img_card.line.color.rgb = COLOR_BORDER
        img_card.line.width = Pt(1)
        slide.shapes.add_picture(img_path, img_left, img_top + Inches(0.3), width=img_width)

    add_footer(slide, current_slide, total_slides)
    return slide

def add_example_slide(prs, ex_num, title, problem_stmt, solution_steps, current_slide, total_slides=26):
    """Creates a step-by-step worked engineering example slide."""
    slide = create_base_slide(prs)
    add_header(slide, f"Worked Engineering Example {ex_num}: {title}")

    # Problem Box (Top)
    prob_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.3), Inches(12.133), Inches(1.6))
    prob_box.fill.solid()
    prob_box.fill.fore_color.rgb = COLOR_CARD_BG
    prob_box.line.color.rgb = SUA_GREEN
    prob_box.line.width = Pt(1.5)

    tb_p = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(1.4))
    tf_p = tb_p.text_frame
    tf_p.word_wrap = True
    p_lbl = tf_p.paragraphs[0]
    p_lbl.text = f"PROBLEM SPECIFICATION & AGRICULTURAL CONTEXT:"
    p_lbl.font.size = Pt(11)
    p_lbl.font.bold = True
    p_lbl.font.color.rgb = SUA_DARKGREEN
    
    p_txt = tf_p.add_paragraph()
    p_txt.text = problem_stmt
    p_txt.font.size = Pt(12)
    p_txt.font.color.rgb = COLOR_TEXT

    # Solution Box (Bottom)
    sol_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(3.05), Inches(12.133), Inches(3.8))
    sol_box.fill.solid()
    sol_box.fill.fore_color.rgb = COLOR_WHITE
    sol_box.line.color.rgb = COLOR_BORDER
    sol_box.line.width = Pt(1)

    tb_s = slide.shapes.add_textbox(Inches(0.8), Inches(3.15), Inches(11.7), Inches(3.5))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    p_slbl = tf_s.paragraphs[0]
    p_slbl.text = "STEP-BY-STEP MATHEMATICAL SOLUTION & VERIFICATION:"
    p_slbl.font.size = Pt(11)
    p_slbl.font.bold = True
    p_slbl.font.color.rgb = SUA_GREEN

    for step in solution_steps:
        p_step = tf_s.add_paragraph()
        p_step.space_after = Pt(4)
        p_step.font.size = Pt(11.5)
        p_step.font.color.rgb = COLOR_TEXT
        p_step.text = step

    add_footer(slide, current_slide, total_slides)
    return slide

def add_case_study_slide(prs, case_num, title, location, problem_desc, solution_desc, impact_metrics, current_slide, total_slides=26):
    """Creates a Tanzanian agricultural engineering field case study slide."""
    slide = create_base_slide(prs)
    add_header(slide, f"Tanzanian Field Case Study {case_num}: {title}")

    # Left Column: Problem & Context
    box_l = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.3), Inches(5.9), Inches(5.5))
    box_l.fill.solid()
    box_l.fill.fore_color.rgb = COLOR_WHITE
    box_l.line.color.rgb = COLOR_BORDER
    box_l.line.width = Pt(1)

    tb_l = slide.shapes.add_textbox(Inches(0.8), Inches(1.45), Inches(5.5), Inches(5.1))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p_lt = tf_l.paragraphs[0]
    p_lt.text = f"FIELD LOCATION & PROBLEM IDENTIFICATION"
    p_lt.font.size = Pt(13)
    p_lt.font.bold = True
    p_lt.font.color.rgb = RGBColor(185, 28, 28) # Red accent

    p_loc = tf_l.add_paragraph()
    p_loc.text = f"• Geographic Location: {location}"
    p_loc.font.size = Pt(12)
    p_loc.font.bold = True
    p_loc.font.color.rgb = COLOR_TEXT
    p_loc.space_after = Pt(8)

    p_pdesc = tf_l.add_paragraph()
    p_pdesc.text = problem_desc
    p_pdesc.font.size = Pt(12)
    p_pdesc.font.color.rgb = COLOR_TEXT

    # Right Column: Engineering Solution & Impact
    box_r = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.3), Inches(5.9), Inches(5.5))
    box_r.fill.solid()
    box_r.fill.fore_color.rgb = COLOR_CARD_BG
    box_r.line.color.rgb = SUA_GREEN
    box_r.line.width = Pt(1.5)

    tb_r = slide.shapes.add_textbox(Inches(7.0), Inches(1.45), Inches(5.5), Inches(5.1))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p_rt = tf_r.paragraphs[0]
    p_rt.text = "SUA ENGINEERING SOLUTION & AGRONOMIC IMPACT"
    p_rt.font.size = Pt(13)
    p_rt.font.bold = True
    p_rt.font.color.rgb = SUA_DARKGREEN

    p_sdesc = tf_r.add_paragraph()
    p_sdesc.text = solution_desc
    p_sdesc.font.size = Pt(12)
    p_sdesc.font.color.rgb = COLOR_TEXT
    p_sdesc.space_after = Pt(10)

    p_it = tf_r.add_paragraph()
    p_it.text = "Measurable Performance Metrics:"
    p_it.font.size = Pt(12)
    p_it.font.bold = True
    p_it.font.color.rgb = SUA_GREEN

    for metric in impact_metrics:
        p_m = tf_r.add_paragraph()
        p_m.text = "✔ " + metric
        p_m.font.size = Pt(11.5)
        p_m.font.color.rgb = COLOR_TEXT
        p_m.space_after = Pt(4)

    add_footer(slide, current_slide, total_slides)
    return slide

def add_lab_slide(prs, title, objectives, procedures, current_slide, total_slides=26):
    """Creates a laboratory bench protocol slide."""
    slide = create_base_slide(prs)
    add_header(slide, f"Laboratory Bench Protocol: {title}")

    # Top Card: Lab Objectives
    box_top = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.3), Inches(12.133), Inches(1.5))
    box_top.fill.solid()
    box_top.fill.fore_color.rgb = COLOR_CARD_BG
    box_top.line.color.rgb = SUA_GREEN
    box_top.line.width = Pt(1)

    tb_top = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(1.3))
    tf_top = tb_top.text_frame
    tf_top.word_wrap = True
    p_ot = tf_top.paragraphs[0]
    p_ot.text = "PRACTICAL LAB LEARNING OUTCOMES & BENCH REQUIREMENTS:"
    p_ot.font.size = Pt(11)
    p_ot.font.bold = True
    p_ot.font.color.rgb = SUA_DARKGREEN

    for obj in objectives:
        p_o = tf_top.add_paragraph()
        p_o.text = "• " + obj
        p_o.font.size = Pt(11)
        p_o.font.color.rgb = COLOR_TEXT

    # Bottom Card: Experimental Bench Procedures
    box_bot = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(2.95), Inches(12.133), Inches(3.9))
    box_bot.fill.solid()
    box_bot.fill.fore_color.rgb = COLOR_WHITE
    box_bot.line.color.rgb = COLOR_BORDER
    box_bot.line.width = Pt(1)

    tb_bot = slide.shapes.add_textbox(Inches(0.8), Inches(3.05), Inches(11.7), Inches(3.6))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    p_pt = tf_bot.paragraphs[0]
    p_pt.text = "STEP-BY-STEP PROTOTYPING & DIAGNOSTIC PROCEDURE:"
    p_pt.font.size = Pt(11)
    p_pt.font.bold = True
    p_pt.font.color.rgb = SUA_GREEN

    for proc in procedures:
        p_pr = tf_bot.add_paragraph()
        p_pr.space_after = Pt(4)
        p_pr.font.size = Pt(11.5)
        p_pr.font.color.rgb = COLOR_TEXT
        p_pr.text = proc

    add_footer(slide, current_slide, total_slides)
    return slide

def add_summary_slide(prs, lecture_num, takeaways, formula_cheatsheet, current_slide=25, total_slides=26):
    """Creates a summary and formula cheat-sheet slide."""
    slide = create_base_slide(prs)
    add_header(slide, f"Lecture {lecture_num} Synthesis: Key Takeaways & Formula Sheet")

    # Left Column: Key Takeaways
    box_l = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.3), Inches(5.9), Inches(5.5))
    box_l.fill.solid()
    box_l.fill.fore_color.rgb = COLOR_WHITE
    box_l.line.color.rgb = COLOR_BORDER
    box_l.line.width = Pt(1)

    tb_l = slide.shapes.add_textbox(Inches(0.8), Inches(1.45), Inches(5.5), Inches(5.1))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p_lt = tf_l.paragraphs[0]
    p_lt.text = "CORE CONCEPTUAL TAKEAWAYS"
    p_lt.font.size = Pt(13)
    p_lt.font.bold = True
    p_lt.font.color.rgb = SUA_DARKGREEN

    for t in takeaways:
        p = tf_l.add_paragraph()
        p.space_after = Pt(6)
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT
        p.text = "✔ " + t

    # Right Column: Formula Sheet
    box_r = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.3), Inches(5.9), Inches(5.5))
    box_r.fill.solid()
    box_r.fill.fore_color.rgb = COLOR_CARD_BG
    box_r.line.color.rgb = SUA_GREEN
    box_r.line.width = Pt(1.5)

    tb_r = slide.shapes.add_textbox(Inches(7.0), Inches(1.45), Inches(5.5), Inches(5.1))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p_rt = tf_r.paragraphs[0]
    p_rt.text = "CRITICAL ENGINEERING FORMULAS"
    p_rt.font.size = Pt(13)
    p_rt.font.bold = True
    p_rt.font.color.rgb = SUA_GREEN

    for formula in formula_cheatsheet:
        p = tf_r.add_paragraph()
        p.space_after = Pt(6)
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT
        p.text = "★ " + formula

    add_footer(slide, current_slide, total_slides)
    return slide

def add_review_slide(prs, lecture_num, questions, preview_text, current_slide=26, total_slides=26):
    """Creates the concluding review questions and next lecture preview slide."""
    slide = create_base_slide(prs)
    add_header(slide, f"Lecture {lecture_num} Self-Assessment & Upcoming Topics")

    # Top Box: Review Questions
    box_q = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.3), Inches(12.133), Inches(4.0))
    box_q.fill.solid()
    box_q.fill.fore_color.rgb = COLOR_WHITE
    box_q.line.color.rgb = COLOR_BORDER
    box_q.line.width = Pt(1)

    tb_q = slide.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.7), Inches(3.7))
    tf_q = tb_q.text_frame
    tf_q.word_wrap = True
    p_qt = tf_q.paragraphs[0]
    p_qt.text = "SELF-ASSESSMENT & PROBLEM-SOLVING EXERCISES:"
    p_qt.font.size = Pt(12)
    p_qt.font.bold = True
    p_qt.font.color.rgb = SUA_DARKGREEN

    for q in questions:
        p = tf_q.add_paragraph()
        p.space_after = Pt(5)
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT
        p.text = "Q: " + q

    # Bottom Box: Next Lecture Preview
    box_prev = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.45), Inches(12.133), Inches(1.4))
    box_prev.fill.solid()
    box_prev.fill.fore_color.rgb = COLOR_CARD_BG
    box_prev.line.color.rgb = SUA_GREEN
    box_prev.line.width = Pt(1.5)

    tb_prev = slide.shapes.add_textbox(Inches(0.8), Inches(5.5), Inches(11.7), Inches(1.2))
    tf_prev = tb_prev.text_frame
    tf_prev.word_wrap = True
    p_pt = tf_prev.paragraphs[0]
    p_pt.text = "NEXT LECTURE PREVIEW & REQUIRED PREPARATION:"
    p_pt.font.size = Pt(11)
    p_pt.font.bold = True
    p_pt.font.color.rgb = SUA_GREEN

    p_pbody = tf_prev.add_paragraph()
    p_pbody.text = preview_text
    p_pbody.font.size = Pt(11.5)
    p_pbody.font.color.rgb = COLOR_TEXT

    add_footer(slide, current_slide, total_slides)
    return slide

def generate_all_slides():
    """Generates all 9 lecture presentations (26 slides each) and converts them to PDF."""
    from slides_part1 import build_lecture_1_deck, build_lecture_2_deck, build_lecture_3_deck
    from slides_part2 import build_lecture_4_deck, build_lecture_5_deck, build_lecture_6_deck
    from slides_part3 import build_lecture_7_deck, build_lecture_8_deck, build_lecture_9_deck

    deck_builders = [
        (1, build_lecture_1_deck),
        (2, build_lecture_2_deck),
        (3, build_lecture_3_deck),
        (4, build_lecture_4_deck),
        (5, build_lecture_5_deck),
        (6, build_lecture_6_deck),
        (7, build_lecture_7_deck),
        (8, build_lecture_8_deck),
        (9, build_lecture_9_deck)
    ]

    print("=" * 70)
    print("AEN 214: INTRODUCTION TO ELECTRONICS — LECTURE SLIDE GENERATOR")
    print("Department of Agricultural Engineering, Sokoine University of Agriculture")
    print("=" * 70)

    pptx_files = []

    for num, builder in deck_builders:
        prs = Presentation()
        prs.slide_width = Inches(13.333)
        prs.slide_height = Inches(7.5)

        print(f"\n[Building] Lecture {num} PowerPoint deck (26 slides)...")
        builder(prs)

        out_pptx = os.path.join(LECTURES_DIR, f"AEN_214_Lecture_{num}.pptx")
        prs.save(out_pptx)
        pptx_files.append(out_pptx)
        print(f"[Success] Saved {out_pptx} ({os.path.getsize(out_pptx)} bytes, {len(prs.slides)} slides)")

    print("\n" + "=" * 70)
    print("CONVERTING ALL 9 PPTX PRESENTATIONS TO PDF VIA LIBREOFFICE")
    print("=" * 70)

    for pptx_path in pptx_files:
        base_name = os.path.basename(pptx_path)
        pdf_name = base_name.replace(".pptx", ".pdf")
        pdf_path = os.path.join(LECTURES_DIR, pdf_name)

        print(f"[Converting] {base_name} -> {pdf_name}...")
        cmd = ["libreoffice", "--headless", "--convert-to", "pdf", pptx_path, "--outdir", LECTURES_DIR]
        res = subprocess.run(cmd, capture_output=True, text=True)

        if os.path.exists(pdf_path):
            print(f"[Success] Converted {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
        else:
            print(f"[Error] Failed to convert {pptx_path}:\n{res.stderr}")

    print("\n[Completed] All 9 lecture PowerPoint decks and PDF slides generated successfully!")

if __name__ == "__main__":
    generate_all_slides()

