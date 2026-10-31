# 🧠 AGE 316: Microcomputer Systems
### Sokoine University of Agriculture (SUA) | Department of Agricultural Engineering

[![Course Level](https://img.shields.io/badge/Level-Undergraduate%20(Year%203)-blue.svg)](#)
[![Target Programs](https://img.shields.io/badge/Core%20Programs-BSc%20AE%20(Year%203)%20%7C%20BSc%20BPHE%20(Year%203)-forestgreen.svg)](#target-audience--degree-program-competencies)
[![Platform](https://img.shields.io/badge/Firmware-Embedded%20C%20%7C%20Arduino-teal.svg)](#)

---

## 📖 Course Overview

**AGE 316: Microcomputer Systems** is a core third-year embedded systems course offered by the Department of Agricultural Engineering at Sokoine University of Agriculture. Instructed by **Dr. Kadeghe Fue**, the course demystifies the "brains" of modern agricultural automation: embedded microprocessors and microcontrollers.

Students learn the internal architecture of microcomputers (CPU registers, ALU, bus structures, Harvard vs. Von Neumann architectures, memory hierarchy), hardware peripheral management (timers, counters, interrupts, ADCs), serial communication protocols (UART, SPI, I2C), and practical firmware engineering using embedded C / Arduino for agricultural machinery and food bioprocess controllers.

---

## 🎯 Target Audience & Degree Program Competencies

AGE 316 is a required professional engineering course specifically designated for two third-year cohorts:

1. **BSc in Agricultural Engineering (BSc AE — 3rd Year)**:
   * **Implement & Machinery ECUs**: Designing microcontroller-based embedded electronic control units (ECUs) to monitor tractor engine RPM, seed drop rates on planters, and implement hitch positions.
   * **Real-Time Interrupts**: Programming hardware interrupts (external INT pins) to read high-speed optical encoders for tractor wheel slip and PTO speed measurements.
   * **Actuator Control**: Driving high-power relays, linear actuators, and hydraulic spool valves using transistor driver circuits and pulse-width modulation (PWM).

2. **BSc in Bioprocess and Post-Harvest Engineering (BSc BPHE — 3rd Year)**:
   * **Dryer Closed-Loop Control**: Developing embedded firmware to read digital temperature/humidity sensors (DHT22, SHT3x) and execute bang-bang or PID control algorithms for grain dryers and curing kilns.
   * **Cold Storage & Silo Automation**: Programming multi-channel data acquisition units to log silo environmental temperatures, activate aeration blowers, and trigger audible/visual warning thresholds.
   * **Sorting & Packaging Conveyors**: Controlling stepper and servo motors for automated conveyor diverter gates and packaging batch scales.

---

## 🗺️ Core Curriculum & Key Topics

* **Microcomputer & Embedded Systems Fundamentals**: Definition, embedded systems vs. general-purpose computers, microcontroller vs. microprocessor trade-offs.
* **CPU & Memory Architecture**: ALU operation, status registers (flags), Program Counter (PC), Stack Pointer (SP), Flash program memory, SRAM, EEPROM.
* **Embedded Firmware Development**: Structure of microcomputer code (`setup()` initialization and `loop()` execution), direct port manipulation, and bitwise operations.
* **Analog-to-Digital Conversion (ADC)**: Quantization error, reference voltage ($V_{ref}$), bit resolution ($10\text{-bit} = 1024$ levels), multi-channel analog multiplexing.
* **Timers, Counters, and Interrupts**: Timer prescalers, hardware timer overflows, and Interrupt Service Routines (ISRs) for deterministic time-critical responses.
* **Serial Communication Buses**: UART baud rates, I2C addressing (master/slave architecture), and SPI high-speed synchronous peripheral transfers.
* **Actuation Drivers**: Relay isolation (flyback diodes, optocouplers), MOSFET power switches, and H-Bridge motor drivers (e.g., L298N).

---

## 🗂️ Materials in this Directory

* **Lecture Presentations & Notes (`.pptx` / `.pdf`)**:
  * Lectures 1 to 15 covering embedded architectures, memory mapping, programming, and interfacing.
* **Continuous Assessment Tests**:
  * `AE 316 Test 1 2024-2025.docx` & `AE 316 Test 1 2024-2025 2.docx`
  * `AE 316 Test 2 2023-2024.docx`
* **Official University Examinations**:
  * [`UNIVERSITY EXAMINATION PAPER AGE 316 2024-2025.docx`](file:///home/kadefue/Course_Notes/AGE%20316/UNIVERSITY%20EXAMINATION%20PAPER%20AGE%20316%202024-2025.docx) (BSc AE 3rd Year & BSc BPHE 3rd Year).
  * [`AGE 316 2023_2024 UE.docx`](file:///home/kadefue/Course_Notes/AGE%20316/AGE%20316%202023_2024%20UE.docx)
* **Assignments & Spreadsheets**:
  * `AGE 316 ASSIGNMENT 1 2024-25.xls` & `ASSIGNMENT 2 2024-25.xls`
  * Continuous grading records: `AGE 316 TEST 1 2024-25.xls`, `TEST 2 2024-25.xls`.
