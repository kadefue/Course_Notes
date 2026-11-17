"""Regression tests for equation formatting in generated slides."""

import unittest

from pptx import Presentation
from pptx.util import Inches

from build_slides import add_title_slide, notation_runs, text_box


class EquationNotationTests(unittest.TestCase):
    def test_equation_indices_and_powers(self):
        examples = {
            "V_GS = 10^-3": [("V", 0), ("GS", -25000), (" = 10", 0), ("-3", 30000)],
            "T^(3/2)": [("T", 0), ("3/2", 30000)],
            "2^(N-1)": [("2", 0), ("N-1", 30000)],
            "10^16": [("10", 0), ("16", 30000)],
            "B_{i+1}": [("B", 0), ("i+1", -25000)],
            "B_{2's}": [("B", 0), ("2's", -25000)],
            "S_N-1": [("S", 0), ("N-1", -25000)],
            "I_DC_avg": [("I", 0), ("DC,avg", -25000)],
            "dI_D |_(Q-point)": [
                ("dI", 0), ("D", -25000), (" |", 0), ("Q-point", -25000)
            ],
            "I_D²": [("I", 0), ("D", -25000), ("²", 0)],
        }
        for source, expected in examples.items():
            with self.subTest(source=source):
                self.assertEqual(notation_runs(source), expected)

    def test_rejects_unmatched_markers(self):
        for source in ("V_", "10^", "B_{broken"):
            with self.subTest(source=source):
                with self.assertRaises(ValueError):
                    notation_runs(source)

    def test_text_box_emits_formatted_editable_runs(self):
        presentation = Presentation()
        slide = presentation.slides.add_slide(presentation.slide_layouts[6])
        shape = text_box(slide, 0, 0, 8, 1, "V_GS = 10^-3\nI_D²", 28)
        paragraph = shape.text_frame.paragraphs[0]
        self.assertEqual(shape.text_frame.text, "VGS = 10-3\vID²")
        self.assertEqual(
            [run._r.get_or_add_rPr().get("baseline") for run in paragraph.runs],
            [None, "-25000", None, "30000", None, "-25000", None],
        )
        self.assertEqual(shape.width, Inches(8))


class SlideMetadataTests(unittest.TestCase):
    def test_title_slide_academic_year(self):
        presentation = Presentation()
        slide = add_title_slide(presentation, 1, "Example", "Example subtitle")
        text = " ".join(shape.text_frame.text for shape in slide.shapes if shape.has_text_frame)
        self.assertIn("Academic Year 2026/2027", text)
        self.assertNotIn("2025/2026", text)


if __name__ == "__main__":
    unittest.main()
