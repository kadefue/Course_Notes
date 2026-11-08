#!/usr/bin/env python3
"""Build six image-rich BIT 111 compendia from the existing course scripts."""

import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from compendium_base import (
    COLOR_BORDER,
    COLOR_BG_LIGHT,
    COLOR_SUA_GREEN,
    COLOR_WHITE,
    Image,
    PageBreak,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    SimpleDocTemplate,
    NumberedCanvas,
    create_custom_table,
    get_custom_stylesheet,
    inch,
    letter,
)

ROOT = SCRIPTS_DIR.parent
NOTES_DIR = ROOT / "Notes"
FIGURES_DIR = ROOT / "Figures"
ONLINE_FIGURES_DIR = FIGURES_DIR / "Internet"
ATTRIBUTIONS_FILE = ONLINE_FIGURES_DIR / "attributions.json"

TITLES = {
    1: ("Introduction to Computers", "History, generations, classifications, and uses of microcomputers"),
    2: ("Main Components of a Microcomputer", "The processor, memory, storage, input/output devices, and peripherals"),
    3: ("Personal Computer Security", "Protecting accounts, devices, and information"),
    4: ("Functions and Types of Operating Systems", "Operating-system roles, interfaces, file management, and common commands"),
    5: ("Microcomputer Applications", "Word processing, spreadsheets, web use, and email"),
    6: ("Data Security and Malware Defense", "Privacy, safe computing, malware awareness, and information care"),
}


def load_attributions():
    if not ATTRIBUTIONS_FILE.is_file():
        raise FileNotFoundError(
            "Internet figure attributions are missing. Run "
            "Scripts/prepare_internet_figures.py first."
        )
    with ATTRIBUTIONS_FILE.open(encoding="utf-8") as file:
        manifest = json.load(file)
    for topic in range(1, 7):
        figures = manifest.get(str(topic), [])
        if len(figures) < 8:
            raise RuntimeError(f"Topic {topic} has fewer than eight attributed images.")
        for figure in figures[:8]:
            image_path = ONLINE_FIGURES_DIR / figure["filename"]
            if not image_path.is_file():
                raise FileNotFoundError(f"Missing internet figure: {image_path}")
    return manifest


def add_online_figure_pages(story, topic, figures, styles):
    for index, figure in enumerate(figures[:8], start=1):
        story.append(PageBreak())
        story.append(
            Paragraph(
                f"ONLINE FIGURE {index}: {html.escape(figure['title'])}",
                styles["SecH1"],
            )
        )
        image = Image(str(ONLINE_FIGURES_DIR / figure["filename"]))
        max_width, max_height = 6.7 * inch, 4.5 * inch
        scale = min(max_width / image.imageWidth, max_height / image.imageHeight)
        image.drawWidth = image.imageWidth * scale
        image.drawHeight = image.imageHeight * scale
        story.append(image)
        story.append(Spacer(1, 5))
        description = figure.get("description") or figure["title"]
        story.append(
            Paragraph(
                f"<b>What to notice:</b> {html.escape(description)}",
                styles["DocBody"],
            )
        )
        story.append(
            Paragraph(
                f"<b>Topic {topic} connection:</b> "
                f"{html.escape(TITLES[topic][0])}. Discuss what the figure helps "
                "you recognize and what information it does not provide by itself.",
                styles["DocBody"],
            )
        )
        creator = html.escape(figure.get("creator", "Creator not credited"))
        license_name = html.escape(figure["license"])
        url = html.escape(figure["source_url"], quote=True)
        story.append(
            Paragraph(
                f"<b>Attribution:</b> {creator}. "
                f"<a href='{url}' color='#005a24'>Wikimedia Commons source page</a>. "
                f"License: {license_name}.",
                styles["FigCaption"],
            )
        )
        story.append(Spacer(1, 8))


def make_figure_page_title(slide):
    title = slide.get("title", "Topic material")
    subtitle = slide.get("sub_title")
    return title, subtitle


def add_slide_notes(story, topic, slides_data, styles):
    for slide in slides_data:
        story.append(PageBreak())
        title, subtitle = make_figure_page_title(slide)
        story.append(Paragraph(html.escape(title), styles["SecH1"]))
        if subtitle:
            story.append(Paragraph(html.escape(subtitle), styles["SecH2"]))

        slide_type = slide.get("type", "bullet")
        if slide_type == "figure":
            figure_path = FIGURES_DIR / slide["img"]
            if figure_path.is_file():
                image = Image(str(figure_path))
                max_width, max_height = 6.5 * inch, 2.8 * inch
                scale = min(max_width / image.imageWidth, max_height / image.imageHeight)
                image.drawWidth = image.imageWidth * scale
                image.drawHeight = image.imageHeight * scale
                story.append(image)
                story.append(Spacer(1, 3))
                story.append(
                    Paragraph(html.escape(slide.get("caption", "")), styles["FigCaption"])
                )
        elif slide_type == "table":
            column_widths = slide.get("col_widths", [])
            if column_widths:
                total_width = sum(column_widths)
                column_widths = [
                    width * 7.2 / total_width * inch
                    for width in column_widths
                ]
            story.append(
                create_custom_table(
                    slide["headers"],
                    slide["rows"],
                    column_widths or None,
                )
            )

        bullets = slide.get("bullets", [])
        for bullet in bullets:
            text = html.unescape(str(bullet).strip())
            text = re.sub(r"<[^>]*>", "", text)
            text = html.escape(text)
            story.append(Paragraph(f"• {text}", styles["DocBody"]))
        callout = slide.get("callout")
        if callout:
            story.append(Spacer(1, 4))
            story.append(
                Paragraph(
                    f"<b>{html.escape(callout.get('title', 'Key idea'))}</b>",
                    styles["SecH3"],
                )
            )
            story.append(
                Paragraph(html.escape(callout.get("body", "")), styles["DocBody"])
            )
        story.append(Spacer(1, 6))
        story.append(
            Paragraph(
                "<b>Study prompt:</b> Explain this idea in your own words and connect it "
                "to an example from your discipline.",
                styles["DocBody"],
            )
        )


def make_reference_page(story, topic, styles):
    story.append(PageBreak())
    story.append(Paragraph("READING AND IMAGE CREDITS", styles["SecH1"]))
    readings = [
        "Smith, J. L., Wang, S., &amp; Mortati, J. (2019). "
        "<i>Information Systems for Business and Beyond</i>. "
        "Open textbook. https://opentextbook.site/informationsystems2019/",
        "Vermaat, M. E., Sebok, S. L., Freund, S. M., Campbell, J. T., &amp; "
        "Frydenberg, M. (2018). <i>Discovering Computers: Digital Technology, Data, "
        "and Devices</i> (16th ed.). Cengage. "
        "https://faculty.cengage.com/works/9781337285100",
    ]
    if topic == 5:
        readings.append(
            "Microsoft. (n.d.). <i>Overview of formulas in Excel</i>. Microsoft Support. "
            "https://support.microsoft.com/en-us/excel/get-started/"
            "overview-of-formulas-in-excel"
        )
    if topic in (3, 6):
        readings.append(
            "Pascoe, C., Quinn, S., &amp; Scarfone, K. (2024). "
            "<i>The NIST Cybersecurity Framework (CSF) 2.0</i> (NIST CSWP 29). "
            "National Institute of Standards and Technology. "
            "https://doi.org/10.6028/NIST.CSWP.29"
        )
    for reading in readings:
        story.append(Paragraph(reading, styles["DocBullet"]))
    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "Online image credits appear beside each image. Images were selected from "
            "Wikimedia Commons and included only where a public-domain or stated reuse "
            "license could be checked on the file page.",
            styles["DocBody"],
        )
    )


def add_cover(story, topic, styles):
    title, summary = TITLES[topic]
    header = [
        [Paragraph("SOKOINE UNIVERSITY OF AGRICULTURE", styles["CoverUniv"])],
        [Paragraph("Department of Informatics and Information Technology (DIIT)", styles["CoverDept"])],
        [Paragraph("BIT 111: MICROCOMPUTERS AND APPLICATIONS", styles["CourseCode"])],
        [Paragraph(f"TOPIC {topic}: {title.upper()} — LECTURE COMPENDIUM", styles["CourseTitle"])],
        [Paragraph(
            "<b>Audience:</b> First-year undergraduate students<br/>"
            "<b>Approach:</b> Introductory concepts, guided examples, and "
            "discipline-relevant applications<br/>"
            f"<b>Topic overview:</b> {html.escape(summary)}",
            styles["MetaBox"],
        )],
    ]
    table = Table(header, colWidths=[7.2 * inch])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), COLOR_BG_LIGHT),
        ("BOX", (0, 0), (-1, -1), 1.2, COLOR_SUA_GREEN),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(table)
    story.append(Spacer(1, 10))


def build_pdf(topic, story):
    out_path = NOTES_DIR / f"BIT_111_Topic_{topic}_Compendium.pdf"
    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=letter,
        leftMargin=46,
        rightMargin=46,
        topMargin=54,
        bottomMargin=46,
        title=f"BIT 111 Topic {topic}: {TITLES[topic][0]}",
        author="Sokoine University of Agriculture",
    )
    doc.build(
        story,
        canvasmaker=lambda *args, **kwargs: NumberedCanvas(
            *args, doc_title=f"BIT 111 Topic {topic}: {TITLES[topic][0]}", **kwargs
        ),
    )
    result = subprocess.run(
        ["pdfinfo", str(out_path)], check=True, capture_output=True, text=True
    )
    page_line = next(line for line in result.stdout.splitlines() if line.startswith("Pages:"))
    page_count = int(page_line.split(":", 1)[1].strip())
    if page_count < 40:
        raise RuntimeError(
            f"Topic {topic} compendium has {page_count} pages; at least 40 are required."
        )
    print(f"Generated {out_path} ({page_count} pages)")


def build_all_compendia():
    manifest = load_attributions()
    styles = get_custom_stylesheet()
    from build_compedia_topic1 import generate_topic_1_story
    from build_compedia_topic2 import generate_topic_2_story
    from slides_topics_1_to_3 import (
        get_topic_3_slides,
    )
    from slides_topics_4_to_6 import (
        get_topic_4_slides,
        get_topic_5_slides,
        get_topic_6_slides,
    )

    topic_stories = {
        1: generate_topic_1_story(),
        2: generate_topic_2_story(),
    }
    slide_sources = {
        3: get_topic_3_slides(),
        4: get_topic_4_slides(),
        5: get_topic_5_slides(),
        6: get_topic_6_slides(),
    }
    for topic in range(1, 7):
        story = topic_stories.get(topic)
        if story is None:
            story = []
            add_cover(story, topic, styles)
            add_slide_notes(story, topic, slide_sources[topic], styles)
        add_online_figure_pages(story, topic, manifest[str(topic)], styles)
        make_reference_page(story, topic, styles)
        build_pdf(topic, story)


if __name__ == "__main__":
    build_all_compendia()
