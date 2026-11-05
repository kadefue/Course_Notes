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
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, KeepTogether
from compendium_base import (
    NumberedCanvas, get_custom_stylesheet, Paragraph, rectify_scientific_text,
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
        "If a 12V DC source is placed across this resistor, compute the power dissipated (<i>P</i> = <i>V</i><sup>2</sup> / <i>R</i>) and state whether a 1/4W rating is adequate.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 2 (5 Marks):</b> Explain the physical differences between an insulator, a semiconductor, and a conductor in terms of "
        "their energy band structures, forbidden energy gaps (<i>E</i><sub>g</sub>), and the presence of charge carriers at absolute zero (0 K) versus room temperature (300 K).",
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
        "<b>Question 5 (8 Marks):</b> An analog soil moisture sensor signal conditioning circuit uses a series RC low-pass filter with <i>R</i> = 15 kΩ and <i>C</i> = 4.7 μF. "
        "(a) Calculate the circuit time constant <i>τ</i> = <i>R</i> · <i>C</i>. (b) Determine the time required for the capacitor to charge from 0V to 90% of a 5V step input using <i>v</i><sub>C</sub>(<i>t</i>) = <i>V</i><sub>supply</sub> · [ 1 - <i>e</i><sup>-<i>t</i> / <i>τ</i></sup> ]. "
        "(c) Calculate the electrostatic energy stored in the capacitor <i>W</i><sub>C</sub> = 0.5 · <i>C</i> · <i>V</i><sup>2</sup> when fully charged to 5V.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 6 (9 Marks):</b> A monocrystalline silicon PN junction diode is fabricated with an acceptor doping concentration <i>N</i><sub>A</sub> = 4.0 × 10<sup>17</sup> cm<sup>-3</sup> and "
        "donor doping concentration <i>N</i><sub>D</sub> = 1.0 × 10<sup>16</sup> cm<sup>-3</sup> at a temperature <i>T</i> = 300 K (intrinsic carrier concentration <i>n</i><sub>i</sub> = 1.5 × 10<sup>10</sup> cm<sup>-3</sup>). "
        "(a) Calculate the junction built-in barrier potential <i>V</i><sub>0</sub> = <i>V</i><sub>T</sub> · ln[ (<i>N</i><sub>A</sub> · <i>N</i><sub>D</sub>) / <i>n</i><sub>i</sub><sup>2</sup> ]. (b) If the junction temperature rises to 350 K, explain qualitatively and calculate quantitatively "
        "the directional change in <i>V</i><sub>0</sub> (assume thermal voltage <i>V</i><sub>T</sub> scales linearly with <i>T</i>).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 7 (9 Marks):</b> Starting from the Shockley diode equation <i>I</i><sub>D</sub> = <i>I</i><sub>S</sub> · [ <i>e</i><sup><i>V</i><sub>D</sub> / (<i>ηV</i><sub>T</sub>)</sup> - 1 ], prove mathematically that the dynamic AC junction "
        "resistance is given by <i>r</i><sub>d</sub> = (<i>η</i> · <i>V</i><sub>T</sub>) / <i>I</i><sub>D</sub>. For a silicon diode with <i>η</i> = 1 and <i>V</i><sub>T</sub> = 26 mV, calculate <i>r</i><sub>d</sub> at: (i) <i>I</i><sub>D</sub> = 0.5 mA, (ii) <i>I</i><sub>D</sub> = 2.0 mA, and (iii) <i>I</i><sub>D</sub> = 20 mA.",
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
        "Design a 12V DC power supply to operate an automated greenhouse drip-irrigation solenoid manifold from a 230 <i>V</i><sub>rms</sub>, 50 Hz single-phase AC generator. "
        "The four solenoid valves draw a continuous load current <i>I</i><sub>dc</sub> = 2.0 A. A full-wave bridge rectifier using four 1N5404 silicon diodes (<i>V</i><sub>F</sub> = 0.8 V) "
        "with a parallel reservoir capacitor filter is selected.<br/>"
        "(a) Determine the required transformer secondary RMS voltage (<i>V</i><sub>sec</sub>) to maintain a minimum peak load voltage of 15.0 V.<br/>"
        "(b) Sizing the smoothing filter capacitor <i>C</i> using <i>V</i><sub>r(pp)</sub> = <i>I</i><sub>dc</sub> / (2 · <i>f</i> · <i>C</i>) to ensure peak-to-peak ripple voltage does not exceed 0.8 <i>V</i><sub>pp</sub>.<br/>"
        "(c) Calculate the minimum Peak Inverse Voltage (PIV) rating required for the rectifier diodes, including a 100% safety margin (PIV ≥ 2 · <i>V</i><sub>m</sub>).<br/>"
        "(d) Select an appropriate standard commercial capacitor value and specify its minimum working voltage (WVDC).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 10 (11 Marks) - Hall Effect Tractor PTO Tachometer:</b><br/>"
        "A precision digital tachometer on a tractor Power Take-Off (PTO) shaft incorporates an N-type semiconductor Hall effect sensor slab with thickness "
        "<i>t</i> = 0.20 mm and electron carrier concentration <i>n</i> = 3.2 × 10<sup>15</sup> cm<sup>-3</sup>. A regulated bias current <i>I</i><sub>x</sub> = 20 mA flows longitudinally through the sensor. "
        "When a magnetic gear tooth passes within 2 mm of the sensor, a perpendicular magnetic flux density <i>B</i><sub>z</sub> = 0.42 Tesla is measured.<br/>"
        "(a) Derive the expression for the Hall coefficient <i>R</i><sub>H</sub> = 1 / (<i>n</i> · <i>q</i>) and compute its numerical value.<br/>"
        "(b) Calculate the generated Hall voltage <i>V</i><sub>H</sub> = (<i>R</i><sub>H</sub> · <i>I</i><sub>x</sub> · <i>B</i><sub>z</sub>) / <i>t</i> in millivolts.<br/>"
        "(c) If electrical noise from the tractor alternator induces a 2.5 mV stray voltage, calculate the Signal-to-Noise Ratio (SNR) in decibels (dB) "
        "via SNR = 20 · log<sub>10</sub>(<i>V</i><sub>signal</sub> / <i>V</i><sub>noise</sub>) and suggest a differential amplifier topology to eliminate common-mode alternator noise.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 11 (11 Marks) - Sensor Analog Input Overvoltage Protection:</b><br/>"
        "An analog soil conductivity probe installed along an outdoor farm furrow is connected to a 3.3V microcontroller ADC pin via a 50-meter cable. "
        "Inductive switching from nearby borehole pumps induces AC transient spikes of ±25V peak into the cable. "
        "Design a double-diode clipper protection network using two silicon diodes (<i>V</i><sub>K</sub> = 0.7 V) and a series current-limiting resistor <i>R</i><sub>S</sub>.<br/>"
        "(a) Draw the complete circuit schematic showing connection to the 3.3V power rail and ground.<br/>"
        "(b) Determine the maximum and minimum voltages delivered to the ADC pin during ±25V transient surges (clamped to <i>V</i><sub>DD</sub> + <i>V</i><sub>K</sub> and -<i>V</i><sub>K</sub>).<br/>"
        "(c) If the maximum allowable transient current through each protection diode is 20 mA, calculate the minimum safe value <i>R</i><sub>S</sub> = (<i>V</i><sub>peak</sub> - <i>V</i><sub>clamp</sub>) / <i>I</i><sub>max</sub> and wattage rating of series resistor <i>R</i><sub>S</sub>.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 12 (12 Marks) - Capacitive Grain Moisture Sensor Filtering:</b><br/>"
        "A continuous-flow maize dryer utilizes a cylindrical coaxial capacitor sensor whose dielectric constant varies linearly with grain moisture content "
        "(<i>C</i><sub>dry</sub> = 120 pF at 12% moisture; <i>C</i><sub>wet</sub> = 480 pF at 28% moisture). The sensor is excited by a 100 kHz sinusoidal oscillator.<br/>"
        "(a) Calculate the capacitive reactance <i>X</i><sub>C</sub> = 1 / (2 · <i>π</i> · <i>f</i> · <i>C</i>) of the sensor at both dry (12%) and wet (28%) grain conditions.<br/>"
        "(b) The sensor forms an AC voltage divider with an inductor <i>L</i> to convert moisture variations into amplitude variations. "
        "Determine the required inductance <i>L</i> = 1 / [ 4 · <i>π</i><sup>2</sup> · <i>f</i><sup>2</sup> · <i>C</i> ] so that the circuit achieves electrical resonance at 100 kHz when grain moisture is exactly at the target storage value of 14% (<i>C</i> = 165 pF).<br/>"
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
        "Explain why the drain current saturates at a constant value (<i>I</i><sub>DSS</sub>) beyond pinch-off (<i>V</i><sub>DS</sub> > |<i>V</i><sub>P</sub>|) rather than dropping to zero.",
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
        "The load resistance varies from 340 Ω to 1.2 kΩ. The Zener diode has ratings: <i>V</i><sub>Z</sub> = 6.8 V, <i>I</i><sub>ZK</sub> = 3 mA, and <i>P</i><sub>Z(max)</sub> = 1.0 W. "
        "Calculate the permissible range for series current-limiting resistor <i>R</i><sub>S(min)</sub> and <i>R</i><sub>S(max)</sub> using governing boundary equations and select a suitable standard E24 resistor value.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 6 (9 Marks):</b> For a silicon NPN transistor configured in Common-Emitter mode with <i>β</i> = 120 and <i>I</i><sub>CBO</sub> = 50 nA at 25°C, "
        "(a) Calculate the Common-Base current gain <i>α</i> = <i>β</i> / (<i>β</i> + 1). (b) Calculate the open-base collector-emitter leakage current <i>I</i><sub>CEO</sub> = (<i>β</i> + 1) · <i>I</i><sub>CBO</sub>. "
        "(c) If the junction temperature rises to 75°C causing <i>I</i><sub>CBO</sub> to increase eight-fold, compute the new value of <i>I</i><sub>CEO</sub>.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 7 (9 Marks):</b> An N-channel JFET has saturation drain current <i>I</i><sub>DSS</sub> = 14 mA and pinch-off voltage <i>V</i><sub>P</sub> = -4.5 V. "
        "Using Shockley's equation <i>I</i><sub>D</sub> = <i>I</i><sub>DSS</sub> · [ 1 - (<i>V</i><sub>GS</sub> / <i>V</i><sub>P</sub>) ]<sup>2</sup>: (a) Calculate drain current <i>I</i><sub>D</sub> for <i>V</i><sub>GS</sub> = 0V, -1.0V, -2.0V, -3.0V, and -4.5V. "
        "(b) Calculate maximum transconductance <i>g</i><sub>m0</sub> = 2 · <i>I</i><sub>DSS</sub> / |<i>V</i><sub>P</sub>|. (c) Compute operating transconductance <i>g</i><sub>m</sub> at <i>V</i><sub>GS</sub> = -2.0 V.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 8 (9 Marks):</b> A Common-Emitter BJT amplifier with voltage-divider bias has circuit values: <i>V</i><sub>CC</sub> = 15 V, <i>R</i><sub>1</sub> = 47 kΩ, <i>R</i><sub>2</sub> = 12 kΩ, "
        "<i>R</i><sub>C</sub> = 3.3 kΩ, <i>R</i><sub>E</sub> = 1.2 kΩ, and <i>β</i> = 100. (a) Determine the DC quiescent operating point (<i>I</i><sub>CQ</sub>, <i>V</i><sub>CEQ</sub>). "
        "(b) Calculate the small-signal dynamic emitter resistance <i>r</i><sub>e</sub> = 26 mV / <i>I</i><sub>EQ</sub>. (c) Calculate the AC voltage gain <i>A</i><sub>v</sub> = - (<i>R</i><sub>C</sub> || <i>R</i><sub>L</sub>) / <i>r</i><sub>e</sub> assuming the emitter resistor is bypassed with a large capacitor <i>C</i><sub>E</sub>.",
        styles['DocBody']
    ))

    # PART C: AGRICULTURAL ENGINEERING SYSTEMS DESIGN
    story.append(Spacer(1, 6))
    story.append(Paragraph("PART C: Agricultural Actuator & Power Electronics Design [45 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 9 (11 Marks) - Solar Array Shading Protection:</b><br/>"
        "A solar-powered borehole water pumping installation comprises three series strings of 400W monocrystalline photovoltaic modules. "
        "Each module produces a string current <i>I</i><sub>string</sub> = 10.5 A. During dusty dry-season conditions in central Tanzania, acacia tree leaves shade one substring.<br/>"
        "(a) Explain the electrical and thermal consequences of cell reverse breakdown if bypass diodes are omitted.<br/>"
        "(b) Compare the power dissipation in a sealed IP67 junction box when using a standard silicon rectifier diode (<i>V</i><sub>F</sub> = 1.0 V at 10.5 A) "
        "versus an MBR1645 Schottky barrier diode (<i>V</i><sub>F</sub> = 0.42 V at 10.5 A) using <i>P</i> = <i>I</i> · <i>V</i><sub>F</sub>.<br/>"
        "(c) If the junction box has a thermal resistance to ambient <i>θ</i><sub>ca</sub> = 8.5 °C/W and ambient temperature is 42°C, compute the steady-state temperature inside the enclosure <i>T</i><sub>case</sub> = <i>T</i><sub>amb</sub> + <i>P</i> · <i>θ</i><sub>ca</sub> for both diode types.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 10 (11 Marks) - BJT Saturated Switch for Grain Aeration Fan:</b><br/>"
        "An automated maize storage silo uses an ESP32 microcontroller (3.3V logic, maximum safe GPIO current = 12 mA) to actuate a 12V, 15W cooling fan relay.<br/>"
        "(a) Calculate the required collector saturation current <i>I</i><sub>C(sat)</sub> = <i>P</i> / <i>V</i><sub>CC</sub>.<br/>"
        "(b) The relay is switched using a BD139 NPN power transistor with minimum saturation gain <i>β</i><sub>min</sub> = 40. "
        "Using an overdrive factor ODF = 3.0 to ensure solid saturation across temperature extremes, compute the required base current <i>I</i><sub>B(forced)</sub> = ODF · [ <i>I</i><sub>C(sat)</sub> / <i>β</i><sub>min</sub> ].<br/>"
        "(c) Sizing the series base resistor <i>R</i><sub>B</sub> = (<i>V</i><sub>GPIO</sub> - <i>V</i><sub>BE(sat)</sub>) / <i>I</i><sub>B(forced)</sub> (assume <i>V</i><sub>BE(sat)</sub> = 0.85 V) and check whether the ESP32 GPIO pin current rating is respected.<br/>"
        "(d) Explain the necessity of the anti-parallel freewheeling diode across the relay coil and specify an appropriate diode part number.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 11 (11 Marks) - Power MOSFET Thermal Sizing for 24V Solar Irrigation Pump:</b><br/>"
        "A 24V, 360W DC submersible solar pump (full-load current <i>I</i><sub>D</sub> = 15 A) is speed-controlled via PWM from an agricultural automation board. "
        "An IRF3205 N-channel Power MOSFET is selected, having on-state resistance <i>R</i><sub>DS(on)</sub> = 8.0 mΩ (0.008 Ω), junction-to-case thermal resistance <i>θ</i><sub>jc</sub> = 0.75 °C/W, "
        "and maximum rated junction temperature <i>T</i><sub>j(max)</sub> = 175°C. The control box operates in an outdoor shed where ambient temperature reaches <i>T</i><sub>amb</sub> = 45°C.<br/>"
        "(a) Calculate the static conduction power loss <i>P</i><sub>cond</sub> = <i>I</i><sub>D</sub><sup>2</sup> · <i>R</i><sub>DS(on)</sub> in the MOSFET at full 15A continuous current.<br/>"
        "(b) If junction-to-ambient thermal resistance without a heatsink is <i>θ</i><sub>ja</sub> = 62 °C/W, prove that the MOSFET will burn out if operated without a heatsink via <i>T</i><sub>j</sub> = <i>T</i><sub>amb</sub> + <i>P</i><sub>cond</sub> · <i>θ</i><sub>ja</sub>.<br/>"
        "(c) Calculate the maximum allowable heatsink thermal resistance <i>θ</i><sub>sa</sub> = [ (<i>T</i><sub>j</sub> - <i>T</i><sub>amb</sub>) / <i>P</i><sub>cond</sub> ] - <i>θ</i><sub>jc</sub> - <i>θ</i><sub>cs</sub> to maintain the MOSFET junction temperature below a safe design limit of <i>T</i><sub>j</sub> = 90°C (assume thermal grease interface <i>θ</i><sub>cs</sub> = 0.50 °C/W).",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 12 (12 Marks) - High-Impedance Soil pH Transducer Buffer:</b><br/>"
        "Glass-membrane electrochemical soil pH sensors have an extraordinarily high internal source resistance (<i>R</i><sub>source</sub> ≈ 100 MΩ to 1 GΩ) and output an analog signal "
        "of approximately 59.2 mV per pH unit at 25°C. Connecting this probe to a standard BJT amplifier causes severe signal attenuation.<br/>"
        "(a) Explain why a standard BJT amplifier cannot be used for direct buffering of a glass pH electrode.<br/>"
        "(b) Design a Common-Drain (Source Follower) buffer amplifier using a 2N5457 N-channel JFET (<i>I</i><sub>DSS</sub> = 5.0 mA, <i>V</i><sub>P</sub> = -2.5 V). "
        "Draw the circuit schematic and derive the expression for input resistance <i>R</i><sub>in</sub> and voltage gain <i>A</i><sub>v</sub> = (<i>g</i><sub>m</sub> · <i>R</i><sub>S</sub>) / (1 + <i>g</i><sub>m</sub> · <i>R</i><sub>S</sub>).<br/>"
        "(c) What precautions regarding PCB contamination (humidity, agricultural fertilizer dust, and flux residue) must be taken to maintain 10<sup>12</sup> Ω insulation resistance on the sensor board?",
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
        "overflow occurs and verify by checking the sign-bit carry condition <i>V</i> = <i>C</i><sub>in</sub> ⊕ <i>C</i><sub>out</sub>:<br/>"
        "(a) (+54) + (+82)<br/>"
        "(b) (+75) - (+98) [i.e., (+75) + (-98)]",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 3 (5 Marks):</b> Perform the BCD addition of decimal numbers 678 + 485 using 8421 BCD arithmetic. "
        "Show the binary addition for each decimal digit decade and illustrate where the +6 (0110<sub>2</sub>) correction factor must be applied.",
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
        "<b>Question 7 (9 Marks):</b> A 1-bit binary Full Adder circuit accepts inputs <i>A</i>, <i>B</i>, and <i>C</i><sub>in</sub>. "
        "(a) Construct the complete 8-row truth table for outputs Sum (<i>S</i>) and Carry-out (<i>C</i><sub>out</sub>). "
        "(b) Write the minimized Boolean expressions for <i>S</i> and <i>C</i><sub>out</sub>. (c) Draw the logic diagram using two Half Adders and an OR gate.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 8 (9 Marks):</b> Using Boolean algebra axioms and De Morgan's theorems, algebraically prove the following identities:<br/>"
        "(a) <i>A</i> + (<i>A</i> · <i>B</i>) = <i>A</i> + <i>B</i><br/>"
        "(b) (<i>A</i> + <i>B</i>) · (<i>A</i> + <i>C</i>) = <i>A</i> + <i>B</i> · <i>C</i><br/>"
        "(c) (<i>A</i> · <i>B</i> · <i>C</i>) = <i>A</i> + <i>B</i> + <i>C</i>",
        styles['DocBody']
    ))

    # PART C: BOOLEAN MINIMIZATION & AGRICULTURAL SYSTEMS SYNTHESIS
    story.append(Spacer(1, 6))
    story.append(Paragraph("PART C: K-Map Minimization & Agricultural Safety Synthesis [45 Marks]", styles['SecH1']))
    story.append(Paragraph(
        "<b>Question 9 (11 Marks) - Automated Silo Fumigation Exhaust Logic:</b><br/>"
        "A grain silo fumigation system has four safety sensors: <i>P</i> (Phosphine Gas Detected), <i>T</i> (Temperature > 35°C), <i>D</i> (Silo Access Door Closed), and <i>E</i> (Emergency Switch Active). "
        "The exhaust ventilation blower (<i>B</i>) must turn ON (<i>B</i> = 1) according to the truth function: <i>B</i>(<i>P</i>, <i>T</i>, <i>D</i>, <i>E</i>) = ∑ <i>m</i>(2, 3, 6, 7, 10, 11, 14, 15).<br/>"
        "(a) Plot this function on a 4-variable Karnaugh Map (Gray code ordered).<br/>"
        "(b) Identify all prime implicants and essential prime implicants.<br/>"
        "(c) Derive the minimized Sum of Products (SOP) expression.<br/>"
        "(d) Implement the minimized expression using NAND-NAND logic gates.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 10 (11 Marks) - Grain Dryer Burner Safety Interlock with Don't Cares:</b><br/>"
        "An automated cross-flow grain dryer burner shutoff circuit <i>F</i>(<i>A</i>, <i>B</i>, <i>C</i>, <i>D</i>) is monitored by four binary inputs: <i>A</i> = High Burner Temp; <i>B</i> = Flame Detected; "
        "<i>C</i> = Airflow Blower Running; <i>D</i> = Master Control Armed. The shutdown alarm triggers for minterms: <i>F</i> = ∑ <i>m</i>(0, 1, 4, 5, 8, 9, 12). "
        "Due to mechanical sensor interlocks, input states <i>d</i> = ∑ <i>d</i>(10, 11, 13, 14, 15) can never physically occur.<br/>"
        "(a) Map the minterms and Don't Care conditions onto a 4-variable K-map.<br/>"
        "(b) Form the largest possible groups by leveraging the Don't Care terms.<br/>"
        "(c) Write the minimal SOP expression and compare the gate count against a design that treats all Don't Cares as zeros.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 11 (11 Marks) - Autonomous Combine Harvester Header Height Controller:</b><br/>"
        "An autonomous wheat combine harvester uses three ultrasonic height sensors located on the left (<i>L</i>), center (<i>C</i>), and right (<i>R</i>) of the cutting header. "
        "Each sensor outputs '1' if the cutter bar is too close to the ground (&lt; 10 cm). A hydraulic lift actuator must raise the header (<i>Y</i> = 1) if "
        "at least two out of the three sensors indicate ground proximity, OR if an obstacle proximity sensor (<i>O</i> = 1) triggers.<br/>"
        "(a) Formulate the truth table for the 4-variable function <i>Y</i>(<i>O</i>, <i>L</i>, <i>C</i>, <i>R</i>).<br/>"
        "(b) Plot the function on a 4-variable K-map.<br/>"
        "(c) Obtain the minimal SOP expression for hydraulic lift actuation.<br/>"
        "(d) Identify any static-1 hazards and add redundant prime implicants if necessary to guarantee glitch-free hydraulic valve switching.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Question 12 (12 Marks) - Digital Agricultural Dosing Pump Controller:</b><br/>"
        "A dairy cattle automated parlor dosing system dispenses liquid nutritional supplement based on 3 binary inputs: <i>A</i> (Animal ID Validated), "
        "<i>W</i> (Animal Weight > 450 kg), and <i>M</i> (Milk Yield > 25 Liters/day). The dispenser valve <i>V</i> operates according to: <i>V</i> = <i>A</i> · (<i>W</i> · <i>M</i> + <i>W</i> · <i>M</i>) + <i>A</i> · <i>W</i> · <i>M</i>.<br/>"
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
