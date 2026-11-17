# 🛠️ AGE 418: Assignment Generation Scripts

This directory houses the reproducible Python scripts used to compile and maintain **Practical Assignment 1 (Academic Year 2026/2027)** for **AGE 418: Sensors and Controls in Precision Agriculture** at Sokoine University of Agriculture (SUA).

---

## 📋 Directory Contents

| Script | Purpose | Output Deliverables |
| :--- | :--- | :--- |
| [`pdf_builder.py`](file:///Users/kadefue/Course%20Notes/AGE%20418/Scripts/pdf_builder.py) | Pure Python PDF generator engine (PDF 1.4 specification). Implements standard Type 1 Helvetica font metrics, raw RGBA PNG parsing/unfiltering with alpha masks (`SUA.png`), running headers with mini-logos, callout boxes, and running footers with dynamic page numbering. | Supporting module / class library. |
| [`generate_assignment_1_pdf.py`](file:///Users/kadefue/Course%20Notes/AGE%20418/Scripts/generate_assignment_1_pdf.py) | Compiles the official 5-page publication-grade PDF document of Practical Assignment 1. Automatically embeds the SUA crest, metadata table, research questions, guidelines, and GitHub submission instructions. | • `AGE 418/Assignment 2026-2027/Assignment 1.pdf`<br>• `AGE 418/Assignment 2026/2027/Assignment 1.pdf` |
| [`generate_assignment_1_md.py`](file:///Users/kadefue/Course%20Notes/AGE%20418/Scripts/generate_assignment_1_md.py) | Generates and updates the rich Markdown versions of Practical Assignment 1, including full tables, callout blocks, mathematical formatting, and programmatic alignments for **BSc AE** and **BSc IWRE**. | • `AGE 418/Assignment 2026-2027/Assignment 1.md`<br>• `AGE 418/Assignment 2026-2027/README.md`<br>• `AGE 418/Assignment 2026/2027/Assignment 1.md`<br>• `AGE 418/Assignment 2026/2027/README.md` |

---

## ⚙️ Requirements & Dependencies

* **Python**: Python 3.8+
* **Dependencies**: **Zero external dependencies** (strictly uses Python standard library: `os`, `sys`, `struct`, `zlib`).
* **Assets**: Requires `SUA.png` in the repository root directory (`Course Notes/SUA.png`).

---

## 🚀 Usage Instructions

To regenerate all assignment files, run the following commands from terminal:

```bash
# 1. Regenerate Markdown Guides & Documentation
python3 "generate_assignment_1_md.py"

# 2. Recompile the Official 5-Page PDF Deliverable
python3 "generate_assignment_1_pdf.py"
```

Both scripts use dynamic relative path discovery (`os.path.abspath(os.path.join(script_dir, "..", ".."))`), allowing execution from any working directory.
