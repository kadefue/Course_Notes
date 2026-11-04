#!/usr/bin/env python3
"""
slides_part3.py
Slide content definitions for Lectures 7, 8, and 9 (26 slides each).
AEN 214: Introduction to Electronics - Sokoine University of Agriculture.
"""

import os
from pptx import Presentation
from pptx.util import Inches
from build_slides import (
    add_title_slide, add_bullet_slide, add_example_slide,
    add_case_study_slide, add_lab_slide, add_summary_slide, add_review_slide
)

def build_lecture_7_deck(prs):
    lec_num = 7
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Number Systems & Digital Arithmetic",
                    "Binary, Octal, Hexadecimal, Two's Complement, BCD, Gray Codes & Tractor CAN-Bus Telemetry", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 7 Learning Outcomes & Analytical Scope", [
        "Master Positional Radix Systems: Decimal (base 10), Binary (base 2), Octal (base 8), and Hexadecimal (base 16).",
        "Execute Inter-Base Conversion Algorithms: Repeated division/multiplication and direct nibble/byte grouping.",
        "Perform Binary Arithmetic: Multi-bit addition, binary subtraction, binary multiplication, and binary division.",
        "Understand Signed Integer Representation: Signed-magnitude, 1's complement, and 2's complement encoding.",
        "Analyze Two's Complement Subtraction & Overflow: Subtraction via addition, sign bit extension, and hardware overflow detection.",
        "Differentiate Specialized Digital Codes: Binary Coded Decimal (BCD), Excess-3 code, and Reflected Gray code.",
        "Apply Digital Codes to Agriculture: Rotary shaft optical encoders, wind direction vanes, and ISO 11783 (ISOBUS) CAN frames."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "The Digital Domain in Agricultural Engineering", [
        "From Analog Transducers to Digital Bits: Microcontrollers inside tractors, harvesters, and drones compute strictly in binary.",
        "High-Speed In-Field Telemetry: Soil moisture networks, weather stations, and drone LiDAR stream gigabytes of digital words.",
        "Sensor Calibration Precision: ADCs convert physical analog voltages (soil salinity, canopy temperature) into 10-bit or 16-bit binary words.",
        "Precision Harvester Yield Monitors: Optical shaft encoders on grain clean elevators use Gray code to eliminate angular measurement errors.",
        "Standardized Farm Bus Networks: ISO 11783 (ISOBUS) connects tractor displays to implements via hexadecimal CAN-bus message frames."
    ], image_file="img_tractor_electronics.jpg", current_slide=3, total_slides=total)

    # 4. Positional Number Systems Architecture
    add_bullet_slide(prs, "Positional Number Systems: Radix & Positional Weight", [
        "General Radix Formulation: A number N in base r is evaluated by: N = Sum [ d_i · r^i ], where d_i are valid digits (0 <= d_i < r).",
        "Radix-10 (Decimal): Digits {0, 1, ..., 9}; Weights: 10^3 (thousands), 10^2 (hundreds), 10^1 (tens), 10^0 (units), 10^-1 (tenths).",
        "Radix-2 (Binary): Digits {0, 1}; Weights: 2^7 (128), 2^6 (64), 2^5 (32), 2^4 (16), 2^3 (8), 2^2 (4), 2^1 (2), 2^0 (1).",
        "Radix-8 (Octal): Digits {0, 1, 2, 3, 4, 5, 6, 7}; Used for compact human representation of 3-bit binary clusters.",
        "Radix-16 (Hexadecimal): Digits {0–9, A, B, C, D, E, F}; Used for byte-level human representation (1 Hex digit = exactly 4 binary bits)."
    ], image_file="fig7_1_number_systems_hierarchy.png", current_slide=4, total_slides=total)

    # 5. Inter-Base Conversion Algorithms
    add_bullet_slide(prs, "Inter-Base Conversion Algorithms", [
        "Decimal-to-Binary Integer Conversion: Successive division by 2; remainders read from bottom (MSB) to top (LSB).",
        "Decimal-to-Binary Fractional Conversion: Successive multiplication by 2; integer carries read from top to bottom.",
        "Direct Binary-to-Hexadecimal Mapping: Group binary bits into clusters of 4 (nibbles) starting from binary point; replace with Hex digit.",
        "Direct Hexadecimal-to-Binary Mapping: Expand each individual Hex digit into its equivalent 4-bit binary nibble.",
        "Octal Conversions: Group binary bits into clusters of 3; each octal digit corresponds exactly to 3 binary bits (e.g. 7_8 = 111_2)."
    ], current_slide=5, total_slides=total)

    # 6. Binary Addition & Subtraction
    add_bullet_slide(prs, "Fundamental Binary Arithmetic Operations", [
        "Binary Addition Axioms: 0 + 0 = 0; 0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 0 with Carry of 1 (10_2); 1 + 1 + 1 = 1 with Carry of 1 (11_2).",
        "Columnar Multi-Bit Addition: Add bit pairs along with incoming carry bit; propagate carry to next higher significance bit.",
        "Binary Subtraction Axioms: 0 - 0 = 0; 1 - 0 = 1; 1 - 1 = 0; 0 - 1 = 1 with Borrow of 1 from adjacent higher bit.",
        "Hardware Disadvantage of Subtraction: Building separate binary subtractor circuits with borrow logic requires complex, bulky hardware.",
        "The Complement Solution: Digital microprocessors perform all subtractions using addition via **Two's Complement** arithmetic!"
    ], current_slide=6, total_slides=total)

    # 7. Signed Integer Representations
    add_bullet_slide(prs, "Signed Integer Representations: Sign-Magnitude to 2's Complement", [
        "Signed-Magnitude Representation: Most Significant Bit (MSB) is sign bit (0 = Positive, 1 = Negative); remaining bits are magnitude.",
        "Sign-Magnitude Flaws: Two distinct zeros (+0 and -0) confuse ALU comparison logic; requires separate adder and subtractor hardware.",
        "One's Complement: Invert every bit of the number (0 -> 1, 1 -> 0); still suffers from dual zeros (+0 = 0000_2, -0 = 1111_2).",
        "Two's Complement: Invert every bit (1's complement) and ADD 1: B_{2's} = /B + 1.",
        "Two's Complement Supremacy: Has a unique zero (00000000_2); allows addition and subtraction to use the EXACT same adder hardware!",
        "Dynamic Range for N bits: -2^(N-1) to + (2^(N-1) - 1). For 8 bits: -128 to +127."
    ], image_file="fig7_2_twos_complement_circle.png", current_slide=7, total_slides=total)

    # 8. Two's Complement Subtraction & Arithmetic Overflow
    add_bullet_slide(prs, "Two's Complement Subtraction & Overflow Detection", [
        "Subtraction Rule: To compute A - B, calculate: Result = A + B_{2's} = A + (/B + 1).",
        "End-Around Carry Rule: Any carry bit generated beyond the MSB is simply discarded; the remaining N bits are the mathematically correct result.",
        "Arithmetic Overflow Hazard: Occurs when the result of adding two numbers exceeds the representable dynamic range of the N-bit register.",
        "Overflow Conditions: Adding two positive numbers yields a negative result (MSB = 1), OR adding two negative numbers yields a positive result (MSB = 0).",
        "Hardware Overflow Detection Rule: An overflow occurs if and only if: C_in(MSB) XOR C_out(MSB) = 1 (Carry into MSB differs from carry out).",
        "ALU Flag: Microcontroller hardware automatically sets the 'V' (Overflow) status flag, triggering software safety traps."
    ], current_slide=8, total_slides=total)

    # 9. Worked Example 1: Signed 2's Complement Subtraction
    add_example_slide(prs, 1, "Signed Two's Complement Subtraction with Overflow Check",
                      "A digital fertilizer injection rate computer on a Massey Ferguson tractor calculates difference Delta Q = Q_actual - Q_target in 8-bit signed two's complement. If actual delivery is Q_actual = +58 Liters/ha and target is Q_target = +85 Liters/ha: (a) Express +58 and +85 in 8-bit binary, (b) Find the two's complement of +85, (c) Perform the subtraction via addition (58 - 85), (d) Check for arithmetic overflow.",
                      [
                          "1. Convert to 8-Bit Binary:",
                          "   • +58 = 32 + 16 + 8 + 2 = 00111010_2.",
                          "   • +85 = 64 + 16 + 4 + 1 = 01010101_2.",
                          "2. Form Two's Complement of +85 (-85):",
                          "   • Take 1's complement: Invert bits of 01010101_2 -> 10101010_2.",
                          "   • Add 1: 10101010_2 + 1 = 10101011_2 (Represents -85 in 2's complement).",
                          "3. Execute Addition (A + B_{2's}):",
                          "     00111010  (+58)",
                          "   + 10101011  (-85)",
                          "   = 11100101",
                          "4. Verify Magnitude & Sign of Result (11100101_2):",
                          "   • MSB is '1', indicating a negative quantity.",
                          "   • Invert and add 1 to find magnitude: 11100101 -> 00011010 + 1 = 00011011_2 = 16 + 8 + 2 + 1 = 27_10.",
                          "   • Result = -27 Liters/ha (Correct: 58 - 85 = -27).",
                          "5. Overflow Check: Adding positive (+58) and negative (-85) numbers CANNOT cause overflow; C_in(MSB)=0, C_out(MSB)=0 -> V=0."
                      ], current_slide=9, total_slides=total)

    # 10. Binary Coded Decimal (BCD)
    add_bullet_slide(prs, "Binary Coded Decimal (BCD 8421 Code)", [
        "Concept: Encodes each decimal digit (0 through 9) into its separate 4-bit binary equivalent.",
        "Direct Decimal Mapping: 0=0000, 1=0001, 2=0010, ..., 8=1000, 9=1001. Digits 1010_2 through 1111_2 (10 to 15) are INVALID BCD states.",
        "Agricultural Instrument Displays: Used in weighing scales, digital grain moisture meters, and milking parlor rate displays.",
        "BCD Addition Rule: Add standard binary nibbles. If a nibble sum exceeds 9 (1001_2) OR if a nibble carry occurs: ADD 6 (0110_2) to correct!",
        "BCD Correction Mechanics: Adding 6 skips the 6 invalid 4-bit states, forcing the correct decimal carry into the next higher decade.",
        "Packed vs Unpacked BCD: Packed BCD stores two decimal digits per 8-bit byte (e.g. '74' = 0111 0100_2); maximizes memory density."
    ], current_slide=10, total_slides=total)

    # 11. Gray Code & Shaft Optical Encoders
    add_bullet_slide(prs, "Unit-Distance Reflected Gray Code & Optical Encoders", [
        "The Race Condition Vulnerability: In standard binary, advancing from 3 (011_2) to 4 (100_2) requires THREE bits to change simultaneously.",
        "Mechanical Alignment Skew: Mechanical tolerances cause bits to switch at slightly different nanoseconds, producing momentary false readings (e.g. 7 or 0).",
        "The Gray Code Solution: Unit-distance code where adjacent numerical values differ by **EXACTLY ONE BIT** throughout the entire sequence.",
        "Binary-to-Gray Conversion Algorithm: Gray MSB = Binary MSB; Subsequent Gray bits: G_i = B_i XOR B_{i+1}.",
        "Gray-to-Binary Conversion Algorithm: Binary MSB = Gray MSB; Subsequent Binary bits: B_i = B_{i+1} XOR G_i.",
        "Tractor & Combine Encoders: Mandatory for optical shaft encoders measuring wheel steering angle and combine threshing cylinder speed."
    ], current_slide=11, total_slides=total)

    # 12. Worked Example 2: Gray Code Shaft Encoder
    add_example_slide(prs, 2, "Binary-to-Gray Conversion for Combine Harvester Header",
                      "An absolute optical shaft encoder monitoring the cutterbar tilt angle on a combine harvester in Morogoro outputs an 8-bit position word. At a critical tilt angle, the raw binary reading is B = 10110110_2 (182_10). To prevent race-condition glitch errors during fast tilting: (a) Convert binary word B to its 8-bit Gray code G, (b) Demonstrate the single-bit transition property if the tilt increments to B = 10110111_2 (183_10).",
                      [
                          "1. Binary Word: B = B_7 B_6 B_5 B_4 B_3 B_2 B_1 B_0 = 1 0 1 1 0 1 1 0_2.",
                          "2. Apply Binary-to-Gray Formula (G_i = B_i XOR B_{i+1}; G_7 = B_7):",
                          "   • G_7 = B_7 = 1",
                          "   • G_6 = B_7 XOR B_6 = 1 XOR 0 = 1",
                          "   • G_5 = B_6 XOR B_5 = 0 XOR 1 = 1",
                          "   • G_4 = B_5 XOR B_4 = 1 XOR 1 = 0",
                          "   • G_3 = B_4 XOR B_3 = 1 XOR 0 = 1",
                          "   • G_2 = B_3 XOR B_2 = 0 XOR 1 = 1",
                          "   • G_1 = B_2 XOR B_1 = 1 XOR 1 = 0",
                          "   • G_0 = B_1 XOR B_0 = 1 XOR 0 = 1",
                          "   Gray Code Result G = 11101101_Gray.",
                          "3. Next Increment B = 10110111_2 (183_10):",
                          "   • G_0 = B_1 XOR B_0 = 1 XOR 1 = 0 (only bit G_0 flips from 1 to 0!).",
                          "   • All other 7 bits remain identical: G_next = 11101100_Gray.",
                          "4. Verification: Exactly ONE bit toggled during the numerical increment; eliminates mechanical contact race errors completely."
                      ], current_slide=12, total_slides=total)

    # 13. Alphanumeric Codes: ASCII & Unicode
    add_bullet_slide(prs, "Alphanumeric Coding: ASCII, UTF-8 & Farm Telemetry", [
        "American Standard Code for Information Interchange (ASCII): 7-bit binary code representing 128 characters (letters, numbers, control symbols).",
        "ASCII Structure: '0' to '9' = 30_16 to 39_16; 'A' to 'Z' = 41_16 to 5A_16; 'a' to 'z' = 61_16 to 7A_16.",
        "Control Characters: CR (Carriage Return = 0D_16), LF (Line Feed = 0A_16), ACK (Acknowledge = 06_16), NAK (Negative Ack = 15_16).",
        "NMEA 0183 GPS Strings: Precision farming GPS receivers output ASCII sentences (e.g. '$GPGGA,...') over serial UART at 9,600 baud.",
        "Extended ASCII & UTF-8: 8-bit to 32-bit encodings supporting international characters and engineering symbols (e.g. °C, micro, Ohm)."
    ], current_slide=13, total_slides=total)

    # 14. ISO 11783 (ISOBUS) & Tractor CAN-Bus
    add_bullet_slide(prs, "ISO 11783 (ISOBUS) & Controller Area Network (CAN)", [
        "The Agricultural Bus Standard: Standardizes electronic communication between tractors and mounted implements (sprayers, seeders, balers).",
        "Physical Layer: Differential voltage bus (CAN_H, CAN_L) operating at 250 kbps; twisted-pair with 120 Ohm termination resistors.",
        "29-Bit Extended CAN Identifier: Structured into Priority (3 bits), Parameter Group Number (PGN, 18 bits), and Source Address (8 bits).",
        "Parameter Group Numbers (PGNs): Hexadecimal identifiers defining data payload (e.g. PGN 65265 / 00FEF1_16 = Vehicle Speed & Distance).",
        "Universal Terminal (UT): Allows any implement ECU to upload its graphical user interface directly to the virtual terminal in the tractor cab."
    ], current_slide=14, total_slides=total)

    # 15. Worked Example 3: ISO 11783 CAN-Bus Decoding
    add_example_slide(prs, 3, "Decoding ISO 11783 (ISOBUS) Tractor Wheel Speed",
                      "An autonomous tractor ISOBUS CAN-bus datalogger captures a vehicle speed message frame with raw Hexadecimal payload: [ 4E 1F 00 00 FF FF FF FF ]. According to ISO 11783-7, Bytes 1 and 2 represent Wheel-Based Vehicle Speed encoded as a 16-bit unsigned integer with Little-Endian byte order (Least Significant Byte first), with a resolution of 1/1000 km/h per bit (0.001 km/h/bit) and zero offset. Calculate: (a) 16-bit hexadecimal speed word, (b) Decimal equivalent integer, (c) Tractor forward ground speed in km/h.",
                      [
                          "1. Extract Bytes 1 and 2 from Payload: Byte 1 = 4E_16, Byte 2 = 1F_16.",
                          "2. Assemble Little-Endian 16-Bit Word (LSB first -> Byte 2 is MSB, Byte 1 is LSB):",
                          "   Raw Hex Word = 1F 4E_16.",
                          "3. Convert Hexadecimal to Decimal Integer:",
                          "   • 1F4E_16 = (1 · 16^3) + (15 · 16^2) + (4 · 16^1) + (14 · 16^0).",
                          "   • = (1 · 4,096) + (15 · 256) + (4 · 16) + (14 · 1) = 4,096 + 3,840 + 64 + 14 = 8,014_10.",
                          "4. Apply ISOBUS Physical Scaling Factor (0.001 km/h per bit):",
                          "   Tractor Speed = Raw Integer · Scaling Factor = 8,014 · 0.001 km/h = 8.014 km/h.",
                          "5. Agronomic Verification: 8.01 km/h is the optimal forward operating speed for tractor-mounted boom sprayers in weed control."
                      ], current_slide=15, total_slides=total)

    # 16. Error Detection: Parity & Cyclic Redundancy Checks (CRC)
    add_bullet_slide(prs, "Digital Error Detection: Parity & CRC in Farm Telemetry", [
        "Transmission Noise in Fields: High-power ignition noise and electric motor surges corrupt data bits on wireless farm telemetry links.",
        "Parity Bit: Appends a single bit to make total number of 1s either even (Even Parity) or odd (Odd Parity); detects single-bit errors.",
        "Parity Limitation: Fails to detect double-bit errors (e.g. two 0s flipped to 1s); inadequate for safety-critical tractor controls.",
        "Cyclic Redundancy Check (CRC): Treats data stream as a binary polynomial; divides by generator polynomial G(x) using modulo-2 arithmetic.",
        "CRC-15 in ISOBUS CAN: 15-bit CRC checksum appends to every CAN frame; detects burst errors up to 15 bits with 99.9999% reliability.",
        "Automatic Retransmission: If receiver CRC mismatch occurs, CAN hardware automatically drops frame and requests immediate retransmission."
    ], current_slide=16, total_slides=total)

    # 17. Fixed-Point vs Floating-Point Number Systems
    add_bullet_slide(prs, "Fixed-Point vs Floating-Point in Ag Microcontrollers", [
        "Integer Microcontrollers: Low-cost 8-bit and 32-bit microcontrollers (e.g. ATmega328P, Cortex-M0) lack hardware Floating Point Units (FPUs).",
        "Floating-Point Penalty: Software floating-point emulation requires hundreds of CPU clock cycles, choking real-time sensor loops.",
        "Q-Format Fixed-Point Arithmetic: Binary point is fixed at a predetermined position; e.g. Q4.12 stores 4 integer bits and 12 fractional bits.",
        "Integer Scaling: Represent soil moisture (0.00% to 100.00%) as an integer scaled by 100 (0 to 10,000 counts); executes at single-cycle speed.",
        "IEEE 754 Floating-Point: Standard 32-bit single precision (1 sign bit, 8 exponent bits, 23 mantissa bits); used in high-end tractor autopilot GPS."
    ], current_slide=17, total_slides=total)

    # 18. Microcontroller ADC Quantization
    add_bullet_slide(prs, "Analog-to-Digital Conversion (ADC) Quantization", [
        "Continuous to Discrete: ADC samples continuous analog sensor voltages and quantizes them into N-bit discrete binary numbers.",
        "Resolution (Quantization Step Size Q): Q = V_ref / (2^N - 1) ≈ V_ref / 2^N (Volts/count).",
        "10-Bit ADC (e.g. Arduino): 2^10 = 1,024 levels. For V_ref = 5.0 V, step size Q = 5.0 V / 1,024 = 4.883 mV.",
        "12-Bit ADC (e.g. STM32, ESP32): 2^12 = 4,096 levels. For V_ref = 3.3 V, step size Q = 3.3 V / 4,096 = 0.8057 mV.",
        "Quantization Error: Inherent uncertainty of ± 0.5 Q; Can only be reduced by increasing ADC bit depth N.",
        "ADC Binary Output Word: Digital Code D = round[ (V_in / V_ref) · (2^N - 1) ]."
    ], current_slide=18, total_slides=total)

    # 19. Practical Field Hardening for Digital Buses
    add_bullet_slide(prs, "Hardening Digital Busses Against Agricultural EMI", [
        "Differential Signaling: CAN_H and CAN_L transmit inverted voltages; common-mode noise couples equally to both and is rejected by receiver.",
        "Shielded Twisted Pair (STP): 120 Ohm characteristic impedance cable prevents transmission line reflections; grounded foil shields EMI.",
        "Split Termination: Two 60 Ohm resistors with center-tap capacitor (4.7 nF to ground) suppress high-frequency common-mode noise.",
        "Opto-Isolated CAN Transceivers: Isolates 24V tractor electrical transients from sensitive 3.3V autopilot microcontroller boards.",
        "ESD Diode Arrays: PESD2CAN protection diodes clamp ±30 kV electrostatic discharges from dry grain augers and operators."
    ], current_slide=19, total_slides=total)

    # 20. Case Study 1
    add_case_study_slide(prs, 1, "Gray Code Optical Encoder Header Height Control",
                         "Kilombero Sugar Estate Sugarcane Combine Mechanization, Tanzania",
                         "Modern sugarcane combine harvesters operating at Kilombero experienced intermittent violent header gouging into the soil. At specific crop height positions, the cutterbar suddenly slammed into the ground, breaking tungsten blades and costing 8,500 USD in blade replacements and downtime.",
                         "SUA agricultural engineers logged the raw 8-bit binary shaft encoder attached to the hydraulic height linkage. When the linkage transitioned from position 127 (01111111_2) to 128 (10000000_2), all eight bits were required to change state simultaneously. Mechanical vibration caused bit 7 to switch 18 microseconds ahead of the rest, creating a transient reading of 255 (full height), causing the ECU to slam the header down! Engineers replaced the sensor with an 8-bit Gray code encoder.",
                         [
                             "Completely eliminated cutterbar gouging glitches; zero broken blades across two seasons.",
                             "Transition race condition eliminated since only ONE bit changes between adjacent states.",
                             "Saved an estimated 32,000 USD in cutter blades, gearboxes, and harvester downtime."
                         ], current_slide=20, total_slides=total)

    # 21. Case Study 2
    add_case_study_slide(prs, 2, "ISOBUS Telemetry Failure in Precision Rice Seeding",
                         "Mbarali Paddy Scheme Mechanized Seed Drilling, Mbeya, Tanzania",
                         "A precision 16-row pneumatic rice seed drill linked to a New Holland tractor cab terminal via ISO 11783 CAN-bus suffered intermittent seed metering cutoffs. The cab monitor displayed erroneous seed population drops, causing operators to unnecessarily halt planting in prime weather.",
                         "Engineers discovered that the implement ECU was running an 8-bit microcontroller using software floating-point emulation to calculate seed spacing in meters. When seed metering frequency surpassed 80 pulses/second, floating-point execution delays triggered CAN buffer overruns, dropping vehicle speed message frames. Engineers converted all seed rate mathematics to 16-bit Q8.8 fixed-point integer arithmetic.",
                         [
                             "Seeding calculation execution time plummeted from 4.2 ms to 14 microseconds.",
                             "CAN message frame loss dropped to 0.000%, eliminating all nuisance cab alarms.",
                             "Seed planting uniformity reached 98.6% across 220 hectares of paddy fields."
                         ], current_slide=21, total_slides=total)

    # 22. Laboratory Bench Protocol
    add_lab_slide(prs, "Binary Conversions & Logic Analyzer CAN-Bus Protocol", [
        "Execute manual and computerized radix conversions between Binary, Hexadecimal, and BCD.",
        "Demonstrate 2's complement signed integer addition and verify arithmetic overflow flag on ALU.",
        "Capture Gray code shaft optical encoder output transitions on 8-channel logic analyzer.",
        "Decode raw Hexadecimal CAN-bus message packets captured from an agricultural tractor simulator."
    ], [
        "Step 1: Write C program implementing integer-to-hexadecimal and 2's complement algorithms on Arduino UNO.",
        "Step 2: Inject test additions (+120 + +15; -90 + -50); verify signed result and observe status register overflow flag.",
        "Step 3: Connect optical rotary shaft encoder to breadboard; attach 8-channel USB logic analyzer to data outputs.",
        "Step 4: Rotate encoder slowly; capture state transitions; verify that exactly one bit changes per angular increment.",
        "Step 5: Connect CAN transceiver module to PC; transmit ISOBUS frame; decode PGN and data payload in Wireshark."
    ], current_slide=22, total_slides=total)

    # 23. Troubleshooting & Pitfalls
    add_bullet_slide(prs, "Diagnostic Troubleshooting in Digital Number Systems", [
        "Arithmetic Overflow Ignored: Failing to check the overflow status bit results in large positive quantities turning negative (e.g. +127 + 1 = -128).",
        "Sign Extension Failure: Converting an 8-bit negative signed integer (e.g. 11110000_2) to 16-bit requires sign extension (11111111 11110000_2).",
        "Endianness Confusion: Big-Endian stores MSB first; Little-Endian stores LSB first (e.g. CAN bus, x86); swapping bytes corrupts telemetry data.",
        "Invalid BCD States: Feeding binary values 10 through 15 into a BCD display driver (74LS47) produces corrupted garbled display segments.",
        "Missing CAN Bus Termination: Omitting the 120 Ohm termination resistors at bus ends causes transmission line reflections, corrupting data frames."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "Convert decimal number 347.625_10 into its exact equivalent in: (a) Binary, (b) Octal, (c) Hexadecimal.",
        "Represent -68_10 as an 8-bit signed integer using: (a) Signed-magnitude, (b) One's complement, (c) Two's complement.",
        "Perform the subtraction 45_10 - 78_10 using 8-bit two's complement arithmetic and verify the result.",
        "Explain why Gray code is preferred over standard binary code in agricultural rotary position encoders.",
        "A 12-bit ADC has an analog input range of 0.0 V to 3.3 V. Calculate the digital output code when V_in = 2.15 V."
    ], "Lecture 8 will explore Introduction to Digital Electronics: Logic gates (AND, OR, NOT, NAND, NOR, XOR), universal synthesis, and flip-flops.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "Digital agricultural electronics operate in binary (base 2); Hexadecimal provides compact 4-bit byte representation.",
        "Two's complement is the universal signed integer standard, enabling addition and subtraction on the exact same hardware.",
        "Arithmetic overflow occurs when adding two like-signed numbers produces a result of the opposite sign (C_in != C_out).",
        "Gray code changes only ONE bit per step, eliminating race conditions in optical shaft encoders.",
        "ISO 11783 (ISOBUS) standardizes tractor-implement digital communication using 29-bit CAN identifiers and Hex payloads."
    ], [
        "Radix Value: N = Sum [ d_i · r^i ]",
        "Two's Complement: B_{2's} = /B + 1",
        "Subtraction via Addition: A - B = A + (/B + 1)",
        "Overflow Condition: V = C_in(MSB) XOR C_out(MSB)",
        "Binary to Gray: G_i = B_i XOR B_{i+1}; G_MSB = B_MSB",
        "ADC Step Size: Q = V_ref / (2^N - 1)",
        "CAN Termination: R_term = 120 Ohm at both bus ends"
    ], current_slide=25, total_slides=total)

    # 26. References & Reading List
    add_bullet_slide(prs, "Prescribed References & Practical Laboratory Preparation", [
        "Mano, M. M., & Ciletti, M. D. (2017). Digital Design: With an Introduction to Verilog HDL (6th ed.). Pearson.",
        "Floyd, T. L. (2015). Digital Fundamentals (11th ed.). Pearson.",
        "ISO 11783: Tractors and machinery for agriculture and forestry — Serial control and communications data network (ISOBUS).",
        "Laboratory Preparation: Review hexadecimal nibble grouping and truth tables before attending Lab Session 7.",
        "Field Assignment: Complete Assignment 3, Questions 1 to 4 on number systems and CAN-bus telemetry."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

def build_lecture_8_deck(prs):
    lec_num = 8
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Introduction to Digital Electronics",
                    "Logic Gates, Universal Gate Synthesis, Propagation Delay, Adders, Subtractors & Latches", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 8 Learning Outcomes & Combinational Scope", [
        "Master Primary Logic Gates: Analyze truth tables, Boolean expressions, and IEEE symbols for AND, OR, and NOT gates.",
        "Evaluate Secondary & Universal Gates: NAND, NOR, XOR, and XNOR gate operations and parity testing.",
        "Synthesize Universal Gate Circuits: Implement NOT, AND, OR, NOR, and XOR using purely NAND or purely NOR gates.",
        "Analyze Digital Electrical Parameters: Propagation delay t_pd, rise/fall times, noise margins, and power dissipation.",
        "Design Combinational Arithmetic Circuits: Half Adder, Full Adder, Ripple Carry Adder, and Half/Full Subtractors.",
        "Implement Multi-Condition Agricultural Interlocks: Greenhouse climate control, grain elevator safety, and pump priming.",
        "Introduce Sequential Logic Elements: Bistable multivibrators, active-LOW SR latches, and switch debouncers."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "Digital Logic in Agricultural Machinery Automation", [
        "The Decision-Making Core: Logic gates form the hardware decision engine of every farm machinery safety and control system.",
        "Fail-Safe Hardware Interlocks: Hardwired logic guarantees emergency shutdown of grain augers even if software crashes.",
        "Real-Time Response: Discrete hardware logic gates respond in nanoseconds, preventing mechanical operator injury.",
        "Universal Gate Flexibility: Remote farm workshops can replace any damaged logic chip using abundant 74LS00 Quad NAND ICs.",
        "Combinational Sensor Processing: Combines inputs from soil moisture, ambient humidity, and wind speed into pump commands."
    ], image_file="img_logic_gates_ic.jpg", current_slide=3, total_slides=total)

    # 4. Definition of a Logic Gate & Logic Levels
    add_bullet_slide(prs, "Definition of a Logic Gate & Voltage Thresholds", [
        "Definition: An electronic circuit with one or more binary inputs and a single binary output that executes a Boolean logical function.",
        "Binary Voltage Abstraction: Digital circuits map continuous electrical voltages into discrete binary logic states: Logic 0 (LOW) and Logic 1 (HIGH).",
        "TTL Voltage Standards (5V Supply): V_IL(max) = 0.8 V, V_IH(min) = 2.0 V, V_OL(max) = 0.4 V, V_OH(min) = 2.4 V.",
        "CMOS Voltage Standards (5V Supply): V_IL(max) = 1.5 V, V_IH(min) = 3.5 V, V_OL(max) = 0.05 V, V_OH(min) = 4.95 V.",
        "Indeterminate Zone: Voltages between V_IL and V_IH are invalid; gates may oscillate or draw excessive current in this region."
    ], current_slide=4, total_slides=total)

    # 5. Primary Logic Gates: AND, OR, NOT
    add_bullet_slide(prs, "Primary Logic Gates: AND, OR, and Inverter (NOT)", [
        "AND Gate: Output is HIGH if and only if ALL inputs are HIGH: Y = A · B. Equivalent to series electrical contacts.",
        "OR Gate: Output is HIGH if ANY input is HIGH: Y = A + B. Equivalent to parallel electrical contacts.",
        "NOT Gate (Inverter): Output is the exact opposite of the input: Y = /A. Single-input logic negation.",
        "Truth Tables: Mathematical matrices listing all 2^N possible binary input combinations and resulting output states.",
        "IEEE Distinctive Shape Symbols: AND has flat input face with curved output; OR has curved input face with pointed output; NOT is triangle with bubble."
    ], image_file="fig8_1_standard_logic_gates.png", current_slide=5, total_slides=total)

    # 6. Secondary Logic Gates: NAND, NOR, XOR, XNOR
    add_bullet_slide(prs, "Secondary Logic Gates: NAND, NOR, XOR, and XNOR", [
        "NAND Gate (NOT-AND): AND followed by an inverter: Y = /(A · B). Output is LOW only when ALL inputs are HIGH.",
        "NOR Gate (NOT-OR): OR followed by an inverter: Y = /(A + B). Output is HIGH only when ALL inputs are LOW.",
        "XOR Gate (Exclusive-OR): Output is HIGH when inputs are DIFFERENT: Y = A ⊕ B = /A·B + A·/B. Senses parity and inequalities.",
        "XNOR Gate (Exclusive-NOR): Output is HIGH when inputs are IDENTICAL: Y = /(A ⊕ B) = A·B + /A·/B. Digital magnitude comparator.",
        "Active-LOW Bubbles: Inversion bubbles at inputs or outputs denote active-LOW signal polarity."
    ], current_slide=6, total_slides=total)

    # 7. The Universal NAND Gate
    add_bullet_slide(prs, "The Universal NAND Gate: Complete Functional Completeness", [
        "Functional Completeness: Any Boolean logic expression can be implemented using NOTHING but 2-input NAND gates!",
        "Synthesizing an INVERTER: Tie both inputs of a NAND gate together: Y = /(A · A) = /A.",
        "Synthesizing an AND Gate: Follow a NAND gate with an Inverter: Y = / ( /(A · B) ) = A · B (Requires 2 NAND gates).",
        "Synthesizing an OR Gate: Invert inputs A and B before feeding into NAND: Y = /( /A · /B ) = //A + //B = A + B (via De Morgan; 3 NAND gates).",
        "Synthesizing a NOR Gate: Follow the synthesized OR gate with an inverter: Y = /(A + B) (Requires 4 NAND gates).",
        "Agricultural Supply Chain Impact: Technicians need to stock only 74LS00 or CD4011 Quad 2-input NAND ICs to repair any farm logic board!"
    ], current_slide=7, total_slides=total)

    # 8. The Universal NOR Gate
    add_bullet_slide(prs, "The Universal NOR Gate: Functional Completeness", [
        "Universal NOR Architecture: Dual to the NAND gate; any Boolean expression can be realized using NOR gates alone.",
        "Synthesizing an INVERTER: Tie both inputs of a NOR gate together: Y = /(A + A) = /A.",
        "Synthesizing an OR Gate: Follow a NOR gate with a NOR inverter: Y = / ( /(A + B) ) = A + B (Requires 2 NOR gates).",
        "Synthesizing an AND Gate: Invert inputs before feeding into NOR: Y = /( /A + /B ) = //A · //B = A · B (via De Morgan; 3 NOR gates).",
        "Synthesizing a NAND Gate: Follow the synthesized AND gate with an inverter: Y = /(A · B) (Requires 4 NOR gates).",
        "Silicon Fab Preference: In CMOS technology, NAND gates are faster than NOR gates due to high electron mobility in N-channel pull-down networks."
    ], current_slide=8, total_slides=total)

    # 9. Dynamic Timing: Propagation Delay & Noise Margins
    add_bullet_slide(prs, "Digital Dynamic Parameters & Noise Margins", [
        "Propagation Delay (t_pd): Finite time elapsed between input transition and output response; t_pd = 0.5 · (t_pLH + t_pHL) (typically 5 to 30 ns).",
        "Rise Time (t_r) & Fall Time (t_f): Time required for output voltage to transition between 10% and 90% of steady-state logic levels.",
        "High-State Noise Margin: NM_H = V_OH(min) - V_IH(min). For standard TTL: NM_H = 2.4V - 2.0V = 0.40 V.",
        "Low-State Noise Margin: NM_L = V_IL(max) - V_OL(max). For standard TTL: NM_L = 0.8V - 0.4V = 0.40 V.",
        "CMOS Superiority: CMOS noise margins approach 30% to 40% of supply voltage (NM ≈ 1.5V at 5V V_DD); vastly superior in noisy farm environments!"
    ], current_slide=9, total_slides=total)

    # 10. Worked Example 1: Universal NAND Synthesis
    add_example_slide(prs, 1, "Universal NAND Realization of Dairy Milk Vat Interlock",
                      "A dairy milk chilling tank agitator motor in Arusha operates according to Boolean logic: Y = A · B + /C, where A = Milk Level Normal, B = Temperature Above 4°C, and C = Tank Wash Cycle Active. To simplify spares inventory, the farm workshop manager insists on building the entire circuit using standard 74HC00 Quad 2-Input NAND ICs. (a) Express Y using only NAND operators via De Morgan's theorem, (b) Draw the NAND gate interconnection, (c) Determine the minimum number of 74HC00 ICs required.",
                      [
                          "1. Apply Double Negation (Involution): Y = //( A · B + /C ).",
                          "2. Apply De Morgan's Law to Inner Expression: / ( (A · B) + /C ) = /(A · B) · //C = /(A · B) · C.",
                          "3. Complete Inverted Expression: Y = / [ /(A · B) · C ].",
                          "4. Verify NAND Realization:",
                          "   • Gate 1 (2-input NAND): Inputs A and B -> Output X_1 = /(A · B).",
                          "   • Gate 2 (2-input NAND): Inputs X_1 and C -> Output Y = / [ X_1 · C ] = / [ /(A · B) · C ] = A · B + /C.",
                          "5. Circuit Gate Count & Package Requirement:",
                          "   • Total 2-input NAND gates required = EXACTLY TWO GATES!",
                          "   • A single 74HC00 IC contains FOUR independent 2-input NAND gates.",
                          "   • Exactly ONE 74HC00 IC is required, with two spare gates available for future automation expansion."
                      ], current_slide=10, total_slides=total)

    # 11. Combinational Arithmetic: The Half Adder
    add_bullet_slide(prs, "Combinational Arithmetic: The Half Adder", [
        "Circuit Function: Adds two single-bit binary inputs (A and B) and produces a Sum bit (S) and an outgoing Carry bit (C).",
        "Truth Table Analysis: S is HIGH when inputs differ (0+1=1, 1+0=1); C is HIGH only when both inputs are 1 (1+1=0, Carry 1).",
        "Boolean Formulations: Sum: S = A ⊕ B = /A·B + A·/B; Carry: C = A · B.",
        "Hardware Implementation: Synthesized using exactly one 2-input XOR gate (for Sum) and one 2-input AND gate (for Carry).",
        "Half Adder Limitation: Lacks an incoming carry input (C_in); cannot be cascaded to add multi-bit binary numbers."
    ], current_slide=11, total_slides=total)

    # 12. Combinational Arithmetic: The Full Adder
    add_bullet_slide(prs, "Combinational Arithmetic: The Full Adder", [
        "Circuit Function: Adds three single-bit inputs: operands A and B, plus incoming carry C_in from previous lower stage.",
        "Full Adder Boolean Equations: Sum: S = A ⊕ B ⊕ C_in; Outgoing Carry: C_out = A · B + C_in · (A ⊕ B).",
        "Two-Half-Adder Architecture: Full adder is synthesized by cascading two Half Adders and an OR gate.",
        "Half Adder 1: S_1 = A ⊕ B; C_1 = A · B.",
        "Half Adder 2: S = S_1 ⊕ C_in = (A ⊕ B) ⊕ C_in; C_2 = S_1 · C_in = (A ⊕ B) · C_in.",
        "Final Carry: C_out = C_1 + C_2 = A · B + (A ⊕ B) · C_in.",
        "Transistor Count: CMOS transmission gate full adder requires only 28 transistors."
    ], image_file="fig8_3_half_full_adder_circuits.png", current_slide=12, total_slides=total)

    # 13. Parallel Binary Ripple-Carry Adder
    add_bullet_slide(prs, "Parallel Multi-Bit Ripple-Carry Adder (74LS283)", [
        "N-Bit Parallel Adder: Cascades N Full Adder stages in series to add two N-bit binary words simultaneously.",
        "Carry Propagation Path: Outgoing carry C_out of stage k connects directly to incoming carry C_in of stage k+1.",
        "The Ripple-Carry Bottleneck: Most Significant Bit sum (S_N-1) cannot be computed until the carry ripples through all preceding N stages!",
        "Total Addition Delay: t_total = (N - 1) · t_carry + max(t_carry, t_sum); For 32 bits at 10 ns/stage, delay reaches 320 ns.",
        "Carry Lookahead Adder (CLA): Fast adder that pre-computes carries in parallel using Generate (G = A·B) and Propagate (P = A+B) logic."
    ], current_slide=13, total_slides=total)

    # 14. Binary Subtractors: Half & Full Subtractors
    add_bullet_slide(prs, "Binary Subtractors: Half & Full Subtractor Circuits", [
        "Half Subtractor: Subtracts single-bit subtrahend B from minuend A, producing Difference (D) and Borrow-out (B_out).",
        "Half Subtractor Equations: Difference: D = A ⊕ B; Borrow-out: B_out = /A · B.",
        "Full Subtractor: Computes A - B - B_in, taking into account incoming borrow B_in from lower significant bit.",
        "Full Subtractor Equations: Difference: D = A ⊕ B ⊕ B_in; Borrow-out: B_out = /A · B + B_in · /(A ⊕ B).",
        "Adder-Subtractor Combined Circuit: Place XOR gates on input B lines controlled by mode signal M (M=0 -> Add; M=1 -> 2's Complement Subtract!)."
    ], current_slide=14, total_slides=total)

    # 15. Worked Example 2: Ripple-Carry Adder Propagation Delay
    add_example_slide(prs, 2, "Propagation Delay Analysis in Tractor Autopilot Adder",
                      "An autonomous tractor GPS navigation controller utilizes an 8-bit parallel ripple-carry adder (cascaded 74HC283 full adders) to compute real-time coordinate offsets. Datasheet timing specifications: Carry-in to Carry-out propagation delay t_carry = 12.0 ns; Carry-in to Sum bit delay t_sum = 16.0 ns; Operand input (A, B) to Carry-out delay t_gate = 18.0 ns. Determine: (a) Total time required to generate the final MSB carry C_8, (b) Total time required for all 8 sum bits to settle into valid steady state, (c) Maximum operating clock frequency of the ALU.",
                      [
                          "1. Time to Generate Final Carry C_8: Stage 0 generates C_1 from operands A_0, B_0 in t_gate. Subsequent 7 stages ripple carry through t_carry.",
                          "   t_C8 = t_gate + (8 - 1) · t_carry = 18.0 ns + (7 · 12.0 ns) = 18.0 ns + 84.0 ns = 102.0 ns.",
                          "2. Time for All Sum Bits to Settle Validly:",
                          "   • Sum bits S_0 through S_6 settle earlier.",
                          "   • Final sum bit S_7 settles after carry arrives at stage 7 plus the carry-to-sum delay: t_settle = t_gate + (8 - 2) · t_carry + t_sum.",
                          "   t_settle = 18.0 ns + (6 · 12.0 ns) + 16.0 ns = 18.0 + 72.0 + 16.0 = 106.0 ns.",
                          "3. Worst-Case Computational Latency: Total settling latency t_max = max(t_C8, t_settle) = 106.0 ns.",
                          "4. Maximum ALU Clock Frequency: f_max = 1 / t_max = 1 / (106.0 x 10^-9 s) = 9.434 x 10^6 Hz = 9.43 MHz.",
                          "5. Engineering Assessment: To achieve 50 MHz autopilot processing, the design must upgrade from ripple-carry to a Carry-Lookahead Adder (CLA)."
                      ], current_slide=15, total_slides=total)

    # 16. Agricultural Combinational Logic Design
    add_bullet_slide(prs, "Multi-Sensor Combinational Control in Greenhouses", [
        "Autonomous Greenhouse Climate Controller: Regulates evaporative cooling pad pumps, exhaust fans, and motorized ridge vents.",
        "Sensor Inputs: Temperature High (T: > 32°C), Humidity Low (H: < 50%), Solar Radiation High (S: > 800 W/m²), Wind High (W: > 40 km/h).",
        "Control Output: Evaporative Cooling Pump (P): Activate when temperature is high, humidity is low, AND wind is not dangerous.",
        "Boolean Function Synthesis: P = T · /H · /W; Ridge vents must close automatically during severe winds: V_close = W + /T · /S.",
        "Hardware Realization: Hardwired logic gate networks execute safety shutdowns without depending on microcontroller firmware."
    ], image_file="fig8_4_greenhouse_ventilation_system.png", current_slide=16, total_slides=total)

    # 17. Worked Example 3: Grain Elevator Safety Interlock
    add_example_slide(prs, 3, "Fail-Safe Combinational Logic for Grain Silo Conveyor",
                      "Design a fail-safe digital interlock circuit for a 50-tonne/hour vertical bucket elevator at the Morogoro grain storage depot. The elevator drive motor must START (Y = 1) only if ALL of the following safety conditions are satisfied: (1) Main emergency stop pushbutton is ARMED (E = 1), (2) Discharge chute is CLEAR of grain blockage (C = 1), and (3) EITHER the Manual Start button is pressed (M = 1) OR the Automated Bin Level Controller requests fill (A = 1). In addition, if the Belt Slip sensor detects belt slippage (S = 1), the motor must IMMEDIATELY TRIP (Y = 0) regardless of all other inputs. (a) Formulate the Boolean expression, (b) Synthesize using standard logic gates.",
                      [
                          "1. Analyze Safety Conditions & Assign Variables: Motor runs (Y = 1) if: E = 1, C = 1, (M = 1 OR A = 1), and S = 0 (Slip absent).",
                          "2. Formulate Boolean Logic Expression: Y = E · C · (M + A) · /S.",
                          "3. Gate Synthesis Strategy:",
                          "   • Stage 1 (OR gate): Inputs M and A -> Output X_1 = (M + A).",
                          "   • Stage 2 (Inverter): Input S -> Output X_2 = /S.",
                          "   • Stage 3 (4-input AND gate): Inputs E, C, X_1, X_2 -> Output Y = E · C · (M + A) · /S.",
                          "4. Alternative All-NAND Synthesis: Apply De Morgan: Y = / [ /(E · C) + /X_1 + S ].",
                          "5. Fail-Safe Wiring: Emergency Stop (E) is wired normally-closed (NC) so that a severed wire automatically trips E = 0, halting the conveyor!"
                      ], current_slide=17, total_slides=total)

    # 18. Introduction to Sequential Logic: The SR Latch
    add_bullet_slide(prs, "Introduction to Sequential Logic: The Bistable SR Latch", [
        "Combinational vs Sequential: Combinational outputs depend strictly on present inputs; Sequential outputs depend on present inputs AND past history (memory).",
        "Active-LOW NAND SR Latch: Cross-coupled 2-input NAND gates with active-LOW inputs /Set (/S) and /Reset (/R).",
        "Operating States: /S=0, /R=1 -> Set (Q=1); /S=1, /R=0 -> Reset (Q=0); /S=1, /R=1 -> Hold / Memory (Q remains unchanged).",
        "Forbidden (Invalid) State: /S=0, /R=0 forces both Q=1 and /Q=1; violating complementary output definition; causes race when released.",
        "Mechanical Switch Debouncing: Mechanical pushbuttons bounce for 5 to 20 ms, generating dozens of false digital clock pulses.",
        "SR Debouncer Action: An SPDT switch with an SR latch latches cleanly on first contact bounce, providing a single pristine digital pulse."
    ], current_slide=18, total_slides=total)

    # 19. Practical Agro-Environment Protection
    add_bullet_slide(prs, "Hardening Digital Logic in Harsh Farm Environments", [
        "Unused Input Pin Rule: NEVER leave CMOS logic input pins floating (acts as high-impedance antenna, picking up EMI and causing gate latchup).",
        "Pull-up and Pull-down Resistors: Terminate all unused CMOS inputs solidly to V_DD or GND via 10 kOhm resistors.",
        "Power Rail Decoupling: Place a 0.1 microFarad ceramic capacitor directly adjacent to the V_CC pin of every single logic IC on the PCB.",
        "Inductive Suppression: Farm relays driven by logic outputs must have flyback diodes and optical isolators to block 500V kickbacks.",
        "Schmitt-Trigger Inputs: Specify 74HC14 or 74HCT14 Schmitt-trigger inverters on all external sensor lines to clean up slow, noisy edge transitions."
    ], current_slide=19, total_slides=total)

    # 20. Case Study 1
    add_case_study_slide(prs, 1, "Switch Debouncing Failure in Dairy Milking Pulsator",
                         "Msolwa Dairy Farm Automated Milking Parlor, Kilombero, Tanzania",
                         "Automated dairy milking units featured digital pulse counters to measure individual cow milk yield via a tipping-bucket mechanism (50 ml per tip). The digital counters registered over 300% false milk yield, reading 45 liters per cow instead of 12 liters and corrupting dairy management breeding records.",
                         "SUA engineers hooked a digital oscilloscope to the mechanical magnetic reed switch on the tipping bucket. Oscilloscope traces revealed severe contact bounce: each physical bucket tip generated 8 to 14 electrical bounces spanning 12 milliseconds. The high-speed digital counter registered every single bounce as an independent 50 ml delivery. Engineers installed an active-LOW cross-coupled NAND SR latch (74HC00) debouncer.",
                         [
                             "Completely eliminated contact bounce; exactly ONE pulse registered per mechanical tip.",
                             "Milk measurement accuracy restored to within ±0.5% of verified weight.",
                             "Saved the cooperative over 16,000 USD in misallocated nutritional feed supplements."
                         ], current_slide=20, total_slides=total)

    # 21. Case Study 2
    add_case_study_slide(prs, 2, "Fail-Safe Logic Interlock for Grain Silo Deflagration",
                         "National Food Reserve Agency (NFRA) Complex, Morogoro, Tanzania",
                         "Grain elevators handle dry maize that generates explosive organic dust clouds. A bucket elevator leg bearing overheated to 180°C, igniting suspended corn dust and blowing off explosion relief panels. The PLC software loop lagged by 1.2 seconds, failing to shut off the feed auger in time.",
                         "Engineers bypassed the software PLC for critical life-safety functions, installing a dedicated hardwired combinational logic tripping network using MIL-spec 74LS series gates. The circuit inputs: Bearing Temperature Sensor (B), Belt Alignment Sensor (A), Motor Current Overload (I), and Fire Suppression Pressure (P). The hardwired circuit trips the 100A main vacuum contactor within 18 nanoseconds of limit exceedance.",
                         [
                             "Emergency tripping response time accelerated from 1.2 seconds down to 18 nanoseconds.",
                             "Successfully halted feed auger during a subsequent bearing failure, preventing an explosion.",
                             "Earned full safety compliance certification from OSHA Tanzania."
                         ], current_slide=21, total_slides=total)

    # 22. Laboratory Bench Protocol
    add_lab_slide(prs, "Digital Logic Gates & Universal Synthesis Bench Protocol", [
        "Verify truth tables of 74LS08 (AND), 74LS32 (OR), 74LS04 (NOT), and 74LS00 (NAND) ICs on breadboard.",
        "Synthesize an OR gate and an XOR gate using purely 74LS00 Quad 2-Input NAND gates.",
        "Assemble a Half Adder circuit using 74LS86 (XOR) and 74LS08 (AND) and verify Sum and Carry truth table.",
        "Build a switch debouncer using cross-coupled NAND gates and observe bounce suppression on DSO."
    ], [
        "Step 1: Insert 74LS00, 74LS08, 74LS86 ICs onto breadboard. Connect Pin 14 to +5.0V and Pin 7 to GND. Add 0.1 uF decoupling caps.",
        "Step 2: Connect input switches to logic 0 (GND) and logic 1 (+5V). Connect gate outputs to red LEDs with 330 Ohm resistors.",
        "Step 3: Sweep all 4 input combinations; record output LED states; verify manufacturer truth tables.",
        "Step 4: Wire the Universal NAND circuit for Y = A + B (3 NAND gates); prove that output matches standard OR gate.",
        "Step 5: Connect noisy mechanical pushbutton to DSO Channel 1 (unbounced); connect SR latch output to Channel 2; observe debouncing."
    ], current_slide=22, total_slides=total)

    # 23. Troubleshooting & Pitfalls
    add_bullet_slide(prs, "Diagnostic Troubleshooting of Digital Logic Circuits", [
        "Floating CMOS Inputs: Leaving unused CMOS gates open causes intense power supply oscillations and random switching; tie all inputs.",
        "Missing V_CC or Ground Pin: IC may appear to partially function via parasitic input clamping diodes, but exhibits erratic, corrupted outputs.",
        "Excessive Fan-Out Loading: Connecting too many gate inputs to a single output exceeds I_OL / I_OH ratings; voltage levels degrade into invalid zone.",
        "Propagation Delay Race Hazards: Unequal signal propagation paths cause momentary false glitch pulses ('glitches'); add consensus gates.",
        "Reversed IC Orientation: Inserting a DIP-14 IC backwards (pin 1 where pin 14 belongs) connects V_CC to GND, destroying chip instantly."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "Define an active-LOW logic signal and explain why open-collector / open-drain buses utilize active-LOW signaling.",
        "Prove algebraically and draw the schematic showing how a 2-input XOR gate is synthesized using exactly four 2-input NAND gates.",
        "Differentiate between a Half Adder and a Full Adder. Why is a Half Adder insufficient for adding multi-bit binary words?",
        "Explain the cause of the ripple-carry bottleneck in a parallel adder, and describe how Carry Lookahead logic solves it.",
        "Why is mechanical switch debouncing mandatory in agricultural electronic counters, and how does an SR latch eliminate bounce?"
    ], "Lecture 9 will explore Boolean Algebra & Karnaugh Maps: Axioms, De Morgan's laws, SOP/POS, K-map minimization, and static hazards.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "Logic gates execute binary Boolean decisions based on well-defined voltage threshold levels (TTL vs CMOS).",
        "NAND and NOR gates are functionally complete universal gates capable of synthesizing any logic function.",
        "Propagation delay (t_pd) sets the fundamental upper limit on digital processing speed and clock frequencies.",
        "Full Adders combine two Half Adders and an OR gate to add three bits including incoming carry C_in.",
        "Bistable SR latches store one bit of digital memory and provide perfect bounce-free mechanical switch pulses."
    ], [
        "AND Gate: Y = A · B; OR Gate: Y = A + B",
        "NAND Gate: Y = /(A · B); NOR Gate: Y = /(A + B)",
        "XOR Gate: Y = A ⊕ B = /A·B + A·/B",
        "Universal NAND Inverter: /A = /(A · A)",
        "Universal NAND OR: A + B = /( /A · /B )",
        "Half Adder: S = A ⊕ B; C = A · B",
        "Full Adder: S = A ⊕ B ⊕ C_in; C_out = AB + C_in(A ⊕ B)"
    ], current_slide=25, total_slides=total)

    # 26. References & Reading List
    add_bullet_slide(prs, "Prescribed References & Practical Laboratory Preparation", [
        "Mano, M. M., & Ciletti, M. D. (2018). Digital Design: With an Introduction to Verilog HDL (6th ed.). Pearson.",
        "Floyd, T. L. (2015). Digital Fundamentals (11th ed.). Pearson.",
        "Karim, M. A., & Chen, X. (2017). Digital Design: Basic Concepts and Principles. CRC Press.",
        "Laboratory Preparation: Review DIP-14 pinout diagrams (74LS00, 74LS08, 74LS32, 74LS86) before Lab Session 8.",
        "Field Assignment: Complete Assignment 3, Questions 5 to 8 on logic gate synthesis and full adder circuits."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

def build_lecture_9_deck(prs):
    lec_num = 9
    total = 26

    # 1. Title
    add_title_slide(prs, lec_num, "Boolean Algebra & Karnaugh Maps",
                    "Axioms, De Morgan's Theorems, Canonical SOP/POS, 2/3/4-Variable K-Maps, Don't-Cares & Glitch Elimination", 1, total)

    # 2. Objectives
    add_bullet_slide(prs, "Lecture 9 Learning Outcomes & Optimization Scope", [
        "Master Boolean Axioms & Theorems: Identity, Null, Idempotent, Involution, Complementarity, and Absorption laws.",
        "Apply the Principle of Duality: Dual transformations of Boolean identities and equivalent electrical contact networks.",
        "Prove De Morgan's Laws: Rigorous mathematical induction and algebraic expansion across multi-variable expressions.",
        "Evaluate Canonical & Standard Forms: Canonical Sum-of-Products (minterms m_i) and Product-of-Sums (maxterms M_i).",
        "Construct Karnaugh Maps (K-Maps): 2-variable, 3-variable, and 4-variable maps labeled in Gray code sequence.",
        "Extract Minimal SOP/POS Equations: Toroidal wrap-around adjacency, corner quads, Essential Prime Implicants (EPIs).",
        "Exploit Don't-Care Conditions (X / d): Optimize BCD alarms and eliminate Static-1 hazards using consensus product terms."
    ], current_slide=2, total_slides=total)

    # 3. Agricultural Motivation
    add_bullet_slide(prs, "Logic Minimization in Commercial Agriculture", [
        "Reducing Silicon Cost & Power: Unsimplified logic requires dozens of gate ICs; minimized logic fits in a single low-power chip.",
        "Accelerating Machine Response: Fewer cascaded gate levels reduce total propagation delay, enabling faster emergency braking.",
        "Improving Vibration Reliability: Every unneeded IC package eliminated removes 14 solder joints that could crack on vibrating tractors.",
        "Exploiting Impossible States (Don't-Cares): Agricultural sensors have physical constraints (e.g. BCD values 10-15 never occur).",
        "Eliminating Safety Glitches: Static-1 hazards cause momentary false sensor trips, dumping hydraulic fluid or stopping irrigation pumps."
    ], image_file="img_grain_silo.jpg", current_slide=3, total_slides=total)

    # 4. Foundations of Boolean Algebra & Axioms
    add_bullet_slide(prs, "Foundations of Boolean Algebra: Axioms & Postulates", [
        "Huntington's Postulates: Mathematical algebraic system defined over set B = {0, 1} with two binary operators: AND (·) and OR (+).",
        "Closure: For all A, B in {0, 1}: A · B in {0, 1} and A + B in {0, 1}.",
        "Identity Elements: Identity for OR is 0: A + 0 = A; Identity for AND is 1: A · 1 = A.",
        "Commutative Laws: A + B = B + A; A · B = B · A (Order of operands does not affect logical result).",
        "Distributive Laws: A · (B + C) = (A · B) + (A · C); AND distributes over OR.",
        "Second Distributive Law: A + (B · C) = (A + B) · (A + C); OR distributes over AND (Unique to Boolean algebra!).",
        "Complementarity Laws: A + /A = 1; A · /A = 0."
    ], current_slide=4, total_slides=total)

    # 5. Core Boolean Algebraic Theorems
    add_bullet_slide(prs, "Core Boolean Algebraic Theorems & Laws", [
        "Idempotent Laws: A + A = A; A · A = A (Combining identical terms yields no change).",
        "Null (Dominance) Laws: A + 1 = 1; A · 0 = 0 (Dominant elements overwrite variable).",
        "Involution Law (Double Negation): //A = A.",
        "Associative Laws: (A + B) + C = A + (B + C); (A · B) · C = A · (B · C).",
        "Absorption (Redundancy) Laws: A + (A · B) = A; A · (A + B) = A; A + (/A · B) = A + B.",
        "Consensus Theorem: A · B + /A · C + B · C = A · B + /A · C (The redundant term B · C can be eliminated!).",
        "Principle of Duality: Any true Boolean identity remains true if: (1) AND and OR are swapped, and (2) 0 and 1 are swapped."
    ], current_slide=5, total_slides=total)

    # 6. De Morgan's Theorems & Switching Duality
    add_bullet_slide(prs, "De Morgan's Theorems & Electrical Switching Circuits", [
        "First Law: The complement of a product equals the sum of the complements: /(A · B) = /A + /B.",
        "Second Law: The complement of a sum equals the product of the complements: /(A + B) = /A · /B.",
        "Generalized N-Variable Form: /(X_1 · X_2 · ... · X_N) = /X_1 + /X_2 + ... + /X_N.",
        "Series-Parallel Switching Duality: Two normally-closed contacts in series break circuit if EITHER opens: /(A + B) = /A · /B.",
        "Gate Transformation Rule: A NAND gate is logically equivalent to a Negative-OR gate (OR with inverted inputs).",
        "Gate Transformation Rule: A NOR gate is logically equivalent to a Negative-AND gate (AND with inverted inputs)."
    ], image_file="fig9_1_demorgan_switching_circuits.png", current_slide=6, total_slides=total)

    # 7. Canonical Forms: Minterms & Maxterms
    add_bullet_slide(prs, "Canonical Boolean Forms: Minterms & Maxterms", [
        "Minterm (Standard Product Term, m_i): A product term containing EVERY system variable exactly once in either true or complemented form.",
        "Minterm Evaluation: A minterm produces logic '1' for exactly ONE row of the truth table (e.g. for row 101_2: m_5 = A · /B · C).",
        "Canonical Sum-of-Products (SOP): The logical OR of all minterms for which output Y = 1: Y = Sum m(1, 3, 5, 7).",
        "Maxterm (Standard Sum Term, M_i): A sum term containing EVERY system variable exactly once in either true or complemented form.",
        "Maxterm Evaluation: A maxterm produces logic '0' for exactly ONE row of the truth table (e.g. for row 010_2: M_2 = A + /B + C).",
        "Canonical Product-of-Sums (POS): The logical AND of all maxterms for which output Y = 0: Y = Prod M(0, 2, 4, 6).",
        "Complementary Relationship: Sum m(List_1) = Prod M(List_2), where List_1 and List_2 partition all 2^N rows."
    ], current_slide=7, total_slides=total)

    # 8. The Karnaugh Map (K-Map) Architecture
    add_bullet_slide(prs, "The Karnaugh Map: Geometric 2D Adjacency", [
        "Visual Minimization Matrix: A 2D graphical representation of a truth table where logical adjacency corresponds to physical geometric adjacency.",
        "Gray Code Labeling: Adjacent row and column coordinates are ordered in Gray code: 00, 01, 11, 10 (NEVER standard binary 00, 01, 10, 11!).",
        "The Unit-Distance Property: Moving one cell horizontally or vertically changes EXACTLY ONE binary variable (e.g. 01 to 11 changes only bit 1).",
        "Cell Count: An N-variable K-map contains exactly 2^N cells (2-var = 4 cells; 3-var = 8 cells; 4-var = 16 cells).",
        "Toroidal Topology: The K-map is geometrically continuous (a torus); the top edge wraps to bottom edge, and left edge wraps to right edge!"
    ], image_file="fig9_2_kmap_configurations.png", current_slide=8, total_slides=total)

    # 9. K-Map Grouping Rules
    add_bullet_slide(prs, "Rigorous K-Map Grouping (Implicant) Rules", [
        "Rule 1 (Power of 2): Groups must contain a number of cells that is a power of 2: 1 (single), 2 (pair), 4 (quad), 8 (octet), 16 (hexadecet).",
        "Rule 2 (Rectangular Geometry): Groups must form solid rectangles or squares; diagonal or L-shaped groupings are strictly forbidden.",
        "Rule 3 (Variable Elimination): Combining 2 cells eliminates 1 variable; 4 cells eliminates 2 variables; 8 cells eliminates 3 variables!",
        "Rule 4 (Maximal Group Size): Always form the LARGEST possible groups first; larger groups yield simpler terms with fewer literals.",
        "Rule 5 (Overlapping Groups): 1-cells may be shared by multiple groups if doing so enlarges adjacent groups.",
        "Rule 6 (Essential Prime Implicants): A group is an EPI if it covers at least one '1' that is not covered by any other group; MUST be included."
    ], current_slide=9, total_slides=total)

    # 10. Worked Example 1: 3-Variable K-Map Minimization
    add_example_slide(prs, 1, "3-Variable K-Map Minimization for Drip Irrigation Pump",
                      "A solar-powered drip irrigation pump at Kilombero Sugar nursery operates according to 3 binary sensor inputs: Reservoir Water Available (A), Soil Moisture Deficit (B), and Solar Irradiance High (C). The truth table defines the pump enable function as: Y(A, B, C) = Sum m( 1, 3, 4, 5, 6, 7 ). (a) Plot the minterms on an 8-cell Karnaugh map, (b) Form the maximal groups of 1-cells, (c) Determine the essential prime implicants and write the minimal SOP expression.",
                      [
                          "1. Construct 3-Variable K-Map (Row A [0, 1]; Columns BC [00, 01, 11, 10]):",
                          "   • Row A=0: Cell 0=0, Cell 1=1, Cell 3=1, Cell 2=0.",
                          "   • Row A=1: Cell 4=1, Cell 5=1, Cell 7=1, Cell 6=1.",
                          "2. Identify Maximal Groups of 1-cells:",
                          "   • Group 1 (Entire Row A=1): Cells (4, 5, 7, 6). Variables B and C vary through (00, 01, 11, 10), while A remains constant at 1.",
                          "     Reduced Product Term 1 = **A** (eliminates 2 variables: B and C).",
                          "   • Group 2 (Quad of 4): Columns BC=01 and BC=11 across both rows (Cells 1, 3, 5, 7). Variable A varies (0 and 1), B varies (0 and 1), while C remains constant at 1.",
                          "     Reduced Product Term 2 = **C** (eliminates 2 variables: A and B).",
                          "3. Completeness Check: All six 1-cells (1, 3, 4, 5, 6, 7) are completely covered by Group 1 and Group 2.",
                          "4. Final Minimal SOP Expression: **Y = A + C**.",
                          "5. Hardware Impact: The raw canonical expression required six 3-input AND gates and one 6-input OR gate (25 transistors). The K-map minimized it to a single 2-input OR gate (6 transistors)—a 76% hardware reduction!"
                      ], current_slide=10, total_slides=total)

    # 11. 4-Variable K-Maps: Corner & Toroidal Adjacencies
    add_bullet_slide(prs, "4-Variable K-Maps: Corner & Toroidal Wrap-Around", [
        "16-Cell Architecture: Rows labeled AB [00, 01, 11, 10]; Columns labeled CD [00, 01, 11, 10].",
        "Toroidal Edge Adjacencies: Row 00 is adjacent to Row 10 (top to bottom); Column 00 is adjacent to Column 10 (left to right).",
        "The Four-Corner Quad: Cells (0, 2, 8, 10) form a valid, highly efficient Quad of 4!",
        "Elimination Across 4 Corners: Across rows 00 and 10: A varies, B=0 (/B). Across columns 00 and 10: C varies, D=0 (/D).",
        "Reduced Corner Term: The four corners combine into the compact product term: **/B · /D**.",
        "Center 2x2 Quad: Cells (5, 7, 13, 15) combine into product term: **B · D**."
    ], current_slide=11, total_slides=total)

    # 12. Worked Example 2: 4-Variable K-Map with Corner Wrap
    add_example_slide(prs, 2, "4-Variable K-Map Minimization for Greenhouse Climate Fan",
                      "An automated greenhouse climate controller in Morogoro monitors 4 binary sensors: Temperature High (A), Humidity High (B), Light High (C), and CO2 Low (D). The exhaust ventilation fan function is defined by: F(A, B, C, D) = Sum m( 0, 2, 5, 7, 8, 10, 13, 15 ). (a) Populate the 16-cell K-map, (b) Identify the toroidal wrap-around and center groups, (c) Extract the minimal SOP expression, (d) Express in XOR/XNOR logic.",
                      [
                          "1. Populate 16-Cell K-Map (Rows AB, Columns CD):",
                          "   • Row AB=00: Cell 0=1, Cell 1=0, Cell 3=0, Cell 2=1.",
                          "   • Row AB=01: Cell 4=0, Cell 5=1, Cell 7=1, Cell 6=0.",
                          "   • Row AB=11: Cell 12=0, Cell 13=1, Cell 15=1, Cell 14=0.",
                          "   • Row AB=10: Cell 8=1, Cell 9=0, Cell 11=0, Cell 10=1.",
                          "2. Form Maximal Groups:",
                          "   • Group 1 (Four Corners): Cells (0, 2, 8, 10).",
                          "     - Rows 00 & 10: A cancels (0 and 1), B remains 0 -> /B.",
                          "     - Columns 00 & 10: C cancels (0 and 1), D remains 0 -> /D.",
                          "     - Reduced Term 1 = **/B · /D**.",
                          "   • Group 2 (Center 2x2 Quad): Cells (5, 7, 13, 15).",
                          "     - Rows 01 & 11: A cancels, B remains 1 -> B.",
                          "     - Columns 01 & 11: C cancels, D remains 1 -> D.",
                          "     - Reduced Term 2 = **B · D**.",
                          "3. Minimal SOP Expression: **F = /B · /D + B · D**.",
                          "4. Gate Realization: Notice that /B·/D + B·D is the exact definition of Exclusive-NOR! **F = /(B ⊕ D)**.",
                          "5. Brilliant Hardware Simplification: The complex 4-sensor system simplifies to a single 2-input XNOR gate comparing B and D!"
                      ], current_slide=12, total_slides=total)

    # 13. Don't-Care Conditions (d / X)
    add_bullet_slide(prs, "Don't-Care Conditions (d / X) in Digital Design", [
        "Physical Origin: Input combinations that can NEVER physically occur due to hardware constraints, or whose output is irrelevant.",
        "BCD Illegal States: In 4-bit Binary Coded Decimal, inputs 1010_2 through 1111_2 (10 to 15) are illegal; their outputs are Don't-Cares.",
        "K-Map Optimization Rule: Treat Don't-Care cells (X) as '1' IF doing so enlarges a group; treat them as '0' if they do not help.",
        "No Obligation Rule: You are NEVER obligated to cover a Don't-Care cell; only cover them if they enlarge valid 1-cell groups.",
        "Hardware Benefit: Incorporating Don't-Cares frequently allows pairs to become quads, and quads to become octets, cutting gate count by > 50%!"
    ], current_slide=13, total_slides=total)

    # 14. Worked Example 3: BCD Grain Scale with Don't-Cares
    add_example_slide(prs, 3, "Exploiting Don't-Cares for BCD Grain Moisture Scale Alarm",
                      "A digital grain moisture scale at Morogoro NFRA depot outputs a 4-bit BCD digit (bits A, B, C, D where A is MSB). An alarm must trip (Y = 1) if moisture exceeds safe thresholds, corresponding to decimal digits 7, 8, 9: Y = Sum m( 7, 8, 9 ). Input combinations 10 through 15 are invalid BCD states: d = Sum d( 10, 11, 12, 13, 14, 15 ). (a) Minimize WITHOUT Don't-Cares, (b) Minimize WITH Don't-Cares, (c) Compare resulting hardware complexity.",
                      [
                          "1. Case A: Minimization WITHOUT Don't-Cares (treat all X as 0):",
                          "   • Cell 7 (0111_2) cannot combine with 8 or 9: Isolated cell -> Term = /A · B · C · D.",
                          "   • Cells 8 (1000_2) and 9 (1001_2) form a Pair of 2 in Row 10 -> Term = A · /B · /C.",
                          "   • Resulting Expression: Y = /A · B · C · D + A · /B · /C (Requires two complex 4-input/3-input AND gates and 1 OR gate).",
                          "2. Case B: Minimization WITH Don't-Cares (X at 10, 11, 12, 13, 14, 15):",
                          "   • Row 10 (cells 8, 9, 11, 10) and Row 11 (cells 12, 13, 15, 14) can be combined into a massive **Octet of 8 cells** (8, 9, 10, 11, 12, 13, 14, 15)!",
                          "     In this octet, B, C, D all cancel; only A=1 remains constant. Reduced Term 1 = **A**.",
                          "   • Cell 7 (0111_2): Combine with adjacent Don't-Care cell 15 (1111_2) to form a **Pair of 2**.",
                          "     Across cells 7 and 15, A cancels (0 and 1); B=1, C=1, D=1 remain constant. Reduced Term 2 = **B · C · D**.",
                          "3. Final Minimal SOP Expression: **Y = A + B · C · D**.",
                          "4. Hardware Comparison: Using Don't-Cares eliminated one 4-input gate and two inverters, cutting gate count by 60%!"
                      ], current_slide=14, total_slides=total)

    # 15. Product-of-Sums (POS) Maxterm Minimization
    add_bullet_slide(prs, "Product-of-Sums (POS) Maxterm K-Map Minimization", [
        "Maxterm Grouping Strategy: Group the **0-cells (maxterms)** on the K-map instead of the 1-cells!",
        "Coordinate Inversion Rule: In POS form, a variable value of 0 represents the TRUE literal, and 1 represents the COMPLEMENTED literal.",
        "Sum Term Extraction: For a group of 0-cells where variable X = 0 -> include literal (X); where variable X = 1 -> include literal (/X).",
        "Final POS Expression: The logical product (AND) of all extracted sum terms: Y = (A + B) · (C + /D).",
        "Hardware Advantage: When a truth table contains significantly fewer 0s than 1s, POS minimization yields a drastically simpler circuit."
    ], current_slide=15, total_slides=total)

    # 16. Hazards in Combinational Logic: Static-1 Hazards
    add_bullet_slide(prs, "Hazards & Glitches in Combinational Logic", [
        "The Hazard Definition: A transient temporary false output pulse ('glitch') caused by unequal gate propagation delays during an input transition.",
        "Static-1 Hazard: Output is theoretically supposed to remain constant at 1, but momentarily dips to 0 for several nanoseconds (1 -> 0 -> 1).",
        "Static-0 Hazard: Output is supposed to remain constant at 0, but momentarily spikes to 1 (0 -> 1 -> 0).",
        "Dynamic Hazard: Output transitions three or more times during a single input transition (e.g. 0 -> 1 -> 0 -> 1).",
        "Agricultural Hazard Consequence: A 10 ns glitch on an emergency brake line trips tractor hydraulic valves or resets seed counters!"
    ], current_slide=16, total_slides=total)

    # 17. Hazard Detection on K-Maps & Consensus Elimination
    add_bullet_slide(prs, "Hazard Detection on K-Maps & Consensus Elimination", [
        "Visual Hazard Rule: A static hazard exists if and only if two adjacent 1-cells on the K-map are covered by **different (separate) groups** without an overlap.",
        "The Propagation Race: When the input variable transitions between those adjacent cells, one AND gate turns OFF slightly before the other turns ON.",
        "Momentary Dropout: For a window of 5–15 ns, BOTH AND gates output 0 simultaneously, causing the OR gate output to glitch to 0.",
        "Hazard Elimination via Consensus Terms: Add an intentionally redundant **Consensus Product Term** covering the boundary between the two groups.",
        "Fail-Safe Holding Action: Although algebraically redundant in steady state, the consensus gate remains firmly ON during the transition, holding output steadily at 1!"
    ], current_slide=17, total_slides=total)

    # 18. Five-Variable K-Maps (Split-Plane Minimization)
    add_bullet_slide(prs, "Five-Variable K-Maps: Dual 16-Cell Overlay Architecture", [
        "32-Cell Architecture: A 5-variable function (A, B, C, D, E) contains 2^5 = 32 minterms; mapped onto two identical 16-cell sub-maps side-by-side.",
        "Plane A = 0 (Left Plane): Cells 0 through 15; variables BCDE.",
        "Plane A = 1 (Right Plane): Cells 16 through 31; variables BCDE.",
        "3D Inter-Plane Adjacency Rule: Cells are adjacent within each 16-cell plane AND they are **3D-adjacent** between planes if they occupy the EXACT SAME (row, col) coordinates!",
        "Super-Octets & Hexadecets: A Quad of 4 in Plane A=0 combining with the identical Quad in Plane A=1 forms a **3D Super-Octet of 8 cells**, eliminating variable A!"
    ], current_slide=18, total_slides=total)

    # 19. Algorithmic Minimization: Quine-McCluskey (Tabular)
    add_bullet_slide(prs, "Algorithmic Minimization: The Quine-McCluskey Method", [
        "K-Map Limitation: K-maps become visually unwieldy and error-prone for functions with 5 or more variables.",
        "Algorithmic Tabular Approach: The Quine-McCluskey (Q-M) method is an exact, computer-programmable minimization algorithm.",
        "Step 1 (Index Grouping): Group minterms by the number of 1s in their binary representations (Group 0, 1, 2, ...).",
        "Step 2 (Single-Bit Merging): Compare terms between adjacent groups; merge terms differing by 1 bit, replacing the bit with a hyphen ('-').",
        "Step 3 (Prime Implicants): Iterate until no further merges are possible; all unmerged terms are declared **Prime Implicants (PIs)**.",
        "Step 4 (PI Table & Petrick's Method): Construct PI chart to identify Essential Prime Implicants (EPIs) covering all minterms at minimum cost.",
        "FPGA CAD Tools: Embedded inside Verilog and VHDL synthesis compilers for agricultural tractor ECU microchips."
    ], current_slide=19, total_slides=total)

    # 20. Case Study 1
    add_case_study_slide(prs, 1, "Bagasse Boiler Flameout Safety Hazard Mitigated",
                         "Kilombero Sugar Company Cogeneration Plant, Morogoro, Tanzania",
                         "At the Kilombero Sugar cogeneration factory, industrial steam boilers burn crushed sugarcane stalks (bagasse) to generate 15 MW of electricity. The burner safety circuit monitored Induced Draft Fan Pressure (P), Bagasse Chute Clear (F), Flame Active (S), and Water Level (L). During harvest peak, heavy variable-frequency feeder speed shifts caused false flameout emergency shutdowns costing 12,000 USD/hour in lost steam.",
                         "SUA engineers discovered an unmitigated static-1 hazard in the safety relay logic network: Y = P·/F + F·S. When feeder sensor F transitioned from 0 to 1 with P=1 and S=1, an 8-millisecond dropout glitch de-energized the main fuel solenoid. Engineers added the redundant consensus term P·S to the circuit.",
                         [
                             "Consensus gate held fuel solenoid solidly energized during all feeder switching transients.",
                             "Completely eliminated nuisance boiler flameout shutdowns across the milling campaign.",
                             "Saved an estimated 48,000 USD in downtime during peak harvesting."
                         ], current_slide=20, total_slides=total)

    # 21. Case Study 2
    add_case_study_slide(prs, 2, "Maize Silo Aeration Fan Multi-Variable Optimization",
                         "National Food Reserve Agency (NFRA) Storage Depot, Morogoro, Tanzania",
                         "Commercial grain aeration blowers operating on 20,000 tonnes of stored maize required fan operation only when air equilibrium moisture content (EMC) prevented grain re-wetting: Grain Moisture High (A), Ambient Humidity Low (B), Headspace Temp High (C), and Ambient Air Cooler than Grain (D). Technicians originally used an ad-hoc 18-rung ladder logic program that conflicted, running blowers during humid night rains and causing grain molding.",
                         "SUA agricultural engineers mapped the problem into a 4-variable Karnaugh map with don't-care conditions (dry season temperature extremes). The logic collapsed from 18 rungs down to a compact, elegant two-term expression: **Blower = B · ( A · D + C )**.",
                         [
                             "Simplified logic collapsed PLC program memory by 75% and eliminated logic race conditions.",
                             "Reduced monthly aeration fan electricity consumption by 32% (saving 3,800 USD/month).",
                             "Grain surface moisture maintained strictly under 13.5%, eliminating post-harvest mold."
                         ], current_slide=21, total_slides=total)

    # 22. Laboratory Bench Protocol
    add_lab_slide(prs, "K-Map Simplification & Static Hazard DSO Verification", [
        "Breadboard the unsimplified Boolean circuit: Y_raw = A·B + A·(B+C) + B·(B+C) using 74LS08 and 74LS32 ICs.",
        "Breadboard the K-map minimized equivalent circuit: Y_min = B + A·C on adjacent breadboard section.",
        "Sweep all 8 binary input combinations using a 3-switch DIP array and verify 100% truth table equivalence.",
        "Set up a static-1 hazard circuit (Y = A·/B + B·C); capture transient 10 ns glitch on DSO; solder consensus gate and verify elimination."
    ], [
        "Step 1: Wire Y_raw using 3 AND gates and 2 OR gates; wire Y_min using 1 AND gate and 1 OR gate.",
        "Step 2: Connect inputs to 3-pin DIP switch; connect outputs to Red LED (raw) and Green LED (minimized).",
        "Step 3: Sweep inputs A, B, C from 000_2 to 111_2; verify both LEDs light identically across all 8 states.",
        "Step 4: Measure propagation delay on DSO: Y_raw delay ≈ 38 ns (3 levels); Y_min delay ≈ 18 ns (2 levels). Speed doubled!",
        "Step 5: Assemble hazard circuit; trigger DSO on negative edge of output; capture 8 ns dip to 0.4V during B transition; add consensus term A·C to eliminate."
    ], current_slide=22, total_slides=total)

    # 23. Troubleshooting & Pitfalls
    add_bullet_slide(prs, "Diagnostic Troubleshooting of Boolean Logic & K-Maps", [
        "Incorrect K-Map Coordinates: Labeling coordinates in standard binary (00, 01, 10, 11) breaks unit-distance adjacency; leads to wrong groups!",
        "Non-Power-of-2 Groups: Grouping 3 or 6 cells is mathematically illegal and produces corrupted Boolean terms; groups must be 1, 2, 4, 8, 16.",
        "Overlooking Toroidal Wrap: Failing to group the 4 corners or edge cells results in unminimized expressions with unnecessary gate literals.",
        "Ignoring Don't-Cares: Treating Don't-Cares as 0s misses opportunities to form massive octets or quads, bloating hardware complexity.",
        "Omitting Consensus Terms in High-Speed Relays: Eliminating static hazards is mandatory in safety-critical machinery to prevent false tripping."
    ], current_slide=23, total_slides=total)

    # 24. Review Questions
    add_review_slide(prs, lec_num, [
        "State the Principle of Duality in Boolean algebra and find the dual of the equation: A + /A · B = A + B.",
        "Explain why Karnaugh map coordinates are labeled in Gray code sequence (00, 01, 11, 10) rather than standard binary.",
        "Minimize the 4-variable Boolean function F(A, B, C, D) = Sum m( 0, 2, 5, 7, 8, 10, 13, 15 ) using a 16-cell K-map.",
        "What is a Don't-Care condition in digital design, and under what circumstances should a Don't-Care cell be included in a group?",
        "Define a Static-1 hazard. How is it detected visually on a K-map, and how does adding a consensus term eliminate it?"
    ], "Congratulations! You have completed all 9 lecture modules of AEN 214: Introduction to Electronics at SUA.", current_slide=24, total_slides=total)

    # 25. Key Takeaways & Cheat-Sheet
    add_summary_slide(prs, lec_num, [
        "Boolean algebra provides the mathematical framework for analyzing and minimizing digital switching networks.",
        "De Morgan's laws allow seamless conversion between AND-OR and universal NAND-NOR gate topologies.",
        "Karnaugh maps exploit Gray-code geometric adjacency to eliminate variables in power-of-2 groups (2, 4, 8, 16).",
        "Don't-Care conditions (X) must be leveraged to enlarge group sizes, drastically simplifying hardware.",
        "Static hazards create transient glitches due to propagation delays; eliminated by adding redundant consensus implicants."
    ], [
        "Involution: //A = A; Idempotent: A + A = A; A · A = A",
        "Second Distributive Law: A + (B · C) = (A + B) · (A + C)",
        "De Morgan's Laws: /(A · B) = /A + /B; /(A + B) = /A · /B",
        "Consensus Theorem: AB + /AC + BC = AB + /AC",
        "K-Map Cell Elimination: 2 cells -> 1 var; 4 cells -> 2 vars; 8 cells -> 3 vars",
        "Four-Corner Quad: Cells (0, 2, 8, 10) -> /B · /D",
        "Hazard-Free SOP: Y_{safe} = A·/B + B·C + A·C (Consensus)"
    ], current_slide=25, total_slides=total)

    # 26. References & Reading List
    add_bullet_slide(prs, "Prescribed References & Coursework Capstone Defense", [
        "Mano, M. M., & Ciletti, M. D. (2018). Digital Design: With an Introduction to Verilog HDL (6th ed.). Pearson.",
        "Roth, C. H., & Kinney, L. L. (2020). Fundamentals of Logic Design (7th ed.). Cengage Learning.",
        "Floyd, T. L. (2015). Digital Fundamentals (11th ed.). Pearson.",
        "Final Capstone Project Defense: Multi-disciplinary groups will present their autonomous agricultural prototypes next week.",
        "Coursework Submissions: Ensure Assignment 1, 2, and 3 are finalized and submitted via SUA LMS before the final examination."
    ], current_slide=26, total_slides=total)

    print(f"[Done] Built Lecture {lec_num} deck ({len(prs.slides)} slides).")

print("slides_part3 module complete with Lectures 7, 8, and 9.")
