#!/usr/bin/env python3
"""
make_all_materials.py
Master generation and compilation engine for BIT 111: Microcomputers and Applications.
Department of Informatics and Information Technology (DIIT),
Sokoine University of Agriculture (SUA).

Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Builds six comprehensive course compendia (at least 40 pages each), six
course assignments, and six 16:9 lecture slide decks (at least 30 slides
each), using the existing course content and attributed Internet figures.
"""

import os
import subprocess
import sys

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))


def run_script(filename):
    script_path = os.path.join(SCRIPTS_DIR, filename)
    print(f"[Running] {filename}")
    subprocess.run([sys.executable, script_path], check=True)


def main():
    print("Building the six BIT 111 compendia, lecture decks, and course materials...")
    run_script("generate_figures.py")
    run_script("prepare_internet_figures.py")
    run_script("build_compendia.py")
    run_script("build_assignments.py")
    run_script("build_slides.py")
    print("All six BIT 111 compendia, assignments, and lecture decks generated.")


if __name__ == "__main__":
    main()
