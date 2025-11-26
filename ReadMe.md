
# 📘 EOS-φ: Continuous Emotion State Architecture

*A minimal, interpretable demo of smooth emotional state evolution for conversational AI systems.*

This repository accompanies a short research note introducing **EOS-φ**, a lightweight mechanism for modeling **continuous emotional state** in language model systems. The goal is simple:

> Demonstrate how a persistent emotional vector can evolve gradually—rather than snapping between styles or tones—using a transparent, reproducible update rule.

EOS-φ does **not** modify model weights and does **not** rely on hidden heuristics.
It shows how smooth emotional continuity can emerge from a simple, mathematically grounded process.

---

# 🧠 Core Idea

Human emotional expression is **continuous**, not binary or switch-like.
This project implements a minimal model that captures that continuity:

[
E_{t+1} = \alpha E_t + (1 - \alpha) S_i
]

Where:

* (E_t) — the current emotional state vector
* (S_i) — the freshly observed emotional “slice” (e.g., playful, warm, rude)
* (\alpha) — emotional inertia (closer to 1 = slower change)

This update rule ensures:

* **smooth transitions** between tones
* **persistence** of previous state
* **no abrupt personality flips**
* **interpretability** (all vectors are small, observable, editable)

The demo uses **3 dimensions** (warmth, playfulness, politeness) purely for visualization.
The full concept scales to higher-dimensional embeddings.

---

# 📂 Repository Structure

```
eos-phi/
│
├── eos_phi/
│   ├── state.py        # EOS-φ update rule + EmotionState class
│   └── scenarios.py    # predefined tone slices + example sequences
│
├── notebooks/
│   └── 01_eos_phi_demo.ipynb   # runnable visual demo
│
├── requirements.txt      # minimal dependencies
└── paper/                # (optional) accompanying PDF / draft
```

---

# ▶️ Running the Demo

### 1. Create the virtual environment (optional but recommended)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the notebook

```bash
jupyter notebook notebooks/01_eos_phi_demo.ipynb
```

This shows plots of how (E_t) evolves as different tonal slices are applied.

---

# 📊 What the Demo Shows

The notebook gives a simple visualization of:

* Emotional state evolution over time
* How each slice affects the trajectory
* How (\alpha) controls emotional inertia
* Human-readable interpretations of state changes

The result:
A clean, reproducible demonstration of emotional continuity in conversational agents.

---

# 🎯 Purpose of This Repository

This repo is intentionally **minimal**:

* It demonstrates the mechanism clearly
* It avoids weight modification or heavy systems
* It exposes state vectors transparently
* It can be extended to higher-dimensional embeddings
* It provides a conceptual “bridge” between affective computing and LLM behavior research

The goal is for researchers and faculty to understand the intuition quickly:

> *How can we maintain a smooth, persistent emotional state inside a dialogue system using a simple, interpretable update rule?*

---

# 📧 Contact

If you’d like to discuss extensions, embeddings-based versions, or integration into larger adaptive systems, feel free to reach out.

personal email: kabeer.latane18@gmail.com
academic email: kabeerlatane@ufl.edu

---

