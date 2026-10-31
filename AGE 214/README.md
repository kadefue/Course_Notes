# ⚡ AEN 214 / AGE 214: Introduction to Electronics
### Sokoine University of Agriculture (SUA) | Department of Agricultural Engineering

[![Course Level](https://img.shields.io/badge/Level-Undergraduate%20(Year%202)-blue.svg)](#)
[![Curriculum](https://img.shields.io/badge/Curriculum-New%20(AEN%20214)%20%2F%20Legacy%20(AGE%20214)-success.svg)](#-curriculum-transition-notice-20252026--20262027)
[![Programs](https://img.shields.io/badge/Target%20Programs-BSc%20AE%20%7C%20BSc%20IWRE%20%7C%20BSc%20BPHE-forestgreen.svg)](#target-audience--degree-program-relevance)
[![Lab](https://img.shields.io/badge/Lab-Electronics%20%26%20Precision%20Agriculture%20(EPAL)-purple.svg)](#)

---

> [!NOTE] Curriculum Transition Notice (Academic Years 2025/2026 & 2026/2027)
> Under the revised curriculum launched in academic year **2025/2026**, this course is officially designated as **AEN 214: Introduction to Electronics**.
> In the current academic year **2026/2027**, **First-Year** and **Second-Year** students follow the new curriculum (**AEN 214**), while continuing senior students (Third and Fourth Years) remain under the older curriculum (**AGE 214**).
> The comprehensive compendia, slide decks, and laboratory tutorials in this directory provide full coverage for students across both curriculum designations.

---

## 📖 Course Overview

**AEN 214 / AGE 214: Introduction to Electronics** is the foundational electronic engineering course for second-year undergraduate students in the School of Engineering and Technology (SoET) at Sokoine University of Agriculture. Delivered by the **Electronics and Precision Agriculture Lab (EPAL)** under **Dr. Kadeghe Goodluck Fue**, the course establishes the physical and circuit-level foundations required for modern agricultural sensors, instrumentation, microcomputers, and automated machinery controls.

The curriculum covers semiconductor physics, discrete active and passive components (diodes, BJTs, FETs, MOSFETs), analog operational amplifiers (Op-Amps), power supply design, and introductory digital interfacing for Data Acquisition (DAQ) systems.

---

## 🎯 Target Audience & Degree Program Relevance

1. **BSc in Agricultural Engineering (BSc AE)**:
   * **Power Electronics**: Understanding MOSFET and transistor switching circuits to drive high-current agricultural actuators (solenoids, linear actuators, starter motors).
   * **Implement Instrumentation**: Designing amplifier conditioning circuits for strain gauges and load cells on tractor three-point hitches.
   * **Power Conversion**: Converting erratic 12V/24V tractor alternator DC to stable 5V/3.3V DC for onboard electronic control units (ECUs).

2. **BSc in Irrigation and Water Resources Engineering (BSc IWRE)**:
   * **Sensor Signal Amplification**: Conditioning weak millivolt analog signals from capacitive soil moisture probes, ultrasonic level sensors, and pressure transducers using operational amplifiers.
   * **Valve Actuation Circuits**: Designing transistor driver stages to actuate 12V/24V solenoid irrigation valves safely without back-EMF damage.

3. **BSc in Bioprocess and Post-Harvest Engineering (BSc BPHE)**:
   * **Thermal Instrumentation**: Interfacing RTD (Pt100) and thermistor temperature sensors with bridge and differential amplifier circuits for grain dryers and pasteurizers.
   * **Process Heating & Speed Control**: Utilizing power transistors and solid-state relays (SSRs) to regulate heater coils, blower fans, and conveyor motors.

---

## 🗺️ Syllabus & Lecture Breakdown

| Lecture | Topic | Core Theoretical Concepts & Laboratory Applications |
| :--- | :--- | :--- |
| **Lec 1** | **Introduction & Semiconductor Physics** | Energy bands, valence/conduction bands, intrinsic vs extrinsic carriers, doping. |
| **Lec 2** | **Classification of Materials** | Conductors, semiconductors, insulators, Fermi-Dirac distribution, carrier mobility. |
| **Lec 3** | **The PN Junction Diode** | Depletion region formation, built-in potential $V_{bi}$, forward and reverse bias physics. |
| **Lec 4** | **Diode Characteristics & Equivalent Circuits** | Shockley diode equation, dynamic resistance $r_d$, piece-wise linear models. |
| **Lec 5** | **Rectifier Circuits** | Half-wave, full-wave center-tapped, and bridge rectifiers; PIV, ripple factor ($\gamma$), and efficiency ($\eta$). |
| **Lec 6** | **Filters & Zener Voltage Regulators** | Shunt capacitor filters, ripple voltage reduction, Zener breakdown voltage regulation. |
| **Lec 7** | **Clippers and Clampers** | Biased clipping circuits, peak limiters, DC restorers and clamping networks. |
| **Lec 8** | **Bipolar Junction Transistor (BJT)** | NPN/PNP physics, current amplification factors ($\alpha, \beta$), active, saturation, and cutoff regions. |
| **Lec 9** | **BJT Circuit Configurations** | Common-Emitter (CE), Common-Base (CB), and Common-Collector (CC / Emitter Follower). |
| **Lec 10** | **BJT DC Biasing & Load Lines** | Fixed bias, collector-to-base bias, voltage divider bias, and Q-point stability factors. |
| **Lec 11** | **Junction Field Effect Transistors (JFET)** | Voltage-controlled operation, drain characteristics, pinch-off voltage $V_P$, transconductance $g_m$. |
| **Lec 12** | **MOSFETs (Enhancement & Depletion)** | Channel formation, threshold voltage $V_{th}$, high-power MOSFET switches, CMOS overview. |
| **Lec 13** | **Operational Amplifiers (Op-Amps) Theory** | Ideal vs practical Op-Amps, open-loop gain $A_{OL}$, infinite input impedance, CMRR, slew rate. |
| **Lec 14** | **Basic Op-Amp Circuits & Applications** | Inverting/non-inverting amps, voltage followers, summing amps, difference amplifiers, comparators. |
| **Lec 15** | **Digital Electronics & Transducers** | Digital logic basics, ADC/DAC conversion principles, transducers, and DAQ architecture in Agriculture 4.0. |

---

## 🗂️ Materials in this Directory

* **Lecture Compendia (`.pdf`)**: 15 complete academic compendia typeset in $\LaTeX$ (`AGE214Lecture1CompendiumFixed.tex.pdf` through `AGE214Lecture15CompendiumFixed.tex.pdf`).
* **Lecture Presentations (`.pptx`)**: 15 slide decks covering each individual lecture module.
