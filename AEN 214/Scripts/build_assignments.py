#!/usr/bin/env python3
"""
build_assignments.py
Generates the three comprehensive open coursework assignments for:
AEN 214: INTRODUCTION TO ELECTRONICS
Department of Agricultural Engineering, Sokoine University of Agriculture.
Saved in the Assignment/ directory.
Each assignment contains 12 tiered questions (Simple -> Moderate -> Complex Engineering Design).
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from compendium_base import (
    NumberedCanvas, get_custom_stylesheet,
    COLOR_PRIMARY, COLOR_SECONDARY, COLOR_ACCENT, COLOR_BG_LIGHT, COLOR_BORDER, COLOR_DARK
)

ASSIGNMENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Assignment"))
os.makedirs(ASSIGNMENT_DIR, exist_ok=True)

def render_assignment_pdf(filename, story):
    out_path = os.path.join(ASSIGNMENT_DIR, filename)
    doc = SimpleDocTemplate(
        out_path,
        pagesize=letter,
        leftMargin=46,
        rightMargin=46,
        topMargin=46,
        bottomMargin=46
    )
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[Success] Generated {out_path} ({os.path.getsize(out_path)} bytes)")
    return out_path

def create_assignment_header(asn_num, title, topics_covered, due_info):
    styles = get_custom_stylesheet()
    story = []
    
    header_data = [
        [Paragraph("SOKOINE UNIVERSITY OF AGRICULTURE", styles['CoverUniv'])],
        [Paragraph("School of Engineering and Technology | Department of Agricultural Engineering", styles['CoverDept'])],
        [Spacer(1, 4)],
        [Paragraph("AEN 214: INTRODUCTION TO ELECTRONICS", styles['CourseCode'])],
        [Paragraph(f"OPEN COURSEWORK ASSIGNMENT {asn_num}: {title.upper()}", styles['CourseTitle'])],
        [Paragraph(f"<b>Curriculum Coverage:</b> {topics_covered}<br/><b>Due Date / Submission:</b> {due_info} | <b>Total Marks:</b> 100 Marks", styles['MetaBox'])]
    ]
    tbl = Table(header_data, colWidths=[7.2 * inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), COLOR_BG_LIGHT),
        ('BOX', (0, 0), (-1, -1), 1.2, COLOR_PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 10))

    instructions = (
        "<b>Instructions to Candidates:</b><br/>"
        "1. This assignment is an open engineering coursework assessment designed to develop analytical and practical circuit design competence.<br/>"
        "2. Answer <b>ALL twelve (12) questions</b>. Questions are tiered into Part A (Foundational Concepts), Part B (Quantitative Circuit Analysis), and Part C (Agricultural Engineering Systems Design).<br/>"
        "3. Show all mathematical derivations, state all engineering assumptions clearly, sketch labeled schematics where applicable, and cite proper SI units.<br/>"
        "4. Neatness, logical presentation, and clear engineering justification contribute to the final grade."
    )
    inst_tbl = Table([[Paragraph(instructions, styles['DocBody'])]], colWidths=[7.2 * inch])
    inst_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 0.8, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(inst_tbl)
    story.append(Spacer(1, 12))
    return story

# -------------------------------------------------------------
# ASSIGNMENT 1: TOPICS 1 - 3
# -------------------------------------------------------------
def build_assignment_1():
    styles = get_custom_stylesheet()
    story = create_assignment_header(
        1, "Passive Components, Semiconductor Physics & Diode Circuits",
        "Topic 1 (Passive Components), Topic 2 (Semiconductor Physics), Topic 3 (Semiconductor Diodes)",
        "Week 5 of Semester | Individual Submission"
    )

    # PART A: SIMPLE / FOUNDATIONAL CONCEPTS
    story.append(Paragraph("PART A: Foundational Concepts & Component Physics [20 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 1 (5 Marks):</b> A through-hole carbon film resistor has five colored bands in sequence: Red, Violet, Black, Brown, Brown. "
        "Decode its nominal resistance, tolerance percentage, and calculate the maximum and minimum permissible resistance values. "
        "If a 12V DC source is placed across this resistor, compute the power dissipated and state whether a 1/4W rating is adequate.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 2 (5 Marks):</b> Explain the physical differences between an insulator, a semiconductor, and a conductor in terms of "
        "their energy band structures, forbidden energy gaps (E_g), and the presence of charge carriers at absolute zero (0 K) versus room temperature (300 K).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 3 (5 Marks):</b> Define the term <i>doping</i>. Explain how adding minute traces of Phosphorus (Group V) to a pure silicon crystal produces an N-type semiconductor, "
        "and explain why the resulting crystal remains electrically neutral as a whole despite having free mobile electrons.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 4 (5 Marks):</b> Distinguish between the 1st (ideal), 2nd (constant voltage drop), and 3rd (piecewise linear) approximations of a PN junction diode. "
        "State typical circuit operating conditions under which each approximation is most appropriately applied by an engineer.",
        styles['DocBody']
    ))

    # PART B: QUANTITATIVE CIRCUIT ANALYSIS
    story.append(Spacer(1, 6))
    story.append(Paragraph("PART B: Quantitative Circuit Analysis & Derivations [35 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 5 (8 Marks):</b> An analog soil moisture sensor signal conditioning circuit uses a series RC low-pass filter with R = 15 kΩ and C = 4.7 μF. "
        "(a) Calculate the circuit time constant τ. (b) Determine the time required for the capacitor to charge from 0V to 90% of a 5V step input. "
        "(c) Calculate the electrostatic energy stored in the capacitor when fully charged to 5V.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 6 (9 Marks):</b> A monocrystalline silicon PN junction diode is fabricated with an acceptor doping concentration N_A = 4.0 × 10¹⁷ cm⁻³ and "
        "donor doping concentration N_D = 1.0 × 10¹⁶ cm⁻³ at a temperature T = 300 K (intrinsic carrier concentration n_i = 1.5 × 10¹⁰ cm⁻³). "
        "(a) Calculate the junction built-in barrier potential V₀. (b) If the junction temperature rises to 350 K, explain qualitatively and calculate quantitatively "
        "the directional change in V₀ (assume thermal voltage V_T scales linearly with T).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 7 (9 Marks):</b> Starting from the Shockley diode equation I_D = I_S · [e^(V_D / (η V_T)) - 1], prove mathematically that the dynamic AC junction "
        "resistance is given by r_d = (η · V_T) / I_D. For a silicon diode with η = 1 and V_T = 26 mV, calculate r_d at: (i) I_D = 0.5 mA, (ii) I_D = 2.0 mA, and (iii) I_D = 20 mA.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 8 (9 Marks):</b> A center-tapped transformer full-wave rectifier and a full-wave bridge rectifier are both powered from identical AC supplies. "
        "Compare both rectifiers with respect to: (a) Peak Inverse Voltage (PIV) rating required for the diodes, (b) Transformer Utilization Factor (TUF), "
        "and (c) Total forward diode voltage drop during peak conduction.",
        styles['DocBody']
    ))

    # PART C: AGRICULTURAL ENGINEERING SYSTEMS DESIGN
    story.append(Spacer(1, 6))
    story.append(Paragraph("PART C: Agricultural Engineering Systems Design [45 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 9 (11 Marks) - Solar Irrigation Power Rectification:</b><br/>"
        "Design a 12V DC power supply to operate an automated greenhouse drip-irrigation solenoid manifold from a 230V_rms, 50Hz single-phase AC generator. "
        "The four solenoid valves draw a continuous load current I_dc = 2.0 A. A full-wave bridge rectifier using four 1N5404 silicon diodes (V_F = 0.8 V) "
        "with a parallel reservoir capacitor filter is selected.<br/>"
        "(a) Determine the required transformer secondary RMS voltage (V_sec) to maintain a minimum peak load voltage of 15.0V.<br/>"
        "(b) Sizing the smoothing filter capacitor C to ensure peak-to-peak ripple voltage does not exceed 0.8 V_p-p.<br/>"
        "(c) Calculate the minimum Peak Inverse Voltage (PIV) rating required for the rectifier diodes, including a 100% safety margin.<br/>"
        "(d) Select an appropriate standard commercial capacitor value and specify its minimum working voltage (WVDC).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 10 (11 Marks) - Hall Effect Tractor PTO Tachometer:</b><br/>"
        "A precision digital tachometer on a tractor Power Take-Off (PTO) shaft incorporates an N-type semiconductor Hall effect sensor slab with thickness "
        "t = 0.20 mm and electron carrier concentration n = 3.2 × 10¹⁵ cm⁻³. A regulated bias current I_x = 20 mA flows longitudinally through the sensor. "
        "When a magnetic gear tooth passes within 2 mm of the sensor, a perpendicular magnetic flux density B_z = 0.42 Tesla is measured.<br/>"
        "(a) Derive the expression for the Hall coefficient R_H and compute its numerical value.<br/>"
        "(b) Calculate the generated Hall voltage V_H in millivolts.<br/>"
        "(c) If electrical noise from the tractor alternator induces a 2.5 mV stray voltage, calculate the Signal-to-Noise Ratio (SNR) in decibels (dB) "
        "and suggest a differential amplifier topology to eliminate common-mode alternator noise.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 11 (11 Marks) - Sensor Analog Input Overvoltage Protection:</b><br/>"
        "An analog soil conductivity probe installed along an outdoor farm furrow is connected to a 3.3V microcontroller ADC pin via a 50-meter cable. "
        "Inductive switching from nearby borehole pumps induces AC transient spikes of ±25V peak into the cable. "
        "Design a double-diode clipper protection network using two silicon diodes (V_K = 0.7 V) and a series current-limiting resistor R_S.<br/>"
        "(a) Draw the complete circuit schematic showing connection to the 3.3V power rail and ground.<br/>"
        "(b) Determine the maximum and minimum voltages delivered to the ADC pin during ±25V transient surges.<br/>"
        "(c) If the maximum allowable transient current through each protection diode is 20 mA, calculate the minimum safe value and wattage rating of series resistor R_S.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 12 (12 Marks) - Capacitive Grain Moisture Sensor Filtering:</b><br/>"
        "A continuous-flow maize dryer utilizes a cylindrical coaxial capacitor sensor whose dielectric constant varies linearly with grain moisture content "
        "(C_dry = 120 pF at 12% moisture; C_wet = 480 pF at 28% moisture). The sensor is excited by a 100 kHz sinusoidal oscillator.<br/>"
        "(a) Calculate the capacitive reactance X_C of the sensor at both dry (12%) and wet (28%) grain conditions.<br/>"
        "(b) The sensor forms an AC voltage divider with an inductor L to convert moisture variations into amplitude variations. "
        "Determine the required inductance L so that the circuit achieves electrical resonance at 100 kHz when grain moisture is exactly at the target storage value of 14% (C = 165 pF).<br/>"
        "(c) What safety hazards arise if high-moisture grain causes localized dielectric heating inside the capacitor sensor?",
        styles['DocBody']
    ))

    render_assignment_pdf("AEN_214_Assignment_1.pdf", story)

# -------------------------------------------------------------
# ASSIGNMENT 2: TOPICS 4 - 6
# -------------------------------------------------------------
def build_assignment_2():
    styles = get_custom_stylesheet()
    story = create_assignment_header(
        2, "Special Purpose Diodes, BJTs & Power Field Effect Transistors",
        "Topic 4 (Special Diodes), Topic 5 (Bipolar Junction Transistors), Topic 6 (Field Effect Transistors)",
        "Week 9 of Semester | Individual Submission"
    )

    # PART A: CONCEPTUAL PRINCIPLES
    story.append(Paragraph("PART A: Foundational Physics & Transistor Theory [20 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 1 (5 Marks):</b> Contrast Zener breakdown with Avalanche breakdown across four distinct criteria: (a) Doping level, "
        "(b) Typical breakdown voltage threshold, (c) Physical carrier multiplication mechanism, and (d) Temperature coefficient of breakdown voltage.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 2 (5 Marks):</b> Explain why an NPN Bipolar Junction Transistor cannot be effectively modeled or fabricated simply by connecting "
        "two discrete back-to-back PN junction diodes with copper wire. Refer to base width, carrier lifetime, and recombination mechanics.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 3 (5 Marks):</b> Describe the pinch-off phenomenon in an N-channel Junction Field Effect Transistor (JFET). "
        "Explain why the drain current saturates at a constant value (I_DSS) beyond pinch-off (V_DS > |V_P|) rather than dropping to zero.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 4 (5 Marks):</b> Explain why power MOSFETs are immune to thermal runaway and can be operated in parallel arrays with negligible risk, "
        "whereas paralleling power BJTs without emitter ballasting resistors leads to thermal destruction.",
        styles['DocBody']
    ))

    # PART B: QUANTITATIVE CIRCUIT ANALYSIS
    story.append(Spacer(1, 6))
    story.append(Paragraph("PART B: Quantitative Transistor Circuit Analysis [35 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 5 (8 Marks):</b> A 6.8V Zener diode shunt regulator is supplied from an unregulated DC input that fluctuates between 11V and 15V. "
        "The load resistance varies from 340 Ω to 1.2 kΩ. The Zener diode has ratings: V_Z = 6.8 V, I_ZK = 3 mA, and P_Z(max) = 1.0 W. "
        "Calculate the permissible range for series current-limiting resistor R_S and select a suitable standard E24 resistor value.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 6 (9 Marks):</b> For a silicon NPN transistor configured in Common-Emitter mode with β = 120 and I_CBO = 50 nA at 25°C, "
        "(a) Calculate the Common-Base current gain α. (b) Calculate the open-base collector-emitter leakage current I_CEO. "
        "(c) If the junction temperature rises to 75°C causing I_CBO to increase eight-fold, compute the new value of I_CEO.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 7 (9 Marks):</b> An N-channel JFET has saturation drain current I_DSS = 14 mA and pinch-off voltage V_P = -4.5 V. "
        "Using Shockley's equation: (a) Calculate drain current I_D for V_GS = 0V, -1.0V, -2.0V, -3.0V, and -4.5V. "
        "(b) Calculate maximum transconductance g_m0. (c) Compute operating transconductance g_m at V_GS = -2.0 V.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 8 (9 Marks):</b> A Common-Emitter BJT amplifier with voltage-divider bias has circuit values: V_CC = 15 V, R1 = 47 kΩ, R2 = 12 kΩ, "
        "R_C = 3.3 kΩ, R_E = 1.2 kΩ, and β = 100. (a) Determine the DC quiescent operating point (I_CQ, V_CEQ). "
        "(b) Calculate the small-signal dynamic emitter resistance r_e. (c) Calculate the AC voltage gain A_v assuming the emitter resistor is bypassed with a large capacitor C_E.",
        styles['DocBody']
    ))

    # PART C: AGRICULTURAL ENGINEERING SYSTEMS DESIGN
    story.append(Spacer(1, 6))
    story.append(Paragraph("PART C: Agricultural Actuator & Power Electronics Design [45 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 9 (11 Marks) - Solar Array Shading Protection:</b><br/>"
        "A solar-powered borehole water pumping installation comprises three series strings of 400W monocrystalline photovoltaic modules. "
        "Each module produces a string current I_string = 10.5 A. During dusty dry-season conditions in central Tanzania, acacia tree leaves shade one substring.<br/>"
        "(a) Explain the electrical and thermal consequences of cell reverse breakdown if bypass diodes are omitted.<br/>"
        "(b) Compare the power dissipation in a sealed IP67 junction box when using a standard silicon rectifier diode (V_F = 1.0 V at 10.5A) "
        "versus an MBR1645 Schottky barrier diode (V_F = 0.42 V at 10.5A).<br/>"
        "(c) If the junction box has a thermal resistance to ambient R_θ = 8.5 °C/W and ambient temperature is 42°C, compute the steady-state temperature inside the enclosure for both diode types.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 10 (11 Marks) - BJT Saturated Switch for Grain Aeration Fan:</b><br/>"
        "An automated maize storage silo uses an ESP32 microcontroller (3.3V logic, maximum safe GPIO current = 12 mA) to actuate a 12V, 15W cooling fan relay.<br/>"
        "(a) Calculate the required collector saturation current I_C(sat).<br/>"
        "(b) The relay is switched using a BD139 NPN power transistor with minimum saturation gain β_min = 40. "
        "Using an overdrive factor ODF = 3.0 to ensure solid saturation across temperature extremes, compute the required base current I_B(forced).<br/>"
        "(c) Sizing the series base resistor R_B (assume V_BE(sat) = 0.85 V) and check whether the ESP32 GPIO pin current rating is respected.<br/>"
        "(d) Explain the necessity of the anti-parallel freewheeling diode across the relay coil and specify an appropriate diode part number.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 11 (11 Marks) - Power MOSFET Thermal Sizing for 24V Solar Irrigation Pump:</b><br/>"
        "A 24V, 360W DC submersible solar pump (full-load current I_D = 15 A) is speed-controlled via PWM from an agricultural automation board. "
        "An IRF3205 N-channel Power MOSFET is selected, having on-state resistance R_DS(on) = 8.0 mΩ (0.008 Ω), junction-to-case thermal resistance R_θJC = 0.75 °C/W, "
        "and maximum rated junction temperature T_j(max) = 175°C. The control box operates in an outdoor shed where ambient temperature reaches T_amb = 45°C.<br/>"
        "(a) Calculate the static conduction power loss P_cond in the MOSFET at full 15A continuous current.<br/>"
        "(b) If junction-to-ambient thermal resistance without a heatsink is R_θJA = 62 °C/W, prove that the MOSFET will burn out if operated without a heatsink.<br/>"
        "(c) Calculate the maximum allowable heatsink thermal resistance R_θ(heatsink) to maintain the MOSFET junction temperature below a safe design limit of T_j = 90°C (assume thermal grease interface R_θ(case-to-sink) = 0.50 °C/W).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 12 (12 Marks) - High-Impedance Soil pH Transducer Buffer:</b><br/>"
        "Glass-membrane electrochemical soil pH sensors have an extraordinarily high internal source resistance (R_source ≈ 100 MΩ to 1 GΩ) and output an analog signal "
        "of approximately 59.2 mV per pH unit at 25°C. Connecting this probe to a standard BJT amplifier causes severe signal attenuation.<br/>"
        "(a) Explain why a standard BJT amplifier cannot be used for direct buffering of a glass pH electrode.<br/>"
        "(b) Design a Common-Drain (Source Follower) buffer amplifier using a 2N5457 N-channel JFET (I_DSS = 5.0 mA, V_P = -2.5 V). "
        "Draw the circuit schematic and derive the expression for input resistance R_in and voltage gain A_v.<br/>"
        "(c) What precautions regarding PCB contamination (humidity, agricultural fertilizer dust, and flux residue) must be taken to maintain 10¹² Ω insulation resistance on the sensor board?",
        styles['DocBody']
    ))

    render_assignment_pdf("AEN_214_Assignment_2.pdf", story)

# -------------------------------------------------------------
# ASSIGNMENT 3: TOPICS 7 - 9
# -------------------------------------------------------------
def build_assignment_3():
    styles = get_custom_stylesheet()
    story = create_assignment_header(
        3, "Number Systems, Digital Electronics & Boolean Karnaugh Maps",
        "Topic 7 (Number Systems), Topic 8 (Digital Electronics), Topic 9 (Boolean Algebra & K-Maps)",
        "Week 13 of Semester | Individual Submission"
    )

    # PART A: NUMBER SYSTEMS & ARITHMETIC
    story.append(Paragraph("PART A: Radix Conversions & Signed Digital Arithmetic [20 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 1 (5 Marks):</b> Convert the decimal value 219.6875 into: (a) Pure Binary (up to 4 fractional bits), (b) Hexadecimal, and (c) Octal. "
        "Show all successive division and multiplication steps clearly.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 2 (5 Marks):</b> Perform the following signed 8-bit two's complement additions and subtractions. In each case, state whether an arithmetic "
        "overflow occurs and verify by checking the sign-bit carry condition V = C_in ⊕ C_out:<br/>"
        "(a) (+54) + (+82)<br/>"
        "(b) (+75) - (+98) [i.e., (+75) + (-98)]",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 3 (5 Marks):</b> Perform the BCD addition of decimal numbers 678 + 485 using 8421 BCD arithmetic. "
        "Show the binary addition for each decimal digit decade and illustrate where the +6 (0110_2) correction factor must be applied.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 4 (5 Marks):</b> An autonomous tractor front-wheel steering shaft encoder outputs angular position in 4-bit Gray code. "
        "(a) Convert the Gray code words 1101 and 1010 into standard binary. (b) Explain why Gray code eliminates mechanical and optical reading race hazards "
        "relative to standard binary encoding.",
        styles['DocBody']
    ))

    # PART B: DIGITAL LOGIC & UNIVERSAL GATES
    story.append(Spacer(1, 6))
    story.append(Paragraph("PART B: Logic Gate Synthesis & Arithmetic Circuits [35 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 5 (8 Marks):</b> Construct the truth tables and write the Boolean algebraic expressions for 3-input NAND, NOR, and XOR gates. "
        "Explain how the XOR gate functions as an odd parity generator for agricultural serial telemetry.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 6 (9 Marks):</b> Prove that the NAND gate is a universal logic gate by drawing the exact schematic connections to synthesize: "
        "(a) Inverter (NOT), (b) 2-input AND gate, (c) 2-input OR gate, and (d) 2-input NOR gate. Use only standard 2-input NAND gates.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 7 (9 Marks):</b> A 1-bit binary Full Adder circuit accepts inputs A, B, and C_in. "
        "(a) Construct the complete 8-row truth table for outputs Sum (S) and Carry-out (C_out). "
        "(b) Write the minimized Boolean expressions for S and C_out. (c) Draw the logic diagram using two Half Adders and an OR gate.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 8 (9 Marks):</b> Using Boolean algebra axioms and De Morgan's theorems, algebraically prove the following identities:<br/>"
        "(a) A + A̅·B = A + B<br/>"
        "(b) (A + B) · (A + C) = A + B·C<br/>"
        "(c) (A · B · C)̅ = A̅ + B̅ + C̅",
        styles['DocBody']
    ))

    # PART C: BOOLEAN MINIMIZATION & AGRICULTURAL SYSTEMS SYNTHESIS
    story.append(Spacer(1, 6))
    story.append(Paragraph("PART C: K-Map Minimization & Agricultural Safety Synthesis [45 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 9 (11 Marks) - Automated Silo Fumigation Exhaust Logic:</b><br/>"
        "A grain silo fumigation system has four safety sensors: P (Phosphine Gas Detected), T (Temperature > 35°C), D (Silo Access Door Closed), and E (Emergency Switch Active). "
        "The exhaust ventilation blower (B) must turn ON (B = 1) according to the truth function: B(P, T, D, E) = ∑ m(2, 3, 6, 7, 10, 11, 14, 15).<br/>"
        "(a) Plot this function on a 4-variable Karnaugh Map (Gray code ordered).<br/>"
        "(b) Identify all prime implicants and essential prime implicants.<br/>"
        "(c) Derive the minimized Sum of Products (SOP) expression.<br/>"
        "(d) Implement the minimized expression using NAND-NAND logic gates.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 10 (11 Marks) - Grain Dryer Burner Safety Interlock with Don't Cares:</b><br/>"
        "An automated cross-flow grain dryer burner shutoff circuit F(A, B, C, D) is monitored by four binary inputs: A = High Burner Temp; B = Flame Detected; "
        "C = Airflow Blower Running; D = Master Control Armed. The shutdown alarm triggers for minterms: F = ∑ m(0, 1, 4, 5, 8, 9, 12). "
        "Due to mechanical sensor interlocks, input states d = ∑ d(10, 11, 13, 14, 15) can never physically occur.<br/>"
        "(a) Map the minterms and Don't Care conditions onto a 4-variable K-map.<br/>"
        "(b) Form the largest possible groups by leveraging the Don't Care terms.<br/>"
        "(c) Write the minimal SOP expression and compare the gate count against a design that treats all Don't Cares as zeros.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 11 (11 Marks) - Autonomous Combine Harvester Header Height Controller:</b><br/>"
        "An autonomous wheat combine harvester uses three ultrasonic height sensors located on the left (L), center (C), and right (R) of the cutting header. "
        "Each sensor outputs '1' if the cutter bar is too close to the ground (< 10 cm). A hydraulic lift actuator must raise the header (Y = 1) if "
        "at least two out of the three sensors indicate ground proximity, OR if an obstacle proximity sensor (O = 1) triggers.<br/>"
        "(a) Formulate the truth table for the 4-variable function Y(O, L, C, R).<br/>"
        "(b) Plot the function on a 4-variable K-map.<br/>"
        "(c) Obtain the minimal SOP expression for hydraulic lift actuation.<br/>"
        "(d) Identify any static-1 hazards and add redundant prime implicants if necessary to guarantee glitch-free hydraulic valve switching.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 12 (12 Marks) - Digital Agricultural Dosing Pump Controller:</b><br/>"
        "A dairy cattle automated parlor dosing system dispenses liquid nutritional supplement based on 3 binary inputs: A (Animal ID Validated), "
        "W (Animal Weight > 450 kg), and M (Milk Yield > 25 Liters/day). The dispenser valve V operates according to: V = A · (W̅ · M + W · M) + A · W̅ · M̅.<br/>"
        "(a) Simplify the Boolean expression algebraically to its absolute minimum literal count.<br/>"
        "(b) Verify your algebraic minimization by constructing a 3-variable Karnaugh Map.<br/>"
        "(c) Draw the final simplified circuit using standard logic gates.<br/>"
        "(d) If an active-LOW relay module is used to drive the pump, express the required logic function using De Morgan's theorem.",
        styles['DocBody']
    ))

    render_assignment_pdf("AEN_214_Assignment_3.pdf", story)

def main():
    print("Generating all 3 open coursework assignments for AEN 214 in Assignment/ directory...")
    build_assignment_1()
    build_assignment_2()
    build_assignment_3()
    print("All assignments generated successfully!")

if __name__ == "__main__":
    main()
