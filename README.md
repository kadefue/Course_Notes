# 📚 Course Notes & Academic Knowledge Base

A comprehensive, centralized repository containing notes, formulas, diagrams, lecture summaries, and reference guides across all academic subjects.

---

## 🗺️ Subject Architecture & Knowledge Map

The diagram below maps how the key disciplines connect across foundational theory, core technical domains, and practical applications.

```mermaid
graph TD
    classDef foundation fill:#3b82f6,stroke:#1d4ed8,stroke-width:2px,color:#fff;
    classDef core fill:#8b5cf6,stroke:#6d28d9,stroke-width:2px,color:#fff;
    classDef applied fill:#10b981,stroke:#047857,stroke-width:2px,color:#fff;
    classDef domain fill:#f59e0b,stroke:#b45309,stroke-width:2px,color:#fff;

    subgraph Foundations ["🧠 Foundations"]
        MATH["📐 Mathematics & Calculus"]:::foundation
        STATS["📊 Probability & Statistics"]:::foundation
        LOGIC["⚙️ Discrete Math & Logic"]:::foundation
    end

    subgraph Core ["💻 Core Principles"]
        DSA["🗂️ Data Structures & Algorithms"]:::core
        SYS["🖥️ Computer Systems & Arch"]:::core
        OS["🐧 Operating Systems & Networks"]:::core
    end

    subgraph Applied ["🚀 Applied Systems"]
        ML["🤖 Machine Learning & AI"]:::applied
        DB["💾 Databases & Distributed Systems"]:::applied
        SWE["🛠️ Software Engineering & Design"]:::applied
    end

    subgraph Domains ["🔬 Domain Electives"]
        BIO["🧬 Computational Biology & Bioinformatics"]:::domain
        SEC["🛡️ Cybersecurity & Cryptography"]:::domain
        PHYS["⚛️ Physics & Simulation"]:::domain
    end

    MATH --> DSA
    STATS --> ML
    LOGIC --> DSA
    DSA --> SWE
    SYS --> OS
    OS --> DB
    DSA --> ML
    MATH --> PHYS
    DB --> Applied
    ML --> BIO
```

---

## 📖 Subject Summaries & Visual Overviews

---

### 1. 📐 Mathematics & Linear Algebra
> **Focus**: Vector spaces, matrix transformations, calculus optimization, and eigenvalues.

* **Key Concepts**: Basis & Dimension, Matrix Decompositions (LU, QR, SVD), Multivariable Calculus, Gradient Descent.
* **Core Application**: Foundation for Machine Learning loss functions and graphics pipelines.

```mermaid
flowchart LR
    A["Matrix A"] --> B["Eigenvalues & Eigenvectors\n(A v = λ v)"]
    A --> C["Singular Value Decomposition\n(U Σ Vᵀ)"]
    B --> D["Principal Component Analysis (PCA)"]
    C --> E["Dimensionality Reduction & Latent Embeddings"]
```

---

### 2. 🗂️ Data Structures & Algorithms (DSA)
> **Focus**: Efficiency, asymptotic complexity, foundational memory structures, and algorithmic paradigms.

* **Key Concepts**: Trees, Graphs, Hash Tables, Heaps, Dynamic Programming, Divide-and-Conquer, Greedy Algorithms.

```mermaid
flowchart TD
    ROOT["Algorithmic Strategy"]
    ROOT --> REC["Recursion & Subproblems"]
    ROOT --> ITER["Iterative & State-Based"]

    REC --> DP["Dynamic Programming\n- Memoization (Top-down)\n- Tabulation (Bottom-up)"]
    REC --> DNC["Divide & Conquer\n- Merge Sort\n- Quick Sort"]
    
    ITER --> GREEDY["Greedy Choice\n- Dijkstra\n- Huffman Coding"]
    ITER --> GRAPH["Graph Traversal\n- BFS (Shortest Path)\n- DFS (Topological Sort)"]
```

#### 📊 Complexity Reference Matrix
| Structure / Algorithm | Access | Search | Insertion | Deletion | Space |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Array** | $O(1)$ | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Hash Table** | N/A | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg | $O(n)$ |
| **Binary Search Tree (Balanced)** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Quick / Merge Sort** | — | — | — | — | $O(n \log n)$ |

---

### 3. 🖥️ Computer Systems & Operating Systems
> **Focus**: Memory hierarchies, virtualization, concurrency, kernel primitives, and I/O.

```mermaid
sequenceDiagram
    autonumber
    actor User as User Process
    participant Kernel as OS Kernel
    participant Memory as Virtual Memory / TLB
    participant Hardware as Physical Hardware / Disk

    User->>Kernel: System Call (read/write, fork)
    Kernel->>Memory: Address Translation & Page Table Lookup
    alt Page Hit
        Memory-->>Kernel: Physical Frame Address
    else Page Fault
        Memory-->>Kernel: Page Fault Trap
        Kernel->>Hardware: Fetch Block from Secondary Storage
        Hardware-->>Memory: Swap Frame into RAM
    end
    Kernel-->>User: Return to User Space with Data
```

* **Core Topics**: Processes vs. Threads, Race Conditions & Mutexes, Deadlock Avoidance, Virtual Memory & Paging, File Systems.

---

### 4. 🤖 Machine Learning & Artificial Intelligence
> **Focus**: Predictive modeling, representation learning, loss optimization, and neural architectures.

```mermaid
flowchart LR
    subgraph Input ["1. Data Ingestion"]
        X["Raw Features (X)"]
        Y["Ground Truth (y)"]
    end

    subgraph Forward ["2. Forward Pass"]
        X --> MODEL["Model Weights & Layers\nŷ = f(X; W, b)"]
        MODEL --> LOSS["Loss Computation\nL(ŷ, y)"]
        Y --> LOSS
    end

    subgraph Backward ["3. Optimization"]
        LOSS --> GRAD["Backpropagation\n(∂L/∂W via Chain Rule)"]
        GRAD --> OPT["Optimizer (SGD / Adam)\nW ← W - η ∇W"]
        OPT -. Updates .-> MODEL
    end
```

---

### 5. 💾 Databases & Distributed Systems
> **Focus**: ACID transactions, relational normal forms, distributed consensus, and replication models.

```mermaid
stateDiagram-v2
    [*] --> Active: Begin Transaction
    Active --> PartiallyCommitted: All Operations Succeeded
    Active --> Failed: Operation Exception / Abort
    PartiallyCommitted --> Committed: Flush WAL & Write Commit Log
    PartiallyCommitted --> Failed: Storage Failure
    Failed --> Aborted: Execute Rollback
    Committed --> [*]: End (Durable)
    Aborted --> [*]: State Restored
```

* **Relational vs. Distributed**:
  * **ACID**: Atomicity, Consistency, Isolation, Durability (RDBMS / OLTP).
  * **CAP Theorem**: Consistency, Availability, Partition Tolerance (Distributed systems must choose two under network partition).

---

## 🗂️ Workspace Directory Organization