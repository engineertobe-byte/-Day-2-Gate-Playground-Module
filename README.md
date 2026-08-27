# ⚛️ Week 1, Day 2: Gate Playground Module

**QAI Labs Quantum Computing & AI/ML Internship**  
*The Quantum Portfolio Project — Module 2 of 7 (29% Complete)*

This module builds a small library of reusable gate functions (X, Z, H, CNOT, Toffoli) with a visual state-vector printout after each. It is designed to prove **fluency with unitary gates** — the #1 skill interviewers sanity-check first.

> **Reference:** `Week1_Quantum_Portfolio_Project.pdf`, Day 2 Core Task


---

## 🔢 Gate Reference & Mathematical Definitions

The following unitary gates are implemented in `module_gates.py` using the modern Qiskit 2.3.0 `Statevector` API.

### 1. Pauli-X (NOT Gate)

$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

| Initial State | Resulting State |
|:---:|:---:|
| $\vert 0 \rangle$ | $\vert 1 \rangle$ |
| $\vert 1 \rangle$ | $\vert 0 \rangle$ |

<br>

### 2. Pauli-Z (Phase Flip)

$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

| Initial State | Resulting State |
|:---:|:---:|
| $\vert 0 \rangle$ | $\vert 0 \rangle$ |
| $\vert 1 \rangle$ | $-\vert 1 \rangle$ |

<br>

### 3. Hadamard (Superposition)

$$
H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

| Initial State | Resulting State |
|:---:|:---:|
| $\vert 0 \rangle$ | $\frac{\vert 0 \rangle + \vert 1 \rangle}{\sqrt{2}}$ |
| $\vert 1 \rangle$ | $\frac{\vert 0 \rangle - \vert 1 \rangle}{\sqrt{2}}$ |

<br>

### 4. CNOT (Entangling Gate)

| Control ($\vert q_0 \rangle$) | Target ($\vert q_1 \rangle$) | Output State |
|:---:|:---:|:---:|
| $\vert 0 \rangle$ | $\vert 0 \rangle$ | $\vert 00 \rangle$ |
| $\vert 0 \rangle$ | $\vert 1 \rangle$ | $\vert 01 \rangle$ |
| $\vert 1 \rangle$ | $\vert 0 \rangle$ | $\vert 11 \rangle$ |
| $\vert 1 \rangle$ | $\vert 1 \rangle$ | $\vert 10 \rangle$ |

<br>

### 5. Toffoli (CCX - Universal Classical)

| Control 0 | Control 1 | Target In | Target Out |
|:---:|:---:|:---:|:---:|
| $\vert 0 \rangle$ | $\vert 0 \rangle$ | $\vert 0 \rangle$ | $\vert 0 \rangle$ |
| $\vert 1 \rangle$ | $\vert 1 \rangle$ | $\vert 0 \rangle$ | $\vert 1 \rangle$ |
| *(other combos)* | | | *Target unchanged* |

---

## 🛠️ Usage

The core deliverable is `module_gates.py`, a clean Python library containing a reusable `apply_gate()` function.

### How to run:
```bash
pip install -r requirements.txt
python module_gates.py
```

### Expected Terminal Output (Excerpt)
```text
==================================================
Gate Applied : H
Initial State: |0⟩
Statevector  : [0.7071+0.j 0.7071+0.j]
Probabilities: [0.5 0.5]
==================================================

==================================================
Gate Applied : X
Initial State: |1⟩
Statevector  : [1.+0.j 0.+0.j]
Probabilities: [1. 0.]
==================================================
```

---


---

## ✅ Daily Checklist

- [x] `module_gates.py` runs top-to-bottom with no errors
- [x] All 5 gates (X, Z, H, CNOT, Toffoli) demonstrated on both $\vert 0 \rangle$ and $\vert 1 \rangle$
- [x] Statevector output matches theoretical matrices
- [x] Committed and pushed before closing laptop
- [ ] **Tomorrow:** Day 3 — Deutsch-Jozsa From Scratch (Custom Oracles)

---

*Part of the 7-day Quantum Portfolio Project. Built incrementally, one module a day.*
