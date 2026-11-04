#!/usr/bin/env python3
"""
build_compedia.py
Master build script for AEN 214: Introduction to Electronics.
Sequentially invokes build_compedia_1.py through build_compedia_9.py to compile
all lecture notes (compendia) into the Notes/ directory.
Also builds the course outline and assignments.
Department of Agricultural Engineering, Sokoine University of Agriculture.
"""

import os
import sys
import subprocess
import time

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name, description):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if not os.path.exists(script_path):
        print(f"[Error] Script {script_name} not found at {script_path}")
        return False

    print(f"\n==================================================")
    print(f"--> [Compiling] {description} ({script_name})...")
    print(f"==================================================")
    start_t = time.time()
    try:
        # Import module directly or execute as subprocess
        res = subprocess.run([sys.executable, script_path], cwd=SCRIPTS_DIR, check=True)
        elapsed = time.time() - start_t
        print(f"[OK] Completed {script_name} in {elapsed:.2f}s")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[FAILED] Error running {script_name}: {e}")
        return False
    except Exception as e:
        print(f"[FAILED] Unexpected error running {script_name}: {e}")
        return False

def main():
    print("*****************************************************************")
    print("*  AEN 214: INTRODUCTION TO ELECTRONICS - MASTER COMPENDIA BUILD *")
    print("*  Department of Agricultural Engineering - SUA Morogoro        *")
    print("*****************************************************************")
    total_start = time.time()

    # Step 1: Ensure figures exist
    figures_script = "generate_figures.py"
    if os.path.exists(os.path.join(SCRIPTS_DIR, figures_script)):
        print("\nVerifying course figures and hardware images...")
        run_script(figures_script, "Course Figures & Hardware Crawler")

    # Step 2: Build Lecture Compendia 1 through 9
    compendia_scripts = [
        ("build_compedia_1.py", "Lecture 1: Passive Electronic Components"),
        ("build_compedia_2.py", "Lecture 2: Semiconductor Physics"),
        ("build_compedia_3.py", "Lecture 3: Semiconductor Diode & Circuits"),
        ("build_compedia_4.py", "Lecture 4: Special Purpose Diodes"),
        ("build_compedia_5.py", "Lecture 5: Bipolar Junction Transistor (BJT)"),
        ("build_compedia_6.py", "Lecture 6: Field Effect Transistor (FET & MOSFET)"),
        ("build_compedia_7.py", "Lecture 7: Number Systems & Arithmetic Operations"),
        ("build_compedia_8.py", "Lecture 8: Introduction to Digital Electronics"),
        ("build_compedia_9.py", "Lecture 9: Boolean Algebra & Karnaugh Maps")
    ]

    success_count = 0
    for script_file, desc in compendia_scripts:
        if run_script(script_file, desc):
            success_count += 1

    # Step 3: Build Course Outline Document
    run_script("build_outline.py", "Official Course Outline & Learning Contract")

    # Step 4: Build Coursework Assignments 1, 2, 3
    run_script("build_assignments.py", "Three Open Coursework Assignments (Assignment 1, 2, 3)")

    # Step 5: Build Lecture Slides (PPTX & PDF)
    run_script("build_slides.py", "Lecture Slides (9 PPTX & PDF Presentations)")

    total_time = time.time() - total_start
    print("\n*****************************************************************")
    print(f"*  BUILD SUMMARY: {success_count}/9 Compendia successfully generated! *")
    print(f"*  Total Elapsed Time: {total_time:.2f} seconds                        *")
    print("*****************************************************************")

if __name__ == "__main__":
    main()
