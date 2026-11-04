#!/usr/bin/env python3
"""
generate_figures.py
Generates high-resolution schematic diagrams, scientific plots, and downloads
real-world open hardware images for AEN 214 Introduction to Electronics.
Stored in the Figures/ directory.
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as logic
import requests

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Figures"))
os.makedirs(FIGURES_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.0

# -------------------------------------------------------------
# CRAWL / DOWNLOAD AUTHENTIC OPEN HARDWARE IMAGES VIA WIKIPEDIA API
# -------------------------------------------------------------
def crawl_hardware_images():
    """Fetches high-quality open-access component images from Wikipedia Commons API."""
    headers = {'User-Agent': 'AEN214ElectronicsCourseNotes/1.0 (contact: info@sua.ac.tz)'}
    components = {
        "fig_real_resistors.png": "Resistor",
        "fig_real_capacitors.png": "Capacitor",
        "fig_real_diodes.png": "Diode",
        "fig_real_bjt.png": "Bipolar_junction_transistor",
        "fig_real_mosfet.png": "MOSFET",
        "fig_real_breadboard.png": "Breadboard"
    }
    for filename, title in components.items():
        filepath = os.path.join(FIGURES_DIR, filename)
        if not os.path.exists(filepath):
            try:
                api = f'https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=600'
                res = requests.get(api, headers=headers, timeout=10).json()
                pages = res.get('query', {}).get('pages', {})
                for p in pages.values():
                    thumb = p.get('thumbnail')
                    if thumb and 'source' in thumb:
                        img_data = requests.get(thumb['source'], headers=headers, timeout=15)
                        if img_data.status_code == 200:
                            with open(filepath, 'wb') as f:
                                f.write(img_data.content)
                            print(f"[Crawled] Downloaded {filename} ({len(img_data.content)} bytes)")
            except Exception as e:
                print(f"[Crawl notice] Could not fetch {title}: {e}")

# -------------------------------------------------------------
# LECTURE 1 FIGURES: PASSIVE COMPONENTS
# -------------------------------------------------------------
def generate_lecture_1_figures():
    # 1.1 Resistor Color Code Guide
    fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    res_body = patches.FancyBboxPatch((2, 1.8), 6, 1.4, boxstyle="round,pad=0.2", fc="#d2b48c", ec="#5c4033", lw=2)
    ax.add_patch(res_body)
    ax.plot([0.5, 2], [2.5, 2.5], color='#7f8c8d', lw=5)
    ax.plot([8, 9.5], [2.5, 2.5], color='#7f8c8d', lw=5)
    
    ax.add_patch(patches.Rectangle((3.0, 1.6), 0.4, 1.8, fc="#8B4513", ec="none"))
    ax.add_patch(patches.Rectangle((4.2, 1.6), 0.4, 1.8, fc="#000000", ec="none"))
    ax.add_patch(patches.Rectangle((5.4, 1.6), 0.4, 1.8, fc="#FF0000", ec="none"))
    ax.add_patch(patches.Rectangle((7.0, 1.6), 0.4, 1.8, fc="#CFB53B", ec="none"))
    
    ax.text(3.2, 3.8, '1st Digit\nBrown = 1', ha='center', fontsize=9, fontweight='bold')
    ax.text(4.4, 0.8, '2nd Digit\nBlack = 0', ha='center', fontsize=9, fontweight='bold')
    ax.text(5.6, 3.8, 'Multiplier\nRed = 10²', ha='center', fontsize=9, fontweight='bold')
    ax.text(7.2, 0.8, 'Tolerance\nGold = ±5%', ha='center', fontsize=9, fontweight='bold')
    
    ax.set_title("Standard 4-Band Resistor Color Code: 1.0 kΩ ±5%", fontsize=11, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig1_1_resistor_color_code.png"))
    plt.close()

    # 1.2 RC Charging and Discharging
    t = np.linspace(0, 5, 200)
    v_charge = 1 - np.exp(-t)
    v_discharge = np.exp(-t)
    
    fig, ax = plt.subplots(figsize=(7, 3.8), dpi=300)
    ax.plot(t, v_charge, label=r'Charging: $v_C(t) = V_s(1 - e^{-t/\tau})$', color='#1f77b4', lw=2.2)
    ax.plot(t, v_discharge, label=r'Discharging: $v_C(t) = V_0 e^{-t/\tau}$', color='#d62728', lw=2.2, linestyle='--')
    ax.axvline(1, color='gray', linestyle=':', lw=1.2)
    ax.axhline(0.632, color='gray', linestyle=':', lw=1.2)
    ax.axhline(0.368, color='gray', linestyle=':', lw=1.2)
    ax.scatter([1, 1], [0.632, 0.368], color=['#1f77b4', '#d62728'], zorder=5)
    ax.text(1.1, 0.63, r'$t = \tau (63.2\%)$', color='#1f77b4', fontweight='bold')
    ax.text(1.1, 0.36, r'$t = \tau (36.8\%)$', color='#d62728', fontweight='bold')
    ax.set_xlabel(r'Time in Time Constants ($t/\tau$, $\tau = RC$)', fontsize=10)
    ax.set_ylabel(r'Normalized Voltage ($v_C / V_s$)', fontsize=10)
    ax.set_title('Capacitor Transient Response: Charging & Discharging', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(frameon=True, loc='center right')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig1_2_rc_transient.png"))
    plt.close()

    # 1.3 Reactance vs Frequency
    f = np.logspace(1, 6, 300)
    C = 10e-6
    L = 10e-3
    Xc = 1 / (2 * np.pi * f * C)
    Xl = 2 * np.pi * f * L
    f0 = 1 / (2 * np.pi * np.sqrt(L * C))
    
    fig, ax = plt.subplots(figsize=(7, 3.8), dpi=300)
    ax.loglog(f, Xc, label=r'Capacitive Reactance $X_C = \frac{1}{2\pi f C}$', color='#e67e22', lw=2.2)
    ax.loglog(f, Xl, label=r'Inductive Reactance $X_L = 2\pi f L$', color='#2980b9', lw=2.2)
    ax.axvline(f0, color='darkgreen', linestyle='--', lw=1.5, label=f'Resonant freq $f_0 \\approx {f0:.1f}$ Hz')
    ax.set_xlabel('Frequency (Hz)', fontsize=10)
    ax.set_ylabel(r'Reactance ($\Omega$)', fontsize=10)
    ax.set_title('Variation of Reactance with Frequency', fontsize=11, fontweight='bold')
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig1_3_reactance_curves.png"))
    plt.close()

    # 1.4 Schemdraw Low-Pass Filter
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=11)
        d += elm.SourceSin().label('$V_{in}(t)$', loc='left')
        d += elm.Resistor().right().label('$R$', loc='top')
        d += elm.Dot()
        d.push()
        d += elm.Capacitor().down().label('$C$', loc='right')
        d += elm.Line().left()
        d.pop()
        d += elm.Line().right().length(2)
        d += elm.Dot(open=True).label('$V_{out}(t)$', loc='right')
        d.save(os.path.join(FIGURES_DIR, "fig1_4_passive_filter_schematic.png"))
    print("[Gen] Lecture 1 figures ready.")

# -------------------------------------------------------------
# LECTURE 2 FIGURES: SEMICONDUCTOR PHYSICS
# -------------------------------------------------------------
def generate_lecture_2_figures():
    # 2.1 Bohr Silicon Atom Model
    fig, ax = plt.subplots(figsize=(5.5, 5.5), dpi=300)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.add_patch(patches.Circle((0, 0), 0.8, color='#e74c3c', zorder=5))
    ax.text(0, 0, '+14\nSi Nucleus', color='white', ha='center', va='center', fontweight='bold', fontsize=8.5)
    
    radii = [1.5, 2.5, 3.5]
    electrons_per_shell = [2, 8, 4]
    shell_labels = ['K: 2e⁻', 'L: 8e⁻', 'M: 4 Valence e⁻']
    colors = ['#3498db', '#2ecc71', '#f39c12']
    
    for r, n_e, lbl, col in zip(radii, electrons_per_shell, shell_labels, colors):
        circle = patches.Circle((0, 0), r, fill=False, color='gray', linestyle='--', lw=1.2)
        ax.add_patch(circle)
        angles = np.linspace(0, 2*np.pi, n_e, endpoint=False)
        for ang in angles:
            ex = r * np.cos(ang)
            ey = r * np.sin(ang)
            ax.add_patch(patches.Circle((ex, ey), 0.12, color=col, zorder=6))
            
    ax.text(0, 3.75, 'Outer Shell: 4 Valence Electrons (Group IV)', ha='center', fontsize=9.5, fontweight='bold', color='#d35400')
    ax.set_title("Bohr Atomic Model of Silicon (Z = 14)", fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig2_1_bohr_atom_silicon.png"))
    plt.close()

    # 2.2 Energy Band Comparison
    fig, axes = plt.subplots(1, 3, figsize=(10, 4.2), dpi=300)
    types = ['Insulator (Glass, Diamond)', 'Semiconductor (Si, Ge)', 'Conductor (Copper, Al)']
    
    for i, ax in enumerate(axes):
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 7)
        ax.set_title(types[i], fontsize=9, fontweight='bold')
        ax.axis('off')
        
        vb_y = 1.0
        vb_h = 1.5
        ax.add_patch(patches.Rectangle((0.5, vb_y), 3.0, vb_h, fc='#34495e', ec='black'))
        ax.text(2.0, vb_y + vb_h/2, 'Valence Band\n(Filled)', color='white', ha='center', va='center', fontweight='bold', fontsize=8)
        
        if i == 0:
            cb_y = 5.0
            cb_h = 1.5
            ax.add_patch(patches.Rectangle((0.5, cb_y), 3.0, cb_h, fc='#95a5a6', ec='black'))
            ax.text(2.0, cb_y + cb_h/2, 'Conduction Band\n(Empty)', color='white', ha='center', va='center', fontweight='bold', fontsize=8)
            ax.annotate('', xy=(3.7, cb_y), xytext=(3.7, vb_y + vb_h), arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
            ax.text(3.7, (cb_y + vb_y + vb_h)/2, ' Eg > 5 eV\n Forbidden Gap', va='center', fontsize=7.5, color='red', fontweight='bold')
        elif i == 1:
            cb_y = 3.5
            cb_h = 1.8
            ax.add_patch(patches.Rectangle((0.5, cb_y), 3.0, cb_h, fc='#2980b9', ec='black'))
            ax.text(2.0, cb_y + cb_h/2, 'Conduction Band\n(Partially Filled @ 300K)', color='white', ha='center', va='center', fontweight='bold', fontsize=8)
            ax.annotate('', xy=(3.7, cb_y), xytext=(3.7, vb_y + vb_h), arrowprops=dict(arrowstyle='<->', color='darkgreen', lw=1.5))
            ax.text(3.7, (cb_y + vb_y + vb_h)/2, ' Eg = 1.1 eV', va='center', fontsize=8, color='darkgreen', fontweight='bold')
        else:
            cb_y = 2.0
            cb_h = 2.0
            ax.add_patch(patches.Rectangle((0.5, cb_y), 3.0, cb_h, fc='#e67e22', ec='black', alpha=0.7))
            ax.text(2.0, cb_y + cb_h/2, 'Overlapping Conduction\n& Valence Bands (Eg=0)', color='white', ha='center', va='center', fontweight='bold', fontsize=8)

    plt.suptitle("Energy Band Diagrams: Insulators, Semiconductors, and Conductors", fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig2_2_energy_bands.png"))
    plt.close()

    # 2.3 PN Junction Depletion Region
    fig, ax = plt.subplots(figsize=(8, 3.8), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    ax.add_patch(patches.Rectangle((1, 1), 4, 3, fc='#e8f8f5', ec='#16a085', lw=2))
    ax.add_patch(patches.Rectangle((5, 1), 4, 3, fc='#fef9e7', ec='#f39c12', lw=2))
    ax.add_patch(patches.Rectangle((3.8, 1), 2.4, 3, fc='#eaeded', ec='red', lw=1.5, linestyle='--'))
    
    ax.text(4.4, 2.5, "Negative\nAcceptor Ions\n(- - -)", ha='center', va='center', color='#c0392b', fontsize=8, fontweight='bold')
    ax.text(5.6, 2.5, "Positive\nDonor Ions\n(+ + +)", ha='center', va='center', color='#2980b9', fontsize=8, fontweight='bold')
    
    ax.text(2.4, 2.5, "P-Type Region\nMajority: Holes (h⁺)\nMinority: Electrons (e⁻)", ha='center', va='center', color='#16a085', fontsize=8.5, fontweight='bold')
    ax.text(7.6, 2.5, "N-Type Region\nMajority: Electrons (e⁻)\nMinority: Holes (h⁺)", ha='center', va='center', color='#d35400', fontsize=8.5, fontweight='bold')
    
    ax.annotate('', xy=(4.0, 0.6), xytext=(6.0, 0.6), arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(5.0, 0.3, "Internal Electric Field (E-field)", ha='center', color='red', fontweight='bold', fontsize=8)
    
    ax.set_title("Unbiased PN Junction: Depletion Layer and Built-in Barrier Potential (V₀ ≈ 0.7V for Si)", fontsize=10.5, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig2_3_pn_junction_equilibrium.png"))
    plt.close()

    # 2.4 Hall Effect Sensor Principle
    fig, ax = plt.subplots(figsize=(7, 3.8), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    slab = patches.Polygon([[2, 2], [6, 2], [7, 3.5], [3, 3.5]], fc='#bdc3c7', ec='#2c3e50', lw=2)
    ax.add_patch(slab)
    ax.annotate('', xy=(6.5, 2.75), xytext=(1.0, 2.75), arrowprops=dict(arrowstyle='->', color='blue', lw=2.5))
    ax.text(1.2, 3.0, 'Current $I_x$', color='blue', fontweight='bold', fontsize=10)
    ax.annotate('', xy=(4.5, 5.5), xytext=(4.5, 2.8), arrowprops=dict(arrowstyle='->', color='green', lw=2.5))
    ax.text(4.7, 5.2, 'Magnetic Field $B_z$', color='green', fontweight='bold', fontsize=10)
    ax.annotate('', xy=(5.2, 4.2), xytext=(3.5, 1.3), arrowprops=dict(arrowstyle='<->', color='crimson', lw=2))
    ax.text(5.5, 3.9, r'Hall Voltage $V_H = \frac{I_x B_z}{n q t}$', color='crimson', fontweight='bold', fontsize=10)
    ax.set_title("Hall Effect Sensor Operation in Agricultural Machinery Speed Sensing", fontsize=10.5, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig2_4_hall_effect_sensor.png"))
    plt.close()
    print("[Gen] Lecture 2 figures ready.")

# -------------------------------------------------------------
# LECTURE 3 FIGURES: SEMICONDUCTOR DIODE & CIRCUITS
# -------------------------------------------------------------
def generate_lecture_3_figures():
    # 3.1 Diode IV Characteristics
    v = np.linspace(-5, 0.9, 500)
    Is = 1e-9
    Vt = 0.026
    i = np.where(v < -4.5, -40e-3, np.where(v < 0.6, Is * (np.exp(np.clip(v, -10, 0.6)/Vt) - 1), 0.001 * np.exp((v-0.6)*15)))
    
    fig, ax = plt.subplots(figsize=(7, 4), dpi=300)
    ax.plot(v, i * 1000, color='#2980b9', lw=2.2, label='Silicon Diode (1N4007)')
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    ax.axvline(0.7, color='red', linestyle='--', lw=1.2, label=r'Knee Voltage $V_K \approx 0.7$ V')
    ax.set_xlim(-5.5, 1.0)
    ax.set_ylim(-15, 30)
    ax.set_xlabel('Diode Voltage $V_D$ (V)', fontsize=10)
    ax.set_ylabel('Diode Current $I_D$ (mA)', fontsize=10)
    ax.set_title('Complete I-V Characteristic Curve of a Silicon PN Diode', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(frameon=True, loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig3_1_diode_iv_characteristics.png"))
    plt.close()

    # 3.2 Bridge Rectifier Schematic
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        d += elm.SourceSin().label('$V_{in}(t)$', loc='left')
        d += elm.Line().right().length(1.5)
        d += elm.Dot()
        d += elm.Diode().theta(45).label('$D_1$', loc='top')
        d += elm.Dot()
        d.push()
        d += elm.Line().right().length(2)
        d += elm.Resistor().down().label('$R_L$', loc='right')
        d += elm.Line().left().length(2)
        d.pop()
        d += elm.Diode().theta(-45).label('$D_2$', loc='bottom')
        d += elm.Diode().theta(-135).label('$D_3$', loc='bottom')
        d += elm.Diode().theta(135).label('$D_4$', loc='top')
        d.save(os.path.join(FIGURES_DIR, "fig3_2_bridge_rectifier_schematic.png"))

    # 3.3 Rectifier Waveforms
    t = np.linspace(0, 4 * np.pi, 500)
    vin = np.sin(t)
    v_half = np.maximum(vin - 0.1, 0)
    v_full = np.abs(vin)
    v_filtered = 0.9 + 0.1 * np.cos(2*t)
    
    fig, axes = plt.subplots(3, 1, figsize=(8, 5.5), sharex=True, dpi=300)
    axes[0].plot(t, vin, color='#2c3e50', lw=1.8)
    axes[0].set_title('AC Input Voltage Waveform ($V_{in}$)', fontsize=9, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(t, v_half, color='#e67e22', lw=1.8, label='Half-Wave Output')
    axes[1].plot(t, v_full, color='#27ae60', lw=1.8, linestyle='--', label='Full-Wave Bridge Output')
    axes[1].set_title('Rectified Output without Filtering', fontsize=9, fontweight='bold')
    axes[1].legend(loc='upper right', fontsize=8)
    axes[1].grid(True, alpha=0.3)
    
    axes[2].plot(t, v_full, color='#bdc3c7', lw=1, linestyle=':')
    axes[2].plot(t, v_filtered, color='#c0392b', lw=2.0, label=r'Filtered DC ($V_{dc}$ with Ripple $V_r$)')
    axes[2].set_title('Filtered DC Output with Smoothing Capacitor Filter', fontsize=9, fontweight='bold')
    axes[2].legend(loc='lower right', fontsize=8)
    axes[2].grid(True, alpha=0.3)
    axes[2].set_xlabel('Time (rad)', fontsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig3_3_rectifier_waveforms.png"))
    plt.close()

    # 3.4 Diode Clipper & Clamper Circuits
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        d += elm.SourceSin().label('$V_{in}$', loc='left')
        d += elm.Resistor().right().label('$R$', loc='top')
        d += elm.Dot()
        d.push()
        d += elm.Diode().down().label('Diode', loc='right')
        d += elm.Line().left()
        d.pop()
        d += elm.Line().right().length(1.5)
        d += elm.Dot(open=True).label('$V_{out}$ (Clipped)', loc='right')
        d.save(os.path.join(FIGURES_DIR, "fig3_4_clipper_clamper_circuits.png"))
    print("[Gen] Lecture 3 figures ready.")

# -------------------------------------------------------------
# LECTURE 4 FIGURES: SPECIAL PURPOSE DIODES
# -------------------------------------------------------------
def generate_lecture_4_figures():
    # 4.1 Zener Voltage Regulator Circuit
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        d += elm.SourceV().label('$V_{in}$ (Unregulated)', loc='left')
        d += elm.Resistor().right().label('$R_S$', loc='top')
        d += elm.Dot()
        d.push()
        d += elm.Zener().down().reverse().label('$V_Z = 5.1$V', loc='right')
        d += elm.Line().left()
        d.pop()
        d += elm.Line().right().length(2)
        d += elm.Dot()
        d.push()
        d += elm.Resistor().down().label('$R_L$ (Load)', loc='right')
        d += elm.Line().left().length(2)
        d.pop()
        d += elm.Line().right().length(1)
        d += elm.Dot(open=True).label('$V_{out} = V_Z$', loc='right')
        d.save(os.path.join(FIGURES_DIR, "fig4_1_zener_regulator_schematic.png"))

    # 4.2 Zener Reverse Breakdown IV
    vz = np.linspace(-7, 1, 400)
    iz = np.where(vz < -5.1, -100 * (np.abs(vz) - 5.1), np.where(vz > 0.7, 50 * (vz - 0.7), 0))
    fig, ax = plt.subplots(figsize=(7, 3.8), dpi=300)
    ax.plot(vz, iz, color='#8e44ad', lw=2.2)
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    ax.axvline(-5.1, color='crimson', linestyle='--', lw=1.2)
    ax.text(-5.0, -40, 'Zener Breakdown Voltage $V_Z = -5.1$V\nRegulated Region', color='crimson', fontweight='bold', fontsize=8.5)
    ax.set_xlabel('Zener Voltage $V_Z$ (V)', fontsize=10)
    ax.set_ylabel('Zener Current $I_Z$ (mA)', fontsize=10)
    ax.set_title('Zener Diode I-V Characteristics: Breakdown & Voltage Regulation', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig4_2_zener_iv_characteristics.png"))
    plt.close()

    # 4.3 LED Circuit
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        d += elm.SourceV().label('+5V DC', loc='left')
        d += elm.Resistor().right().label(r'$R_{limit} = 220\Omega$', loc='top')
        d += elm.LED().down().label(r'LED ($\lambda=565$nm)', loc='right')
        d += elm.Ground()
        d.save(os.path.join(FIGURES_DIR, "fig4_3_led_operation.png"))

    # 4.4 Schottky vs Standard Diode
    v_f = np.linspace(0, 0.9, 200)
    i_pn = 1e-9 * (np.exp(v_f / 0.026) - 1)
    i_schottky = 1e-6 * (np.exp(v_f / 0.026) - 1)
    
    fig, ax = plt.subplots(figsize=(7, 3.8), dpi=300)
    ax.plot(v_f, i_schottky * 1000, label='Schottky Diode (Forward Drop ≈ 0.3V, Ultra-fast)', color='#d35400', lw=2.2)
    ax.plot(v_f, i_pn * 1000, label='Silicon PN Diode (Forward Drop ≈ 0.7V)', color='#2980b9', lw=2.2, linestyle='--')
    ax.set_ylim(0, 50)
    ax.set_xlabel('Forward Voltage $V_F$ (V)', fontsize=10)
    ax.set_ylabel('Forward Current $I_F$ (mA)', fontsize=10)
    ax.set_title('Conduction Comparison: Schottky Diode vs Silicon Diode', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig4_4_schottky_diode.png"))
    plt.close()
    print("[Gen] Lecture 4 figures ready.")

# -------------------------------------------------------------
# LECTURE 5 FIGURES: BJT TRANSISTORS
# -------------------------------------------------------------
def generate_lecture_5_figures():
    # 5.1 BJT Symbols
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        d += elm.BjtNpn().label('NPN Transistor\n(e.g., 2N2222)', loc='right')
        d += elm.Line().right().at((3.5, 0)).length(1)
        d += elm.BjtPnp().at((5.5, 0)).label('PNP Transistor\n(e.g., 2N3906)', loc='right')
        d.save(os.path.join(FIGURES_DIR, "fig5_1_bjt_structure_symbols.png"))

    # 5.2 BJT CE Output Characteristics & DC Load Line
    vce = np.linspace(0, 15, 300)
    ib_values = [10, 20, 30, 40, 50]
    beta = 100
    
    fig, ax = plt.subplots(figsize=(7.5, 4.2), dpi=300)
    for ib in ib_values:
        ic_sat = (beta * ib * 1e-3) * (1 - np.exp(-vce / 0.8)) * (1 + 0.02 * vce)
        ax.plot(vce, ic_sat, color='#2c3e50', lw=1.6, label=f'$I_B = {ib}\\mu$A')
        
    vcc = 12
    rc = 2.0
    ic_load = (vcc - vce) / rc
    ax.plot(vce[vce <= vcc], ic_load[vce <= vcc], color='crimson', lw=2.2, linestyle='--', label=r'DC Load Line ($V_{CC}=12$V, $R_C=2$k$\Omega$)')
    
    vq = 6.0
    iq = (vcc - vq) / rc
    ax.scatter([vq], [iq], color='darkgreen', s=70, zorder=6)
    ax.text(vq + 0.3, iq + 0.3, 'Q-Point ($V_{CEQ}=6$V, $I_{CQ}=3$mA)', color='darkgreen', fontweight='bold', fontsize=8.5)
    
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 7)
    ax.set_xlabel('Collector-Emitter Voltage $V_{CE}$ (V)', fontsize=10)
    ax.set_ylabel('Collector Current $I_C$ (mA)', fontsize=10)
    ax.set_title('BJT CE Output Characteristics & DC Load Line with Q-Point', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(frameon=True, loc='upper right', fontsize=8.5)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig5_2_bjt_ce_output_characteristics.png"))
    plt.close()

    # 5.3 Voltage Divider Biased CE Amplifier
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        q1 = elm.BjtNpn().label('Q1 (2N2222)', loc='right')
        d += q1
        d += elm.Resistor().at(q1.collector).up().label(r'$R_C = 2.2k\Omega$', loc='right')
        d += elm.Line().up().length(0.5).label('$+V_{CC} = 12$V', loc='right')
        d += elm.Resistor().at(q1.base).up().label(r'$R_1 = 33k\Omega$', loc='left')
        d += elm.Line().right().tox(q1.collector)
        d += elm.Resistor().at(q1.base).down().label(r'$R_2 = 10k\Omega$', loc='left')
        d += elm.Ground()
        d += elm.Resistor().at(q1.emitter).down().label(r'$R_E = 1k\Omega$', loc='right')
        d += elm.Ground()
        d += elm.Capacitor().at(q1.base).left().label('$C_1$', loc='top')
        d += elm.Dot(open=True).label('$V_{in}$', loc='left')
        d += elm.Capacitor().at(q1.collector).right().label('$C_2$', loc='top')
        d += elm.Dot(open=True).label('$V_{out}$', loc='right')
        d.save(os.path.join(FIGURES_DIR, "fig5_3_voltage_divider_bias.png"))

    # 5.4 BJT Solenoid Relay Driver
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        q = elm.BjtNpn().label('Switching BJT', loc='right')
        d += q
        d += elm.Ground().at(q.emitter)
        d += elm.Resistor().at(q.base).left().label(r'$R_B = 1k\Omega$', loc='top')
        d += elm.Dot(open=True).label('MCU GPIO\n(3.3V / 5V)', loc='left')
        d += elm.Line().at(q.collector).up().length(1)
        d += elm.Dot()
        d.push()
        d += elm.Inductor().up().label('12V Irrigation\nSolenoid Valve', loc='right')
        d += elm.Dot()
        d.pop()
        d += elm.Diode().up().reverse().label('Flyback\n1N4007', loc='left')
        d += elm.Line().right()
        d += elm.Line().up().length(0.5).label('+12V DC Supply', loc='right')
        d.save(os.path.join(FIGURES_DIR, "fig5_4_bjt_relay_driver.png"))
    print("[Gen] Lecture 5 figures ready.")

# -------------------------------------------------------------
# LECTURE 6 FIGURES: FET & MOSFET
# -------------------------------------------------------------
def generate_lecture_6_figures():
    # 6.1 JFET Characteristics
    vds = np.linspace(0, 10, 300)
    vgs_vals = [0, -1, -2, -3]
    idss = 10.0
    vp = -4.0
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4), dpi=300)
    
    for vgs in vgs_vals:
        vds_sat = vgs - vp
        id_sat = idss * (1 - vgs/vp)**2
        id_curve = np.where(vds < vds_sat, id_sat * (2*(vds/vds_sat) - (vds/vds_sat)**2), id_sat * (1 + 0.015*vds))
        ax1.plot(vds, id_curve, lw=1.8, label=f'$V_{{GS}} = {vgs}$ V')
        
    ax1.set_xlabel('Drain-Source Voltage $V_{DS}$ (V)', fontsize=10)
    ax1.set_ylabel('Drain Current $I_D$ (mA)', fontsize=10)
    ax1.set_title('JFET Drain Characteristics', fontsize=11, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(frameon=True)
    
    vgs_t = np.linspace(vp, 0, 100)
    id_t = idss * (1 - vgs_t / vp)**2
    ax2.plot(vgs_t, id_t, color='#c0392b', lw=2.2, label=r"$I_D = I_{DSS}(1 - \frac{V_{GS}}{V_P})^2$")
    ax2.axvline(vp, color='black', linestyle='--', label=f'Pinch-off $V_P = {vp}$ V')
    ax2.set_xlabel('Gate-Source Voltage $V_{GS}$ (V)', fontsize=10)
    ax2.set_ylabel('Drain Current $I_D$ (mA)', fontsize=10)
    ax2.set_title('JFET Transfer Characteristics', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig6_2_jfet_characteristics.png"))
    plt.close()

    # 6.2 Power MOSFET Motor Driver
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        m = elm.NFet().label('Power MOSFET\nIRF540N', loc='right')
        d += m
        d += elm.Ground().at(m.source)
        d += elm.Resistor().at(m.gate).left().label(r'$R_G = 100\Omega$', loc='top')
        d += elm.Dot(open=True).label('PWM Signal\nfrom MCU', loc='left')
        d += elm.Resistor().at(m.gate).down().label(r'$R_{pull-down} = 10k\Omega$', loc='right')
        d += elm.Ground()
        d += elm.Motor().at(m.drain).up().label('24V Solar\nWater Pump', loc='right')
        d += elm.Line().up().length(0.5).label('+24V DC Supply', loc='right')
        d.save(os.path.join(FIGURES_DIR, "fig6_4_power_mosfet_motor_driver.png"))
    print("[Gen] Lecture 6 figures ready.")

# -------------------------------------------------------------
# LECTURE 7 FIGURES: NUMBER SYSTEMS & ARITHMETIC
# -------------------------------------------------------------
def generate_lecture_7_figures():
    # 7.1 Number Systems Hierarchy
    fig, ax = plt.subplots(figsize=(8, 3.8), dpi=300)
    ax.axis('off')
    
    systems = [
        ("Binary\n(Base 2)", "Symbols: 0, 1\nFundamental digital logic & memory bit", "#3498db", 1.5),
        ("Octal\n(Base 8)", "Symbols: 0 - 7\nCompact 3-bit grouping ($2^3 = 8$)", "#2ecc71", 4.0),
        ("Decimal\n(Base 10)", "Symbols: 0 - 9\nHuman-readable interface & agricultural sensors", "#e67e22", 6.5),
        ("Hexadecimal\n(Base 16)", "Symbols: 0-9, A-F\nCompact 4-bit byte representation ($2^4 = 16$)", "#9b59b6", 9.0)
    ]
    
    for name, desc, col, x in systems:
        box = patches.FancyBboxPatch((x-1.1, 1.2), 2.2, 2.2, boxstyle="round,pad=0.2", fc=col, ec='black', lw=1.5, alpha=0.85)
        ax.add_patch(box)
        ax.text(x, 2.7, name, ha='center', va='center', color='white', fontweight='bold', fontsize=9.5)
        ax.text(x, 1.8, desc, ha='center', va='center', color='white', fontsize=7.5)
        
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 4.5)
    ax.set_title("Digital Number Systems and Their Positional Radices", fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig7_1_number_systems_hierarchy.png"))
    plt.close()

    # 7.2 Two's Complement Number Circle
    fig, ax = plt.subplots(figsize=(5.5, 5.5), dpi=300)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    circle = patches.Circle((0, 0), 1.0, fill=False, color='#34495e', lw=2)
    ax.add_patch(circle)
    
    values = [
        ("0000", "+0", 0), ("0001", "+1", 1), ("0010", "+2", 2), ("0011", "+3", 3),
        ("0100", "+4", 4), ("0101", "+5", 5), ("0110", "+6", 6), ("0111", "+7", 7),
        ("1000", "-8", 8), ("1001", "-7", 9), ("1010", "-6", 10), ("1011", "-5", 11),
        ("1100", "-4", 12), ("1101", "-3", 13), ("1110", "-2", 14), ("1111", "-1", 15)
    ]
    
    for bin_code, dec_val, idx in values:
        angle = np.pi/2 - idx * (2 * np.pi / 16)
        x_inner = 0.85 * np.cos(angle)
        y_inner = 0.85 * np.sin(angle)
        x_outer = 1.25 * np.cos(angle)
        y_outer = 1.25 * np.sin(angle)
        
        color = '#27ae60' if idx <= 7 else '#c0392b'
        ax.text(x_inner, y_inner, bin_code, ha='center', va='center', fontsize=7.5, color='#2c3e50', fontweight='bold')
        ax.text(x_outer, y_outer, dec_val, ha='center', va='center', fontsize=8.5, color=color, fontweight='bold')
        
    ax.text(0, 0, "4-Bit 2's\nComplement\nModular Ring", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#2c3e50')
    ax.set_title("Two's Complement Representation (-8 to +7)", fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig7_2_twos_complement_circle.png"))
    plt.close()
    print("[Gen] Lecture 7 figures ready.")

# -------------------------------------------------------------
# LECTURE 8 FIGURES: LOGIC GATES & DIGITAL CIRCUITS
# -------------------------------------------------------------
def generate_lecture_8_figures():
    # 8.1 Logic Gates using schemdraw.logic
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        d += logic.And().label('AND: $Y = A \\cdot B$', loc='right')
        d += logic.Or().at((4, 0)).label('OR: $Y = A + B$', loc='right')
        d += logic.Not().at((8, 0)).label(r'NOT: $Y = \bar{A}$', loc='right')
        d += logic.Nand().at((0, -3)).label(r'NAND: $Y = \overline{A \cdot B}$', loc='right')
        d += logic.Nor().at((4, -3)).label(r'NOR: $Y = \overline{A + B}$', loc='right')
        d += logic.Xor().at((8, -3)).label(r'XOR: $Y = A \oplus B$', loc='right')
        d.save(os.path.join(FIGURES_DIR, "fig8_1_standard_logic_gates.png"))

    # 8.2 Half Adder Circuit
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        x1 = logic.Xor().label('Sum: $S = A \\oplus B$', loc='right')
        d += x1
        a1 = logic.And().at((0, -2.5)).label('Carry: $C = A \\cdot B$', loc='right')
        d += a1
        d += elm.Line().at(x1.in1).left().length(1.5).label('A', loc='left')
        d += elm.Line().at(x1.in2).left().length(1.5).label('B', loc='left')
        d.save(os.path.join(FIGURES_DIR, "fig8_3_half_full_adder_circuits.png"))

    # 8.3 Greenhouse Automated Ventilation Logic Circuit
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=10)
        a1 = logic.And().label('Temp and Humid Match', loc='right')
        d += a1
        d += elm.Line().at(a1.in1).left().length(1.0).label('Temp Sensor High', loc='left')
        d += elm.Line().at(a1.in2).left().length(1.0).label('Humidity Sensor High', loc='left')
        o1 = logic.Or().at((4.5, -0.5)).label('Ventilation Fan Actuator', loc='right')
        d += o1
        d += elm.Line().at(a1.out).toy(o1.in1).tox(o1.in1)
        d += elm.Line().at(o1.in2).left().length(2.0).label('Manual Emergency Override', loc='left')
        d.save(os.path.join(FIGURES_DIR, "fig8_4_greenhouse_ventilation_system.png"))
    print("[Gen] Lecture 8 figures ready.")

# -------------------------------------------------------------
# LECTURE 9 FIGURES: BOOLEAN ALGEBRA & KARNAUGH MAPS
# -------------------------------------------------------------
def generate_lecture_9_figures():
    # 9.1 De Morgan's Law Switching Circuit Analogy
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3.2), dpi=300)
    
    ax1.set_xlim(0, 8)
    ax1.set_ylim(0, 4)
    ax1.axis('off')
    ax1.plot([1, 2.5], [2, 2], 'k-', lw=2)
    ax1.plot([2.5, 3.5], [2, 2.8], 'crimson', lw=2.5)
    ax1.plot([3.5, 4.5], [2, 2], 'k-', lw=2)
    ax1.plot([4.5, 5.5], [2, 2.8], 'crimson', lw=2.5)
    ax1.plot([5.5, 7], [2, 2], 'k-', lw=2)
    ax1.text(3.0, 3.1, 'Switch A', color='crimson', fontweight='bold', ha='center')
    ax1.text(5.0, 3.1, 'Switch B', color='crimson', fontweight='bold', ha='center')
    ax1.set_title(r"Series Connection: Logic AND ($Y = A \cdot B$)", fontsize=9.5, fontweight='bold')
    
    ax2.set_xlim(0, 8)
    ax2.set_ylim(0, 4)
    ax2.axis('off')
    ax2.plot([1, 2.5], [2, 2], 'k-', lw=2)
    ax2.plot([2.5, 2.5], [1, 3], 'k-', lw=2)
    ax2.plot([2.5, 3.5], [3, 3], 'k-', lw=2)
    ax2.plot([3.5, 4.5], [3, 3.7], 'royalblue', lw=2.5)
    ax2.plot([4.5, 5.5], [3, 3], 'k-', lw=2)
    ax2.plot([2.5, 3.5], [1, 1], 'k-', lw=2)
    ax2.plot([3.5, 4.5], [1, 1.7], 'royalblue', lw=2.5)
    ax2.plot([4.5, 5.5], [1, 1], 'k-', lw=2)
    ax2.plot([5.5, 5.5], [1, 3], 'k-', lw=2)
    ax2.plot([5.5, 7], [2, 2], 'k-', lw=2)
    ax2.text(4.0, 3.9, 'Switch A', color='royalblue', fontweight='bold', ha='center')
    ax2.text(4.0, 1.9, 'Switch B', color='royalblue', fontweight='bold', ha='center')
    ax2.set_title(r"Parallel Connection: Logic OR ($Y = A + B$)", fontsize=9.5, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig9_1_demorgan_switching_circuits.png"))
    plt.close()

    # 9.2 4-Variable Karnaugh Map Grid with Gray Code
    fig, ax = plt.subplots(figsize=(5.5, 5.5), dpi=300)
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.axis('off')
    
    for i in range(5):
        ax.plot([0, 4], [i, i], 'k-', lw=1.5)
        ax.plot([i, i], [0, 4], 'k-', lw=1.5)
        
    cols = ['00', '01', '11', '10']
    rows = ['00', '01', '11', '10']
    
    ax.text(-0.5, 4.5, 'AB \\ CD', fontweight='bold', fontsize=10, ha='center', va='center')
    for j, c in enumerate(cols):
        ax.text(j + 0.5, 4.3, c, fontweight='bold', fontsize=9.5, ha='center', va='center', color='#2980b9')
    for i, r in enumerate(rows):
        ax.text(-0.4, 3.5 - i, r, fontweight='bold', fontsize=9.5, ha='center', va='center', color='#27ae60')
        
    minterms = [
        [0, 1, 3, 2],
        [4, 5, 7, 6],
        [12, 13, 15, 14],
        [8, 9, 11, 10]
    ]
    
    for r_idx in range(4):
        for c_idx in range(4):
            m = minterms[r_idx][c_idx]
            ax.text(c_idx + 0.85, 3.15 - r_idx, f'm{m}', fontsize=7.5, color='gray')
            
    quad = patches.Rectangle((1.05, 1.05), 1.9, 1.9, fc='gold', ec='orange', lw=2, alpha=0.4, linestyle='--')
    ax.add_patch(quad)
    ax.text(2.0, 2.0, "Group of 4 (Quad)\nEliminates 2 Variables", ha='center', va='center', color='#d35400', fontweight='bold', fontsize=8.5)
    
    ax.set_title("4-Variable Karnaugh Map (Gray Code Order)", fontsize=11, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig9_2_kmap_configurations.png"))
    plt.close()
    print("[Gen] Lecture 9 figures ready.")

def main():
    print("Generating all course figures and downloading hardware images for AEN 214...")
    crawl_hardware_images()
    generate_lecture_1_figures()
    generate_lecture_2_figures()
    generate_lecture_3_figures()
    generate_lecture_4_figures()
    generate_lecture_5_figures()
    generate_lecture_6_figures()
    generate_lecture_7_figures()
    generate_lecture_8_figures()
    generate_lecture_9_figures()
    print(f"All figures successfully generated in {FIGURES_DIR}!")

if __name__ == "__main__":
    main()
