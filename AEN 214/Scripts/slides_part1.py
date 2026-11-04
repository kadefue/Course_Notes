#!/usr/bin/env python3
"""
slides_part1.py
Slide content definitions for Lectures 1, 2, and 3 (26 slides each).
"""

from pptx import Presentation
from pptx.util import Inches
from build_slides import (
    add_title_slide, add_bullet_slide, add_example_slide,
    add_case_study_slide, add_lab_slide, add_summary_slide, add_review_slide
)

def build_lecture_1_deck(prs):
    lec_num = 1
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Passive Electronic Components",
                    "Resistors, Capacitors, Inductors & AC Reactance in Agricultural Instrumentation", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 1 Learning Outcomes & Session Roadmap", [
        "Decode Resistor Specifications: Read 4-band and 5-band color codes, EIA-96 SMD markings, tolerances, and power ratings.",
        "Evaluate Specialized Transducers: Understand thermistors (NTC/PTC), LDRs, strain gauges, and varistors in agricultural sensing.",
        "Analyze Capacitive Energy Storage: Calculate capacitance, electric fields, dielectric breakdown, and electrolytic polarity.",
        "Model RC Transient Dynamics: Solve differential charging and discharging equations and determine time constant tau = RC.",
        "Understand Electromagnetic Induction: Apply Faraday's and Lenz's laws to inductors, chokes, and energy storage.",
        "Prevent Inductive Transients: Mitigate relay/solenoid inductive kickback using freewheeling flyback diodes.",
        "Calculate AC Reactance & Resonance: Determine X_C, X_L, cutoff frequencies, and resonant LC tank parameters."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "Passive Components in Tanzanian AgriTech Systems", [
        "Foundational Hardware Layer: Every tractor ECU, solar inverter, and automated greenhouse relies on passive components.",
        "Extreme Agro-Climatic Stress: In Morogoro, Dodoma, and Arusha, components face ambient heat (45°C), high humidity, and red dust.",
        "Sensor Interfacing: Passive resistor dividers convert high-impedance soil moisture and temperature signals for microcontrollers.",
        "Power Quality Filtering: Heavy irrigation pumps and diesel generators induce voltage sags and spikes that require LC filter stages.",
        "Economic Reliability: Selecting inadequate resistor power ratings or low-voltage capacitors causes catastrophic farm equipment fires."
    ], image_file="img_resistors_assorted.jpg", current_slide=3, total_slides=total)

    # 4. Resistors: Fundamental Physics
    add_bullet_slide(prs, "Resistor Fundamentals: Conduction & Ohm's Law", [
        "Governing Equation: Ohm's Law states V = I · R; Electric current is directly proportional to applied voltage.",
        "Physical Resistance Equation: R = rho · (L / A), where rho is resistivity (Ohm-m), L is conductor length, and A is cross-sectional area.",
        "Temperature Dependence: R(T) = R_0 [1 + alpha · (T - T_0)], where alpha is the Temperature Coefficient of Resistance (TCR).",
        "Conductor Materials: Copper has low resistivity (1.68 x 10^-8 Ohm-m); Nichrome alloy provides high resistance for heating elements.",
        "Power Dissipation: Electrical energy is converted to heat via Joule heating: P = I² · R = V² / R = V · I (Watts)."
    ], current_slide=4, total_slides=total)

    # 5. Resistor Construction & Classification
    add_bullet_slide(prs, "Resistor Types & Physical Construction", [
        "Carbon Film Resistors: General purpose, economical, moderate stability (±5% tolerance), suited for basic breadboarding.",
        "Metal Film Resistors: Nichrome deposited on ceramic rods; low noise, high precision (±0.1% to ±1%), essential for analog sensors.",
        "Wirewound Resistors: Manganin/Constantan wire wound on ceramic cores; high power (5W to 100W+), used in motor braking and heaters.",
        "Surface Mount Devices (SMD): Compact ceramic chip resistors (0805, 0603 packages) mounted in automated tractor GPS boards.",
        "High-Frequency Derating: Parasitic lead inductance (L_lead) and shunt capacitance (C_shunt) degrade high-frequency performance."
    ], image_file="fig1_1_resistor_color_code.png", current_slide=5, total_slides=total)

    # 6. Color Code & Markings
    add_bullet_slide(prs, "Standard Resistor Color Coding & Numerical Codes", [
        "Standard 4-Band System: Band 1 (1st digit), Band 2 (2nd digit), Band 3 (Multiplier 10^n), Band 4 (Tolerance %: Gold=±5%, Silver=±10%).",
        "Precision 5-Band System: Bands 1, 2, 3 (Significant digits), Band 4 (Multiplier), Band 5 (Tolerance: Brown=±1%, Red=±2%).",
        "Mnemonic Memory Aid: Bad Boys Ring Our Young Girls But Violet Gives Willingly (Black, Brown, Red, Orange, Yellow, Green, Blue, Violet, Gray, White).",
        "SMD 3-Digit Code: '472' = 47 x 10² Ohm = 4.7 kOhm; '104' = 10 x 10⁴ Ohm = 100 kOhm; 'R' denotes decimal point: '4R7' = 4.7 Ohm.",
        "EIA-96 High-Precision System: Two-digit lookup code followed by an alphabetic multiplier letter (e.g. 01C = 10 kOhm ±1%)."
    ], current_slide=6, total_slides=total)

    # 7. Thermal Ratings & Derating
    add_bullet_slide(prs, "Power Ratings & Agricultural Thermal Derating", [
        "Standard Package Ratings: Through-hole resistors are rated at 0.125W (1/8W), 0.25W (1/4W), 0.5W (1/2W), 1.0W, 2.0W, and 5.0W+.",
        "Maximum Surface Temperature: Resistors reach 125°C to 155°C at full rated power; ambient air must carry away dissipated heat.",
        "Field Derating Rule: In tropical African agricultural environments (ambient > 40°C), derate rated power by 50% (P_safe <= 0.50 · P_rated).",
        "Component Spacing: Mount power resistors at least 5 mm above PCB substrate to avoid scorching fiberglass and adjacent traces.",
        "Flammability: Use flame-proof metal oxide resistors in poultry brooders to prevent fire ignition from accumulated flammable feathers."
    ], current_slide=7, total_slides=total)

    # 8. Special Purpose Resistors
    add_bullet_slide(prs, "Special Purpose Resistors in Agricultural Automation", [
        "Negative Temperature Coefficient (NTC) Thermistors: Resistance drops non-linearly as temperature increases; monitors grain silos.",
        "Positive Temperature Coefficient (PTC) Thermistors: Self-resetting polymeric overcurrent fuses protecting DC pump motors.",
        "Light Dependent Resistors (LDRs): Cadmium Sulfide (CdS) photoconductive cells; resistance drops from 1 MOhm (dark) to 500 Ohm (sun).",
        "Piezoresistive Strain Gauges: Foil resistors that change value under strain (Delta R / R = G · epsilon); weigh livestock on dairy platforms.",
        "Metal Oxide Varistors (MOVs): Non-linear voltage-clamping zinc-oxide ceramic discs that suppress lightning surges on farm mains."
    ], current_slide=8, total_slides=total)

    # 9. Capacitors: Electrostatics & Dielectrics
    add_bullet_slide(prs, "Capacitors: Electrostatic Principles & Dielectrics", [
        "Physical Structure: Two parallel conducting plates separated by an insulating dielectric medium.",
        "Capacitance Equation: C = (epsilon_r · epsilon_0 · A) / d, where epsilon_0 = 8.854 x 10^-12 F/m, and epsilon_r is relative permittivity.",
        "Charge-Voltage Law: Q = C · V; Charge stored Q (Coulombs) is proportional to terminal potential difference V (Volts).",
        "Electrostatic Energy: W = 0.5 · C · V² = 0.5 · (Q² / C); Stored in the polarized electric field of the dielectric.",
        "Dielectric Breakdown: Exceeding breakdown field strength (E_max = V_max / d) causes dielectric punch-through and short-circuit failure."
    ], image_file="img_capacitors_types.jpg", current_slide=9, total_slides=total)

    # 10. Capacitor Types & Parasitics
    add_bullet_slide(prs, "Capacitor Technologies & Non-Ideal Parasitics", [
        "Ceramic Capacitors (Class 1 NP0/C0G): Extremely stable, ultra-low loss, zero DC bias effect; ideal for RF and precision timing.",
        "Ceramic Capacitors (Class 2 X7R, Y5V): High capacitance per volume; used for DC power rail decoupling near microcontrollers.",
        "Aluminum Electrolytic Capacitors: Liquid/gel electrolyte with thin Al2O3 oxide film; polarized; high capacitance for power smoothing.",
        "Film Capacitors (Polypropylene/Polyester): Low ESR and high AC ripple current capability; used across AC induction motor run windings.",
        "Equivalent Series Resistance (ESR): Internal ohmic loss; causes heating during high-frequency ripple currents in solar MPPT inverters."
    ], current_slide=10, total_slides=total)

    # 11. RC Transient Response
    add_bullet_slide(prs, "RC Circuit Transient Analysis & Time Constant", [
        "First-Order Differential Model: Kirchhoff's Loop Law: V_s = i(t) · R + v_C(t) = R · C · (dv_C / dt) + v_C(t).",
        "Charging Characteristic: v_C(t) = V_s · [1 - exp(-t / tau)], where time constant tau = R · C (seconds).",
        "Discharging Characteristic: v_C(t) = V_0 · exp(-t / tau), discharging stored energy into load resistor R.",
        "Transient Benchmarks: At t = 1 tau, capacitor reaches 63.2% of final voltage; at t = 5 tau, capacitor reaches 99.3% (steady state).",
        "Hardware Timer Applications: RC timing networks define delay intervals in irrigation solenoid pulsers and watchdog reset circuits."
    ], image_file="fig1_2_rc_transient.png", current_slide=11, total_slides=total)

    # 12. Worked Example 1
    add_example_slide(prs, 1, "Resistor Color Decoding & Thermal Derating",
                      "A precision sensor conditioning circuit for a soil moisture probe uses a 5-band resistor with bands: Orange (3), White (9), Black (0), Brown (x10), Brown (±1%). In continuous operation at Morogoro (ambient 42°C), it drops 15.0V. Calculate: (a) Nominal resistance and tolerance, (b) Power dissipated, (c) Minimum manufacturer wattage rating with a 50% safety factor.",
                      [
                          "1. Decode Bands: Band 1=3, Band 2=9, Band 3=0 -> Digits '390'. Band 4 is multiplier: x10^1 = x10. Nominal R = 390 x 10 = 3,900 Ohm (3.9 kOhm).",
                          "2. Tolerance: Band 5 is Brown -> ±1% tolerance. Range = 3,900 ± 39 Ohm (3,861 Ohm to 3,939 Ohm).",
                          "3. Calculate Operating Power: P = V² / R = (15.0 V)² / 3,900 Ohm = 225 / 3,900 = 0.0577 W (57.7 mW).",
                          "4. Apply Field Derating Factor: Required Rating P_rated >= P_operating / 0.50 = 0.0577 W / 0.50 = 0.1154 W.",
                          "5. Commercial Selection: Standard 0.25 W (1/4 W) metal-film resistor provides generous safety margin and long-term stability."
                      ], current_slide=12, total_slides=total)

    # 13. Worked Example 2
    add_example_slide(prs, 2, "RC Charging Transient in Drip Irrigation Controller",
                      "An automated drip irrigation pulse timer at Kilombero Sugar nursery uses an RC charging circuit with R = 470 kOhm and electrolytic capacitor C = 100 microFarad powered from a regulated V_s = 12.0 V solar battery rail. The Schmitt-trigger timer fires when v_C reaches 8.0 V. Determine: (a) Time constant tau, (b) Time delay t_fire to reach 8.0 V, (c) Energy stored in the capacitor at trigger.",
                      [
                          "1. Time Constant Calculation: tau = R · C = (470 x 10^3 Ohm) · (100 x 10^-6 F) = 47.0 seconds.",
                          "2. Formulate Transient Equation: v_C(t) = V_s · [1 - exp(-t / tau)] -> 8.0 V = 12.0 V · [1 - exp(-t / 47.0)].",
                          "3. Solve for Exponential Term: 1 - exp(-t / 47.0) = 8.0 / 12.0 = 0.6667 -> exp(-t / 47.0) = 0.3333.",
                          "4. Invert via Natural Logarithm: -t / 47.0 = ln(0.3333) = -1.0986 -> t_fire = 47.0 · 1.0986 = 51.63 seconds.",
                          "5. Stored Electrostatic Energy: W = 0.5 · C · V² = 0.5 · (100 x 10^-6 F) · (8.0 V)² = 0.5 · 10^-4 · 64 = 3.20 mJ."
                      ], current_slide=13, total_slides=total)

    # 14. Inductors: Electromagnetism & Cores
    add_bullet_slide(prs, "Inductors: Magnetic Physics & Faraday's Law", [
        "Self-Inductance Equation: L = (mu_r · mu_0 · N² · A) / l, where N is turn count, A is core area, and l is magnetic path length.",
        "Faraday-Lenz Law: Terminal induced EMF opposes rate of change of current: v_L(t) = L · (di / dt).",
        "Magnetic Energy Storage: Stored magnetic field energy W = 0.5 · L · I² (Joules).",
        "Core Types: Air core (zero saturation, low inductance), Ferrite core (high frequency, switch-mode power), Laminated iron (50 Hz mains).",
        "Current Continuity Rule: Current through an inductor cannot change instantaneously (Delta I / Delta t < infinity)."
    ], image_file="img_inductors_toroid.jpg", current_slide=14, total_slides=total)

    # 15. Inductive Kickback & Flyback Protection
    add_bullet_slide(prs, "The Inductive Kickback Hazard in Farm Actuators", [
        "The Kickback Phenomenon: Abruptly opening a switch driving a relay, hydraulic valve, or solenoid forces di/dt to large negative values.",
        "Transient Voltage Spike: v_spike = -L · (di/dt) can generate reverse surges of 200V to 1,500V across open contacts or switching transistors.",
        "Component Destruction: Causes dielectric arcing across relay contacts, transistor collector punch-through, and microchip latchup.",
        "Flyback Diode Clamping: Connect a fast rectifier diode (e.g. 1N4007 or UF4007) in anti-parallel across the inductive solenoid coil.",
        "Conduction Mechanism: When the switch opens, coil current circulates safely through the forward-biased flyback diode until dissipated."
    ], current_slide=15, total_slides=total)

    # 16. AC Reactance & Impedance
    add_bullet_slide(prs, "Capacitive & Inductive Reactance in AC Circuits", [
        "Capacitive Reactance: X_C = 1 / (2 · pi · f · C) (Ohms); Inversely proportional to frequency (blocks DC, passes AC high frequencies).",
        "Inductive Reactance: X_L = 2 · pi · f · L (Ohms); Directly proportional to frequency (passes DC, blocks high-frequency electrical noise).",
        "Phase Relationships: In a pure capacitor, current leads voltage by 90° ('ICE'); in an inductor, voltage leads current by 90° ('ELI').",
        "Complex Impedance: Z_total = R + j(X_L - X_C); Magnitude |Z| = sqrt[ R² + (X_L - X_C)² ], Phase theta = arctan[(X_L - X_C) / R].",
        "Series Resonance Condition: When X_L = X_C, reactance cancels, impedance drops to pure resistance R, and current reaches maximum."
    ], image_file="fig1_3_reactance_curves.png", current_slide=16, total_slides=total)

    # 17. Passive Filters for Agricultural Transducers
    add_bullet_slide(prs, "Passive RC & LC Filter Topologies for Agro-Sensors", [
        "Low-Pass RC Filter: Series resistor R and shunt capacitor C; Cutoff frequency f_c = 1 / (2 · pi · R · C).",
        "Agricultural Noise Suppression: Low-pass filters strip 50 Hz power hum and alternator hash from analog pH and moisture probes.",
        "High-Pass RC Filter: Series capacitor C and shunt resistor R; blocks DC drift while passing fast transient acoustic emission pulses.",
        "LC Band-Pass Tank: Combines parallel inductor and capacitor; tunes to specific carrier frequencies in livestock RFID telemetry.",
        "Insertion Loss & Roll-off: Single-stage passive RC filter attenuates at -20 dB/decade (-6 dB/octave) above corner frequency f_c."
    ], image_file="fig1_4_passive_filter_schematic.png", current_slide=17, total_slides=total)

    # 18. Worked Example 3
    add_example_slide(prs, 3, "LC Tank Resonance for Livestock RFID Tag",
                      "An automated cattle gate RFID transceiver operating under ISO 11784/11785 standards requires an LC resonant tank tuned precisely to carrier frequency f_0 = 134.2 kHz. The antenna coil has an inductance L = 470 microHenry. Calculate: (a) Tuning capacitance C required, (b) Inductive reactance X_L at resonance, (c) Tank quality factor Q if coil series resistance R = 4.2 Ohm.",
                      [
                          "1. Resonance Formula: f_0 = 1 / [2 · pi · sqrt(L · C)] -> sqrt(L · C) = 1 / [2 · pi · f_0].",
                          "2. Square Both Sides: L · C = 1 / [4 · pi² · f_0²] -> C = 1 / [4 · pi² · f_0² · L].",
                          "3. Substitute Parameters: f_0 = 134,200 Hz; L = 470 x 10^-6 H. Calculate: 4 · pi² · (134,200)² = 7.108 x 10^11 s^-2.",
                          "   Denom = 7.108 x 10^11 · 470 x 10^-6 = 3.341 x 10^8 -> C = 1 / 3.341 x 10^8 = 2.993 x 10^-9 F = 2.99 nF (use 3.0 nF).",
                          "4. Reactance at Resonance: X_L = 2 · pi · (134,200 Hz) · (470 x 10^-6 H) = 396.3 Ohm.",
                          "5. Quality Factor Calculation: Q = X_L / R = 396.3 Ohm / 4.2 Ohm = 94.36 (High Q provides excellent RFID reading distance)."
                      ], current_slide=18, total_slides=total)

    # 19. Practical Agro-Environment Protection
    add_bullet_slide(prs, "Environmental Protection for Farm Passive Components", [
        "Tropical Humidity & Condensation: Moisture creates ionic leakage paths between high-impedance resistor traces; conformal coating required.",
        "Corrosive Fertilizer & Ammonia Gas: In poultry houses and pig barns, sulfur and ammonia corrode copper leads; use hermetic seals.",
        "Tractor Chassis Mechanical Shock: Engine vibration fractures brittle ceramic chip capacitors; specify automotive AEC-Q200 components.",
        "Thermal Expansion Stress: Solar sensor junction boxes cycle from 15°C (night) to 65°C (noon); differential expansion causes solder cracking.",
        "Lightning & Mains Surges: Rural Tanzanian distribution grids experience frequent inductive spikes; MOV and gas discharge tubes are mandatory."
    ], current_slide=19, total_slides=total)

    # 20. Case Study 1
    add_case_study_slide(prs, 1, "Flyback Clamping in Sugarcane Solenoid Valve Bank",
                         "Kilombero Sugar Company, Morogoro Region, Tanzania",
                         "A multi-zone hydraulic valve manifold controlling automatic sugarcane cutter height experienced recurrent MOSFET switch failures. Every 3 days, a driver transistor failed short-circuit, dumping hydraulic fluid and idling cane harvesters during peak harvesting campaign.",
                         "SUA agricultural engineers inspected the failed driver PCB and discovered that the 24V, 1.8A hydraulic solenoids lacked flyback diode protection. Oscilloscope monitoring captured negative inductive kickback voltage spikes exceeding -480V at valve de-energization, puncturing transistor junctions. Fast-recovery BYV26E avalanche diodes were installed directly across each solenoid coil terminal with anti-vibration potting.",
                         [
                             "Eliminated 100% of driver transistor electrical failures across the entire milling season.",
                             "Saved an estimated 14,000 USD in downtime and replacement electronics.",
                             "Valve de-activation response stabilized within 12 ms without hydraulic hammer."
                         ], current_slide=20, total_slides=total)

    # 21. Case Study 2
    add_case_study_slide(prs, 2, "Passive RC Filtering for Paddy Soil Salinity Sensor",
                         "Mbarali Rice Irrigation Scheme, Mbeya Region, Tanzania",
                         "Precision agricultural sensors measuring soil electrical conductivity (EC) in flooded paddy fields produced erratic telemetry readings. High 50 Hz powerline hum and switching noise from adjacent 45 kW electric pumping stations coupled into the long buried transducer cables, causing false salinity alarms.",
                         "Engineers designed a balanced 2nd-order passive RC low-pass filter with corner frequency f_c = 15 Hz (R = 10 kOhm, C = 1 microFarad polypropylene film capacitor). A high-impedance buffer shielded the sensor from capacitive loading. The passive filter attenuated high-frequency generator interference by 42 dB while preserving valid agricultural soil dynamics.",
                         [
                             "Measurement noise reduced from ±18.4% down to ±0.8% of full-scale reading.",
                             "Enabled reliable automated variable-rate flush irrigation in saline paddy plots.",
                             "100% passive design operating maintenance-free without external battery draw."
                         ], current_slide=21, total_slides=total)

    # 22. Laboratory Bench Protocol
    add_lab_slide(prs, "Bench Prototyping & Diagnostic Protocol for Passives", [
        "Master resistance measurement using 4-wire Kelvin probes and decode unknown color-band resistors.",
        "Capture capacitor charge/discharge exponential curves on digital storage oscilloscope (DSO).",
        "Verify RC time constant tau and measure AC filter cutoff frequency (-3 dB point).",
        "Observe inductive kickback pulse and verify flyback diode voltage clamping."
    ], [
        "Step 1: Inspect 10 assorted resistors; record nominal color code value, tolerance, and measured DMM resistance.",
        "Step 2: Assemble RC circuit (R = 100 kOhm, C = 47 microFarad) on breadboard. Connect DSO Channel 1 across capacitor.",
        "Step 3: Apply 10V step input; trigger DSO; measure 10% to 90% rise time and verify empirical tau against tau = R · C.",
        "Step 4: Connect 12V relay coil to bench DC supply through manual pushbutton switch. Probe coil voltage with 10x DSO probe.",
        "Step 5: Release pushbutton; capture inductive kickback spike amplitude (> 200V). Solder 1N4007 diode; repeat and observe clamped 0.7V drop."
    ], current_slide=22, total_slides=total)

    # 23. Troubleshooting & Pitfalls
    add_bullet_slide(prs, "Diagnostic Troubleshooting & Common Component Failures", [
        "Open-Circuit Resistor: Overheated carbon resistors drift high in value or fail open; visual blistering or black discoloration.",
        "Electrolytic Capacitor Degradation: Electrolyte dries out in hot climates, causing capacitance drop and soaring ESR (causes hum).",
        "Reversed Electrolytic Polarity: Reverse DC voltage generates internal hydrogen gas; catastrophic casing rupture and safety vent blowout.",
        "Shorted Ceramic Capacitor: Mechanical bending stress cracks multilayer ceramic capacitors (MLCC), creating low-resistance shorts.",
        "Inductor Core Saturation: Excessive DC bias current pushes ferrite core into saturation; inductance collapses, causing overcurrent."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "A 4-band resistor has bands Yellow, Violet, Orange, Gold. What is its nominal resistance and acceptable manufacturing range?",
        "Why must an electrolytic capacitor never be connected with reverse polarity in an agricultural DC power supply?",
        "Derive the formula for time constant tau of a series RC circuit and prove that at t = tau, the capacitor charges to 63.2%.",
        "Explain the physical origin of inductive kickback in a solenoid valve and draw the schematic of a flyback protection diode.",
        "Calculate the cutoff frequency of a passive low-pass RC filter with R = 3.3 kOhm and C = 0.1 microFarad."
    ], "Lecture 2 will explore Semiconductor Physics: Bohr's atomic model, silicon energy bands, intrinsic vs extrinsic doping, and PN junction kinetics.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "Passive components (R, L, C) form the bedrock of all analog and digital agricultural electronic systems.",
        "Resistor power ratings must be derated by 50% in tropical Tanzanian operating environments.",
        "Capacitor charge/discharge dynamics follow first-order exponential curves defined by tau = R · C.",
        "Inductive kickback poses severe hazards to semiconductor switches and requires mandatory flyback diodes.",
        "AC reactance is frequency-dependent: Capacitors block DC (X_C -> inf), while inductors block high frequencies (X_L = 2*pi*f*L)."
    ], [
        "Ohm's Law: V = I · R; Power: P = I²R = V²/R",
        "Physical Resistance: R = rho · (L / A)",
        "Capacitance: C = (eps_r · eps_0 · A) / d; Q = C · V",
        "RC Charging: v_C(t) = V_s · [1 - exp(-t / RC)]",
        "Inductor Voltage: v_L(t) = L · (di / dt); W = 0.5 · L · I²",
        "Reactance: X_C = 1 / (2*pi*f*C); X_L = 2*pi*f*L",
        "Resonant Frequency: f_0 = 1 / [2*pi*sqrt(L*C)]"
    ], current_slide=25, total_slides=total)

    # 26. References & Preview
    add_bullet_slide(prs, "Prescribed References & Practical Laboratory Preparation", [
        "Boylestad, R. L., & Nashelsky, L. (2018). Electronic Devices and Circuit Theory (11th ed.). Pearson Education.",
        "Sedra, A. S., & Smith, K. C. (2020). Microelectronic Circuits (8th ed.). Oxford University Press.",
        "Floyd, T. L. (2017). Electronic Devices: Conventional Current Version (10th ed.). Pearson.",
        "Laboratory Preparation: Bring digital multimeter, safety goggles, breadboard, and scientific calculator to Lab Session 1.",
        "Field Assignment: Complete Assignment 1, Questions 1 to 4 covering passive components and submit via SUA LMS."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

def build_lecture_2_deck(prs):
    lec_num = 2
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Semiconductor Physics",
                    "Band Theory, Carrier Transport, PN Junctions & Hall Effect Transducers", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 2 Learning Outcomes & Theoretical Scope", [
        "Master Atomic Physics of Silicon: Analyze Bohr model, tetrahedral covalent lattice, and energy levels.",
        "Differentiate Solid-State Bands: Evaluate Valence Band, Conduction Band, and forbidden energy gap E_g.",
        "Distinguish Insulators, Semiconductors, Conductors: Quantify resistivity and thermal bandgap excitation.",
        "Understand Extrinsic Doping: Contrast N-type donor doping (Group V) and P-type acceptor doping (Group III).",
        "Formulate Carrier Kinetics: Apply Law of Mass Action (n·p = n_i²) and calculate total electrical conductivity.",
        "Analyze PN Junction Depletion Dynamics: Model space-charge formation, diffusion current, and barrier voltage V_0.",
        "Apply the Hall Effect: Design non-contact magnetic speed sensors for tractor wheels and combine harvester shafts."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "Solid-State Semiconductors in Modern Agriculture", [
        "Transition from Mechanical to Electronic: Solid-state physics powers all agricultural transducers, ECUs, and solar converters.",
        "Harsh Agro-Climatic Reality: Silicon chips in tractors operate from morning chill (15°C) to engine block heat (> 90°C).",
        "Intrinsic Carrier Runaway: Thermal carrier generation at elevated temperatures threatens sensor accuracy and bias stability.",
        "Tough Soil-Engaging Sensors: Hall effect magnetic sensors detect shaft rotation through mud, dust, and slurry where optics fail.",
        "Solar Photovoltaic Generation: The PN junction is the fundamental physical building block converting Tanzanian sunlight into pumping power."
    ], image_file="fig2_1_bohr_atom_silicon.png", current_slide=3, total_slides=total)

    # 4. Silicon Atomic Structure & Covalent Lattice
    add_bullet_slide(prs, "The Silicon Atom & Covalent Crystal Lattice", [
        "Atomic Structure: Silicon (Si, atomic number Z = 14); Electron configuration 1s² 2s² 2p⁶ 3s² 3p².",
        "Valence Shell: Four electrons in the outermost n=3 shell dictate semiconductor chemical and electrical properties.",
        "Diamond Cubic Crystal: In crystalline silicon, each atom forms four shared covalent bonds with adjacent silicon atoms.",
        "Thermal Equilibrium at 0 Kelvin: Every valence electron is tightly locked in covalent bonds; silicon behaves as a perfect insulator.",
        "Thermal Lattice Vibrations: At room temperature (T = 300 K), thermal energy breaks bonds, generating free electron-hole pairs."
    ], current_slide=4, total_slides=total)

    # 5. Energy Band Theory in Solids
    add_bullet_slide(prs, "Energy Band Formation in Solid-State Materials", [
        "Pauli Exclusion Principle: When N isolated silicon atoms assemble into a crystal, discrete atomic levels split into continuous bands.",
        "Valence Band (VB): The lower energy band filled with valence bonding electrons at ground state.",
        "Conduction Band (CB): The higher energy band containing quasi-free mobile electrons that conduct electric current.",
        "Forbidden Energy Gap (E_g): The energy difference between the top of the VB (E_V) and the bottom of the CB (E_C).",
        "Electron-Volt (eV): Energy gained by an electron accelerating across 1 Volt potential: 1 eV = 1.602 x 10^-19 Joules."
    ], image_file="fig2_2_energy_bands.png", current_slide=5, total_slides=total)

    # 6. Insulators, Conductors, and Semiconductors
    add_bullet_slide(prs, "Classification of Materials by Bandgap Energy", [
        "Insulators: Wide forbidden gap (E_g > 5 eV, e.g. Diamond, SiO2); thermal energy at 300K cannot excite valence electrons across gap.",
        "Conductors (Metals): Conduction and valence bands overlap (E_g = 0 eV, e.g. Copper, Aluminum); vast sea of free electrons (10^28 m^-3).",
        "Semiconductors: Moderate forbidden gap (E_g ≈ 1.12 eV for Si, 0.67 eV for Ge, 1.42 eV for GaAs); controllable thermal excitation.",
        "Temperature Coefficient of Resistance: Metals possess positive TCR (resistance increases with heat); semiconductors have negative TCR.",
        "Silicon Dominance: Silicon's wider bandgap (1.12 eV vs 0.67 eV Ge) allows higher temperature operation (up to 150°C vs 75°C Ge)."
    ], current_slide=6, total_slides=total)

    # 7. Intrinsic Semiconductors & Hole Dynamics
    add_bullet_slide(prs, "Intrinsic Semiconductors & Carrier Generation", [
        "Intrinsic Semiconductor: Pure, ultra-refined crystal with negligible impurity atoms (< 1 part per billion).",
        "Thermal Generation: Thermal agitation kicks an electron from the VB to the CB, leaving behind a vacant covalent state called a **Hole**.",
        "Hole Dynamics: An adjacent valence electron hops into the vacancy; the hole behaves physically as an effective mobile charge +q.",
        "Intrinsic Carrier Concentration (n_i): In pure silicon at 300 K, n_i = p_i ≈ 1.5 x 10^10 cm^-3 (or 1.5 x 10^16 m^-3).",
        "Temperature Sensitivity: n_i(T) = B · T^(3/2) · exp[-E_g / (2 · k_B · T)]; n_i doubles roughly every 8°C rise in temperature!"
    ], current_slide=7, total_slides=total)

    # 8. Extrinsic Doping: N-Type Semiconductors
    add_bullet_slide(prs, "Extrinsic Doping: N-Type Semiconductor Physics", [
        "Doping Purpose: Introducing controlled impurity atoms to increase electrical conductivity by up to six orders of magnitude.",
        "N-Type Dopants: Group V pentavalent elements (Phosphorus [P], Arsenic [As], Antimony [Sb]).",
        "Conduction Mechanism: Four valence electrons bond with silicon; the fifth electron is weakly bound (ionization energy ≈ 0.045 eV).",
        "Donor Energy Level (E_D): Lies just 0.045 eV below the conduction band edge E_C; virtually all donors ionize at room temperature.",
        "Carrier Densities: Majority carriers are electrons (n ≈ N_D); minority carriers are holes (p = n_i² / N_D). Fixed ions are N_D⁺."
    ], current_slide=8, total_slides=total)

    # 9. Extrinsic Doping: P-Type Semiconductors
    add_bullet_slide(prs, "Extrinsic Doping: P-Type Semiconductor Physics", [
        "P-Type Dopants: Group III trivalent elements (Boron [B], Gallium [Ga], Indium [In]).",
        "Conduction Mechanism: Three valence electrons bond with adjacent silicon atoms, leaving one incomplete bond (a vacant hole).",
        "Acceptor Energy Level (E_A): Lies just 0.045 eV above the valence band edge E_V; captures valence electrons easily.",
        "Thermal Ionization: Valence electrons hop into acceptor levels, creating mobile holes in the valence band and fixed negative ions N_A⁻.",
        "Carrier Densities: Majority carriers are holes (p ≈ N_A); minority carriers are electrons (n = n_i² / N_A)."
    ], current_slide=9, total_slides=total)

    # 10. Law of Mass Action & Conductivity
    add_bullet_slide(prs, "The Law of Mass Action & Electrical Conductivity", [
        "Law of Mass Action: In thermal equilibrium, the product of electron and hole concentrations is constant: n · p = n_i²(T).",
        "Physical Significance: Increasing donor doping N_D increases electron density n and drastically suppresses hole density p.",
        "Drift Conductivity Equation: Total electrical conductivity sigma = q · (n · mu_n + p · mu_p) (Siemens/meter or (Ohm·m)^-1).",
        "Mobility Disparity: Electron mobility mu_n (≈ 1,350 cm²/V·s) is roughly 2.8 times higher than hole mobility mu_p (≈ 480 cm²/V·s).",
        "Resistivity Formulation: Electrical resistivity rho = 1 / sigma = 1 / [ q · (n · mu_n + p · mu_p) ]."
    ], current_slide=10, total_slides=total)

    # 11. Carrier Transport: Drift vs Diffusion
    add_bullet_slide(prs, "Carrier Transport Mechanisms: Drift & Diffusion", [
        "Drift Current: Charge carrier motion driven by an applied electric field E: J_drift = q(n·mu_n + p·mu_p) · E.",
        "Diffusion Current: Charge carrier motion driven by spatial concentration gradients (from high to low density regions).",
        "Fick's Law of Diffusion: J_diff,n = q · D_n · (dn / dx); J_diff,p = -q · D_p · (dp / dx), where D is diffusion coefficient (cm²/s).",
        "Einstein Relation: Connects thermal diffusivity to electrical mobility: D_n / mu_n = D_p / mu_p = V_T = (k_B · T) / q.",
        "Thermal Voltage (V_T): At room temperature T = 300 K, V_T = (1.38 x 10^-23 · 300) / (1.602 x 10^-19) ≈ 25.86 mV (standard 26 mV)."
    ], current_slide=11, total_slides=total)

    # 12. Worked Example 1
    add_example_slide(prs, 1, "Extrinsic Doping & Law of Mass Action in Farm Silicon",
                      "A silicon substrate for an agricultural microcontroller ADC is uniformly doped with Phosphorus donor atoms at N_D = 2.0 x 10^16 cm^-3 at room temperature (T = 300 K, n_i = 1.5 x 10^10 cm^-3). Assume electron mobility mu_n = 1,250 cm²/V·s and hole mobility mu_p = 450 cm²/V·s. Calculate: (a) Majority carrier concentration n, (b) Minority carrier concentration p, (c) Electrical conductivity sigma.",
                      [
                          "1. Majority Carrier Density: Since N_D >> n_i, full donor ionization occurs: n ≈ N_D = 2.0 x 10^16 cm^-3.",
                          "2. Minority Carrier Density via Mass Action: n · p = n_i² -> p = n_i² / n = (1.5 x 10^10)² / (2.0 x 10^16) = (2.25 x 10^20) / (2.0 x 10^16) = 1.125 x 10^4 cm^-3.",
                          "3. Note the Enormous Disparity: Majority electrons outnumber minority holes by a factor of 1.78 x 10^12!",
                          "4. Electrical Conductivity Formulation: sigma = q · (n · mu_n + p · mu_p) ≈ q · n · mu_n (minority holes contribute negligibly).",
                          "5. Calculate: sigma = (1.602 x 10^-19 C) · (2.0 x 10^16 cm^-3) · (1,250 cm²/V·s) = 4.005 (Ohm·cm)^-1 = 400.5 S/m. (Resistivity rho = 1/sigma = 0.25 Ohm·cm)."
                      ], current_slide=12, total_slides=total)

    # 13. The PN Junction: Depletion Layer Physics
    add_bullet_slide(prs, "The PN Junction: Space Charge Depletion Region", [
        "Junction Formation: Joining P-type and N-type silicon creates steep carrier concentration gradients across the metallurgical boundary.",
        "Carrier Diffusion: Free electrons diffuse from N into P; mobile holes diffuse from P into N, recombining at the interface.",
        "Uncompensated Fixed Ions: Electron departure leaves positively charged donor cores (N_D⁺) on the N-side; hole departure leaves N_A⁻ on P-side.",
        "Space Charge Region (Depletion Layer): Region completely depleted of mobile charge carriers; contains only uncompensated bound ions.",
        "Internal Electric Field: Points from positive donor ions (N-side) to negative acceptor ions (P-side), halting further diffusion."
    ], image_file="fig2_3_pn_junction_equilibrium.png", current_slide=13, total_slides=total)

    # 14. Built-in Barrier Potential V0
    add_bullet_slide(prs, "Built-in Barrier Potential V_0 & Energy Bands", [
        "Built-in Potential Equation: V_0 = V_T · ln[ (N_A · N_D) / n_i² ], where V_T = k_B · T / q is the thermal voltage.",
        "Typical Silicon Values: For standard doping levels (10^16 to 10^17 cm^-3), V_0 ranges between 0.65 V and 0.75 V at 300 K.",
        "Energy Band Bending: In equilibrium, Fermi levels (E_F) align flat across the junction; conduction and valence bands bend by q·V_0.",
        "Potential Hill: Electrons in N-side conduction band face an energy barrier of q·V_0 preventing transit into the P-side.",
        "Contact Potential Measurement: V_0 cannot be measured with an ordinary voltmeter because contact potentials at probe leads cancel it."
    ], current_slide=14, total_slides=total)

    # 15. Forward vs Reverse Bias Kinetics
    add_bullet_slide(prs, "Biased PN Junction: Forward & Reverse Regimes", [
        "Forward Bias (V_ext > 0 on P, negative on N): Opposes internal E-field; reduces barrier height from V_0 to (V_0 - V_ext).",
        "Depletion Layer Thinning: Allows massive exponential injection of majority electrons across into P and holes into N.",
        "Reverse Bias (V_ext < 0 on P, positive on N): Aids internal E-field; increases barrier height to (V_0 + |V_R|).",
        "Depletion Layer Widening: Space charge width widens: W_dep proportional to sqrt(V_0 + |V_R|); halts majority diffusion.",
        "Reverse Saturation Current (I_S): Thermally generated minority carriers swept across junction by field; minuscule (pA to nA)."
    ], current_slide=15, total_slides=total)

    # 16. Reverse Breakdown Mechanisms
    add_bullet_slide(prs, "Reverse Breakdown: Zener Tunneling vs Avalanche", [
        "Breakdown Phenomenon: When reverse voltage exceeds V_BR, reverse current increases abruptly without destruction if current is limited.",
        "Zener Breakdown Mechanism: Occurs in heavily doped junctions (V_BR < 5V); narrow depletion layer (< 10 nm) produces intense E-field (> 10^6 V/m).",
        "Quantum Mechanical Tunneling: Valence electrons tunnel directly through the thin barrier into the conduction band; negative temp coefficient.",
        "Avalanche Breakdown Mechanism: Occurs in lightly doped junctions (V_BR > 6V); wider depletion layer allows carriers to accelerate.",
        "Impact Ionization: Fast carriers collide with crystal lattice atoms, knocking loose new electron-hole pairs in chain reaction; positive temp coefficient."
    ], current_slide=16, total_slides=total)

    # 17. Worked Example 2
    add_example_slide(prs, 2, "Calculation of Built-in Barrier Potential V_0",
                      "A silicon PN junction diode manufactured for an automated tractor alternator regulator has acceptor doping N_A = 5.0 x 10^16 cm^-3 on the P-side and donor doping N_D = 1.0 x 10^16 cm^-3 on the N-side. Operating in a hot engine bay at T = 350 K, intrinsic concentration rises to n_i = 4.0 x 10^11 cm^-3. Calculate: (a) Thermal voltage V_T at 350 K, (b) Built-in potential V_0 at 350 K, (c) Compare with V_0 at 300 K (where n_i = 1.5 x 10^10 cm^-3, V_T = 25.86 mV).",
                      [
                          "1. Thermal Voltage at 350 K: V_T = (k_B · T) / q = (1.3806 x 10^-23 J/K · 350 K) / (1.602 x 10^-19 C) = 0.03016 V = 30.16 mV.",
                          "2. Built-in Potential at 350 K: V_0 = V_T · ln[ (N_A · N_D) / n_i² ].",
                          "   Ratio = (5.0 x 10^16 · 1.0 x 10^16) / (4.0 x 10^11)² = (5.0 x 10^32) / (1.6 x 10^23) = 3.125 x 10^9.",
                          "   ln(3.125 x 10^9) = 21.863 -> V_0(350 K) = 0.03016 V · 21.863 = 0.6594 V (659.4 mV).",
                          "3. Compare at 300 K: Ratio = (5.0 x 10^32) / (1.5 x 10^10)² = 2.222 x 10^12 -> ln(2.222 x 10^12) = 28.429.",
                          "   V_0(300 K) = 0.02586 V · 28.429 = 0.7352 V (735.2 mV).",
                          "4. Temperature Effect: V_0 decreases by ~75.8 mV as temperature rises by 50°C (rate ≈ -1.5 mV/°C due to exponential surge in n_i)."
                      ], current_slide=17, total_slides=total)

    # 18. The Hall Effect Physics
    add_bullet_slide(prs, "The Hall Effect: Magnetohydrodynamic Physics", [
        "Lorentz Force Principle: A moving charge q in perpendicular electric (E) and magnetic (B) fields experiences force F = q(E + v x B).",
        "Charge Deflection: Current I_x flows along x-axis; perpendicular magnetic field B_z exerts transverse Lorentz force F_y = q · v_x · B_z.",
        "Hall Electric Field (E_H): Deflected charges pile up on lateral faces, building transverse field E_H that exactly counterbalances magnetic force.",
        "Hall Voltage Equation: V_H = E_H · w = (I_x · B_z) / (n · q · t) = R_H · (I_x · B_z) / t, where t is semiconductor thickness.",
        "Hall Coefficient: R_H = 1 / (n · q) for electrons; inversely proportional to carrier concentration n (semiconductors produce large V_H!)."
    ], image_file="fig2_4_hall_effect_sensor.png", current_slide=18, total_slides=total)

    # 19. Hall Sensors in Farm Machinery
    add_bullet_slide(prs, "Hall Effect Sensors in Agricultural Machinery", [
        "PTO Shaft Tachometers: Senses passing teeth of tractor power-take-off gear; immune to dust, flying chaff, and grease.",
        "Combine Harvester Threshing Cylinder Monitoring: Detects shaft speed drop indicating drum slugging or belt slippage before jamming.",
        "True Ground Speed Radar & Wheel Encoders: Measures wheel revolutions to calculate slip percentage in muddy paddy cultivation.",
        "Brushless DC (BLDC) Motor Commutation: Senses rotor permanent magnet position to time stator phases in agricultural drone sprayers.",
        "Non-Contact Current Sensing: Measures magnetic field surrounding heavy solar pump cables without physical electrical contact."
    ], current_slide=19, total_slides=total)

    # 20. Worked Example 3
    add_example_slide(prs, 3, "Tractor PTO Shaft Hall Effect Speed Sensor",
                      "A Hall effect transducer is mounted on a Massey Ferguson tractor PTO gearbox to detect gear tooth passage. The semiconductor sensor slice is N-type silicon with thickness t = 0.50 mm and donor carrier density n = 1.0 x 10^15 cm^-3 (1.0 x 10^21 m^-3). A control current I_x = 10.0 mA flows through the sensor. A neodymium target magnet attached to the PTO shaft applies a peak field B_z = 0.35 Tesla. Calculate: (a) Hall coefficient R_H, (b) Peak Hall voltage V_H generated, (c) Frequency of V_H pulses if the PTO rotates at 540 RPM and the sensor monitors a 12-tooth gear.",
                      [
                          "1. Hall Coefficient: R_H = -1 / (n · q) = -1 / (1.0 x 10^21 m^-3 · 1.602 x 10^-19 C) = -6.242 x 10^-3 m³/C.",
                          "2. Calculate Hall Voltage: V_H = (I_x · B_z) / (n · q · t) = |R_H| · (I_x · B_z) / t.",
                          "   Substitute: I_x = 10.0 x 10^-3 A; B_z = 0.35 T; t = 0.50 x 10^-3 m.",
                          "   V_H = (6.242 x 10^-3 m³/C · 0.010 A · 0.35 T) / (0.50 x 10^-3 m) = (2.185 x 10^-5) / (5.0 x 10^-4) = 0.0437 V = 43.7 mV.",
                          "3. Pulse Frequency at 540 RPM: Shaft speed f_shaft = 540 rev / 60 s = 9.0 rev/second (9.0 Hz).",
                          "   With a 12-tooth target gear: Pulse frequency f_pulse = 9.0 Hz · 12 teeth = 108.0 Hz.",
                          "4. System Integration: The 43.7 mV, 108 Hz sinusoidal pulse train is amplified and squared by a comparator into a 5V digital signal."
                      ], current_slide=20, total_slides=total)

    # 21. Case Study 1
    add_case_study_slide(prs, 1, "Hall Sensor Threshing Cylinder Jam Protection",
                         "Kilombero Valley Teak & Rice Basin, Morogoro, Tanzania",
                         "During peak wet-season paddy harvesting, combine harvesters frequently suffered threshing drum slugging when heavy, damp rice straw choked the concave. Slipping drive belts burned out in under 90 seconds before operators noticed engine pitch changes, costing 3,200 USD per breakdown.",
                         "SUA mechatronics engineers installed a rugged hermetic Hall effect speed transducer on the secondary threshing shaft, pairing it with a 16-tooth ferrous target ring. A microcontroller compares engine RPM with threshing drum RPM every 50 ms. If drum slip exceeds 8%, an automated electro-hydraulic clutch disengages the header and sounds a high-decibel alarm within 120 ms.",
                         [
                             "Completely eliminated burnt drive belts and cylinder drum jams across 4 harvesting seasons.",
                             "Automated disengagement response time reduced from > 15 seconds (human) to 120 ms.",
                             "Saved an estimated 28,000 USD in downtime and mechanical repairs across 6 harvesters."
                         ], current_slide=21, total_slides=total)

    # 22. Case Study 2
    add_case_study_slide(prs, 2, "Solar Well Pump Inverter Thermal Runaway Mitigated",
                         "Bahi Wetland & Solar Borehole Project, Dodoma Region, Tanzania",
                         "In semi-arid Dodoma, solar photovoltaic borehole pumping systems operated in ambient temperatures exceeding 43°C. The central inverter junction boxes mounted directly beneath solar panels frequently suffered semiconductor diode and transistor latch-up failures between 12:00 PM and 2:30 PM.",
                         "Thermal analysis revealed that internal junction temperatures were surpassing 145°C. At this temperature, intrinsic carrier generation n_i surged by a factor of 85, collapsing reverse breakdown voltage and creating thermal carrier leakage runaway. Engineers retrofitted the enclosures with thermal chimney solar shields and upsized the silicon heat sinks.",
                         [
                             "Junction operating temperature dropped from 148°C to a safe 82°C under peak insolation.",
                             "Pumping uptime restored to 100%, delivering 65,000 liters/day of irrigation water.",
                             "Extended estimated power semiconductor MTBF from 6 months to over 7 years."
                         ], current_slide=22, total_slides=total)

    # 23. Laboratory Bench Protocol
    add_lab_slide(prs, "Semiconductor Diode & Hall Sensor Bench Characterization", [
        "Measure silicon and germanium PN junction barrier voltages using curve tracer / bench supply.",
        "Determine the temperature coefficient of built-in barrier voltage Delta V / Delta T.",
        "Observe reverse breakdown characteristics on high-voltage test supply.",
        "Calibrate a Hall effect sensor module against known magnetic fields and gear rotation."
    ], [
        "Step 1: Wire 1N4007 (Si) and 1N34A (Ge) diodes on breadboard with 1 kOhm current-limiting resistor.",
        "Step 2: Sweep DC supply from 0.0V to 1.5V; log diode voltage V_D and current I_D on digital multimeters.",
        "Step 3: Plot forward I-V curve; extract knee barrier voltage (V_knee ≈ 0.65V for Si, 0.28V for Ge).",
        "Step 4: Immerse diode in controlled hot-water bath (30°C to 70°C); record V_D at fixed I_D = 1.0 mA; compute -2.1 mV/°C slope.",
        "Step 5: Mount Hall sensor module (UGN3503) adjacent to motorized gear wheel; connect DSO; verify pulse amplitude vs gap distance."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "Explain why intrinsic silicon behaves as an insulator at 0 Kelvin but conducts electricity at room temperature (300 K).",
        "State the Law of Mass Action. If silicon is doped with 10^17 cm^-3 Boron atoms, what is the minority electron density?",
        "Derive the equation for the built-in barrier potential V_0 of a PN junction and explain its temperature dependence.",
        "Contrast Zener breakdown and Avalanche breakdown in terms of doping concentration and temperature coefficients.",
        "Explain the physical principle of the Hall effect and write the equation for the generated Hall voltage V_H."
    ], "Lecture 3 will explore Semiconductor Diodes & Applications: Shockley equation, dynamic resistance, rectification, and clippers/clampers.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "Semiconductor electrical behavior is governed by energy bandgap E_g (1.12 eV for Si at 300 K).",
        "Extrinsic doping (N-type donors, P-type acceptors) increases carrier density and conductivity by millions of times.",
        "In thermal equilibrium, the Law of Mass Action (n · p = n_i²) holds strictly constant across all doping levels.",
        "The PN junction depletion region creates a built-in barrier potential V_0 ≈ 0.7 V for Si (decreases by ~2 mV/°C).",
        "The Hall effect provides rugged, non-contact magnetic speed and position sensing immune to agricultural grime."
    ], [
        "Mass Action: n · p = n_i²(T)",
        "Conductivity: sigma = q(n·mu_n + p·mu_p); rho = 1/sigma",
        "Einstein Relation: D / mu = V_T = k_B · T / q ≈ 26 mV",
        "Built-in Potential: V_0 = V_T · ln[ (N_A · N_D) / n_i² ]",
        "Depletion Width: W_dep proportional to sqrt(V_0 + V_R)",
        "Hall Voltage: V_H = (I_x · B_z) / (n · q · t) = R_H · (I_x · B_z) / t",
        "Hall Coefficient: R_H = 1 / (n · q)"
    ], current_slide=25, total_slides=total)

    # 26. References & Reading List
    add_bullet_slide(prs, "Prescribed References & Practical Laboratory Preparation", [
        "Streetman, B. G., & Banerjee, S. (2016). Solid State Electronic Devices (7th ed.). Pearson.",
        "Sedra, A. S., & Smith, K. C. (2020). Microelectronic Circuits (8th ed.). Oxford University Press.",
        "Boylestad, R. L., & Nashelsky, L. (2018). Electronic Devices and Circuit Theory (11th ed.). Pearson Education.",
        "Laboratory Preparation: Review semiconductor diode safety procedures and wear ESD wrist straps during Lab Session 2.",
        "Field Assignment: Complete Assignment 1, Questions 5 to 8 on semiconductor physics and submit via SUA LMS."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

def build_lecture_3_deck(prs):
    lec_num = 3
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Semiconductor Diode & Circuits",
                    "Shockley Equation, Rectification, Power Smoothing, Clippers & Clampers", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 3 Learning Outcomes & Practical Scope", [
        "Model Diode I-V Characteristics: Master the Shockley equation, reverse saturation current I_S, and ideality factor eta.",
        "Derive Dynamic AC Resistance: Calculate small-signal resistance r_d = eta·V_T / I_DQ and understand junction capacitance.",
        "Evaluate Diode Approximations: Contrast ideal (0V), 2nd approximation (0.7V offset), and 3rd piecewise linear models.",
        "Analyze AC-to-DC Rectification: Design Half-Wave, Center-Tapped Full-Wave, and Full-Wave Bridge rectifier circuits.",
        "Design Power Smoothing Filters: Calculate DC output voltage V_DC, peak-to-peak ripple V_r, and ripple factor gamma.",
        "Synthesize Waveform Conditioning Circuits: Design positive/negative diode clippers (limiters) and clampers (DC restorers).",
        "Apply Diodes in AgriTech Power: Size solar charge controller rectifiers and battery reverse-polarity protection diodes."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "Diode Power Circuits in Agricultural Electrification", [
        "The AC-to-DC Bridge: Farm microcontrollers, sensor transmitters, and DC solenoid valves require pure DC power.",
        "Rural Grid Volatility: TANESCO rural supply lines experience severe voltage sags (down to 160V) and surges (> 270V).",
        "Solar Water Pumping: Photovoltaic panels generate fluctuating DC that requires diode steering, blocking, and rectification.",
        "Tractor Alternator Packs: 3-phase automotive alternators rely on six heavy-duty press-fit silicon diodes to charge 12V batteries.",
        "Battery Reverse-Polarity Destruction: Farm operators frequently connect tractor booster cables backwards; diodes provide fail-safe protection."
    ], image_file="img_diodes_rectifier.jpg", current_slide=3, total_slides=total)

    # 4. The Shockley Diode Equation
    add_bullet_slide(prs, "The Shockley Diode Equation & Operating Regimes", [
        "Governing Equation: I_D = I_S · [ exp( V_D / (eta · V_T) ) - 1 ], where I_S is reverse saturation current.",
        "Ideality Factor (eta): eta = 1.0 for pure diffusion current (Germanium, high-current Silicon); eta ≈ 2.0 at low currents in Silicon.",
        "Thermal Voltage: V_T = (k_B · T) / q ≈ 25.86 mV at 300 K (commonly taken as 26 mV in engineering calculations).",
        "Forward Bias Regime (V_D > 0.5 V): The exponential term dominates: I_D ≈ I_S · exp[ V_D / (eta · V_T) ].",
        "Reverse Bias Regime (V_D < -0.1 V): The exponential vanishes: I_D ≈ -I_S; current saturates to minuscule thermal leakage.",
        "Temperature Dependence: I_S doubles approximately every 5°C rise in temperature in silicon diodes."
    ], image_file="fig3_1_diode_iv_characteristics.png", current_slide=4, total_slides=total)

    # 5. Dynamic AC Junction Resistance rd
    add_bullet_slide(prs, "Static vs Dynamic Diode Junction Resistance", [
        "Static (DC) Resistance: R_D = V_DQ / I_DQ; The ratio of total DC voltage to total DC current at the operating Q-point.",
        "Dynamic (AC) Resistance: r_d = dV_D / dI_D |_(Q-point); The slope of the tangent line on the non-linear I-V curve.",
        "Mathematical Derivation: Since I_D ≈ I_S · exp[ V_D / (eta · V_T) ], differentiating gives: dI_D / dV_D = I_D / (eta · V_T).",
        "Reciprocal Slope Formula: r_d = (eta · V_T) / I_DQ ≈ 26 mV / I_DQ (for eta = 1 at room temperature).",
        "Practical Significance: At I_DQ = 1.0 mA, r_d = 26 Ohm; at I_DQ = 26 mA, r_d = 1.0 Ohm. Resistance drops as current rises!"
    ], current_slide=5, total_slides=total)

    # 6. Diode Circuit Approximations
    add_bullet_slide(prs, "Piecewise Linear Diode Approximations", [
        "First Approximation (Ideal Diode): Perfect switch; 0V drop in forward bias (closed switch), 0A in reverse bias (open switch).",
        "Second Approximation (Constant Voltage Drop): Forward-biased diode modeled as a constant 0.7V DC source (0.3V for Germanium).",
        "Third Approximation (Complete Piecewise Model): Includes constant 0.7V offset in series with bulk dynamic resistance r_B: V_D = 0.7V + I_D · r_B.",
        "Reverse Recovery Time (t_rr): Time required for stored minority carriers to recombine before diode blocks reverse voltage.",
        "Junction Capacitances: Depletion capacitance C_dep dominates in reverse bias; Diffusion capacitance C_diff dominates in forward bias."
    ], current_slide=6, total_slides=total)

    # 7. Half-Wave Rectification Analysis
    add_bullet_slide(prs, "Half-Wave Rectifier Analysis & Metrics", [
        "Circuit Operation: Single diode in series with AC secondary winding and load resistor R_L.",
        "Positive Half-Cycle (0 to pi): Diode forward-biased (ON); conducts current; v_out(t) = v_in(t) - V_knee.",
        "Negative Half-Cycle (pi to 2pi): Diode reverse-biased (OFF); blocks current; v_out(t) = 0V.",
        "Peak Output Voltage: V_m(out) = V_m - 0.7 V, where V_m = sqrt(2) · V_rms.",
        "DC Average Output Voltage: V_DC = V_m(out) / pi ≈ 0.318 · V_m(out).",
        "Peak Inverse Voltage (PIV): Maximum reverse voltage across diode: PIV = V_m.",
        "Rectification Efficiency: Maximum theoretical efficiency eta_max = 40.6%; leaves large ripple and poor transformer utilization."
    ], current_slide=7, total_slides=total)

    # 8. Full-Wave Bridge Rectification
    add_bullet_slide(prs, "Full-Wave Bridge Rectifier Architecture", [
        "Four-Diode Bridge Topology: Conduction occurs on both AC half-cycles without requiring a bulky center-tapped transformer.",
        "Positive Half-Cycle: Diodes D1 and D2 conduct in series through load R_L; D3 and D4 are reverse-biased.",
        "Negative Half-Cycle: Diodes D3 and D4 conduct in series through load R_L in the SAME direction; D1 and D2 are reverse-biased.",
        "Peak Output Voltage: V_m(out) = V_m - 2 · V_knee = V_m - 1.4 V (due to two series conducting diodes).",
        "DC Average Output Voltage: V_DC = (2 · V_m(out)) / pi ≈ 0.636 · V_m(out) (double that of half-wave!).",
        "Peak Inverse Voltage: PIV = V_m(out) + 0.7 V ≈ V_m; Ripple frequency is 2 · f_in (100 Hz on 50 Hz TANESCO grid).",
        "Rectification Efficiency: Maximum theoretical efficiency eta_max = 81.2%."
    ], image_file="fig3_2_bridge_rectifier_schematic.png", current_slide=8, total_slides=total)

    # 9. Rectifier Waveform Comparisons
    add_bullet_slide(prs, "Comparative Rectifier Output Waveforms", [
        "Unfiltered Pulsating DC: Output contains large AC harmonic ripple voltages superimposed on the average DC level.",
        "Ripple Frequency: Half-wave ripple frequency = f_in (50 Hz); Full-wave ripple frequency = 2 · f_in (100 Hz).",
        "Transformer Utilization Factor (TUF): Bridge rectifier TUF = 0.812; Center-tapped TUF = 0.672; Half-wave TUF = 0.287.",
        "Diode Conduction Angle: Current flows for 180° in each branch of a full-wave rectifier compared to only 180° per cycle in half-wave.",
        "Thermal Dissipation: Power loss in bridge diodes: P_loss = 2 · V_D · I_DC_avg; requires aluminum heat sinking above 3 Amperes."
    ], image_file="fig3_3_rectifier_waveforms.png", current_slide=9, total_slides=total)

    # 10. Capacitor Input Smoothing Filters
    add_bullet_slide(prs, "Capacitor Input Smoothing Filters & Ripple Factor", [
        "Smoothing Action: A large electrolytic capacitor C is placed in parallel with load R_L.",
        "Charging Phase: Diode conducts briefly at waveform peaks, rapidly charging C to peak voltage V_peak.",
        "Discharging Phase: When input drops below capacitor voltage, diodes cut off; C discharges slowly through R_L with time constant tau = R_L · C.",
        "Peak-to-Peak Ripple Voltage: V_r(p-p) ≈ I_DC / (2 · f · C) = V_DC / (2 · f · R_L · C) (for full-wave rectifier).",
        "DC Output Voltage with Filter: V_DC ≈ V_peak - 0.5 · V_r(p-p).",
        "Ripple Factor (gamma): gamma = V_r,rms / V_DC ≈ 1 / [ 4 · sqrt(3) · f · R_L · C ]; Lower gamma indicates purer DC.",
        "Diode Surge Current (I_surge): During initial turn-on, uncharged capacitor pulls intense inrush current; requires surge-rated diodes."
    ], current_slide=10, total_slides=total)

    # 11. Worked Example 1
    add_example_slide(prs, 1, "Dynamic Resistance of Temperature Sensor Diode",
                      "A 1N4148 silicon small-signal diode is used as a linear temperature sensor probe in a Morogoro poultry egg incubator. Operating under forward bias at room temperature (T = 300 K, eta = 1.0, V_T = 26 mV), its quiescent DC current is set to I_DQ = 2.50 mA. When forward voltage shifts by Delta V = 10 mV, calculate: (a) Dynamic AC junction resistance r_d, (b) Corresponding change in diode current Delta I, (c) Recalculate r_d if bias current is increased to 20.0 mA.",
                      [
                          "1. Dynamic Resistance Formula: r_d = (eta · V_T) / I_DQ.",
                          "2. Calculate at 2.50 mA: r_d = (1.0 · 26 mV) / 2.50 mA = 0.026 V / 0.0025 A = 10.40 Ohm.",
                          "3. Small-Signal Current Change: Delta I ≈ Delta V / r_d = 10 mV / 10.40 Ohm = 0.010 V / 10.40 Ohm = 0.9615 mA (961.5 microA).",
                          "4. Recalculate at 20.0 mA: r_d = 26 mV / 20.0 mA = 0.026 V / 0.020 A = 1.30 Ohm.",
                          "5. Engineering Insight: Increasing the DC operating current by 8 times reduces the dynamic junction resistance by 8 times, providing a much stiffer signal source for sensor interfacing."
                      ], current_slide=11, total_slides=total)

    # 12. Worked Example 2
    add_example_slide(prs, 2, "Full-Wave Bridge Rectifier & Filter for Drip PLC",
                      "Design a full-wave bridge rectifier power supply for an automated drip irrigation PLC at Kilombero Sugar Estate. The step-down transformer secondary delivers V_rms = 18.0 V at f = 50 Hz. The PLC load draws a continuous DC current I_DC = 1.50 A. Silicon diodes have forward drop V_D = 0.70 V. Calculate: (a) Peak output voltage V_peak, (b) Required filter capacitance C to limit peak-to-peak ripple to V_r(p-p) <= 1.20 V, (c) Resulting DC output voltage V_DC, (d) Minimum diode PIV rating.",
                      [
                          "1. Peak AC Secondary Voltage: V_m = sqrt(2) · V_rms = 1.4142 · 18.0 V = 25.46 V.",
                          "2. Peak Rectified Output Voltage: Bridge drops two diodes: V_peak = V_m - 2·V_D = 25.46 V - 1.40 V = 24.06 V.",
                          "3. Sizing Smoothing Filter: V_r(p-p) = I_DC / (2 · f · C) -> C = I_DC / (2 · f · V_r(p-p)).",
                          "   Substitute: C = 1.50 A / (2 · 50 Hz · 1.20 V) = 1.50 / 120 = 0.0125 F = 12,500 microFarad (select standard 15,000 microF / 35V).",
                          "4. Average DC Output Voltage: V_DC = V_peak - 0.5 · V_r(p-p) = 24.06 V - 0.5(1.20 V) = 24.06 V - 0.60 V = 23.46 V.",
                          "5. Diode PIV Requirement: PIV = V_m - V_D = 25.46 V - 0.70 V = 24.76 V. (With 2x farm safety factor, specify 1N5402 with PIV >= 100V)."
                      ], current_slide=12, total_slides=total)

    # 13. Diode Clipper Circuits (Limiters)
    add_bullet_slide(prs, "Diode Clipper (Limiter) Circuit Topologies", [
        "Circuit Function: Removes (clips) portions of an input signal above or below a specified reference level without distorting the remainder.",
        "Positive Clipper: Diode conducts when input exceeds reference V_ref + 0.7V, shunting excess voltage to ground or reference rail.",
        "Negative Clipper: Diode placed in reverse polarity; clips the negative excursion below -V_ref - 0.7V.",
        "Biased Clippers: A DC bias battery in series with the diode sets the clipping threshold to any desired positive or negative potential.",
        "Combination (Dual) Clipper: Two anti-parallel diodes clamp input signal between +0.7V and -0.7V; protects microcontroller ADC pins."
    ], image_file="fig3_4_clipper_clamper_circuits.png", current_slide=13, total_slides=total)

    # 14. Diode Clamper Circuits (DC Restorers)
    add_bullet_slide(prs, "Diode Clamper (DC Restorer) Circuits", [
        "Circuit Function: Shifts the entire AC waveform to a different DC reference level without altering the peak-to-peak waveshape.",
        "Circuit Architecture: Requires a series capacitor C, a shunt diode D, and a parallel discharge resistor R_L.",
        "Positive Clamper: Diode cathode grounded; diode conducts on negative peaks, charging capacitor to V_peak; output shifted positively above 0V.",
        "Negative Clamper: Diode anode grounded; capacitor charges to positive peak; entire waveform shifted negatively below 0V.",
        "Clamping Time Constant Rule: The RC discharge time constant must be much larger than the signal period: R_L · C >= 10 · T_signal."
    ], current_slide=14, total_slides=total)

    # 15. Worked Example 3
    add_example_slide(prs, 3, "Diode Input Overvoltage Limiter for Tractor ECU",
                      "An analog soil conductivity sensor on an autonomous tractor outputs an analog signal v_in that fluctuates between -4.0 V and +9.0 V. The tractor microcontroller ADC input accepts strictly 0.0 V to +5.0 V. Design a biased dual-diode clipper using 1N4148 silicon diodes (V_D = 0.70 V) and a series current-limiting resistor R = 2.2 kOhm. Determine: (a) The required bias voltages V_bias,high and V_bias,low, (b) Output voltage range, (c) Maximum diode power dissipation during +9.0 V overvoltage.",
                      [
                          "1. Top Limiter Design (Clip at +5.0 V): We require output clamped to +5.0 V. Since diode drops 0.70 V: V_out,max = V_bias,high + V_D -> 5.0 V = V_bias,high + 0.70 V -> V_bias,high = 4.30 V (or connect diode anode to +5.0V rail -> clips at 5.0 + 0.7 = 5.7V).",
                          "   Using precise bias: V_bias,high = 4.30 V clamps output at exactly +5.0 V.",
                          "2. Bottom Limiter Design (Clip at 0.0 V): We require output clamped to 0.0 V. Since bottom diode drops 0.70 V: V_out,min = V_bias,low - V_D -> 0.0 V = V_bias,low - 0.70 V -> V_bias,low = +0.70 V (or ground anode -> clips at -0.7V).",
                          "   Using precise bias: V_bias,low = +0.70 V clamps output at exactly 0.0 V.",
                          "3. Peak Overvoltage Current: At v_in = +9.0 V, output is clamped to +5.0 V. Voltage across series resistor: V_R = 9.0 V - 5.0 V = 4.0 V.",
                          "   Diode Forward Current: I_D = V_R / R = 4.0 V / 2,200 Ohm = 1.818 mA.",
                          "4. Diode Power Dissipation: P_diode = V_D · I_D = 0.70 V · 1.818 mA = 1.27 mW (well within 1N4148 rating of 500 mW!)."
                      ], current_slide=15, total_slides=total)

    # 16. Diode Selection & Commercial Ratings
    add_bullet_slide(prs, "Commercial Diode Specifications & Selection Guide", [
        "Maximum Average Forward Current (I_F(AV)): Rated continuous DC forward current (e.g. 1N4007 = 1.0A; 1N5408 = 3.0A; 6A10 = 6.0A).",
        "Peak Inverse Voltage (PIV / V_RRM): Maximum repetitive peak reverse voltage before avalanche breakdown (1N4007 = 1,000V).",
        "Forward Voltage Drop (V_F): Typical forward drop at rated current (0.7V to 1.1V for silicon; 0.3V to 0.45V for Schottky).",
        "Peak Forward Surge Current (I_FSM): Maximum allowable single half-sine inrush current (1N4007 = 30A for 8.3 ms).",
        "Thermal Resistance (theta_JA): Junction-to-ambient thermal resistance; determines temperature rise Delta T = P_diss · theta_JA."
    ], current_slide=16, total_slides=total)

    # 17. Reverse Polarity Protection Topologies
    add_bullet_slide(prs, "DC Battery Reverse-Polarity Protection Topologies", [
        "Series Diode Protection: Place rectifier diode in series with positive DC input; blocks reverse current completely.",
        "Forward Drop Drawback: Series diode dissipates power: P_loss = V_D · I_load; at 5A load, drops 0.7V and generates 3.5W heat.",
        "Shunt Diode with Fuse (Crowbar): Place reverse-biased diode across supply rails behind a fast-acting fuse.",
        "Crowbar Action: Correct polarity -> diode is OFF; Reversed polarity -> diode conducts heavily, blowing the fuse within 10 ms.",
        "MOSFET Reverse Protection: P-channel MOSFET provides reverse protection with ultra-low voltage drop (R_DS(on) < 10 mOhm)."
    ], current_slide=17, total_slides=total)

    # 18. AC and DC Superposition in Diodes
    add_bullet_slide(prs, "Small-Signal AC Superposition & Diode Load Line", [
        "Quiescent Operating Point (Q-point): The DC voltage V_DQ and current I_DQ established by DC bias supplies and resistors.",
        "DC Load Line Equation: I_D = (V_CC - V_D) / R_L; Straight line connecting (V_CC, 0) and (0, V_CC / R_L) on I-V plane.",
        "Q-point Intersection: Intersection of DC load line and non-linear diode characteristic curve determines exact operating point.",
        "Small-Signal AC Model: When small AC signal v_ac is superimposed, diode behaves as linear dynamic resistance r_d.",
        "Total Instantaneous Output: v_out(t) = V_DQ + v_ac(t) · [ R_L / (R_L + r_d) ]; Verified by superposition principle."
    ], current_slide=18, total_slides=total)

    # 19. Practical Farm Environment Hardening
    add_bullet_slide(prs, "Hardening Diode Circuits for Rural Agriculture", [
        "Thermal Heatsinking: High-current bridge rectifiers (> 10A) must be bolted to finned aluminum extrusions with thermal paste.",
        "Dust and Mud Accumulation: Heavy red laterite dust forms insulating blankets over heatsinks, causing thermal runaway; use IP66 sealed housings.",
        "Lightning Induced Spikes: Rural TANESCO overhead lines pick up electrostatic charges; parallel 1.5KE400A TVS diodes protect bridge inputs.",
        "Electrolytic Filter Derating: Specify 105°C rated capacitors rather than consumer 85°C types to guarantee 10-year lifespan under tropical sun.",
        "Vibration Resistance: Heavy bridge rectifiers on tractor chassis must be mechanically staked with RTV silicone adhesive."
    ], current_slide=19, total_slides=total)

    # 20. Case Study 1
    add_case_study_slide(prs, 1, "Solar Milking Machine Battery Reverse Clamping",
                         "Msolwa Ujamaa Dairy Cooperative, Kilombero, Tanzania",
                         "A community dairy cooperative powered their automated milking pulsator and milk chilling vat from a 24V solar battery bank. During night battery swaps, attendants accidentally reversed the heavy battery booster cables twice in one month, blowing the main inverter motherboard and spoiling 450 liters of fresh milk.",
                         "SUA agricultural engineers retrofitted the DC input stage with a heavy-duty 50A, 1,200V stud-mount silicon rectifier diode (1N1188) in anti-parallel behind a 40A fast-blow automotive ceramic fuse. An adjacent warning buzzer was wired to sound instantly if reverse polarity is detected.",
                         [
                             "Successfully protected inverter electronics during two subsequent accidental cable reversals.",
                             "Saved over 4,500 USD in potential motherboard repair costs and milk wastage.",
                             "Zero operating power loss during normal dairy milking machine running."
                         ], current_slide=20, total_slides=total)

    # 21. Case Study 2
    add_case_study_slide(prs, 2, "Bridge Rectifier Failure in Grain Aeration Blowers",
                         "National Food Reserve Agency (NFRA) Silo Depot, Morogoro, Tanzania",
                         "Commercial grain aeration blowers operating at a 20,000-tonne maize storage depot experienced frequent DC power supply burnouts during the rainy season. DC control boards lost power, shutting down ventilation fans and causing grain caking and moisture hot spots in silo bins 3 and 7.",
                         "Forensic analysis of the blown 4-diode bridges revealed that high-voltage inductive switching spikes from adjacent 75 kW blower motors were generating peak reverse surges exceeding 850V, exceeding the 400V PIV rating of the factory-installed bridges. Engineers replaced the bridges with 1,000V, 25A metal-cased KBPC2510 modules paired with 0.1 microF snubber capacitors.",
                         [
                             "Achieved 100% power supply reliability through two consecutive wet storage campaigns.",
                             "Grain moisture remained safely uniform at 13.2% without a single metric ton lost to spoilage.",
                             "Snubber capacitors absorbed motor inductive spikes, reducing transient noise by 88%."
                         ], current_slide=21, total_slides=total)

    # 22. Laboratory Bench Protocol
    add_lab_slide(prs, "Full-Wave Bridge Rectifier & Filter Characterization", [
        "Assemble a full-wave bridge rectifier circuit on breadboard using four 1N4007 diodes.",
        "Measure input AC and unfiltered pulsating DC waveforms on digital storage oscilloscope.",
        "Add electrolytic filter capacitors (100 microF, 470 microF, 1,000 microF) and quantify ripple voltage reduction.",
        "Implement a positive diode clipper and verify clipping threshold against DC bias supply."
    ], [
        "Step 1: Connect 12V AC secondary transformer winding to bridge input on breadboard; connect 1 kOhm load resistor.",
        "Step 2: Connect DSO Ch 1 across transformer secondary; connect DSO Ch 2 across load resistor. Record V_peak and V_DC.",
        "Step 3: Insert 470 microFarad capacitor across load. Measure peak-to-peak ripple V_r(p-p) and calculate empirical ripple factor.",
        "Step 4: Increase load current by placing 220 Ohm resistor in parallel; observe ripple voltage increase on DSO screen.",
        "Step 5: Assemble biased clipper circuit with 3V DC bench source; inject 10V p-p sine wave; verify flat clipping at 3.7V."
    ], current_slide=22, total_slides=total)

    # 23. Troubleshooting & Pitfalls
    add_bullet_slide(prs, "Diagnostic Troubleshooting of Diode Circuits", [
        "Open-Circuit Diode: DMM diode test reads 'OL' (overload) in BOTH forward and reverse directions; in bridge, causes half-wave output.",
        "Shorted Diode: DMM reads near 0.000 V and beeps in BOTH directions; in bridge, shorts the transformer secondary and blows fuse.",
        "Excessive Ripple Voltage: Dried-out electrolytic filter capacitor loses capacitance; DC voltage drops and AC hum increases drastically.",
        "Thermal Overheating: Diode exceeds 150°C junction temperature; silicon thermal leakage increases until thermal runaway occurs.",
        "Reverse Leakage Surge: High operating temperatures in engine bays cause I_S to surge, triggering false alarms in high-impedance sensors."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "Write the Shockley diode equation and define all parameters including thermal voltage V_T and ideality factor eta.",
        "Derive the small-signal dynamic resistance r_d of a diode and calculate its value at I_DQ = 5.0 mA at 300 K.",
        "Compare Half-Wave, Center-Tapped Full-Wave, and Bridge rectifiers in terms of PIV, average DC output, and efficiency.",
        "Explain why a capacitor input filter causes intense surge currents through rectifier diodes during initial power turn-on.",
        "Draw the circuit diagram of a dual-diode clipper that limits an analog sensor signal between -0.7 V and +3.3 V."
    ], "Lecture 4 will explore Special Purpose Diodes: Zener shunt regulators, LEDs for PAR grow lighting, and Schottky solar bypass diodes.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "The diode conducts exponentially in forward bias (0.7V for Si) and blocks current in reverse bias.",
        "Small-signal dynamic resistance is inversely proportional to DC bias current: r_d ≈ 26 mV / I_DQ.",
        "Full-wave bridge rectifiers provide 81.2% maximum theoretical efficiency with PIV = V_m.",
        "Smoothing capacitors reduce ripple to V_r(p-p) ≈ I_DC / (2 · f · C); larger capacitance yields purer DC.",
        "Clippers limit voltage excursions for ADC pin protection; clampers restore or shift DC reference levels."
    ], [
        "Shockley Equation: I_D = I_S · [ exp( V_D / (eta · V_T) ) - 1 ]",
        "Dynamic Resistance: r_d = (eta · V_T) / I_DQ ≈ 26 mV / I_DQ",
        "Half-Wave DC: V_DC = V_peak / pi; PIV = V_m",
        "Full-Wave Bridge DC: V_DC = 2·V_peak / pi; V_peak = V_m - 1.4V",
        "Filter Ripple Voltage: V_r(p-p) = I_DC / (2 · f · C)",
        "Ripple Factor: gamma = 1 / [ 4 · sqrt(3) · f · R_L · C ]",
        "Diode Power Loss: P = V_D · I_avg"
    ], current_slide=25, total_slides=total)

    # 26. References & Reading List
    add_bullet_slide(prs, "Prescribed References & Practical Laboratory Preparation", [
        "Boylestad, R. L., & Nashelsky, L. (2018). Electronic Devices and Circuit Theory (11th ed.). Pearson Education.",
        "Sedra, A. S., & Smith, K. C. (2020). Microelectronic Circuits (8th ed.). Oxford University Press.",
        "Floyd, T. L. (2017). Electronic Devices: Conventional Current Version (10th ed.). Pearson.",
        "Laboratory Preparation: Review oscilloscope AC coupling vs DC coupling modes before Lab Session 3.",
        "Field Assignment: Complete Assignment 1, Questions 9 to 12 on diode rectification and filtering."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

print("slides_part1 module complete with Lectures 1, 2, and 3.")

