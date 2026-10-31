# 📡 AGE 310: Instrumentation and Measurements
### Sokoine University of Agriculture (SUA) | Department of Agricultural Engineering

[![Course Level](https://img.shields.io/badge/Level-Undergraduate%20(Year%203)-blue.svg)](#)
[![Programs](https://img.shields.io/badge/Target%20Programs-BSc%20AE%20%7C%20BSc%20IWRE%20%7C%20BSc%20BPHE-forestgreen.svg)](#target-audience--degree-program-competencies)
[![Lab](https://img.shields.io/badge/Lab-Electronics%20%26%20Precision%20Agriculture%20(EPAL)-purple.svg)](#)

---

## 📖 Course Overview

**AGE 310: Instrumentation and Measurements** is a core third-year engineering course offered by the Department of Agricultural Engineering at Sokoine University of Agriculture. Instructed by **Dr. Kadeghe Fue** at the **Electronics and Precision Agriculture Lab (EPAL)**, this course provides comprehensive training on how physical variables in agricultural, hydrological, and biological processes are transduced, conditioned, digitized, transmitted, and controlled.

The curriculum covers the full instrumentation chain—from physical sensor physics and signal conditioning to dynamic system response modeling, feedback control loops, agricultural robotics, unmanned aerial vehicles (UAVs), machine vision, and IoT smart farming architectures.

---

## 🎯 Target Audience & Degree Program Competencies

This course is simultaneously taken by all three undergraduate engineering cohorts, providing specialized competencies for each:

1. **BSc in Agricultural Engineering (BSc AE)**:
   * **Implement Dynamometry**: Measuring draft, vertical, and lateral forces on tractor three-point hitches using strain gauge load cells and Wheatstone bridge circuits.
   * **Mobile Machinery Automation**: Implementing CAN bus (ISO 11783 / ISOBUS) communication protocols between tractors and implements.
   * **Field Robotics & UAVs**: Kinematic modeling of autonomous agricultural mobile robots (Lecture 12) and multispectral drone survey operations (Lecture 13).

2. **BSc in Irrigation and Water Resources Engineering (BSc IWRE)**:
   * **Hydraulic Pressure & Level Transduction**: Applying piezoresistive pressure transmitters to monitor pipeline hydraulics and hydrostatic/ultrasonic level sensors in canals and tanks.
   * **Soil-Water Measurement**: Deploying and calibrating capacitive, frequency domain (FDR), and time-domain (TDR) dielectric soil moisture probes.
   * **Automated Actuation & Telemetry**: Interfacing electric solenoid valves, motorized butterfly valves, and LoRaWAN/MQTT telemetry nodes for wide-area irrigation networks.

3. **BSc in Bioprocess and Post-Harvest Engineering (BSc BPHE)**:
   * **Thermal Dynamic Response**: Modeling first-order sensor lag ($\tau$) of thermocouples and RTDs inside pasteurizers, dryers, and fermentation vessels (Lecture 10).
   * **Optical Sorting & Machine Vision (Lec 14)**: Building machine vision inspection systems using digital cameras and image processing (thresholding, segmentation) to grade produce and reject defective grains.
   * **Continuous Mass Measurement**: Calibrating load cells for grain hopper scales, packaging lines, and continuous conveyor weighing.

---

## 🗺️ Syllabus & Lecture Breakdown

| Lecture | Topic | Detailed Engineering Content |
| :--- | :--- | :--- |
| **Lecture 1** | **Introduction & Generalized Measurement Chain** | Sensor, signal conditioning, ADC, processing, and display stages; Active vs passive sensors. |
| **Lecture 2** | **Measurement Standards, Errors & Calibration** | Systematic vs random errors, Gaussian distribution, uncertainty propagation, primary/secondary standards. |
| **Lecture 3** | **Resistive Transducers** | Strain gauges, gauge factor, quarter/half/full Wheatstone bridges, RTDs (Pt100), and thermistors. |
| **Lecture 4** | **Capacitive & Inductive Transducers** | Parallel-plate capacitive moisture sensors, inductive proximity switches, and LVDTs. |
| **Lecture 5** | **Piezoelectric & Photoelectric Transducers** | Piezoelectric impact sensors (grain loss), photodiodes, phototransistors, and pyranometers. |
| **Lecture 6** | **Signal Conditioning Circuits** | Instrumentation amplifiers (IN-AMPs), high CMRR, active Butterworth filters, ADC quantization. |
| **Lecture 7** | **Actuators & Final Control Elements** | Solenoid valves, stepper motors, servomotors, DC motors, pneumatic cylinders, and driver circuits. |
| **Lecture 8** | **Digital Logic & Microcontrollers** | Logic gates, Boolean algebra, MCU peripherals, timers, and digital I/O in instrumentation. |
| **Lecture 9** | **Data Communication Protocols** | UART serial, SPI, I2C, RS-485 Modbus, and tractor-implement CAN bus (ISOBUS). |
| **Lecture 10**| **Dynamic Characteristics of Instruments** | Zero-order, 1st-order (time constant $\tau$), and 2nd-order (damping $\zeta$, natural frequency $\omega_n$) response. |
| **Lecture 11**| **Introduction to Control Systems** | Open-loop vs closed-loop feedback, block diagrams, transfer functions, and PID controller tuning. |
| **Lecture 12**| **Agricultural Robotics** | Mobile robot kinematics, steering geometries (Ackermann, differential), navigation, robotic harvesters. |
| **Lecture 13**| **Agricultural Drones (UAVs)** | Fixed-wing vs multirotor flight mechanics, multispectral payloads, flight mission planning, spray drones. |
| **Lecture 14**| **Machine Vision in Agriculture** | Image acquisition, illumination, RGB/HSV color spaces, thresholding, edge detection, automated grading. |
| **Lecture 15**| **IoT and Smart Farming** | End-to-end IoT architectures, sensor nodes, edge gateways, LoRaWAN, MQTT broker, cloud dashboards. |

---

## 🗂️ Materials in this Directory

* **Lecture Compendia (`.pdf`)**: Complete set of 15 academic compendia authored by Dr. Kadeghe Fue (`AGE 310 Compendium - Lecture 1.pdf` through `Lecture 15IoT and Smart Farming.pdf`).
* **Lecture Presentations (`.pptx`)**: 15 slide decks covering all lecture modules.
* **Assignments & Data**:
  * `AGE 310_ASS_1.xlsx`: Quantitative sensor calibration and instrumentation calculation assignments.
* **University Examinations**:
  * `AGE 310_UE 2025_FUE_23 FEB 2026.doc`: Official University Final Examination paper covering BSc AE, BSc IWRE, and BSc BPHE cohorts.

---

## 👨‍🏫 Laboratory Leadership & Teaching Staff

* **Teaching Laboratory**: **Electronics and Precision Agriculture Lab (EPAL)** ([**www.epalab.org**](https://www.epalab.org))
* **Principal Investigator (PI) & Lead Instructor**: **Dr. Kadeghe Goodluck Fue**, PhD, P.Eng (T)
  * *Email*: `kadeghe.fue@sua.ac.tz` | *Website*: [**www.kadefue.com**](https://www.kadefue.com)
* **Laboratory Technician**: **Mr. Patrick Mathias**
* **Department**: Department of Agricultural Engineering (DAE), Sokoine University of Agriculture

### 👨‍🔬 About the Instructor
**Dr. Kadeghe Goodluck Fue** is a Senior Lecturer of Mechatronics, AI, and Precision Agriculture at SUA and a Registered Professional Engineer (PE11382). He holds a Ph.D. in Engineering (AI and Robotics) from the University of Georgia, USA, an M.Sc. in Agricultural & Biological Engineering from the University of Florida, USA, and a B.Sc. in Computer Engineering & IT from the University of Dar es Salaam. With 15+ years in instrumentation, autonomous systems, and sensor fusion, Dr. Fue leads research projects funded by USAID and the US National Academies. Students are encouraged to visit [**www.kadefue.com**](https://www.kadefue.com) and [**www.epalab.org**](https://www.epalab.org) to explore ongoing instrumentation and drone research.

### 🚀 Student Innovations & Entrepreneurship
AGE 310 concepts—machine vision, environmental sensors, strain load cells, and IoT telemetry—are the technical foundation for prominent student startups fostered in EPAL and the YEESI Lab ([**yeesi.epalab.org**](https://yeesi.epalab.org)):
* **AGROSCAN Company Ltd** (mechanization telemetry and equipment rental platform **FARMHIRE**, driven by EPAL student innovators including Stephano Mashauri and Dickson Massawe)
* **Afya ya Mnyama** (IoT sensor tags monitoring animal vitals using dynamic temperature and biometric sensors)
* **AgriMfumo Ltd** (automated irrigation telemetry and smart sensor interfaces)

Students are encouraged to utilize EPAL's testing benches and fabrication tools to design market-ready instrumentation products!
