#!/usr/bin/env python3
"""
build_compedia_4.py
Comprehensive Lecture Compendium for:
LECTURE 4: SPECIAL PURPOSE DIODES
Course: AEN 214 Introduction to Electronics
Department of Agricultural Engineering, Sokoine University of Agriculture (SUA).
Target Length: > 15 Pages (16-18 pages).
"""

import os
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, PageBreak, KeepTogether
from compendium_base import (
    get_custom_stylesheet, create_banner_header, create_callout,
    create_example, create_figure, create_custom_table, render_pdf
)

def build_lecture_4():
    styles = get_custom_stylesheet()
    story = []

    # 1. Header Banner
    topics = [
        "4.1 Zener Diode Physics: Field Emission (Zener) vs Impact Ionization (Avalanche) Breakdown",
        "4.2 Zener Voltage Regulator Design: Mathematical Proofs of Line & Load Regulation",
        "4.3 Light Emitting Diodes (LEDs): Electroluminescence, Direct Bandgaps & Photon Wavelengths",
        "4.4 Greenhouse Horticultural Lighting: Photosynthetically Active Radiation (PAR) Engineering",
        "4.5 Photodiodes, Phototransistors & Solar Cells: Photoconductive vs Photovoltaic Modes",
        "4.6 Optocouplers & Galvanic Isolation: Eliminating Ground Loops in Agricultural Telemetry",
        "4.7 Schottky Barrier Diodes: Metal-Semiconductor Physics & Zero Reverse Recovery Time",
        "4.8 Solar PV Bypass & Blocking Architectures: Mitigating Partial Shading Hotspots",
        "4.9 Transient Voltage Suppression (TVS) Diodes: Surviving Tropical Lightning Surges",
        "4.10 Practical Laboratory Bench Protocol: Zener Regulation & Optoisolator CTR Testing",
        "4.11 Tanzanian Agricultural Field Case Studies: Arusha Horticulture & Dodoma Solar Pumping",
        "4.12 Comprehensive Self-Assessment: Conceptual, Quantitative & System Design Problems"
    ]
    story.extend(create_banner_header(4, "Special Purpose Diodes & Optoelectronics", topics))

    # -------------------------------------------------------------
    # SECTION 1: ZENER DIODE PHYSICS & BREAKDOWN
    # -------------------------------------------------------------
    story.append(Paragraph("4.1 Zener Diode Physics & Breakdown Mechanisms", styles['SecH1']))
    story.append(Paragraph(
        "While standard rectifier diodes are destroyed if driven into reverse breakdown, the <b>Zener Diode</b> is a heavily doped silicon "
        "PN junction specifically fabricated to operate continuously and reliably in the reverse breakdown regime. "
        "When reverse biased beyond a specific threshold called the <b>Zener Breakdown Voltage (V<sub>Z</sub>)</b>, the diode exhibits a dramatic "
        "collapse in dynamic resistance, maintaining a remarkably stable terminal voltage across large variations in reverse current. "
        "In agricultural instrumentation—such as reference voltage generators for microcontroller analog-to-digital converters, "
        "battery overvoltage clamps on farm tractors, and sensor signal limiters—Zener diodes serve as essential voltage-regulating components.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Two Distinct Breakdown Mechanisms:</b><br/>"
        "Depending on the doping concentration and the resulting breakdown voltage, reverse conduction is governed by two fundamentally different physical processes:<br/>"
        "<b>1. Zener Breakdown (Field Emission):</b> Occurs in junctions with extremely heavy doping (donor and acceptor concentrations <i>N_A, N_D > 10¹⁸ cm⁻³</i>). "
        "The depletion layer is exceptionally thin (<i>W < 10 nm</i>). Even at low reverse voltages (<i>V_R < 5 V</i>), the resulting electric field across the junction "
        "reaches colossal magnitudes exceeding <b>E > 3 × 10⁷ V/m (300 kV/cm)</b>. This intense electric field directly pulls valence electrons out of their "
        "covalent bonds into the conduction band via quantum mechanical tunneling (field emission). "
        "<i>Temperature Coefficient:</i> Negative (<i>TC < 0</i>). As temperature rises, the semiconductor bandgap decreases slightly, facilitating tunneling at lower voltages.<br/>"
        "<b>2. Avalanche Breakdown (Impact Ionization):</b> Dominates in lightly doped junctions with wider depletion regions, typically occurring at <b>V_R > 6 V</b>. "
        "Thermally generated minority carriers entering the depletion layer are accelerated by the electric field, acquiring immense kinetic energy. "
        "These energetic carriers collide violently with lattice atoms, knocking bound valence electrons into the conduction band (impact ionization). "
        "The newly liberated electron-hole pairs are themselves accelerated, causing cumulative exponential carrier multiplication (an avalanche). "
        "<i>Temperature Coefficient:</i> Positive (<i>TC > 0</i>). As temperature rises, lattice vibrations increase, causing more frequent collisions and shorter mean free paths; carriers require higher reverse voltages to acquire sufficient kinetic energy to cause impact ionization.<br/>"
        "<b>Zero Temperature Coefficient Reference Diodes:</b> Around <b>V<sub>Z</sub> ≈ 5.6 V</b>, the negative temperature coefficient of Zener tunneling exactly cancels the positive coefficient of avalanche breakdown, providing an exceptionally temperature-stable voltage reference (<i>TC ≈ 0 mV/°C</i>), critical for precision precision weighing scales in Morogoro grain silos.",
        styles['DocBody']
    ))

    story.append(create_figure("fig4_2_zener_iv_characteristics.png", "Zener Diode Complete I-V Characteristics Showing Reverse Knee (I_ZK), Test Current (I_ZT), and Maximum Safe Current (I_ZM)", target_width=5.5*inch))

    # -------------------------------------------------------------
    # SECTION 2: ZENER REGULATOR MATHEMATICAL ANALYSIS
    # -------------------------------------------------------------
    story.append(Paragraph("4.2 Zener Voltage Regulator Mathematical Analysis & Design Equations", styles['SecH1']))
    story.append(Paragraph(
        "A basic shunt Zener regulator consists of a series current-limiting resistor <i>R_S</i> connected between an unregulated DC input source <i>V_S</i> "
        "and a parallel combination of the Zener diode and the load resistor <i>R_L</i>. To maintain tight regulation, the Zener diode must remain "
        "in breakdown under all operating conditions (from minimum input voltage and maximum load current, to maximum input voltage and zero load current).",
        styles['DocBody']
    ))

    story.append(create_figure("fig4_1_zener_regulator_schematic.png", "Schematic of Shunt Zener Voltage Regulator Providing Stable V_out Despite Fluctuating Input V_S and Varying Load I_L", target_width=5.5*inch))

    story.append(Paragraph(
        "<b>1. Fundamental Kirchhoff Circuit Equations:</b><br/>"
        "Applying Kirchhoff's Current Law (KCL) at the output node:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>I<sub>S</sub> = I<sub>Z</sub> + I<sub>L</sub></b><br/>"
        "Applying Kirchhoff's Voltage Law (KVL) around the input loop:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>V<sub>S</sub> - I<sub>S</sub> · R<sub>S</sub> - V<sub>out</sub> = 0 &implies; I<sub>S</sub> = (V<sub>S</sub> - V<sub>out</sub>) / R<sub>S</sub></b><br/>"
        "where <i>V<sub>out</sub> ≈ V<sub>Z</sub></i> (assuming ideal Zener resistance <i>Z_Z = 0</i>), and <i>I<sub>L</sub> = V<sub>out</sub> / R<sub>L</sub></i>.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>2. Derivation of Allowable Series Resistor Range (R<sub>S,min</sub> and R<sub>S,max</sub>):</b><br/>"
        "To guarantee that the diode remains active without overheating or dropping out of breakdown:<br/>"
        "• <b>Maximum Allowable Resistance (R<sub>S,max</sub>):</b> Governed by the worst-case minimum input voltage (<i>V_{S,min}</i>) and maximum load demand (<i>I_{L,max}</i>). "
        "The Zener current must not drop below its minimum knee current (<i>I_{ZK}</i>):",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>R<sub>S,max</sub> = ( V<sub>S,min</sub> - V<sub>Z</sub> ) / ( I<sub>ZK</sub> + I<sub>L,max</sub> ) &nbsp;&nbsp;[Ohms]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "• <b>Minimum Allowable Resistance (R<sub>S,min</sub>):</b> Governed by the worst-case maximum input voltage (<i>V_{S,max}</i>) and minimum load demand (<i>I_{L,min}</i>, such as an open circuit <i>I_L = 0</i>). "
        "The Zener current must not exceed its maximum rated thermal current (<i>I_{ZM} = P_{Z,max} / V_Z</i>):",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>R<sub>S,min</sub> = ( V<sub>S,max</sub> - V<sub>Z</sub> ) / ( I<sub>ZM</sub> + I<sub>L,min</sub> ) &nbsp;&nbsp;[Ohms]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "For a feasible design, the engineer must select a standard resistor <i>R_S</i> satisfying: <b>R<sub>S,min</sub> ≤ R<sub>S</sub> ≤ R<sub>S,max</sub></b>.<br/>"
        "<b>3. Realistic Zener Model & Regulation Metrics:</b><br/>"
        "Accounting for finite internal dynamic Zener impedance <i>Z_Z = ΔV_Z / ΔI_Z</i>, the actual output voltage changes slightly:<br/>"
        "• <b>Line Regulation:</b> Measures the change in output voltage per volt change in input voltage:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Line Regulation = ΔV<sub>out</sub> / ΔV<sub>S</sub> = ( Z<sub>Z</sub> || R<sub>L</sub> ) / [ R<sub>S</sub> + ( Z<sub>Z</sub> || R<sub>L</sub> ) ] ≈ Z<sub>Z</sub> / R<sub>S</sub></b> &nbsp;&nbsp;(since <i>Z_Z << R_L, R_S</i>)<br/>"
        "• <b>Load Regulation:</b> Measures the change in output voltage when load current varies from no-load (<i>I_L = 0</i>) to full-load (<i>I_{L,max}</i>):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Load Regulation = ΔV<sub>out</sub> / ΔI<sub>L</sub> = - ( Z<sub>Z</sub> · R<sub>S</sub> ) / ( Z<sub>Z</sub> + R<sub>S</sub> ) ≈ - Z<sub>Z</sub></b>",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 3: LIGHT EMITTING DIODES (LEDS)
    # -------------------------------------------------------------
    story.append(Paragraph("4.3 Light Emitting Diodes (LEDs): Electroluminescence Physics", styles['SecH1']))
    story.append(Paragraph(
        "The <b>Light Emitting Diode (LED)</b> is an optoelectronic semiconductor device that converts electrical energy directly into optical radiation "
        "via <b>injection electroluminescence</b>. When forward biased, electrons from the N-conduction band and holes from the P-valence band are injected "
        "across the depletion layer. Upon meeting, excess electrons spontaneously recombine with holes, dropping from higher conduction energy states to "
        "lower valence energy states and releasing their energy in the form of optical photons.",
        styles['DocBody']
    ))

    story.append(create_figure("fig4_3_led_operation.png", "Radiative Recombination in Direct Bandgap LEDs Generating Monochromatic Photons Governed by Planck's Law", target_width=5.5*inch))

    story.append(Paragraph(
        "<b>Direct vs Indirect Bandgap Semiconductors:</b><br/>"
        "Silicon and Germanium are <i>indirect bandgap</i> semiconductors: the minimum of the conduction band does not align in crystal momentum space (k-space) "
        "with the maximum of the valence band. Recombination requires a simultaneous collision with a lattice vibration (phonon) to conserve momentum; "
        "the transition is highly improbable and almost all energy is dissipated as heat (lattice phonons), making silicon useless for light emission.<br/>"
        "LEDs are fabricated from compound <b>direct bandgap</b> semiconductors (Group III-V alloys such as Gallium Arsenide (GaAs), Gallium Nitride (GaN), "
        "and Indium Gallium Aluminum Phosphide (InGaAlP)). Conduction and valence band extrema align perfectly in momentum space, enabling direct, radiative "
        "recombination with quantum efficiencies exceeding 50% to 80%.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Mathematical Derivation of Emitted Wavelength (Planck's Law):</b><br/>"
        "The energy of an emitted photon (<i>E = h · ν = (h · c) / λ</i>) corresponds directly to the semiconductor bandgap energy <i>E_g</i>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>λ = ( h · c ) / E<sub>g</sub></b><br/>"
        "where <i>h = 6.626 × 10⁻³⁴ J·s</i> is Planck's constant, <i>c = 2.998 × 10⁸ m/s</i> is the speed of light, and <i>1 eV = 1.6022 × 10⁻¹⁹ J</i>.<br/>"
        "Expressing wavelength in nanometers (nm) and bandgap in electron-volts (eV):",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>λ [nm] = 1,239.8 / E<sub>g</sub> [eV] &nbsp;&nbsp;≈&nbsp;&nbsp; 1,240 / E<sub>g</sub></b>", styles['FormulaBox']))
    story.append(Paragraph(
        "Because bandgap determines forward operating voltage (<i>V_F ≈ E_g / q + 0.2V</i>), LEDs of different colors exhibit widely disparate forward voltages:<br/>"
        "• <b>Infrared (GaAs, E_g = 1.42 eV):</b> λ ≈ 880–940 nm, V_F ≈ 1.2–1.4 V (Used in optical seed counters and TV remote controls).<br/>"
        "• <b>Red (AlGaAs, E_g = 1.9 eV):</b> λ ≈ 660 nm, V_F ≈ 1.8–2.1 V (Crucial for plant photosynthetic chlorophyll-a excitation).<br/>"
        "• <b>Green (InGaN, E_g = 2.3 eV):</b> λ ≈ 525 nm, V_F ≈ 2.8–3.2 V.<br/>"
        "• <b>Blue (GaN / InGaN, E_g = 2.75 eV):</b> λ ≈ 450 nm, V_F ≈ 3.0–3.6 V (Chlorophyll-b excitation and stomatal opening control).<br/>"
        "• <b>White LED:</b> A royal blue GaN chip (λ = 450 nm) coated with a Cerium-doped Yttrium Aluminum Garnet (Ce:YAG) yellow phosphor.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 4: HORTICULTURAL LIGHTING ENGINEERING
    # -------------------------------------------------------------
    story.append(Paragraph("4.4 Horticultural Lighting Engineering & Photosynthetically Active Radiation (PAR)", styles['SecH1']))
    story.append(Paragraph(
        "In modern automated greenhouses—such as commercial tomato and floriculture installations in Arusha and Mount Meru foothills—"
        "artificial supplemental lighting extends photoperiods and accelerates growth. Agricultural engineers do not measure agricultural light in human visual "
        "lumens or lux (which are weighted to human eye sensitivity peaking at 555 nm green). Instead, horticultural lighting is quantified using "
        "<b>Photosynthetically Active Radiation (PAR)</b> covering the spectral band from <b>400 nm to 700 nm</b>.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Key Horticultural Photometric Metrics:</b><br/>"
        "• <b>Photosynthetic Photon Flux (PPF, μmol/s):</b> The total number of PAR photons emitted by a luminaire per second.<br/>"
        "• <b>Photosynthetic Photon Flux Density (PPFD, μmol/m²·s):</b> The number of PAR photons incident on a 1 square meter crop canopy per second. "
        "For greenhouse tomatoes, target PPFD is 300 to 500 μmol/m²·s.<br/>"
        "• <b>Daily Light Integral (DLI, mol/m²·day):</b> Total photon dose delivered per day: <i>DLI = PPFD × photoperiod (hours) × 0.0036</i>.<br/>"
        "• <b>Spectral Ratios:</b> Photosynthesis is driven primarily by two absorption peaks: <b>Chlorophyll A (430 nm blue and 662 nm red)</b> and "
        "<b>Chlorophyll B (453 nm blue and 642 nm red)</b>. Modern horticultural LED fixtures combine 450 nm Royal Blue LEDs with 660 nm Deep Red LEDs "
        "in an 80:20 red-to-blue ratio, providing 2.8 μmol/Joule efficacy—triple the efficiency of legacy High-Pressure Sodium (HPS) lamps.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 5: OPTOCOUPLERS & GALVANIC ISOLATION
    # -------------------------------------------------------------
    story.append(Paragraph("4.5 Optocouplers (Optoisolators) & Agricultural Noise Immunity", styles['SecH1']))
    story.append(Paragraph(
        "An <b>Optocoupler (Optoisolator)</b> packages an infrared LED (typically GaAs, λ = 940 nm) and an optical photosensor "
        "(photodiode, phototransistor, or photo-triac) inside a light-tight opaque enclosure, separated by a transparent dielectric insulating barrier. "
        "Signal transmission occurs strictly via light photons, providing complete <b>galvanic electrical isolation</b> (typically 2,500 V to 5,000 V RMS).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Engineering Purpose in Agricultural Automation:</b><br/>"
        "In agricultural machinery, tractors, and solar pumping installations, high-power inductive switching (solenoid valves, starter motors, inverter PWM drives) "
        "induces severe ground loops, Common-Mode Voltage (CMV) transients, and electromagnetic interference (EMI). "
        "Connecting a sensitive 3.3V microcontroller (ESP32) directly to a long field cable or motor driver risks immediate silicon burnout. "
        "Optoisolators (such as the industry-standard 4N25, PC817, and 6N137) decouple grounds entirely, guaranteeing zero ground loops.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Current Transfer Ratio (CTR):</b> The fundamental figure of merit for an optocoupler, defined as the ratio of output collector current <i>I_C</i> "
        "to input forward LED current <i>I_F</i>, expressed as a percentage:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>CTR = ( I<sub>C</sub> / I<sub>F</sub> ) × 100%</b><br/>"
        "Standard phototransistor optocouplers have CTR values between 50% and 300%. However, CTR degrades over operating lifetime (10% to 20% over 5 years) "
        "and decreases significantly at elevated operating temperatures. Agricultural circuits must be engineered with conservative overdrive factors (2× to 3×).",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 6: SCHOTTKY DIODES & SOLAR BYPASS
    # -------------------------------------------------------------
    story.append(Paragraph("4.6 Schottky Barrier Diodes & Solar PV Bypass Architectures", styles['SecH1']))
    story.append(Paragraph(
        "Unlike standard PN junction diodes that rely on a semiconductor-to-semiconductor metallurgical interface, the <b>Schottky Barrier Diode</b> "
        "is formed by depositing a metal contact (such as platinum, titanium, or molybdenum) directly onto an N-type semiconductor (typically silicon).",
        styles['DocBody']
    ))

    story.append(create_figure("fig4_4_schottky_diode.png", "Schottky Barrier Metal-Semiconductor Junction Energy Band Profile Illustrating Absence of Minority Carrier Storage", target_width=5.5*inch))

    story.append(Paragraph(
        "<b>Key Characteristics of Schottky Diodes:</b><br/>"
        "1. <b>Majority Carrier Transport:</b> Conduction occurs solely via majority electrons injected from semiconductor into metal via thermionic emission. "
        "There is virtually <b>zero minority carrier injection</b>, which means there is no minority carrier storage delay during turn-off. "
        "The reverse recovery time is negligible (<i>t_rr < 100 ps</i>), enabling ultra-high frequency operation (> 1 MHz) in switch-mode power supplies.<br/>"
        "2. <b>Ultra-Low Forward Voltage Drop:</b> The built-in barrier potential is significantly lower than a silicon PN junction: "
        "<b>V<sub>F</sub> ≈ 0.20 V to 0.45 V</b> (compared to 0.7V to 1.1V for silicon PN). Conduction losses are reduced by 50% to 70%.<br/>"
        "3. <b>Trade-offs:</b> Higher reverse leakage current (<i>I_R ≈ 10 μA to 1 mA</i>) and lower maximum reverse breakdown ratings (typically 20V to 100V).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Solar Photovoltaic Bypass Protection:</b><br/>"
        "In a solar PV module, 60 or 72 monocrystalline cells are wired in series. If bird droppings, dust, or tree branches shade a single cell, "
        "that shaded cell ceases generating electricity and turns into a high-resistance load. The remaining fully illuminated cells force current through the shaded cell, "
        "reverse-biasing it to 20V–30V. The resulting local power dissipation (<i>P = I × V ≈ 10A × 25V = 250 W</i>) causes catastrophic localized heating (hotspots) "
        "that can shatter the protective glass, melt EVA encapsulant, and cause panel fires. "
        "Connecting anti-parallel Schottky bypass diodes across strings of 20 to 24 cells provides an alternate low-resistance bypass path when a cell string is reverse biased, "
        "clamping negative voltage to just -0.4V and completely eliminating hot-spot destruction.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 6B: VARACTOR, PIN & TUNNEL DIODES
    # -------------------------------------------------------------
    story.append(Paragraph("4.6b Varactor Diodes, PIN Diodes & Special Microwave Devices", styles['SecH1']))
    story.append(Paragraph(
        "Beyond power and optoelectronic applications, several specialized diodes operate in agricultural wireless sensor networks (WSNs) and radar level sensing:<br/>"
        "<b>1. Varactor (Varicap) Diodes:</b> Designed to optimize the voltage-variable junction capacitance <i>C_j(V_R)</i> under reverse bias. "
        "As reverse voltage increases, the depletion layer widens, reducing capacitance according to <b>C_j = C_0 / (1 + V_R / V_0)^γ</b> (where γ ≈ 0.5 for abrupt junctions and γ ≈ 1 to 2 for hyperabrupt junctions). "
        "Varactors provide electronic frequency tuning in Voltage-Controlled Oscillators (VCOs) for farm LoRa transceivers (433 MHz and 868 MHz bands) and FM telemetry links without moving mechanical capacitors.<br/>"
        "<b>2. PIN Diodes:</b> Feature a wide, undoped intrinsic (I) semiconductor region sandwiched between heavily doped P and N regions. "
        "At low frequencies, it behaves like an ordinary diode. At radio frequencies (> 10 MHz), minority carrier storage prevents rectification; "
        "instead, the device acts as an almost pure, linear current-controlled RF resistor (from 10 kΩ at zero bias down to 0.5 Ω at 10 mA forward bias). "
        "In agricultural telemetry, PIN diodes act as high-speed RF transmit/receive (T/R) switches and variable attenuators in farm drone telemetry links.<br/>"
        "<b>3. Tunnel Diodes:</b> Heavily doped with impurity concentrations exceeding 10¹⁹ cm⁻³, creating a degenerate semiconductor where conduction and valence bands overlap. "
        "Under small forward bias (50 mV to 300 mV), electrons tunnel directly across the ultra-thin depletion region, producing a unique <b>Negative Differential Resistance (NDR)</b> region where current decreases as voltage increases (<i>dI/dV < 0</i>). "
        "Tunnel diodes are used in ultra-high frequency microwave oscillators for FMCW non-contact radar grain silo level measurement gauges.",
        styles['DocBody']
    ))

    story.append(create_figure("img_schottky_diode.jpg", "High-Current Industrial Schottky Barrier Rectifier Diode Used in Solar Battery Charge Controllers", target_width=5.5*inch))
    story.append(create_figure("img_zener_diode.jpg", "Precision Glass-Encapsulated Zener Voltage Reference Diode (1N4733A)", target_width=5.5*inch))

    # -------------------------------------------------------------
    # SECTION 7: COMPARATIVE ENGINEERING SPECIFICATIONS TABLE
    # -------------------------------------------------------------
    story.append(Paragraph("4.7 Engineering Comparison of Special Purpose Diodes", styles['SecH1']))
    comp_headers = ["Diode Type", "Junction Physics / Structure", "Conduction Mechanism", "Forward Drop (V_F)", "Key Agricultural System Application"]
    comp_rows = [
        ["Zener Diode", "Heavily doped Silicon PN", "Controlled reverse tunneling / avalanche", "0.7V (fwd), V_Z: 2.4V to 200V (rev)", "ADC reference voltages, tractor overvoltage clamps"],
        ["Light Emitting Diode", "Direct bandgap III-V (GaN, GaAs)", "Forward radiative recombination (photons)", "1.4V (IR) to 3.5V (Blue/UV)", "Greenhouse PAR grow lights, optical seed counters"],
        ["Photodiode", "Silicon PIN or PN with optical window", "Reverse photoconductive / photovoltaic", "0.6V (fwd), Linear I_ph vs Lux (rev)", "Solar pyranometers, crop canopy leaf area index"],
        ["Optocoupler", "IR LED + Phototransistor package", "Photon-mediated galvanic barrier", "1.2V (input LED), V_CE(sat) = 0.2V", "2.5kV isolated PLC relay drivers, inverter PWM isolation"],
        ["Schottky Diode", "Metal-Silicon barrier (Pt-Si, Mo-Si)", "Majority carrier thermionic emission", "0.25V to 0.45V (Ultra-low)", "Solar PV bypass diodes, tractor alternator rectifiers"],
        ["TVS Diode", "Large-junction P-N avalanche clamp", "Sub-nanosecond avalanche shunting", "1.0V (fwd), V_BR: 6.8V to 440V (rev)", "Lightning transient suppression on RS-485 farm LoRa"]
    ]
    story.append(create_custom_table(comp_headers, comp_rows, [1.3*inch, 1.5*inch, 1.5*inch, 1.5*inch, 1.4*inch]))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 8: WORKED NUMERICAL EXAMPLES
    # -------------------------------------------------------------
    story.append(Paragraph("4.8 Step-by-Step Worked Engineering Calculations", styles['SecH1']))

    # Example 1
    ex1_steps = [
        "1. Identify input and load parameters: Solar battery terminal voltage varies from V_{S,min} = 11.5 V (partially discharged) to V_{S,max} = 14.8 V (bulk charging). Regulated output voltage V_Z = 5.1 V. Load current varies from I_{L,min} = 10 mA to I_{L,max} = 60 mA.",
        "2. Zener diode specifications (1N4733A): V_Z = 5.1 V, P_{Z,max} = 1.0 Watt, I_{ZK} = 1.0 mA, Z_Z = 7.0 Ω.",
        "3. Compute maximum rated Zener current: I_{ZM} = P_{Z,max} / V_Z = 1.0 W / 5.1 V = 0.196 A = 196 mA.",
        "4. Calculate R_{S,max} (at minimum input and maximum load): R_{S,max} = (V_{S,min} - V_Z) / (I_{ZK} + I_{L,max}) = (11.5 V - 5.1 V) / (1.0 mA + 60 mA) = 6.4 V / 61 mA = 104.9 Ω.",
        "5. Calculate R_{S,min} (at maximum input and minimum load): R_{S,min} = (V_{S,max} - V_Z) / (I_{ZM} + I_{L,min}) = (14.8 V - 5.1 V) / (196 mA + 10 mA) = 9.7 V / 206 mA = 47.1 Ω.",
        "6. Resistor Selection & Tolerance: Choose standard 5% value R_S = 68 Ω (comfortably between 47.1 Ω and 104.9 Ω).",
        "7. Resistor Power Rating: Maximum power occurs at V_{S,max}: P_{R_S} = (V_{S,max} - V_Z)² / R_S = (14.8 - 5.1)² / 68 = (9.7)² / 68 = 94.09 / 68 = 1.38 Watts. Specify a 3-Watt or 5-Watt wirewound resistor for thermal longevity under tropical ambient conditions.",
        "8. Line Regulation Calculation: With Z_Z = 7.0 Ω, ΔV_out / ΔV_S ≈ Z_Z / R_S = 7.0 / 68 = 0.103 V/V. Over a 3.3V input shift, output shifts by only 0.34V."
    ]
    story.append(create_example(1, "Zener Voltage Regulator Design for Tractor Cab Sensor Instrumentation Rail",
                                "Design a 5.1V Zener shunt voltage regulator to supply a micro-meteorological sensor array mounted on a tractor cab in Morogoro. The tractor 12V electrical system varies between 11.5V and 14.8V. The sensor load draws between 10 mA and 60 mA. Using a 1N4733A Zener diode (V_Z = 5.1V, P_Z = 1.0W, I_ZK = 1.0 mA, Z_Z = 7.0 Ω): (a) Calculate allowable limits for series resistor R_S, (b) Select standard resistor and determine its power dissipation rating, (c) Evaluate line regulation.",
                                ex1_steps))

    # Example 2
    ex2_steps = [
        "1. Identify parameters: Applied DC supply voltage V_CC = 12.0 V; High-power Royal Blue LED forward voltage V_{F,blue} = 3.3 V; Deep Red LED forward voltage V_{F,red} = 2.1 V; String current I_LED = 350 mA = 0.35 A.",
        "2. Red String Design: Connect 4 Red LEDs in series. Total forward drop V_{string,red} = 4 × 2.1 V = 8.4 V. Voltage dropped across current-limiting resistor: V_{R,red} = V_CC - V_{string,red} = 12.0 V - 8.4 V = 3.6 V.",
        "3. Ballast Resistor Calculation (Red): R_{red} = V_{R,red} / I_LED = 3.6 V / 0.35 A = 10.28 Ω. Select standard 10.0 Ω resistor. Recomputed current: I = 3.6 V / 10.0 Ω = 360 mA.",
        "4. Resistor Power Rating (Red): P_{R,red} = I² · R = (0.36 A)² × 10.0 Ω = 1.30 Watts. Specify a 3W or 5W rated metal-oxide resistor.",
        "5. Blue String Design: Connect 3 Blue LEDs in series. Total forward drop V_{string,blue} = 3 × 3.3 V = 9.9 V. Voltage across resistor: V_{R,blue} = 12.0 V - 9.9 V = 2.1 V.",
        "6. Ballast Resistor Calculation (Blue): R_{blue} = V_{R,blue} / I_LED = 2.1 V / 0.35 A = 6.00 Ω. Select standard 6.2 Ω resistor.",
        "7. Resistor Power Rating (Blue): P_{R,blue} = (0.35 A)² × 6.2 Ω = 0.76 Watts. Specify a 2W resistor.",
        "8. Efficiency Comparison: Red string electrical efficiency = P_LED / P_total = 8.4V / 12.0V = 70.0%. Blue string efficiency = 9.9V / 12.0V = 82.5%."
    ]
    story.append(create_example(2, "Greenhouse Supplemental PAR Grow Light LED String Driver Calculations",
                                "An automated floriculture greenhouse in Arusha utilizes supplemental LED grow lights driven from a 12V DC bus. Design the ballast resistors for: (a) A string of 4 series Deep Red LEDs (V_F = 2.1V each, I = 350 mA), and (b) A string of 3 series Royal Blue LEDs (V_F = 3.3V each, I = 350 mA). Calculate resistor values, minimum power wattage ratings with a 2× safety factor, and overall electrical conversion efficiency.",
                                ex2_steps))

    # Example 3
    ex3_steps = [
        "1. Identify parameters: Photon wavelength λ = 660 nm (Chlorophyll-a deep red absorption peak); Total radiant optical power emitted P_opt = 450 mW = 0.450 W; Planck's constant h = 6.626 × 10⁻³⁴ J·s; Speed of light c = 2.998 × 10⁸ m/s; Avogadro's number N_A = 6.022 × 10²³ photons/mol.",
        "2. Compute energy of a single 660 nm photon: E_photon = (h · c) / λ = (6.626 × 10⁻³⁴ × 2.998 × 10⁸) / (660 × 10⁻⁹ m) = 1.9865 × 10⁻¹⁶ / 6.60 × 10⁻⁷ = 3.010 × 10⁻¹⁹ Joules.",
        "3. Convert photon energy to electron-volts: E_photon(eV) = 3.010 × 10⁻¹⁹ J / 1.6022 × 10⁻¹⁹ J/eV = 1.878 eV. (Matches semiconductor bandgap E_g).",
        "4. Calculate photon emission rate per second: Photon Rate = P_opt / E_photon = 0.450 J/s / (3.010 × 10⁻¹⁹ J/photon) = 1.495 × 10¹⁸ photons/second.",
        "5. Convert to Photosynthetic Photon Flux (PPF in μmol/s): PPF = [ (1.495 × 10¹⁸ photons/s) / (6.022 × 10²³ photons/mol) ] × 10⁶ μmol/mol = 2.482 μmol/s.",
        "6. Luminous Efficacy Metric: If the LED consumes 1.25 W of electrical power (I = 600 mA, V_F = 2.08 V): Horticultural Efficacy = 2.482 μmol/s / 1.25 W = 1.986 μmol/Joule."
    ]
    story.append(create_example(3, "Photosynthetic Photon Flux (PPF) Calculation from LED Spectral Radiant Power",
                                "A 660 nm deep-red AlGaAs horticultural LED chip emits 450 mW of optical radiant flux at a forward current of 600 mA and forward voltage of 2.08 V. Calculate: (a) The energy of an emitted photon in Joules and eV, (b) The total number of photons emitted per second, (c) The Photosynthetic Photon Flux (PPF) in micromoles per second (μmol/s), and (d) The photosynthetic photon efficacy in μmol/Joule.",
                                ex3_steps))

    # Example 4
    ex4_steps = [
        "1. Identify parameters: Microcontroller GPIO voltage V_GPIO = 3.3 V; GPIO source current limit I_GPIO(max) = 12 mA; Optocoupler PC817 IR LED forward drop V_F = 1.2 V; Relay coil rated voltage V_coil = 24.0 V; Relay coil resistance R_coil = 480 Ω; Relay coil current I_coil = 24.0 V / 480 Ω = 50 mA; Minimum specified CTR = 50% at 25°C.",
        "2. Thermal & Lifetime Derating for Tropical Agriculture: Operating inside a 55°C sealed field box degrades CTR by 25% (CTR_temp = 50% × 0.75 = 37.5%). LED aging over 5 years degrades CTR by another 20% (CTR_end_of_life = 37.5% × 0.80 = 30.0%).",
        "3. Design Strategy: Since phototransistor saturation current (I_C = 50 mA) would require an excessive LED input current (I_F = 50 mA / 0.30 = 167 mA, far exceeding GPIO capability), use the optocoupler to drive a secondary BJT switch (2N3904 or 2N2222) rather than driving the 50 mA coil directly.",
        "4. Optocoupler Phototransistor Pull-Down: Bias phototransistor collector with R_C = 4.7 kΩ from a 5V supply. Collector saturation current I_C = (5.0 V - 0.2 V) / 4.7 kΩ = 1.02 mA.",
        "5. Required Input LED Current: I_F = I_C / CTR_derated = 1.02 mA / 0.30 = 3.40 mA (Well within ESP32 12 mA limit).",
        "6. Input Resistor Calculation: R_in = (V_GPIO - V_F) / I_F = (3.3 V - 1.2 V) / 3.40 mA = 2.1 V / 0.0034 A = 617.6 Ω. Select standard 620 Ω resistor.",
        "7. Secondary Transistor: The optocoupler pulls down the base of a PNP transistor or feeds the base of an NPN transistor, energizing the 50 mA solenoid relay with total galvanic isolation (5,000 V_rms rating)."
    ]
    story.append(create_example(4, "Galvanically Isolated Solenoid Relay Driver Design with Optocoupler PC817",
                                "Design an optically isolated interface between an ESP32 microcontroller (3.3V logic) and a 24V DC drip irrigation hydraulic valve relay coil (R_coil = 480 Ω, I_coil = 50 mA). Using a PC817 optocoupler with minimum CTR = 50%, V_F = 1.2V, accounting for a 30% CTR degradation due to tropical field temperatures and aging: (a) Evaluate direct drive feasibility, (b) Design an opto-isolated two-stage driver, and (c) Size the input current-limiting resistor R_in for safe 3.3V GPIO operation.",
                                ex4_steps))

    # Example 5
    ex5_steps = [
        "1. Identify system parameters: Monocrystalline solar PV module with 60 series cells; Imp = 9.2 A; Vmp = 32.4 V; Open circuit Voc = 39.6 V; Three strings of 20 cells, each bridged by a bypass diode. Ambient temperature T_amb = 42°C in Chamwino, Dodoma.",
        "2. Shading Scenario: Tree foliage completely shades one cell in String 1. The remaining 19 cells in String 1 and 40 cells in Strings 2 and 3 continue generating full current I = 9.2 A.",
        "3. Unprotected Condition (No Bypass Diode): String 1 shaded cell is forced into reverse breakdown by the 59 illuminated cells: V_rev ≈ 32 V. Power dissipated in single shaded cell: P_cell = I × V_rev = 9.2 A × 32 V = 294.4 Watts! Concentrated on a 156 mm × 156 mm silicon wafer, junction temperature exceeds 220°C in under 90 seconds, igniting the backsheet and destroying the module.",
        "4. Protected Condition with Schottky Bypass Diode (15SQ045, V_F = 0.44 V @ 9.2 A): The bypass diode across String 1 turns ON, routing the full 9.2 A string current around the shaded cell string.",
        "5. Power Dissipated in Schottky Diode: P_diode = I × V_F = 9.2 A × 0.44 V = 4.05 Watts.",
        "6. Comparison with Standard Silicon PN Diode (1N5404, V_F = 1.05 V @ 9.2 A): P_silicon = 9.2 A × 1.05 V = 9.66 Watts (2.38× higher heat generation inside junction box).",
        "7. Junction Temperature Rise: For the junction box with thermal resistance R_th(j-a) = 14 °C/W: T_j(Schottky) = 42°C + (4.05 W × 14 °C/W) = 42 + 56.7 = 98.7°C (Safely below 150°C rating). T_j(Silicon) = 42°C + (9.66 W × 14 °C/W) = 42 + 135.2 = 177.2°C (Exceeds maximum silicon rating, melting junction box)."
    ]
    story.append(create_example(5, "Solar PV Bypass Diode Thermal & Power Analysis Under Shading in Dodoma",
                                "A 300W monocrystalline solar PV module installed on a rural clinic water pumping system in Chamwino, Dodoma, has 60 cells divided into three 20-cell series strings with bypass diodes. Maximum power current is Imp = 9.2 A. Shading causes String 1 to drop out. Compare thermal dissipation and junction temperatures inside the sealed junction box (T_amb = 42°C, R_th = 14 °C/W) between: (a) An unprotected shaded cell, (b) A standard silicon bypass diode (V_F = 1.05 V), and (c) A 15SQ045 Schottky barrier bypass diode (V_F = 0.44 V).",
                                ex5_steps))

    # Example 6
    ex6_steps = [
        "1. Identify parameters: Long-distance RS-485 differential communication line (A and B wires) connecting a weather station in an open sugarcane field to the central farm office (distance = 1,200 m). Line operating signal voltage = 0V to 5.0V differential. TVS diode bidirectional clamp (SMBJ5.0CA).",
        "2. TVS Diode Specifications: Reverse Standoff Voltage V_RWM = 5.0 V (diode remains high-impedance under normal operation, leakage < 5 μA); Breakdown Voltage V_BR = 6.40 V to 7.00 V (starts conducting); Maximum Clamping Voltage V_C = 9.2 V at peak pulse current I_PP = 65.2 A (10/1000 μs waveform); Peak Pulse Power P_PK = 600 Watts.",
        "3. Lightning Transient Waveform: Standard IEC 61000-4-5 surge event induces an open-circuit peak voltage spike V_surge = 2,000 V with source impedance R_source = 42 Ω.",
        "4. Peak Surge Current: I_surge(peak) ≈ (V_surge - V_C) / R_source = (2000 V - 9.2 V) / 42 Ω = 1990.8 V / 42 Ω = 47.4 A.",
        "5. TVS Capability Verification: Since 47.4 A < 65.2 A (rated I_PP), the SMBJ5.0CA easily absorbs the surge without failure.",
        "6. Clamping Effectiveness: The RS-485 transceiver (MAX485) has an absolute maximum rating of -8.0 V to +12.5 V on lines A/B. Because the TVS clamps the line tightly to 9.2 V (well below +12.5 V), the transceiver survives the lightning surge completely undamaged."
    ]
    story.append(create_example(6, "Transient Voltage Suppression (TVS) Diode Selection for Long-Range Ag-Telemetry RS-485",
                                "An automated weather station at Kilombero Sugar Estate communicates with the main irrigation control hub over a 1.2 km RS-485 differential cable. Tropical thunderstorms regularly induce 2 kV lightning transients onto the cable. Design a TVS diode protection network using bidirectional SMBJ5.0CA devices. Verify reverse standoff voltage, evaluate peak surge current for a 2,000V / 42Ω surge event, and demonstrate that transceiver absolute maximum voltage limits are preserved.",
                                ex6_steps))

    # Example 7
    ex7_steps = [
        "1. Identify RF system parameters: High-frequency LC tank oscillator operating in the 433 MHz ISM band for cattle tracking LoRa transponders across pastoral rangelands in Manyara. Inductance L = 22 nH. Desired frequency tuning range f_min = 430.0 MHz to f_max = 440.0 MHz.",
        "2. Fundamental Resonance Equation: f = 1 / [ 2π · √(L · C_total) ] &implies; C_total = 1 / [ (2π · f)² · L ].",
        "3. Calculate required total capacitance at minimum frequency (f_min = 430 MHz): C_max = 1 / [ (2π × 430 × 10⁶)² × (22 × 10⁻⁹) ] = 1 / [ (7.301 × 10¹⁸) × (2.2 × 10⁻⁸) ] = 1 / 1.606 × 10¹¹ = 6.226 pF.",
        "4. Calculate required total capacitance at maximum frequency (f_max = 440 MHz): C_min = 1 / [ (2π × 440 × 10⁶)² × (22 × 10⁻⁹) ] = 1 / [ (7.644 × 10¹⁸) × (2.2 × 10⁻⁸) ] = 1 / 1.682 × 10¹¹ = 5.945 pF.",
        "5. Circuit Stray Capacitance: PCB traces and transistor parasitics contribute fixed stray capacitance C_stray = 2.50 pF. Therefore, the varactor diode must supply: C_v(max) = 6.226 - 2.50 = 3.726 pF, and C_v(min) = 5.945 - 2.50 = 3.445 pF.",
        "6. Varactor Tuning Voltage Range: Using a hyperabrupt silicon varactor (BB135) with model C_v(V_R) = 18 pF / (1 + V_R / 0.7)⁰·⁸⁵, calculate the reverse tuning control voltage V_tune to steer the transponder frequency precisely onto the central LoRa gateway uplink channel (433.175 MHz).",
        "7. Engineering Conclusion: Varactor diodes eliminate all mechanical trimmers, providing hermetic vibration immunity when mounted on livestock collars subject to mud, bush impact, and tropical rain."
    ]
    story.append(create_example(7, "Varactor Diode Frequency Synthesis for Rangeland Cattle Tracking LoRa Transponders",
                                "A livestock telemetry collar developed at SUA Mechanization Lab uses a varactor-tuned LC tank oscillator (L = 22 nH) in its 433 MHz LoRa transceiver. Given stray circuit capacitance C_stray = 2.50 pF: (a) Determine the required resonant capacitance range to cover 430 MHz to 440 MHz, (b) Calculate the net varactor capacitance values C_v(min) and C_v(max), and (c) Discuss the reliability advantages of solid-state electronic tuning over mechanical trimmer capacitors in harsh African rangeland environments.",
                                ex7_steps))
    story.append(Paragraph("4.9 Practical Laboratory Bench Protocol: Zener Regulation & Optoisolator CTR Characterization", styles['SecH1']))
    story.append(Paragraph(
        "<b>Laboratory Objectives:</b><br/>"
        "1. Plot the reverse breakdown I-V characteristic curve of a 1N4733A (5.1V) Zener diode and extract its dynamic impedance <i>Z_Z</i>.<br/>"
        "2. Construct a shunt Zener voltage regulator and measure line regulation (ΔV_out/ΔV_in) and load regulation (ΔV_out/ΔI_L).<br/>"
        "3. Measure the forward voltage vs current curves of Red, Green, Blue, and Infrared LEDs, and calculate empirical bandgap energies.<br/>"
        "4. Characterize a PC817 optocoupler: measure input LED current <i>I_F</i> vs output collector current <i>I_C</i>, calculate CTR, and observe galvanic signal transmission on a digital storage oscilloscope.",
        styles['DocBody']
    ))

    lab4_headers = ["Step #", "Experimental Bench Procedure", "Required Test Equipment", "Expected Technical Measurement / Observation"]
    lab4_rows = [
        ["1", "Zener Reverse Curve: Connect 1N4733A Zener in reverse bias with a 220 Ω series resistor to variable bench power supply.", "Variable DC Supply (0-20V), 2× Fluke DMMs, 1N4733A", "Current remains < 1 μA until V_in reaches ≈ 5.0 V; sharp knee occurs at 5.1 V, beyond which voltage clamps tightly."],
        ["2", "Zener Impedance Extraction: Increase I_Z from 10 mA to 30 mA. Measure ΔV_Z and ΔI_Z. Compute Z_Z = ΔV_Z / ΔI_Z.", "DMM (0.1 mV resolution)", "V_Z shifts from 5.10 V to 5.24 V (ΔV = 140 mV); Calculated Z_Z = 140 mV / 20 mA = 7.0 Ω."],
        ["3", "Shunt Regulator Line Regulation: Set load resistor R_L = 470 Ω. Sweep input voltage from 8.0 V to 16.0 V in 1.0 V steps.", "DC Supply, 68 Ω 3W series resistor, DMM", "Output voltage remains between 5.08 V and 5.22 V across the entire 8V swing (Line regulation ≈ 17.5 mV/V)."],
        ["4", "Load Regulation: Fix V_in = 12.0 V. Vary R_L across 100 Ω, 220 Ω, 470 Ω, 1.0 kΩ, and open circuit. Measure V_out and I_L.", "Decade Resistance Box, DMM", "Output voltage drops by only 65 mV as load current jumps from 0 to 45 mA. Verify Zener dropout if R_L < 80 Ω."],
        ["5", "LED Forward Drop Spectroscopy: Measure forward voltage V_F at I_F = 20 mA for IR (940nm), Red (660nm), Green (525nm), and Blue (450nm).", "DMM, 5V Supply, Red/Green/Blue/IR LEDs", "IR: V_F ≈ 1.35V; Red: V_F ≈ 2.05V; Green: V_F ≈ 2.95V; Blue: V_F ≈ 3.25V. Higher photon energy corresponds to higher V_F."],
        ["6", "Optocoupler CTR: Wire PC817 input LED with 330 Ω resistor to 5V. Wire output phototransistor collector to 5V via 1.0 kΩ resistor.", "PC817 Optocoupler, DSO, Function Generator", "Measure I_F = 11.5 mA; Measure I_C = 13.8 mA. Calculate experimental CTR = (13.8 / 11.5) × 100% = 120%."],
        ["7", "Noise Immunity: Inject 50 Hz common-mode AC noise between input ground and output ground. Verify clean square wave output.", "DSO Channel 1 & 2, Noise Generator", "Zero noise coupling observed on output channel; verifies total galvanic isolation and infinite ground loop impedance."]
    ]
    story.append(create_custom_table(lab4_headers, lab4_rows, [0.8*inch, 2.4*inch, 1.8*inch, 2.2*inch]))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 10: TANZANIAN FIELD CASE STUDIES
    # -------------------------------------------------------------
    story.append(Paragraph("4.10 Tanzanian Agricultural Engineering Field Case Studies", styles['SecH1']))
    story.append(Paragraph(
        "<b>Case Study 1: Solar Pumping Array Shading Catastrophe in Dodoma Rural</b><br/>"
        "At an off-grid community water point in Chamwino District, Dodoma, a 2.2 kW solar array powering a Grundfos submersible borehole pump suffered "
        "a severe 40% drop in daily pumped water yield after six months of operation. Visual inspection of the 8-panel array revealed dark, bubbled "
        "discoloration on several solar cells in the bottom tier. Local technicians initially suspected sand abrasion. "
        "However, agricultural engineering thermal imaging revealed localized cell temperatures exceeding 145°C. "
        "Investigations discovered that dry season thorn acacia branches cast a narrow horizontal shadow across the bottom row of cells every morning. "
        "The junction boxes on the budget solar panels had been fitted with cheap general-purpose rectifier diodes (1N5408) instead of low-barrier Schottky diodes. "
        "The high forward voltage drop and extreme heat caused the diodes to fail open-circuit. With no bypass path, the shaded cells acted as resistive heaters, "
        "burning the EVA laminates. Replacing the bypass diodes with heavy-duty MBR20100CT dual Schottky diodes (100V, 20A) and pruning the overhanging "
        "acacia branches restored pump output from 18 m³/day to 42 m³/day.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Case Study 2: Precision Drip Fertigation Flow Meter Lightning Damage in Kilombero</b><br/>"
        "The Kilombero Valley experiences intense convective lightning activity during the October–December wet season. "
        "An automated drip fertigation system monitoring fertilizer injection across 150 hectares utilized paddle-wheel flow sensors equipped with "
        "Hall-effect transducers communicating over 800-meter shielded twisted-pair cables. "
        "Following a nearby thunderstorm, five flow meter input channels on the central industrial PLC were completely destroyed. "
        "Oscilloscope monitoring of the ground lines showed lightning ground potential rise (GPR) exceeding 1,500 V between the field pump house "
        "and the central office. SUA engineers redesigned the interface by installing bidirectional Transient Voltage Suppression (TVS) diodes "
        "(SMCJ15CA) and high-speed optocouplers (6N137, 10 Mbps) at every cable entry point. "
        "Over the subsequent three rainy seasons, zero flow meter or PLC port failures occurred despite dozens of direct lightning strikes on the estate perimeter.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 11: REVIEW QUESTIONS & PROBLEMS
    # -------------------------------------------------------------
    story.append(Paragraph("4.11 Comprehensive Self-Assessment & Review Questions", styles['SecH1']))
    story.append(Paragraph("<b>PART A: Conceptual & Theoretical Questions</b>", styles['SecH2']))
    q_part_a = [
        "1. Differentiate between Zener breakdown (field emission) and Avalanche breakdown (impact ionization) in terms of doping concentration, depletion width, electric field strength, and temperature coefficient.",
        "2. Why does a Zener diode with a breakdown rating of approximately 5.6 V exhibit near-zero temperature drift?",
        "3. Define the terms: Zener knee current (I_ZK), Zener test current (I_ZT), maximum rated Zener current (I_ZM), and dynamic Zener impedance (Z_Z).",
        "4. Why does an indirect bandgap semiconductor like silicon emit virtually no visible light when forward biased, whereas direct bandgap III-V semiconductors emit intense light?",
        "5. Derive Planck's wavelength equation λ = 1240 / E_g [nm] from fundamental physical constants.",
        "6. What is Photosynthetically Active Radiation (PAR)? Why do agricultural engineers quantify horticultural lighting in micromoles of photons (PPFD) rather than lumens or lux?",
        "7. Explain why royal blue (450 nm) and deep red (660 nm) LEDs are combined in horticultural luminaires instead of using monochromatic green light.",
        "8. Define Current Transfer Ratio (CTR) of an optocoupler. Explain why CTR degrades over time and at elevated ambient temperatures.",
        "9. Describe the structural difference between a Schottky barrier diode and a standard PN junction diode. Why do Schottky diodes have near-zero reverse recovery time?",
        "10. Explain the role of bypass diodes in a solar PV module. What catastrophic consequence occurs if a bypass diode fails open-circuit during partial cell shading?"
    ]
    for q in q_part_a:
        story.append(Paragraph(q, styles['DocBullet']))

    story.append(Paragraph("<b>PART B: Quantitative Analytical Problems</b>", styles['SecH2']))
    q_part_b = [
        "11. A 6.2 V Zener diode (1N4735A) has a power rating of P_Z = 1.0 W, minimum knee current I_ZK = 1.0 mA, and dynamic impedance Z_Z = 5.0 Ω. (a) Calculate the maximum safe continuous current I_ZM. (b) If reverse current increases from 10 mA to 50 mA, calculate the exact change in terminal voltage ΔV_Z and the new terminal voltage.",
        "12. A shunt Zener regulator must supply a constant 9.1 V to a precision soil moisture telemetry node. Input voltage varies from 14.0 V to 20.0 V, and load current ranges from 15 mA to 75 mA. Using a 9.1V, 1.0W Zener diode (I_ZK = 0.5 mA): (a) Calculate the minimum and maximum allowable values for series resistor R_S. (b) Select a standard 5% resistor value. (c) Determine the maximum power dissipation required for R_S.",
        "13. Calculate the semiconductor bandgap energy E_g (in eV) required to fabricate LEDs emitting at: (a) Ultraviolet (λ = 385 nm), (b) Royal Blue (λ = 450 nm), (c) Pure Green (λ = 525 nm), (d) Deep Red (λ = 660 nm), and (e) Far Red (λ = 730 nm).",
        "14. A greenhouse PAR luminaire contains 48 Deep Red LEDs (V_F = 2.15 V @ 700 mA) and 12 Royal Blue LEDs (V_F = 3.25 V @ 700 mA). If the entire luminaire is driven from a constant-current switch-mode power supply delivering 700 mA: (a) Calculate the total DC forward voltage drop across the series string. (b) Compute the total electrical power consumed. (c) If total emitted PAR photon flux is 185 μmol/s, calculate the luminaire efficacy in μmol/Joule.",
        "15. A solar module consists of 72 series monocrystalline cells delivering 9.5 A at maximum power point. A bypass diode across a 24-cell group conducts when that group is shaded. Compare power dissipation in the bypass diode if using: (a) A standard silicon diode with V_F = 1.15 V, versus (b) A Schottky barrier diode with V_F = 0.42 V. Calculate the percentage reduction in heat generation achieved by the Schottky diode."
    ]
    for q in q_part_b:
        story.append(Paragraph(q, styles['DocBullet']))

    story.append(Paragraph("<b>PART C: Agricultural Systems Design Challenges</b>", styles['SecH2']))
    q_part_c = [
        "16. <b>Solar Greenhouse Microcontroller Multi-Rail Power Supply:</b> Design a multi-output regulated DC power supply fed from a 24V solar battery bank (varying from 21.0 V to 29.5 V). The system must supply: (1) A 12.0 V rail for ventilation fan relays drawing 150 mA, and (2) A 5.0 V rail for an ESP32 microcontroller drawing 80 mA. Using Zener diodes, power pass transistors, and current-limiting resistors, synthesize the complete schematic, calculate all component ratings under maximum ambient temperature (50°C), and perform a complete thermal heatsink calculation.",
        "17. <b>Precision Optical Seed Drill Seed Drop Sensor:</b> Design a seed counting sensor for a precision maize planter operating at 8 km/h. Seeds fall through a 25 mm diameter drop tube at up to 30 seeds per second. Design an optical sensing curtain using high-speed infrared LEDs (940 nm) and silicon PIN photodiodes. Specify the optical configuration, calculate the required photodiode load resistor to achieve a rise time < 10 μs, and design a comparator circuit to output clean 0V to 3.3V logic pulses for every passing maize kernel.",
        "18. <b>Lightning & EMP Hardening for Automated Center Pivot:</b> An automated center-pivot irrigation machine in Kilombero spans 400 meters of exposed steel structure in an open valley. The main control tower houses microprocessors communicating with tower end-guns via an RS-485 serial bus. Design a comprehensive surge suppression network incorporating gas discharge tubes (GDTs), transient voltage suppression (TVS) diodes, series PPTC resettable fuses, and optoisolators. Provide the schematic, explain the multi-stage coordination sequence, and calculate peak energy absorption capability."
    ]
    for q in q_part_c:
        story.append(Paragraph(q, styles['DocBullet']))

    # -------------------------------------------------------------
    # SECTION 12: REFERENCES
    # -------------------------------------------------------------
    story.append(Spacer(1, 8))
    story.append(Paragraph("4.12 Prescribed Textbooks & Research Bibliography", styles['SecH1']))
    refs = [
        "1. Boylestad, R. L., & Nashelsky, L. (2018). <i>Electronic Devices and Circuit Theory</i> (11th ed.). Pearson Education.",
        "2. Sedra, A. S., & Smith, K. C. (2020). <i>Microelectronic Circuits</i> (8th ed.). Oxford University Press.",
        "3. Schubert, E. F. (2018). <i>Light-Emitting Diodes</i> (3rd ed.). Cambridge University Press.",
        "4. Sze, S. M., & Ng, K. K. (2007). <i>Physics of Semiconductor Devices</i> (3rd ed.). John Wiley & Sons.",
        "5. Nelson, J. (2003). <i>The Physics of Solar Cells</i>. Imperial College Press.",
        "6. Floyd, T. L. (2017). <i>Electronic Devices: Conventional Current Version</i> (10th ed.). Pearson.",
        "7. Williams, S. E., & Wilson, T. A. (2023). Introduction to Semiconductor Devices and Circuits. <i>Journal of Applied Physics</i>, 135(6), 065420."
    ]
    for r in refs:
        story.append(Paragraph(r, styles['DocBody']))

    render_pdf("AEN_214_Lecture_4_Compendium.pdf", story)

if __name__ == "__main__":
    build_lecture_4()
