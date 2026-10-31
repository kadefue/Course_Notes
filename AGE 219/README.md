# 💻 AGE 219: Basics of Computer Programming
### Sokoine University of Agriculture (SUA) | Department of Agricultural Engineering

[![Course Level](https://img.shields.io/badge/Level-Undergraduate%20(Year%202)-blue.svg)](#)
[![Programs](https://img.shields.io/badge/Target%20Programs-BSc%20AE%20%7C%20BSc%20IWRE%20%7C%20BSc%20BPHE-forestgreen.svg)](#target-audience--degree-program-case-studies)
[![Toolchain](https://img.shields.io/badge/Toolchain-Python%203.x%20%7C%20Google%20Colab-orange.svg)](#)

---

## 📖 Course Overview

**AGE 219: Basics of Computer Programming** is the introductory programming and computational problem-solving course for second-year engineering students in the School of Engineering and Technology (SoET) at Sokoine University of Agriculture. Instructed by **Dr. Kadeghe Fue**, the course serves as the foundational bridge transitioning traditional agricultural mechanics and civil hydraulics into **Agriculture 4.0** and **AgriTech**.

Utilizing **Python 3.x** and **Google Colaboratory**, students master programming logic, data structures, modular programming, object-oriented design, file processing, and data visualization entirely within interactive cloud environments without complex local software installation requirements.

---

## 🎯 Target Audience & Degree Program Case Studies

Every programming concept in AGE 219 is paired with an authentic biosystems engineering case study tailored to our three undergraduate cohorts:

1. **BSc in Agricultural Engineering (BSc AE)**:
   * **Fertilizer Application Calculation (Lec 2)**: Programmatic calculation of nitrogen, phosphorus, and potassium (NPK) application rates (kg/ha) for maize cultivation.
   * **Implement Draft Force Modeling (Lec 5)**: Custom functions calculating the specific draft force and power requirements of moldboard plows based on soil shear strength and implement geometry.
   * **Machinery OOP & Telematics (Lecs 8 & 9)**: Object-Oriented `Tractor` classes modeling fuel consumption, operational speed, and slip; visualizing engine load vs. fuel efficiency from CAN-bus telematics.

2. **BSc in Irrigation and Water Resources Engineering (BSc IWRE)**:
   * **Smart Irrigation Simulator (Lec 3)**: Conditional control flow logic (`if/elif/else`) simulating automated solenoid valve triggers based on field soil moisture tension thresholds.
   * **Cumulative Rainfall & Water Requirements (Lec 4)**: Iterative loops processing 7-day cumulative rainfall records to calculate net irrigation requirements against crop evapotranspiration ($ET_c$).
   * **Weather Data Ingestion (Lec 7)**: Reading historical meteorological CSV datasets to compute reference evapotranspiration ($ET_o$) using temperature and solar radiation data.

3. **BSc in Bioprocess and Post-Harvest Engineering (BSc BPHE)**:
   * **IoT Greenhouse & Silo Telemetry (Lec 6)**: Organizing multi-sensor payloads (temperature, relative humidity, $CO_2$) in structured nested dictionaries and lists.
   * **Frost & Spoilage Event Detection (Lec 7)**: Parsing storage facility temperature logs to flag critical temperature-dip events threatening produce quality.
   * **Capstone Mini-Project: "The Smart Grain Bin Manager" (Lec 10)**: Full-stack integration calculating equilibrium moisture content (EMC), psychrometric dew point, and spoilage risk to trigger automated bin aeration fans.

---

## 🗺️ Detailed Lecture Schedule

| Lecture | Topic & Engineering Scope | Practical Applied Case Study |
| :--- | :--- | :--- |
| **Lecture 1** | **Introduction to Programming & Colab** | The role of code in Agriculture 4.0; Code cells vs. Markdown; *"Hello, Farm!"* script. |
| **Lecture 2** | **Variables, Data Types & Operators** | PEP 8 conventions, type casting, arithmetic/comparison operators; Fertilizer rate math. |
| **Lecture 3** | **Control Flow & Decision Making** | Conditional logic, logical operators (`and`, `or`, `not`); Soil moisture irrigation engine. |
| **Lecture 4** | **Iteration and Loops** | `for`/`while` loops, accumulator patterns; 7-day cumulative rainfall & crop water budget. |
| **Lecture 5** | **Functions & Modular Programming** | Function definitions, arguments, return values; Tractor plow draft force calculation. |
| **Lecture 6** | **Data Structures (Lists & Dictionaries)** | List indexing/slicing, key-value mappings; Structuring IoT greenhouse telemetry. |
| **Lecture 7** | **File Handling & Data Import** | Reading/writing CSV files, cloud uploads; Identifying orchard frost events from CSV. |
| **Lecture 8** | **Object-Oriented Programming (OOP)** | Classes, `__init__`, encapsulation; Agricultural machinery objects (`Tractor` class). |
| **Lecture 9** | **Data Analysis & Plotting (Pandas/Matplotlib)** | DataFrames, data cleaning, line/scatter plots; Tractor engine load vs. fuel consumption. |
| **Lecture 10**| **Final Mini-Project Integration** | Full-stack computational logic; *"The Smart Grain Bin Manager"* automated storage system. |

---

## 🗂️ Materials in this Directory

* **Syllabus & Contract**:
  * [`Course Outline.pdf`](file:///home/kadefue/Course_Notes/AGE%20219/Course%20Outline.pdf): Official Course Syllabus and Learning Contract including academic honesty and AI guidelines.
* **Compendia (`.pdf`)**:
  * 10 complete lecture compendia (`Lecture Compendium 1.pdf` through `Lecture Compendium 10.pdf`).
* **Lecture Presentations (`.pptx`)**:
  * Slide decks for Lectures 1 through 10.
* **Assignments & Continuous Tests**:
  * `Assignment 2.pdf`
  * Continuous Assessment Tests: `AGE 219 Test One 2023-2024.docx`, `AGE 219 Test Two 2023-2024.docx`, and `AGE 219 Test 1 2024_2025.docx`.

---

## ⚖️ Academic Integrity & AI Policy

* **Code Originality**: Students are required to write their own logic. Copying code without attribution is considered academic misconduct. Students must be prepared to explain every line of their code during oral defense evaluations.
* **Responsible AI Usage**: Generative AI (ChatGPT, Gemini) is permitted solely as a personal tutor to explain errors and debug syntax. Generating complete assignments using AI is prohibited. All AI assistance must be disclosed in the Python notebook header comments.
