#!/usr/bin/env python3
"""Build readable, paginated AEN 214 lecture presentations and PDFs."""

import argparse
import os
from pathlib import Path
import re
import subprocess
import tempfile

from PIL import Image, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = ROOT / "Figures"
LECTURES_DIR = ROOT / "Lectures"
GREEN = RGBColor(0, 136, 54)
DARK_GREEN = RGBColor(0, 90, 36)
TEXT = RGBColor(17, 24, 39)
MUTED = RGBColor(75, 85, 99)
WHITE = RGBColor(255, 255, 255)
LIGHT_GREEN = RGBColor(240, 253, 244)
BORDER = RGBColor(209, 213, 219)
FONT_NAME = "DejaVu Sans"
BODY_SIZE = 28
BODY_LINE = 36
HEADING_SIZE = 24
HEADING_LINE = 32
BODY_TOP = 1.43
BODY_BOTTOM = 6.85
FONT_REGULAR = ImageFont.truetype("DejaVuSans.ttf", BODY_SIZE * 4)
FONT_BOLD = ImageFont.truetype("DejaVuSans-Bold.ttf", BODY_SIZE * 4)
SCRIPT_PATTERN = re.compile(
    r"(?P<marker>[_^])(?:\{(?P<braced>[^{}]+)\}|\((?P<parenthesized>[^()]+)\)"
    r"|(?P<simple>[+-]?[A-Za-z0-9]+(?:[+-][0-9]+)?))"
)


def notation_runs(text):
    """Convert source equation markers to (text, baseline) presentation runs."""
    runs = []
    position = 0
    for match in SCRIPT_PATTERN.finditer(text):
        ordinary = text[position:match.start()]
        if "_" in ordinary or "^" in ordinary:
            raise ValueError(f"Invalid equation notation: {text!r}")
        if ordinary:
            runs.append((ordinary, 0))
        value = match.group("braced") or match.group("parenthesized") or match.group("simple")
        baseline = -25000 if match.group("marker") == "_" else 30000
        if runs and not ordinary and baseline == -25000 and runs[-1][1] == baseline:
            previous, _ = runs.pop()
            value = previous + "," + value
        runs.append((value, baseline))
        position = match.end()
    ordinary = text[position:]
    if "_" in ordinary or "^" in ordinary:
        raise ValueError(f"Invalid equation notation: {text!r}")
    if ordinary:
        runs.append((ordinary, 0))
    return runs


def wrapped_lines(text, width_inches, size, bold=False):
    """Wrap using conservative font metrics; the resulting breaks are explicit."""
    font = FONT_BOLD if bold else FONT_REGULAR
    max_width = width_inches * 72 * 4 * 0.94
    lines = []
    for source_line in text.split("\n"):
        words = source_line.split()
        if not words:
            lines.append("")
            continue
        line = words[0]
        for word in words[1:]:
            candidate = line + " " + word
            if font.getlength(candidate) * size / BODY_SIZE <= max_width:
                line = candidate
            else:
                lines.append(line)
                line = word
        if font.getlength(line) * size / BODY_SIZE > max_width:
            raise ValueError(f"Word is too wide for a slide: {line!r}")
        lines.append(line)
    return lines


def text_box(slide, left, top, width, height, text, size, color=TEXT,
             bold=False, align=PP_ALIGN.LEFT, line_height=None):
    shape = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    frame = shape.text_frame
    frame.word_wrap = False
    frame.auto_size = MSO_AUTO_SIZE.NONE
    frame.margin_left = frame.margin_right = 0
    frame.margin_top = frame.margin_bottom = 0
    frame.vertical_anchor = MSO_ANCHOR.TOP
    paragraph = frame.paragraphs[0]
    paragraph.font.name = FONT_NAME
    paragraph.font.size = Pt(size)
    paragraph.font.bold = bold
    paragraph.font.color.rgb = color
    paragraph.alignment = align
    if line_height is not None:
        paragraph.line_spacing = Pt(line_height)
    for line_index, line in enumerate(text.split("\n")):
        if line_index:
            paragraph.add_line_break()
        for value, baseline in notation_runs(line):
            run = paragraph.add_run()
            run.text = value
            if baseline:
                # python-pptx does not expose DrawingML's baseline attribute.
                run._r.get_or_add_rPr().set("baseline", str(baseline))
    return shape


def rectangle(slide, left, top, width, height, fill, border=None):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if border is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = border
    return shape


def add_picture_fit(slide, path, left, top, width, height):
    with Image.open(path) as image:
        image_width, image_height = image.size
    scale = min(width / image_width, height / image_height)
    actual_width, actual_height = image_width * scale, image_height * scale
    slide.shapes.add_picture(
        str(path), Inches(left + (width - actual_width) / 2),
        Inches(top + (height - actual_height) / 2),
        width=Inches(actual_width), height=Inches(actual_height),
    )


def create_base_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def add_header(slide, title, continuation=False):
    rectangle(slide, 0, 0, 13.333, 1.18, GREEN)
    text_box(slide, 0.5, 0.08, 10.8, 0.22,
             "AEN 214: INTRODUCTION TO ELECTRONICS", 11, WHITE, True)
    if continuation:
        title += " (continued)"
    size = 23
    lines = wrapped_lines(title, 10.9, size, bold=True)
    while len(lines) > 2 and size > 16:
        size -= 1
        lines = wrapped_lines(title, 10.9, size, bold=True)
    if len(lines) > 2:
        raise ValueError(f"Slide title does not fit: {title}")
    text_box(slide, 0.5, 0.34, 10.9, 0.78, "\n".join(lines),
             size, WHITE, True, line_height=size + 2)
    add_picture_fit(slide, FIGURES_DIR / "SUA.png", 11.9, 0.10, 0.95, 0.94)


def add_footer(slide, current_slide, total_slides):
    rectangle(slide, 0.5, 7.03, 12.33, 0.015, BORDER)
    text_box(slide, 0.5, 7.11, 9.8, 0.22,
             "Sokoine University of Agriculture | Department of Agricultural Engineering",
             10, MUTED)
    text_box(slide, 10.5, 7.11, 2.3, 0.22,
             f"Slide {current_slide} of {total_slides}", 10, GREEN, True,
             align=PP_ALIGN.RIGHT)


def add_title_slide(prs, lecture_num, title, subtitle, current_slide=1, total_slides=26):
    slide = create_base_slide(prs)
    rectangle(slide, 0, 0, 13.333, 7.5, RGBColor(248, 250, 248))
    rectangle(slide, 0.5, 0.4, 12.33, 2.05, GREEN)
    add_picture_fit(slide, FIGURES_DIR / "SUA.png", 0.8, 0.7, 1.3, 1.4)
    text_box(slide, 2.4, 0.65, 9.9, 0.4,
             "SOKOINE UNIVERSITY OF AGRICULTURE", 24, WHITE, True)
    text_box(slide, 2.4, 1.16, 9.9, 0.75,
             "School of Engineering and Technology\nDepartment of Agricultural Engineering",
             18, WHITE, line_height=23)
    text_box(slide, 2.4, 2.0, 9.9, 0.35,
             f"AEN 214: INTRODUCTION TO ELECTRONICS — LECTURE {lecture_num}",
             19, WHITE, True)
    rectangle(slide, 0.5, 2.7, 12.33, 2.55, WHITE, BORDER)
    title_lines = wrapped_lines(title, 11.3, 32, bold=True)
    subtitle_lines = wrapped_lines(subtitle, 11.3, 23)
    if len(title_lines) > 2 or len(subtitle_lines) > 3:
        raise ValueError(f"Title slide content does not fit: {title}")
    text_box(slide, 0.9, 2.95, 11.3, 1.15, "\n".join(title_lines),
             32, DARK_GREEN, True, line_height=38)
    text_box(slide, 0.9, 4.12, 11.3, 1.0, "\n".join(subtitle_lines),
             23, MUTED, line_height=28)
    rectangle(slide, 0.5, 5.5, 12.33, 1.35, LIGHT_GREEN, GREEN)
    text_box(slide, 0.9, 5.7, 11.3, 0.35,
             "Course Instructor: Dr. Kadeghe Goodluck Fue, PhD, P.Eng (T)",
             19, TEXT, True)
    text_box(slide, 0.9, 6.15, 11.3, 0.52,
             "Electronics & Precision Agriculture Laboratory | Academic Year 2025/2026\n"
             "Sokoine University of Agriculture",
             16, MUTED, line_height=20)
    return slide


def add_content_slides(prs, title, blocks, image_file=None):
    """Lay out (text, is_heading) blocks, spilling onto as many slides as needed."""
    image_path = FIGURES_DIR / image_file if image_file else None
    if image_path is not None and not image_path.is_file():
        raise FileNotFoundError(f"Slide image not found: {image_path}")
    remaining = list(blocks)
    first_slide = None
    continuation = False
    while remaining:
        slide = create_base_slide(prs)
        if first_slide is None:
            first_slide = slide
        add_header(slide, title, continuation)
        with_image = image_path is not None and not continuation
        width = 7.0 if with_image else 11.9
        rectangle(slide, 0.5, 1.28, 7.4 if with_image else 12.33, 5.64, WHITE, BORDER)
        if with_image:
            rectangle(slide, 8.05, 1.28, 4.78, 5.64, WHITE, BORDER)
            add_picture_fit(slide, image_path, 8.2, 1.43, 4.48, 5.34)
        y = BODY_TOP
        last_was_heading = False
        while remaining:
            content, heading = remaining[0]
            size = HEADING_SIZE if heading else BODY_SIZE
            line_height = HEADING_LINE if heading else BODY_LINE
            lines = wrapped_lines(content, width, size, bold=heading)
            available = int(((BODY_BOTTOM - y) * 72 + 0.01) // line_height)
            if (heading and len(remaining) > 1
                    and y + (len(lines) * line_height + BODY_LINE) / 72 + 0.10 > BODY_BOTTOM):
                break
            if available < 1:
                break
            if len(lines) > available and y > BODY_TOP and not last_was_heading:
                break
            count = min(len(lines), available)
            chunk = lines[:count]
            height = count * line_height / 72
            text_box(slide, 0.7, y, width, height, "\n".join(chunk), size,
                     DARK_GREEN if heading else TEXT, heading, line_height=line_height)
            y += height + 0.10
            if count == len(lines):
                remaining.pop(0)
                last_was_heading = heading
            else:
                remaining[0] = (" ".join(lines[count:]), heading)
                break
        if y == BODY_TOP:
            raise ValueError(f"Cannot fit content on slide: {title}")
        continuation = True
    return first_slide


def add_bullet_slide(prs, title, bullets, image_file=None, current_slide=2, total_slides=26):
    return add_content_slides(prs, title, [("• " + bullet, False) for bullet in bullets], image_file)


def add_example_slide(prs, ex_num, title, problem_stmt, solution_steps, current_slide, total_slides=26):
    blocks = [("PROBLEM SPECIFICATION & AGRICULTURAL CONTEXT", True),
              (problem_stmt, False), ("STEP-BY-STEP SOLUTION & VERIFICATION", True)]
    blocks.extend((step, False) for step in solution_steps)
    return add_content_slides(prs, f"Worked Engineering Example {ex_num}: {title}", blocks)


def add_case_study_slide(prs, case_num, title, location, problem_desc, solution_desc,
                         impact_metrics, current_slide, total_slides=26):
    blocks = [("FIELD LOCATION & PROBLEM", True), ("Geographic Location: " + location, False),
              (problem_desc, False), ("ENGINEERING SOLUTION & AGRONOMIC IMPACT", True),
              (solution_desc, False), ("MEASURABLE PERFORMANCE METRICS", True)]
    blocks.extend(("• " + metric, False) for metric in impact_metrics)
    return add_content_slides(prs, f"Tanzanian Field Case Study {case_num}: {title}", blocks)


def add_lab_slide(prs, title, objectives, procedures, current_slide, total_slides=26):
    blocks = [("PRACTICAL LAB LEARNING OUTCOMES & BENCH REQUIREMENTS", True)]
    blocks.extend(("• " + obj, False) for obj in objectives)
    blocks.append(("STEP-BY-STEP PROTOTYPING & DIAGNOSTIC PROCEDURE", True))
    blocks.extend((proc, False) for proc in procedures)
    return add_content_slides(prs, f"Laboratory Bench Protocol: {title}", blocks)


def add_summary_slide(prs, lecture_num, takeaways, formula_cheatsheet, current_slide=25, total_slides=26):
    blocks = [("CORE CONCEPTUAL TAKEAWAYS", True)]
    blocks.extend(("• " + item, False) for item in takeaways)
    blocks.append(("CRITICAL ENGINEERING FORMULAS", True))
    blocks.extend(("• " + formula, False) for formula in formula_cheatsheet)
    return add_content_slides(prs, f"Lecture {lecture_num} Synthesis: Key Takeaways & Formula Sheet", blocks)


def add_review_slide(prs, lecture_num, questions, preview_text, current_slide=26, total_slides=26):
    blocks = [("SELF-ASSESSMENT & PROBLEM-SOLVING EXERCISES", True)]
    blocks.extend(("Q: " + question, False) for question in questions)
    blocks.extend([("NEXT LECTURE PREVIEW & REQUIRED PREPARATION", True), (preview_text, False)])
    return add_content_slides(prs, f"Lecture {lecture_num} Self-Assessment & Upcoming Topics", blocks)


def generate_all_slides(output_dir=LECTURES_DIR):
    from slides_part1 import build_lecture_1_deck, build_lecture_2_deck, build_lecture_3_deck
    from slides_part2 import build_lecture_4_deck, build_lecture_5_deck, build_lecture_6_deck
    from slides_part3 import build_lecture_7_deck, build_lecture_8_deck, build_lecture_9_deck

    builders = [build_lecture_1_deck, build_lecture_2_deck, build_lecture_3_deck,
                build_lecture_4_deck, build_lecture_5_deck, build_lecture_6_deck,
                build_lecture_7_deck, build_lecture_8_deck, build_lecture_9_deck]
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="aen214-lo-") as profile_dir:
        profile_arg = f"-env:UserInstallation={Path(profile_dir).as_uri()}"
        for number, builder in enumerate(builders, 1):
            prs = Presentation()
            prs.slide_width = Inches(13.333)
            prs.slide_height = Inches(7.5)
            builder(prs)
            for index, slide in enumerate(prs.slides, 1):
                add_footer(slide, index, len(prs.slides))
            pptx_path = output_dir / f"AEN_214_Lecture_{number}.pptx"
            pdf_path = pptx_path.with_suffix(".pdf")
            prs.save(str(pptx_path))
            with tempfile.TemporaryDirectory(prefix="aen214-pdf-") as pdf_dir:
                result = subprocess.run(
                    ["libreoffice", profile_arg, "--headless", "--convert-to", "pdf",
                     "--outdir", pdf_dir, str(pptx_path)],
                    capture_output=True, text=True, check=True,
                )
                converted = Path(pdf_dir) / pdf_path.name
                if not converted.is_file() or converted.stat().st_size == 0:
                    raise RuntimeError(f"PDF conversion failed for {pptx_path}: {result.stdout} {result.stderr}")
                os.replace(converted, pdf_path)
            print(f"Lecture {number}: {len(prs.slides)} slides -> {pptx_path.name}, {pdf_path.name}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=LECTURES_DIR,
                        help="Directory for generated PPTX and PDF files (default: Lectures)")
    args = parser.parse_args()
    generate_all_slides(args.output_dir)
