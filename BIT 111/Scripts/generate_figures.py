#!/usr/bin/env python3
"""
generate_figures.py
Generates publication-quality technical diagrams, architectural flowcharts,
and schematics for BIT 111: Microcomputers and Applications.
Department of Informatics and Information Technology (DIIT),
Sokoine University of Agriculture (SUA).
"""

import os
import sys

LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

# Set matplotlib cache directory to /tmp
os.environ['MPLCONFIGDIR'] = '/tmp/mpl_bit111'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

FIGURES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Figures"))
os.makedirs(FIGURES_DIR, exist_ok=True)

SUA_GREEN = "#008836"
SUA_DARK = "#005a24"
CHARCOAL = "#1e293b"
BG_LIGHT = "#f8fafc"
BORDER_GRAY = "#94a3b8"
ACCENT_BLUE = "#0284c7"
ACCENT_AMBER = "#d97706"
ACCENT_RED = "#dc2626"

def save_fig(fig, filename):
    out_path = os.path.join(FIGURES_DIR, filename)
    fig.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"[Created] {out_path}")

# -------------------------------------------------------------
# FIGURE 1.1: COMPUTER GENERATIONS TIMELINE
# -------------------------------------------------------------
def build_fig1_1():
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.set_facecolor(BG_LIGHT)
    
    gens = [
        ("1st Gen\n(1940-1956)", "Vacuum Tubes\nMagnetic Drums\nMachine Code\nENIAC, UNIVAC", 0.5),
        ("2nd Gen\n(1956-1963)", "Transistors\nMagnetic Core\nAssembly/FORTRAN\nIBM 7094", 2.3),
        ("3rd Gen\n(1964-1971)", "Integrated Circuits\nKeyboards/Monitors\nOperating Systems\nIBM System/360", 4.1),
        ("4th Gen\n(1971-Present)", "VLSI / Microprocessors\nPersonal Computers\nGUI, Internet\nIntel 4004 to Core i9", 5.9),
        ("5th Gen\n(Present-Beyond)", "Ultra Large Scale ULSI\nAI & Neural Processing\nParallel/Quantum\nAutonomous Systems", 7.7)
    ]
    
    ax.annotate("", xy=(9.2, 2.0), xytext=(0.1, 2.0),
                arrowprops=dict(arrowstyle="->", color=SUA_GREEN, lw=3))
    
    for title, desc, x in gens:
        # Box
        rect = patches.FancyBboxPatch((x-0.75, 2.4), 1.5, 1.4, boxstyle="round,pad=0.1",
                                      ec=SUA_DARK, fc="white", lw=1.5)
        ax.add_patch(rect)
        ax.text(x, 3.1, title, ha="center", va="center", fontsize=9, fontweight="bold", color=SUA_DARK)
        
        # Details below
        rect_desc = patches.FancyBboxPatch((x-0.75, 0.4), 1.5, 1.3, boxstyle="round,pad=0.08",
                                           ec=BORDER_GRAY, fc="white", lw=1.0)
        ax.add_patch(rect_desc)
        ax.text(x, 1.05, desc, ha="center", va="center", fontsize=7.2, color=CHARCOAL)
        
        # Connecting dot on line
        ax.plot(x, 2.0, marker="o", markersize=8, color=SUA_GREEN)
        ax.plot([x, x], [2.0, 2.4], color=SUA_GREEN, lw=1.5, ls="--")
        ax.plot([x, x], [2.0, 1.7], color=BORDER_GRAY, lw=1.5, ls="--")
        
    ax.set_xlim(-0.2, 9.6)
    ax.set_ylim(0.1, 4.0)
    ax.axis("off")
    ax.set_title("Evolution of Computer Generations (1st through 5th Generation Architecture)",
                 fontsize=11, fontweight="bold", color=SUA_DARK, pad=12)
    save_fig(fig, "fig1_1_computer_generations.png")

# -------------------------------------------------------------
# FIGURE 1.2: VON NEUMANN ARCHITECTURE
# -------------------------------------------------------------
def build_fig1_2():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_facecolor(BG_LIGHT)
    
    # CPU Container
    cpu_box = patches.FancyBboxPatch((2.6, 1.4), 3.8, 2.6, boxstyle="round,pad=0.1",
                                     ec=SUA_DARK, fc="#f0fdf4", lw=2)
    ax.add_patch(cpu_box)
    ax.text(4.5, 3.75, "CENTRAL PROCESSING UNIT (CPU)", ha="center", fontsize=10, fontweight="bold", color=SUA_DARK)
    
    # Inside CPU: CU, ALU, Registers
    cu = patches.Rectangle((2.8, 2.6), 1.6, 0.9, ec=SUA_GREEN, fc="white", lw=1.2)
    ax.add_patch(cu)
    ax.text(3.6, 3.05, "Control Unit\n(CU)", ha="center", va="center", fontsize=8.5, fontweight="bold")
    
    alu = patches.Rectangle((4.6, 2.6), 1.6, 0.9, ec=SUA_GREEN, fc="white", lw=1.2)
    ax.add_patch(alu)
    ax.text(5.4, 3.05, "Arithmetic Logic\nUnit (ALU)", ha="center", va="center", fontsize=8.5, fontweight="bold")
    
    regs = patches.Rectangle((3.2, 1.6), 2.6, 0.7, ec=SUA_GREEN, fc="white", lw=1.2)
    ax.add_patch(regs)
    ax.text(4.5, 1.95, "Registers (PC, IR, MAR, MDR, ACC)", ha="center", va="center", fontsize=8, fontweight="bold")
    
    # Input Device
    inp = patches.FancyBboxPatch((0.4, 2.1), 1.5, 1.2, boxstyle="round,pad=0.08", ec=ACCENT_BLUE, fc="white", lw=1.5)
    ax.add_patch(inp)
    ax.text(1.15, 2.7, "INPUT\nDEVICES", ha="center", va="center", fontsize=9, fontweight="bold", color=ACCENT_BLUE)
    ax.text(1.15, 2.3, "Keyboard, Mouse\nSensor, Scanner", ha="center", va="center", fontsize=7, color=CHARCOAL)
    
    # Output Device
    out = patches.FancyBboxPatch((7.1, 2.1), 1.5, 1.2, boxstyle="round,pad=0.08", ec=ACCENT_AMBER, fc="white", lw=1.5)
    ax.add_patch(out)
    ax.text(7.85, 2.7, "OUTPUT\nDEVICES", ha="center", va="center", fontsize=9, fontweight="bold", color=ACCENT_AMBER)
    ax.text(7.85, 2.3, "Monitor, Printer\nActuator, Speaker", ha="center", va="center", fontsize=7, color=CHARCOAL)
    
    # Primary Memory
    mem = patches.FancyBboxPatch((3.0, 0.2), 3.0, 0.9, boxstyle="round,pad=0.08", ec="#7c3aed", fc="white", lw=1.5)
    ax.add_patch(mem)
    ax.text(4.5, 0.72, "PRIMARY MEMORY (RAM / ROM)", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#7c3aed")
    ax.text(4.5, 0.42, "Stored Program & Shared Data Instructions", ha="center", va="center", fontsize=7.2, color=CHARCOAL)
    
    # Arrows
    # Input -> CPU
    ax.annotate("", xy=(2.6, 2.7), xytext=(1.9, 2.7), arrowprops=dict(arrowstyle="->", color=ACCENT_BLUE, lw=2))
    # CPU -> Output
    ax.annotate("", xy=(7.1, 2.7), xytext=(6.4, 2.7), arrowprops=dict(arrowstyle="->", color=ACCENT_AMBER, lw=2))
    # CPU <-> Memory (Bidirectional System Bus)
    ax.annotate("", xy=(4.2, 1.4), xytext=(4.2, 1.1), arrowprops=dict(arrowstyle="<->", color=SUA_DARK, lw=2))
    ax.annotate("", xy=(4.8, 1.4), xytext=(4.8, 1.1), arrowprops=dict(arrowstyle="<->", color=SUA_DARK, lw=2))
    ax.text(5.7, 1.25, "System Bus\n(Data, Addr, Ctrl)", fontsize=7.2, color=SUA_DARK)
    
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 4.3)
    ax.axis("off")
    ax.set_title("The Classical Von Neumann Computer Architecture Model", fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig1_2_von_neumann_architecture.png")

# -------------------------------------------------------------
# FIGURE 1.3: COMPUTER CLASSIFICATIONS
# -------------------------------------------------------------
def build_fig1_3():
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.set_facecolor(BG_LIGHT)
    
    classes = [
        ("Supercomputers", "Extreme computational power\nPFLOPS to ExaFLOPS scale\nWeather, Nuclear, AI models\nFrontier, Fugaku, Summit", "#991b1b"),
        ("Mainframe Computers", "Massive transaction throughput\nHigh fault-tolerance & reliability\nBanking, Airlines, Telecom\nIBM z16, LinuxONE", "#1e40af"),
        ("Minicomputers / Midrange", "Multi-user departmental servers\nScientific & Lab automation\nBridged micro to mainframe\nDEC VAX, IBM AS/400", "#065f46"),
        ("Microcomputers (PCs)", "Single-chip microprocessor (CPU)\nDesktops, Laptops, Workstations\nSmartphones, Tablets, Single-board\nApple Mac, Dell, Raspberry Pi", SUA_GREEN)
    ]
    
    y = 3.2
    for title, desc, color in classes:
        # Title pill
        ax.add_patch(patches.FancyBboxPatch((0.5, y-0.25), 2.4, 0.55, boxstyle="round,pad=0.05", ec=color, fc=color))
        ax.text(1.7, y, title, ha="center", va="center", color="white", fontsize=8.8, fontweight="bold")
        
        # Details pill
        ax.add_patch(patches.FancyBboxPatch((3.1, y-0.35), 5.4, 0.75, boxstyle="round,pad=0.05", ec=BORDER_GRAY, fc="white", lw=1.2))
        ax.text(3.3, y, desc, va="center", color=CHARCOAL, fontsize=7.8)
        
        # Arrow
        ax.annotate("", xy=(3.1, y), xytext=(2.9, y), arrowprops=dict(arrowstyle="->", color=color, lw=1.5))
        y -= 0.95
        
    ax.set_xlim(0.2, 8.8)
    ax.set_ylim(0.1, 3.8)
    ax.axis("off")
    ax.set_title("Taxonomy of Computer Systems by Scale, Architecture, and Processing Capacity",
                 fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig1_3_computer_classifications.png")

# -------------------------------------------------------------
# FIGURE 2.1: MICROCOMPUTER HARDWARE ARCHITECTURE
# -------------------------------------------------------------
def build_fig2_1():
    fig, ax = plt.subplots(figsize=(9.2, 4.6))
    ax.set_facecolor(BG_LIGHT)
    
    # Motherboard base
    mb = patches.FancyBboxPatch((0.5, 0.3), 8.2, 3.8, boxstyle="round,pad=0.1", ec=SUA_DARK, fc="#f0fdf4", lw=2)
    ax.add_patch(mb)
    ax.text(4.6, 3.85, "MICROCOMPUTER MOTHERBOARD SYSTEM ARCHITECTURE", ha="center", fontsize=9.5, fontweight="bold", color=SUA_DARK)
    
    # CPU Socket
    cpu = patches.Rectangle((1.0, 2.2), 2.2, 1.3, ec=CHARCOAL, fc="#e2e8f0", lw=1.5)
    ax.add_patch(cpu)
    ax.text(2.1, 3.1, "CPU (Microprocessor)\nALU | CU | Cache (L1/L2/L3)", ha="center", va="center", fontsize=7.5, fontweight="bold")
    ax.text(2.1, 2.5, "Memory Controller & PCIe Root", ha="center", va="center", fontsize=6.8, color=CHARCOAL)
    
    # RAM Slots
    ram = patches.Rectangle((4.0, 2.2), 2.0, 1.3, ec="#0284c7", fc="white", lw=1.5)
    ax.add_patch(ram)
    ax.text(5.0, 2.85, "System RAM (DDR4/DDR5)\nDual-Channel Bus", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#0284c7")
    ax.text(5.0, 2.4, "High-Speed Memory Bus (64-bit)", ha="center", va="center", fontsize=6.8, color=CHARCOAL)
    
    # Chipset (PCH)
    pch = patches.Rectangle((2.6, 0.7), 2.2, 1.1, ec="#d97706", fc="white", lw=1.5)
    ax.add_patch(pch)
    ax.text(3.7, 1.35, "Platform Controller Hub (PCH)\nSATA, USB, Audio, LAN", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#d97706")
    ax.text(3.7, 0.95, "DMI / System Link", ha="center", va="center", fontsize=6.8, color=CHARCOAL)
    
    # Storage NVMe & SATA
    stor = patches.Rectangle((6.5, 2.2), 1.8, 1.3, ec="#7c3aed", fc="white", lw=1.5)
    ax.add_patch(stor)
    ax.text(7.4, 2.85, "Mass Storage\nNVMe M.2 SSD", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#7c3aed")
    ax.text(7.4, 2.4, "PCIe Gen 4/5 (x4 lanes)", ha="center", va="center", fontsize=6.8, color=CHARCOAL)
    
    # External I/O Ports
    io_ports = patches.Rectangle((5.4, 0.7), 2.9, 1.1, ec=SUA_GREEN, fc="white", lw=1.5)
    ax.add_patch(io_ports)
    ax.text(6.85, 1.35, "External Peripheral I/O Interfaces", ha="center", va="center", fontsize=7.5, fontweight="bold", color=SUA_GREEN)
    ax.text(6.85, 0.95, "USB 3.2/Type-C | HDMI/DP | RJ-45 | Audio", ha="center", va="center", fontsize=6.8, color=CHARCOAL)
    
    # Interconnecting lines
    ax.annotate("", xy=(4.0, 2.85), xytext=(3.2, 2.85), arrowprops=dict(arrowstyle="<->", color="#0284c7", lw=2))
    ax.annotate("", xy=(6.5, 2.85), xytext=(6.0, 2.85), arrowprops=dict(arrowstyle="<->", color="#7c3aed", lw=2))
    ax.annotate("", xy=(2.6, 2.2), xytext=(3.2, 1.8), arrowprops=dict(arrowstyle="<->", color="#d97706", lw=2))
    ax.annotate("", xy=(5.4, 1.25), xytext=(4.8, 1.25), arrowprops=dict(arrowstyle="<->", color=SUA_DARK, lw=2))
    
    ax.set_xlim(0, 9.2)
    ax.set_ylim(0, 4.4)
    ax.axis("off")
    ax.set_title("Logical and Physical Interconnects of a Modern Microcomputer System", fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig2_1_microcomputer_hardware_block.png")

# -------------------------------------------------------------
# FIGURE 2.2: MEMORY HIERARCHY PYRAMID
# -------------------------------------------------------------
def build_fig2_2():
    fig, ax = plt.subplots(figsize=(8.8, 4.4))
    ax.set_facecolor(BG_LIGHT)
    
    levels = [
        ("CPU Registers (<1 KB, ~0.5 ns)", 0.20, "#dc2626"),
        ("L1 / L2 / L3 Cache (Up to 128 MB, 1-10 ns)", 0.38, "#ea580c"),
        ("Main Memory: DRAM DDR4/DDR5 (8-128 GB, 50-80 ns)", 0.56, "#d97706"),
        ("Solid-State Drives: NVMe PCIe SSD (500 GB - 4 TB, 10-100 µs)", 0.74, "#0284c7"),
        ("Magnetic Hard Disk Drives: HDD (2-20 TB, 5-15 ms)", 0.90, "#059669"),
        ("Optical / Cloud / Magnetic Tape Archival (Petabytes, Seconds-Hours)", 1.05, "#475569")
    ]
    
    y = 3.6
    for title, width_factor, color in levels:
        half_w = width_factor * 3.5
        x_left = 4.4 - half_w
        x_right = 4.4 + half_w
        
        poly = patches.Polygon([[x_left, y-0.45], [x_left+0.2, y], [x_right-0.2, y], [x_right, y-0.45]],
                               ec="white", fc=color, lw=1.2)
        ax.add_patch(poly)
        ax.text(4.4, y-0.25, title, ha="center", va="center", color="white", fontsize=7.5, fontweight="bold")
        y -= 0.52
        
    # Side arrows for Speed vs Capacity/Cost
    ax.annotate("", xy=(0.4, 3.6), xytext=(0.4, 0.7), arrowprops=dict(arrowstyle="->", color="#dc2626", lw=2.5))
    ax.text(0.2, 2.15, "Increasing Access Speed\n& Cost per Bit", rotation=90, va="center", ha="center", fontsize=7.5, fontweight="bold", color="#dc2626")
    
    ax.annotate("", xy=(8.4, 0.7), xytext=(8.4, 3.6), arrowprops=dict(arrowstyle="->", color="#059669", lw=2.5))
    ax.text(8.6, 2.15, "Increasing Storage Capacity\n& Latency", rotation=-90, va="center", ha="center", fontsize=7.5, fontweight="bold", color="#059669")
    
    ax.set_xlim(0, 8.8)
    ax.set_ylim(0.3, 4.0)
    ax.axis("off")
    ax.set_title("The Microcomputer Memory Hierarchy: Speed, Capacity, and Cost Trade-offs",
                 fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig2_2_memory_hierarchy_pyramid.png")

# -------------------------------------------------------------
# FIGURE 3.1: PC SECURITY LAYERS
# -------------------------------------------------------------
def build_fig3_1():
    fig, ax = plt.subplots(figsize=(9, 4.3))
    ax.set_facecolor(BG_LIGHT)
    
    layers = [
        ("Layer 1: Physical & Chassis Controls", "Chassis intrusion lock, Kensington security slot, tamper seals, port blockers", "#047857"),
        ("Layer 2: Firmware & Hardware Security", "Power-On Password (POP), BIOS/UEFI Supervisor password, Drive ATA lock", "#0284c7"),
        ("Layer 3: Cryptographic Hardware Root of Trust", "TPM 2.0 (Trusted Platform Module), Secure Boot, BitLocker / LUKS full disk encryption", "#7c3aed"),
        ("Layer 4: Operating System Authentication", "User account login passwords, PINs, Windows Hello biometrics, multi-factor auth (MFA)", "#d97706"),
        ("Layer 5: Access Control & Authorization", "User Account Control (UAC), Principle of Least Privilege, File ACLs, Role separation", "#dc2626")
    ]
    
    y = 3.3
    for title, desc, color in layers:
        rect_title = patches.FancyBboxPatch((0.5, y-0.25), 3.2, 0.55, boxstyle="round,pad=0.06", ec=color, fc=color)
        ax.add_patch(rect_title)
        ax.text(2.1, y, title, ha="center", va="center", color="white", fontsize=8, fontweight="bold")
        
        rect_desc = patches.FancyBboxPatch((3.9, y-0.3), 4.7, 0.65, boxstyle="round,pad=0.06", ec=BORDER_GRAY, fc="white", lw=1.2)
        ax.add_patch(rect_desc)
        ax.text(4.1, y, desc, va="center", color=CHARCOAL, fontsize=7.2)
        
        ax.annotate("", xy=(3.9, y), xytext=(3.7, y), arrowprops=dict(arrowstyle="->", color=color, lw=1.5))
        y -= 0.72
        
    ax.set_xlim(0.2, 8.8)
    ax.set_ylim(0.1, 3.8)
    ax.axis("off")
    ax.set_title("Multi-Layered Defense-in-Depth Personal Computer (PC) Security Architecture",
                 fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig3_1_pc_security_layers.png")

# -------------------------------------------------------------
# FIGURE 4.1: OS ARCHITECTURE LAYERS
# -------------------------------------------------------------
def build_fig4_1():
    fig, ax = plt.subplots(figsize=(8.8, 4.3))
    ax.set_facecolor(BG_LIGHT)
    
    boxes = [
        ("USER APPLICATIONS (Word, Excel, Web Browser, GIS, Python)", 3.4, 0.55, "#0284c7", "white", 8.2),
        ("USER INTERFACE & SHELL (GUI: Windows Explorer, GNOME | CLI: cmd, bash)", 2.65, 0.55, "#059669", "white", 8.0),
        ("SYSTEM CALL INTERFACE (API: Win32, POSIX, open(), read(), fork())", 1.9, 0.55, "#7c3aed", "white", 8.0),
        ("OPERATING SYSTEM KERNEL (Process Mgmt, Memory Paging, File Systems, Drivers)", 1.15, 0.55, SUA_DARK, "white", 8.2),
        ("PHYSICAL HARDWARE (CPU, RAM, Disks, Video Card, Network, Peripherals)", 0.4, 0.55, CHARCOAL, "white", 8.2)
    ]
    
    for title, y, h, bg, fg, fs in boxes:
        rect = patches.FancyBboxPatch((1.0, y-0.25), 6.8, h, boxstyle="round,pad=0.06", ec=bg, fc=bg)
        ax.add_patch(rect)
        ax.text(4.4, y, title, ha="center", va="center", color=fg, fontsize=fs, fontweight="bold")
        
    # Vertical arrows connecting layers
    for y_arr in [3.1, 2.35, 1.6, 0.85]:
        ax.annotate("", xy=(4.4, y_arr-0.2), xytext=(4.4, y_arr+0.1), arrowprops=dict(arrowstyle="<->", color=SUA_GREEN, lw=2))
        
    ax.set_xlim(0.5, 8.3)
    ax.set_ylim(0.1, 3.8)
    ax.axis("off")
    ax.set_title("Hierarchical Layered Operating System Architecture", fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig4_1_os_architecture_layers.png")

# -------------------------------------------------------------
# FIGURE 4.2: PROCESS STATE TRANSITION DIAGRAM
# -------------------------------------------------------------
def build_fig4_2():
    fig, ax = plt.subplots(figsize=(8.8, 4.0))
    ax.set_facecolor(BG_LIGHT)
    
    states = [
        ("NEW", (1.2, 2.0), "#475569"),
        ("READY", (3.2, 2.0), "#0284c7"),
        ("RUNNING", (5.6, 2.0), SUA_GREEN),
        ("TERMINATED", (7.6, 2.0), "#dc2626"),
        ("BLOCKED / WAITING", (4.4, 0.6), "#d97706")
    ]
    
    for name, (x, y), color in states:
        circle = patches.FancyBboxPatch((x-0.7, y-0.35), 1.4, 0.7, boxstyle="round,pad=0.08", ec=color, fc=color)
        ax.add_patch(circle)
        ax.text(x, y, name, ha="center", va="center", color="white", fontsize=8, fontweight="bold")
        
    # Arrows
    # New -> Ready
    ax.annotate("Admitted", xy=(2.5, 2.0), xytext=(1.9, 2.0), arrowprops=dict(arrowstyle="->", color=CHARCOAL, lw=1.5), fontsize=7.2, va="bottom")
    # Ready -> Running
    ax.annotate("Scheduler\nDispatch", xy=(4.9, 2.0), xytext=(3.9, 2.0), arrowprops=dict(arrowstyle="->", color=SUA_GREEN, lw=1.8), fontsize=7.2, va="bottom")
    # Running -> Ready (Interrupt)
    ax.annotate("", xy=(3.2, 2.35), xytext=(5.6, 2.35), arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.5, connectionstyle="arc3,rad=-0.3"))
    ax.text(4.4, 2.8, "Interrupt / Time-slice expired", ha="center", fontsize=7.2, color="#dc2626")
    # Running -> Terminated
    ax.annotate("Exit", xy=(6.9, 2.0), xytext=(6.3, 2.0), arrowprops=dict(arrowstyle="->", color=CHARCOAL, lw=1.5), fontsize=7.2, va="bottom")
    # Running -> Blocked
    ax.annotate("I/O or Event Wait", xy=(5.0, 0.95), xytext=(5.6, 1.65), arrowprops=dict(arrowstyle="->", color="#d97706", lw=1.5), fontsize=7.2)
    # Blocked -> Ready
    ax.annotate("I/O Completion", xy=(3.2, 1.65), xytext=(3.8, 0.95), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=1.5), fontsize=7.2)
    
    ax.set_xlim(0.3, 8.5)
    ax.set_ylim(0.1, 3.2)
    ax.axis("off")
    ax.set_title("Operating System Process State Lifecycle and Transitions", fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig4_2_process_state_transition.png")

# -------------------------------------------------------------
# FIGURE 5.1: SPREADSHEET CELL ADDRESSING
# -------------------------------------------------------------
def build_fig5_1():
    fig, ax = plt.subplots(figsize=(9, 4.0))
    ax.set_facecolor(BG_LIGHT)
    
    types = [
        ("Relative Reference\n=A1 + B1", "When copied down or across, column letters and row numbers change dynamically based on offset.", "#0284c7", 0.6),
        ("Absolute Reference\n=$A$1 * C1", "Both column ($A) and row ($1) are locked with dollar signs; formula always references the fixed cell.", SUA_GREEN, 3.2),
        ("Mixed Reference\n=$A1 + B$2", "Either column is locked ($A1) while row changes, or row is locked (B$2) while column changes.", "#7c3aed", 5.8)
    ]
    
    for title, desc, color, x in types:
        rect_title = patches.FancyBboxPatch((x, 2.3), 2.4, 0.9, boxstyle="round,pad=0.08", ec=color, fc=color)
        ax.add_patch(rect_title)
        ax.text(x+1.2, 2.75, title, ha="center", va="center", color="white", fontsize=8.2, fontweight="bold")
        
        rect_desc = patches.FancyBboxPatch((x, 0.5), 2.4, 1.6, boxstyle="round,pad=0.08", ec=BORDER_GRAY, fc="white", lw=1.2)
        ax.add_patch(rect_desc)
        ax.text(x+1.2, 1.3, desc, ha="center", va="center", color=CHARCOAL, fontsize=7.5, wrap=True)
        
        ax.annotate("", xy=(x+1.2, 2.1), xytext=(x+1.2, 2.3), arrowprops=dict(arrowstyle="->", color=color, lw=1.5))
        
    ax.set_xlim(0.2, 8.8)
    ax.set_ylim(0.2, 3.5)
    ax.axis("off")
    ax.set_title("Spreadsheet Formula Addressing Mechanics: Relative, Absolute, and Mixed",
                 fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig5_1_spreadsheet_addressing.png")

# -------------------------------------------------------------
# FIGURE 5.2: EMAIL PROTOCOLS ARCHITECTURE
# -------------------------------------------------------------
def build_fig5_2():
    fig, ax = plt.subplots(figsize=(9, 4.0))
    ax.set_facecolor(BG_LIGHT)
    
    # Sender MUA
    s_mua = patches.Rectangle((0.5, 1.5), 1.5, 1.2, ec="#0284c7", fc="white", lw=1.5)
    ax.add_patch(s_mua)
    ax.text(1.25, 2.2, "Sender Client\n(MUA)", ha="center", fontsize=8, fontweight="bold", color="#0284c7")
    ax.text(1.25, 1.8, "Outlook, Thunderbird\nWebmail (SUA)", ha="center", fontsize=6.8, color=CHARCOAL)
    
    # Sender SMTP Server
    s_mta = patches.Rectangle((2.8, 1.5), 1.5, 1.2, ec=SUA_GREEN, fc="white", lw=1.5)
    ax.add_patch(s_mta)
    ax.text(3.55, 2.2, "Sending Mail\nServer (MTA)", ha="center", fontsize=8, fontweight="bold", color=SUA_GREEN)
    ax.text(3.55, 1.8, "smtp.sua.ac.tz\nPostfix / Exchange", ha="center", fontsize=6.8, color=CHARCOAL)
    
    # Receiver Mail Server
    r_mta = patches.Rectangle((5.1, 1.5), 1.5, 1.2, ec=SUA_GREEN, fc="white", lw=1.5)
    ax.add_patch(r_mta)
    ax.text(5.85, 2.2, "Receiving Mail\nServer (MDA)", ha="center", fontsize=8, fontweight="bold", color=SUA_GREEN)
    ax.text(5.85, 1.8, "mail.dest.org\nSpam Filter & Spool", ha="center", fontsize=6.8, color=CHARCOAL)
    
    # Receiver MUA
    r_mua = patches.Rectangle((7.3, 1.5), 1.5, 1.2, ec="#7c3aed", fc="white", lw=1.5)
    ax.add_patch(r_mua)
    ax.text(8.05, 2.2, "Recipient Client\n(MUA)", ha="center", fontsize=8, fontweight="bold", color="#7c3aed")
    ax.text(8.05, 1.8, "Smartphones, Laptops\nWebmail Reader", ha="center", fontsize=6.8, color=CHARCOAL)
    
    # Protocol Arrows
    # MUA -> Sending MTA (SMTP submission port 587)
    ax.annotate("", xy=(2.8, 2.1), xytext=(2.0, 2.1), arrowprops=dict(arrowstyle="->", color=SUA_DARK, lw=2))
    ax.text(2.4, 2.3, "SMTP\n(Port 587)", ha="center", fontsize=7.2, fontweight="bold", color=SUA_DARK)
    
    # MTA -> MTA (SMTP relay port 25 via Internet/DNS MX)
    ax.annotate("", xy=(5.1, 2.1), xytext=(4.3, 2.1), arrowprops=dict(arrowstyle="->", color="#dc2626", lw=2))
    ax.text(4.7, 2.3, "SMTP / TLS\n(Port 25)\nInternet DNS MX", ha="center", fontsize=6.8, fontweight="bold", color="#dc2626")
    
    # Receiving MTA -> Recipient MUA (IMAP / POP3)
    ax.annotate("", xy=(7.3, 2.1), xytext=(6.6, 2.1), arrowprops=dict(arrowstyle="->", color="#7c3aed", lw=2))
    ax.text(6.95, 2.3, "IMAP / POP3\n(Port 993/995)", ha="center", fontsize=7.2, fontweight="bold", color="#7c3aed")
    
    ax.set_xlim(0.2, 9.1)
    ax.set_ylim(0.8, 3.2)
    ax.axis("off")
    ax.set_title("End-to-End Internet Electronic Mail (Email) Transport Architecture", fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig5_2_email_protocols_architecture.png")

# -------------------------------------------------------------
# FIGURE 6.1: 3-2-1 BACKUP STRATEGY
# -------------------------------------------------------------
def build_fig6_1():
    fig, ax = plt.subplots(figsize=(8.8, 4.0))
    ax.set_facecolor(BG_LIGHT)
    
    rules = [
        ("3 COPIES OF DATA", "Maintain at least three independent copies of all critical data (1 primary operational working copy + 2 backup replicas).", "#0284c7", 0.5),
        ("2 DIFFERENT MEDIA", "Store backups on at least two distinct storage technologies (e.g., Internal NVMe SSD + External HDD / Optical / NAS).", SUA_GREEN, 3.2),
        ("1 OFFSITE COPY", "Keep at least one backup replica offsite, in a separate physical location or secure cloud repository to survive disasters.", "#dc2626", 5.9)
    ]
    
    for title, desc, color, x in rules:
        rect_title = patches.FancyBboxPatch((x, 2.3), 2.4, 0.8, boxstyle="round,pad=0.08", ec=color, fc=color)
        ax.add_patch(rect_title)
        ax.text(x+1.2, 2.7, title, ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
        
        rect_desc = patches.FancyBboxPatch((x, 0.5), 2.4, 1.6, boxstyle="round,pad=0.08", ec=BORDER_GRAY, fc="white", lw=1.2)
        ax.add_patch(rect_desc)
        ax.text(x+1.2, 1.3, desc, ha="center", va="center", color=CHARCOAL, fontsize=7.5)
        
    ax.set_xlim(0.2, 8.6)
    ax.set_ylim(0.2, 3.5)
    ax.axis("off")
    ax.set_title("The Industry Standard 3-2-1 Data Backup and Disaster Recovery Strategy",
                 fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig6_1_backup_321_rule.png")

# -------------------------------------------------------------
# FIGURE 6.2: MALWARE TAXONOMY
# -------------------------------------------------------------
def build_fig6_2():
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.set_facecolor(BG_LIGHT)
    
    # Root
    root = patches.FancyBboxPatch((3.5, 3.2), 2.0, 0.6, boxstyle="round,pad=0.06", ec=CHARCOAL, fc=CHARCOAL)
    ax.add_patch(root)
    ax.text(4.5, 3.5, "MALICIOUS SOFTWARE\n(MALWARE)", ha="center", va="center", color="white", fontsize=8.2, fontweight="bold")
    
    categories = [
        ("Viruses", "Attaches to host files\nRequires host execution\nInfects other executables", 0.5, "#dc2626"),
        ("Worms", "Self-replicating & standalone\nSpreads over networks\nConsumes bandwidth & memory", 2.2, "#ea580c"),
        ("Trojan Horses", "Disguised as useful software\nOpens stealth backdoors\nDoes not self-replicate", 3.9, "#d97706"),
        ("Ransomware", "Encrypts user files (AES/RSA)\nDemands ransom for key\nExamples: WannaCry, LockBit", 5.6, "#7c3aed"),
        ("Spyware / Rootkits", "Stealth surveillance (keylogs)\nSubverts OS kernel/hypervisor\nConceals process existence", 7.3, "#047857")
    ]
    
    for title, desc, x, color in categories:
        rect_t = patches.FancyBboxPatch((x, 1.9), 1.5, 0.55, boxstyle="round,pad=0.06", ec=color, fc=color)
        ax.add_patch(rect_t)
        ax.text(x+0.75, 2.17, title, ha="center", va="center", color="white", fontsize=7.5, fontweight="bold")
        
        rect_d = patches.FancyBboxPatch((x, 0.4), 1.5, 1.3, boxstyle="round,pad=0.06", ec=BORDER_GRAY, fc="white", lw=1.0)
        ax.add_patch(rect_d)
        ax.text(x+0.75, 1.05, desc, ha="center", va="center", color=CHARCOAL, fontsize=6.8)
        
        # Connecting lines from root
        ax.plot([4.5, x+0.75], [3.2, 2.45], color=BORDER_GRAY, lw=1.2, ls="--")
        
    ax.set_xlim(0.2, 9.1)
    ax.set_ylim(0.1, 4.0)
    ax.axis("off")
    ax.set_title("Taxonomy and Characteristics of Modern Malicious Software (Malware)",
                 fontsize=11, fontweight="bold", color=SUA_DARK)
    save_fig(fig, "fig6_2_malware_taxonomy.png")

if __name__ == "__main__":
    print("Generating all diagrams and schematics for BIT 111...")
    build_fig1_1()
    build_fig1_2()
    build_fig1_3()
    build_fig2_1()
    build_fig2_2()
    build_fig3_1()
    build_fig4_1()
    build_fig4_2()
    build_fig5_1()
    build_fig5_2()
    build_fig6_1()
    build_fig6_2()
    print("All BIT 111 diagrams generated successfully!")
