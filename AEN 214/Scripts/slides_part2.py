#!/usr/bin/env python3
"""
slides_part2.py
Slide content definitions for Lectures 4, 5, and 6 (26 slides each).
AEN 214: Introduction to Electronics - Sokoine University of Agriculture.
"""

import os
from pptx import Presentation
from pptx.util import Inches
from build_slides import (
    add_title_slide, add_bullet_slide, add_example_slide,
    add_case_study_slide, add_lab_slide, add_summary_slide, add_review_slide
)

def build_lecture_4_deck(prs):
    lec_num = 4
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Special Purpose Diodes",
                    "Zener Regulators, LEDs & PAR Lighting, Schottky Solar Bypass, and Photodiodes", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 4 Learning Outcomes & Practical Scope", [
        "Master Zener Diode Physics: Differentiate Zener tunneling vs avalanche breakdown, knee current I_ZK, and power limits.",
        "Design Zener Shunt Voltage Regulators: Size series resistor R_S across variable DC line voltages and fluctuating sensor loads.",
        "Analyze Light Emitting Diodes (LEDs): Evaluate direct vs indirect bandgap physics, forward drop V_F, and electroluminescence.",
        "Apply LEDs to Photosynthetic Lighting: Calculate Photosynthetically Active Radiation (PAR) and Photosynthetic Photon Flux (PPF).",
        "Evaluate Schottky Barrier Diodes: Metal-semiconductor junction physics, ultra-low forward drop (0.3V), and zero reverse recovery.",
        "Implement Solar Panel Bypass Protection: Prevent hot-spot thermal damage and current choking in shaded photovoltaic strings.",
        "Understand Optical & Surge Devices: Analyze PIN photodiodes, solar cells, and Transient Voltage Suppressors (TVS)."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "Special Purpose Diodes in AgriTech Systems", [
        "Unregulated Off-Grid Power: Solar panels and battery banks experience severe voltage swings (10.5V to 14.8V).",
        "Stable Reference Voltages: Zener diodes provide ultra-stable 3.3V and 5.0V voltage references for microcontroller ADCs.",
        "Controlled-Environment Agriculture (CEA): High-efficiency LED grow luminaires deliver tailored spectral recipes in Arusha greenhouses.",
        "Solar Water Pumping Efficiency: High forward voltage drops across ordinary silicon diodes waste valuable solar energy.",
        "Schottky Diodes in Solar Arrays: Reduce bypass conduction power losses by 60%, delivering more water per kilowatt of solar PV."
    ], image_file="img_zener_diode.jpg", current_slide=3, total_slides=total)

    # 4. Zener Diode Fundamentals
    add_bullet_slide(prs, "Zener Diode Fundamentals & Breakdown Physics", [
        "Heavy Doping Profile: Silicon PN junction with high impurity doping (10^18 to 10^19 cm^-3); extremely narrow depletion layer (< 10 nm).",
        "Reverse Breakdown Characteristic: In reverse bias, voltage remains almost perfectly constant at V_Z despite huge current changes.",
        "Zener Knee Current (I_ZK): Minimum reverse current required to enter the stable breakdown voltage plateau (typically 0.25 to 1.0 mA).",
        "Zener Test Current (I_ZT): Specified manufacturer test current where nominal Zener voltage V_Z is guaranteed (typically 5 to 20 mA).",
        "Maximum Zener Current (I_ZM): Maximum safe reverse current limited by package thermal dissipation: I_ZM = P_Z(max) / V_Z."
    ], image_file="fig4_2_zener_iv_characteristics.png", current_slide=4, total_slides=total)

    # 5. Zener Dynamic Impedance & Tempco
    add_bullet_slide(prs, "Zener Dynamic Impedance & Temperature Coefficient", [
        "Dynamic Zener Impedance: r_z = Delta V_Z / Delta I_Z; The inverse slope of the vertical breakdown I-V characteristic.",
        "Ideal vs Practical Model: Ideal Zener: r_z = 0 (perfect battery V_Z); Practical Zener: V_Z(actual) = V_Z0 + I_Z · r_z.",
        "Regulation Quality: Lower dynamic impedance r_z yields stiffer voltage regulation against load current fluctuations.",
        "Temperature Coefficient (TC): Quantifies Zener voltage drift with temperature: TC = (Delta V_Z / V_Z) / Delta T x 100% (°C^-1).",
        "Zero-Tempco Point: Diodes with V_Z ≈ 5.6 V achieve nearly zero temperature drift because negative Zener and positive Avalanche TC cancel!"
    ], current_slide=5, total_slides=total)

    # 6. Zener Shunt Voltage Regulator Architecture
    add_bullet_slide(prs, "Zener Shunt Voltage Regulator Architecture", [
        "Circuit Topology: Series ballast resistor R_S placed between unregulated DC supply V_in and parallel combination of Zener and load R_L.",
        "Kirchhoff's Current Law: Total input current I_S splits into Zener current and load current: I_S = I_Z + I_L.",
        "Voltage Dropping Action: Series resistor drops the difference voltage: V_RS = V_in - V_Z; Current I_S = (V_in - V_Z) / R_S.",
        "Line Regulation: When input V_in increases, excess current shunts through Zener diode (Delta I_Z), keeping V_out = V_Z rock steady.",
        "Load Regulation: When load R_L pulls more current I_L, current is diverted away from Zener diode without changing V_out."
    ], image_file="fig4_1_zener_regulator_schematic.png", current_slide=6, total_slides=total)

    # 7. Zener Regulator Design Criteria
    add_bullet_slide(prs, "Design Boundaries for Zener Shunt Regulators", [
        "Condition 1 (Minimum Input Voltage & Maximum Load Current): Zener must maintain minimum knee current I_ZK to prevent dropout.",
        "Maximum Resistor Value: R_S(max) = (V_in(min) - V_Z) / (I_L(max) + I_ZK).",
        "Condition 2 (Maximum Input Voltage & Minimum Load Current): Zener must not exceed maximum thermal dissipation P_Z(max).",
        "Minimum Resistor Value: R_S(min) = (V_in(max) - V_Z) / (I_L(min) + I_ZM), where I_ZM = P_Z(max) / V_Z.",
        "Ballast Resistor Wattage: Resistor power rating must withstand maximum dissipation: P_RS = (V_in(max) - V_Z)² / R_S."
    ], current_slide=7, total_slides=total)

    # 8. Worked Example 1: Zener Regulator
    add_example_slide(prs, 1, "Zener Shunt Regulator for Greenhouse Soil Moisture ADC",
                      "Design a 5.1V Zener shunt voltage regulator to power a precision soil moisture ADC module in a Morogoro greenhouse. Unregulated DC supply varies between V_in(min) = 11.0 V and V_in(max) = 15.0 V. The ADC load current varies from I_L(min) = 5.0 mA to I_L(max) = 35.0 mA. The 1N4733A Zener diode has V_Z = 5.1 V, P_Z(max) = 1.0 W, and knee current I_ZK = 1.0 mA. Determine: (a) Maximum allowable R_S, (b) Minimum allowable R_S, (c) Standard 5% resistor selection, (d) Resistor power rating.",
                      [
                          "1. Calculate Maximum Allowable Zener Current: I_ZM = P_Z(max) / V_Z = 1.0 W / 5.1 V = 0.1961 A = 196.1 mA.",
                          "2. Calculate R_S(max) to Guarantee Regulation at Worst-Case Low Input:",
                          "   R_S(max) = (V_in(min) - V_Z) / (I_L(max) + I_ZK) = (11.0 V - 5.1 V) / (35.0 mA + 1.0 mA) = 5.9 V / 36.0 mA = 163.9 Ohm.",
                          "3. Calculate R_S(min) to Prevent Zener Burnout at Worst-Case High Input:",
                          "   R_S(min) = (V_in(max) - V_Z) / (I_L(min) + I_ZM) = (15.0 V - 5.1 V) / (5.0 mA + 196.1 mA) = 9.9 V / 201.1 mA = 49.2 Ohm.",
                          "4. Standard Resistor Selection: Choose standard value within 49.2 Ohm < R_S < 163.9 Ohm. Select standard R_S = 100 Ohm (5%).",
                          "5. Resistor Power Rating: P_RS(max) = (V_in(max) - V_Z)² / R_S = (15.0 - 5.1)² / 100 = (9.9)² / 100 = 0.980 W. (Use 2.0 W wirewound resistor with 50% safety factor)."
                      ], current_slide=8, total_slides=total)

    # 9. Light Emitting Diodes (LEDs)
    add_bullet_slide(prs, "Light Emitting Diodes: Electroluminescence Physics", [
        "Direct vs Indirect Bandgap: Silicon has indirect bandgap (recombination yields heat/phonons); compound semiconductors have direct bandgap.",
        "Spontaneous Photon Emission: Forward bias injects electrons and holes; radiative recombination emits photons with energy E = h · f = h · c / lambda.",
        "Emission Wavelength: lambda = (h · c) / E_g ≈ 1240 / E_g(eV) (nanometers). Bandgap energy E_g dictates emitted color!",
        "Semiconductor Materials: Gallium Arsenide (GaAs: Infrared, 900 nm), AlGaInP (Red/Amber, 620-660 nm), InGaN (Blue/Green/UV, 450 nm).",
        "Forward Voltage Drop Disparity: Red LEDs: V_F ≈ 1.8V to 2.1V; Blue/White LEDs: V_F ≈ 3.0V to 3.4V (proportional to bandgap energy!)."
    ], image_file="fig4_3_led_operation.png", current_slide=9, total_slides=total)

    # 10. Agricultural Horticultural LED Lighting
    add_bullet_slide(prs, "Photosynthetically Active Radiation (PAR) & Grow Lighting", [
        "Chlorophyll Absorption Peaks: Chlorophyll 'a' absorbs heavily at 430 nm (deep blue) and 662 nm (deep red); Chlorophyll 'b' at 453 nm and 642 nm.",
        "Photosynthetically Active Radiation (PAR): Spectral waveband from 400 nm to 700 nm driving crop photosynthesis.",
        "Photosynthetic Photon Flux (PPF): Total micromoles of PAR photons emitted per second (micro-mol/s); efficacy > 2.8 micro-mol/Joule.",
        "Spectral Tuning Recipes: High blue ratio (450 nm) prevents stem elongation and promotes leafy growth; Deep red (660 nm) accelerates flowering.",
        "Commercial CEA Advantage: LED luminaires produce 65% less radiant heat than high-pressure sodium (HPS) lamps, cutting greenhouse cooling costs."
    ], image_file="img_led_macro.jpg", current_slide=10, total_slides=total)

    # 11. Worked Example 2: LED Current Limiting & Array
    add_example_slide(prs, 2, "PAR LED Grow Light String Sizing for Arusha Roses",
                      "A commercial floriculture greenhouse in Arusha utilizes high-intensity deep-red LED arrays (lambda = 660 nm) for supplemental flowering stimulation. Each LED has forward voltage V_F = 2.20 V at rated continuous forward current I_F = 350 mA. The string is powered from a regulated 24.0 V DC power bus. Determine: (a) Maximum number of series LEDs in one string, (b) Series ballast resistor R_limit, (c) Resistor power dissipation, (d) Electrical efficiency of the string.",
                      [
                          "1. Determine Maximum Series LED Count: Total LED drop must not exceed supply: N · V_F < V_supply -> N < 24.0 V / 2.20 V = 10.9.",
                          "   Allowing a 2.0 V headroom for stable current regulation, choose N = 9 series LEDs.",
                          "2. Total Series LED Forward Voltage: V_string = 9 · 2.20 V = 19.80 V.",
                          "3. Ballast Resistor Calculation: V_R = V_supply - V_string = 24.0 V - 19.80 V = 4.20 V.",
                          "   R_limit = V_R / I_F = 4.20 V / 0.350 A = 12.0 Ohm.",
                          "4. Resistor Power Dissipation: P_R = I_F² · R_limit = (0.350 A)² · 12.0 Ohm = 0.1225 · 12.0 = 1.47 W. (Use 3.0W or 5.0W rating).",
                          "5. Electrical Efficiency of String: P_LEDs = 19.80 V · 0.35 A = 6.93 W; P_total = 24.0 V · 0.35 A = 8.40 W.",
                          "   Efficiency eta = P_LEDs / P_total = 6.93 W / 8.40 W = 82.5%."
                      ], current_slide=11, total_slides=total)

    # 12. Schottky Barrier Diodes
    add_bullet_slide(prs, "Schottky Barrier Diodes: Metal-Semiconductor Physics", [
        "Metal-Semiconductor Junction: Replaces the P-type region with a deposited metal barrier (Platinum, Tungsten, or Chromium on N-type silicon).",
        "Majority Carrier Conduction: Operates purely via thermionic electron emission over the Schottky barrier height q·Phi_B.",
        "Zero Minority Carrier Storage: Since no holes are injected into N-silicon, reverse recovery time is virtually zero (t_rr < 100 picoseconds).",
        "Ultra-Low Forward Voltage Drop: V_F ≈ 0.25 V to 0.45 V at typical currents (roughly half that of a standard PN junction diode).",
        "Trade-Offs: Higher reverse leakage current (microA to mA) and lower maximum reverse breakdown voltage (typically V_RRM <= 100 V)."
    ], image_file="fig4_4_schottky_diode.png", current_slide=12, total_slides=total)

    # 13. Solar Photovoltaic Bypass Protection
    add_bullet_slide(prs, "Solar Panel Hot-Spot Prevention via Bypass Diodes", [
        "The Shading Vulnerability: When dust, bird droppings, or tree shadows obscure one cell in a series string, that cell stops generating current.",
        "Reverse Bias Choking: Unshaded cells force full string current through the shaded cell, driving it into heavy reverse bias (V_rev > 25V).",
        "Hot-Spot Destruction: The shaded cell dissipates all string power as localized heat (P = I_string · V_rev > 150W), melting EVA encapsulation and cracking glass.",
        "Bypass Diode Action: Placing anti-parallel Schottky diodes across groups of 18–24 cells provides an alternate low-resistance bypass path.",
        "Schottky Thermal Advantage: With 10A string current, a standard silicon diode dissipates P = 10A · 0.9V = 9.0W; a Schottky dissipates only 10A · 0.38V = 3.8W."
    ], image_file="img_schottky_diode.jpg", current_slide=13, total_slides=total)

    # 14. Worked Example 3: Schottky Solar Bypass Sizing
    add_example_slide(prs, 3, "Thermal Sizing of Solar Bypass Diodes at Dodoma",
                      "A 400W solar photovoltaic module installed at a Dodoma borehole pumping station consists of 72 series cells partitioned into 3 sub-strings of 24 cells each, protected by 3 bypass diodes in the junction box. The module short-circuit current is I_sc = 11.2 A. Under cloud edge shading, one sub-string is fully bypassed. Ambient temperature inside the junction box reaches T_amb = 55°C. Compare: (a) Standard 15A silicon rectifier (V_F = 0.85V, theta_JA = 8.5°C/W), versus (b) 15A Schottky diode (V_F = 0.36V, theta_JA = 8.5°C/W). Determine junction temperatures.",
                      [
                          "1. Power Dissipated in Standard Silicon Diode: P_Si = I_sc · V_F(Si) = 11.2 A · 0.85 V = 9.52 W.",
                          "2. Junction Temperature Rise for Silicon Diode: Delta T_Si = P_Si · theta_JA = 9.52 W · 8.5°C/W = 80.9°C.",
                          "   Total Silicon Junction Temp: T_J(Si) = T_amb + Delta T_Si = 55°C + 80.9°C = 135.9°C. ( dangerously close to 150°C silicon limit!).",
                          "3. Power Dissipated in Schottky Diode: P_Schottky = I_sc · V_F(Schottky) = 11.2 A · 0.36 V = 4.032 W.",
                          "4. Junction Temperature Rise for Schottky Diode: Delta T_Schottky = P_Schottky · theta_JA = 4.032 W · 8.5°C/W = 34.3°C.",
                          "   Total Schottky Junction Temp: T_J(Schottky) = 55°C + 34.3°C = 89.3°C (comfortable 60°C safety margin!).",
                          "5. Engineering Conclusion: Schottky diodes cut junction box heat generation by 58%, preventing junction box melting."
                      ], current_slide=14, total_slides=total)

    # 15. Photodiodes & Solar Cells
    add_bullet_slide(prs, "Photodiodes & Solar Photovoltaic Transducers", [
        "Reverse-Biased Operation: Photodiodes operate in the 3rd quadrant (reverse bias) where photocurrent is strictly proportional to light intensity.",
        "Internal Photoelectric Effect: Incident photons with energy h·f > E_g break valence bonds, creating electron-hole pairs in the depletion layer.",
        "Electric Field Sweep: Internal junction field instantly sweeps electrons to N and holes to P, generating photocurrent: I_photo = R_lambda · P_opt.",
        "PIN Photodiode: Wide intrinsic (I) layer sandwiched between P and N widens depletion volume, maximizing optical sensitivity and speed.",
        "Solar Photovoltaic Cell: Operates in the 4th quadrant (forward bias, delivering power); large-area silicon PN junction optimized for solar energy."
    ], current_slide=15, total_slides=total)

    # 16. Transient Voltage Suppressor (TVS) Diodes
    add_bullet_slide(prs, "Transient Voltage Suppressors (TVS) for Farm Transients", [
        "Silicon Avalanche Diodes: Engineered specifically for high-energy transient absorption rather than continuous steady-state regulation.",
        "Response Time: Ultra-fast picosecond response clamping time (< 1 ps), clamping electrostatic discharge (ESD) and lightning surges.",
        "Peak Pulse Power Ratings: Standard packages absorb 400W, 600W, 1,500W (1.5KE series), or 5,000W for standard 10/1000 microsecond surge pulses.",
        "Unidirectional vs Bidirectional TVS: Unidirectional used on DC supplies; bidirectional (back-to-back Zeners) used on AC lines and CAN-bus telemetry.",
        "Tractor CAN-Bus Protection: Bidirectional TVS clamps differential data lines (CAN_H, CAN_L) to prevent transceiver chip latch-up."
    ], current_slide=16, total_slides=total)

    # 17. Varactor & Tunnel Diodes
    add_bullet_slide(prs, "Varactor & Tunnel Diodes in Agricultural Communications", [
        "Varactor Diode (Varicap): Silicon diode designed to exploit variable junction capacitance under reverse bias: C_j proportional to (V_R + V_0)^-n.",
        "Voltage-Controlled Tuning: By altering reverse DC voltage from 1V to 15V, capacitance tunes from 100 pF to 10 pF.",
        "VCO & Farm IoT Transceivers: Frequency modulation in LoRa/Zigbee farm telemetry radios transmitting soil moisture data across large plantations.",
        "Tunnel (Esaki) Diode: Extremely degenerate doping (10^20 cm^-3); produces negative differential resistance (dV/dI < 0) at low forward bias.",
        "Negative Resistance Oscillation: Used in microwave Doppler radar ground-speed sensors mounted underneath tractors to monitor wheel slippage."
    ], current_slide=17, total_slides=total)

    # 18. Optical Coupling & Isolation
    add_bullet_slide(prs, "Optocouplers: Galvanic Isolation in Farm Automation", [
        "Physical Structure: Infrared LED optically coupled to a silicon phototransistor inside a light-tight DIP package.",
        "Galvanic Isolation: Provides 2,500V to 5,000V of electrical isolation between sensitive microcontrollers and noisy farm power machinery.",
        "Ground Loop Elimination: Eliminates ground potential differences between remote pumping stations and central farm control computers.",
        "Current Transfer Ratio (CTR): Percentage ratio of phototransistor collector current to LED forward current: CTR = (I_C / I_F) x 100%.",
        "Solid-State Relays (SSRs): High-voltage optocouplers driving anti-parallel TRIACs to silently switch AC irrigation pumps without contact bounce."
    ], current_slide=18, total_slides=total)

    # 19. Practical Field Derating & Heat Sinking
    add_bullet_slide(prs, "Thermal Engineering & Field Packaging for Diodes", [
        "Junction-to-Case Thermal Resistance (theta_JC): Heat flow path from silicon die to metal tab; requires thermal grease (silicone paste).",
        "Heat Sink Selection: Total thermal resistance theta_total = theta_JC + theta_CS + theta_SA; determines maximum safe continuous current.",
        "Dust Blanket Derating: In dusty grain elevator environments, derate heatsink thermal dissipation by 35% due to insulating particulate layer.",
        "Solar Panel Junction Box Ingress: Junction boxes must meet IP67 hermetic ingress standards to block torrential monsoonal rains.",
        "TVS Surge Coordination: Pair TVS diodes with upstream polymeric PTC reset fuses to guarantee sustained protection against long-duration overvoltages."
    ], current_slide=19, total_slides=total)

    # 20. Case Study 1
    add_case_study_slide(prs, 1, "Schottky Solar Bypass Retrofit at Dodoma Borehole",
                         "Makutupora Groundwater Basin, Dodoma Region, Tanzania",
                         "A 15 kW solar photovoltaic borehole pumping installation powering community drip irrigation suffered melted junction boxes and cracked solar panels. Acacia tree morning shadows across bottom panel rows caused unshaded cells to drive shaded strings into intense reverse breakdown, melting bypass diode solder and starting localized fires.",
                         "SUA agricultural engineers inspected the failed junction boxes and discovered factory-fitted standard silicon diodes that overheated under the 10.8A string current. Engineers retrofitted the entire 48-panel array with 15A, 45V trench Schottky barrier diodes (V1545PW) mounted on anodized aluminum heat spreader clips.",
                         [
                             "Reduced junction box operating temperatures from 142°C to a stable 76°C under full shading.",
                             "Completely eliminated solar panel hot-spot burnouts across 3 years of operation.",
                             "Increased annual solar water delivery by 8.4% through reduced diode conduction losses."
                         ], current_slide=20, total_slides=total)

    # 21. Case Study 2
    add_case_study_slide(prs, 2, "PAR LED Spectrum Optimization for Greenhouse Roses",
                         "Mount Meru Floriculture Estate, Arusha Region, Tanzania",
                         "A high-value export greenhouse growing premium roses experienced delayed flowering cycles during overcast rainy seasons. Conventional high-pressure sodium (HPS) lighting consumed excessive electrical power (400W per lamp) and generated intense radiant heat that scorched delicate flower petals.",
                         "SUA horticulture and mechatronics engineers installed tailored multi-spectral LED luminaire arrays combining 660 nm deep red (75%), 450 nm royal blue (15%), and 730 nm far red (10%). The LED fixtures delivered a uniform photosynthetic photon flux density (PPFD) of 220 micro-mol/m²·s directly over the crop canopy with precise dimming control.",
                         [
                             "Shortened flower maturation cycle by 9 days, enabling peak Valentine's Day export delivery.",
                             "Electrical lighting energy consumption slashed by 54% compared to HPS lamps.",
                             "Petal scorching completely eliminated due to low-heat solid-state lighting emission."
                         ], current_slide=21, total_slides=total)

    # 22. Laboratory Bench Protocol
    add_lab_slide(prs, "Zener Shunt Regulation & LED Spectrum Characterization", [
        "Measure Zener diode breakdown curve and evaluate knee current I_ZK on curve tracer.",
        "Build a 5.1V Zener shunt regulator and measure line regulation and load regulation.",
        "Determine the forward voltage drop V_F of Red, Green, Blue, and White LEDs.",
        "Characterize a Schottky diode against a silicon diode to observe forward drop disparity."
    ], [
        "Step 1: Wire 5.1V Zener diode (1N4733A) in series with 470 Ohm resistor to variable DC bench supply.",
        "Step 2: Sweep DC supply from 0V to 15V; record V_Z and I_Z; identify Zener knee point on graph.",
        "Step 3: Connect variable decade resistance box as load R_L; vary I_L from 0 to 30 mA; log V_out to calculate load regulation %.",
        "Step 4: Test Red (GaAsP), Green (GaP), and Blue (InGaN) LEDs at I_F = 15 mA; verify relationship between photon energy and V_F.",
        "Step 5: Measure forward voltage of 1N5819 Schottky vs 1N4007 silicon diode at 500 mA on DSO; confirm 0.35V vs 0.85V drop."
    ], current_slide=22, total_slides=total)

    # 23. Troubleshooting & Pitfalls
    add_bullet_slide(prs, "Diagnostic Troubleshooting of Special Purpose Diodes", [
        "Zener Regulator Dropout: If input voltage V_in dips too low, Zener drops below knee current I_ZK and output loses regulation.",
        "Zener Thermal Burnout: If load is disconnected without sizing R_S for full load removal, all current shunts through Zener, exceeding P_Z(max).",
        "LED Reverse Voltage Vulnerability: Most LEDs have low reverse breakdown ratings (V_R < 5V); easily destroyed if connected backwards to 12V rails.",
        "Schottky Thermal Leakage Runaway: In high-temperature engine compartments, Schottky reverse leakage surges exponentially, causing runaway.",
        "TVS Degradation: Repeated intense lightning surges cause TVS diodes to degrade and eventually fail as a permanent low-resistance short circuit."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "Differentiate between Zener breakdown and Avalanche breakdown in terms of physical mechanism, voltage thresholds, and temperature coefficients.",
        "Why is a ballast resistor R_S mandatory in a Zener shunt regulator circuit, and what happens if R_S is made too large or too small?",
        "Explain why compound semiconductors (e.g. GaAs, InGaN) emit light efficiently upon forward bias, while elemental silicon does not.",
        "Why are Schottky barrier diodes preferred over standard PN junction diodes as bypass diodes in solar photovoltaic panels?",
        "A 6.2V Zener diode has dynamic resistance r_z = 5.0 Ohm. If Zener current increases by 15 mA, calculate the change in regulated voltage."
    ], "Lecture 5 will explore the Bipolar Junction Transistor (BJT): Physics, biasing rules, CE/CB/CC configurations, DC load lines, and switches.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "Zener diodes provide highly stable voltage references when operated in reverse breakdown (V_Z).",
        "Zener shunt regulator design requires sizing R_S between R_S(min) and R_S(max) to balance dropout and thermal limits.",
        "LEDs convert electrical energy directly into light via radiative recombination in direct-bandgap materials.",
        "Tailored LED spectra (PAR: 450 nm blue + 660 nm red) dramatically improve greenhouse crop photosynthesis.",
        "Schottky barrier diodes offer ultra-low forward drops (0.3V) and zero t_rr, making them ideal for solar bypass protection."
    ], [
        "Zener Power Limit: P_Z(max) = V_Z · I_ZM",
        "Ballast Resistor Max: R_S(max) = (V_in(min) - V_Z) / (I_L(max) + I_ZK)",
        "Ballast Resistor Min: R_S(min) = (V_in(max) - V_Z) / (I_L(min) + I_ZM)",
        "LED Photon Wavelength: lambda = 1240 / E_g(eV) (nm)",
        "Schottky Forward Drop: V_F ≈ 0.25 V to 0.45 V",
        "Photocurrent: I_photo = R_lambda · P_optical",
        "Junction Temperature: T_J = T_amb + P_diss · theta_JA"
    ], current_slide=25, total_slides=total)

    # 26. References & Reading List
    add_bullet_slide(prs, "Prescribed References & Practical Laboratory Preparation", [
        "Boylestad, R. L., & Nashelsky, L. (2018). Electronic Devices and Circuit Theory (11th ed.). Pearson Education.",
        "Sedra, A. S., & Smith, K. C. (2020). Microelectronic Circuits (8th ed.). Oxford University Press.",
        "Floyd, T. L. (2017). Electronic Devices: Conventional Current Version (10th ed.). Pearson.",
        "Laboratory Preparation: Review LED current limiting resistor calculations before attending Lab Session 4.",
        "Field Assignment: Complete Assignment 2, Questions 1 to 4 on special purpose diodes and submit via SUA LMS."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

def build_lecture_5_deck(prs):
    lec_num = 5
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Bipolar Junction Transistor (BJT)",
                    "Physics, Biasing Rules, Operating Regions, DC Load Line, Saturated Switches & CE Amplifiers", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 5 Learning Outcomes & Practical Scope", [
        "Understand BJT Construction: Analyze physical doping, base width, NPN vs PNP topologies, and symbols.",
        "Master BJT Biasing Rules: Forward-biased emitter-base junction, reverse-biased collector-base junction, and voltages.",
        "Relate Transistor Currents: Derive I_E = I_B + I_C, current gains alpha and beta, and evaluate relationship beta = alpha / (1 - alpha).",
        "Analyze Circuit Configurations: Compare Common-Emitter (CE), Common-Base (CB), and Common-Collector (CC) modes.",
        "Plot Characteristic Curves & DC Load Line: Locate Cutoff, Active, and Saturation regions; determine Q-point.",
        "Prevent Thermal Runaway: Quantify leakage current I_CEO and design negative feedback emitter degeneration.",
        "Design Saturated Transistor Switches & CE Amplifiers: Interface microcontrollers to heavy farm relays, solenoids, and sensors."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "The Transistor: The Engine of Agricultural Electronics", [
        "The Solid-State Revolution: Replaced fragile mechanical contacts with robust solid-state amplification and switching.",
        "Microcontroller Actuator Driving: Arduino/ESP32 pins deliver only 20 mA; transistors switch 2A solenoids and 10A tractor fans.",
        "Sensor Signal Conditioning: Microvolt outputs from load cells and pH probes are amplified linearly by BJT stages before digitization.",
        "Harsh Agro-Climatic Thermal Stress: High ambient temperatures in engine bays and silos risk transistor thermal runaway.",
        "Reliable Machinery Automation: Understanding BJT saturation guarantees that irrigation valves open fully without burning out transistors."
    ], image_file="img_bjt_to92.jpg", current_slide=3, total_slides=total)

    # 4. BJT Physical Structure & Topology
    add_bullet_slide(prs, "BJT Physical Structure: Doping & Geometry", [
        "Three-Terminal Architecture: Composed of three distinct semiconductor regions: Emitter (E), Base (B), and Collector (C).",
        "Emitter Region: Heavily doped (N⁺⁺ in NPN) to inject a massive quantity of majority charge carriers into the base.",
        "Base Region: Extremely thin (< 1 micrometer) and lightly doped (P⁻ in NPN) to minimize electron-hole recombination (< 1-2%).",
        "Collector Region: Moderately doped (N⁻) and physically large to dissipate heat generated by collecting carriers.",
        "Topologies: NPN Transistor (electrons are majority carriers; faster, most common); PNP Transistor (holes are majority carriers)."
    ], image_file="fig5_1_bjt_structure_symbols.png", current_slide=4, total_slides=total)

    # 5. Core Operating Physics & Biasing Rules
    add_bullet_slide(prs, "BJT Conduction Physics & Two Fundamental Biasing Rules", [
        "Rule 1 (Base-Emitter Forward Bias): The base-emitter junction must be forward biased: V_BE ≈ 0.70 V for Silicon (0.3V for Ge).",
        "Rule 2 (Base-Collector Reverse Bias): The base-collector junction must be reverse biased: V_CB > 0 V (i.e. V_C > V_B in NPN).",
        "Carrier Injection Mechanism: Forward-biased BE junction injects massive flood of electrons from emitter into the ultra-thin base.",
        "Base Transit: Over 98-99% of injected electrons diffuse across the thin base without recombining, reaching the collector junction.",
        "Collector Sweeping: The intense reverse-bias electric field at the CB junction sweeps electrons into the collector, forming I_C."
    ], current_slide=5, total_slides=total)

    # 6. Transistor Currents & Current Gains
    add_bullet_slide(prs, "Kirchhoff's Current Law & BJT Current Gains", [
        "Current Conservation: By Kirchhoff's Current Law: I_E = I_B + I_C (Emitter current equals base plus collector current).",
        "Common-Base Current Gain (alpha): The fraction of emitter current reaching collector: alpha = I_C / I_E (typically 0.980 to 0.998).",
        "Common-Emitter Current Gain (beta or h_FE): Current amplification factor: beta = I_C / I_B (typically 50 to 400+).",
        "Inter-Gain Mathematical Relationship: Since I_E = I_B + I_C: beta = alpha / (1 - alpha); alpha = beta / (beta + 1).",
        "Base Current Magnitude: I_B = I_C / beta; Base current is minuscule compared to collector and emitter currents."
    ], current_slide=6, total_slides=total)

    # 7. BJT Circuit Configurations
    add_bullet_slide(prs, "Comparative BJT Circuit Configurations", [
        "Common-Emitter (CE): Input on Base, Output on Collector. High voltage gain (A_v > 100), high current gain (beta), 180° phase inversion.",
        "Common-Collector (CC / Emitter Follower): Input on Base, Output on Emitter. Unity voltage gain (A_v ≈ 1), high current gain.",
        "CC Impedance Transformation: High input impedance (Z_in > 100 kOhm) and low output impedance (Z_out < 50 Ohm); ideal sensor buffer.",
        "Common-Base (CB): Input on Emitter, Output on Collector. Current gain alpha < 1, high voltage gain, non-inverting; used in high-frequency RF.",
        "Agricultural Preference: CE is standard for digital switching and audio preamps; CC is standard for high-impedance transducer buffering."
    ], current_slide=7, total_slides=total)

    # 8. Transistor Static Characteristic Curves
    add_bullet_slide(prs, "BJT Common-Emitter Output Characteristics", [
        "Output Characteristic Family: Plots Collector Current I_C versus Collector-Emitter Voltage V_CE for various constant Base Currents I_B.",
        "Cutoff Region: I_B = 0; both junctions reverse-biased; I_C ≈ I_CEO ≈ 0; transistor behaves as an open switch.",
        "Active (Linear) Region: BE forward-biased, CB reverse-biased; I_C = beta · I_B (nearly horizontal curves); used for linear amplification.",
        "Saturation Region: Both junctions forward-biased; V_CE drops to saturation voltage V_CE(sat) ≈ 0.1V to 0.2V; behaves as a closed switch.",
        "Breakdown Limit: Exceeding maximum collector-emitter rating V_CEO causes avalanche punch-through and transistor destruction."
    ], image_file="fig5_2_bjt_ce_output_characteristics.png", current_slide=8, total_slides=total)

    # 9. DC Load Line Analysis & Q-Point
    add_bullet_slide(prs, "DC Load Line Analysis & Optimal Q-Point", [
        "Kirchhoff's Voltage Law in Output Loop: V_CC = I_C · R_C + V_CE -> I_C = (V_CC / R_C) - (V_CE / R_C).",
        "Load Line Endpoints: Point 1 (Saturation): V_CE = 0 -> I_C(sat) = V_CC / R_C; Point 2 (Cutoff): I_C = 0 -> V_CE(cutoff) = V_CC.",
        "Quiescent Operating Point (Q-point): The specific steady-state DC operating point (V_CEQ, I_CQ) at the intersection of load line and I_B curve.",
        "Optimal Linear Biasing: For maximum undistorted AC output swing in amplifiers, place Q-point at the center: V_CEQ = V_CC / 2.",
        "Digital Switching Biasing: Transistor switches between Cutoff (I_C = 0, V_CE = V_CC) and Full Saturation (V_CE = V_CE(sat), I_C = I_C(sat))."
    ], current_slide=9, total_slides=total)

    # 10. Thermal Runaway & Leakage Currents
    add_bullet_slide(prs, "Leakage Currents & Thermal Runaway Mitigation", [
        "Reverse Collector-Base Leakage (I_CBO): Minority carrier leakage across reverse-biased CB junction with emitter open.",
        "Collector-Emitter Leakage (I_CEO): I_CEO = (beta + 1) · I_CBO; Base leakage is amplified by beta! Doubles every 10°C rise in temperature.",
        "The Thermal Runaway Feedback Loop: Temperature rise -> I_CBO surges -> I_C increases -> Power dissipation P_D = V_CE · I_C increases -> Heat increases -> Melts silicon!",
        "Emitter Degeneration Resistor (R_E): Placing resistor R_E in emitter leg provides negative feedback: If I_C rises -> V_E = I_E · R_E rises -> V_BE = V_B - V_E drops -> I_C drops!",
        "Stability Factor (S): S = dI_C / dI_CBO; Lower S provides superior bias stability against temperature fluctuations in tractor engine compartments."
    ], current_slide=10, total_slides=total)

    # 11. Voltage Divider Bias (Universal Bias)
    add_bullet_slide(prs, "Voltage Divider Bias: Universal Circuit Architecture", [
        "Beta-Independent Biasing: Simple base resistor bias is heavily dependent on beta (which varies 300% across batches and temperature).",
        "Voltage Divider Topology: Resistors R_1 and R_2 form a stiff divider across supply V_CC, establishing fixed base voltage V_B.",
        "Thevenin Equivalent Analysis: V_TH = V_CC · [ R_2 / (R_1 + R_2) ]; R_TH = R_1 || R_2 = (R_1 · R_2) / (R_1 + R_2).",
        "Collector Current Equation: I_C ≈ I_E = (V_TH - V_BE) / [ R_E + (R_TH / (beta + 1)) ].",
        "Stiff Bias Design Condition: Design divider current to be at least 10 times base current: I_div >= 10 · I_B -> R_TH <= 0.10 · beta · R_E.",
        "Universal Stability: When condition holds: I_C ≈ (V_TH - 0.7 V) / R_E; completely independent of beta!"
    ], image_file="fig5_3_voltage_divider_bias.png", current_slide=11, total_slides=total)

    # 12. Worked Example 1: Voltage Divider Bias
    add_example_slide(prs, 1, "Universal Voltage Divider DC Bias Design",
                      "Design a stable voltage divider bias network for a 2N3904 NPN transistor in a Morogoro weather station anemometer pre-amplifier. Specifications: V_CC = 12.0 V, target quiescent collector current I_CQ = 2.0 mA, collector voltage V_CQ = 6.0 V, and beta = 150. Use standard design rules: set emitter voltage V_E = 0.10 · V_CC (1.2 V) and divider current I_div = 10 · I_B. Calculate: (a) Collector resistor R_C, (b) Emitter resistor R_E, (c) Bias resistors R_1 and R_2, (d) Exact Q-point (V_CEQ, I_CQ).",
                      [
                          "1. Collector Resistor Calculation: Voltage drop across R_C: V_RC = V_CC - V_CQ = 12.0 V - 6.0 V = 6.0 V.",
                          "   R_C = V_RC / I_CQ = 6.0 V / 2.0 mA = 3,000 Ohm (3.0 kOhm).",
                          "2. Emitter Resistor Calculation: With V_E = 1.20 V and I_E ≈ I_CQ = 2.0 mA: R_E = V_E / I_E = 1.20 V / 2.0 mA = 600 Ohm (use standard 620 Ohm).",
                          "3. Base Voltage & Base Current: V_B = V_E + V_BE = 1.20 V + 0.70 V = 1.90 V. Base current I_B = I_CQ / beta = 2.0 mA / 150 = 13.33 microA.",
                          "4. Sizing Voltage Divider Resistors: Divider current I_div = 10 · I_B = 10 · 13.33 microA = 133.3 microA.",
                          "   R_2 = V_B / I_div = 1.90 V / 133.3 microA = 14,250 Ohm (use standard 15 kOhm).",
                          "   R_1 = (V_CC - V_B) / (I_div + I_B) = (12.0 V - 1.90 V) / 146.6 microA = 10.1 V / 146.6 microA = 68,890 Ohm (use standard 68 kOhm).",
                          "5. Resulting Q-Point: V_CEQ = V_CQ - V_E = 6.0 V - 1.2 V = 4.80 V; I_CQ = 2.0 mA. (Robustly centered on load line!)."
                      ], current_slide=12, total_slides=total)

    # 13. BJT as a Saturated Low-Side Switch
    add_bullet_slide(prs, "BJT as a Saturated Low-Side Switch for Actuators", [
        "Digital Switching Function: Operates between full OFF (Cutoff: I_B = 0, load de-energized) and full ON (Saturation: V_CE ≈ 0.2V, load energized).",
        "Low-Side Switching Architecture: Emitter connected to GND; load connected between V_CC and Collector; Base driven via series resistor R_B.",
        "Load Current in Saturation: I_C(sat) ≈ (V_CC - V_CE(sat)) / R_load ≈ V_CC / R_load.",
        "Overdrive Factor (ODF): To guarantee deep saturation against beta degradation and temperature, design base current with ODF = 2 to 5: I_B(sat) = ODF · [ I_C(sat) / beta_min ].",
        "Base Resistor Sizing Equation: R_B = (V_IN(logic) - V_BE(sat)) / I_B(sat).",
        "Transistor Conduction Loss: In saturation, power dissipated is minimal: P_sat = I_C(sat) · V_CE(sat) + I_B(sat) · V_BE(sat)."
    ], image_file="fig5_4_bjt_relay_driver.png", current_slide=13, total_slides=total)

    # 14. Inductive Actuator Driving & Flyback Clamping
    add_bullet_slide(prs, "Driving Inductive Farm Actuators (Relays & Solenoids)", [
        "Inductive Stored Energy: Relay coils and hydraulic valves store magnetic energy W = 0.5 · L · I².",
        "Turn-Off Inductive Spike: When base drive goes LOW, transistor cuts off instantaneously; coil forces v_L = -L(di/dt) -> hundreds of volts.",
        "Collector Punch-Through: Spike exceeds V_CEO rating of transistor; causes avalanche dielectric puncture and permanent short circuit.",
        "Flyback Diode Integration: Connect fast diode (1N4007 or UF4007) in parallel with coil, cathode to V_CC, anode to Collector.",
        "Safe Dissipation Loop: When BJT opens, inductive current circulates through forward-biased flyback diode, decaying harmlessly through coil internal resistance."
    ], current_slide=14, total_slides=total)

    # 15. Worked Example 2: BJT Relay Driver Design
    add_example_slide(prs, 2, "Automated Drip Irrigation Solenoid Driver Design",
                      "Design a low-side BJT saturated switch to drive a 12.0 V, 300 mA drip irrigation solenoid valve at Kilombero Sugar nursery. The circuit is controlled directly from an ESP32 microcontroller 3.3V digital GPIO pin (V_OH = 3.3 V, maximum pin current 12 mA). The transistor is a BD139 NPN power transistor with minimum beta_min = 40, V_BE(sat) = 0.85 V, and V_CE(sat) = 0.25 V. Use an overdrive factor ODF = 3. Determine: (a) Saturated collector current I_C(sat), (b) Required base current I_B(sat), (c) Base resistor R_B, (d) Transistor power dissipation in ON state, (e) Verify ESP32 pin current limit.",
                      [
                          "1. Saturated Collector Current: I_C(sat) = (V_CC - V_CE(sat)) / R_solenoid = (12.0 V - 0.25 V) / (12.0 V / 0.30 A) = 11.75 V / 40.0 Ohm = 0.2938 A = 293.8 mA.",
                          "2. Calculate Required Base Current with ODF = 3: I_B(sat) = ODF · [ I_C(sat) / beta_min ] = 3 · [ 293.8 mA / 40 ] = 3 · 7.345 mA = 22.04 mA.",
                          "   Check ESP32 Limit: 22 mA exceeds 12 mA pin limit! Adjust ODF to 1.5: I_B(sat) = 1.5 · 7.345 mA = 11.0 mA (safe for ESP32 pin!).",
                          "3. Base Resistor Calculation: R_B = (V_OH - V_BE(sat)) / I_B(sat) = (3.30 V - 0.85 V) / 11.0 mA = 2.45 V / 0.011 A = 222.7 Ohm (select standard 220 Ohm, 5%).",
                          "4. Transistor Power Dissipation in Saturated ON State:",
                          "   P_sat = I_C(sat) · V_CE(sat) + I_B(sat) · V_BE(sat) = (0.294 A · 0.25 V) + (0.011 A · 0.85 V) = 0.0735 W + 0.0094 W = 0.0829 W = 82.9 mW.",
                          "5. Thermal Assessment: BD139 (TO-126 package rated at 1.25W free air) dissipates only 83 mW; operates completely cool without external heatsink."
                      ], current_slide=15, total_slides=total)

    # 16. Small-Signal AC Models (re and Hybrid-pi)
    add_bullet_slide(prs, "Small-Signal BJT Models: re & Hybrid-pi Parameters", [
        "Small-Signal Operation: When input AC signal amplitude is small (< 10 mV), non-linear exponential BJT curves are approximated linearly.",
        "AC Emitter Resistance (r_e): The dynamic resistance of the forward-biased base-emitter junction: r_e = V_T / I_EQ ≈ 26 mV / I_EQ.",
        "Hybrid-pi Input Resistance (r_pi): Dynamic input resistance looking into base: r_pi = (beta + 1) · r_e ≈ beta · r_e.",
        "Transconductance (g_m): Voltage-to-current gain factor: g_m = Delta I_C / Delta V_BE = I_CQ / V_T ≈ 38.5 · I_CQ (mA/V or mS).",
        "Small-Signal Collector Current: i_c = g_m · v_be = beta · i_b; Transistor acts as an ideal voltage-controlled current source."
    ], current_slide=16, total_slides=total)

    # 17. Single-Stage Common-Emitter Amplifier
    add_bullet_slide(prs, "Single-Stage Common-Emitter AC Amplifier", [
        "Circuit Components: Coupling capacitors C_in and C_out block DC bias voltages while passing AC sensor signals freely.",
        "Emitter Bypass Capacitor (C_E): Placed in parallel with R_E; shorts AC signals to ground, boosting AC voltage gain.",
        "AC Small-Signal Equivalent Circuit: DC supplies replaced with AC ground; coupling and bypass capacitors replaced with AC short circuits.",
        "Voltage Gain with C_E: A_v = v_out / v_in = - (R_C || R_load) / r_e; Negative sign indicates 180° phase inversion.",
        "Voltage Gain without C_E (Unbypassed): A_v = - (R_C || R_load) / (r_e + R_E); Gain is reduced but linearized and stabilized against temperature.",
        "Input Impedance: Z_in = R_1 || R_2 || [ beta · (r_e + R_E) ]; Output Impedance: Z_out ≈ R_C."
    ], current_slide=17, total_slides=total)

    # 18. Worked Example 3: CE Amplifier Analysis
    add_example_slide(prs, 3, "CE Amplifier Gain for Grain Silo Acoustic Sensor",
                      "A single-stage Common-Emitter preamplifier boosts acoustic emission signals from a grain silo weevil sensor in Morogoro. Circuit parameters: V_CC = 15.0 V, R_1 = 47 kOhm, R_2 = 10 kOhm, R_C = 4.7 kOhm, R_E = 1.0 kOhm, load resistor R_load = 10 kOhm, beta = 200, and fully bypassed emitter (C_E = 100 microF). Quiescent current is established at I_CQ = 1.80 mA. Calculate: (a) Dynamic emitter resistance r_e, (b) AC load resistance r_L, (c) Small-signal voltage gain A_v, (d) Amplifier input impedance Z_in.",
                      [
                          "1. Dynamic Emitter Resistance: r_e = 26 mV / I_EQ ≈ 26 mV / 1.80 mA = 14.44 Ohm.",
                          "2. Effective AC Collector Load: Collector sees R_C in parallel with R_load: r_L = R_C || R_load = (4.7 kOhm · 10 kOhm) / (4.7 + 10) = 47 / 14.7 = 3.197 kOhm = 3,197 Ohm.",
                          "3. Small-Signal Voltage Gain with Bypass Capacitor: A_v = - r_L / r_e = - 3,197 Ohm / 14.44 Ohm = - 221.4 (Inverting gain of 221.4x, or 46.9 dB).",
                          "4. Base Input Impedance: Dynamic base impedance Z_base = beta · r_e = 200 · 14.44 Ohm = 2,888 Ohm (2.89 kOhm).",
                          "5. Total Stage Input Impedance: Z_in = R_1 || R_2 || Z_base. Calculate parallel combination: R_1 || R_2 = (47 · 10) / 57 = 8.246 kOhm.",
                          "   Z_in = (8.246 kOhm · 2.888 kOhm) / (8.246 + 2.888) = 23.81 / 11.13 = 2.139 kOhm (2.14 kOhm)."
                      ], current_slide=18, total_slides=total)

    # 19. Practical Agro-Environment Protection
    add_bullet_slide(prs, "BJT Hardening for Agricultural Environments", [
        "Thermal Sinking of Power BJTs: Packages like TO-220 (TIP122) and TO-247 must be torqued to aluminum heatsinks with mica isolators.",
        "Automotive Alternator Load Dump: Transistors on 12V tractor chassis must withstand 60V load dump transients during battery disconnection.",
        "Static Base Protection: High input impedance base circuits are susceptible to static charge; place 100 kOhm pulldown to ground.",
        "Conformal Coating: Salt mist and fertilizer ammonia cause dendritic copper growth between closely spaced TO-92 leads; silicone coat PCB.",
        "Base Overdrive Current Safety: Never connect a BJT base directly to a voltage supply without a series current-limiting resistor (destroys BE junction!)."
    ], current_slide=19, total_slides=total)

    # 20. Case Study 1
    add_case_study_slide(prs, 1, "BJT Driver Thermal Runaway in Brooder Heaters",
                         "Poultry Brooder Facility, SUA Main Campus, Morogoro, Tanzania",
                         "An automated poultry chick brooder heating system used 2N3055 power BJTs to switch 12V electric heating mats. In the humid, 35°C brooder environment, the simple fixed base-resistor drive circuit suffered recurrent transistor burnouts every 2 weeks, leaving vulnerable day-old chicks without warmth and resulting in high chick mortality.",
                         "SUA agricultural engineers diagnosed thermal runaway: As ambient temperature rose, BJT leakage I_CEO surged, increasing collector current and internal die temperature in a positive feedback loop until junction melting occurred. Engineers retrofitted the circuit with a negative feedback emitter degeneration resistor and a 1N4148 thermal compensation diode mounted directly on the heatsink.",
                         [
                             "Thermal runaway eliminated completely; zero transistor failures over 18 months.",
                             "Brooder ambient temperature regulated to within ±0.4°C of target 34.0°C setpoint.",
                             "Day-old chick survival rate increased from 82% to 98.5%."
                         ], current_slide=20, total_slides=total)

    # 21. Case Study 2
    add_case_study_slide(prs, 2, "Tractor Hydraulic Solenoid Valve Driver Upgrade",
                         "Kilombero Sugar Estate Sugarcane Mechanization Depot, Tanzania",
                         "Sugarcane haulage tractors retrofitted with automated GPS row-following steering used discrete BJT low-side switches to actuate electro-hydraulic steering spool valves. Drivers frequently burnt out during hot midday operations because base drive resistors were undersized, keeping transistors in the active region rather than deep saturation.",
                         "Engineers discovered that the BD139 transistors were operating with V_CE = 1.4V instead of V_CE(sat) = 0.2V, causing them to dissipate P = 1.4V · 1.5A = 2.1W continuously in free air. By redesigning the base drive circuit with an overdrive factor ODF = 3 and adding a complementary buffer stage, V_CE collapsed to 0.18V, dropping dissipation to 0.27W.",
                         [
                             "Transistor operating temperature plummeted from 135°C to a cool 48°C.",
                             "Steering hydraulic response time improved from 280 ms to 45 ms.",
                             "Enabled continuous 24-hour sugarcane harvesting operations without electrical shutdowns."
                         ], current_slide=21, total_slides=total)

    # 22. Laboratory Bench Protocol
    add_lab_slide(prs, "BJT Static Characteristics & Saturated Switch Verification", [
        "Measure BJT common-emitter output characteristics and plot family of curves on DSO/curve tracer.",
        "Determine current gain beta (h_FE) and observe beta variation with collector current.",
        "Assemble a saturated low-side BJT relay driver circuit and measure V_CE(sat) and V_BE(sat).",
        "Wire a single-stage Common-Emitter amplifier and measure voltage gain with and without bypass capacitor."
    ], [
        "Step 1: Mount 2N3904 NPN transistor on breadboard. Wire 100 kOhm potentiometer in base circuit and 1 kOhm resistor in collector.",
        "Step 2: Set I_B to 10 microA, 20 microA, 30 microA; sweep V_CC from 0 to 12V; record I_C and V_CE; plot CE characteristics.",
        "Step 3: Measure V_CE(sat) while driving 12V relay coil with I_B = 1.0 mA; confirm V_CE(sat) <= 0.2V.",
        "Step 4: Wire voltage divider CE amplifier (R_1=47k, R_2=10k, R_C=3.3k, R_E=680, C_E=47uF). Inject 1 kHz, 10 mV sine wave.",
        "Step 5: Measure output amplitude on DSO; verify 180° phase inversion and compute voltage gain A_v; remove C_E and observe gain reduction."
    ], current_slide=22, total_slides=total)

    # 23. Troubleshooting & Pitfalls
    add_bullet_slide(prs, "Diagnostic Troubleshooting of BJT Circuits", [
        "Floating Base Terminal: Leaving base unconnected allows electrostatic noise to turn transistor partially ON; always use pulldown resistor.",
        "Active Region Overheating: Inadequate base current keeps switching transistor in active region (high V_CE · I_C); transistor scorches PCB.",
        "Reversed Collector and Emitter: Transistor will still amplify slightly (inverse beta ≈ 2-5), but voltage rating collapses and gain is terrible.",
        "Open-Circuit Base-Emitter Junction: DMM diode check reads 'OL' from Base to Emitter; caused by excessive reverse base-emitter voltage (> 6V).",
        "Collector-Emitter Short Circuit: DMM reads 0 Ohm between Collector and Emitter in both directions; caused by overvoltage or thermal melting."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "State the two fundamental biasing rules for a BJT operating in the active linear region.",
        "Derive the relationship between common-base current gain alpha and common-emitter current gain beta.",
        "Explain the mechanism of thermal runaway in a BJT. How does an emitter degeneration resistor provide negative feedback stabilization?",
        "Why is an overdrive factor (ODF) necessary when designing a BJT saturated switch to drive an inductive farm solenoid valve?",
        "Explain the function of coupling capacitors C_in, C_out and emitter bypass capacitor C_E in a single-stage CE amplifier."
    ], "Lecture 6 will explore Field Effect Transistors (FETs): JFETs, MOSFETs, gate charge dynamics, and power MOSFETs in solar pump drivers.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "The BJT is a current-controlled bipolar device: A small base current I_B controls a large collector current I_C = beta · I_B.",
        "Operating regions: Cutoff (switch OFF), Saturation (switch ON, V_CE ≈ 0.2V), and Active (linear amplifier).",
        "Voltage divider bias provides stable, beta-independent quiescent Q-point operation against temperature swings.",
        "Saturated switches require base overdrive (ODF >= 2) to ensure minimum saturation voltage and low conduction losses.",
        "Inductive loads require mandatory flyback diode clamping across relay coils to prevent transistor collector punch-through."
    ], [
        "Current Conservation: I_E = I_B + I_C",
        "Current Gains: alpha = I_C / I_E; beta = I_C / I_B = alpha / (1 - alpha)",
        "DC Load Line: I_C = (V_CC / R_C) - (V_CE / R_C)",
        "Saturated Switch Base Current: I_B(sat) = ODF · [ I_C(sat) / beta_min ]",
        "Dynamic Emitter Resistance: r_e ≈ 26 mV / I_EQ",
        "CE Voltage Gain: A_v = - (R_C || R_load) / r_e (bypassed)",
        "Input Impedance: Z_in = R_1 || R_2 || (beta · r_e)"
    ], current_slide=25, total_slides=total)

    # 26. References & Reading List
    add_bullet_slide(prs, "Prescribed References & Practical Laboratory Preparation", [
        "Boylestad, R. L., & Nashelsky, L. (2018). Electronic Devices and Circuit Theory (11th ed.). Pearson Education.",
        "Sedra, A. S., & Smith, K. C. (2020). Microelectronic Circuits (8th ed.). Oxford University Press.",
        "Floyd, T. L. (2017). Electronic Devices: Conventional Current Version (10th ed.). Pearson.",
        "Laboratory Preparation: Review BJT pinout configurations (TO-92 EBC vs CBE) before attending Lab Session 5.",
        "Field Assignment: Complete Assignment 2, Questions 5 to 8 on BJT biasing and saturated switching."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

def build_lecture_6_deck(prs):
    lec_num = 6
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Field Effect Transistor (FET)",
                    "JFETs, MOSFETs, Gate Charge Dynamics, Power MOSFETs & Solar Irrigation Pump Inverters", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 6 Learning Outcomes & Practical Scope", [
        "Contrast Unipolar vs Bipolar Physics: Voltage-controlled FET operation vs current-controlled BJT mechanics.",
        "Analyze JFET Principles: Understand pinch-off voltage V_P, saturation current I_DSS, and Shockley's equation.",
        "Evaluate Transconductance g_m: Derive g_m = dI_D / dV_GS and determine operating point transconductance.",
        "Analyze JFET Biasing Networks: Design Self-Bias and Voltage Divider Bias configurations.",
        "Differentiate MOSFET Topologies: Depletion-Enhancement (DE-MOSFET) vs Enhancement-Only (E-MOSFET) devices.",
        "Master Power MOSFET Dynamics: Gate charge Q_G, threshold voltage V_GS(th), ON-resistance R_DS(on), and heat sinking.",
        "Deploy Power MOSFETs in AgriTech: Design solar brushless DC pump inverters and implement ESD protection protocols."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "Field Effect Transistors in Modern Agro-Mechatronics", [
        "The Powerhouse of Solar Irrigation: High-efficiency solar water pumping systems rely exclusively on Power MOSFETs.",
        "Negligible Gate Drive Power: Ultra-high input impedance (> 10^12 Ohm) allows microcontrollers to control kilowatts of motor power.",
        "High-Speed PWM Actuation: Power MOSFETs switch at 20 kHz to 100 kHz with minimal switching losses in variable-rate sprayers.",
        "Superior Thermal Stability: MOSFETs have a positive temperature coefficient of ON-resistance (R_DS(on)), preventing thermal runaway.",
        "Harsh Agro-Climatic Vulnerability: Insulated silicon dioxide (SiO2) gate dielectric is microscopically thin; easily punctured by static electricity."
    ], image_file="img_mosfet_power.jpg", current_slide=3, total_slides=total)

    # 4. FET vs BJT Fundamental Comparison
    add_bullet_slide(prs, "Fundamental Comparison: FET versus BJT", [
        "Control Mechanism: BJT is current-controlled (I_C controlled by I_B); FET is voltage-controlled (I_D controlled by gate voltage V_GS).",
        "Carrier Type: BJT is bipolar (conduction involves both electrons and holes); FET is unipolar (conduction involves only majority carriers).",
        "Input Impedance: BJT input impedance is moderate (1 kOhm to 10 kOhm); FET input impedance is astronomical (10^9 to 10^14 Ohm).",
        "Thermal Coefficient: BJT has negative tempco (prone to thermal runaway); Power MOSFET has positive tempco (inherently self-stabilizing).",
        "Switching Speed: FETs have zero minority carrier storage time; switch orders of magnitude faster than power BJTs.",
        "Noise Performance: FETs exhibit substantially lower thermal and flicker noise; ideal for high-impedance agricultural sensor preamps."
    ], current_slide=4, total_slides=total)

    # 5. JFET Physical Structure & Operation
    add_bullet_slide(prs, "Junction Field Effect Transistor (JFET) Physics", [
        "N-Channel JFET Construction: Bar of N-type silicon with Drain (D) and Source (S) ohmic contacts at opposite ends.",
        "Gate Electrodes: Two heavily doped P⁺ regions embedded on opposite sides of the channel, connected together as the Gate (G).",
        "Normally-ON Depletion Device: With V_GS = 0 V and small V_DS, majority electrons flow freely from source to drain through the open channel.",
        "Reverse-Biased Gate Junction: Applying negative gate voltage (V_GS < 0) widens the P⁺N depletion regions into the channel, constricting channel width.",
        "Voltage-Controlled Resistor (Ohmic Region): At low V_DS, the channel behaves as a linear resistor whose resistance is modulated by V_GS."
    ], image_file="fig6_2_jfet_characteristics.png", current_slide=5, total_slides=total)

    # 6. Pinch-off Voltage & Shockley's Equation
    add_bullet_slide(prs, "Pinch-off Voltage V_P & Shockley's Transfer Equation", [
        "Pinch-Off Phenomenon: As drain voltage V_DS increases, the drain-end depletion layers expand until they touch (pinch off) at V_DS = |V_P|.",
        "Saturation (Active) Region: Beyond pinch-off (V_DS >= V_GS - V_P), current saturates to a constant level governed strictly by gate voltage V_GS.",
        "Pinch-Off Voltage (V_P): Gate-to-source cutoff voltage that pinches channel completely shut at V_DS = 0 (typically -2V to -8V for N-channel).",
        "Drain Saturation Current (I_DSS): Maximum drain current flowing when V_GS = 0 V and V_DS >= |V_P|.",
        "Shockley's Transfer Equation: In saturation region: I_D = I_DSS · [ 1 - (V_GS / V_P) ]².",
        "Square-Law Characteristic: Drain current varies quadratically with gate voltage; provides pure second-harmonic transfer without higher distortions."
    ], current_slide=6, total_slides=total)

    # 7. JFET Transconductance gm
    add_bullet_slide(prs, "JFET Small-Signal Transconductance g_m", [
        "Definition of Transconductance: The rate of change of drain current with respect to gate-source voltage: g_m = dI_D / dV_GS |_(Q-point).",
        "Mathematical Derivation: Differentiating Shockley's equation: dI_D / dV_GS = 2 · I_DSS · [ 1 - (V_GS / V_P) ] · (-1 / V_P).",
        "Operating Transconductance Formula: g_m = g_m0 · [ 1 - (V_GS / V_P) ], where maximum transconductance g_m0 = (2 · I_DSS) / |V_P|.",
        "Transconductance in Terms of Drain Current: g_m = g_m0 · sqrt( I_D / I_DSS ); Transconductance is proportional to square root of drain current.",
        "Units: Measured in Siemens (S), milliSiemens (mS), or micro-mhos (typically 1.0 mS to 10.0 mS for small-signal JFETs)."
    ], current_slide=7, total_slides=total)

    # 8. JFET Biasing: Self-Bias Architecture
    add_bullet_slide(prs, "JFET Self-Bias Circuit Architecture", [
        "Single-Supply Biasing: JFET requires negative V_GS, but Self-Bias generates this negative potential using a single positive supply V_DD.",
        "Source Resistor Mechanism: Source current I_D flows through resistor R_S, establishing a positive source voltage: V_S = I_D · R_S.",
        "Gate Resistor Grounding: Large gate resistor R_G (1 MOhm to 10 MOhm) ties gate to ground: Since gate current I_G ≈ 0, V_G = 0 V.",
        "Resulting Negative Bias: V_GS = V_G - V_S = 0 - I_D · R_S = - I_D · R_S.",
        "Self-Regulating Action: If I_D attempts to rise -> V_S rises -> V_GS becomes more negative -> constricts channel -> forces I_D back down!",
        "Source Resistor Sizing: R_S = |V_GSQ| / I_DQ; Sized from desired Q-point coordinates."
    ], current_slide=8, total_slides=total)

    # 9. Worked Example 1: JFET Self-Bias Design
    add_example_slide(prs, 1, "JFET Self-Bias Q-Point for Soil pH Probe Pre-Amp",
                      "A 2N5458 N-channel JFET buffers a high-impedance soil pH glass electrode sensor in a Morogoro agricultural chemistry lab. Manufacturer datasheet specifications: I_DSS = 8.0 mA and V_P = -4.0 V. The circuit uses self-bias with V_DD = 18.0 V, drain resistor R_D = 2.2 kOhm, and source resistor R_S = 560 Ohm. Gate resistor R_G = 2.2 MOhm. Determine: (a) Quiescent drain current I_DQ, (b) Quiescent gate-source voltage V_GSQ, (c) Quiescent drain-source voltage V_DSQ, (d) Transconductance g_m at Q-point.",
                      [
                          "1. Formulate System of Equations: Equation 1 (Shockley): I_D = I_DSS · [ 1 - (V_GS / V_P) ]²; Equation 2 (Bias Line): V_GS = - I_D · R_S.",
                          "2. Substitute V_GS into Shockley: I_D = 8.0 mA · [ 1 - (- I_D · 560 / -4.0) ]² = 0.008 · [ 1 - 140 · I_D ]².",
                          "3. Expand Quadratic: I_D = 0.008 · [ 1 - 280 · I_D + 19,600 · I_D² ] = 0.008 - 2.24 · I_D + 156.8 · I_D².",
                          "   Standard Quadratic: 156.8 · I_D² - 3.24 · I_D + 0.008 = 0.",
                          "   Using quadratic formula: I_DQ = [ 3.24 - sqrt(3.24² - 4 · 156.8 · 0.008) ] / (2 · 156.8) = [ 3.24 - 2.341 ] / 313.6 = 0.002867 A = 2.87 mA.",
                          "4. Calculate Voltages: V_GSQ = - I_DQ · R_S = - (2.87 mA · 560 Ohm) = - 1.607 V.",
                          "   V_DSQ = V_DD - I_DQ · (R_D + R_S) = 18.0 V - 2.87 mA · (2,200 + 560) = 18.0 V - 7.92 V = 10.08 V.",
                          "5. Calculate Operating Transconductance: g_m0 = (2 · I_DSS) / |V_P| = (2 · 8.0 mA) / 4.0 V = 4.0 mS.",
                          "   g_m = g_m0 · [ 1 - (V_GSQ / V_P) ] = 4.0 mS · [ 1 - (-1.607 / -4.0) ] = 4.0 · (1 - 0.4018) = 2.39 mS."
                      ], current_slide=9, total_slides=total)

    # 10. MOSFET Architecture: IGFET Physics
    add_bullet_slide(prs, "MOSFET Architecture: Insulated Gate Field Effect Physics", [
        "Insulated Gate Structure: Metal gate electrode is electrically isolated from the semiconductor channel by an ultra-thin Silicon Dioxide (SiO2) layer.",
        "Zero Gate Current: Gate oxide dielectric resistance exceeds 10^14 Ohm; DC gate leakage current is measured in pico-Amperes (pA).",
        "Depletion-Enhancement MOSFET (DE-MOSFET): Built with a physical silicon channel; can operate in either depletion mode (V_GS < 0) or enhancement mode (V_GS > 0).",
        "Enhancement-Only MOSFET (E-MOSFET): No physical channel exists at zero bias; completely normally-OFF (I_D = 0 at V_GS = 0).",
        "Channel Inversion: Applying positive V_GS repels holes and attracts minority electrons to the surface, creating an inverted N-type conductive layer.",
        "Threshold Voltage (V_GS(th)): Minimum positive gate voltage required to form the conductive inversion channel (typically 1.5V to 4.0V)."
    ], current_slide=10, total_slides=total)

    # 11. Enhancement MOSFET Equations
    add_bullet_slide(prs, "Enhancement MOSFET Governing Equations", [
        "Cutoff Region (V_GS < V_GS(th)): Inversion channel is not formed; drain current I_D = 0; switch is fully OPEN.",
        "Ohmic (Triode / Linear) Region (V_GS > V_GS(th) and V_DS < V_GS - V_GS(th)): Channel conducts as a continuous resistor.",
        "Ohmic Current Equation: I_D = k · [ 2 · (V_GS - V_GS(th)) · V_DS - V_DS² ], where k is device transconductance parameter (A/V²).",
        "Saturation (Active) Region (V_DS >= V_GS - V_GS(th)): Drain-end channel pinches off; current saturates into constant current source.",
        "Saturation Current Equation: I_D = k · [ V_GS - V_GS(th) ]².",
        "Device Constant k: k = 0.5 · mu_n · C_ox · (W / L), where C_ox is gate capacitance per unit area, and W/L is channel width-to-length ratio."
    ], current_slide=11, total_slides=total)

    # 12. Power MOSFETs: Trench HEXFET Architecture
    add_bullet_slide(prs, "Power MOSFETs: Vertical Trench Architecture", [
        "Planar vs Vertical Conduction: Small-signal FETs conduct horizontally across the chip surface; Power MOSFETs conduct vertically from top to bottom.",
        "Vertical DMOS / Trench HEXFET: Current flows vertically from source on the top surface down through epitaxial drift layer to drain on the bottom tab.",
        "Massive Paralleled Cells: Millions of microscopic hexagonal cells integrated in parallel on a single silicon die to achieve massive current ratings (50A to 200A+).",
        "Ultra-Low ON-Resistance (R_DS(on)): State-of-the-art power MOSFETs achieve R_DS(on) under 5 milli-Ohms (mOhm), minimizing conduction I²R losses.",
        "Integral Body Diode: Inherent parasitic PN junction between P-body and N-drift layer forms an internal reverse flyback diode across Drain and Source."
    ], current_slide=12, total_slides=total)

    # 13. Gate Charge Dynamics & Gate Drivers
    add_bullet_slide(prs, "Gate Charge Dynamics & Driver Circuit Requirements", [
        "The Gate Capacitance Myth: MOSFET gates do not draw DC current, but they exhibit significant parasitic capacitance: C_iss = C_gs + C_gd.",
        "Miller Capacitance (C_gd): Gate-to-drain capacitance undergoes Miller multiplication during switching transitions, forming the **Miller Plateau**.",
        "Total Gate Charge (Q_G): Total electrical charge (nanocoulombs, nC) that must be transferred to charge gate to desired V_GS.",
        "Switching Inrush Current: To switch in t_sw = 50 nanoseconds, peak gate current required: I_gate(peak) = Q_G / t_sw (can exceed 2 to 5 Amperes!).",
        "Dedicated Gate Driver ICs: Microcontroller GPIO pins cannot supply 2A transients; dedicated gate driver ICs (TC4427, IR2110) are mandatory."
    ], current_slide=13, total_slides=total)

    # 14. Logic-Level vs Standard Power MOSFETs
    add_bullet_slide(prs, "Logic-Level vs Standard Power MOSFET Selection", [
        "Standard Power MOSFETs (e.g. IRF540N): Require full V_GS = 10.0 V to reach minimum rated ON-resistance R_DS(on) (44 mOhm).",
        "The 3.3V / 5V Gate Pitfall: Driving a standard IRF540 directly from a 3.3V or 5V microcontroller pin leaves it in the high-resistance linear region!",
        "Thermal Destruction: At V_GS = 3.3V, R_DS surges to > 2 Ohm; a 10A solar pump motor causes P = I²R = 200W dissipation, incinerating the transistor.",
        "Logic-Level Power MOSFETs (e.g. IRLZ44N, IRL540): Engineered with ultra-thin gate oxides; guarantee minimum R_DS(on) at V_GS = 4.5V or 3.3V.",
        "Rule of Thumb: For direct microcontroller GPIO driving, ALWAYS specify logic-level 'IRL' prefix rather than standard 'IRF' prefix devices."
    ], current_slide=14, total_slides=total)

    # 15. Worked Example 2: Power MOSFET Solar Pump Driver
    add_example_slide(prs, 2, "Power MOSFET Switch Sizing for Solar Water Pump",
                      "Design a low-side solid-state power switch for a 24.0 V, 120 W DC brushless solar irrigation pump at Bahi, Dodoma. Continuous motor current is I_load = 5.0 A. Ambient temperature reaches T_amb = 45°C. Compare: (a) Standard IRF540N driven at V_GS = 4.5 V (where R_DS(on) = 0.18 Ohm), versus (b) Logic-level IRLZ44N driven at V_GS = 4.5 V (where R_DS(on) = 0.028 Ohm). The TO-220 package has junction-to-ambient thermal resistance theta_JA = 62°C/W (free air without heatsink). Calculate power dissipations and junction temperatures.",
                      [
                          "1. Standard IRF540N Analysis at V_GS = 4.5 V:",
                          "   Conduction Power Dissipation: P_IRF = I_load² · R_DS(on) = (5.0 A)² · 0.18 Ohm = 25 · 0.18 = 4.50 W.",
                          "   Junction Temperature Rise: Delta T_IRF = P_IRF · theta_JA = 4.50 W · 62°C/W = 279°C.",
                          "   Total Junction Temperature: T_J(IRF) = 45°C + 279°C = 324°C (catastrophic silicon die burnout! Max rating is 175°C).",
                          "2. Logic-Level IRLZ44N Analysis at V_GS = 4.5 V:",
                          "   Conduction Power Dissipation: P_IRL = I_load² · R_DS(on) = (5.0 A)² · 0.028 Ohm = 25 · 0.028 = 0.70 W.",
                          "   Junction Temperature Rise: Delta T_IRL = P_IRL · theta_JA = 0.70 W · 62°C/W = 43.4°C.",
                          "   Total Junction Temperature: T_J(IRL) = 45°C + 43.4°C = 88.4°C (completely safe, operates comfortably under free convection!).",
                          "3. Engineering Impact: Selecting the correct logic-level MOSFET eliminated heatsink cost and guaranteed reliable operation."
                      ], current_slide=15, total_slides=total)

    # 16. Power MOSFET Motor Driver Architecture
    add_bullet_slide(prs, "Power MOSFET H-Bridge & BLDC Motor Inverters", [
        "H-Bridge Architecture: Four MOSFETs arranged in an H-network allow bidirectional forward, reverse, and regenerative braking of DC motors.",
        "High-Side vs Low-Side Switches: Low-side N-channel MOSFETs have grounded sources; high-side MOSFETs have sources floating at motor voltage.",
        "High-Side Gate Bootstrapping: High-side N-channel MOSFET requires gate voltage V_gate = V_bus + 10V; achieved via bootstrap capacitor and diode.",
        "Three-Phase BLDC Inverter: Six power MOSFETs configured into three half-bridge legs drive 3-phase permanent magnet solar submersible pumps.",
        "Pulse Width Modulation (PWM): Microcontroller switches MOSFETs at 20 kHz, modulating duty cycle to achieve variable-speed water pumping."
    ], image_file="fig6_4_power_mosfet_motor_driver.png", current_slide=16, total_slides=total)

    # 17. Electrostatic Discharge (ESD) Hazards & Handling
    add_bullet_slide(prs, "Electrostatic Discharge (ESD) Protection Protocols", [
        "The Dielectric Puncture Threat: SiO2 gate dielectric is only 5 to 50 nanometers thick; punctures permanently at V_GS > 20 V to 30 V.",
        "Human Body Model (HBM): A technician walking across a nylon carpet or dry African grain floor accumulates static potentials exceeding 15,000 V!",
        "Invisible Latent Damage: Minor ESD zap creates microscopic gate oxide pinholes; device passes bench test but fails prematurely in the field.",
        "Internal Protection Diodes: Many modern small-signal MOSFETs incorporate back-to-back Zener diodes across Gate and Source to clamp ESD.",
        "Field Handling Protocol: Wear grounded antistatic wrist straps; store MOSFETs in conductive black ESD foam; solder with grounded-tip irons."
    ], current_slide=17, total_slides=total)

    # 18. Paralleling Power MOSFETs & Positive Tempco
    add_bullet_slide(prs, "Paralleling Power MOSFETs: The Positive Tempco Advantage", [
        "The BJT Current Hogging Dilemma: BJTs have negative tempco (hotter transistor draws more current), causing thermal runaway when paralleled.",
        "MOSFET Self-Balancing Mechanism: Silicon mobility decreases with temperature, causing R_DS(on) to increase as temperature rises (+0.6%/°C).",
        "Current Sharing Dynamics: If MOSFET A runs hotter than MOSFET B -> R_DS(on) of A increases -> current automatically diverts into B!",
        "Direct Paralleling: Multiple power MOSFETs can be connected in parallel without external emitter ballasting resistors to handle hundreds of Amps.",
        "Individual Gate Resistors: Always provide a dedicated 10 Ohm to 47 Ohm series gate damping resistor for each parallel MOSFET to prevent parasitic HF ringing."
    ], current_slide=18, total_slides=total)

    # 19. Practical Agro-Environment Protection
    add_bullet_slide(prs, "MOSFET Circuit Hardening for Rural Agriculture", [
        "Gate Pulldown Resistors: Always place a 10 kOhm to 100 kOhm resistor directly between Gate and Source to ensure OFF state during MCU boot.",
        "Flyback Snubbers: Pair integral body diodes with external RC snubbers (10 Ohm + 4.7 nF) to suppress high-frequency inductive motor ringing.",
        "Overvoltage Clamping: Solder a bidirectional 18V Zener or TVS diode directly across Gate-Source pins on the PCB.",
        "Thermal Heatsinking: For motor currents exceeding 10A, mount MOSFETs to finned aluminum heatsinks with thermal silicone insulator pads.",
        "Tropical Humidity Ingress: Encapsulate high-voltage gate drive traces in conformal polyurethane coating to prevent ionic surface leakage."
    ], current_slide=19, total_slides=total)

    # 20. Case Study 1
    add_case_study_slide(prs, 1, "Solar Submersible Pump MOSFET Inverter Failure",
                         "Mbarali Paddy Rice Irrigation Scheme, Mbeya Region, Tanzania",
                         "A 7.5 kW solar photovoltaic submersible borehole pumping station suffered complete inverter blowouts every 4 to 6 weeks. Three half-bridge power MOSFET modules (IRFP260N) repeatedly suffered explosive drain-to-source punch-through, cutting off irrigation water to 40 hectares of rice paddies.",
                         "SUA mechatronics engineers conducted DSO trace diagnostics and discovered two fatal design defects: (1) Inverter gate driver used standard 5V logic pulses that under-drove the 10V gates, causing excessive conduction heating, and (2) Long 80-meter submerged motor cables generated massive inductive voltage reflections (> 280V) that exceeded the 200V MOSFET breakdown rating.",
                         [
                             "Retrofitted with 500V, 0.075 Ohm CoolMOS power transistors with 12V high-current gate drivers.",
                             "Installed dv/dt output line choke filters to suppress motor cable voltage reflections.",
                             "Inverter operated 100% reliably throughout two entire 120-day paddy rice seasons."
                         ], current_slide=20, total_slides=total)

    # 21. Case Study 2
    add_case_study_slide(prs, 2, "Precision PWM Variable-Rate Fertilizer Injection",
                         "Kilombero Valley Teak & Sugar Plantations, Morogoro, Tanzania",
                         "Tractor-mounted liquid fertilizer injection systems required high-speed variable-rate solenoid valve pulsing (100 Hz PWM) linked to tractor GPS forward velocity. The original mechanical relay switches failed within 3 days due to contact arcing, causing uneven fertilizer distribution and crop lodging.",
                         "Engineers designed a solid-state PWM driver module using logic-level IRLB8721 power MOSFETs (R_DS(on) = 8.7 mOhm) controlled directly by an STM32 microcontroller. A fast ultra-fast recovery diode (MUR420) was placed across the 12V, 4A fertilizer solenoid valve to handle the 100 Hz inductive freewheeling current.",
                         [
                             "Achieved over 25 million valve switching cycles without a single electrical failure.",
                             "Fertilizer application accuracy improved to within ±1.5% across varying tractor speeds.",
                             "Reduced liquid fertilizer wastage by 18%, saving the estate over 22,000 USD annually."
                         ], current_slide=21, total_slides=total)

    # 22. Laboratory Bench Protocol
    add_lab_slide(prs, "JFET Transfer Curves & Power MOSFET Switching Bench Protocol", [
        "Measure N-channel JFET (2N5458) transfer characteristics and extract I_DSS and pinch-off V_P.",
        "Characterize JFET self-bias circuit and verify operating Q-point against theoretical equations.",
        "Demonstrate gate threshold voltage V_GS(th) and switching action of logic-level power MOSFET.",
        "Drive a DC motor with PWM signal and observe V_DS switching waveforms and body diode clamping on DSO."
    ], [
        "Step 1: Wire 2N5458 JFET on breadboard; connect variable DC supply across Drain-Source (V_DS = 10V).",
        "Step 2: Sweep gate voltage V_GS from 0V to -5V using second DC supply; record I_D; plot curve and extract I_DSS and V_P.",
        "Step 3: Assemble self-bias circuit (R_D = 2.2k, R_S = 470, R_G = 1M); measure V_GSQ and V_DSQ with DMM; verify math.",
        "Step 4: Mount IRLZ44N power MOSFET; connect 12V DC cooling fan as load; apply 0V then 3.3V to gate; record V_DS.",
        "Step 5: Inject 10 kHz PWM signal from function generator into gate; connect DSO across drain; observe switching rise/fall times."
    ], current_slide=22, total_slides=total)

    # 23. Troubleshooting & Pitfalls
    add_bullet_slide(prs, "Diagnostic Troubleshooting of FET Circuits", [
        "Floating Gate Latch-Up: A disconnected MOSFET gate acts as an antenna, floating to random voltages and oscillating; always tie with pulldown.",
        "Insufficient Gate Drive Voltage: Driving standard MOSFETs with 3.3V logic causes extreme conduction heating and thermal failure.",
        "Punctured Gate Dielectric: DMM resistance between Gate and Source reads < 100 kOhm (should be infinite); caused by ESD or inductive spike.",
        "Body Diode Reverse Recovery Ringing: Slow internal body diode in bridge inverters creates shoot-through currents; add external Schottky bypass.",
        "Parasitic Gate Oscillation: High-speed switching induces high-frequency VHF ringing on gate lead; cure by adding 22 Ohm series gate resistor."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "Differentiate between a JFET and a MOSFET in terms of physical structure, input impedance, and gate conduction mechanism.",
        "State Shockley's equation for a JFET in saturation and explain the physical significance of parameters I_DSS and V_P.",
        "Explain why a power MOSFET has a positive temperature coefficient of ON-resistance, and why this allows safe direct paralleling.",
        "Why is it hazardous to drive a standard power MOSFET (e.g. IRF540N) directly from a 3.3V microcontroller GPIO pin?",
        "Explain the Miller effect in power MOSFET switching and describe why the gate voltage plateaus during turn-on."
    ], "Lecture 7 will explore Number Systems & Binary Arithmetic: Radix conversions, signed 2's complement, BCD, and tractor CAN-bus codes.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "FETs are unipolar voltage-controlled devices with astronomical input impedance (> 10^12 Ohm).",
        "JFETs are normally-ON depletion devices; channel conduction is governed by Shockley's square-law equation.",
        "Power MOSFETs (HEXFETs) feature vertical trench structures with ultra-low ON-resistance (R_DS(on) < 10 mOhm).",
        "Logic-level MOSFETs (IRLZ series) are mandatory for direct 3.3V / 5V microcontroller switching.",
        "Thin SiO2 gate dielectrics are highly susceptible to ESD damage; strict static handling and gate TVS clamping are required."
    ], [
        "JFET Shockley Equation: I_D = I_DSS · [ 1 - (V_GS / V_P) ]²",
        "Maximum Transconductance: g_m0 = (2 · I_DSS) / |V_P|",
        "Operating Transconductance: g_m = g_m0 · [ 1 - (V_GS / V_P) ]",
        "JFET Self-Bias: V_GS = - I_D · R_S",
        "E-MOSFET Saturation: I_D = k · [ V_GS - V_GS(th) ]²",
        "MOSFET Conduction Loss: P_cond = I_D(rms)² · R_DS(on)",
        "Peak Gate Current: I_gate(peak) = Q_G / t_sw"
    ], current_slide=25, total_slides=total)

    # 26. References & Reading List
    add_bullet_slide(prs, "Prescribed References & Practical Laboratory Preparation", [
        "Boylestad, R. L., & Nashelsky, L. (2018). Electronic Devices and Circuit Theory (11th ed.). Pearson Education.",
        "Sedra, A. S., & Smith, K. C. (2020). Microelectronic Circuits (8th ed.). Oxford University Press.",
        "Rashid, M. H. (2014). Power Electronics: Devices, Circuits, and Applications (4th ed.). Pearson.",
        "Laboratory Preparation: Review antistatic ESD handling procedures before attending Lab Session 6.",
        "Field Assignment: Complete Assignment 2, Questions 9 to 12 on JFET biasing and power MOSFET inverter design."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

print("slides_part2 module complete with Lectures 4, 5, and 6.")
