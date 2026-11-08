#!/usr/bin/env python3
"""
slides_topics_4_to_6.py
High-density lecture slide definitions for Topics 4, 5, and 6.
BIT 111: MICROCOMPUTERS AND APPLICATIONS
Sokoine University of Agriculture (SUA).
Instructor: Madam Bertha Msuliche Lebalwa (MSc)
Each topic features strictly >= 30 slides (33-35 slides per topic).
"""

def get_topic_4_slides():
    return [
        {
            "type": "bullet",
            "title": "Topic 4: Lecture Outline & Learning Roadmap",
            "sub_title": "Operating Systems, Process Management & Commands (Coverage: 4.1, 4.2, 4.3)",
            "bullets": [
                "• Section 4.1: OS Evolution, Core Architecture & Subsystem Categories",
                "    - The OS as Extended Machine & Resource Arbiter; Kernel models (Monolithic, Microkernel, Hybrid)",
                "    - Dual-mode operation (Ring 0 vs Ring 3); System calls and interrupt handling",
                "    - Process management: PCB, 5-state lifecycle, CPU scheduling algorithms (FCFS, SJF, SRTF, RR)",
                "    - Memory management: Logical vs physical addressing, Paging, TLB, Virtual memory",
                "    - File systems: FAT32, NTFS, ext4; Allocation structures and Journaling",
                "• Section 4.2: Disk Operating System (MS-DOS) Architecture & Commands",
                "    - DOS architecture: `IO.SYS`, `MSDOS.SYS`, `COMMAND.COM`",
                "    - Internal commands (`DIR`, `COPY`, `DEL`, `MD`, `CD`, `TYPE`) vs External (`FORMAT`, `CHKDSK`, `XCOPY`)",
                "    - Batch scripting (`.BAT`): Variables, parameters `%1-%9`, conditionals `IF`, loops `FOR`, redirection",
                "• Section 4.3: Modern GUI Operating Systems (Windows & Linux) and Administration",
                "    - Windows architecture: Registry, Task Manager, Event Viewer, PowerShell cmdlets",
                "    - Linux architecture: Filesystem Hierarchy Standard (FHS), shell pipelines, process controls (`ps`, `top`, `kill`)"
            ],
            "callout": {
                "title": "PEDAGOGICAL OBJECTIVE",
                "body": "Understand how the operating system bridges the gap between raw microprocessor silicon and user applications through process abstraction, resource scheduling, and command interfaces."
            }
        },
        {
            "type": "bullet",
            "title": "Topic 4: Intended Learning Outcomes (ILOs)",
            "sub_title": "Core Operating Systems Competencies for SUA Undergraduates",
            "bullets": [
                "• Explain the dual roles of an operating system: Extended Machine (Abstraction) and Resource Arbiter.",
                "• Contrast Monolithic kernels, Microkernels, and Hybrid kernels in performance and fault isolation.",
                "• Trace process state transitions across the 5-state lifecycle and calculate CPU scheduling metrics.",
                "• Detail virtual memory address translation using the MMU, Page Tables, and TLB.",
                "• Distinguish internal MS-DOS commands from external disk executables and write automated batch scripts.",
                "• Evaluate file systems (FAT32, NTFS, ext4) regarding journaling, volume limits, and permissions.",
                "• Execute administrative system commands in Windows (PowerShell) and Linux (Bash) environments."
            ]
        },
        {
            "type": "figure",
            "title": "Operating System Architectural Hierarchy",
            "img": "fig4_1_os_architecture_layers.png",
            "caption": "The multi-tiered OS architectural model bridging hardware, kernel, system calls, and user applications.",
            "bullets": [
                "• Hardware Layer: Physical CPU, memory, buses, timers, and peripheral controllers.",
                "• Kernel Mode (Ring 0): Unrestricted hardware access executing process scheduling, memory allocation, and device drivers.",
                "• System Call Interface: Protected software interrupt gate (e.g., `sys_enter`, `syscall`, `int 0x80`).",
                "• User Mode (Ring 3): Sandboxed execution of user applications, shell CLI, and GUI desktop environments without direct hardware access."
            ]
        },
        {
            "type": "bullet",
            "title": "OS Kernel Architectural Paradigms",
            "sub_title": "Monolithic Kernels vs Microkernels vs Hybrid Models",
            "bullets": [
                "• Monolithic Kernels (e.g., Linux, traditional UNIX):",
                "    - All core OS services (scheduler, memory manager, file systems, device drivers, network stack) run together in Ring 0.",
                "    - Advantage: Ultra-fast performance; direct function calls between subsystems.",
                "    - Disadvantage: A single buggy device driver can crash the entire operating system (Kernel Panic).",
                "• Microkernels (e.g., Mach, QNX, seL4):",
                "    - Ring 0 stripped down to bare minimum: IPC (Inter-Process Communication), basic scheduling, low-level memory.",
                "    - Device drivers, file systems, and network stacks execute in User Space (Ring 3) as modular servers.",
                "    - Advantage: Extreme fault tolerance and security; crash of a driver does not crash the kernel.",
                "• Hybrid Kernels (e.g., Windows NT kernel, Apple macOS XNU):",
                "    - Combines microkernel modularity with monolithic performance by keeping select drivers in kernel space."
            ]
        },
        {
            "type": "bullet",
            "title": "Dual-Mode Operation & Hardware Protection",
            "sub_title": "Preventing Errant User Programs from Crashing Microcomputers",
            "bullets": [
                "• The Dual-Mode Protection Mechanism (enforced by CPU hardware status bit):",
                "    - 1. User Mode (Ring 3): Application execution mode; privileged CPU instructions (e.g., disabling interrupts, direct I/O port writes) are strictly forbidden.",
                "    - 2. Kernel / Supervisor Mode (Ring 0): Full instruction set enabled with direct hardware manipulation.",
                "• System Calls (Syscalls): The sanctioned software API for user applications to request kernel services (e.g., `read()`, `write()`, `fork()`, `open()`).",
                "• Mechanism: Application sets up arguments in registers, triggers a software trap/interrupt; CPU switches from Ring 3 to Ring 0, kernel validates parameters, executes task, and returns control switching back to Ring 3."
            ]
        },
        {
            "type": "figure",
            "title": "The Five-State Process Lifecycle",
            "img": "fig4_2_process_state_transition.png",
            "caption": "The classical 5-state process lifecycle illustrating CPU scheduling and I/O wait transitions.",
            "bullets": [
                "• New: Process being created and its Process Control Block (PCB) allocated.",
                "• Ready: Process residing in main memory, waiting for the OS CPU scheduler to dispatch it.",
                "• Running: Instructions currently executing on the physical CPU core.",
                "• Waiting (Blocked): Process suspended waiting for an external event (disk I/O, keyboard input, network packet).",
                "• Terminated: Process completed execution; resources deallocated by the kernel."
            ]
        },
        {
            "type": "bullet",
            "title": "Process Management & The Process Control Block (PCB)",
            "sub_title": "The Kernel's Data Structure Representing a Living Process",
            "bullets": [
                "• Process Definition: A program in execution; an active entity with a program counter, memory segments, and assigned OS resources.",
                "• Process Control Block (PCB) Data Fields:",
                "    - Process Identifier (PID): Unique integer assigned by kernel.",
                "    - Process State: New, Ready, Running, Waiting, or Terminated.",
                "    - Program Counter (PC): Memory address of next instruction to execute.",
                "    - CPU Registers: Saved accumulator, index, stack pointer, and flag registers.",
                "    - CPU Scheduling Info: Process priority and queue pointers.",
                "    - Memory Management Info: Base/limit registers, page table pointers.",
                "    - Accounting & I/O Status: CPU time used, open file descriptors, allocated I/O devices.",
                "• Context Switching: The CPU state save and restore cycle when preempting one process for another (pure computational overhead)."
            ]
        },
        {
            "type": "bullet",
            "title": "CPU Scheduling Algorithms & Metrics",
            "sub_title": "Optimizing Processor Utilization and Response Time",
            "bullets": [
                "• Performance Metrics: Turnaround Time (Completion - Arrival), Waiting Time (Turnaround - Burst), Response Time, Throughput.",
                "• Common CPU Scheduling Algorithms:",
                "    - 1. First-Come, First-Served (FCFS): Non-preemptive; simple FIFO queue; suffers from severe 'Convoy Effect' if a long process arrives first.",
                "    - 2. Shortest Job First (SJF): Non-preemptive; mathematically optimal for minimum average waiting time; requires predicting future burst times.",
                "    - 3. Shortest Remaining Time First (SRTF): Preemptive version of SJF; interrupts currently running process if a shorter job arrives.",
                "    - 4. Round Robin (RR): Preemptive; each process allocated a fixed time quantum q; cycles circularly through ready queue; ideal for interactive timesharing."
            ]
        },
        {
            "type": "bullet",
            "title": "Worked Scheduling Problem: FCFS vs SRTF",
            "sub_title": "Comparative Analysis of CPU Waiting and Turnaround Times",
            "bullets": [
                "• Scenario: Processes P1 (Arrival=0ms, Burst=8ms), P2 (Arrival=2ms, Burst=4ms), P3 (Arrival=4ms, Burst=2ms).",
                "• FCFS Execution Order: P1 [0–8ms] → P2 [8–12ms] → P3 [12–14ms]:",
                "    - P1: Waiting = 0 - 0 = 0 ms; Turnaround = 8 - 0 = 8 ms.",
                "    - P2: Waiting = 8 - 2 = 6 ms; Turnaround = 12 - 2 = 10 ms.",
                "    - P3: Waiting = 12 - 4 = 8 ms; Turnaround = 14 - 4 = 10 ms.",
                "    - Average Waiting Time = (0 + 6 + 8) / 3 = 4.67 ms. Average Turnaround = 9.33 ms.",
                "• SRTF Execution Order: P1 [0–2ms, rem 6] → P2 [2–4ms, rem 2] → P3 [4–6ms, finishes] → P2 [6–8ms, finishes] → P1 [8–14ms, finishes]:",
                "    - P3: Waiting = 4 - 4 = 0 ms; Turnaround = 6 - 4 = 2 ms.",
                "    - P2: Waiting = (2-2) + (6-4) = 2 ms; Turnaround = 8 - 2 = 6 ms.",
                "    - P1: Waiting = (0-0) + (8-2) = 6 ms; Turnaround = 14 - 0 = 14 ms.",
                "    - Average Waiting Time = (0 + 2 + 6) / 3 = 2.67 ms (43% faster waiting than FCFS!)."
            ]
        },
        {
            "type": "bullet",
            "title": "Concurrency, Race Conditions, and Deadlocks",
            "sub_title": "Multi-Thread Synchronization and The Coffman Conditions",
            "bullets": [
                "• Race Condition: A situation where multiple concurrent threads access shared data, and the final outcome depends on the non-deterministic timing of thread execution.",
                "• Critical Section: Code segment accessing shared resources that must be executed with Mutual Exclusion (mutex locks, semaphores).",
                "• Deadlock: A permanent stalling state where two or more processes are unable to proceed because each holds a resource the other needs.",
                "• The Four Coffman Conditions (Must all hold simultaneously for deadlock):",
                "    1. Mutual Exclusion: At least one resource must be held in non-shareable mode.",
                "    2. Hold and Wait: A process holds resources while requesting additional ones.",
                "    3. No Preemption: Resources cannot be forcibly seized from a holding process.",
                "    4. Circular Wait: A closed chain of processes exists where P<sub>0</sub> waits for P<sub>1</sub>, and P<sub>n</sub> waits for P<sub>0</sub>."
            ]
        },
        {
            "type": "bullet",
            "title": "Memory Management: Paging & Virtual Memory",
            "sub_title": "Translating Virtual Addresses to Physical DRAM Frames",
            "bullets": [
                "• Logical (Virtual) vs Physical Address Space: Applications operate in contiguous virtual memory isolated from actual fragmented physical RAM.",
                "• Paging Mechanism: Divides virtual memory into fixed-size blocks called Pages (typically 4 KiB); physical memory divided into Frames of identical size.",
                "• Memory Management Unit (MMU): Hardware on the CPU die translating virtual page numbers (VPN) to physical frame numbers (PFN) via Page Tables.",
                "• Translation Lookaside Buffer (TLB): High-speed on-die associative cache buffering recent address translations, eliminating memory lookup overhead.",
                "• Demand Paging & Page Faults: Pages loaded into DRAM only when accessed; referencing an unmapped page triggers a Page Fault interrupt, causing the OS to fetch the page from secondary storage (swap space)."
            ]
        },
        {
            "type": "table",
            "title": "Enterprise File Systems Comparison",
            "headers": ["Feature / Attribute", "FAT32", "exFAT", "NTFS", "ext4 (Linux)"],
            "rows": [
                ["Max File Size", "4 GiB", "16 EiB", "16 TiB - 8 PiB", "16 TiB"],
                ["Max Volume Size", "2 TiB (32-bit)", "128 PiB", "8 PiB", "1 EiB"],
                ["Journaling Support", "No (Corruption prone)", "No", "Yes (USN Journal)", "Yes (JBD2 Journal)"],
                ["Access Control (ACLs)", "None (Universal read)", "None", "Full NTFS Permissions", "Full POSIX Permissions"],
                ["Native Encryption", "None", "None", "EFS (Encrypting FS)", "fscrypt (Native)"],
                ["Target Ecosystem", "Legacy USB Drives", "Cross-Platform Flash", "Windows OS & Servers", "Linux OS & Servers"]
            ],
            "col_widths": [2.2, 2.0, 2.0, 2.5, 2.5]
        },
        {
            "type": "bullet",
            "title": "MS-DOS Architecture: Three Core Files",
            "sub_title": "The 16-Bit Real-Mode Disk Operating System",
            "bullets": [
                "• Historical Significance: 16-bit single-user, single-tasking command-line OS created by Tim Paterson (86-DOS) and licensed by Microsoft as MS-DOS / PC-DOS (1981).",
                "• The Three Fundamental System Files:",
                "    - 1. `IO.SYS`: Low-level hardware interface containing basic device drivers (screen, keyboard, serial, floppy); interfaces directly with ROM BIOS.",
                "    - 2. `MSDOS.SYS`: The DOS operating system kernel; manages the file system, memory allocation, directory structures, and system call interrupts (`INT 21h`).",
                "    - 3. `COMMAND.COM`: The default command-line command interpreter (shell); parses user commands, executes batch files, and houses all internal commands.",
                "• Boot Sequence: ROM BIOS POST → MBR → Boot Sector → Loads `IO.SYS` → Loads `MSDOS.SYS` → Parses `CONFIG.SYS` → Executes `COMMAND.COM` → Runs `AUTOEXEC.BAT`."
            ]
        },
        {
            "type": "bullet",
            "title": "MS-DOS Internal Commands",
            "sub_title": "Resident in RAM: Handled Directly by COMMAND.COM",
            "bullets": [
                "• Definition: Built directly into `COMMAND.COM`; always resident in main memory, executing instantly without requiring disk access.",
                "• Essential Internal Directory & File Commands:",
                "    - `DIR`: Lists files, subdirectories, file sizes, and timestamps in current directory.",
                "    - `MD` or `MKDIR`: Creates a new subdirectory (e.g., `MD D:\\SUA_DATA`).",
                "    - `CD` or `CHDIR`: Changes the current working directory (e.g., `CD \\ACADEMIC\\BIT111`).",
                "    - `RD` or `RMDIR`: Removes an empty directory.",
                "    - `COPY`: Copies one or more files to another destination (e.g., `COPY notes.txt E:\\`).",
                "    - `DEL` or `ERASE`: Deletes specified files from the disk.",
                "    - `REN`: Renames files or directories without moving them.",
                "    - `TYPE`: Displays contents of a text file on the screen.",
                "    - `CLS`: Clears the display screen; `VER`: Displays operating system version."
            ]
        },
        {
            "type": "bullet",
            "title": "MS-DOS External Commands",
            "sub_title": "Disk-Resident Executables: Stored as .COM, .EXE, or .BAT Files",
            "bullets": [
                "• Definition: Separate executable files stored on secondary storage; loaded into RAM only when invoked by the user.",
                "• Essential External Disk & File Management Commands:",
                "    - `FORMAT.COM`: Formats a disk volume with a file system, creating the boot sector, FAT tables, and root directory.",
                "    - `CHKDSK.EXE`: Analyzes disk volume integrity, checks for lost allocation clusters, and reports free/bad sectors.",
                "    - `XCOPY.EXE`: Advanced file/directory copy utility supporting recursive directory tree copying (`/S /E /Y /V`).",
                "    - `ROBOCOPY.EXE` (Modern Windows): Robust file copying utility with multi-threading, restartable mode, and mirror synchronization.",
                "    - `ATTRIB.EXE`: Views or modifies file attributes: Read-only (`+R`), Hidden (`+H`), System (`+S`), Archive (`+A`).",
                "    - `TREE.COM`: Graphically displays directory path hierarchy of a drive."
            ]
        },
        {
            "type": "bullet",
            "title": "MS-DOS Batch Scripting & Automation",
            "sub_title": "Automating Multi-Step Operations via .BAT Files",
            "bullets": [
                "• Batch File: Plain text file containing sequential DOS commands executed by `COMMAND.COM` or Windows `cmd.exe`.",
                "• Key Syntax Elements:",
                "    - `@ECHO OFF`: Suppresses command echoing to clean up terminal output.",
                "    - Command-line arguments: Positional variables `%1`, `%2`, through `%9`.",
                "    - Conditionals: `IF EXIST filename (command) ELSE (command)`.",
                "    - Flow Control: `GOTO label` and `:label` definitions.",
                "    - Iteration: `FOR %%F IN (*.DAT) DO (command)`.",
                "    - Redirection Operators: Output redirect `>` (overwrite), `>>` (append), Input redirect `<`, Pipe `|`."
            ]
        },
        {
            "type": "bullet",
            "title": "Modern GUI Operating Systems: The WIMP Paradigm",
            "sub_title": "Windows, Icons, Menus, and Pointer Interfaces",
            "bullets": [
                "• Evolution from CLI to GUI: Douglas Engelbart (NLS, 1968) → Xerox PARC (Alto, 1973) → Apple Macintosh (1984) → Windows 95.",
                "• WIMP Elements:",
                "    - Windows: Rectangular screen viewports isolating running application contexts.",
                "    - Icons: Small graphical pictograms representing files, programs, and system entities.",
                "    - Menus: Drop-down or context-sensitive lists of executable options.",
                "    - Pointer: Mouse/trackpad cursor translating physical 2D hand movement into on-screen spatial targeting.",
                "• Modern Desktop Environments: Windows Shell / Fluent Design; Linux GNOME, KDE Plasma, XFCE."
            ]
        },
        {
            "type": "bullet",
            "title": "Windows System Management Utilities",
            "sub_title": "Core MMC Consoles and Administrative Tools",
            "bullets": [
                "• Task Manager (`taskmgr`): Inspects running processes, CPU/RAM/Disk utilization, startup programs, and thread status.",
                "• Device Manager (`devmgmt.msc`): Hardware abstraction console displaying driver versions, IRQ assignments, and hardware device conflicts.",
                "• Disk Management (`diskmgmt.msc`): Initializes MBR/GPT partition tables, shrinks/extends volumes, formats NTFS/exFAT drives.",
                "• Event Viewer (`eventvwr.msc`): Centralized diagnostic log repository recording Application, Security, Setup, and System error logs.",
                "• Services MMC (`services.msc`): Controls background daemon processes (Start, Stop, Restart, Startup Type: Auto/Manual/Disabled).",
                "• Windows Registry (`regedit`): Hierarchical database storing OS configuration (`HKEY_LOCAL_MACHINE`, `HKEY_CURRENT_USER`)."
            ]
        },
        {
            "type": "bullet",
            "title": "Modern Windows Administration: PowerShell",
            "sub_title": "Object-Oriented Automation vs Traditional Text Shells",
            "bullets": [
                "• Paradigm Shift: Unlike traditional text-based shells (DOS/Bash), PowerShell passes structured .NET objects across the pipeline, not raw character streams.",
                "• Verb-Noun Syntax: Consistent command naming pattern (`Get-Service`, `Stop-Process`, `Set-ExecutionPolicy`).",
                "• Essential Administrative Cmdlets:",
                "    - `Get-Process | Where-Object WorkingSet -gt 500MB | Stop-Process`: Kills processes consuming >500 MB RAM.",
                "    - `Get-Service -Name Spooler | Restart-Service`: Restarts print spooler daemon.",
                "    - `Get-EventLog -LogName System -EntryType Error -Newest 10`: Extracts latest 10 critical system errors.",
                "    - `Test-NetConnection -ComputerName www.sua.ac.tz -Port 443`: Verifies TCP socket reachability."
            ]
        },
        {
            "type": "bullet",
            "title": "Linux Architecture & Filesystem Hierarchy Standard",
            "sub_title": "The Structure of the Enterprise Open-Source OS",
            "bullets": [
                "• Philosophy: 'Everything is a file' — storage devices, serial ports, and processes are exposed via virtual filesystems.",
                "• FHS Directory Hierarchy:",
                "    - `/bin` & `/sbin`: Essential user and system administration binary executables.",
                "    - `/etc`: System-wide configuration files (e.g., `/etc/passwd`, `/etc/fstab`, `/etc/network`).",
                "    - `/home`: User personal directories and application data.",
                "    - `/var`: Variable data files (log files in `/var/log`, mail spools, web root `/var/www`).",
                "    - `/dev`: Special device nodes representing hardware (`/dev/sda`, `/dev/nvme0n1`).",
                "    - `/proc` & `/sys`: Virtual pseudo-filesystems exposing live kernel state and hardware metrics."
            ]
        },
        {
            "type": "bullet",
            "title": "Linux Terminal Diagnostics & Process Control",
            "sub_title": "Inspecting System Performance and Managing Daemons",
            "bullets": [
                "• Process Inspection: `ps aux` (BSD syntax), `ps -ef` (System V syntax), `top`, `htop` (interactive ncurses monitor).",
                "• Signal Transmission: `kill -15 PID` (SIGTERM - polite termination request allowing cleanup) vs `kill -9 PID` (SIGKILL - immediate uninterceptable kernel abort).",
                "• Process Scheduling Priority: `nice -n 10 command` (launches process with lower CPU priority); `renice -n -5 -p PID` (boosts running process priority).",
                "• Service Management via systemd: `systemctl status service_name`, `systemctl start/stop/restart`, `systemctl enable` (auto-start on boot).",
                "• Storage Telemetry: `df -h` (filesystem disk space usage), `du -sh /path` (directory space consumption)."
            ]
        },
        {
            "type": "bullet",
            "title": "Real-Time Operating Systems (RTOS) in Agriculture",
            "sub_title": "Deterministic Guarantees vs Best-Effort Desktop Systems",
            "bullets": [
                "• RTOS Definition: An operating system designed to execute processes within strictly bounded, deterministic time constraints (deadlines).",
                "• Categories:",
                "    - Hard Real-Time: Missing a single deadline is considered total system failure (e.g., autonomous tractor obstacle avoidance, airbag deployment).",
                "    - Soft Real-Time: Missing a deadline degrades quality of service but does not cause catastrophic system failure (e.g., video streaming telemetry).",
                "• Why GPOS (Windows/Ubuntu) Fails at Real-Time: Non-deterministic kernel preemption latency, complex virtual memory page faults, and background garbage collection.",
                "• Agricultural Harvester Case Study: High-speed optical grain sorters use RTOS (e.g., FreeRTOS, VxWorks) to actuate pneumatic air-ejector valves in < 2 ms when rejecting discolored grains."
            ]
        },
        {
            "type": "bullet",
            "title": "OS Boot Architecture: Firmware to Init / Systemd (PID 1)",
            "sub_title": "The Step-by-Step Transition from Silicon to Multi-User Shell",
            "bullets": [
                "• Boot Sequence Stages:",
                "    1. POST & Firmware: UEFI initializes hardware, verifies CPU/RAM, executes Secure Boot validation.",
                "    2. Bootloader: UEFI executes EFI bootloader (GRUB2 on Linux / Windows Boot Manager `bootmgr.efi`).",
                "    3. Kernel Initialization: Kernel decompressed into RAM, sets up page tables, MMU, interrupts, device drivers.",
                "    4. Root Filesystem Mount: Mounts initial RAM disk (`initramfs`) to load storage drivers, then mounts real root `/`.",
                "    5. Init / Systemd (PID 1): The ancestor process of all user-space daemons, launching target services (networking, SSH, display manager).",
                "• Windows Equivalent: `ntoskrnl.exe` initialized → launches Session Manager Subsystem (`smss.exe`) → launches `csrss.exe` and `wininit.exe`."
            ]
        },
        {
            "type": "bullet",
            "title": "Page Replacement Algorithms: FIFO to LRU and Clock",
            "sub_title": "Managing Limited Physical Memory Under Heavy Workloads",
            "bullets": [
                "• The Page Replacement Problem: When a page fault occurs and all DRAM frames are occupied, the OS must evict a victim page to secondary storage.",
                "• 1. First-In, First-Out (FIFO): Evicts the oldest loaded page; simple queue; suffers from Belady's Anomaly (allocating more physical frames can paradoxically increase page faults).",
                "• 2. Optimal Page Replacement (OPT / MIN): Evicts the page that will not be used for the longest future duration; theoretically optimal but impossible to implement in practice (requires future knowledge).",
                "• 3. Least Recently Used (LRU): Evicts the page unused for the longest past time (approximates OPT based on temporal locality); high overhead to track timestamps.",
                "• 4. Clock Algorithm (Second-Chance): Practical approximation of LRU using a single reference bit per frame scanned circularly by a clock pointer."
            ]
        },
        {
            "type": "bullet",
            "title": "Virtual Memory Thrashing & The Working Set Model",
            "sub_title": "Understanding System Freezes Caused by Paging Collapse",
            "bullets": [
                "• Thrashing Definition: A state where the CPU spends more time swapping pages between RAM and disk than executing real user instructions.",
                "• The Collapse Mechanism: If the sum of working sets of all running processes exceeds total physical RAM, page fault frequency skyrockets → CPU utilization plummets to near zero → OS scheduler misinterprets low CPU usage and launches more processes, worsening the collapse.",
                "• Working Set Model (Peter Denning):",
                "    - Working Set W(t, Δ): The set of pages referenced by a process in the most recent time window Δ.",
                "    - Operating System Policy: The OS must ensure that each process has enough frames allocated to hold its working set. If total demand exceeds physical memory, the OS suspends (swaps out) entire processes to restore equilibrium."
            ]
        },
        {
            "type": "bullet",
            "title": "File Allocation Architecture: Inodes & Extents",
            "sub_title": "Contiguous, Linked List, and Indexed File Block Mapping",
            "bullets": [
                "• 1. Contiguous Allocation: File blocks stored in sequential disk sectors; fast sequential access; severe external fragmentation; difficult file expansion.",
                "• 2. Linked List Allocation: Each disk block contains a pointer to the next block; eliminates external fragmentation; slow random access; pointer corruption destroys remaining file.",
                "• 3. Indexed Allocation (UNIX Inode Architecture):",
                "    - Inode: Metadata structure containing file size, permissions, timestamps, and an array of block pointers.",
                "    - Direct Pointers (typically 12): Point directly to data blocks (fast access for small files).",
                "    - Indirect Pointers: Single, Double, and Triple indirect pointers pointing to pointer tables, allowing files to scale to terabytes.",
                "• Modern Extent-Based Allocation: Extents (start block + length) used in ext4 and NTFS to reduce pointer overhead for large contiguous files."
            ]
        },
        {
            "type": "bullet",
            "title": "Hypervisors & Virtualization: Type-1 vs Type-2",
            "sub_title": "Hardware Abstraction and Multi-Tenant Server Consolidation",
            "bullets": [
                "• Virtual Machine (VM): Complete software emulation of an entire physical computer, including virtual CPU, virtual BIOS/UEFI, virtual RAM, and virtual storage.",
                "• Type-1 Hypervisor (Bare-Metal):",
                "    - Installs and runs directly on bare physical server hardware (e.g., VMware ESXi, Proxmox VE, Microsoft Hyper-V Server, KVM).",
                "    - Superior performance, low virtualization latency, high security isolation; the enterprise standard for university cloud datacenters.",
                "• Type-2 Hypervisor (Hosted):",
                "    - Runs as an application inside an existing host operating system (e.g., Oracle VirtualBox, VMware Workstation).",
                "    - Dependent on host OS stability; used primarily for student labs, testing, and cross-platform software development."
            ]
        },
        {
            "type": "bullet",
            "title": "Containerization: Linux Namespaces & Docker vs VMs",
            "sub_title": "Operating System-Level Virtualization and Microservices",
            "bullets": [
                "• Paradigm Difference: While Virtual Machines virtualize the underlying physical hardware, Containers virtualize the operating system kernel.",
                "• Linux Kernel Foundations of Containers:",
                "    - Namespaces: Isolate process visibility across PID (process IDs), NET (network interfaces/ports), MNT (filesystem mounts), and IPC.",
                "    - Control Groups (cgroups): Restrict and measure resource consumption (limiting container CPU cores, memory limits, I/O bandwidth).",
                "• Container Advantages over VMs:",
                "    - Near-Zero Boot Time: Boots in milliseconds (just launching a sandboxed process, not booting an entire OS kernel).",
                "    - Featherweight Footprint: Shares host kernel; container images often < 100 MB vs 20+ GB for a VM disk image.",
                "    - Portability: Docker packages agricultural AI scripts with exact Python dependencies for uniform execution."
            ]
        },
        {
            "type": "bullet",
            "title": "Linux Storage Management: Logical Volume Manager (LVM)",
            "sub_title": "Dynamic Partitioning and Online Storage Resizing",
            "bullets": [
                "• The Static Partition Limitation: Traditional MBR/GPT partitions have fixed sizes; resizing requires unmounting filesystems and risks data loss.",
                "• LVM Architectural Layers:",
                "    - Physical Volumes (PV): Raw physical partitions or entire disks initialized for LVM (`pvcreate /dev/sdb1`).",
                "    - Volume Groups (VG): Storage pools created by aggregating multiple PVs into a unified storage pool (`vgcreate data_pool /dev/sdb1 /dev/sdc1`).",
                "    - Logical Volumes (LV): Virtual partitions carved out of the Volume Group, formatted with a filesystem (ext4/XFS) and mounted (`lvcreate -L 50G -n crop_docs data_pool`).",
                "• Key Benefits: Online volume expansion (`lvextend -L +20G /dev/data_pool/crop_docs -r`) and atomic read-only storage snapshots for backup."
            ]
        },
        {
            "type": "bullet",
            "title": "Shell I/O Redirection & Pipeline Diagnostics",
            "sub_title": "Composing Modular Terminal Tools via Standard Streams",
            "bullets": [
                "• The Three Standard POSIX Streams:",
                "    - Standard Input (`stdin`, File Descriptor `0`): Keyboard input by default.",
                "    - Standard Output (`stdout`, File Descriptor `1`): Terminal screen display.",
                "    - Standard Error (`stderr`, File Descriptor `2`): Unbuffered diagnostic error messages.",
                "• Redirection Operators:",
                "    - `command > file.txt`: Redirects `stdout`, overwriting file.",
                "    - `command >> file.txt`: Redirects `stdout`, appending to file.",
                "    - `command 2> errors.log`: Redirects only `stderr` to file.",
                "    - `command &> all_output.log`: Redirects both `stdout` and `stderr`.",
                "• Pipelines (`|`): Passes `stdout` of left command directly as `stdin` of right command:",
                "    - Example: `ps aux | grep python3 | awk '{print $2, $4}' | sort -nr`."
            ]
        },
        {
            "type": "bullet",
            "title": "Topic 4: Key Takeaways & Synthesis Matrix",
            "sub_title": "Summary of Operating Systems Principles for Academic Mastery",
            "bullets": [
                "• OS Foundations: Resource Arbiter and Extended Machine; Kernel Mode (Ring 0) protects hardware from User Mode (Ring 3).",
                "• Kernels: Monolithic (fast, single address space) vs Microkernel (modular, IPC-based, isolated drivers).",
                "• Process Scheduling: Managed via PCB; SRTF minimizes average waiting time; Round Robin prevents starvation.",
                "• Memory & Storage: Paging enables virtual memory via MMU/TLB; Journaling (NTFS/ext4) prevents metadata corruption during sudden power cuts.",
                "• MS-DOS: Driven by `IO.SYS`, `MSDOS.SYS`, and `COMMAND.COM`; internal commands resident in RAM, external commands on disk.",
                "• Systems Administration: Windows leverages PowerShell object pipelines; Linux leverages Bash text streams and FHS hierarchy."
            ]
        },
        {
            "type": "bullet",
            "title": "Review Quiz & Knowledge Check",
            "sub_title": "Self-Testing Key OS Concepts",
            "bullets": [
                "1. Why is an operating system's kernel executed in Ring 0 while user web browsers execute in Ring 3?",
                "2. What is the fundamental difference between an Internal DOS command and an External DOS executable?",
                "3. Explain how a Journaling file system (such as ext4 or NTFS) prevents volume corruption when power fails.",
                "4. What causes process 'Starvation' in Shortest Remaining Time First (SRTF) CPU scheduling?",
                "5. Why is a standard desktop Linux or Windows OS unsuitable for hard real-time tractor guidance controls?"
            ]
        },
        {
            "type": "bullet",
            "title": "Reading Assignments & Homework Notice",
            "sub_title": "Preparation for Next Lecture & Continuous Assessment",
            "bullets": [
                "• Required Readings:",
                "    - Silberschatz, Galvin & Gagne - Operating System Concepts (10th Ed.), Chapters 1, 3, 5, 8 & 9.",
                "    - Tanenbaum & Bos - Modern Operating Systems (4th Ed.), Chapters 1, 2 & 4.",
                "• Homework Assignment 4 Notice:",
                "    - Available on SUA Moodle / Assignment directory: `BIT_111_Assignment_4.pdf`.",
                "    - Total Allocation: 100 Marks (Covers Process Scheduling, Batch Scripting, and Administrative Utilities).",
                "    - Submission Deadline: End of Week 8 by 17:00 EAT.",
                "• Next Lecture Preview: Topic 5 — Microcomputer Applications (Word Processing, Advanced Spreadsheets, Internet Protocols)."
            ]
        }
    ]

# -------------------------------------------------------------
# TOPIC 5 SLIDES DATA
# -------------------------------------------------------------
def get_topic_5_slides():
    return [
        {
            "type": "bullet",
            "title": "Topic 5: Lecture Outline & Learning Roadmap",
            "sub_title": "Productivity Applications, Spreadsheets & Web Systems (Coverage: 5.1, 5.2, 5.3)",
            "bullets": [
                "• Section 5.1: Word Processing Systems & Academic Document Engineering",
                "    - Structural document architecture: Character/paragraph formatting, section breaks, margins",
                "    - Advanced automation: Heading styles, automated Table of Contents (TOC), cross-references",
                "    - Mail merge architecture: Data sources, merge fields, and conditional rule filters (`IF...THEN`)",
                "• Section 5.2: Spreadsheet Applications & Quantitative Systems",
                "    - Electronic grid architecture: Cell addressing modes (Relative, Absolute, Mixed, 3D references)",
                "    - Function syntax & modeling: Mathematical, Logical (`IF`, `IFS`, `AND`, `OR`), Lookups (`INDEX-MATCH`, `XLOOKUP`)",
                "    - Financial and statistical functions (`NPV`, `IRR`, `COUNTIF`, `SUMIFS`); Pivot Tables & PivotCharts",
                "• Section 5.3: Web Browsing, Internet Protocols & Electronic Mail Architecture",
                "    - World Wide Web: URLs, HTTP/HTTPS request-response cycles, status codes, and TLS certificates",
                "    - Email protocols: SMTP (message submission/relay), POP3 vs IMAP4 (retrieval and sync)",
                "    - Email security & anti-spoofing standards: SPF, DKIM, and DMARC"
            ],
            "callout": {
                "title": "APPLICATION FOCUS",
                "body": "Master the quantitative algorithms and document automation workflows required for academic research, farm operations, and enterprise data analysis at SUA."
            }
        },
        {
            "type": "bullet",
            "title": "Topic 5: Intended Learning Outcomes (ILOs)",
            "sub_title": "Core Productivity & Communications Competencies",
            "bullets": [
                "• Engineer complex multi-section academic documents with dynamic numbering and automated tables of contents.",
                "• Design automated mail merge pipelines for dynamic reporting and student notifications.",
                "• Apply relative, absolute, mixed, and 3D cell referencing in complex spreadsheet calculations.",
                "• Formulate nested logical tests, multi-condition statistical formulas, and robust lookup architectures.",
                "• Construct dynamic business intelligence dashboards utilizing Pivot Tables, Slicers, and PivotCharts.",
                "• Dissect Uniform Resource Locators (URLs) and trace HTTP/HTTPS client-server request-response cycles.",
                "• Contrast POP3 and IMAP4 mail retrieval protocols and formulate SPF/DKIM anti-spoofing policies."
            ]
        },
        {
            "type": "bullet",
            "title": "Word Processing: Academic Document Engineering",
            "sub_title": "Beyond Basic Typing: Structural Typography and Sectioning",
            "bullets": [
                "• Document Architecture: Hierarchical layers (Document → Sections → Paragraphs → Characters).",
                "• Section Breaks vs Page Breaks:",
                "    - Page Break: Simply forces following text onto a new physical page; retains identical margins, orientation, and headers/footers.",
                "    - Section Break (Next Page): Divides document into independent formatting zones with distinct margins, page numbering formats, and orientations (Portrait vs Landscape).",
                "• Thesis Compilation Rule at SUA:",
                "    - Section 1 (Preliminary Pages): Roman numerals (i, ii, iii) centered at footer.",
                "    - Section 2 (Chapter 1 onwards): Arabic numerals (1, 2, 3) aligned at top-right.",
                "    - Unlink Headers/Footers: 'Link to Previous' MUST be disabled between sections."
            ]
        },
        {
            "type": "bullet",
            "title": "Automated Academic Referencing & Tables of Contents",
            "sub_title": "Leveraging Semantic Heading Styles for Document Integrity",
            "bullets": [
                "• The Semantic Heading Standard: Never manually format headings by changing font size and bolding.",
                "• Heading Styles (Heading 1, Heading 2, Heading 3):",
                "    - Provides semantic structure recognized by document outline compilers.",
                "    - Enables one-click generation of the automated Table of Contents (TOC).",
                "• Dynamic Updates: Modifying a chapter heading automatically updates the TOC and page numbers across a 200-page document via `F9` (Update Field).",
                "• Table of Figures & Captions: Figures and tables tagged with official captions (`Insert Caption`), generating automated lists of figures and tables.",
                "• Cross-Referencing: Dynamic links to numbered headings or figures that automatically track changes in figure numbering."
            ]
        },
        {
            "type": "bullet",
            "title": "Mail Merge Architecture & Enterprise Dispatches",
            "sub_title": "Mass Customization of Letters, Transcripts, and Advisory Notices",
            "bullets": [
                "• Core Architecture: Combines a standardized template with a structured transactional data source.",
                "• The Three Components of Mail Merge:",
                "    1. Main Document: Standardized text containing boilerplate prose and merge field placeholders (e.g., `«First_Name»`, `«Balance_Due»`).",
                "    2. Data Source: Structured tabular dataset (Excel spreadsheet, Access database, CSV file) where columns represent fields and rows represent records.",
                "    3. Merged Output Document: Consolidated multi-page file or direct email dispatch containing individual customized records.",
                "• Conditional Logic Rules: Using Word `IF...THEN...ELSE` fields to dynamically insert customized advice based on numerical thresholds (e.g., 'Warning: Overdue Payment' if `Balance > 0`)."
            ]
        },
        {
            "type": "figure",
            "title": "Spreadsheet Cell Addressing Paradigms",
            "img": "fig5_1_spreadsheet_addressing.png",
            "caption": "Relative, Absolute, Mixed, and 3D Spreadsheet Referencing Mechanisms.",
            "bullets": [
                "• Relative Referencing (`A1`): Offset-based; shifts row and column coordinates dynamically when copied across cells.",
                "• Absolute Referencing (`$A$1`): Locked coordinates via `$` anchors; remains fixed regardless of copy destination.",
                "• Mixed Referencing (`$A1` or `A$1`): Column locked and row floating, or row locked and column floating; vital for 2D multiplication tables and matrix multipliers.",
                "• 3D Referencing (`Sheet1:Sheet4!B5`): Aggregates identical cell coordinates across multiple consecutive worksheet tabs."
            ]
        },
        {
            "type": "bullet",
            "title": "Advanced Spreadsheet Functions: Logical Modeling",
            "sub_title": "Automating Multi-Condition Agricultural Decisions",
            "bullets": [
                "• Single `IF` Statement: `=IF(logical_test, value_if_true, value_if_false)`.",
                "• Boolean Operators: `=AND(condition1, condition2)` and `=OR(condition1, condition2)`.",
                "• Nested `IF` & Modern `IFS`:",
                "    - Example: Cattle Weight Gain Evaluation:",
                "    `=IFS(D2 >= 1.2, \"Superior Gain\", D2 >= 0.8, \"Normal Gain\", TRUE, \"Suboptimal - Review Feed\")`.",
                "• Multi-Condition Aggregations:",
                "    - `=COUNTIFS(Breed_Range, \"Friesian\", Yield_Range, \">=20\")`.",
                "    - `=SUMIFS(Milk_Liters, Farm_Block, \"Mazimbu\", Lactation_Stage, \"Mid\")`.",
                "    - `=AVERAGEIFS(Soil_Nitrogen, Zone, \"Uruguru\", Crop, \"Maize\")`."
            ]
        },
        {
            "type": "bullet",
            "title": "Lookup Architectures: VLOOKUP vs INDEX-MATCH vs XLOOKUP",
            "sub_title": "The Evolution of Relational Data Retrieval in Spreadsheets",
            "bullets": [
                "• `VLOOKUP` (`lookup_val, table_array, col_index, [range_lookup]`):",
                "    - Severe Limitations: Can only search left-to-right (lookup column MUST be first); breaks if columns are inserted/deleted.",
                "• `INDEX` + `MATCH` Architectural Combination:",
                "    - `=INDEX(return_range, MATCH(lookup_val, lookup_range, 0))`.",
                "    - Advantages: Unrestricted left-to-right or right-to-left retrieval; immune to column insertions; faster calculation on large datasets.",
                "• `XLOOKUP` (Modern Excel Standard):",
                "    - `=XLOOKUP(lookup_val, lookup_range, return_range, [if_not_found], [match_mode])`.",
                "    - Combines advantages of INDEX-MATCH with concise syntax and native exact-match default."
            ]
        },
        {
            "type": "bullet",
            "title": "Financial Modeling: Capital Budgeting Functions",
            "sub_title": "Evaluating Agricultural Machinery Investments at SUA",
            "bullets": [
                "• Net Present Value (`NPV`): Calculates current value of future cash inflows discounted at capital interest rate r:",
                "    - Formula: `=NPV(rate, cash_flow_range) + initial_outlay` (Note: Initial outlay in Year 0 is added outside NPV).",
                "• Internal Rate of Return (`IRR`):",
                "    - Formula: `=IRR(values_range)`.",
                "    - Calculates the exact discount rate where Net Present Value equals zero; if IRR > Cost of Capital, project is viable.",
                "• Loan Amortization (`PMT`):",
                "    - Formula: `=PMT(rate, nper, pv, [fv], [type])`.",
                "    - Computes periodic loan payment for agricultural tractor financing based on constant interest rate and fixed installments."
            ]
        },
        {
            "type": "bullet",
            "title": "Business Intelligence: Pivot Tables & PivotCharts",
            "sub_title": "Multidimensional Summarization of Enterprise Datasets",
            "bullets": [
                "• Pivot Table: High-speed analytical engine that groups, aggregates, cross-tabulates, and pivots large transactional records without writing complex formulas.",
                "• Four Core Functional Quadrants:",
                "    1. Rows: Categorical variables defining horizontal row headers (e.g., Agricultural Region).",
                "    2. Columns: Categorical variables defining vertical column headers (e.g., Crop Variety).",
                "    3. Values: Numerical fields to aggregate (Sum, Average, Count, Max, Min).",
                "    4. Filters: Global dataset criteria (e.g., Harvest Year).",
                "• Slicers & Timelines: Interactive graphical filtering buttons enabling one-click exploratory data dashboards.",
                "• Calculated Fields: Custom mathematical formulas operating on aggregated pivot table metrics."
            ]
        },
        {
            "type": "bullet",
            "title": "The World Wide Web: Architecture & URLs",
            "sub_title": "The Global Distributed Hypermedia System",
            "bullets": [
                "• Core Architecture: Client-server hypermedia infrastructure running over TCP/IP, proposed by Tim Berners-Lee (1989).",
                "• Anatomy of a Uniform Resource Locator (URL):",
                "    `https://www.sua.ac.tz:443/academics/courses?dept=diit&level=100#syllabus`",
                "    - Protocol / Scheme: `https://` (HyperText Transfer Protocol Secure).",
                "    - Fully Qualified Domain Name (FQDN): `www.sua.ac.tz` (resolved via DNS to server IP).",
                "    - Port Number: `:443` (standard encrypted TLS port; HTTP defaults to 80).",
                "    - Path: `/academics/courses` (hierarchical resource location on web server).",
                "    - Query String: `?dept=diit&level=100` (key-value parameters passed to backend script).",
                "    - Fragment / Anchor: `#syllabus` (client-side jump target within web page)."
            ]
        },
        {
            "type": "bullet",
            "title": "The HTTP/HTTPS Request-Response Cycle",
            "sub_title": "Stateless Communication and RESTful Operations",
            "bullets": [
                "• Client Request: Web browser opens TCP connection (port 80/443), sends HTTP request header:",
                "    - HTTP Methods: `GET` (retrieve resource), `POST` (submit data/payload), `PUT` (replace resource), `DELETE` (remove resource).",
                "• Server Response: Server processes request and returns HTTP status code, response headers, and payload (HTML/JSON).",
                "• Standard HTTP Status Code Classes:",
                "    - 1xx (Informational): Request received, continuing process.",
                "    - 2xx (Success): `200 OK`, `201 Created`.",
                "    - 3xx (Redirection): `301 Moved Permanently`, `302 Found`.",
                "    - 4xx (Client Error): `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`.",
                "    - 5xx (Server Error): `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`."
            ]
        },
        {
            "type": "figure",
            "title": "Electronic Mail Protocol Architecture",
            "img": "fig5_2_email_protocols_architecture.png",
            "caption": "The complete email pipeline: MUA, MSA, MTA, MDA, SMTP, POP3, and IMAP4.",
            "bullets": [
                "• Sender MUA (Outlook/Thunderbird) submits email to Mail Submission Agent (MSA) via SMTP (Port 587 with STARTTLS).",
                "• Mail Transfer Agent (MTA - Postfix/Sendmail) performs DNS MX record lookup and relays message across internet via SMTP (Port 25).",
                "• Receiving MTA transfers message to Mail Delivery Agent (MDA - Dovecot), storing it in the user's mailbox.",
                "• Recipient MUA retrieves or synchronizes mail via POP3 (Port 995) or IMAP4 (Port 993)."
            ]
        },
        {
            "type": "bullet",
            "title": "Email Retrieval: POP3 vs IMAP4",
            "sub_title": "Store-and-Forward Download vs Real-Time Server Synchronization",
            "bullets": [
                "• Post Office Protocol version 3 (POP3 - RFC 1939):",
                "    - Ports: Port 110 (plaintext), Port 995 (POP3S encrypted via TLS).",
                "    - Operational Model: Connects, downloads all messages to local computer disk, and deletes them from server mailbox by default.",
                "    - Limitations: Single-device model; read status, sent items, and custom folders do NOT synchronize across other devices (smartphone, office PC).",
                "• Internet Message Access Protocol version 4 (IMAP4 - RFC 3501):",
                "    - Ports: Port 143 (STARTTLS), Port 993 (IMAPS encrypted via TLS).",
                "    - Operational Model: All email messages, read/unread flags, drafts, and folder structures reside permanently on central server.",
                "    - Advantages: Perfect multi-device synchronization; mandatory standard for modern enterprise email."
            ]
        },
        {
            "type": "bullet",
            "title": "Email Anti-Spoofing Protocols: SPF, DKIM & DMARC",
            "sub_title": "Combatting Domain Phishing and Fraudulent Impersonation",
            "bullets": [
                "• The Vulnerability: Standard SMTP headers allow any sender to forge the `From:` address arbitrarily.",
                "• 1. SPF (Sender Policy Framework - RFC 7208):",
                "    - Domain owner publishes DNS TXT record listing authorized sending mail server IP addresses.",
                "    - Example: `v=spf1 ip4:196.216.180.15 include:_spf.google.com -all`.",
                "• 2. DKIM (DomainKeys Identified Mail - RFC 6376):",
                "    - Sending server cryptographically signs message headers with private key; recipient verifies signature using public key in sender's DNS record.",
                "• 3. DMARC (RFC 7489):",
                "    - Coordinates SPF and DKIM alignment, instructing receiving servers what to do with failing messages (`none`, `quarantine`, `reject`) and generating forensic telemetry reports."
            ]
        },
        {
            "type": "bullet",
            "title": "Academic Typography & Font Engineering",
            "sub_title": "Serif vs Sans-Serif, Kerning, Tracking, and Readability",
            "bullets": [
                "• Typeface Categories:",
                "    - Serif (e.g., Times New Roman, Georgia): Small decorative strokes at letter terminals; guides human eye across horizontal lines; traditional standard for printed body text.",
                "    - Sans-Serif (e.g., Arial, Calibri, DejaVu Sans): Clean geometric glyphs without serifs; optimal legibility on digital computer monitors and slide presentations.",
                "    - Monospaced (e.g., Courier New, Consolas): Every character occupies identical horizontal width; mandatory for code snippets, hexadecimal addresses, and tabular alignment.",
                "• Micro-Typography:",
                "    - Leading (Line Spacing): Vertical distance between baselines (academic standard: 1.5 lines or 12 pt font with 18 pt leading).",
                "    - Kerning: Dynamic spacing adjustment between specific character pairs (e.g., 'AV', 'To')."
            ]
        },
        {
            "type": "bullet",
            "title": "Document Security & The PDF/A Archival Standard",
            "sub_title": "Digital Preservation, Password Protection & Immutability",
            "bullets": [
                "• Word Document Vulnerabilities: Editable `.docx` files risk accidental formula deletion, font substitution on different operating systems, and malicious macro execution.",
                "• Portable Document Format (PDF) by Adobe (ISO 32000): Preserves exact typographical layout, vector graphics, and embedded fonts across any operating system.",
                "• PDF/A Archival Standard (ISO 19005):",
                "    - Specifically designed for 50+ year long-term digital preservation of SUA theses and university charters.",
                "    - Strict Rules: Mandates 100% font embedding; forbids external font references, dynamic JavaScript, audio/video streams, and encryption.",
                "• Document Protection Controls: Setting Document Open Passwords (AES-128/256) and Permission Passwords restricting printing or text copying."
            ]
        },
        {
            "type": "bullet",
            "title": "Spreadsheet Data Validation & Input Sanitization",
            "sub_title": "Preventing Garbage-In Garbage-Out at the Data Entry Layer",
            "bullets": [
                "• Data Validation Engine: Enforces strict data-entry rules on worksheet cells before values are committed.",
                "• Validation Rule Categories:",
                "    - Whole Number / Decimal: Constrains numerical ranges (e.g., Soil pH must be between 3.5 and 9.5).",
                "    - In-Cell Dropdown List: Restricts entries to predefined lookup tables (e.g., `Maize, Rice, Cassava, Sorghum`), eliminating typographical spelling variations.",
                "    - Date Constraints: Ensures transaction dates fall within the active academic semester.",
                "    - Custom Formulas: Uses boolean formulas (e.g., `=ISNUMBER(SEARCH(\"@sua.ac.tz\", C2))` enforcing valid university email addresses).",
                "• Error Alert Styles: Stop (blocks input completely), Warning (prompts confirmation), Information."
            ]
        },
        {
            "type": "bullet",
            "title": "Conditional Formatting: Dynamic Visual Analytics",
            "sub_title": "Automating Visual Anomaly Detection in Experimental Data",
            "bullets": [
                "• Core Concept: Automatically changes cell background color, font formatting, or border based on cell values or custom evaluation formulas.",
                "• Visualization Types:",
                "    - Data Bars: In-cell horizontal bars proportional to cell value, creating instant mini-histograms.",
                "    - Color Scales (Heatmaps): Multi-color gradients (e.g., Green-Yellow-Red) highlighting temperature or yield distribution across 100 farm plots.",
                "    - Icon Sets: Directional arrows, checkmarks, and flags indicating performance above or below benchmark thresholds.",
                "• Formula-Driven Formatting: Highlighting an entire row if a dairy cow's status is 'Quarantine':",
                "    - Rule Formula: `=$F2 = \"Quarantine\"` (applies format across all columns A:G)."
            ]
        },
        {
            "type": "bullet",
            "title": "What-If Analysis: Goal Seek & Scenario Manager",
            "sub_title": "Decision Support and Sensitivity Modeling for Agribusiness",
            "bullets": [
                "• Goal Seek (Backwards Optimization):",
                "    - Calculates the specific input value required to achieve a desired target output value in a formula cell.",
                "    - Example: Determine the maximum tractor loan interest rate allowable to keep monthly payments below 2,500,000 TZS.",
                "• Data Tables (Sensitivity Tables):",
                "    - 1-Variable Table: Shows how varying one input (e.g., fertilizer price) impacts multiple output metrics (profit, ROI, yield).",
                "    - 2-Variable Table: Shows how simultaneously varying two inputs (e.g., rainfall volume vs fertilizer rate) impacts total farm revenue.",
                "• Scenario Manager: Stores multiple named sets of input assumptions (e.g., 'Drought Worst-Case', 'Average Rain', 'Abundant Harvest') and generates comparative summary reports."
            ]
        },
        {
            "type": "bullet",
            "title": "Date and Time Arithmetic in Spreadsheets",
            "sub_title": "Serial Day Numbers and Chronological Calculations",
            "bullets": [
                "• The Underlying Storage Model: Excel stores dates as sequential serial integers starting from January 1, 1900 (Day 1). Today's date is an integer ~46,000.",
                "• Time Storage: Stored as fractional decimal days (e.g., `0.5` = 12:00 PM noon; `0.75` = 6:00 PM).",
                "• Essential Date Functions:",
                "    - `=TODAY()`: Returns current system date (volatile function).",
                "    - `=NOW()`: Returns current system date and exact time.",
                "    - `=DATEDIF(start_date, end_date, \"Y\")`: Computes complete elapsed years between dates (useful for animal ages or employee service length).",
                "    - `=NETWORKDAYS(start_date, end_date, [holidays])`: Calculates exact working business days, automatically excluding weekends and Tanzanian national holidays."
            ]
        },
        {
            "type": "bullet",
            "title": "String Manipulation & Data Cleaning Formulas",
            "sub_title": "Parsing, Cleansing, and Standardizing Raw Text Datasets",
            "bullets": [
                "• The Raw Data Problem: Imported government or lab text files frequently contain irregular leading spaces, mixed capitalization, and concatenated identifiers.",
                "• Text Cleansing Functions:",
                "    - `=TRIM(text)`: Strips all leading, trailing, and duplicate inner spaces.",
                "    - `=PROPER(text)` / `=UPPER(text)` / `=LOWER(text)`: Standardizes capitalization.",
                "• Substring Extraction:",
                "    - `=LEFT(text, num_chars)` and `=RIGHT(text, num_chars)`.",
                "    - `=MID(text, start_pos, num_chars)`: Extracts middle tokens (e.g., extracting year from `SUA-2026-AGR`).",
                "    - `=LEN(text)`: Returns exact character length.",
                "• Delimited Concatenation:",
                "    - `=TEXTJOIN(\", \", TRUE, A2:D2)`: Concatenates ranges with commas, automatically skipping blank cells."
            ]
        },
        {
            "type": "bullet",
            "title": "Modern Dynamic Arrays & The Spill Engine",
            "sub_title": "Next-Generation Formula Execution in Microsoft Excel",
            "bullets": [
                "• Dynamic Array Revolution: A single formula written in one cell can automatically return multiple values that 'spill' into neighboring cells.",
                "• The `#SPILL!` Error: Occurs when the anticipated output range is blocked by existing text or values in any of the destination cells.",
                "• Essential Dynamic Array Functions:",
                "    - `=UNIQUE(array)`: Extracts deduplicated list of unique values (e.g., unique farmer names from 5,000 delivery rows).",
                "    - `=FILTER(array, include_criteria, [if_empty])`: Returns rows matching specific criteria without creating pivot tables.",
                "    - `=SORT(array, [sort_index], [sort_order])`: Sorts ranges dynamically.",
                "    - `=SEQUENCE(rows, [cols], [start], [step])`: Generates arithmetic integer sequences instantly."
            ]
        },
        {
            "type": "bullet",
            "title": "Web Browser Engine Architecture",
            "sub_title": "Parsing HTML, Constructing the DOM, and JavaScript Execution",
            "bullets": [
                "• Core Subsystems of a Modern Web Browser:",
                "    1. User Interface: Address bar, back/forward buttons, bookmarking menu.",
                "    2. Browser Engine: Coordinates actions between UI and rendering engine.",
                "    3. Rendering Engine: Parses HTML and CSS to render graphical web pages (Blink in Chrome/Edge, Gecko in Firefox, WebKit in Safari).",
                "    4. JavaScript Engine: Compiles and executes script code (V8 in Chrome, SpiderMonkey in Firefox).",
                "    5. Networking Layer: Handles HTTP/HTTPS, DNS resolution, and TLS handshakes.",
                "• Critical Rendering Path:",
                "    - Parses HTML → Builds Document Object Model (DOM) tree.",
                "    - Parses CSS → Builds CSS Object Model (CSSOM) tree.",
                "    - Combines DOM + CSSOM → Render Tree → Layout phase → Paint phase."
            ]
        },
        {
            "type": "bullet",
            "title": "Web State Management: Cookies vs LocalStorage",
            "sub_title": "Maintaining Stateful Sessions Across Stateless HTTP",
            "bullets": [
                "• HTTP is Stateless: Each HTTP request is completely independent; servers do not remember previous requests without state mechanisms.",
                "• HTTP Cookies (RFC 6265): Small key-value text pairs (max 4 KB) stored by browser and transmitted back to server with EVERY HTTP request header.",
                "    - Session Cookies: Stored in volatile RAM; deleted when browser closes.",
                "    - Persistent Cookies: Stored on disk until expiration date (e.g., 'Remember Me' logins).",
                "    - Security Flags: `Secure` (transmitted only over HTTPS), `HttpOnly` (inaccessible to JavaScript, neutralizing XSS credential theft), `SameSite=Strict` (prevents CSRF attacks).",
                "• HTML5 Web Storage: `localStorage` (persists indefinitely, 5–10 MB, client-side only) and `sessionStorage` (cleared on tab close)."
            ]
        },
        {
            "type": "bullet",
            "title": "Domain Name System (DNS) Hierarchical Resolution",
            "sub_title": "Translating Human Hostnames into Machine IP Addresses",
            "bullets": [
                "• The Phonebook of the Internet: Resolves `www.sua.ac.tz` to IPv4 `196.216.180.15`.",
                "• The Hierarchical Tree Architecture:",
                "    1. Root DNS Servers (`.`): 13 logical root server clusters managed globally via Anycast routing.",
                "    2. Top-Level Domain (TLD) Servers: Manage gTLDs (`.com`, `.org`) and ccTLDs (`.tz`, `.ke`).",
                "    3. Authoritative Nameservers: Hold official master DNS records for the organization domain (`sua.ac.tz`).",
                "• Essential DNS Record Types:",
                "    - `A` Record: Maps hostname to 32-bit IPv4 address.",
                "    - `AAAA` Record: Maps hostname to 128-bit IPv6 address.",
                "    - `CNAME` (Canonical Name): Alias mapping one hostname to another.",
                "    - `MX` (Mail Exchanger): Identifies mail servers responsible for domain email.",
                "    - `TXT`: Arbitrary text; houses SPF, DKIM public keys, and domain ownership tokens."
            ]
        },
        {
            "type": "bullet",
            "title": "Transport Layer Security (TLS 1.3) Handshake",
            "sub_title": "Establishing Encrypted, Tamper-Proof HTTPS Sessions",
            "bullets": [
                "• Core Goals: Confidentiality (AES-GCM encryption), Integrity (HMAC authentication), Server Authenticity (X.509 digital certificate).",
                "• TLS 1.3 Rapid Handshake Sequence (1-RTT Round Trip Time):",
                "    1. `ClientHello`: Client sends supported cipher suites and ephemeral Diffie-Hellman public key share.",
                "    2. `ServerHello`: Server selects cipher suite, sends its own key share, its X.509 certificate, and digital signature.",
                "    3. Session Key Derivation: Both parties independently calculate the shared symmetric Master Secret using Diffie-Hellman math.",
                "    4. Encrypted Transmission: All subsequent HTTP requests and responses encrypted with high-speed AES-256-GCM.",
                "• Perfect Forward Secrecy (PFS): Even if the server's master private key is stolen years later, past recorded encrypted sessions cannot be decrypted."
            ]
        },
        {
            "type": "bullet",
            "title": "Cloud Productivity Ecosystems in Academic Research",
            "sub_title": "Microsoft 365, Google Workspace, and Private Clouds",
            "bullets": [
                "• Collaborative Cloud Architecture: Real-time co-authoring using Operational Transformation (OT) and Conflict-Free Replicated Data Types (CRDT).",
                "• Enterprise Cloud Suites:",
                "    - Microsoft 365: Word Online, Excel Online, OneDrive, SharePoint; deep enterprise Active Directory integration.",
                "    - Google Workspace: Google Docs, Sheets, Drive; streamlined browser-native collaboration.",
                "    - Self-Hosted Private Clouds (Nextcloud / ownCloud): Deployed on SUA DIIT servers to ensure sensitive national agricultural research data remains sovereign within Tanzanian borders.",
                "• Cloud Storage Mechanics: Delta sync (transmitting only modified byte blocks of large files) and continuous versioning allowing rollback to previous revisions."
            ]
        },
        {
            "type": "bullet",
            "title": "Topic 5: Key Takeaways & Synthesis Matrix",
            "sub_title": "Summary of Applications & Networking for Examination Mastery",
            "bullets": [
                "• Document Engineering: Section breaks isolate independent formatting; heading styles empower dynamic tables of contents; mail merge automates mass communications.",
                "• Spreadsheet Referencing: Relative (`A1`) shifts dynamically; Absolute (`$A$1`) stays locked; Mixed (`$A1`/`A$1`) locks one coordinate.",
                "• Advanced Formulas: Logical `IFS`/`COUNTIFS`/`SUMIFS` automate multi-criteria decisions; `INDEX-MATCH` and `XLOOKUP` provide flexible relational lookups.",
                "• Web Infrastructure: URLs specify protocol, host, port, path, and query; HTTP request-response cycle handles stateless web interactions.",
                "• Email Architecture: SMTP relays messages server-to-server; IMAP4 provides multi-device synchronized retrieval; SPF/DKIM/DMARC eliminate domain spoofing."
            ]
        },
        {
            "type": "bullet",
            "title": "Review Quiz & Knowledge Check",
            "sub_title": "Self-Testing Key Software & Protocol Principles",
            "bullets": [
                "1. Why is a Section Break mandatory if you need Chapter 4 of a thesis in Landscape and Chapter 5 in Portrait?",
                "2. When copying formula `=$C$2 * D5` from cell E5 to E6, what will the resulting formula be? (Ans: `=$C$2 * D6`).",
                "3. Explain two major technical reasons why `INDEX` + `MATCH` is superior to `VLOOKUP` in Excel.",
                "4. Differentiate between POP3 and IMAP4 regarding multi-device message synchronization.",
                "5. What does the `-all` mechanism at the end of an SPF DNS TXT record instruct receiving mail servers to do?"
            ]
        },
        {
            "type": "bullet",
            "title": "Reading Assignments & Homework Notice",
            "sub_title": "Preparation for Next Lecture & Continuous Assessment",
            "bullets": [
                "• Required Readings:",
                "    - Walkenbach, J. - Microsoft Excel 2019 Bible, Chapters 3, 5, 8, 11 & 14.",
                "    - Kurose & Ross - Computer Networking: A Top-Down Approach (8th Ed.), Chapter 2 (Application Layer).",
                "• Homework Assignment 5 Notice:",
                "    - Available on SUA Moodle / Assignment directory: `BIT_111_Assignment_5.pdf`.",
                "    - Total Allocation: 100 Marks (Covers Academic Document Structuring, Advanced Excel Models, and Email Protocols).",
                "    - Submission Deadline: End of Week 10 by 17:00 EAT.",
                "• Next Lecture Preview: Topic 6 — Data Security and Malware Defense (Physical Protection, Cryptography, Anti-Malware)."
            ]
        }
    ]

# -------------------------------------------------------------
# TOPIC 6 SLIDES DATA
# -------------------------------------------------------------
def get_topic_6_slides():
    return [
        {
            "type": "bullet",
            "title": "Topic 6: Lecture Outline & Learning Roadmap",
            "sub_title": "Data Security, Malware Defense & Cryptography (Coverage: 6.1, 6.2, 6.3)",
            "bullets": [
                "• Section 6.1: Physical & Environmental Data Protection",
                "    - Datacenter environmental threats: Power disturbances (sags, spikes, surges, blackouts)",
                "    - Uninterruptible Power Supplies (UPS): Standby, Line-Interactive, Online Double-Conversion topologies",
                "    - Environmental controls: HVAC cooling, ASHRAE standards, and clean agent fire suppression (FM-200)",
                "    - Backup engineering: Full, Differential, Incremental strategies; The 3-2-1 backup rule; RTO vs RPO",
                "• Section 6.2: Controlling Unauthorized Logical Access & Applied Cryptography",
                "    - Identification, Authentication, Authorization, Accounting (IAAA); Kerckhoffs's Principle",
                "    - Symmetric cryptography: AES, block cipher operational modes (ECB vs CBC vs GCM)",
                "    - Asymmetric cryptography: RSA, Elliptic Curve (ECC), Public/Private key pairs, Digital Signatures",
                "    - Cryptographic hash functions (SHA-256) and Public Key Infrastructure (PKI / X.509)",
                "• Section 6.3: Malware Classifications, Attack Vectors & Anti-Malware Defense",
                "    - Malware taxonomy: Viruses, Worms, Trojans, Ransomware, Spyware, Rootkits, Botnets",
                "    - Defensive technologies: Signatures, Heuristics, Behavioral monitoring, Sandboxing, EDR",
                "    - Incident response lifecycle: NIST SP 800-61 framework (Containment, Eradication, Recovery)"
            ],
            "callout": {
                "title": "CAPSTONE TOPIC",
                "body": "Protecting digital agricultural assets, research findings, and institutional infrastructure against physical failure, logical intrusion, and malicious software attacks."
            }
        },
        {
            "type": "bullet",
            "title": "Topic 6: Intended Learning Outcomes (ILOs)",
            "sub_title": "Core Information Assurance Competencies",
            "bullets": [
                "• Formulate comprehensive physical and environmental security controls for institutional datacenters.",
                "• Calculate UPS power sizing requirements (Watts vs VA) and evaluate UPS circuit topologies.",
                "• Design enterprise backup schedules meeting strict Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO).",
                "• Contrast Symmetric (AES) and Asymmetric (RSA/ECC) encryption in key management and throughput.",
                "• Explain the cryptographic mechanism of digital signatures in guaranteeing authenticity and non-repudiation.",
                "• Classify malware specimens according to infection vectors, replication mechanisms, and payload capabilities.",
                "• Execute the NIST SP 800-61 Computer Security Incident Response lifecycle against live threat outbreaks."
            ]
        },
        {
            "type": "bullet",
            "title": "The CIA Triad: Foundations of Data Security",
            "sub_title": "Confidentiality, Integrity, Availability within Academic Computing",
            "bullets": [
                "• 1. Confidentiality: Assurance that information is not disclosed to unauthorized individuals, entities, or processes.",
                "    - Threats: Eavesdropping, packet sniffing, credential theft, unauthorized database dumps.",
                "    - Mitigations: Whole Disk Encryption (BitLocker), TLS network encryption, Least Privilege access.",
                "• 2. Integrity: Guarding against improper information modification or destruction; ensuring non-repudiation and authenticity.",
                "    - Threats: Unauthorized data tampering, man-in-the-middle alterations, silent bit-rot.",
                "    - Mitigations: SHA-256 cryptographic hashes, digital signatures, database transaction ACID logs.",
                "• 3. Availability: Ensuring timely, reliable access to data and computational services for authorized users.",
                "    - Threats: Distributed Denial of Service (DDoS), ransomware encryption, power grid failure, hardware faults.",
                "    - Mitigations: Redundant UPS power, RAID arrays, automated offsite backups, disaster recovery clusters."
            ]
        },
        {
            "type": "bullet",
            "title": "Environmental Security: Power Disturbances",
            "sub_title": "Protecting Microcomputers from Electrical Grid Anomalies",
            "bullets": [
                "• Power Disturbance Taxonomy:",
                "    - Blackout: Complete loss of electrical power for seconds to days; causes sudden system halting and uncommitted cache data loss.",
                "    - Brownout (Sag): Prolonged drop in voltage below nominal levels (e.g., drops to 170V on 230V mains); forces power supplies to draw excessive current, overheating capacitors.",
                "    - Spike / Surge: Transient high-voltage pulse (microseconds to milliseconds) reaching thousands of volts (lightning, industrial switching); destroys silicon semiconductor gates.",
                "    - Electrical Noise (EMI/RFI): High-frequency fluctuations disrupting digital signals on motherboard traces.",
                "• Mitigations: Surge protectors (Metal Oxide Varistors - MOVs), Automatic Voltage Regulators (AVRs), clean dedicated earth grounding, and Uninterruptible Power Supplies (UPS)."
            ]
        },
        {
            "type": "bullet",
            "title": "Uninterruptible Power Supply (UPS) Topologies",
            "sub_title": "Evaluating Standby vs Line-Interactive vs Online Double-Conversion",
            "bullets": [
                "• 1. Standby (Offline) UPS:",
                "    - Inverter remains idle; utility power passes directly to load; battery engages via transfer switch during outage.",
                "    - Transfer Time: 4 to 12 ms; acceptable for consumer PCs, unacceptable for sensitive enterprise servers.",
                "• 2. Line-Interactive UPS:",
                "    - Includes multi-tap autotransformer (AVR) that boosts low voltages and bucks high voltages without depleting battery.",
                "    - Transfer Time: 2 to 4 ms; standard choice for office workstations and network closets.",
                "• 3. Online Double-Conversion UPS (Enterprise Gold Standard):",
                "    - Incoming AC power continuously rectified to DC, which continuously charges battery and feeds inverter generating pristine new AC.",
                "    - Transfer Time: EXACTLY 0 ms (Zero transfer time); provides absolute electrical isolation from grid disturbances."
            ]
        },
        {
            "type": "bullet",
            "title": "Quantitative UPS Power Sizing Calculations",
            "sub_title": "Real Power (Watts) versus Apparent Power (Volt-Amperes)",
            "bullets": [
                "• Real Power (P, Watts): Actual electrical power consumed by hardware performing work: P = V · I · cos(θ).",
                "• Apparent Power (S, Volt-Amperes): Total power flowing through the circuit: S = V · I.",
                "• Power Factor (PF): Ratio of Real Power to Apparent Power: PF = P / S = cos(θ) (typically 0.8 to 0.95 for modern IT).",
                "• Sizing Equation: Required UPS Rating (VA) = Total Connected Watts / Power Factor.",
                "• Worked Sizing Example for SUA DIIT Lab:",
                "    - Connected Load: 20 Microcomputers @ 250 W each = 5,000 W.",
                "    - Power Factor of switched-mode power supplies = 0.85.",
                "    - Apparent Power = 5,000 W / 0.85 = 5,882 VA ≈ 5.88 kVA.",
                "    - Applying 25% safety expansion headroom = 5.88 kVA × 1.25 = 7.35 kVA.",
                "    - Specification Recommendation: Procure an 8 kVA or 10 kVA Online Double-Conversion UPS."
            ]
        },
        {
            "type": "figure",
            "title": "The 3-2-1 Enterprise Backup Rule",
            "img": "fig6_1_backup_321_rule.png",
            "caption": "The gold standard for disaster recovery: 3 copies, 2 different media, 1 offsite/air-gapped copy.",
            "bullets": [
                "• 3 Copies of Data: Maintain the original production data plus at least 2 distinct backup copies.",
                "• 2 Different Storage Media: Utilize diverse media types (e.g., NVMe NAS server + magnetic LTO tape or optical disc) to eliminate media-specific systemic failures.",
                "• 1 Offsite or Air-Gapped Copy: Store at least one copy in a geographically separate facility or cloud vault completely disconnected from the network to survive fire, floods, and ransomware outbreaks.",
                "• Immutability: Write-Once-Read-Many (WORM) storage locks preventing ransomware from deleting backups."
            ]
        },
        {
            "type": "bullet",
            "title": "Backup Strategies: Full, Differential & Incremental",
            "sub_title": "Balancing Backup Window Duration with Restoration Complexity",
            "bullets": [
                "• Full Backup: Copies every single file across the entire selected volume; resets the Archive (`A`) attribute bit.",
                "    - Pros: Fastest and simplest restore (requires only 1 backup set).",
                "    - Cons: Takes the longest time to run; consumes massive storage capacity.",
                "• Differential Backup: Copies only files that have been created or modified since the LAST FULL backup; does NOT reset the Archive bit.",
                "    - Pros: Fast restore (requires Full Backup + Latest Single Differential Backup).",
                "    - Cons: Daily backup size grows progressively larger as week advances.",
                "• Incremental Backup: Copies only files created or modified since the LAST BACKUP OF ANY KIND (Full or Incremental); resets the Archive bit.",
                "    - Pros: Fastest backup execution; minimal daily storage consumption.",
                "    - Cons: Slowest, most complex restore (requires Full Backup + ALL sequential intermediate incrementals)."
            ]
        },
        {
            "type": "bullet",
            "title": "Disaster Recovery Metrics: RTO and RPO",
            "sub_title": "Defining Quantitative Tolerances for Downtime and Data Loss",
            "bullets": [
                "• Recovery Point Objective (RPO):",
                "    - The maximum acceptable age of files that must be recovered from backup storage for normal operations to resume.",
                "    - Measures acceptable data loss in time (e.g., an RPO of 4 hours means the organization can tolerate losing at most 4 hours of transactional work).",
                "    - Dictates the frequency of backup snapshots.",
                "• Recovery Time Objective (RTO):",
                "    - The maximum acceptable duration of time that a system can remain offline following a disaster before normal service is restored.",
                "    - Measures acceptable downtime (e.g., an RTO of 2 hours means systems must be fully re-imaged, data restored, and online within 120 minutes).",
                "    - Dictates disaster recovery infrastructure (hot standby sites vs cold tape restores)."
            ]
        },
        {
            "type": "bullet",
            "title": "Cryptographic Foundations & Kerckhoffs's Principle",
            "sub_title": "The Mathematical Shield Protecting Digital Communications",
            "bullets": [
                "• Kerckhoffs's Principle (Auguste Kerckhoffs, 1883):",
                "    - 'A cryptosystem should be secure even if everything about the system, except the key, is public knowledge.'",
                "    - Elimination of 'Security through Obscurity': Robust algorithms (AES, RSA) rely on public mathematical rigor, not secret proprietary code.",
                "• Fundamental Concepts:",
                "    - Plaintext (P): Original unencrypted human-readable or binary data.",
                "    - Ciphertext (C): Encrypted scrambled data output by cipher: C = E<sub>K</sub>(P).",
                "    - Key (K): Secret mathematical parameter controlling encryption and decryption transformations.",
                "    - Decryption: Inversion operation returning plaintext: P = D<sub>K</sub>(C)."
            ]
        },
        {
            "type": "bullet",
            "title": "Symmetric Cryptography: AES and Operational Modes",
            "sub_title": "Shared Secret Keys, High Throughput, and Block Cipher Modes",
            "bullets": [
                "• Symmetric Cipher Principle: A single secret key is shared between sender and recipient for both encryption and decryption.",
                "• Advanced Encryption Standard (AES - FIPS 197):",
                "    - Rijndael substitution-permutation network operating on fixed 128-bit blocks.",
                "    - Key lengths: 128, 192, or 256 bits (10, 12, or 14 transformation rounds).",
                "    - Hardware Acceleration: Modern CPUs integrate AES-NI instruction set executing at > 5 GB/s.",
                "• Block Cipher Modes of Operation:",
                "    - ECB (Electronic Codebook): Each 128-bit block encrypted independently with same key; CRITICALLY FLAWED (preserves plaintext patterns; e.g., ECB Penguin).",
                "    - CBC (Cipher Block Chaining): Each plaintext block is XORed with previous ciphertext block before encryption; uses Initialization Vector (IV).",
                "    - GCM (Galois/Counter Mode): Modern standard; combines high-speed counter mode encryption with authenticated data integrity (AEAD)."
            ]
        },
        {
            "type": "bullet",
            "title": "Asymmetric Cryptography & Digital Signatures",
            "sub_title": "Public-Key Mathematics: RSA, Elliptic Curves, and Non-Repudiation",
            "bullets": [
                "• Asymmetric Cipher Principle: Utilizes a mathematically linked Key Pair:",
                "    - Public Key: Distributed openly to the entire world; used to encrypt messages or verify signatures.",
                "    - Private Key: Kept strictly secret by the owner; used to decrypt messages or generate signatures.",
                "• Mathematical Trapdoor Functions:",
                "    - RSA: Based on difficulty of factoring product of two massive prime numbers (2048 to 4096 bits).",
                "    - ECC (Elliptic Curve Cryptography): Based on discrete logarithm problem over elliptic curve points (256-bit ECC provides equivalent security to 3072-bit RSA with 1/10th the compute power).",
                "• Digital Signature Mechanics:",
                "    1. Sender hashes document: H = SHA-256(Doc).",
                "    2. Sender encrypts hash with their PRIVATE KEY to produce the Digital Signature.",
                "    3. Recipient decrypts signature using sender's PUBLIC KEY, recalculates hash, and compares. Matching hashes proves Authenticity, Integrity, and Non-Repudiation."
            ]
        },
        {
            "type": "figure",
            "title": "Comprehensive Malware Taxonomy",
            "img": "fig6_2_malware_taxonomy.png",
            "caption": "Taxonomy of malicious software classified by propagation vector, persistence, and payload.",
            "bullets": [
                "• Autonomous Propagators: Worms (network-scanning automated infectors).",
                "• Host-Dependent Infectors: File viruses, macro viruses, boot sector infectors.",
                "• Deceptive Delivery: Trojan Horses, disguised utilities, fake installers.",
                "• Destructive & Extortion Payloads: Ransomware (crypto-lockers), Wiper malware.",
                "• Espionage & Surveillance: Spyware, Keyloggers, Infostealers, Remote Access Trojans (RATs).",
                "• Deep Stealth & Subversion: Rootkits (Kernel-mode hooks, hypervisor rootkits, firmware bootkits)."
            ]
        },
        {
            "type": "bullet",
            "title": "Malware Analysis: Viruses vs Worms vs Trojans",
            "sub_title": "Contrasting Infection Vectors and Propagation Dynamics",
            "bullets": [
                "• Computer Virus:",
                "    - Parasitic code that attaches itself to an existing legitimate host executable file (`.exe`, `.docx` macro, boot sector).",
                "    - REQUIRES human intervention to propagate (e.g., executing the infected file, inserting an infected USB drive).",
                "• Computer Worm:",
                "    - Standalone autonomous program that self-replicates across computer networks without human interaction.",
                "    - Scans IP subnets, exploits unpatched network vulnerabilities (e.g., buffer overflows, SMB bugs), and copies itself (e.g., Morris Worm, Code Red, Conficker).",
                "• Trojan Horse:",
                "    - Program that appears useful or benign (e.g., 'Free Anti-Virus', 'Crack.exe') but conceals hidden malicious functionality.",
                "    - Does NOT self-replicate; relies on deception and social engineering to establish backdoors."
            ]
        },
        {
            "type": "bullet",
            "title": "Ransomware: Anatomy of Modern Cyber Extortion",
            "sub_title": "Cryptographic Hijacking, Double Extortion, and The WannaCry Outbreak",
            "bullets": [
                "• Ransomware Execution Cycle:",
                "    1. Initial Access: Phishing email attachment, vulnerable RDP service, or drive-by download.",
                "    2. Reconnaissance & Privilege Escalation: Discovers active directory shares, deletes local shadow copies (`vssadmin delete shadows /all /quiet`).",
                "    3. Hybrid Encryption Phase: Generates local symmetric AES key, rapidly encrypts user files (`.docx`, `.xlsx`, `.pdf`), and encrypts the AES key using attacker's master RSA-2048 public key.",
                "    4. Ransom Demand: Displays ransom note demanding cryptocurrency payment (Bitcoin, Monero) in exchange for private decryption key.",
                "• Double Extortion: Attackers exfiltrate confidential enterprise data to leak sites before encryption, threatening public release if ransom is unpaid.",
                "• WannaCry Outbreak (2017): Combined ransomware with the EternalBlue worm exploit (CVE-2017-0144), paralyzing >200,000 systems in hours."
            ]
        },
        {
            "type": "bullet",
            "title": "Spyware, Rootkits, and Botnet Architectures",
            "sub_title": "Stealth Surveillance, Kernel Subversion, and Coordinated Attacks",
            "bullets": [
                "• Spyware & Keyloggers: Covertly monitors user activity, capturing keystrokes (stealing passwords), capturing screen grabs, and logging web browsing history.",
                "• Rootkits:",
                "    - Set of software tools designed to maintain administrator/root access while concealing its presence from the OS.",
                "    - User-Mode: Hooks Windows API DLLs to filter directory listings and process trees.",
                "    - Kernel-Mode: Modifies kernel system call dispatch tables (SSDT) or kernel memory, rendering detection by standard anti-virus impossible.",
                "• Botnets (Zombie Networks):",
                "    - Thousands of compromised microcomputers infected with bots reporting to Command-and-Control (C2) servers.",
                "    - Capabilities: Launching massive Distributed Denial of Service (DDoS) flood attacks, sending spam, mining cryptocurrency."
            ]
        },
        {
            "type": "bullet",
            "title": "Modern Anti-Malware Defense Methodologies",
            "sub_title": "Beyond Signatures: Heuristics, Behavior & Endpoint Detection and Response",
            "bullets": [
                "• 1. Signature-Based Detection:",
                "    - Scans files for static sequences of bytes or SHA-256 hashes matching known malware repository.",
                "    - Critical Flaw: Completely blind to Zero-Day exploits and Polymorphic/Metamorphic malware that mutates its binary code on every infection.",
                "• 2. Heuristic Analysis:",
                "    - Decompiles code and searches for suspicious code patterns (e.g., hidden encryption routines, attempts to overwrite MBR).",
                "• 3. Behavioral Monitoring (Anomaly Detection):",
                "    - Continuously inspects active running processes for malicious behavioral anomalies (e.g., process injecting code into `lsass.exe` or rapidly modifying hundreds of files).",
                "• 4. Endpoint Detection and Response (EDR) & Sandboxing:",
                "    - Detonates suspicious executables within isolated micro-virtual machines to analyze network callbacks and filesystem writes before admitting into production."
            ]
        },
        {
            "type": "bullet",
            "title": "NIST Incident Response Lifecycle (NIST SP 800-61)",
            "sub_title": "The Four Phases of Enterprise Cyber Incident Handling",
            "bullets": [
                "• Phase 1 - Preparation: Deploying EDR sensors, hardening endpoints, establishing offline backups, and training incident response team.",
                "• Phase 2 - Detection & Analysis: Monitoring SIEM alerts, determining infection scope, identifying initial attack vector and compromised hosts.",
                "• Phase 3 - Containment, Eradication & Recovery:",
                "    - Short-Term Containment: Isolating infected hosts from network (disconnecting Ethernet / blocking VLANs) while preserving volatile RAM forensics.",
                "    - Eradication: Terminating malicious processes, removing scheduled task persistence mechanisms, applying missing patches.",
                "    - Recovery: Re-imaging systems from known clean gold masters, restoring data from verified immutable backups, verifying security controls.",
                "• Phase 4 - Post-Incident Activity: Conducting 'Lessons Learned' debrief, updating incident response playbooks, and sharing threat intelligence."
            ]
        },
        {
            "type": "bullet",
            "title": "Datacenter Climate Control: HVAC & Thermal Containment",
            "sub_title": "ASHRAE Standards, Static Electricity, and Relative Humidity",
            "bullets": [
                "• The Thermal Threat: Silicon processors generate intense heat (100–300W per CPU socket). Excessive heat causes thermal throttling, hardware degradation, and premature capacitor blowout.",
                "• ASHRAE TC 9.9 Thermal Guidelines for Datacenters:",
                "    - Recommended Operating Temperature: 18°C to 27°C (64.4°F to 80.6°F).",
                "    - Relative Humidity (RH) Envelope: 40% to 60%.",
                "• Humidity Extremes Threat Model:",
                "    - Low Humidity (< 30%): Generates Electrostatic Discharge (ESD); a tiny static spark (> 3,000V) destroys sensitive MOSFET gates on motherboard circuits.",
                "    - High Humidity (> 70%): Causes moisture condensation and conductive dust bridging, triggering destructive short circuits.",
                "• Hot-Aisle / Cold-Aisle Containment: Physical separation of cold intake airflow from exhausted hot server air, improving cooling efficiency by >30%."
            ]
        },
        {
            "type": "bullet",
            "title": "Fire Suppression in Datacenters: Clean Gaseous Agents",
            "sub_title": "Class C Electrical Fire Suppression Without Liquid Damage",
            "bullets": [
                "• The Datacenter Fire Challenge: Water sprinklers cause instant electrical shorts and permanently ruin millions of shillings of server hardware.",
                "• Clean Agent Gaseous Systems (NFPA 2001):",
                "    - FM-200 (Heptafluoropropane) & Novec 1230 (Fluoroketone): Electrically non-conductive, leaves zero chemical residue, extinguishes fires within 10 seconds by absorbing heat at molecular level.",
                "    - Inergen (Nitrogen / Argon / CO<sub>2</sub> blend): Displaces atmospheric oxygen down to 12.5% (starves fire while remaining breathable for humans for short periods).",
                "• Pre-Action Water Sprinkler Systems: Pipes remain dry until two independent smoke detectors trigger, preventing accidental sprinkler burst damage."
            ]
        },
        {
            "type": "bullet",
            "title": "Physical Perimeter Security & Defense-in-Depth",
            "sub_title": "Concentric Security Rings Protecting University Datacenters",
            "bullets": [
                "• Concentric Circles of Protection:",
                "    - Outer Ring: Perimeter fencing, security gates, vehicle barriers, 24/7 security guards.",
                "    - Middle Ring: External building access controlled by proximity RFID keycards and CCTV cameras.",
                "    - Inner Ring (Server Room): Biometric fingerprint/iris locks, mantrap interlock portals (preventing 'tailgating' / piggybacking), anti-passback rules.",
                "    - Core Ring (Equipment Racks): Keyed rack cabinet locks and server chassis intrusion sensors.",
                "• Cable & Device Theft Defenses: Kensington security slots, steel security cabling, and locking port covers."
            ]
        },
        {
            "type": "bullet",
            "title": "Cryptographic Key Lifecycle Management",
            "sub_title": "From Generation to Secure Destruction (NIST SP 800-57)",
            "bullets": [
                "• Security Principle: A cryptographic algorithm is only as secure as the protection of its secret keys.",
                "• The Six Phases of Key Management:",
                "    1. Generation: Generated using a certified Hardware True Random Number Generator (TRNG) with high physical entropy.",
                "    2. Distribution & Exchange: Exchanged securely using asymmetric trapdoor functions (Diffie-Hellman) or Key Encapsulation Mechanisms (KEM).",
                "    3. Storage: Stored inside dedicated Hardware Security Modules (HSMs) or TPM chips; never stored in plaintext on disk.",
                "    4. Usage & Access: Strict authorization enforcing separation of duties; keys restricted to specific operations (e.g., signing only, encryption only).",
                "    5. Rotation (Crypto-Period): Regular scheduled retirement of old keys to limit the volume of ciphertext encrypted under a single key.",
                "    6. Revocation & Destruction: Immediate zeroization when compromised; publishing revocation to CRL/OCSP."
            ]
        },
        {
            "type": "bullet",
            "title": "Public Key Infrastructure (PKI) & X.509 Certificates",
            "sub_title": "The Global Web of Trust Validating Digital Identities",
            "bullets": [
                "• The Impersonation Problem: How does a student know that a public key belonging to `suasms.sua.ac.tz` is authentic and not a hacker's key?",
                "• Certificate Authority (CA): Trusted third-party entity (e.g., DigiCert, Let's Encrypt) that cryptographically binds an organization's public key to their verified identity.",
                "• X.509 Digital Certificate Structure:",
                "    - Subject Name (Domain/Entity) & Issuer (CA Name).",
                "    - Subject's Public Key.",
                "    - Validity Period (Not Before / Not After).",
                "    - Digital Signature of the issuing CA.",
                "• Revocation Mechanisms:",
                "    - Certificate Revocation List (CRL): CA publishes signed list of revoked certificate serial numbers.",
                "    - Online Certificate Status Protocol (OCSP): Real-time query protocol allowing browsers to check revocation status instantly."
            ]
        },
        {
            "type": "bullet",
            "title": "Social Engineering: The Human Vulnerability Vector",
            "sub_title": "Exploiting Psychology Rather Than Software Bugs",
            "bullets": [
                "• Definition: Manipulating people into performing actions or divulging confidential credentials (passwords, banking tokens).",
                "• Attack Taxonomy:",
                "    - Phishing: Mass deceptive emails simulating trusted institutions (banks, university portals) directing victims to credential-harvesting web forms.",
                "    - Spear-Phishing: Highly targeted, customized attacks directed at specific individuals (e.g., emailing the SUA Bursar regarding a specific supplier invoice).",
                "    - Whaling: Spear-phishing targeted directly at high-profile executives (Vice Chancellors, CEOs).",
                "    - Vishing (Voice Phishing) & Smishing (SMS Phishing): Phone calls or mobile texts pretending to be telecom providers.",
                "    - Watering Hole Attack: Compromising legitimate websites frequently visited by the target group.",
                "    - Baiting: Leaving infected USB flash drives in university parking lots or cafeterias labeled 'Exams 2026'."
            ]
        },
        {
            "type": "bullet",
            "title": "Living-off-the-Land (LotL) Attacks & Fileless Malware",
            "sub_title": "Subverting Legitimate Operating System Administration Binaries",
            "bullets": [
                "• Paradigm Shift: Modern sophisticated attackers rarely compile and execute custom `.exe` malware that triggers anti-virus alerts.",
                "• Living-off-the-Land Binaries (LOLBins): Utilizing signed, legitimate administrative OS tools already present on the victim's microcomputer:",
                "    - PowerShell & WMI (Windows Management Instrumentation): Executing in-memory encoded scripts.",
                "    - `certutil.exe`: Native Windows utility abused to download remote malicious payloads over HTTP.",
                "    - `mshta.exe` & `rundll32.exe`: Abused to execute arbitrary malicious DLLs.",
                "• Fileless Malware: Malware residing strictly in volatile system RAM or registry hives; leaves no binary footprint on disk, bypassing traditional file-based signature scanners.",
                "• Defense: Script block logging (PowerShell Event 4104), Constrained Language Mode, and behavioral EDR detection."
            ]
        },
        {
            "type": "bullet",
            "title": "Endpoint Detection & Response (EDR) Architecture",
            "sub_title": "Continuous Telemetry, Threat Hunting, and Automated Isolation",
            "bullets": [
                "• Traditional Anti-Virus vs EDR:",
                "    - Legacy AV: Static gatekeeper; acts only when a file is written to disk matching a known signature.",
                "    - EDR Agent: Flight data recorder continuously streaming low-level operating system events to a central security cloud engine.",
                "• Monitored Telemetry Streams:",
                "    - Process creations and child process spawning trees (e.g., `word.exe` spawning `powershell.exe`).",
                "    - Memory injections and cross-process API hooks (e.g., calls to `VirtualAllocEx` / `WriteProcessMemory`).",
                "    - Network socket connections and domain lookups.",
                "• Automated Containment Capabilities: EDR agent can instantly quarantine a compromised workstation from the university LAN while maintaining an encrypted tunnel for the security team to remediate."
            ]
        },
        {
            "type": "bullet",
            "title": "Sandboxing & Dynamic Malware Detonation",
            "sub_title": "Automated Behavioral Analysis in Isolated Micro-Environments",
            "bullets": [
                "• Sandbox Principle: An isolated, instrumented virtual execution environment where suspicious files are detonated and observed safely.",
                "• Instrumentation Engines: Hooks Windows NT kernel API calls, monitoring:",
                "    - Registry key creations (inspecting persistence mechanisms).",
                "    - File dropped/encrypted across storage volumes.",
                "    - DNS requests and C2 beaconing attempts.",
                "• Malware Sandbox Evasion Tactics & Counter-Measures:",
                "    - Sleep Acceleration / Delayed Execution: Malware sleeps for 20 minutes before executing payload; modern sandboxes fast-forward system timers.",
                "    - Mouse Movement Checking: Malware waits for user mouse movement; sandboxes simulate realistic human pointer movement.",
                "    - Detecting Virtualization Artifacts: Malware inspects MAC addresses and registry for 'VMware' or 'VirtualBox' strings."
            ]
        },
        {
            "type": "bullet",
            "title": "Security Information & Event Management (SIEM)",
            "sub_title": "Centralized Log Ingestion, Correlation, and Alert Triaging",
            "bullets": [
                "• The Log Problem: A university campus generates billions of event logs weekly across firewalls, switches, Linux servers, Windows DCs, and client laptops.",
                "• SIEM Architecture:",
                "    1. Log Ingestion: Ingests Syslog, Windows Event Forwarding (WEF), NetFlow, and cloud telemetry.",
                "    2. Normalization: Parses disparate log formats into standardized schemas (e.g., Elastic Common Schema).",
                "    3. Correlation Engine: Applies threat detection rules across multiple events (e.g., Alert triggers if: 10 failed logins on Windows DC within 60s FOLLOWED BY successful login AND anomalous outbound SSH traffic to unapproved IP).",
                "• Security Orchestration, Automation, and Response (SOAR): Automated playbooks (e.g., automatically blocking malicious IP at the core firewall in milliseconds)."
            ]
        },
        {
            "type": "bullet",
            "title": "Zero-Trust Architecture (ZTA) in Modern Enterprises",
            "sub_title": "NIST SP 800-207: Never Trust, Always Verify",
            "bullets": [
                "• Traditional Perimeter Model ('Castle-and-Moat'): Once inside the corporate intranet, everything is trusted; fundamentally flawed because a single compromised laptop allows lateral movement across the entire network.",
                "• Zero-Trust Core Tenets:",
                "    1. Assume Breach: Operate as though adversaries already possess an active foothold within the internal network.",
                "    2. Never Trust, Always Verify: Every single access request (whether from a dorm room or the Vice Chancellor's desk) must be authenticated, authorized, and encrypted.",
                "    3. Least Privilege Access: Grant access strictly on a per-session, just-in-time, just-enough-access basis.",
                "    4. Continuous Microsegmentation: Isolate university financial subnets, examination databases, and student Wi-Fi into strictly firewalled micro-segments."
            ]
        },
        {
            "type": "bullet",
            "title": "Topic 6: Key Takeaways & Synthesis Matrix",
            "sub_title": "Summary of Data Security & Defense for Course Mastery",
            "bullets": [
                "• CIA Triad: Confidentiality (Encryption/Access), Integrity (Hashing/Signatures), Availability (UPS/RAID/Backups).",
                "• Environmental Controls: Online Double-Conversion UPS provides zero transfer time; 3-2-1 backup rule guarantees disaster survivability.",
                "• Cryptography: Symmetric (AES) excels at high-throughput bulk data; Asymmetric (RSA/ECC) solves key exchange and digital non-repudiation.",
                "• Malware Taxonomy: Viruses require human file execution; Worms replicate autonomously across networks; Trojans deceive users; Ransomware extorts via hybrid encryption.",
                "• Modern Defenses: Signature scanning must be augmented with behavioral analysis, sandboxing, and EDR agents.",
                "• Incident Response: Follow NIST SP 800-61: Prepare → Detect & Analyze → Contain & Eradicate → Recover → Lessons Learned."
            ]
        },
        {
            "type": "bullet",
            "title": "Review Quiz & Knowledge Check",
            "sub_title": "Self-Testing Key Security & Malware Principles",
            "bullets": [
                "1. What is the fundamental operational difference between a Line-Interactive UPS and an Online Double-Conversion UPS?",
                "2. In the 3-2-1 backup strategy, why is at least one copy required to be stored in an offsite or air-gapped location?",
                "3. Explain why the Electronic Codebook (ECB) mode of AES is considered critically insecure for encrypting structured data.",
                "4. Differentiate between a Computer Virus and a Computer Worm regarding human interaction.",
                "5. What mathematical component allows a digital signature to guarantee Non-Repudiation?"
            ]
        },
        {
            "type": "bullet",
            "title": "Course Synthesis & Final Assessment Overview",
            "sub_title": "BIT 111 Course Conclusion & Examination Guidelines",
            "bullets": [
                "• Continuous Assessment Summary:",
                "    - Two Assignments (5%) — Completed via 6 Homework assignments.",
                "    - Two Theory Tests (15%) — Mid-semester and end-of-semester written theory tests.",
                "    - Practical Report (10%) — Laboratory portfolio of terminal, spreadsheet, and security exercises.",
                "    - Practical Test (30%) — Timed laboratory hands-on assessment in SMC computer labs.",
                "    - University Examination (UE) (40%) — Comprehensive 3-hour theoretical examination covering all 6 topics.",
                "    - *Note: Official assessment weights subject to adjustment by Madam Bertha Msuliche Lebalwa (MSc).",
                "• Examination Advice: Focus on mathematical derivations, architectural diagrams, command line syntax, and enterprise agricultural case studies.",
                "• Best wishes to all undergraduate students at Sokoine University of Agriculture!"
            ]
        }
    ]
