# ⚡ AEN 214: Introduction to Electronics
### Sokoine University of Agriculture (SUA) | Department of Agricultural Engineering

[![Course Level](https://img.shields.io/badge/Level-Undergraduate%20(Year%202)-blue.svg)](#)
[![Curriculum](https://img.shields.io/badge/Curriculum-New%20Curriculum%20(AEN%20214)-success.svg)](#-curriculum-overview)
[![Target Programs](https://img.shields.io/badge/Target%20Programs-BSc%20AE%20%7C%20BSc%20IWRE%20%7C%20BSc%20BPHE-forestgreen.svg)](#target-audience--degree-program-relevance)
[![Lab](https://img.shields.io/badge/Lab-Electronics%20%26%20Precision%20Agriculture%20(EPAL)-purple.svg)](#)

---

## 📖 Course Overview & Curriculum Framework

**AEN 214: Introduction to Electronics** is the foundational core course in analog and digital electronics designed for second-year undergraduate engineering students in the School of Engineering and Technology (SoET) at Sokoine University of Agriculture (SUA). Delivered by the **Electronics and Precision Agriculture Lab (EPAL)** under **Dr. Kadeghe Goodluck Fue, PhD, P.Eng (T)**, the course provides the theoretical, physical, and practical hardware foundations for modern agricultural mechanization, sensor instrumentation, precision agriculture, and cyber-physical automation.

### Course Metadata:
* **Course Code:** AEN 214
* **Course Title:** Introduction to Electronics
* **Course Status:** Elective / Core Engineering
* **Credit Rating:** 6 Credits
* **Total Notional Hours:** 60 Hours (Lectures, Tutorials, Laboratory Experiments, Field Case Studies)
* **Academic Year:** 2025/2026 & 2026/2027

---

## 🎯 Course Expected Learning Outcomes (CELOs)

By the conclusion of this course, engineering students will be able to:
1. **Describe and evaluate** fundamental analog and digital electronics concepts and their strategic role in agricultural automation and biosystems engineering.
2. **Analyze electronic components** and evaluate their characteristics, including resistors, capacitors, inductors, diodes, BJTs, and FETs.
3. **Analyze and design basic analog circuits**, such as sensor pre-amplifiers, active/passive filters, voltage regulators, and timing oscillators for farm transducers.
4. **Synthesize and minimize digital logic circuits**, applying Boolean algebra laws, De Morgan's theorems, and Karnaugh maps to implement combinational and sequential agricultural controllers.
5. **Explain principles of data conversion**, including Analog-to-Digital (ADC) and Digital-to-Analog (DAC) converters interfacing field sensors with microcontrollers.
6. **Apply power semiconductors and microcontrollers** to drive high-current agricultural actuators (solenoids, relays, water pumps, linear actuators).
7. **Develop hands-on laboratory skills** in circuit prototyping, breadboarding, oscilloscope diagnostics, and systematic hardware troubleshooting.
8. **Explore emerging trends and technologies** in analog and digital electronics relevant to modern agricultural engineering (IoT telemetry, solar PV balance-of-systems, autonomous robotics).

---

## 🗂️ Directory Architecture

```tree
AEN 214/
├── Notes/                  # Comprehensive Lecture Compendia & Official Syllabus (PDF)
│   ├── AEN_214_Course_Outline.pdf
│   ├── AEN_214_Lecture_1_Compendium.pdf  # Passive Electronic Components
│   ├── AEN_214_Lecture_2_Compendium.pdf  # Semiconductor Physics
│   ├── AEN_214_Lecture_3_Compendium.pdf  # Semiconductor Diode & Circuits
│   ├── AEN_214_Lecture_4_Compendium.pdf  # Special Purpose Diodes
│   ├── AEN_214_Lecture_5_Compendium.pdf  # Bipolar Junction Transistor (BJT)
│   ├── AEN_214_Lecture_6_Compendium.pdf  # Field Effect Transistors (FET & MOSFET)
│   ├── AEN_214_Lecture_7_Compendium.pdf  # Number Systems & Digital Arithmetic
│   ├── AEN_214_Lecture_8_Compendium.pdf  # Introduction to Digital Electronics
│   └── AEN_214_Lecture_9_Compendium.pdf  # Boolean Algebra & Karnaugh Maps
│
├── Assignment/             # Open Coursework Assignments (>10 tiered questions each)
│   ├── AEN_214_Assignment_1.pdf          # Topics 1 - 3 (Passive, Physics, Diodes)
│   ├── AEN_214_Assignment_2.pdf          # Topics 4 - 6 (Special Diodes, BJT, FET)
│   └── AEN_214_Assignment_3.pdf          # Topics 7 - 9 (Numbers, Digital, K-Maps)
│
├── Lectures/               # 16:9 Presentation Slide Decks (PPTX and PDF)
│   ├── AEN_214_Lecture_1.pptx & .pdf
│   ├── AEN_214_Lecture_2.pptx & .pdf
│   ├── AEN_214_Lecture_3.pptx & .pdf
│   ├── AEN_214_Lecture_4.pptx & .pdf
│   ├── AEN_214_Lecture_5.pptx & .pdf
│   ├── AEN_214_Lecture_6.pptx & .pdf
│   ├── AEN_214_Lecture_7.pptx & .pdf
│   ├── AEN_214_Lecture_8.pptx & .pdf
│   └── AEN_214_Lecture_9.pptx & .pdf
│
├── Figures/                # High-resolution schematics, curves, and crawled hardware photos
│   ├── fig1_1_resistor_color_code.png
│   ├── fig1_2_rc_transient.png
│   ├── fig1_3_reactance_curves.png
│   ├── fig1_4_passive_filter_schematic.png
│   ├── fig2_1_bohr_atom_silicon.png
│   ├── fig2_2_energy_bands.png
│   ├── fig2_3_pn_junction_equilibrium.png
│   ├── fig2_4_hall_effect_sensor.png
│   ├── fig3_1_diode_iv_characteristics.png
│   ├── fig3_2_bridge_rectifier_schematic.png
│   ├── fig3_3_rectifier_waveforms.png
│   ├── fig3_4_clipper_clamper_circuits.png
│   ├── fig4_1_zener_regulator_schematic.png
│   ├── fig4_2_zener_iv_characteristics.png
│   ├── fig4_3_led_operation.png
│   ├── fig4_4_schottky_diode.png
│   ├── fig5_1_bjt_structure_symbols.png
│   ├── fig5_2_bjt_ce_output_characteristics.png
│   ├── fig5_3_voltage_divider_bias.png
│   ├── fig5_4_bjt_relay_driver.png
│   ├── fig6_2_jfet_characteristics.png
│   ├── fig6_4_power_mosfet_motor_driver.png
│   ├── fig7_1_number_systems_hierarchy.png
│   ├── fig7_2_twos_complement_circle.png
│   ├── fig8_1_standard_logic_gates.png
│   ├── fig8_3_half_full_adder_circuits.png
│   ├── fig8_4_greenhouse_ventilation_system.png
│   ├── fig9_1_demorgan_switching_circuits.png
│   ├── fig9_2_kmap_configurations.png
│   └── [Authentic crawled hardware photos: resistors, capacitors, diodes, BJTs, MOSFETs, breadboards]
│
└── Scripts/                # Python generation pipeline scripts
    ├── compendium_base.py  # Shared ReportLab academic styling & NumberedCanvas
    ├── generate_figures.py # Matplotlib, schemdraw & Wikipedia API crawler
    ├── build_compedia_1.py # Lecture 1 Compendium Generator
    ├── build_compedia_2.py # Lecture 2 Compendium Generator
    ├── build_compedia_3.py # Lecture 3 Compendium Generator
    ├── build_compedia_4.py # Lecture 4 Compendium Generator
    ├── build_compedia_5.py # Lecture 5 Compendium Generator
    ├── build_compedia_6.py # Lecture 6 Compendium Generator
    ├── build_compedia_7.py # Lecture 7 Compendium Generator
    ├── build_compedia_8.py # Lecture 8 Compendium Generator
    ├── build_compedia_9.py # Lecture 9 Compendium Generator
    ├── build_outline.py    # Official Course Outline & Syllabus Generator
    ├── build_assignments.py# Open Assignments 1, 2, 3 Generator
    ├── build_slides.py     # 16:9 PPTX Slides & LibreOffice PDF Converter
    └── build_compedia.py   # Master orchestration script
```

---

## 🗺️ Detailed Syllabus & Lecture Modules

| Lecture | Curriculum Topic | Core Theoretical Concepts & Derivations | Agricultural Engineering Applications |
| :--- | :--- | :--- | :--- |
| **Lecture 1** | **Passive Electronic Components** | Resistors (carbon, metal film, wirewound, SMD, color codes, power rating, TCR); Capacitors (electrostatics, dielectrics, codes, RC transient timing); Inductors (Faraday/Lenz laws, magnetic cores, flyback spike hazards); Reactance ($X_C, X_L$), impedance, and resonance ($f_0$). | Sizing RC low-pass filters for soil moisture probes; grain silo thermistor monitoring cables; ISO 134.2 kHz livestock RFID ear-tag tank circuits. |
| **Lecture 2** | **Semiconductor Physics** | Atomic Bohr model ($Z=14$ Silicon); Energy band theory (valence, conduction, forbidden bandgap $E_g$); Intrinsic vs extrinsic semiconductors; Doping kinetics (Group V donors, Group III acceptors); Law of Mass Action ($n \cdot p = n_i^2$); Space-charge depletion layer; Built-in barrier potential ($V_0$); Forward/reverse bias kinetics; The Hall Effect ($V_H = I_x B_z / n q t$). | Non-contact Hall effect wheel speed and PTO shaft tachometers; seed-dropping counters; BLDC motor rotor commutation in drone sprayers. |
| **Lecture 3** | **Semiconductor Diode & Circuits** | Shockley diode equation; Derivation of dynamic AC junction resistance ($r_d = \eta V_T / I_D$); Diode approximations (1st, 2nd, 3rd piecewise linear); Half-wave and full-wave bridge rectifiers; Smoothing capacitor sizing ($V_{r(p-p)} = I_{dc} / 2fC$); Diode clippers and clampers. | Full-wave DC power supply design for automated greenhouse valves; dual-Schottky input voltage clipping for combine harvester yield monitors. |
| **Lecture 4** | **Special Purpose Diodes** | Zener diode reverse breakdown (Zener tunneling < 5V vs Avalanche multiplication > 6V); Temperature coefficients; Shunt voltage regulator design (line and load regulation, $R_S$ sizing); LEDs (direct bandgap electroluminescence, $\lambda = 1240/E_g$); Schottky barrier diodes (majority carrier, $t_{rr} \approx 0$, low $V_F$ drop). | Shunt voltage references for tractor cab sensor ADCs; Photosynthetically Active Radiation (PAR) LED grow lights for strawberry greenhouses; Schottky bypass diodes preventing PV solar panel hot-spot fires. |
| **Lecture 5** | **Bipolar Junction Transistor (BJT)** | BJT physics (NPN, PNP, doping profiles); Biasing rules; Configurations (CB, CE, CC); Current gains ($\alpha, \beta, \gamma$); Leakage currents ($I_{CBO}, I_{CEO}$); Thermal runaway and emitter degeneration ($R_E$); DC load line and Q-point stability; Voltage-divider bias; Saturated low-side switch ($ODF \ge 3$); Small-signal CE amplifier ($r_e$ model, $A_v = -R_C / r_e$). | Interfacing 3.3V microcontroller GPIOs with 12V hydraulic irrigation solenoids with flyback diode protection; small-signal CE preamplifiers for load cells. |
| **Lecture 6** | **Field Effect Transistors (FET & MOSFET)** | Unipolar voltage-controlled conduction; JFET structure and pinch-off ($V_P$); Shockley transfer equation ($I_D = I_{DSS}(1 - V_{GS}/V_P)^2$); Transconductance ($g_m$); Depletion-Enhancement MOSFET (DE-MOSFET); Enhancement-only MOSFET (E-MOSFET, inversion layer, $V_{GS(th)}$); Power MOSFETs ($R_{DS(on)}$ in milliohms); Safe paralleling; Gate oxide ESD vulnerability. | High-impedance ($10^{12} \ \Omega$) soil pH electrode buffers; PWM motor speed control for 24V solar submersible borehole pumps; heatsink thermal sizing ($R_{\theta JA}$). |
| **Lecture 7** | **Number Systems & Arithmetic Operations** | Positional radices (Binary, Octal, Decimal, Hexadecimal); Inter-base conversion algorithms; Signed two's complement integer representation (range $-2^{n-1}$ to $+2^{n-1}-1$); Subtraction as addition; Overflow detection ($V = C_{in} \oplus C_{out}$); BCD 8421 coding (+6 correction); Gray code (unit-distance, bit toggling); ASCII & NMEA telemetry. | Absolute Gray-code optical shaft encoders for autonomous tractor steering without race hazards; parsing NMEA 0183 GPS strings ($GPGGA) for field guidance. |
| **Lecture 8** | **Introduction to Digital Electronics** | Logic gates (AND, OR, NOT, NAND, NOR, XOR, XNOR); Truth tables, expressions, and IEEE symbols; Universal gate synthesis using NAND/NOR; Propagation delays ($t_{pd}$); Half Adders and Full Adders (ripple carry); Combinational logic synthesis; Sequential logic (SR latches, D flip-flops, JK flip-flops). | Combinational interlock circuits for automated smart greenhouse ventilation dampers; grain flow data accumulator full adders; tractor pulse counters. |
| **Lecture 9** | **Boolean Algebra & Karnaugh Maps** | Axioms and laws of Boolean algebra (Identity, Null, Idempotent, Distributive, Absorption); De Morgan's theorems; Canonical Sum of Products (SOP, minterms $\sum m$) and Product of Sums (POS, maxterms $\prod M$); 2, 3, and 4-variable Karnaugh Maps (Gray code order); Looping rules; Don't Care conditions ($X$); Static-1 hazard elimination. | Algebraic and K-map optimization of multi-sensor automated cross-flow grain dryer burner shutdown logic; glitch-free hydraulic lift control in combine harvesters. |

---

## 🛠️ Execution & Build Pipeline

All course notes, assignments, figures, and presentations are completely reproducible via the automated Python scripts in `Scripts/`:

```bash
# Navigate to the Scripts directory
cd "AEN 214/Scripts"

# 1. Generate all circuit diagrams, plots, and crawl hardware photos
python3 generate_figures.py

# 2. Compile all 9 lecture compendia individually or via master script
python3 build_compedia.py

# 3. Compile the official course syllabus & learning contract
python3 build_outline.py

# 4. Generate the three open coursework assignments (>10 questions each)
python3 build_assignments.py

# 5. Generate 16:9 PPTX slide decks and convert to PDF via LibreOffice
python3 build_slides.py
```

---

## 📚 Prescribed Textbooks & Reading List

1. **Boylestad, R. L., & Nashelsky, L. (2018).** *Electronic Devices and Circuit Theory* (11th ed.). Pearson Education.
2. **Sedra, A. S., & Smith, K. C. (2020).** *Microelectronic Circuits* (8th ed.). Oxford University Press.
3. **Mano, M. M., & Ciletti, M. D. (2017).** *Digital Design: With an Introduction to the Verilog HDL, VHDL, and SystemVerilog* (6th ed.). Pearson.
4. **Karim, M. A., & Chen, X. (2017).** *Digital Design: Basic Concepts and Principles*. CRC Press.
5. **Person (2015).** *Mechatronics: Electronic Control Systems in Mechanical and Electrical Engineering* (6th ed.). Pearson. ISBN-10: 9781292076683.
6. **Floyd, T. L. (2017).** *Electronic Devices: Conventional Current Version* (10th ed.). Pearson.
7. **Johnson, M. A., & Smith, K. L. (2023).** Fundamentals of Electronics: An Introduction. *IEEE Transactions on Education*, 66(3), 456-465.
8. **Brown, R. J., & Davis, P. W. (2023).** Basic Electronic Components and Circuits. *Journal of Electrical Engineering*, 44(2), 78-85.
9. **Williams, S. E., & Wilson, T. A. (2023).** Introduction to Semiconductor Devices and Circuits. *Journal of Applied Physics*, 135(6), 065420.

---

**Course Instructor:** Dr. Kadeghe Goodluck Fue, PhD, P.Eng (T)  
**Department:** Agricultural Engineering  
**Faculty:** School of Engineering and Technology (SoET)  
**Institution:** Sokoine University of Agriculture (SUA), Morogoro, Tanzania
