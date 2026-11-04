#!/usr/bin/env python3
"""
build_compedia_2.py
Comprehensive Lecture Compendium for:
LECTURE 2: SEMICONDUCTOR PHYSICS
Course: AEN 214 Introduction to Electronics
Department of Agricultural Engineering, Sokoine University of Agriculture (SUA).
Target Length: > 15 Pages.
"""

import os
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, PageBreak, KeepTogether
from compendium_base import (
    get_custom_stylesheet, create_banner_header, create_callout,
    create_example, create_figure, create_custom_table, create_formula_summary_table, render_pdf
)

def build_lecture_2():
    styles = get_custom_stylesheet()
    story = []

    # 1. Header Banner
    topics = [
        "2.1 Atomic Structure, Bohr Model & Quantum Energy Shells (Si & Ge)",
        "2.2 Energy Band Theory of Solids: Valence, Conduction & Forbidden Gap",
        "2.3 Intrinsic Semiconductors, Covalent Bonding & Thermal Generation",
        "2.4 Extrinsic Doping (N-Type & P-Type), Mass Action & Carrier Transport",
        "2.5 The PN Junction Depletion Layer & Mathematical Barrier Derivation",
        "2.6 Forward & Reverse Biasing Physics & Energy Band Diagrams",
        "2.7 The Hall Effect: Lorentz Force & Agricultural Speed Transducers",
        "2.8 Laboratory Bench Protocol: PN Barrier Potential & Temperature Drift",
        "2.9 Tanzanian Agricultural Engineering Applications & Review Problems"
    ]
    story.extend(create_banner_header(2, "Semiconductor Physics", topics))

    # -------------------------------------------------------------
    # SECTION 1: INTRODUCTION & SOLID-STATE FOUNDATIONS
    # -------------------------------------------------------------
    story.append(Paragraph("2.0 Solid-State Physical Foundations in Agricultural Automation", styles['SecH1']))
    story.append(Paragraph(
        "Modern agricultural transformation—from GPS-guided precision tractors and automated drone sprayers to "
        "smart solar-powered irrigation inverters and climate-controlled greenhouses—is powered by solid-state semiconductor devices. "
        "A semiconductor is physically characterized by its intermediate electrical conductivity, lying between that of metallic conductors "
        "(such as copper and aluminum) and electrical insulators (such as glass and quartz). Crucially, unlike metallic conductors whose "
        "electrical resistance increases with rising temperature (positive temperature coefficient of resistance due to enhanced lattice phonon scattering), "
        "pure intrinsic semiconductors exhibit a <b>negative temperature coefficient of resistance (negative TCR)</b>: their electrical conductivity "
        "increases exponentially as thermal energy liberates valence electrons into the conduction band.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "Furthermore, by introducing controlled microscopic impurities (a process termed <b>doping</b> at ratios as minute as one foreign atom per ten million host atoms), "
        "the electrical conductivity of semiconductors can be modulated across eight orders of magnitude. Understanding energy band theory, "
        "Fermi-Dirac statistics, charge carrier kinetics (drift and diffusion), space-charge depletion physics, and junction barrier potentials "
        "is the essential scientific prerequisite for analyzing diodes, bipolar junction transistors, field effect transistors, and optical transducers.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 2: THE ATOM & BOHR MODEL
    # -------------------------------------------------------------
    story.append(Paragraph("2.1 Atomic Structure, Bohr's Model, and Quantum Energy Shells", styles['SecH1']))
    story.append(Paragraph(
        "According to Niels Bohr's quantum model of the atom (1913), electrons orbit a dense, positively charged nucleus in discrete, quantized, "
        "non-radiating circular orbits. The orbital angular momentum of an electron is quantized in integer multiples of reduced Planck's constant: "
        "<i>L = m · v · r = n · (h / 2π) = n · ħ</i>, where <i>n = 1, 2, 3...</i> is the principal quantum number. "
        "The total energy of an electron in orbit <i>n</i> is quantized according to:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>E<sub>n</sub> = - [m · Z² · q⁴] / [8 · ε₀² · h² · n²] = - 13.6 · (Z² / n²) &nbsp;&nbsp;[eV]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "The negative sign denotes that the electron is bound within the electrostatic potential well of the nucleus; energy must be supplied "
        "externally to liberate the electron to the free state (<i>E = 0</i> at <i>n = ∞</i>).",
        styles['DocBody']
    ))

    story.append(create_figure("fig2_1_bohr_atom_silicon.png", "Bohr Atomic Model of Silicon (Z = 14) Illustrating Four Valence Electrons in the M-Shell", target_width=4.8*inch))

    story.append(Paragraph("2.1.1 Atomic Structure of Elemental Semiconductors: Silicon and Germanium", styles['SecH2']))
    story.append(Paragraph(
        "<b>1. Silicon (Si):</b> Atomic number <i>Z = 14</i>. Electron configuration: <i>1s² 2s² 2p⁶ 3s² 3p²</i>.<br/>"
        "&nbsp;&nbsp;&bull; K-Shell (n = 1): 2 electrons (completely filled).<br/>"
        "&nbsp;&nbsp;&bull; L-Shell (n = 2): 8 electrons (completely filled stable octet).<br/>"
        "&nbsp;&nbsp;&bull; M-Shell (n = 3): 4 valence electrons. These four outermost electrons dictate all chemical bonding and solid-state electronic properties.<br/>"
        "<b>2. Germanium (Ge):</b> Atomic number <i>Z = 32</i>. Electron configuration: <i>1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p²</i>.<br/>"
        "&nbsp;&nbsp;&bull; Outermost N-shell (n = 4) contains 4 valence electrons. Because the valence electrons in Germanium are further from the nucleus "
        "(shielded by 28 core electrons), they are more loosely bound, resulting in a lower bandgap (0.67 eV vs 1.12 eV for Silicon). However, Germanium's "
        "high thermal leakage current makes it inferior for high-temperature agricultural field operations.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 3: ENERGY BAND THEORY
    # -------------------------------------------------------------
    story.append(Paragraph("2.2 Energy Band Theory in Solids and Classification of Materials", styles['SecH1']))
    story.append(Paragraph(
        "In an isolated, gas-phase silicon atom, discrete, well-separated quantum energy states exist. However, when billions of silicon atoms "
        "condense into a monocrystalline solid lattice (atomic density <i>N = 5.0 × 10²² atoms/cm³</i> in diamond cubic crystal structure), "
        "the outer electron wavefunctions overlap significantly. According to the <b>Pauli Exclusion Principle</b>, no two identical fermions (electrons) "
        "within an interacting quantum system may occupy the identical quantum state. Consequently, as inter-atomic spacing decreases to the lattice equilibrium "
        "constant (<i>a = 5.43 Å = 0.543 nm</i> for Silicon), each discrete valence energy level splits into <i>N</i> closely spaced sub-levels. "
        "Because <i>N ≈ 10²²</i>, these sub-levels merge into continuous bands of allowed energy:",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>1. Valence Band (VB):</b> The lower permitted energy band occupied by the valence electrons that form covalent chemical bonds binding lattice atoms together. At absolute zero (0 K), the valence band is completely filled with electrons.<br/>"
        "<b>2. Conduction Band (CB):</b> The higher permitted energy band. Electrons in this band possess sufficient kinetic energy to break free from localized atomic bonds and drift freely throughout the crystal under an applied electric field, constituting electric current.<br/>"
        "<b>3. Forbidden Energy Gap (Bandgap, E<sub>g</sub>):</b> The forbidden energy zone separating the top of the valence band (<i>E_V</i>) from the bottom of the conduction band (<i>E_C</i>): <b>E<sub>g</sub> = E<sub>C</sub> - E<sub>V</sub></b>. No quantum electron states can exist inside <i>E_g</i> in a pure, defect-free crystal.",
        styles['DocBody']
    ))

    story.append(create_figure("fig2_2_energy_bands.png", "Comparative Energy Band Diagrams for Insulators, Semiconductors, and Conductors at Room Temperature", target_width=5.8*inch))

    story.append(Paragraph("2.2.1 Three-Way Material Classification Based on Bandgap Energy", styles['SecH2']))
    story.append(Paragraph(
        "<b>1. Insulators (e.g., Diamond, Quartz, SiO₂):</b> Possess an extremely wide forbidden gap (<i>E_g > 5.0 eV</i>; e.g., <i>E_g = 9.0 eV</i> for SiO₂). "
        "At room temperature (300 K), thermal kinetic energy (<i>kT ≈ 0.026 eV</i>) is vastly insufficient to bridge this gap. The conduction band is completely empty, "
        "resulting in near-zero electrical conductivity (<i>σ < 10⁻¹⁴ S/m</i>).<br/>"
        "<b>2. Semiconductors (e.g., Silicon, Germanium, GaAs):</b> Possess a moderate forbidden gap (<i>E_g ≈ 0.5 eV to 2.5 eV</i>; <i>E_g = 1.12 eV</i> for Si at 300 K). "
        "At room temperature, thermal vibrations supply sufficient energy to kick a small but significant number of electrons across <i>E_g</i> into the conduction band, "
        "creating mobile electrons and mobile holes.<br/>"
        "<b>3. Conductors (e.g., Copper, Aluminum, Silver):</b> Conduction and valence bands overlap (<i>E_g = 0 eV</i>), or the valence band is only partially filled. "
        "A vast reservoir of free electrons (density ~ 10²⁸ m⁻³) is available even at 0 K, yielding massive electrical conductivity (<i>σ ≈ 5.8 × 10⁷ S/m</i> for Copper).",
        styles['DocBody']
    ))

    mat_headers = ["Material Class", "Example Material", "Bandgap Energy (Eg @ 300K)", "Electrical Conductivity (σ)", "Free Electron Density (n)"]
    mat_rows = [
        ["Insulator", "Silicon Dioxide (SiO₂)", "9.0 eV", "10⁻¹⁶ to 10⁻¹² S/m", "~ 0 at room temperature"],
        ["Insulator", "Diamond (Carbon C)", "5.47 eV", "10⁻¹⁴ S/m", "~ 0 at room temperature"],
        ["Semiconductor", "Silicon (Si)", "1.12 eV (Indirect)", "10⁻⁴ to 10² S/m (Tunable)", "1.5 × 10¹⁰ cm⁻³ (Intrinsic)"],
        ["Semiconductor", "Germanium (Ge)", "0.67 eV (Indirect)", "2.2 S/m", "2.4 × 10¹³ cm⁻³ (Intrinsic)"],
        ["Semiconductor", "Gallium Arsenide (GaAs)", "1.42 eV (Direct)", "10⁻⁶ S/m", "1.8 × 10⁶ cm⁻³ (Intrinsic)"],
        ["Conductor", "Copper (Cu)", "0 eV (Overlapping bands)", "5.96 × 10⁷ S/m", "~ 8.5 × 10²² cm⁻³"],
        ["Conductor", "Aluminum (Al)", "0 eV (Overlapping bands)", "3.77 × 10⁷ S/m", "~ 6.0 × 10²² cm⁻³"]
    ]
    story.append(create_custom_table(mat_headers, mat_rows, [1.2*inch, 1.5*inch, 1.5*inch, 1.4*inch, 1.6*inch]))

    # -------------------------------------------------------------
    # SECTION 4: INTRINSIC & EXTRINSIC SEMICONDUCTORS
    # -------------------------------------------------------------
    story.append(Paragraph("2.3 Intrinsic Semiconductors, Covalent Bonding, and Hole Formation", styles['SecH1']))
    story.append(Paragraph(
        "An <b>intrinsic semiconductor</b> is a chemically pure monocrystalline material with zero intentional impurities (purity > 99.9999999%, 'nine-nines'). "
        "In a silicon crystal, each atom shares its four valence electrons with four adjacent neighbors, forming four stable two-electron <b>covalent bonds</b>. "
        "At absolute zero (0 K), all valence electrons are locked within these covalent bonds; the valence band is completely full and the conduction band is completely empty. "
        "Hence, pure silicon is a perfect insulator at 0 K.<br/>"
        "At room temperature (<i>T = 300 K ≈ 27°C</i>), thermal lattice vibrations impart kinetic energy to the bonded electrons. A small fraction of electrons gain energy "
        "exceeding <i>E_g = 1.12 eV</i>, breaking their covalent bonds and jumping into the conduction band as free mobile electrons. "
        "The ruptured covalent bond leaves behind a vacancy with an effective positive charge of <i>+q = +1.602 × 10⁻¹⁹ C</i>, designated as a <b>hole</b>.<br/>"
        "A hole acts as a physical positive charge carrier: when an electron from an adjacent intact bond hops into the vacancy, the hole moves in the opposite direction. "
        "In intrinsic semiconductors, thermal generation produces electrons and holes in exactly equal pairs (Electron-Hole Pairs, EHPs):",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>n = p = n<sub>i</sub>(T) = B · T<sup>3/2</sup> · e<sup>- E<sub>g</sub> / (2 k T)</sup></b> &nbsp;&nbsp;[cm⁻³]", styles['FormulaBox']))
    story.append(Paragraph(
        "where <i>n</i> is free electron concentration, <i>p</i> is hole concentration, <i>n_i</i> is intrinsic carrier concentration "
        "(<i>n_i ≈ 1.5 × 10¹⁰ cm⁻³</i> for Silicon at 300 K), <i>k = 1.381 × 10⁻²³ J/K = 8.617 × 10⁻⁵ eV/K</i> is Boltzmann's constant, "
        "and <i>B</i> is a material-dependent coefficient (<i>B ≈ 5.23 × 10¹⁵ cm⁻³·K⁻³/²</i> for Silicon).",
        styles['DocBody']
    ))

    story.append(Paragraph("2.4 Extrinsic Semiconductors: Doping Kinetics and Mass Action", styles['SecH1']))
    story.append(Paragraph(
        "Because intrinsic silicon has only 1.5 × 10¹⁰ free carriers per cm³ amidst 5 × 10²² lattice atoms (less than one free carrier per trillion atoms!), "
        "its electrical conductivity is extremely poor (<i>σ ≈ 4.4 × 10⁻⁴ S/m</i>). To create practical devices, the crystal is deliberately doped with foreign impurity atoms:<br/>"
        "<b>1. N-Type Semiconductor (Pentavalent Donor Doping):</b> Silicon is doped with Group V elements possessing five valence electrons "
        "(Phosphorus [P], Arsenic [As], Antimony [Sb]). Four valence electrons form covalent bonds with adjacent silicon atoms. The fifth extra electron is not required "
        "for bonding and orbits the donor nucleus in a hydrogen-like orbit with an extremely low ionization binding energy (<i>E_D ≈ 0.045 eV</i> below <i>E_C</i>). "
        "At room temperature (where thermal energy <i>kT ≈ 0.026 eV</i>), virtually 100% of donor atoms ionize (complete ionization), donating free electrons to the conduction band "
        "without creating corresponding holes. The ionized donor atoms remain locked in the crystal lattice as immobile positive ions (<i>N_D⁺</i>). "
        "In N-type material: <b>Electrons are MAJORITY carriers (n_n ≈ N_D)</b>, while <b>Holes are MINORITY carriers (p_n)</b>.<br/>"
        "<b>2. P-Type Semiconductor (Trivalent Acceptor Doping):</b> Silicon is doped with Group III elements possessing three valence electrons "
        "(Boron [B], Gallium [Ga], Indium [In]). The dopant atom forms three covalent bonds; the fourth bond lacks an electron, creating a localized vacancy. "
        "This vacancy creates an acceptor energy level <i>E_A</i> just 0.045 eV above the valence band. Valence electrons readily jump into this level, "
        "ionizing the acceptor atom into an immobile negative ion (<i>N_A⁻</i>) and generating a mobile hole in the valence band. "
        "In P-type material: <b>Holes are MAJORITY carriers (p_p ≈ N_A)</b>, while <b>Electrons are MINORITY carriers (n_p)</b>.",
        styles['DocBody']
    ))

    story.append(Paragraph("2.4.2 Carrier Drift, Diffusion & The Einstein Relation Derivation", styles['SecH2']))
    story.append(Paragraph(
        "Charge carriers move through a semiconductor lattice via two independent physical mechanisms:<br/>"
        "<b>1. Carrier Drift:</b> Transport driven by an applied electric field <i>E</i>. The field exerts an electrostatic force "
        "<i>F = q · E</i>, accelerating carriers between collisions with lattice phonons. The average terminal velocity is the <b>drift velocity</b>: "
        "<i>v_d = μ · E</i>, where <i>μ</i> is carrier mobility (cm²/V·s). Drift current density is: <b>J<sub>drift</sub> = q · (n · μ<sub>n</sub> + p · μ<sub>p</sub>) · E</b>.<br/>"
        "<b>2. Carrier Diffusion:</b> Transport driven by spatial concentration gradients (Fick's First Law of Diffusion). "
        "Carriers naturally disperse from regions of high concentration to regions of low concentration through random thermal Brownian motion. "
        "The diffusion current density is proportional to the concentration spatial gradient:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>J<sub>n,diff</sub> = + q · D<sub>n</sub> · (dn/dx) &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; J<sub>p,diff</sub> = - q · D<sub>p</sub> · (dp/dx) &nbsp;&nbsp;[A/cm²]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <i>D_n</i> and <i>D_p</i> are the electron and hole diffusion coefficients (cm²/s).<br/>"
        "<b>Mathematical Derivation of the Einstein Relation:</b><br/>"
        "Consider a non-uniformly doped semiconductor bar at thermal equilibrium with zero net current. An internal electric field <i>E(x)</i> "
        "develops to counteract diffusion. For holes: <i>J_p = q · p · μ_p · E - q · D_p · (dp/dx) = 0 &implies; p · μ_p · E = D_p · (dp/dx)</i>.<br/>"
        "From Boltzmann statistics, hole density follows: <i>p(x) = n_i · e^[ (E_i - E_F) / (kT) ]</i>. Differentiating with respect to <i>x</i>: "
        "<i>dp/dx = [ p / (kT) ] · (dE_i / dx) = - [ p · q / (kT) ] · E(x)</i> (since <i>E(x) = - dV/dx = (1/q) · dE_i/dx</i>).<br/>"
        "Substituting <i>dp/dx</i> back into the zero-current equation: <i>p · μ_p · E = D_p · [ (p · q · E) / (kT) ]</i>.<br/>"
        "Canceling <i>p · E</i> yields the fundamental <b>Einstein Relation</b>:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>D<sub>n</sub> / μ<sub>n</sub> = D<sub>p</sub> / μ<sub>p</sub> = (k · T) / q = V<sub>T</sub> &nbsp;&approx; 25.86 mV &nbsp;&nbsp;(at 300 K)</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "<b>2.4.3 Minority Carrier Lifetime and Diffusion Length (L_n, L_p):</b><br/>"
        "When excess minority carriers are generated by incident photons (as in agricultural pyranometers or solar cells), "
        "they survive for an average duration termed the <b>minority carrier lifetime (τ_n, τ_p)</b> before recombining with majority carriers. "
        "The average distance an excess minority carrier diffuses before recombining is the <b>diffusion length</b>:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>L<sub>n</sub> = √[ D<sub>n</sub> · τ<sub>n</sub> ] &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp; L<sub>p</sub> = √[ D<sub>p</sub> · τ<sub>p</sub> ] &nbsp;&nbsp;[cm or μm]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "In solar photovoltaic cells, the wafer thickness must be less than the minority carrier diffusion length (<i>W < L_p</i>) "
        "to ensure optically generated electron-hole pairs diffuse to the PN junction depletion layer and contribute to output current before recombining.",
        styles['DocBody']
    ))

    # Worked Example 4
    ex4_steps = [
        "1. Identify parameters: Operating temperature T = 300 K (V_T = 0.02586 V); hole mobility in N-type silicon base μ_p = 420 cm²/V·s; minority carrier lifetime τ_p = 12 μs = 1.2 × 10⁻⁵ s.",
        "2. Calculate hole diffusion coefficient D_p via Einstein relation: D_p = μ_p · V_T = (420 cm²/V·s) × 0.02586 V = 10.86 cm²/s.",
        "3. Compute minority carrier diffusion length L_p: L_p = √[ D_p · τ_p ] = √[ (10.86 cm²/s) × (1.2 × 10⁻⁵ s) ] = √[ 1.3032 × 10⁻⁴ cm² ] = 0.01142 cm = 114.2 μm.",
        "4. Photovoltaic design evaluation: For solar cells powering farm water pumps, the silicon wafer thickness is typically 180 μm. Since L_p = 114 μm, carriers generated in the upper two-thirds of the wafer easily reach the PN junction to produce electricity. If wafer quality degrades (reducing lifetime to 2 μs), L_p drops to 46 μm, causing over 60% of photogenerated carriers to recombine uselessly as heat!",
        "5. Recombination velocity check: Surface passivation using silicon nitride (SiN_x) reduces surface recombination velocity S from >10,000 cm/s down to <50 cm/s, maximizing agricultural solar panel efficiency."
    ]
    story.append(create_example(4, "Minority Carrier Diffusion Length & Lifetime in Agricultural Solar Pumping Cells",
                                "A monocrystalline silicon solar cell designed for solar water pumping in Dodoma has an N-type base with hole mobility μ_p = 420 cm²/V·s and minority hole lifetime τ_p = 12 μs at 300 K. Compute the hole diffusion coefficient D_p, the minority carrier diffusion length L_p, and evaluate the required wafer thickness.",
                                ex4_steps))

    # Worked Example 5
    ex5_steps = [
        "1. State intrinsic carrier concentration equation: n_i(T) = B · T^(3/2) · e^(-E_g / (2 k T)).",
        "2. Constants: k = 8.617 × 10⁻⁵ eV/K; E_g = 1.12 eV; B = 5.23 × 10¹⁵ cm⁻³·K⁻³/².",
        "3. Condition 1 (Dodoma Winter Night, T₁ = 15°C = 288.15 K):",
        "   Thermal voltage: k T₁ = (8.617 × 10⁻⁵) × 288.15 = 0.02483 eV.",
        "   Exponent: - E_g / (2 k T₁) = - 1.12 / (2 × 0.02483) = - 22.553.",
        "   T₁^(3/2) = (288.15)^(1.5) = 4,891.4.",
        "   n_i(288K) = (5.23 × 10¹⁵) × (4,891.4) × e^(-22.553) = (2.558 × 10¹⁹) × (1.604 × 10⁻¹⁰) = 4.10 × 10⁹ cm⁻³.",
        "4. Condition 2 (Greenhouse Mid-Day Peak, T₂ = 45°C = 318.15 K):",
        "   Thermal voltage: k T₂ = (8.617 × 10⁻⁵) × 318.15 = 0.02741 eV.",
        "   Exponent: - E_g / (2 k T₂) = - 1.12 / (2 × 0.02741) = - 20.430.",
        "   T₂^(3/2) = (318.15)^(1.5) = 5,674.7.",
        "   n_i(318K) = (5.23 × 10¹⁵) × (5,674.7) × e^(-20.430) = (2.968 × 10¹⁹) × (1.339 × 10⁻⁹) = 3.97 × 10¹⁰ cm⁻³.",
        "5. Ratio of intrinsic carrier increase: n_i(45°C) / n_i(15°C) = (3.97 × 10¹⁰) / (4.10 × 10⁹) = 9.68 times increase!",
        "6. Sensor impact: Reverse saturation leakage current I_S ∝ n_i². Leakage increases by (9.68)² = 93.7 times! This explains why agricultural photodiode and temperature telemetry circuits require temperature compensation to prevent huge calibration offsets across the day."
    ]
    story.append(create_example(5, "Extreme Temperature Dependency of Intrinsic Carriers in Tanzanian Agro-Climates",
                                "Evaluate the shift in intrinsic carrier concentration n_i for silicon operating in Tanzania between a cold winter night in Dodoma (15°C = 288 K) and an enclosed tropical greenhouse afternoon in Morogoro (45°C = 318 K). Compute the percentage increase in n_i and calculate the resulting increase in diode reverse leakage current I_S.",
                                ex5_steps))

    story.append(Paragraph("2.4.4 Complete Charge Neutrality Condition in Doped Crystals", styles['SecH2']))
    story.append(Paragraph(
        "Although extrinsic semiconductors contain high densities of mobile carriers, the overall crystal remains <b>strictly electrically neutral</b>. "
        "The total positive charge density (mobile holes <i>p</i> plus fixed ionized donors <i>N_D⁺</i>) exactly balances the total negative charge density "
        "(mobile electrons <i>n</i> plus fixed ionized acceptors <i>N_A⁻</i>):",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>p + N<sub>D</sub><sup>+</sup> = n + N<sub>A</sub><sup>-</sup> &nbsp;&implies;&nbsp; p - n + N<sub>D</sub> - N<sub>A</sub> = 0</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "In a compensated semiconductor doped with both donors and acceptors: if <i>N_D > N_A</i>, the material behaves as N-type with effective net donor concentration "
        "<i>N_D,eff = N_D - N_A</i>, and majority electron concentration <i>n ≈ N_D - N_A</i>. "
        "Conversely, if <i>N_A > N_D</i>, the material behaves as P-type with <i>p ≈ N_A - N_D</i>.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "Under thermal equilibrium, the rate of thermal carrier generation equals the rate of electron-hole recombination. "
        "This establishes the fundamental <b>Law of Mass Action</b>, valid for both intrinsic and doped semiconductors at constant temperature:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>n · p = n<sub>i</sub>² &nbsp;&nbsp;(Holds at thermal equilibrium)</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "For N-type silicon with donor concentration <i>N_D >> n_i</i>: <i>n_n ≈ N_D</i> and <b>p_n = n<sub>i</sub>² / N_D</b>.<br/>"
        "For P-type silicon with acceptor concentration <i>N_A >> n_i</i>: <i>p_p ≈ N_A</i> and <b>n_p = n<sub>i</sub>² / N_A</b>.<br/>"
        "Total electrical conductivity <i>σ</i> under an electric field is the sum of electron and hole drift currents:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>σ = q · [ n · μ<sub>n</sub> + p · μ<sub>p</sub> ] &nbsp;&nbsp;[S/cm or S/m]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <i>q = 1.602 × 10⁻¹⁹ C</i>, <i>μ_n</i> is electron mobility (≈ 1,350 cm²/V·s in Silicon at 300K), "
        "and <i>μ_p</i> is hole mobility (≈ 480 cm²/V·s). Notice that electron mobility is approximately three times higher than hole mobility "
        "because electrons move freely in the conduction band while holes move via inter-atomic valence hopping. "
        "This is why NPN transistors and N-channel MOSFETs exhibit higher speed and lower on-resistance than PNP and P-channel equivalents.",
        styles['DocBody']
    ))

    # Worked Example 1
    ex1_steps = [
        "1. Identify parameters: Temperature T = 300 K; intrinsic carrier density n_i = 1.5 × 10¹⁰ cm⁻³; Boron acceptor concentration N_A = 2.5 × 10¹⁶ cm⁻³; mobilities μ_p = 450 cm²/V·s, μ_n = 1,300 cm²/V·s.",
        "2. Calculate majority carrier concentration: Under complete thermal ionization at 300 K: p_p ≈ N_A = 2.5 × 10¹⁶ holes/cm³.",
        "3. Calculate minority carrier concentration via Law of Mass Action: n_p = n_i² / N_A = (1.5 × 10¹⁰)² / (2.5 × 10¹⁶) = (2.25 × 10²⁰) / (2.5 × 10¹⁶) = 9,000 electrons/cm³.",
        "4. Calculate electrical conductivity: σ = q · [p · μ_p + n · μ_n]. Since p >> n (2.5 × 10¹⁶ >> 9,000), minority electron contribution is completely negligible: σ ≈ q · N_A · μ_p = (1.602 × 10⁻¹⁹ C) × (2.5 × 10¹⁶ cm⁻³) × (450 cm²/V·s) = 1.802 S/cm = 180.2 S/m.",
        "5. Calculate electrical resistivity: ρ = 1 / σ = 1 / 1.802 S/cm = 0.555 Ω·cm = 5.55 × 10⁻³ Ω·m.",
        "6. Contrast with intrinsic silicon resistivity: σ_intrinsic = q · n_i · (μ_n + μ_p) = (1.602 × 10⁻¹⁹) × (1.5 × 10¹⁰) × (1,300 + 450) = 4.205 × 10⁻⁶ S/cm → ρ_intrinsic = 237,800 Ω·cm. Adding just one Boron atom per 2 million silicon atoms reduced resistivity by 428,000 times!"
    ]
    story.append(create_example(1, "Majority/Minority Carrier Density and Conductivity in P-Type Agricultural Sensor Silicon",
                                "A monocrystalline P-type silicon wafer for an agricultural soil nitrate ion-selective field effect sensor (ISFET) is uniformly doped with Boron at N_A = 2.5 × 10¹⁶ cm⁻³ at 300 K. Calculate the majority hole density p_p, minority electron density n_p, electrical conductivity σ, and electrical resistivity ρ.",
                                ex1_steps))

    # -------------------------------------------------------------
    # SECTION 5: THE PN JUNCTION & DEPLETION PHYSICS
    # -------------------------------------------------------------
    story.append(Paragraph("2.5 The PN Junction: Depletion Physics and Built-In Barrier Potential", styles['SecH1']))
    story.append(Paragraph(
        "When P-type and N-type semiconductor regions are formed adjacent to each other within a continuous monocrystalline lattice, "
        "an extreme carrier concentration gradient is created across the metallurgical boundary: the hole density drops abruptly from "
        "<i>p_p ≈ 10¹⁷ cm⁻³</i> on the P-side to <i>p_n ≈ 10⁴ cm⁻³</i> on the N-side, while electron density drops from <i>n_n ≈ 10¹⁷ cm⁻³</i> "
        "on the N-side to <i>n_p ≈ 10⁴ cm⁻³</i> on the P-side.<br/>"
        "Driven by this concentration gradient, mobile electrons diffuse across the junction from the N-region into the P-region, "
        "and mobile holes diffuse from the P-region into the N-region. As mobile carriers cross, they recombine with opposite majority carriers. "
        "Crucially, the mobile charges leave behind uncompensated, fixed dopant ions locked in the crystal lattice: "
        "<b>positively charged donor ions (N<sub>D</sub>⁺)</b> on the N-side and <b>negatively charged acceptor ions (N<sub>A</sub>⁻)</b> on the P-side.<br/>"
        "This space-charge region is swept completely clear of free mobile charge carriers and is termed the <b>depletion layer</b> (or space-charge region).",
        styles['DocBody']
    ))

    story.append(create_figure("fig2_3_pn_junction_equilibrium.png", "Unbiased PN Junction Space Charge Depletion Region, Electric Field, and Built-In Barrier", target_width=5.8*inch))

    story.append(Paragraph("2.5.1 Mathematical Derivation of the Built-In Barrier Potential (V₀)", styles['SecH2']))
    story.append(Paragraph(
        "The uncompensated space-charge ions create an internal electric field <i>E(x)</i> directed from the positive N-side to the negative P-side. "
        "This field exerts an electrostatic drift force on mobile charges that directly opposes further diffusion. "
        "Thermal equilibrium is achieved when the forward diffusion current is exactly balanced by the reverse drift current for both electrons and holes: "
        "<i>J<sub>total</sub> = J<sub>drift</sub> + J<sub>diffusion</sub> = 0</i>.<br/>"
        "For holes: <i>J_p = q · p · μ_p · E - q · D_p · (dp/dx) = 0</i>, where <i>D_p</i> is the hole diffusion coefficient. "
        "Using the Einstein relation <i>D_p / μ_p = V_T = k T / q</i>, we express the electric field as: <i>E = - dV/dx = (V_T / p) · (dp/dx)</i>.<br/>"
        "Integrating this potential difference across the depletion layer from the P-neutral edge (where <i>p = p_p ≈ N_A</i>) "
        "to the N-neutral edge (where <i>p = p_n = n_i² / N_D</i>):",
        styles['DocBody']
    ))
    story.append(Paragraph("V₀ = - ∫ E dx = V_T · ∫<sub>p_n</sub><sup>p_p</sup> (dp / p) = V_T · ln(p_p / p_n) = V_T · ln[ N_A / (n_i² / N_D) ]", styles['FormulaBox']))
    story.append(Paragraph(
        "This yields the celebrated <b>Built-In Barrier Potential Equation</b>:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>V₀ = V<sub>T</sub> · ln [ (N<sub>A</sub> · N<sub>D</sub>) / n<sub>i</sub>² ] &nbsp;&nbsp;[Volts]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <i>V_T = k T / q ≈ 25.86 mV ≈ 26 mV</i> at 300 K. For standard silicon doping levels (10¹⁶ to 10¹⁸ cm⁻³), "
        "<i>V₀ ≈ 0.65 V to 0.85 V</i> (and ≈ 0.25 V to 0.35 V for Germanium).<br/>"
        "Solving Poisson's equation <i>d²V/dx² = - ρ(x) / ε_s</i> yields the total equilibrium <b>depletion width (W)</b>:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>W = √ [ (2 · ε<sub>s</sub> · V₀ / q) · ( (1 / N<sub>A</sub>) + (1 / N<sub>D</sub>) ) ] &nbsp;&nbsp;[meters]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <i>ε_s = ε_r · ε_0 ≈ 11.7 × 8.854 × 10⁻¹² F/m = 1.036 × 10⁻¹⁰ F/m</i> is the electrical permittivity of silicon.",
        styles['DocBody']
    ))

    # Worked Example 2
    ex2_steps = [
        "1. Identify parameters: T = 300 K → V_T = 0.02586 V; N_A = 1.0 × 10¹⁷ cm⁻³; N_D = 2.0 × 10¹⁶ cm⁻³; n_i = 1.5 × 10¹⁰ cm⁻³; ε_s = 1.036 × 10⁻¹² F/cm.",
        "2. Compute donor-acceptor product: N_A · N_D = (1.0 × 10¹⁷) × (2.0 × 10¹⁶) = 2.0 × 10³³ cm⁻⁶.",
        "3. Compute n_i²: (1.5 × 10¹⁰)² = 2.25 × 10²⁰ cm⁻⁶.",
        "4. Ratio: (N_A · N_D) / n_i² = (2.0 × 10³³) / (2.25 × 10²⁰) = 8.889 × 10¹².",
        "5. Natural logarithm: ln(8.889 × 10¹²) = 29.815.",
        "6. Calculate built-in potential: V₀ = 0.02586 V × 29.815 = 0.7710 V = 771 mV.",
        "7. Calculate depletion width W: W = √[ (2 × 1.036×10⁻¹² × 0.7710 / 1.602×10⁻¹⁹) × (1/10¹⁷ + 1/(2×10¹⁶)) ]",
        "   = √[ (1.5975 × 10⁷) × (1.0×10⁻¹⁷ + 5.0×10⁻¹⁷) ] = √[ (1.5975 × 10⁷) × (6.0 × 10⁻¹⁷) ] = √[ 9.585 × 10⁻¹⁰ ] = 3.096 × 10⁻⁵ cm = 0.310 μm.",
        "8. Calculate peak electric field at metallurgical junction: E_max = (2 · V₀) / W = (2 × 0.7710 V) / (3.096 × 10⁻⁵ cm) = 49,806 V/cm ≈ 5.0 × 10⁶ V/m. Notice the enormous internal field strength (~50 kV/cm) across sub-micron dimensions!"
    ]
    story.append(create_example(2, "Analytical Derivation of Built-In Potential and Depletion Width in Alternator Diode",
                                "A power rectifier diode for a Massey Ferguson tractor alternator is fabricated with acceptor doping N_A = 1.0 × 10¹⁷ cm⁻³ and donor doping N_D = 2.0 × 10¹⁶ cm⁻³ at 300 K. Calculate the junction built-in barrier potential V₀, the equilibrium depletion width W, and the maximum internal electric field intensity E_max.",
                                ex2_steps))

    # -------------------------------------------------------------
    # SECTION 6: FORWARD & REVERSE BIASING
    # -------------------------------------------------------------
    story.append(Paragraph("2.6 Biasing the PN Junction: Forward Bias, Reverse Bias & Band Bending", styles['SecH1']))
    story.append(Paragraph(
        "Applying an external DC voltage across the PN junction dramatically perturbs the equilibrium drift-diffusion balance:<br/>"
        "<b>1. Forward Bias (V<sub>applied</sub> > 0):</b> Positive terminal connected to P-region, negative to N-region.<br/>"
        "&nbsp;&nbsp;&bull; The external electric field directly opposes the internal built-in field.<br/>"
        "&nbsp;&nbsp;&bull; The net junction potential barrier is reduced from <i>V₀</i> to <b>(V₀ - V<sub>applied</sub>)</b>.<br/>"
        "&nbsp;&nbsp;&bull; The depletion layer width narrows: <b>W<sub>forward</sub> = W₀ · √[ 1 - (V<sub>applied</sub> / V₀) ]</b>.<br/>"
        "&nbsp;&nbsp;&bull; Once forward bias reaches the cut-in voltage (~0.7V for Si, ~0.3V for Ge), majority carriers flood across the junction. "
        "Injected minority carriers diffuse through the neutral regions, yielding an enormous exponential forward current: <i>I_D ∝ e^(V_D / V_T)</i>.<br/>"
        "<b>2. Reverse Bias (V<sub>applied</sub> < 0):</b> Positive terminal connected to N-region, negative to P-region.<br/>"
        "&nbsp;&nbsp;&bull; The external electric field reinforces the internal built-in field.<br/>"
        "&nbsp;&nbsp;&bull; The net barrier height increases to <b>(V₀ + |V<sub>applied</sub>|)</b>.<br/>"
        "&nbsp;&nbsp;&bull; The depletion layer widens: <b>W<sub>reverse</sub> = W₀ · √[ 1 + (|V<sub>applied</sub>| / V₀) ]</b>.<br/>"
        "&nbsp;&nbsp;&bull; Majority carrier diffusion is completely halted. The only current is the minuscule <b>reverse saturation current (I<sub>S</sub>)</b> "
        "caused by thermally generated minority carriers that drift into the depletion zone and get swept across by the intense electric field. "
        "Because <i>I_S</i> depends solely on thermal carrier generation (and not on reverse voltage magnitude), it is constant until reverse breakdown occurs.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 7: THE HALL EFFECT
    # -------------------------------------------------------------
    story.append(Paragraph("2.5.2 Junction Capacitance and Diffusion Capacitance in PN Diodes", styles['SecH2']))
    story.append(Paragraph(
        "A reverse-biased PN junction behaves physically as a parallel-plate capacitor whose plate separation equals the depletion width <i>W</i>. "
        "Because the depletion width varies with the square root of the applied reverse voltage, the <b>junction (depletion) capacitance (C<sub>j</sub>)</b> "
        "is voltage-dependent:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>C<sub>j</sub> = (ε<sub>s</sub> · A) / W = C<sub>j0</sub> / √[ 1 + (V<sub>R</sub> / V₀) ] &nbsp;&nbsp;[Farads, F]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <i>C_j0</i> is the zero-bias junction capacitance. This voltage-variable capacitance is exploited in varactor diodes for RF tuning "
        "in agricultural drone telemetry.<br/>"
        "Under <b>forward bias</b>, minority carriers injected across the junction accumulate in the neutral regions before recombining. "
        "This stored minority charge <i>Q_d = I_D · τ_T</i> (where <i>τ_T</i> is transit time) gives rise to <b>diffusion capacitance (C<sub>d</sub>)</b>:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>C<sub>d</sub> = (dQ<sub>d</sub> / dV<sub>D</sub>) = (τ<sub>T</sub> · I<sub>D</sub>) / (η · V<sub>T</sub>) &nbsp;&nbsp;[Farads, F]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "Notice that diffusion capacitance is directly proportional to forward current <i>I_D</i> and is typically hundreds of times larger than <i>C_j</i> "
        "(e.g., hundreds of picofarads to nanofarads). When switching a diode from forward conduction to reverse blocking, this stored minority charge "
        "must be cleared, producing a transient reverse current spike lasting for the <b>reverse recovery time (t<sub>rr</sub>)</b>. "
        "In high-frequency agricultural solar inverters (20 kHz to 100 kHz), standard diodes overheat due to reverse recovery losses, demanding ultrafast or Schottky diodes.",
        styles['DocBody']
    ))

    story.append(Paragraph("2.7.1 Hall Effect Integrated Circuits: Linear Sensors vs. Digital Switches", styles['SecH2']))
    story.append(Paragraph(
        "In commercial agricultural equipment, discrete semiconductor Hall slabs are packaged into integrated circuits (ICs) featuring internal "
        "operational amplifiers, temperature compensation circuitry, and Schmitt-trigger logic:<br/>"
        "<b>1. Linear (Ratiometric) Hall Sensors (e.g., SS49E):</b> Output an analog voltage proportional to magnetic flux density: "
        "<i>V_out = (V_CC / 2) ± Sensitivity · B</i>. Used for contactless throttle pedals on electric farm utility vehicles and hydraulic proportional valve spool position feedback.<br/>"
        "<b>2. Digital Hall Switches (e.g., A3144, US1881):</b> Feature an on-chip Schmitt trigger comparator and open-collector output transistor. "
        "When the magnetic field exceeds the <b>Magnetic Operate Point (B<sub>OP</sub>)</b>, the output pulls LOW. When the field drops below the "
        "<b>Magnetic Release Point (B<sub>RP</sub>)</b>, the output turns OFF. The magnetic hysteresis (<i>B_HYS = B_OP - B_RP</i>) eliminates contact chatter and electrical noise.",
        styles['DocBody']
    ))

    # Worked Example 6
    ex6_steps = [
        "1. Identify milling machine operating parameters: Hammer mill rotor speed N = 2,800 RPM; sensing target is a 24-tooth steel gear wheel mounted on the rotor shaft; digital Hall-effect gear tooth sensor (A3144).",
        "2. Calculate tooth passing frequency at full operational speed: f_tooth = (N / 60) × Number of teeth = (2,800 / 60) × 24 = 46.667 rev/s × 24 = 1,120 Hz = 1.12 kHz.",
        "3. Pulse period: T_pulse = 1 / f_tooth = 1 / 1,120 Hz = 8.928 × 10⁻⁴ s = 892.8 μs.",
        "4. Microcontroller timer input capture resolution: The microcontroller running FreeRTOS on a smart mill monitor has a timer clock f_timer = 80 MHz (clock period t_clk = 12.5 ns).",
        "5. Timer counts per gear tooth pulse: Counts = T_pulse / t_clk = (892.8 × 10⁻⁶ s) / (12.5 × 10⁻⁹ s) = 71,424 timer ticks.",
        "6. Speed measurement precision: At 71,424 ticks, a single tick uncertainty yields an RPM measurement resolution of ΔN / N = 1 / 71,424 ≈ 0.0014% (ultra-high precision!).",
        "7. Clogging alarm threshold: If the hammer mill chamber becomes clogged with wet maize, rotor speed drops by 15% (to 2,380 RPM). The detected pulse frequency drops to 952 Hz (T_pulse = 1,050 μs). The microcontroller detects this within 5 ms, instantly cutting power to the auger feed motor to prevent belt burning and motor burnout."
    ]
    story.append(create_example(6, "Digital Hall-Effect Speed Telemetry for Commercial Maize Hammer Mill in Morogoro",
                                "A commercial maize hammer mill in Morogoro uses an A3144 digital Hall gear-tooth sensor to monitor a 24-tooth steel sprocket on a 2,800 RPM rotor shaft. Calculate the tooth passing frequency, the pulse period, the timer input capture ticks for an 80 MHz microcontroller, and determine the pulse period threshold that triggers an emergency auger shutoff when speed drops by 15% due to chamber clogging.",
                                ex6_steps))
    story.append(Paragraph(
        "Discovered by American physicist Edwin Hall in 1879, the <b>Hall Effect</b> describes the generation of a transverse potential difference "
        "across a current-carrying conductor or semiconductor when immersed in a perpendicular magnetic field. "
        "Consider a semiconductor slab of width <i>w</i>, thickness <i>t</i>, and length <i>L</i> carrying a longitudinal current <i>I_x</i> "
        "along the x-axis, subjected to a normal magnetic flux density <i>B_z</i> along the z-axis.<br/>"
        "Moving charge carriers with drift velocity <i>v_d</i> experience a transverse magnetic <b>Lorentz force</b>: <b>F<sub>B</sub> = q · (v<sub>d</sub> × B)</b>.<br/>"
        "For an N-type semiconductor where carriers are negative electrons (<i>q = -e</i>) drifting in the -x direction: the vector cross-product "
        "deflects electrons toward the bottom face (-y). Negative charges accumulate on the bottom face, leaving positive ionized donor atoms on the top face (+y). "
        "This charge separation sets up a transverse <b>Hall electric field (E<sub>H</sub>)</b> that exerts an opposing electrostatic force: <b>F<sub>E</sub> = q · E<sub>H</sub></b>.<br/>"
        "Equilibrium is reached when electrostatic force exactly balances magnetic force: <i>q · E_H = q · v_d · B_z &implies; E_H = v_d · B_z</i>.<br/>"
        "Since current density is <i>J_x = I_x / (w · t) = n · q · v_d &implies; v_d = I_x / (n · q · w · t)</i>, the transverse Hall voltage <i>V_H = E_H · w</i> is:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>V<sub>H</sub> = (I<sub>x</sub> · B<sub>z</sub>) / (n · q · t) = R<sub>H</sub> · (I<sub>x</sub> · B<sub>z</sub>) / t &nbsp;&nbsp;[Volts]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <b>R<sub>H</sub> = 1 / (n · q)</b> is the <b>Hall Coefficient</b> (m³/C).<br/>"
        "<b>Engineering Significance:</b> In metals, free electron density is massive (<i>n ≈ 10²⁸ m⁻³</i>), making <i>V_H</i> minuscule (microvolts). "
        "In semiconductors, carrier density is thousands of times lower (<i>n ≈ 10²¹ m⁻³</i>), producing robust, easily measurable Hall voltages "
        "(10 mV to 100 mV). Furthermore, the polarity of <i>V_H</i> unambiguously reveals the sign of majority charge carriers (negative for N-type, positive for P-type).",
        styles['DocBody']
    ))

    story.append(create_figure("fig2_4_hall_effect_sensor.png", "Hall Effect Physical Deflection Mechanism in Agricultural Wheel Speed & Shaft RPM Transducers", target_width=5.5*inch))

    story.append(create_callout(
        "Agricultural Machinery Application: Non-Contact Sensing in Sugarcane Harvesters",
        "Austoft sugarcane harvesters operating in the wet, muddy soils of Kilombero utilize Hall effect magnetic proximity sensors to monitor: "
        "(1) Base-cutter disc rotational speed, (2) Chopper drum blade synchronization, and (3) Wheel slip telemetry. "
        "Optical encoders fail instantly due to cane sap, mud, and flying trash. Because Hall sensors detect magnetic flux variations through solid steel "
        "enclosures, they are 100% immune to dirt, water, diesel fuel, and severe mechanical vibration."
    ))

    # Worked Example 3
    ex3_steps = [
        "1. Identify parameters: Sensor thickness t = 0.15 mm = 1.5 × 10⁻⁴ m; longitudinal bias current I_x = 12 mA = 0.012 A; magnetic flux density B_z = 0.28 Tesla; majority electron carrier density n = 2.0 × 10¹⁵ cm⁻³ = 2.0 × 10²¹ m⁻³.",
        "2. Fundamental charge: q = 1.602 × 10⁻¹⁹ C.",
        "3. Compute the Hall coefficient R_H: R_H = 1 / (n · q) = 1 / [ (2.0 × 10²¹ m⁻³) × (1.602 × 10⁻¹⁹ C) ] = 1 / 320.4 = 3.121 × 10⁻³ m³/C.",
        "4. Calculate output Hall voltage: V_H = (R_H · I_x · B_z) / t = (3.121 × 10⁻³ m³/C × 0.012 A × 0.28 T) / (1.5 × 10⁻⁴ m) = (1.0487 × 10⁻⁵) / (1.5 × 10⁻⁴) = 0.06991 V = 69.91 mV.",
        "5. Amplifier design: To interface this 69.9 mV signal with a 3.3V microcontroller ADC, an instrumentation amplifier with gain A_v = 3.3V / 0.070V ≈ 47.1 is designed.",
        "6. Carrier mobility evaluation: If semiconductor conductivity is σ = 380 S/m, calculate electron mobility μ_n: μ_n = σ · R_H = 380 S/m × (3.121 × 10⁻³ m³/C) = 1.186 m²/V·s = 11,860 cm²/V·s (High mobility, typical of Gallium Arsenide or Indium Antimonide)."
    ]
    story.append(create_example(3, "Hall Effect Speed Transducer Calculation for Combine Harvester Drum RPM",
                                "A combine harvester threshing drum rotation sensor uses an N-type semiconductor Hall slab of thickness t = 0.15 mm and donor concentration n = 2.0 × 10¹⁵ cm⁻³. Driven by bias current I_x = 12 mA, a passing gear tooth generates a magnetic flux density B_z = 0.28 T. Calculate the Hall coefficient R_H, the output Hall voltage V_H, and evaluate the electron mobility if conductivity σ = 380 S/m.",
                                ex3_steps))

    # Worked Example 4
    ex4_steps = [
        "1. Identify physical parameters: Base-emitter silicon forward voltage temperature coefficient dV_F/dT = -2.1 mV/°C at constant current bias I_bias = 100 μA. Baseline voltage V_F(25°C) = 0.650 V.",
        "2. Morogoro Silo ambient temperature extremes: Minimum pre-dawn winter temperature T_min = 18°C; Maximum summer peak grain fermentation hotspot temperature T_max = 65°C.",
        "3. Compute forward voltage at minimum temperature (18°C): ΔT_low = 18 - 25 = -7°C. V_F(18°C) = 0.650 V + [(-2.1 mV/°C) × (-7°C)] = 0.650 V + 0.0147 V = 0.6647 V.",
        "4. Compute forward voltage at hotspot threshold (65°C): ΔT_high = 65 - 25 = +40°C. V_F(65°C) = 0.650 V + [(-2.1 mV/°C) × (+40°C)] = 0.650 V - 0.0840 V = 0.5660 V.",
        "5. Signal Span and ADC Resolution: Voltage span ΔV_out = 0.6647 V - 0.5660 V = 98.7 mV. For a 12-bit ADC with 3.3V reference (resolution = 3.3V / 4096 = 0.8057 mV/LSB), the sensor produces (2.1 mV/°C) / 0.8057 mV/LSB = 2.6 LSB per °C, enabling 0.38°C temperature measurement resolution across the maize silo bulk.",
        "6. Design Conclusion: A constant current source biasing a 1N4148 or 2N3904 diode provides a robust, low-cost sensor immune to moisture and corrosion inside grain silos."
    ]
    story.append(create_example(4, "Silicon Bandgap Temperature Transducer Design for Morogoro Maize Silo Hotspot Detection",
                                "Deep inside Morogoro metal maize silos, biological spoilage and insect infestation cause localized hotspots exceeding 55°C. A multi-point probe string uses silicon PN junction diodes biased at constant forward current I_bias = 100 μA. Given dV_F/dT = -2.1 mV/°C and V_F(25°C) = 0.650 V, calculate the sensor voltage across the operational range 18°C to 65°C, determine the span, and evaluate the resolution when digitized by a 12-bit microcontroller ADC (V_ref = 3.3V).",
                                ex4_steps))

    # Worked Example 5
    ex5_steps = [
        "1. Identify junction parameters: Donor concentration N_D = 2.0 × 10¹⁶ cm⁻³; Acceptor concentration N_A = 1.0 × 10¹⁸ cm⁻³ (p⁺-n one-sided abrupt junction); Cross-sectional area A = 1.2 × 10⁻³ cm² = 1.2 × 10⁻⁷ m²; Relative permittivity of silicon ε_r = 11.7; Permittivity of vacuum ε_0 = 8.854 × 10⁻¹² F/m; Built-in barrier potential V_0 = 0.82 V at 300 K.",
        "2. Effective semiconductor permittivity: ε_s = ε_r × ε_0 = 11.7 × 8.854 × 10⁻¹² = 1.036 × 10⁻¹⁰ F/m = 1.036 × 10⁻¹² F/cm.",
        "3. Depletion layer width formula for one-sided abrupt junction (N_A >> N_D): W = √[ (2 · ε_s · (V_0 + V_R)) / (q · N_D) ].",
        "4. Compute depletion width at minimum reverse tuning voltage V_R = 1.0 V: W(1V) = √[ (2 × 1.036 × 10⁻¹² × (0.82 + 1.0)) / (1.602 × 10⁻¹⁹ × 2.0 × 10¹⁶) ] = √[ 3.771 × 10⁻¹² / 3.204 × 10⁻³ ] = √[ 1.177 × 10⁻⁹ cm² ] = 3.43 × 10⁻⁵ cm = 0.343 μm.",
        "5. Compute junction capacitance at V_R = 1.0 V: C_j(1V) = (ε_s · A) / W = [ (1.036 × 10⁻¹² F/cm) × (1.2 × 10⁻³ cm²) ] / (3.43 × 10⁻⁵ cm) = 1.243 × 10⁻¹⁵ / 3.43 × 10⁻⁵ = 3.62 × 10⁻¹¹ F = 36.2 pF.",
        "6. Compute depletion width and capacitance at maximum tuning voltage V_R = 12.0 V: Total reverse voltage = 0.82 + 12.0 = 12.82 V. W(12V) = W(1V) × √(12.82 / 1.82) = 0.343 μm × 2.654 = 0.910 μm. Capacitance C_j(12V) = C_j(1V) / 2.654 = 36.2 pF / 2.654 = 13.64 pF.",
        "7. Capacitance Tuning Ratio: TR = C_j(1V) / C_j(12V) = 36.2 pF / 13.64 pF = 2.65:1. This enables voltage-controlled frequency synthesis from 433 MHz to 434.7 MHz in Tanzanian livestock tracking collar transceivers."
    ]
    # Worked Example 7
    ex7_steps = [
        "1. Problem Definition: A high-power solar photovoltaic pump inverter at Bahi, Dodoma utilizes silicon rectifier diodes with junction area A = 0.05 cm² and donor doping N_D = 1.0 × 10¹⁶ cm⁻³. During peak afternoon pumping at ambient T_amb = 45°C, junction temperature reaches T_j = 125°C (398 K).",
        "2. Formulate Intrinsic Concentration Temperature Law: n_i(T) = B · T^(3/2) · exp[ -E_g / (2 · k_B · T) ], where B = 5.23 × 10¹⁵ cm⁻³·K^(-3/2), E_g = 1.12 eV, and k_B = 8.617 × 10⁻⁵ eV/K.",
        "3. Compute Intrinsic Concentration at 25°C (298 K): n_i(298 K) = 1.50 × 10¹⁰ cm⁻³.",
        "4. Compute Intrinsic Concentration at 125°C (398 K):",
        "   Exponent = -1.12 eV / [ 2 × (8.617 × 10⁻⁵ eV/K) × 398 K ] = -1.12 / 0.06859 = -16.329.",
        "   Prefactor = (5.23 × 10¹⁵) × (398)^(1.5) = (5.23 × 10¹⁵) × 7,940 = 4.153 × 10¹⁹.",
        "   n_i(398 K) = (4.153 × 10¹⁹) × exp(-16.329) = (4.153 × 10¹⁹) × (8.10 × 10⁻⁸) = 3.364 × 10¹² cm⁻³.",
        "5. Intrinsic Ratio Evaluation: n_i surged by a factor of (3.364 × 10¹²) / (1.50 × 10¹⁰) = 224.3 times!",
        "6. Minority Hole Density Surge: p = n_i² / N_D. At 25°C: p = (1.5 × 10¹⁰)² / 10¹⁶ = 2.25 × 10⁴ cm⁻³. At 125°C: p = (3.364 × 10¹²)² / 10¹⁶ = 1.132 × 10⁹ cm⁻³ (surged by 50,300 times!).",
        "7. Reverse Leakage Current Impact: Reverse saturation current I_S is directly proportional to n_i². If I_S(25°C) = 2.0 nA, then at 125°C: I_S(125°C) = 2.0 nA × 50,300 = 100.6 μA. Under 600V reverse bus voltage, continuous leakage dissipation = 600V × 100.6 μA = 60.4 mW. Without heat sinking, this localized leakage initiates destructive thermal runaway."
    ]
    story.append(create_example(7, "High-Temperature Intrinsic Carrier Surge & Thermal Leakage in Dodoma Solar Inverters",
                                "In semi-arid Dodoma, solar pump inverter diodes operate at junction temperatures reaching 125°C. Given silicon donor doping N_D = 1.0 × 10¹⁶ cm⁻³ and bandgap E_g = 1.12 eV, calculate the intrinsic concentration n_i at 125°C, determine the percentage surge over room temperature (25°C), and compute the increase in minority carrier leakage current.",
                                ex7_steps))

    # Worked Example 8
    ex8_steps = [
        "1. Problem Definition: An autonomous drone crop sprayer utilizes high-speed freewheeling silicon diodes in its 48V brushless DC motor ESCs. The P-side has hole diffusion coefficient D_p = 12.0 cm²/s and minority carrier lifetime τ_p = 0.25 μs = 2.5 × 10⁻⁷ s.",
        "2. Diffusion Length Formula: L_p = √( D_p · τ_p ).",
        "3. Calculate Hole Diffusion Length: L_p = √[ 12.0 cm²/s × (2.5 × 10⁻⁷ s) ] = √[ 3.0 × 10⁻⁶ cm² ] = 1.732 × 10⁻³ cm = 17.32 μm.",
        "4. Physical Significance: 17.32 μm is the average distance an injected minority hole travels through the N-region before recombining with an electron.",
        "5. Transit Time Across Base: For an N-base width W_base = 25 μm, since W_base > L_p, substantial minority charge storage occurs.",
        "6. Reverse Recovery Time (t_rr): When the BLDC motor phases switch, stored minority charge Q_rr = I_F · τ_p must be swept out before the diode blocks. For forward current I_F = 8.0 A: Q_rr = 8.0 A × (2.5 × 10⁻⁷ s) = 2.0 μC.",
        "   Under reverse current ramp di/dt = 100 A/μs: t_rr = √[ 2 · Q_rr / (di/dt) ] = √[ 2 × 2.0 × 10⁻⁶ C / (100 × 10⁶ A/s) ] = √[ 4.0 × 10⁻¹⁴ s² ] = 2.0 × 10⁻⁷ s = 200 ns.",
        "7. ESC Switching Loss: At 40 kHz motor PWM frequency, switching power loss P_rr = 0.5 · V_bus · I_peak · t_rr · f_sw = 0.5 × 48V × 20A × 200 ns × 40,000 Hz = 3.84 W per diode (requiring Schottky upgrades for drone flight endurance)."
    ]
    story.append(create_example(8, "Minority Carrier Diffusion Length & Reverse Recovery Dynamics in Drone ESC Diodes",
                                "A high-speed freewheeling diode in an agricultural spray drone motor driver has hole diffusion coefficient D_p = 12.0 cm²/s and lifetime τ_p = 0.25 μs. Calculate the hole diffusion length L_p, determine the stored minority charge at 8.0 A forward current, and compute the reverse recovery time t_rr and switching power dissipation under 40 kHz motor PWM switching.",
                                ex8_steps))

    # Analytical Theory: Derivation of Built-in Potential & Poisson Electrostatics
    story.append(Paragraph("2.6.3 Rigorous Analytical Derivation of Built-In Potential from Drift-Diffusion Balance", styles['SecH2']))
    story.append(Paragraph(
        "Under true thermal equilibrium with zero externally applied voltage, the net hole current across the PN junction must equal zero identically. "
        "The hole current density is the sum of field-driven drift and concentration gradient-driven diffusion:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>J<sub>p</sub>(x) = q · p(x) · μ<sub>p</sub> · E(x) - q · D<sub>p</sub> · [ dp(x) / dx ] = 0</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "Rearranging to express the built-in electric field <i>E</i>(<i>x</i>) as a function of the hole concentration gradient yields:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>E(x) = [ D<sub>p</sub> / μ<sub>p</sub> ] · [ 1 / p(x) ] · [ dp(x) / dx ] = V<sub>T</sub> · [ 1 / p(x) ] · [ dp(x) / dx ]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "where <i>V</i><sub>T</sub> = <i>D</i><sub>p</sub> / <i>μ</i><sub>p</sub> = (<i>k</i><sub>B</sub><i>T</i>) / <i>q</i> is the thermal voltage. "
        "The total electrostatic potential difference between the neutral N-region (<i>x</i> = +<i>x</i><sub>n</sub>) and neutral P-region (<i>x</i> = -<i>x</i><sub>p</sub>) "
        "is obtained by integrating the electric field across the space-charge depletion zone:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>V₀ = - ∫<sub>-x<sub>p</sub></sub><sup>x<sub>n</sub></sup> E(x) dx = - V<sub>T</sub> · ∫<sub>p<sub>p</sub></sub><sup>p<sub>n</sub></sup> [ dp / p ] = V<sub>T</sub> · ln[ p<sub>p</sub> / p<sub>n</sub> ]</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "In the neutral P-region, majority hole concentration is <i>p</i><sub>p</sub> ≈ <i>N</i><sub>A</sub>. "
        "In the neutral N-region, minority hole concentration is dictated by the Law of Mass Action: <i>p</i><sub>n</sub> = <i>n</i><sub>i</sub><sup>2</sup> / <i>N</i><sub>D</sub>. "
        "Substituting these expressions yields the celebrated governing equation for the built-in contact potential:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>V₀ = V<sub>T</sub> · ln[ (N<sub>A</sub> · N<sub>D</sub>) / n<sub>i</sub><sup>2</sup> ] &nbsp;&nbsp;[Volts]</b>", styles['FormulaBox']))

    story.append(Paragraph("2.6.4 Space-Charge Distribution and Poisson Electrostatics", styles['SecH2']))
    story.append(Paragraph(
        "Inside the depletion layer, all mobile carriers have diffused away, leaving uncompensated static ionized dopants. "
        "The space-charge density <i>ρ</i>(<i>x</i>) is modeled as a step function (the depletion approximation):<br/>"
        "&nbsp;&nbsp;&bull; For -<i>x</i><sub>p</sub> ≤ <i>x</i> &lt; 0 (P-side depletion): <b>ρ(x) = - q · N<sub>A</sub></b> (negative acceptor ions)<br/>"
        "&nbsp;&nbsp;&bull; For 0 &lt; <i>x</i> ≤ <i>x</i><sub>n</sub> (N-side depletion): <b>ρ(x) = + q · N<sub>D</sub></b> (positive donor ions)<br/>"
        "Total charge neutrality dictates that <b>q · N<sub>A</sub> · x<sub>p</sub> · A = q · N<sub>D</sub> · x<sub>n</sub> · A &implies; N<sub>A</sub> · x<sub>p</sub> = N<sub>D</sub> · x<sub>n</sub></b>. "
        "Hence, the depletion layer penetrates more deeply into the lightly doped side of the junction.<br/>"
        "Poisson's 1-D electrostatic equation connects electric field gradient to charge density: <b>dE(x)/dx = ρ(x) / ε<sub>s</sub></b>. "
        "Integrating from -<i>x</i><sub>p</sub> to 0 gives the electric field on the P-side, and from 0 to <i>x</i><sub>n</sub> on the N-side. "
        "The maximum electric field occurs precisely at the metallurgical junction (<i>x</i> = 0):",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>E<sub>max</sub> = - (q · N<sub>A</sub> · x<sub>p</sub>) / ε<sub>s</sub> = - (q · N<sub>D</sub> · x<sub>n</sub>) / ε<sub>s</sub> = - [ 2 · (V₀ + V<sub>R</sub>) ] / W</b>", styles['FormulaBox']))
    story.append(Paragraph(
        "A second integration gives the parabolic potential profile <i>V</i>(<i>x</i>) across the depletion zone. "
        "Equating the total potential difference to (<i>V</i><sub>0</sub> + <i>V</i><sub>R</sub>) yields the complete formula for total depletion width:",
        styles['DocBody']
    ))
    story.append(Paragraph("<b>W = x<sub>n</sub> + x<sub>p</sub> = √[ (2 · ε<sub>s</sub> · (V₀ + V<sub>R</sub>) / q) · ( (N<sub>A</sub> + N<sub>D</sub>) / (N<sub>A</sub> · N<sub>D</sub>) ) ]</b>", styles['FormulaBox']))

    # Worked Example 9
    ex9_steps = [
        "1. Problem Definition: A precision turbine fertigation flowmeter installed in an automated sugarcane drip irrigation header in Kilombero uses a multi-pole ring magnet on its rotor. The ring has 8 magnetic pole pairs (16 alternating poles). Flow rate Q ranges from 5.0 m³/h to 50.0 m³/h. The turbine rotor rotates at k_rot = 18.5 RPM per m³/h of flow.",
        "2. Compute Rotor Speed Range:",
        "   At Q_min = 5.0 m³/h: N_min = 18.5 × 5.0 = 92.5 RPM (1.542 rev/s).",
        "   At Q_max = 50.0 m³/h: N_max = 18.5 × 50.0 = 925.0 RPM (15.417 rev/s).",
        "3. Hall Switch Pulse Generation: With 8 pole pairs, the digital Hall switch triggers 8 complete HIGH-LOW pulses per mechanical revolution.",
        "4. Calculate Output Frequency Range:",
        "   f_min = 1.542 rev/s × 8 pulses/rev = 12.33 Hz.",
        "   f_max = 15.417 rev/s × 8 pulses/rev = 123.33 Hz.",
        "5. Flowmeter Meter Factor (K-Factor):",
        "   K = f / Q = (123.33 pulses/s) / (50.0 m³/h / 3600 s/h) = 123.33 / 0.01389 m³/s = 8,880 pulses per m³ (or 8.88 pulses per liter).",
        "6. Microcontroller Pulse Accumulation: The irrigation node uses an ESP32 hardware pulse counter (PCNT) module. For a 10-minute fertigation dose at 30 m³/h: Total volume V = 30 m³/h × (10/60 h) = 5.0 m³ = 5,000 liters. Total pulses recorded = 5,000 L × 8.88 pulses/L = 44,400 pulses.",
        "7. Diagnostic Error Detection: If pulse frequency abruptly drops to zero while the main booster pump relay is energized, the microcontroller flags a 'Pipe Burst / Pump Cavitation Fault' and halts acid injection within 250 ms, preventing soil acidification and fertilizer loss."
    ]
    story.append(create_example(9, "Hall-Effect Turbine Flowmeter Calibration for Sugarcane Fertigation in Kilombero",
                                "An automated drip fertigation header in Kilombero measures liquid fertilizer flow with a turbine meter equipped with an 8-pole-pair magnetic ring and a digital Hall switch. Given a rotor constant of 18.5 RPM per m³/h, determine the pulse output frequency across 5.0 to 50.0 m³/h, calculate the flowmeter K-factor in pulses per liter, and evaluate the pulse count for a 5,000-liter fertigation cycle.",
                                ex9_steps))

    # Worked Example 10
    ex10_steps = [
        "1. Problem Definition: An agronomic LoRa wireless soil moisture sensor node operating in the Dodoma vineyard belt uses a varactor diode (1SV149) in an LC voltage-controlled oscillator (VCO) to tune carrier transmission frequency across the 433 MHz ISM band (f_1 = 433.05 MHz to f_2 = 434.79 MHz).",
        "2. Governing Resonant Tank Formula: f_0 = 1 / [ 2 · π · √( L · C_total ) ].",
        "3. Fixed Inductor Selection: An RF surface-mount inductor L = 12.0 nH = 1.20 × 10⁻⁸ H is selected.",
        "4. Calculate Required Total Capacitance at Band Center (f = 433.92 MHz):",
        "   C_total = 1 / [ 4 · π² · f_0² · L ] = 1 / [ 4 · π² · (433.92 × 10⁶)² · (1.20 × 10⁻⁸) ] = 1 / [ 39.478 × 1.8829 × 10¹⁷ × 1.20 × 10⁻⁸ ] = 1 / 8.920 × 10¹⁰ = 1.121 × 10⁻¹¹ F = 11.21 pF.",
        "5. Calculate Required Capacitance Range:",
        "   At f_high = 434.79 MHz: C_min = 1 / [ 4 · π² · (434.79 × 10⁶)² · (1.20 × 10⁻⁸) ] = 11.16 pF.",
        "   At f_low = 433.05 MHz: C_max = 1 / [ 4 · π² · (433.05 × 10⁶)² · (1.20 × 10⁻⁸) ] = 11.25 pF.",
        "6. Required Varactor Capacitance Tuning: Accounting for fixed circuit board stray capacitance C_stray = 2.50 pF, the varactor junction capacitance must adjust from C_j_min = 11.16 - 2.50 = 8.66 pF to C_j_max = 11.25 - 2.50 = 8.75 pF.",
        "7. Varactor Bias Voltage Tuning: The varactor follows C_j(V_R) = C_j0 / √( 1 + V_R / V_0 ) where C_j0 = 22.0 pF and V_0 = 0.75 V.",
        "   Solving for V_R: (C_j0 / C_j)² = 1 + V_R / V_0  &implies;  V_R = V_0 · [ (C_j0 / C_j)² - 1 ].",
        "   For C_j = 8.75 pF: V_R = 0.75 · [ (22.0 / 8.75)² - 1 ] = 0.75 · [ 6.322 - 1 ] = 0.75 · 5.322 = 3.99 V.",
        "   For C_j = 8.66 pF: V_R = 0.75 · [ (22.0 / 8.66)² - 1 ] = 0.75 · [ 6.454 - 1 ] = 0.75 · 5.454 = 4.09 V.",
        "8. Conclusion: A precision DAC tuning voltage from 3.99V to 4.09V precisely steers the telemetry transmission frequency, preventing RF cross-channel interference between neighboring vineyard sensor clusters."
    ]
    story.append(create_example(10, "Varactor Diode Frequency Tuning for Agronomic Telemetry in Dodoma Vineyards",
                                "An agronomic LoRa wireless node operating in the 433 MHz band utilizes a varactor diode in an LC tank oscillator with L = 12.0 nH and stray capacitance C_stray = 2.50 pF. Determine the total capacitance required for resonance at 433.05 MHz and 434.79 MHz, calculate the required varactor junction capacitance range, and compute the necessary DC reverse bias tuning voltages for a varactor with C_j0 = 22.0 pF and V_0 = 0.75 V.",
                                ex10_steps))

    # -------------------------------------------------------------
    # SECTION 8: LABORATORY BENCH PROTOCOL
    # -------------------------------------------------------------
    story.append(Paragraph("2.8 Practical Laboratory Bench Protocol: PN Barrier Potential & Temperature Drift", styles['SecH1']))
    story.append(Paragraph(
        "This laboratory exercise in the Electronics & Precision Agriculture Lab (EPAL) guides students through experimentally measuring "
        "the forward barrier knee voltage of Silicon and Germanium diodes, extracting dynamic resistance, and observing the negative temperature "
        "coefficient of forward voltage (<i>dV_F / dT ≈ -2.0 mV/°C</i>).",
        styles['DocBody']
    ))

    lab2_headers = ["Step #", "Bench Action / Experimental Procedure", "Required Instrumentation", "Expected Technical Observation"]
    lab2_rows = [
        ["1", "Circuit Setup: Wire a 1N4007 (Silicon) and 1N34A (Germanium) diode in series with a 1.0 kΩ current-limiting resistor.", "Breadboard, 1N4007, 1N34A, 1kΩ resistor", "Ensure correct cathode silver band orientation toward ground."],
        ["2", "Forward Voltage Sweeping: Vary DC power supply voltage from 0V to 5.0V in 0.2V increments. Measure V_D and circuit current I_D.", "Variable DC Power Supply, Fluke DMMs", "Observe negligible current until knee voltage (0.6V for Si, 0.25V for Ge), followed by rapid exponential rise."],
        ["3", "I-V Plotting: Plot I_D vs V_D on linear and semi-log graph paper. Extract knee voltage V_K and reverse saturation current I_S.", "Graph plotting software / Python", "Silicon knee V_K ≈ 0.68V; Germanium knee V_K ≈ 0.28V. Germanium shows higher reverse leakage."],
        ["4", "Thermal Drift Measurement: Submerge diode in an insulated water bath. Heat water from 25°C to 75°C using immersion heater.", "Calibrated Thermocouple, Hot plate", "Monitor V_F while maintaining a constant forward bias current I_D = 2.0 mA."],
        ["5", "TCR Extraction: Compute temperature sensitivity: ΔV_F / ΔT.", "DMM (0.1 mV resolution)", "Verify that forward voltage decreases by approximately -1.9 to -2.2 mV/°C for Silicon."],
        ["6", "Hall Sensor Demo: Pass an N52 neodymium magnet over an A3144 Hall-effect switch IC. Observe logic state transitions on oscilloscope.", "A3144 Hall IC, Neodymium magnet, DSO", "Observe clean digital 0V to 5V square-wave pulses with zero contact bounce."]
    ]
    story.append(create_custom_table(lab2_headers, lab2_rows, [0.8*inch, 2.4*inch, 1.8*inch, 2.2*inch]))

    # -------------------------------------------------------------
    # SECTION 9: TANZANIAN AGRICULTURAL CASE STUDIES
    # -------------------------------------------------------------
    story.append(Paragraph("2.9 Tanzanian Agricultural Engineering Field Case Studies", styles['SecH1']))
    story.append(Paragraph(
        "<b>Case Study 1: Solar Pyranometer Calibration at SUA Crop Museum</b><br/>"
        "Precision irrigation scheduling requires continuous measurement of solar irradiance (W/m²) to compute reference crop evapotranspiration (<i>ET_o</i>) "
        "via the FAO Penman-Monteith equation. Solid-state pyranometers utilize precision monocrystalline silicon photodiode junctions operating in short-circuit "
        "photovoltaic mode. Incident photons generate electron-hole pairs inside the depletion layer at a rate directly proportional to solar flux. "
        "Because the silicon bandgap (1.12 eV) matches solar spectral irradiance from 350 nm to 1,100 nm, calibration stability across Morogoro's sunny and cloudy seasons "
        "enables automated drip-irrigation controllers to match crop water demand with zero wastage.",
        styles['DocBody']
    ))
    story.append(Paragraph(
        "<b>Case Study 2: Tractor Alternator Rectification Failures in Tabora Cotton Fields</b><br/>"
        "In Tabora, agricultural tractors clearing cotton fields operate amidst dense fine dust and ambient temperatures exceeding 38°C. "
        "The three-phase tractor alternator utilizes six press-fit silicon PN junction diodes to rectify 14V AC into 12V DC battery charging current. "
        "Because reverse saturation current doubles for every 10°C rise in junction temperature (<i>I_S(T) = I_S(25°C) · 2^[(T-25)/10]</i>), "
        "accumulated cotton lint blocking alternator cooling vents drove diode junction temperatures above 150°C. "
        "The resulting thermal runaway caused reverse breakdown and melted diode junctions. Installing heavy-duty alternator diodes with lower thermal resistance "
        "and implementing daily compressed-air blowdown protocols eliminated seasonal charging failures.",
        styles['DocBody']
    ))

    # -------------------------------------------------------------
    # SECTION 10: REVIEW QUESTIONS & PROBLEMS
    # -------------------------------------------------------------
    story.append(Paragraph("2.10 Comprehensive Self-Assessment & Review Questions", styles['SecH1']))
    story.append(Paragraph("<b>PART A: Conceptual & Theoretical Questions</b>", styles['SecH2']))
    q_part_a = [
        "1. State Bohr's postulates of atomic structure and explain why electron orbital energy is quantized and negative.",
        "2. Explain the Pauli Exclusion Principle and describe how it causes discrete atomic energy levels to split into continuous energy bands in solid crystals.",
        "3. Differentiate between intrinsic and extrinsic semiconductors in terms of crystal purity, carrier generation, and temperature dependence of conductivity.",
        "4. Why does an N-type semiconductor remain electrically neutral as a whole despite having a high concentration of free mobile electrons?",
        "5. State the Law of Mass Action (n · p = n_i²) and explain its physical basis in terms of thermal generation and recombination rates.",
        "6. Describe the physical mechanism governing the formation of the space-charge depletion layer in an open-circuit PN junction.",
        "7. Derive the Built-In Barrier Potential equation V₀ = V_T · ln[(N_A · N_D) / n_i²] starting from the equilibrium drift-diffusion balance condition.",
        "8. Explain why a digital multimeter connected across the terminals of an isolated, open-circuit PN diode reads 0.0V instead of the built-in barrier potential V₀ (0.7V).",
        "9. What is the Hall Effect? Derive the equation for Hall voltage V_H and explain how it is used to measure magnetic fields and determine semiconductor carrier type.",
        "10. Why does the forward voltage of a silicon diode decrease with rising temperature (dV_F / dT ≈ -2.0 mV/°C)?"
    ]
    for q in q_part_a:
        story.append(Paragraph(q, styles['DocBullet']))

    story.append(Paragraph("<b>PART B: Quantitative Analytical Problems</b>", styles['SecH2']))
    q_part_b = [
        "11. A silicon sample at 300K is doped with Phosphorus at N_D = 4.0 × 10¹⁶ cm⁻³ and Boron at N_A = 1.0 × 10¹⁶ cm⁻³ (compensated semiconductor). (a) State whether the material is N-type or P-type. (b) Calculate the majority and minority carrier concentrations. (c) Compute electrical conductivity σ (given μ_n = 1,200 cm²/V·s, μ_p = 400 cm²/V·s).",
        "12. Calculate the built-in potential V₀ of a silicon PN junction at: (a) T = 300 K (V_T = 25.86 mV, n_i = 1.5 × 10¹⁰ cm⁻³) and (b) T = 373 K (100°C, where n_i increases to 1.3 × 10¹² cm⁻³ and V_T = 32.14 mV). Doping levels: N_A = 5.0 × 10¹⁶ cm⁻³, N_D = 2.0 × 10¹⁶ cm⁻³.",
        "13. An abrupt silicon PN junction diode has N_A = 2.0 × 10¹⁷ cm⁻³ and N_D = 1.0 × 10¹⁶ cm⁻³. Calculate: (a) The built-in potential V₀ at 300K, (b) The total depletion layer width W under zero bias, (c) The depletion width under a reverse bias of V_R = 10 V, and (d) The maximum electric field E_max under 10V reverse bias.",
        "14. A Hall-effect sensor on an automated tractor steering axle uses a P-type silicon slab with thickness t = 0.20 mm, hole concentration p = 5.0 × 10¹⁵ cm⁻³, and bias current I_x = 15 mA. When subjected to a magnetic field B_z = 0.35 Tesla: (a) Calculate the Hall coefficient R_H. (b) Compute the generated Hall voltage V_H. (c) What is the polarity of V_H on the top face?",
        "15. A reverse-biased silicon diode has a reverse saturation current I_S = 1.5 nA at 25°C. Assuming I_S doubles for every 10°C rise in temperature, calculate the reverse leakage current when operated inside an enclosed tractor engine bay at 85°C."
    ]
    for q in q_part_b:
        story.append(Paragraph(q, styles['DocBullet']))

    story.append(Paragraph("<b>PART C: Agricultural Systems Design Challenges</b>", styles['SecH2']))
    q_part_c = [
        "16. <b>Precision Seed Drill Optical Counter:</b> Design an optical seed-drop detection channel using an infrared GaAs LED (λ = 940 nm) and a silicon PIN photodiode. Calculate the photon energy in eV, verify that it exceeds the silicon bandgap (1.12 eV), and calculate the required transimpedance amplifier feedback resistor to convert a 20 μA seed-drop photocurrent pulse into a 2.0V logic signal.",
        "17. <b>Tractor Engine Temperature Sensor Design:</b> Using the temperature coefficient of forward voltage (dV_F / dT = -2.0 mV/°C at constant 1.0 mA bias), design an analog engine coolant temperature monitoring circuit using a 1N4148 silicon diode. Calculate the output voltage span as coolant temperature rises from 20°C to 110°C.",
        "18. <b>Kilombero Cane Harvester Wheel Slip Monitor:</b> Design a dual Hall-effect sensor wheel slip measurement system. A 60-tooth gear wheel on the tractor drive axle rotates at 120 RPM under zero slip. Determine the pulse frequency output and calculate the detected frequency when wheel slip reaches 20% in muddy soil."
    ]
    for q in q_part_c:
        story.append(Paragraph(q, styles['DocBullet']))

    # -------------------------------------------------------------
    # SECTION 10: GOVERNING SCIENTIFIC FORMULAS & ANALYTICAL LAWS
    # -------------------------------------------------------------
    story.append(Spacer(1, 8))
    story.append(Paragraph("2.10 Comprehensive Scientific Formula & Analytical Synthesis", styles['SecH1']))
    story.append(Paragraph(
        "The following analytical formulation synthesizes all governing mathematical models and constitutive solid-state relationships "
        "established in this compendium for semiconductor physics, charge transport kinetics, and PN junction electrostatics:",
        styles['DocBody']
    ))

    lec2_formulas = [
        ["Bandgap Energy & Photons", "<i>E</i><sub>g</sub> = <i>h</i> · <i>f</i> = (<i>h</i> · <i>c</i>) / <i>λ</i>", "Defines minimum photon energy for optical electron-hole generation in crop NDVI sensors and solar cells."],
        ["Law of Mass Action", "<i>n</i> · <i>p</i> = <i>n</i><sub>i</sub><sup>2</sup>(<i>T</i>)", "Fundamental thermal equilibrium carrier product across intrinsic and extrinsic semiconductors."],
        ["Intrinsic Carrier Density", "<i>n</i><sub>i</sub>(<i>T</i>) = <i>B</i> · <i>T</i><sup>3/2</sup> · <i>e</i><sup>-<i>E</i><sub>g</sub> / (2<i>k</i><sub>B</sub><i>T</i>)</sup>", "Exponential thermal generation of carriers responsible for high-temperature sensor drift in tropical soils."],
        ["Electrical Conductivity", "<i>σ</i> = <i>q</i> · ( <i>n</i> · <i>μ</i><sub>n</sub> + <i>p</i> · <i>μ</i><sub>p</sub> )<br/><i>ρ</i> = 1 / <i>σ</i>", "Governs bulk semiconductor resistivity and ohmic contact design for agricultural transducers."],
        ["Einstein Relation", "<i>D</i><sub>n</sub> / <i>μ</i><sub>n</sub> = <i>D</i><sub>p</sub> / <i>μ</i><sub>p</sub> = <i>V</i><sub>T</sub> = (<i>k</i><sub>B</sub><i>T</i>) / <i>q</i>", "Connects thermal carrier diffusion constants with electric field mobility at thermal voltage <i>V</i><sub>T</sub> ≈ 26 mV."],
        ["Total Carrier Transport", "<i>J</i><sub>total</sub> = <i>J</i><sub>drift</sub> + <i>J</i><sub>diff</sub>", "Superposition of field-driven drift current and concentration gradient-driven diffusion current."],
        ["Built-in Barrier Potential", "<i>V</i><sub>0</sub> = <i>V</i><sub>T</sub> · ln[ (<i>N</i><sub>A</sub> · <i>N</i><sub>D</sub>) / <i>n</i><sub>i</sub><sup>2</sup> ]", "Internal electrostatic contact barrier voltage across PN metallurgical junction (≈ 0.7V for Silicon at 300K)."],
        ["Depletion Region Width", "<i>W</i> = √[ 2<i>ε</i><sub>s</sub> (<i>V</i><sub>0</sub> + <i>V</i><sub>R</sub>) / <i>q</i> · (1/<i>N</i><sub>A</sub> + 1/<i>N</i><sub>D</sub>) ]", "Space charge depletion layer thickness under thermal equilibrium and reverse bias <i>V</i><sub>R</sub>."],
        ["Peak Junction Electric Field", "<i>E</i><sub>max</sub> = [ 2 · (<i>V</i><sub>0</sub> + <i>V</i><sub>R</sub>) ] / <i>W</i>", "Maximum internal electric field located at metallurgical interface; governs avalanche breakdown."],
        ["Junction Depletion Capacitance", "<i>C</i><sub>j</sub> = (<i>ε</i><sub>s</sub> · <i>A</i>) / <i>W</i>", "Voltage-dependent junction capacitance governing varactor tuning and diode high-frequency limits."],
        ["Hall Effect Voltage", "<i>V</i><sub>H</sub> = (<i>I</i><sub>x</sub> · <i>B</i><sub>z</sub>) / (<i>n</i> · <i>q</i> · <i>t</i>) = <i>R</i><sub>H</sub> · (<i>I</i><sub>x</sub> · <i>B</i><sub>z</sub>) / <i>t</i>", "Transverse Lorentz force potential for non-contact tractor wheel speed and shaft rotation sensing."],
        ["Hall Coefficient", "<i>R</i><sub>H</sub> = 1 / (<i>n</i> · <i>q</i>) &nbsp;[m<sup>3</sup>/C]", "Fundamental material parameter identifying majority carrier polarity (negative for electrons, positive for holes)."]
    ]
    story.append(create_formula_summary_table(lec2_formulas))

    render_pdf("AEN_214_Lecture_2_Compendium.pdf", story)

if __name__ == "__main__":
    build_lecture_2()

