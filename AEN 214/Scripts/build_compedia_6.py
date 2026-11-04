#!/usr/bin/env python3
"""
build_compedia_6.py
Comprehensive Lecture Compendium for:
LECTURE 6: FIELD EFFECT TRANSISTORS (FET)
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

def build_lecture_6():
    styles = get_custom_stylesheet()
    story = []

    # 1. Header Banner
    topics = [
        "6.1 Physical Principles & Unipolar Conduction: Electric Field Modulation of Channel Width",
        "6.2 Junction Field-Effect Transistors (JFET): Pinch-off Physics & Shockley's Square Law",
        "6.3 JFET Characteristics: Ohmic Region, Active Saturation & Dynamic Transconductance (g_m)",
        "6.4 JFET Biasing Methods: Self-Bias, Voltage Divider Bias & Graphical Transfer Curve Q-Point",
        "6.5 Metal-Oxide-Semiconductor FETs (MOSFET): The Silicon Dioxide Insulating Gate Barrier",
        "6.6 Depletion-Mode MOSFETs (D-MOSFET): Dual-Mode Operation & Dual-Gate Agro Mixers",
        "6.7 Enhancement-Mode MOSFETs (E-MOSFET): Inversion Layer Threshold & Square-Law Equations",
        "6.8 Power MOSFET Architecture (DMOS/Trench): Conduction Resistance R_DS(on) & Heatsinking",
        "6.9 Gate Charge Dynamics (Q_g), Miller Plateau & High-Speed Microcontroller Gate Drivers",
        "6.10 Electrostatic Discharge (ESD) Protection & Safe Handling Protocols for Fragile Oxides",
        "6.11 Practical Laboratory Bench Protocol: JFET Transfer Tracing & MOSFET PWM Motor Driver",
        "6.12 Tanzanian Agricultural Field Case Studies: Singida Solar Pumping & Morogoro Soil EC Probes",
        "6.13 Comprehensive Self-Assessment: Conceptual, Quantitative & System Design Problems"
    ]
    story.extend(create_banner_header(6, "Field Effect Transistors (FET) & Power Drivers", topics))

    # -------------------------------------------------------------
    # SECTION 1: PHYSICAL PRINCIPLES & UNIPOLAR TRANSPORT
    # -------------------------------------------------------------
    story.append(Paragraph("6.1 Physical Principles of Unipolar Field-Effect Transistors", styles['SecH1']))
    story.append(Paragraph(
        "The <b>Field-Effect Transistor (FET)</b> is a three-terminal semiconductor device in which output current is controlled by an electrostatic "
        "electric field created by an applied input voltage. In stark contrast to the BJT—which is a current-controlled, bipolar device requiring continuous "
        "base drive current and relying on both electron and hole transport—the FET is a <b>voltage-controlled, unipolar device</b>. "
        "Current conduction is carried exclusively by majority charge carriers (electrons in N-channel devices, holes in P-channel devices) drifting through "
        "a conducting semiconductor channel.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Fundamental Engineering Advantages of FETs in Agricultural Systems:</b><br/>"
        "1. <b>Extremely High Input Impedance:</b> Because the control gate is either a reverse-biased PN junction (in JFETs: <i>R_in ≈ 10⁸ to 10¹⁰ Ω</i>) "
        "or completely isolated by an ultra-pure Silicon Dioxide (SiO₂) dielectric layer (in MOSFETs: <i>R_in ≈ 10¹² to 10¹⁵ Ω</i>), the steady-state gate current "
        "is virtually zero (picoamperes to femtoamperes). This eliminates loading errors when interfacing high-impedance agricultural transducers, such as "
        "glass-electrode soil pH sensors, capacitive grain moisture probes, and piezoelectric vibration monitors.<br/>"
        "2. <b>Absence of Thermal Runaway:</b> Majority carrier mobility decreases as crystal temperature rises due to enhanced acoustic phonon lattice scattering. "
        "Consequently, the channel on-resistance (<i>R_DS(on)</i>) of power MOSFETs exhibits a <b>positive temperature coefficient</b>. "
        "If a localized hotspot develops or multiple power MOSFETs are paralleled to drive high-current agricultural pumps, hot transistors naturally increase "
        "their resistance, shedding current and forcing cooler parallel devices to share the load. Current hogging and thermal runaway are physically impossible.<br/>"
        "3. <b>Zero Minority Carrier Storage Delay:</b> Because conduction involves no minority carrier injection or recombination, FETs switch off in nanoseconds, "
        "enabling high-frequency (20 kHz to 500 kHz) pulse-width modulation (PWM) in solar water pump motor inverters with negligible switching losses.<br/>"
        "4. <b>Lower Thermal Noise:</b> The absence of carrier recombination in the channel results in significantly lower noise figures than BJTs, ideal for sensitive preamplifiers.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 2: JUNCTION FET (JFET) PHYSICS
    # -------------------------------------------------------------
    story.append(Paragraph("6.2 Junction Field-Effect Transistor (JFET) Physics & Shockley's Law", styles['SecH1']))
    story.append(Paragraph(
        "An N-channel JFET consists of a bar of N-type silicon with ohmic electrical contacts at both ends designated as the <b>Drain (D)</b> "
        "and <b>Source (S)</b>. Heavily doped P⁺ regions are diffused on opposing sides of the channel and connected together to form the <b>Gate (G)</b>. "
        "Under standard operation, the gate-source junction is maintained in reverse bias (<i>V_GS ≤ 0</i>).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Channel Constriction & Pinch-Off Phenomenon:</b><br/>"
        "When a positive drain-source voltage <i>V_DS</i> is applied, electrons flow from source to drain. This drain current <i>I_D</i> produces an ohmic voltage "
        "drop along the channel length. Consequently, the reverse bias across the PN junction is greatest near the drain end (<i>V_GD = V_GS - V_DS</i>) "
        "and smallest near the source. As <i>V_DS</i> increases, the depletion layers widen non-symmetrically, constricting the conducting channel most severely at the drain end.<br/>"
        "When <i>V_DS</i> reaches the critical threshold where depletion layers almost touch, the device reaches <b>Pinch-Off</b> (<i>V_DS = V_P - V_GS</i>). "
        "Beyond pinch-off, further increases in <i>V_DS</i> do not increase current; rather, the channel saturation current remains constant at a level determined strictly by <i>V_GS</i>.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Shockley's Transconductance Equation in Saturation:</b><br/>"
        "In the saturation (pinch-off) region where <i>V_DS ≥ V_GS - V_P</i>, drain current is governed by the celebrated parabolic square-law relationship:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>I<sub>D</sub> = I<sub>DSS</sub> · [ 1 - ( V<sub>GS</sub> / V<sub>P</sub> ) ]² &nbsp;&nbsp;[Amperes]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where the primary JFET device parameters are defined as follows:<br/>"
        "• <b>I<sub>DSS</sub></b> is the Drain-to-Source Saturation Current with Gate Shorted to Source (<i>V_GS = 0</i>), representing the maximum drain current the JFET can conduct in the active region (typically 2 mA to 20 mA for small-signal devices like 2N5457).<br/>"
        "• <b>V<sub>P</sub> (or V<sub>GS(off)</sub>)</b> is the Pinch-off Voltage (negative for N-channel, positive for P-channel), at which the depletion layers completely pinch off the channel, extinguishing drain current to zero (<i>I_D = 0</i>).<br/>"
        "• <b>Dynamic Transconductance (g<sub>m</sub>):</b> Differentiating Shockley's equation with respect to <i>V_GS</i> yields the forward transconductance:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>g<sub>m</sub> = ( dI<sub>D</sub> / dV<sub>GS</sub> ) = [ ( 2 · I<sub>DSS</sub> ) / |V<sub>P</sub>| ] · [ 1 - ( V<sub>GS</sub> / V<sub>P</sub> ) ] = g<sub>m0</sub> · [ 1 - ( V<sub>GS</sub> / V<sub>P</sub> ) ] &nbsp;&nbsp;[Siemens (S)]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <b>g<sub>m0</sub> = ( 2 · I<sub>DSS</sub> ) / |V<sub>P</sub>|</b> is the maximum transconductance at <i>V_GS = 0</i>.",
        styles['DocBody']
    ))

    story.append(create_figure("fig6_2_jfet_characteristics.png", "JFET Drain Output Characteristics Family (I_D vs V_DS) and Universal Parabolic Transfer Curve (I_D vs V_GS)", target_width=5.5*inch))

    # -------------------------------------------------------------
    # SECTION 3: JFET BIASING NETWORKS
    # -------------------------------------------------------------
    story.append(Paragraph("6.3 JFET DC Biasing Methods & Mathematical Formulations", styles['SecH1']))
    story.append(Paragraph(
        "Because JFETs require a negative gate-source voltage (<i>V_GS < 0</i>) for N-channel devices, biasing circuits must generate this negative potential "
        "without requiring a separate negative power supply rail.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>1. JFET Self-Bias:</b><br/>"
        "Self-bias uses a single source resistor <i>R_S</i> connected between source and ground. The gate is tied to ground through a large resistor <i>R_G</i> (1 MΩ to 10 MΩ). "
        "Since gate current is zero (<i>I_G = 0</i>), the gate DC voltage is exactly zero: <i>V_G = 0 V</i>.<br/>"
        "When drain current <i>I_D</i> flows through the source resistor, it establishes a positive source potential: <b>V<sub>S</sub> = I<sub>D</sub> · R<sub>S</sub></b>.<br/>"
        "The resulting gate-to-source voltage is automatically negative:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>V<sub>GS</sub> = V<sub>G</sub> - V<sub>S</sub> = 0 - I<sub>D</sub> · R<sub>S</sub> = - I<sub>D</sub> · R<sub>S</sub> &nbsp;&nbsp;[Volts]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "Equating this linear bias line with Shockley's parabolic equation yields a quadratic equation in <i>I_D</i>, which can be solved analytically or graphically.<br/>"
        "<b>2. JFET Voltage Divider Bias:</b><br/>"
        "To achieve superior Q-point stability against variations in device parameters (<i>I_DSS</i> and <i>V_P</i>), resistors <i>R_1</i> and <i>R_2</i> establish a positive gate voltage: "
        "<b>V<sub>G</sub> = V<sub>DD</sub> · [ R<sub>2</sub> / (R_1 + R_2) ]</b>.<br/>"
        "The gate-source voltage becomes: <b>V<sub>GS</sub> = V<sub>G</sub> - I<sub>D</sub> · R<sub>S</sub></b>.<br/>"
        "Because <i>V_G</i> is positive, a larger source resistor <i>R_S</i> can be used, creating strong negative DC feedback that stabilizes <i>I_D</i> against temperature and manufacturing batch spreads.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 4: MOSFET ARCHITECTURES (D-MOSFET & E-MOSFET)
    # -------------------------------------------------------------
    story.append(Paragraph("6.4 MOSFET Architectures: Depletion vs Enhancement Modes", styles['SecH1']))
    story.append(Paragraph(
        "The <b>Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET)</b>, also termed the Insulated-Gate FET (IGFET), replaces the reverse-biased PN junction "
        "with an ultra-thin layer of Silicon Dioxide (SiO₂, thickness 5 nm to 50 nm) insulating the gate metal/polysilicon from the semiconductor channel. "
        "This yields an almost infinite DC input resistance (<i>R_in > 10¹² Ω</i>) and eliminates gate leakage entirely.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>1. Depletion-Enhancement MOSFET (D-MOSFET):</b><br/>"
        "Fabricated with a physical N-type channel connecting drain and source. When <i>V_GS < 0</i>, negative gate voltage repels channel electrons, operating in "
        "<b>Depletion Mode</b> governed by Shockley's equation. When <i>V_GS > 0</i>, positive gate voltage attracts additional electrons from the substrate, enhancing channel conductivity in "
        "<b>Enhancement Mode</b>. D-MOSFETs are unique in that they can operate with zero gate bias (<i>V_GS = 0</i>), simplifying RF amplifier biasing in agricultural drone telemetry.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>2. Enhancement-Only MOSFET (E-MOSFET):</b><br/>"
        "Fabricated with <b>no physical channel</b> between N⁺ drain and N⁺ source diffusions; they are separated by a P-type substrate. "
        "At <i>V_GS = 0</i>, the device is completely OFF (open circuit). Conduction requires applying a positive gate voltage exceeding the "
        "<b>Gate Threshold Voltage (V<sub>GS(th)</sub>)</b>, typically 1.5 V to 4.0 V (or 0.8 V to 1.8 V for logic-level MOSFETs).<br/>"
        "When <i>V_GS > V_GS(th)</i>, the electric field pulls minority electrons from the P-substrate to the silicon-oxide interface, forming an "
        "<b>N-type Inversion Layer</b> that bridges drain and source.<br/>"
        "In the saturation region (<i>V_DS ≥ V_GS - V_GS(th)</i>), drain current is governed by the universal E-MOSFET square law:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>I<sub>D</sub> = k · [ V<sub>GS</sub> - V<sub>GS(th)</sub> ]² &nbsp;&nbsp;[Amperes]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <b>k = ( μ<sub>n</sub> · C<sub>ox</sub> · W ) / ( 2 · L )</b> is the conduction parameter (A/V²), determined from a known datasheet point: "
        "<b>k = I<sub>D(on)</sub> / [ V<sub>GS(on)</sub> - V<sub>GS(th)</sub> ]²</b>.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 5: POWER MOSFETS & MOTOR DRIVER CIRCUITS
    # -------------------------------------------------------------
    story.append(Paragraph("6.5 Power MOSFETs, Gate Charge Dynamics & Motor Drivers", styles['SecH1']))
    story.append(Paragraph(
        "In agricultural machinery, standard planar MOSFETs are unsuitable for high-current switching due to excessive on-resistance. "
        "<b>Power MOSFETs</b> utilize vertical DMOS (Double-Diffused MOS) or Trench-Gate architectures where current flows vertically from the top surface "
        "to a metallic substrate drain on the bottom of the die. This packs millions of parallel micro-cells into a single chip, driving the "
        "on-resistance down to milliohms: <b>R<sub>DS(on)</sub> ≈ 1.5 mΩ to 25 mΩ</b>.",
        styles['DocBody']
    ))

    story.append(create_figure("fig6_4_power_mosfet_motor_driver.png", "Power MOSFET Low-Side PWM Motor Driver with Gate Driver Resistor, Pull-Down, and Inductive Freewheeling Snubber", target_width=5.5*inch))

    story.append(Paragraph(
        "<b>1. Conduction Loss & Thermal Calculation:</b><br/>"
        "In steady-state conduction, power dissipation is pure I²R resistive heating:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>P<sub>cond</sub> = I<sub>D,rms</sub>² · R<sub>DS(on)</sub>(T<sub>j</sub>)</b><br/>"
        "Because <i>R_DS(on)</i> increases by approximately 80% to 100% as junction temperature rises from 25°C to 125°C, engineers must use the "
        "elevated high-temperature resistance: <i>R_DS(on)(125°C) ≈ 1.8 · R_DS(on)(25°C)</i> in thermal sizing calculations.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>2. Gate Charge Dynamics (Q<sub>g</sub>) & The Miller Plateau:</b><br/>"
        "Although the DC gate current is zero, the MOSFET gate presents significant input capacitances: Gate-to-Source (<i>C_gs</i>) and Gate-to-Drain (<i>C_gd</i>, the Miller capacitance). "
        "To switch the MOSFET ON in time <i>t_sw</i>, the gate driver must source a dynamic peak charging current:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>I<sub>gate(peak)</sub> = Q<sub>g</sub> / t<sub>sw</sub></b><br/>"
        "During turn-on, the gate voltage pauses at the <b>Miller Plateau (V<sub>plateau</sub>)</b> while drain-to-gate capacitance <i>C_gd</i> discharges from <i>V_DS</i> down to near zero. "
        "During this interval, the transistor experiences simultaneous high voltage and high current, generating substantial switching loss: "
        "<b>P<sub>sw</sub> = (1/2) · V<sub>DS</sub> · I<sub>D</sub> · ( t<sub>r</sub> + t<sub>f</sub> ) · f<sub>PWM</sub></b>.<br/>"
        "Directly driving a power MOSFET from a microcontroller GPIO pin (limited to 10-20 mA) causes prolonged switching times (> 1 μs), inducing massive switching losses. "
        "Dedicated gate driver ICs (e.g., TC4420, IR2110) capable of delivering 2A to 6A peak gate currents are mandatory for PWM frequencies > 10 kHz.",
        styles['DocBody']
    ))

    story.append(create_figure("img_mosfet_power.jpg", "High-Current N-Channel Power MOSFET in TO-220 Package (IRF3205: 55V, 110A, 8 mΩ) Used in Solar Inverters", target_width=5.5*inch))
    story.append(create_figure("fig_real_mosfet.png", "Power MOSFET Module showing Substrate Drain Tab and Heavy Copper Terminals for Solar Pump Drivers", target_width=5.5*inch))
    story.append(create_figure("img_solar_water_pump.jpg", "Photovoltaic Solar Borehole Pumping Installation in Chamwino, Dodoma Driven by Power MOSFET Inverter", target_width=5.5*inch))

    # -------------------------------------------------------------
    # SECTION 6.5b: CMOS TRANSMISSION GATES & ANALOG MULTIPLEXERS
    # -------------------------------------------------------------
    story.append(Paragraph("6.5b CMOS Transmission Gates & Agricultural Data Acquisition Multiplexers", styles['SecH1']))
    story.append(Paragraph(
        "<b>1. Complementary MOS (CMOS) Transmission Gate:</b><br/>"
        "In precision agriculture data loggers, a single microcontroller ADC must sample dozens of field sensors (soil moisture at 10cm, 20cm, 50cm, and 100cm depths, solar radiation, soil temperature, leaf wetness). "
        "A single NMOS transistor cannot pass analog signals near the positive supply rail without threshold drop (<i>V_out ≤ V_DD - V_{th}</i>), and a single PMOS transistor cannot pass signals near ground (<i>V_out ≥ |V_{th}|</i>).<br/>"
        "The <b>CMOS Transmission Gate (Analog Bilateral Switch)</b> connects an N-channel MOSFET and a P-channel MOSFET in parallel, controlled by complementary gate clocks (<i>Φ</i> and <i>/Φ</i>). "
        "When active, NMOS conducts low signal levels cleanly to ground (0V) while PMOS conducts high signal levels cleanly to the positive rail (<i>V_DD</i>). "
        "The composite on-resistance remains remarkably flat (<b>R<sub>on</sub> ≈ 50 Ω to 200 Ω</b> across the entire 0V to <i>V_DD</i> span), providing full <b>rail-to-rail analog signal transmission</b> with zero distortion.<br/>"
        "<b>2. Agro-Telemetry Multiplexing:</b> Standard ICs such as the CD4051B (8-channel analog multiplexer) use CMOS transmission gates to sequentially route multiple soil sensors to a single ESP32 analog pin, drastically reducing logger cost and board real estate.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 6: ESD PROTECTION & HANDLING PROTOCOLS
    # -------------------------------------------------------------
    story.append(Paragraph("6.6 Electrostatic Discharge (ESD) Hazards & Handling Protocols", styles['SecH1']))
    story.append(Paragraph(
        "The Silicon Dioxide gate insulator in modern MOSFETs is extraordinarily thin—often less than 20 nanometers. "
        "The dielectric breakdown strength of SiO₂ is approximately <i>10 MV/cm (1 V/nm)</i>, meaning that a gate-source voltage exceeding <b>V<sub>GS(max)</sub> = ±20 V</b> "
        "will cause instantaneous dielectric punch-through, puncturing the oxide and permanently shorting the gate to the channel.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "In dry agricultural regions of Tanzania (such as Dodoma and Shinyanga during the dry season), walking across a nylon workshop carpet or handling dry plastic grain bags "
        "generates human body static voltages exceeding <b>10,000 V to 25,000 V</b>. Touching an unprotected MOSFET gate terminal discharges this charge, "
        "vaporizing the microscopic gate oxide in less than a nanosecond.<br/>"
        "<b>Standard Protective Measures:</b><br/>"
        "• <b>Internal Zener Gate Protection:</b> Modern agricultural sensor MOSFETs incorporate back-to-back monolithic Zener diodes (clamped at ±15V) between gate and source.<br/>"
        "• <b>External Pull-Down Resistor:</b> Always solder a 10 kΩ to 100 kΩ pull-down resistor directly across gate-source terminals to bleed off accumulated static charge.<br/>"
        "• <b>Workshop ESD Protocols:</b> Grounded antistatic wrist straps, conductive ESD foam for component transport, and grounded soldering iron tips.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 7: COMPARATIVE SPECIFICATIONS TABLE
    # -------------------------------------------------------------
    story.append(Paragraph("6.7 Engineering Comparison: JFET vs MOSFET vs BJT", styles['SecH1']))
    comp_headers = ["Parameter / Metric", "BJT (e.g. 2N3904 / TIP31C)", "JFET (e.g. 2N5457)", "E-MOSFET (e.g. 2N7000 / IRF3205)"]
    comp_rows = [
        ["Control Mechanism", "Current-controlled (I_B)", "Voltage-controlled (V_GS)", "Voltage-controlled (V_GS)"],
        ["Conduction Mode", "Bipolar (Majority + Minority)", "Unipolar (Majority carriers)", "Unipolar (Majority carriers)"],
        ["Input Impedance", "Low to Moderate (1 kΩ to 10 kΩ)", "High (10⁸ to 10¹⁰ Ω)", "Extremely High (10¹² to 10¹⁵ Ω)"],
        ["Gate/Base Current", "Continuous DC: I_B = I_C / β", "Zero DC (Reverse junction leakage)", "Zero DC (Insulated dielectric)"],
        ["Governing Equation", "Exponential: I_C = I_S · exp(V_BE/V_T)", "Parabolic: I_D = I_DSS(1 - V_GS/V_P)²", "Square-Law: I_D = k(V_GS - V_th)²"],
        ["Temperature Coefficient", "Negative (V_BE drops, risk of runaway)", "Negative on I_D (Self-stabilizing)", "Positive on R_DS(on) (Zero runaway risk)"],
        ["Switching Speed", "Moderate (Storage time delay)", "Fast (No storage charge)", "Ultra-Fast (10 ns to 50 ns)"],
        ["Agricultural Application", "Linear preamps, relay drivers (< 1A)", "High-Z soil pH buffers, electrometer probes", "High-power PWM solar pumps, inverters (> 50A)"]
    ]
    story.append(create_custom_table(comp_headers, comp_rows, [1.5*inch, 1.8*inch, 1.8*inch, 1.9*inch]))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 8: WORKED NUMERICAL EXAMPLES
    # -------------------------------------------------------------
    story.append(Paragraph("6.8 Step-by-Step Worked Engineering Calculations", styles['SecH1']))

    # Example 1
    ex1_steps = [
        "1. Identify JFET device parameters: Drain saturation current I_DSS = 10.0 mA; Pinch-off voltage V_P = -4.0 V. Self-bias circuit with supply V_DD = 18.0 V, drain resistor R_D = 1.8 kΩ, source resistor R_S = 470 Ω, and gate resistor R_G = 1.0 MΩ.",
        "2. Formulate Bias Line Equation: V_GS = - I_D · R_S = - I_D · (470 Ω).",
        "3. Substitute into Shockley's Equation: I_D = I_DSS · [ 1 - (V_GS / V_P) ]² = 0.010 · [ 1 - (- 470 · I_D / -4.0) ]² = 0.010 · [ 1 - 117.5 · I_D ]².",
        "4. Expand the quadratic equation: I_D = 0.010 · [ 1 - 235 · I_D + 13806.25 · I_D² ] = 0.010 - 2.35 · I_D + 138.06 · I_D².",
        "5. Rearrange into standard quadratic form: 138.06 · I_D² - 3.35 · I_D + 0.010 = 0.",
        "6. Solve for I_D using quadratic formula: a = 138.06, b = -3.35, c = 0.010. Discriminant = b² - 4ac = (-3.35)² - 4(138.06)(0.010) = 11.2225 - 5.5224 = 5.7001. √Disc = 2.3875.",
        "7. Roots: I_D = (3.35 ± 2.3875) / (2 × 138.06) = (3.35 ± 2.3875) / 276.12. Root 1: I_D = 5.7375 / 276.12 = 20.78 mA (Extraneous root, exceeds I_DSS). Root 2 (Physical): I_D = 0.9625 / 276.12 = 0.003486 A = 3.49 mA.",
        "8. Compute Q-Point Voltages: V_GSQ = - I_DQ · R_S = - (3.49 mA) × 470 Ω = - 1.640 V. (Verify: -1.64V is between 0V and -4.0V).",
        "9. Drain-Source Voltage: V_DSQ = V_DD - I_DQ · (R_D + R_S) = 18.0 V - [ 3.49 mA × (1800 + 470) ] = 18.0 V - [ 3.49 mA × 2270 Ω ] = 18.0 V - 7.92 V = 10.08 V.",
        "10. Verify Active Saturation: Check V_DSQ ≥ V_GSQ - V_P: V_GSQ - V_P = -1.64 V - (-4.0 V) = +2.36 V. Since 10.08 V >> 2.36 V, the JFET operates deep in the pinch-off saturation region."
    ]
    story.append(create_example(1, "Analytical Q-Point Solution of JFET Self-Bias Soil Moisture Preamp",
                                "An N-channel JFET in an acoustic leaf moisture preamplifier has I_DSS = 10.0 mA and V_P = -4.0 V. The self-bias circuit has V_DD = 18.0 V, R_D = 1.8 kΩ, R_S = 470 Ω, and R_G = 1.0 MΩ. (a) Derive the exact quadratic equation for drain current and calculate the physical quiescent operating point (I_DQ, V_GSQ, V_DSQ), and (b) Confirm that the transistor is operating in the pinch-off saturation region.",
                                ex1_steps))

    # Example 2
    ex2_steps = [
        "1. Identify device parameters from Example 1: I_DSS = 10.0 mA, V_P = -4.0 V, V_GSQ = -1.64 V, I_DQ = 3.49 mA. AC drain load resistor R_L = 10.0 kΩ; Drain resistor R_D = 1.8 kΩ.",
        "2. Compute maximum transconductance at V_GS = 0: g_m0 = (2 · I_DSS) / |V_P| = (2 × 0.010 A) / 4.0 V = 0.020 / 4.0 = 0.005 S = 5.0 mS = 5,000 μS.",
        "3. Compute operating transconductance at Q-point: g_m = g_m0 · [ 1 - (V_GSQ / V_P) ] = 5.0 mS × [ 1 - (-1.64 / -4.0) ] = 5.0 mS × [ 1 - 0.410 ] = 5.0 mS × 0.590 = 2.95 mS = 2.95 × 10⁻³ S.",
        "4. Effective AC Drain Load: r_d_load = R_D || R_L = (1.8 kΩ × 10.0 kΩ) / (1.8 + 10.0) = 18.0 / 11.8 = 1.525 kΩ = 1,525 Ω.",
        "5. Voltage Gain with Bypassed Source Resistor: A_v = - g_m · (R_D || R_L) = - (2.95 × 10⁻³ S) × 1,525 Ω = - 4.50 V/V. (The negative sign denotes 180° phase inversion).",
        "6. Voltage Gain with Unbypassed Source Resistor (R_S = 470 Ω): A_{v,unbypassed} = - (g_m · r_d_load) / (1 + g_m · R_S) = - 4.50 / [ 1 + (0.00295 × 470) ] = - 4.50 / [ 1 + 1.3865 ] = - 4.50 / 2.3865 = - 1.886 V/V."
    ]
    story.append(create_example(2, "Small-Signal JFET AC Amplifier Gain & Transconductance Analysis",
                                "For the JFET circuit analyzed in Example 1, determine: (a) Maximum transconductance g_m0, (b) Quiescent transconductance g_m at V_GSQ = -1.64 V, (c) Small-signal AC voltage gain A_v with source resistor R_S fully bypassed driving a 10 kΩ load, and (d) AC voltage gain if bypass capacitor C_S is removed.",
                                ex2_steps))

    # Example 3
    ex3_steps = [
        "1. Identify datasheet specifications (2N7000 N-channel E-MOSFET): Threshold voltage V_GS(th) = 2.0 V; Known test point: I_D(on) = 500 mA at V_GS(on) = 10.0 V.",
        "2. Compute conduction parameter k: k = I_D(on) / [ V_GS(on) - V_GS(th) ]² = 0.50 A / [ 10.0 V - 2.0 V ]² = 0.50 / (8.0)² = 0.50 / 64 = 0.0078125 A/V² = 7.813 mA/V².",
        "3. Voltage Divider Bias Circuit: Supply V_DD = 12.0 V; Resistors: R_1 = 100 kΩ, R_2 = 100 kΩ; Drain resistor R_D = 470 Ω; Source connected directly to ground (R_S = 0).",
        "4. Calculate Gate Voltage: Since gate current I_G = 0: V_G = V_DD · [ R_2 / (R_1 + R_2) ] = 12.0 V × [ 100 k / 200 k ] = 6.0 V.",
        "5. Gate-Source Voltage: V_GS = V_G - V_S = 6.0 V - 0 V = 6.0 V. Since V_GS = 6.0 V > V_GS(th) = 2.0 V, the transistor is actively conducting.",
        "6. Calculate Drain Current in Saturation: I_D = k · [ V_GS - V_GS(th) ]² = 0.0078125 A/V² × [ 6.0 V - 2.0 V ]² = 0.0078125 × (4.0)² = 0.0078125 × 16 = 0.125 A = 125 mA.",
        "7. Compute Drain-Source Voltage: V_DS = V_DD - I_D · R_D = 12.0 V - (0.125 A × 470 Ω) = 12.0 V - 58.75 V = - 46.75 V! (PHYSICAL IMPOSSIBILITY &implies; Transistor cannot be in saturation!).",
        "8. Resolution (Ohmic Triode Region Operation): Because the calculated V_DS is negative, the transistor is driven into hard saturation/ohmic region where V_DS is collapsed. In the ohmic region, 2N7000 acts as a closed switch with on-resistance R_DS(on) ≈ 2.0 Ω. Actual drain current is limited by R_D: I_D = 12.0 V / (470 + 2 Ω) = 25.4 mA, and V_DS = 25.4 mA × 2 Ω = 0.051 V."
    ]
    story.append(create_example(3, "Enhancement-Mode MOSFET Conduction Parameter & Triode Region Verification",
                                "A 2N7000 E-MOSFET has V_GS(th) = 2.0 V and conducts I_D(on) = 500 mA at V_GS(on) = 10.0 V. (a) Calculate the conduction parameter k. (b) The transistor is biased with V_DD = 12.0 V, R_1 = R_2 = 100 kΩ, and R_D = 470 Ω. Test whether the assumption of saturation is valid and determine the actual operating region, drain current, and drain voltage.",
                                ex3_steps))

    # Example 4
    ex4_steps = [
        "1. Identify system parameters: 24V DC submersible solar pump motor in Singida drawing continuous rated current I_motor = 16.0 A. Switched via PWM at frequency f = 25 kHz. Power MOSFET: IRF3205 (55V, 110A, TO-220 package).",
        "2. Thermal & Electrical Specifications: R_DS(on) = 8.0 mΩ at 25°C. In high-temperature pump enclosure (T_amb = 45°C), junction operates at ~100°C. Temperature derating factor for silicon R_DS(on) at 100°C is 1.6×: R_DS(on)(100°C) = 8.0 mΩ × 1.6 = 12.8 mΩ = 0.0128 Ω.",
        "3. Conduction Power Loss: P_cond = I_motor² · R_DS(on)(100°C) = (16.0 A)² × 0.0128 Ω = 256 × 0.0128 = 3.277 Watts.",
        "4. Switching Dynamics: Gate driver delivers 1.5 A peak current, achieving rise time t_r = 35 ns and fall time t_f = 45 ns. Total switching transition time t_sw = t_r + t_f = 80 ns = 80 × 10⁻⁹ s.",
        "5. Switching Power Loss: P_sw = (1/2) · V_DS · I_D · (t_r + t_f) · f_PWM = 0.5 × 24.0 V × 16.0 A × (80 × 10⁻⁹ s) × (25,000 Hz) = 192 × (2.0 × 10⁻³ s/s) = 0.384 Watts.",
        "6. Total Transistor Power Dissipation: P_total = P_cond + P_sw = 3.277 W + 0.384 W = 3.661 Watts.",
        "7. Heatsink Thermal Resistance Calculation: Maximum junction temperature T_j(max) = 150°C. Ambient inside enclosure T_amb = 45°C. θ_jc = 0.75 °C/W; θ_cs = 0.50 °C/W. Total allowable thermal resistance: θ_total = (T_j(max) - T_amb) / P_total = (150 - 45) / 3.661 W = 105 / 3.661 = 28.68 °C/W. Applying a 30% thermal safety factor: θ_total(design) = 28.68 × 0.70 = 20.08 °C/W.",
        "8. Heatsink Selection: θ_sa = θ_total(design) - θ_jc - θ_cs = 20.08 - 0.75 - 0.50 = 18.83 °C/W. Specify an aluminum heatsink with θ_sa ≤ 15.0 °C/W."
    ]
    story.append(create_example(4, "Power MOSFET Conduction, Switching & Thermal Heatsink Sizing for 24V Solar Pump PWM",
                                "A 24V DC solar water pumping motor draws 16.0 A continuous current and is modulated at 25 kHz using an IRF3205 N-channel power MOSFET (R_DS(on) = 8 mΩ at 25°C, rising to 12.8 mΩ at operating temperature). Switching transition times are t_r = 35 ns and t_f = 45 ns. Given T_amb = 45°C, θ_jc = 0.75 °C/W, θ_cs = 0.50 °C/W, and T_j(max) = 150°C: (a) Calculate conduction power loss, (b) Calculate switching power loss, (c) Determine total power dissipation, and (d) Size the heatsink with a 30% thermal safety factor.",
                                ex4_steps))

    # Example 5
    ex5_steps = [
        "1. Identify parameters: Power MOSFET total gate charge Q_g = 146 nC (nano-Coulombs) at V_GS = 10.0 V; Desired turn-on switching speed t_on = 50 ns = 50 × 10⁻⁹ s.",
        "2. Required Peak Gate Charging Current: I_gate(peak) = Q_g / t_on = (146 × 10⁻⁹ C) / (50 × 10⁻⁹ s) = 2.92 Amperes.",
        "3. Direct Microcontroller Feasibility Evaluation: An ESP32 or STM32 microcontroller GPIO pin has an absolute maximum source current limit of I_GPIO(max) = 12 mA to 20 mA. If connected directly: Turn-on time t_on = Q_g / I_GPIO = (146 × 10⁻⁹ C) / 0.015 A = 9.73 μs = 9,733 ns (Nearly 200 times slower!). During this 9.7 μs transition, switching losses escalate from 0.38 W to over 74 Watts, causing instant MOSFET thermal explosion.",
        "4. Gate Driver Sizing: A dedicated gate driver IC (e.g. TC4420 or MIC4420) rated for 6.0 A peak output is selected. Driver supply voltage V_DD = 12.0 V.",
        "5. Gate Resistor Calculation: R_gate = (V_DD - V_plateau) / I_gate(peak) = (12.0 V - 5.0 V) / 2.92 A = 7.0 V / 2.92 A = 2.40 Ω. Select standard 2.7 Ω metal-film resistor.",
        "6. Gate Resistor Purpose: Damping parasitic gate trace inductance L_trace to prevent high-frequency LC gate ringing (V_GS oscillations) that causes spurious re-triggering and shoot-through."
    ]
    story.append(create_example(5, "MOSFET Gate Charge Dynamics & Driver IC Peak Current Sizing",
                                "An agricultural inverter power MOSFET requires total gate charge Q_g = 146 nC to reach V_GS = 10 V. The design specifies a switching transition time of 50 ns. (a) Calculate the required peak gate driver current, (b) Prove mathematically why a microcontroller GPIO pin cannot drive this MOSFET directly, and (c) Size the series gate damping resistor R_gate for a 12V gate driver with a 5V Miller plateau.",
                                ex5_steps))

    # Example 6
    ex6_steps = [
        "1. Identify glass electrode characteristics: A combination glass pH probe immersed in irrigation fertigation water presents an internal source resistance R_probe = 200 MΩ = 2.0 × 10⁸ Ω. Probe Nernst output sensitivity = 59.16 mV/pH at 25°C.",
        "2. Loading Error with BJT Input Stage: A high-beta BJT (β = 400, I_B = 50 nA) presents an input resistance Z_in(BJT) ≈ 2.0 MΩ. Voltage division ratio: V_meas / V_probe = Z_in / (R_probe + Z_in) = 2 MΩ / (200 MΩ + 2 MΩ) = 2 / 202 = 0.0099. Over 99% of the signal is lost across probe internal resistance! Furthermore, the 50 nA base current chemically polarizes the glass membrane, permanently ruining the sensor.",
        "3. Solution with Dual-Gate MOSFET / Electrometer JFET (e.g. 2N4117): Gate leakage current I_GSS = 1.0 pA (1.0 × 10⁻¹² A). Input resistance R_in(MOSFET) = 1.0 × 10¹⁴ Ω (100,000 Giga-ohms).",
        "4. Signal Transfer Evaluation: Voltage division ratio: V_meas / V_probe = 10¹⁴ / (2 × 10⁸ + 10¹⁴) = 0.999998 (100.000% signal transfer, zero loading error).",
        "5. Probe Voltage Drop from Gate Leakage: ΔV_error = I_GSS × R_probe = (1.0 × 10⁻¹² A) × (2.0 × 10⁸ Ω) = 0.00020 V = 0.20 mV. At 59.16 mV/pH, this induces a pH measurement error of: Error = 0.20 mV / 59.16 mV/pH = 0.0034 pH units (Exceeds laboratory research standards)."
    ]
    story.append(create_example(6, "Ultra-High Impedance Electrometer Buffer for Soil Fertigation pH Glass Probes",
                                "An electrochemical glass pH sensor used in precision greenhouse fertigation monitoring in Arusha has an internal resistance of 200 MΩ. Contrast the performance of: (a) A standard BJT buffer (Z_in = 2.0 MΩ, I_bias = 50 nA), versus (b) An ultra-low-leakage electrometer MOSFET buffer (Z_in = 10¹⁴ Ω, I_GSS = 1.0 pA). Calculate the percentage signal transfer and the absolute pH measurement offset error.",
                                ex6_steps))

    # Example 7
    ex7_steps = [
        "1. Identify system parameters: Three parallel N-channel power MOSFETs (IRF1404: V_DS = 40V, R_DS(on) = 4.0 mΩ at 25°C, rising to 7.0 mΩ at 125°C) drive a 24V, 60 A DC axial flow grain dryer blower motor.",
        "2. Parallel Current Sharing Physics: In BJTs, if Transistor 1 runs hotter, its base-emitter voltage V_BE decreases (-2 mV/°C), causing it to draw more base current and hog more collector current until it burns out (thermal runaway).",
        "3. Power MOSFET Positive Temperature Coefficient of R_DS(on): For silicon MOSFETs: dR_DS(on) / dT > 0.",
        "4. Quantitative Self-Balancing Demonstration: Assume due to airflow asymmetry, Transistor 1 heats to 125°C (R_DS1 = 7.0 mΩ) while Transistors 2 and 3 remain at 75°C (R_DS2 = R_DS3 = 5.2 mΩ).",
        "5. Parallel Conductance: G_total = (1 / 7.0) + (1 / 5.2) + (1 / 5.2) = 0.1429 + 0.1923 + 0.1923 = 0.5275 S. Equivalent resistance R_eq = 1 / 0.5275 = 1.896 mΩ.",
        "6. Current Distribution across Parallel Branches: Total motor current I_total = 60.0 A. Voltage across parallel bank: V_bank = I_total × R_eq = 60 A × 1.896 mΩ = 0.1137 V.",
        "   • Hot Transistor 1 Current: I_D1 = V_bank / R_DS1 = 0.1137 V / 0.0070 Ω = 16.24 A.",
        "   • Cooler Transistors 2 and 3 Current: I_D2 = I_D3 = 0.1137 V / 0.0052 Ω = 21.88 A each. (Sum: 16.24 + 21.88 + 21.88 = 60.0 A).",
        "7. Engineering Conclusion: The hotter transistor naturally sheds current (carrying only 16.2 A compared to 21.9 A for the cooler devices). Its power dissipation decreases from 2.5 W down to 1.84 W, allowing it to cool down. Power MOSFETs are inherently self-stabilizing and safe to parallel."
    ]
    story.append(create_example(7, "Thermal Stability & Auto-Balancing of Parallel Power MOSFETs in Grain Dryers",
                                "A 60 A DC motor driving a maize dryer fan in Morogoro uses three parallel IRF1404 power MOSFETs. (a) Contrast the paralleling physics of BJTs versus MOSFETs, (b) Assuming Transistor 1 heats to 125°C (R_DS1 = 7.0 mΩ) while Transistors 2 and 3 operate at 75°C (R_DS2 = R_DS3 = 5.2 mΩ), calculate the exact current carried by each transistor, and (c) Demonstrate that the positive temperature coefficient of R_DS(on) prevents thermal runaway.",
                                ex7_steps))

    # Example 8
    ex8_steps = [
        "1. Identify H-bridge parameters: 48V DC reversible linear actuator for combine harvester header tilt control; Rated stall current I_stall = 30.0 A; Operating supply voltage V_bus = 48.0 V.",
        "2. High-Side Switch Selection: If using an N-channel MOSFET for the high-side switch (whose source is connected to motor terminal), the gate voltage must be driven to V_gate = V_bus + 10.0 V = +58.0 V to achieve full saturation.",
        "3. Bootstrap Circuit Operation: When the low-side MOSFET is ON, the motor terminal (phase node) is pulled to ground (0V). A bootstrap diode (fast recovery, e.g. UF4007) charges a bootstrap capacitor C_boot from a 12V auxiliary rail to V_boot ≈ 12.0 V - 0.7 V = 11.3 V.",
        "4. Floating Gate Drive: When the low-side switch turns OFF and high-side turns ON, the phase node swings up to +48V. The bootstrap capacitor floats upward with it, presenting a gate drive voltage of V_gate = 48V + 11.3V = 59.3V relative to ground (and exactly +11.3V relative to source), keeping the N-MOSFET fully turned ON.",
        "5. Bootstrap Capacitor Sizing: Total gate charge Q_g = 120 nC; Driver quiescent current I_q = 50 μA; Maximum ON-time t_on(max) = 10 ms (at minimum PWM frequency 100 Hz); Maximum allowable bootstrap capacitor voltage droop ΔV_boot = 0.50 V.",
        "6. Required Charge: Q_total = Q_g + (I_q × t_on(max)) = 120 nC + (50 μA × 10 ms) = 120 nC + 500 nC = 620 nC = 0.62 μC.",
        "7. Capacitance Calculation: C_boot ≥ Q_total / ΔV_boot = 0.62 μC / 0.50 V = 1.24 μF. Applying a 3× safety margin: C_boot = 3.72 μF (Select standard 4.7 μF, 25V low-ESR ceramic capacitor)."
    ]
    story.append(create_example(8, "Bootstrap Floating Gate Drive Sizing for High-Side N-Channel Inverter MOSFET",
                                "Design a bootstrap gate drive network for a high-side N-channel MOSFET in a 48V combine harvester header actuator H-bridge. Given MOSFET Q_g = 120 nC, driver leakage I_q = 50 μA, maximum pulse width t_on = 10 ms, and allowable voltage droop ΔV_boot = 0.5V: (a) Explain why a gate voltage > 48V is required, (b) Describe the charge-pump mechanism of the bootstrap capacitor and diode, and (c) Calculate the required capacitance C_boot with a 3× engineering safety margin.",
                                ex8_steps))

    # Example 9
    ex9_steps = [
        "1. Identify telemetry system parameters: CD4051B 8-channel CMOS analog multiplexer deployed in an automated paddy irrigation station in Mbarali to sequentially sample 8 soil moisture gypsum blocks (impedances R_sensor = 500 Ω to 50 kΩ). Multiplexer operates from single supply V_DD = 5.0 V, V_SS = 0 V.",
        "2. CMOS Transmission Gate On-Resistance Profile: The parallel NMOS-PMOS transmission gate presents R_on(max) = 280 Ω at input signal mid-rail V_in = 2.5 V, and R_on(min) = 120 Ω near 0V and 5V. Off-channel leakage current I_off = 100 pA at 25°C (rising to 5.0 nA at 60°C).",
        "3. Sampling Acquisition Time & Filtering: The ESP32 ADC sampling capacitor is C_sample = 15 pF. Maximum allowable acquisition error is 0.5 LSB for a 12-bit ADC (error < 1/8192 = 0.0122%), requiring settling time t_settle ≥ 9.0 · τ.",
        "4. Worst-Case Time Constant: Highest source impedance occurs when soil is bone dry: R_sensor = 50 kΩ. Total series resistance: R_total = R_sensor + R_on(max) = 50,000 Ω + 280 Ω = 50,280 Ω. Time constant: τ = R_total × C_sample = 50,280 Ω × (15 × 10⁻¹² F) = 0.754 μs.",
        "5. Minimum Settling Time: t_settle(min) = 9.0 × 0.754 μs = 6.79 μs. The microcontroller ADC sample window must be programmed for at least 10 μs to avoid cross-talk between adjacent soil depth channels.",
        "6. High-Temperature Leakage Error: At 60°C, total leakage through 7 unselected channels is: I_leak = 7 × 5.0 nA = 35.0 nA. Voltage error across 50 kΩ sensor: ΔV_leak = 35 nA × 50 kΩ = 1.75 mV. On a 3.3V full-scale ADC, this induces only 2.1 LSB error (0.053%), demonstrating the outstanding isolation of CMOS transmission gates."
    ]
    story.append(create_example(9, "CMOS Transmission Gate Multiplexing Analysis for Multi-Depth Soil Moisture Arrays",
                                "A CD4051B 8-channel CMOS analog multiplexer (R_on = 280 Ω, I_leak = 5 nA @ 60°C) sequentially samples eight gypsum block soil moisture probes (R_sensor up to 50 kΩ) into an ESP32 microcontroller ADC (C_sample = 15 pF). (a) Calculate the worst-case RC time constant, (b) Determine the minimum ADC settling time required to achieve 12-bit accuracy (< 0.5 LSB error), and (c) Evaluate the DC voltage offset error caused by off-channel leakage current at 60°C tropical field temperatures.",
                                ex9_steps))

    # -------------------------------------------------------------
    # SECTION 9: LABORATORY BENCH PROTOCOL
    # -------------------------------------------------------------
    story.append(Paragraph("6.9 Practical Laboratory Bench Protocol: JFET Curves & MOSFET Motor Driver", styles['SecH1']))
    story.append(Paragraph(
        "<b>Laboratory Objectives:</b><br/>"
        "1. Experimentally plot the drain characteristics (<i>I_D vs V_DS</i>) and transfer curve (<i>I_D vs V_GS</i>) of a 2N5457 N-channel JFET.<br/>"
        "2. Extract the pinch-off voltage <i>V_P</i>, saturation current <i>I_DSS</i>, and calculate maximum transconductance <i>g_m0</i>.<br/>"
        "3. Measure the gate threshold voltage <i>V_GS(th)</i> of a 2N7000 E-MOSFET.<br/>"
        "4. Construct a high-power PWM motor driver circuit using an IRF540N / IRF3205 power MOSFET, gate driver transistor, and inductive flyback diode to control a 12V DC cooling fan, measuring switching waveforms on a digital storage oscilloscope.",
        styles['DocBody']
    ))

    lab6_headers = ["Step #", "Experimental Bench Procedure", "Required Test Equipment", "Expected Technical Measurement / Observation"]
    lab6_rows = [
        ["1", "JFET I_DSS Measurement: Connect 2N5457 JFET with Gate tied to Source (V_GS = 0V). Sweep V_DS from 0V to 15V. Measure I_D.", "Variable DC Supply, Fluke DMM (mA scale)", "I_D rises linearly in ohmic region (0 to 2V), then flattens into saturation at I_DSS ≈ 3.5 to 5.0 mA."],
        ["2", "Pinch-off Extraction: Fix V_DS = 10.0 V. Apply negative voltage to Gate using second DC supply. Sweep V_GS from 0V to -5V.", "Dual DC Supply, 2× DMMs", "I_D decreases parabolically; drops to < 10 μA at V_GS = V_P ≈ -2.2 V (Pinch-off voltage)."],
        ["3", "Transfer Plotting: Record I_D at V_GS = 0, -0.5, -1.0, -1.5, -2.0 V. Plot I_D vs V_GS and overlay theoretical Shockley curve.", "Graph plotting software / Python", "Data points align tightly with parabola: I_D = I_DSS(1 - V_GS/V_P)². Calculate g_m0 = 2·I_DSS/|V_P| ≈ 3.8 mS."],
        ["4", "E-MOSFET Threshold: Wire 2N7000 with Drain tied to Gate (saturation connection: V_DS = V_GS) via 100 kΩ resistor to 10V. Measure V_GS.", "2N7000 MOSFET, 100 kΩ resistor, DMM", "Transistor self-biases at threshold: measured V_GS = V_GS(th) ≈ 2.15 V."],
        ["5", "PWM Driver Assembly: Wire IRF540N power MOSFET to drive 12V DC fan motor. Connect 100 Ω gate resistor and 10 kΩ pull-down.", "IRF540N MOSFET, 12V Fan, Function Gen, DSO", "Drive gate with 5V PWM square wave at 10 kHz. Observe smooth motor speed control from 0% to 100% duty cycle."],
        ["6", "Miller Plateau Observation: Zoom in on MOSFET gate voltage waveform on DSO (50 ns/div timescale) during turn-on.", "DSO (100 MHz bandwidth, 10× probe)", "Observe distinct flat horizontal plateau in gate voltage at V_GS ≈ 3.8 V during drain voltage transition."],
        ["7", "Thermal Verification: Run motor under full load for 10 minutes with and without heatsink. Monitor MOSFET case temperature.", "Infrared Thermometer", "TO-220 case temperature rises to only 38°C due to ultra-low R_DS(on) = 44 mΩ, confirming > 98% efficiency."]
    ]
    story.append(create_custom_table(lab6_headers, lab6_rows, [0.8*inch, 2.4*inch, 1.8*inch, 2.2*inch]))
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 10: TANZANIAN FIELD CASE STUDIES
    # -------------------------------------------------------------
    story.append(Paragraph("6.10 Tanzanian Agricultural Engineering Field Case Studies", styles['SecH1']))
    story.append(Paragraph(
        "<b>Case Study 1: Solar Borehole Pump Inverter Shoot-Through Failures in Singida Rural</b><br/>"
        "Singida Region experiences intense solar insolation and prolonged dry seasons, making solar-powered borehole water pumping vital for community "
        "and livestock survival. At a pastoral water point in Iramba District, a 3.0 kW three-phase solar pump inverter suffered catastrophic failure "
        "of its power MOSFET bridge during the dry season. The inverter used six IRFP460 MOSFETs in an H-bridge configuration switched at 20 kHz. "
        "Post-mortem failure analysis by SUA agricultural engineering specialists discovered that all high-side and low-side transistors in Phase A "
        "had suffered simultaneous source-to-drain short circuits. "
        "Investigation revealed that the microcontroller firmware had been compiled with a dead-time (blanking delay between high-side turn-off and low-side turn-on) "
        "of only 150 nanoseconds. In Singida's intense 42°C heat, the gate driver optocouplers suffered propagation delay drift, while the MOSFETs' "
        "turn-off delay time increased due to elevated junction temperatures. As a result, the high-side and low-side MOSFETs conducted simultaneously "
        "for 80 nanoseconds during each switching cycle, creating a direct short circuit across the 380V DC solar bus (<b>shoot-through current</b> > 120 A). "
        "Reprogramming the inverter microcontroller dead-time to 850 nanoseconds and installing fast active gate pull-down circuits completely eliminated "
        "shoot-through, ensuring uninterrupted water supply for over 6,000 cattle.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Case Study 2: Drip Fertigation Electrical Conductivity (EC) Sensor Polarization in Arusha</b><br/>"
        "Commercial hydroponic green-bean farms in Arusha monitor soil electrical conductivity (EC) to adjust nutrient dosing solutions. "
        "The original analog conditioning circuit utilized a BJT-based operational amplifier. Over weeks of continuous operation, "
        "the microampere input bias currents drawn by the BJT inputs caused galvanic electrochemical polarization of the stainless-steel "
        "sensor electrodes: metallic ions plated onto one probe while oxide films passivated the other. "
        "This led to severe calibration drift (+35% EC measurement error), causing the automation system to starve the crops of essential nitrogen and potassium. "
        "SUA precision farming researchers retrofitted the instrumentation using an ultra-high input impedance Dual-Gate MOSFET electrometer amplifier "
        "(input resistance > 10¹⁴ Ω, input bias current < 0.5 pA) driven by an AC bipolar square-wave excitation at 1.0 kHz. "
        "The complete elimination of DC bias current stopped electrode polarization entirely, restoring EC measurement accuracy to within ±1.5% throughout the harvest.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 11: REVIEW QUESTIONS & PROBLEMS
    # -------------------------------------------------------------
    story.append(Paragraph("6.11 Comprehensive Self-Assessment & Review Questions", styles['SecH1']))
    story.append(Paragraph("<b>PART A: Conceptual & Theoretical Questions</b>", styles['SecH2']))
    q_part_a = [
        "1. Explain why the Field-Effect Transistor (FET) is termed a unipolar, voltage-controlled device, whereas the BJT is a bipolar, current-controlled device.",
        "2. Describe the physical mechanism of channel pinch-off in an N-channel JFET. Why does drain current saturate beyond pinch-off instead of continuing to rise?",
        "3. Write Shockley's transconductance equation for a JFET in saturation and define I_DSS, V_P, and V_GS.",
        "4. Differentiate between Depletion-mode MOSFETs (D-MOSFET) and Enhancement-mode MOSFETs (E-MOSFET) in terms of physical channel presence and gate threshold voltage.",
        "5. Why do power MOSFETs exhibit a positive temperature coefficient of on-resistance R_DS(on), and why does this property prevent thermal runaway when paralleling devices?",
        "6. What is the Miller effect in MOSFET switching? Explain what occurs during the Miller Plateau on the gate voltage waveform.",
        "7. Why is a dedicated high-current gate driver IC required to switch large power MOSFETs at high PWM frequencies, even though DC gate current is zero?",
        "8. Explain why the Silicon Dioxide gate insulator of a MOSFET is vulnerable to Electrostatic Discharge (ESD), and list three workshop handling precautions.",
        "9. Compare the small-signal transconductance g_m of a JFET versus that of a BJT at equivalent quiescent currents.",
        "10. Why are MOSFET electrometer preamplifiers preferred over BJT amplifiers for electrochemical soil pH and electrical conductivity (EC) probes?"
    ]
    for q in q_part_a:
        story.append(Paragraph(q, styles['DocBullet']))

    story.append(Paragraph("<b>PART B: Quantitative Analytical Problems</b>", styles['SecH2']))
    q_part_b = [
        "11. An N-channel JFET has I_DSS = 12.0 mA and V_P = -3.5 V. (a) Calculate drain current I_D for V_GS = 0V, -1.0V, -2.0V, and -3.0V. (b) Compute maximum transconductance g_m0. (c) Determine transconductance g_m at V_GS = -1.5 V.",
        "12. A JFET self-bias circuit has V_DD = 20.0 V, R_D = 2.7 kΩ, R_S = 680 Ω, and R_G = 1.0 MΩ. Given I_DSS = 8.0 mA and V_P = -4.0 V: (a) Formulate the quadratic equation for I_D, (b) Solve for quiescent drain current I_DQ, (c) Calculate V_GSQ and V_DSQ, and (d) Confirm operation in pinch-off saturation.",
        "13. An N-channel E-MOSFET has V_GS(th) = 2.5 V and I_D(on) = 400 mA at V_GS(on) = 8.0 V. (a) Determine conduction parameter k. (b) Calculate drain current when gate-source voltage is V_GS = 5.0 V in saturation. (c) If drain resistor is R_D = 100 Ω and V_DD = 15 V, calculate V_DS and determine whether the device is in saturation or ohmic region.",
        "14. An IRF3205 power MOSFET switches a 24V, 20 A inductive DC motor in a Dodoma solar water pump station. The MOSFET has R_DS(on) = 8.0 mΩ at 25°C (rising to 14.0 mΩ at 110°C). Gate switching times are t_r = 40 ns and t_f = 60 ns at a PWM frequency of 20 kHz. (a) Calculate conduction power loss at 110°C. (b) Compute switching power loss. (c) Calculate total transistor power dissipation.",
        "15. For the MOSFET in Problem 14, thermal ratings are θ_jc = 0.75 °C/W, θ_cs = 0.50 °C/W, and maximum junction temperature is T_j = 150°C. If ambient air inside the solar controller reaches 50°C, calculate the required thermal resistance of the heatsink θ_sa with a 25% safety factor."
    ]
    for q in q_part_b:
        story.append(Paragraph(q, styles['DocBullet']))

    story.append(Paragraph("<b>PART C: Agricultural Systems Design Challenges</b>", styles['SecH2']))
    q_part_c = [
        "16. <b>Three-Phase Brushless Solar Pump Inverter Bridge Design:</b> Design a 48V, 1.5 kW three-phase inverter bridge using N-channel power MOSFETs for a deep-well agricultural borehole pump in Chamwino, Dodoma. Select appropriate MOSFETs, calculate conduction and switching losses at 16 kHz PWM, specify gate driver ICs (IR2104) and bootstrap capacitors, design the dead-time network (t_dead ≥ 500 ns) to prevent shoot-through, and size the shared aluminum heatsink for 48°C ambient conditions.",
        "17. <b>Electrostatic Tree-Sprayer High-Voltage Modulator:</b> Design a solid-state high-voltage pulsing circuit to charge pesticide droplets to -5 kV in an orchard sprayer in Morogoro. The switching stage uses a series stack of high-voltage MOSFETs (1,200V each). Design a dynamic voltage-balancing network using Zener diodes and metal-film resistors to guarantee equal voltage division across the stack during 50 μs pulses, and provide complete gate isolation using pulse transformers.",
        "18. <b>Sub-Picoampere Soil Moisture Electrometer Interface:</b> Design an ultra-low-leakage analog front-end for a capacitive soil moisture matrix sensor operating from 0 to 100% volumetric water content. Use an electrometer-grade Dual-Gate MOSFET with guard rings on the PCB layout to eliminate surface leakage currents across Morogoro clay dust. Provide full circuit schematic, guard ring routing geometry, temperature compensation, and verify bandwidth up to 100 kHz."
    ]
    for q in q_part_c:
        story.append(Paragraph(q, styles['DocBullet']))

    # -------------------------------------------------------------
    # SECTION 12: REFERENCES
    # -------------------------------------------------------------
    story.append(Spacer(1, 8))
    story.append(Paragraph("6.12 Prescribed Textbooks & Research Bibliography", styles['SecH1']))
    refs = [
        "1. Boylestad, R. L., & Nashelsky, L. (2018). <i>Electronic Devices and Circuit Theory</i> (11th ed.). Pearson Education.",
        "2. Sedra, A. S., & Smith, K. C. (2020). <i>Microelectronic Circuits</i> (8th ed.). Oxford University Press.",
        "3. Neamen, D. A. (2012). <i>Semiconductor Physics and Devices: Basic Principles</i> (4th ed.). McGraw-Hill.",
        "4. Rashid, M. H. (2018). <i>Power Electronics: Devices, Circuits, and Applications</i> (4th ed.). Pearson.",
        "5. Floyd, T. L. (2017). <i>Electronic Devices: Conventional Current Version</i> (10th ed.). Pearson.",
        "6. Sze, S. M., & Ng, K. K. (2007). <i>Physics of Semiconductor Devices</i> (3rd ed.). John Wiley & Sons.",
        "7. Williams, S. E., & Wilson, T. A. (2023). Introduction to Semiconductor Devices and Circuits. <i>Journal of Applied Physics</i>, 135(6), 065420."
    ]
    for r in refs:
        story.append(Paragraph(r, styles['DocBody']))

    render_pdf("AEN_214_Lecture_6_Compendium.pdf", story)

if __name__ == "__main__":
    build_lecture_6()
