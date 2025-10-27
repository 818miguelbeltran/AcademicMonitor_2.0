# 📚 Academic Monitoring System (Academic Monitor 2.0)

This project models the **evolutionary design process** of a personal productivity tool using iterative development, feature expansion, and user-centric refinement to achieve specific academic goals.

---

## 📈 Project Evolution & Design Iteration
![Project Evolution Overview](evolutionary-design-overview.png)
*Visual summary of the Academic Monitor 2.0's journey from a simple tracker to a smart planning and analysis tool.*

---

## 🔹 Evolution Stages
- **1\_The\_Start\_W2D2.png:** Began as a **basic tracker** with static numbers and limited input.
- **2\_The\_Upgrade\_W3D4.png:** Upgraded to **accept new scores**, introduced goal-checking logic, and identified the weakest subject area.
- **3\_The\_Help\_Guide\_W3D5.png:** Integrated an **instant help menu** (triggered by typing ‘help’) for user onboarding and program instruction.
- **4\_The\_Data\_Collection\_Start\_W3D5.png:** Implemented a **smart planner setup** with organized, sectioned data collection and safety checks (Course Name, GPA, Weights).

---

## 🔁 Iterative Refinement Flow
Information flows through three phases — **Basic Tracking → Goal Analysis → Smart Planning.**
This structured loop transformed a static utility into an adaptive academic planning system, reinforcing accountability and proactive subject management.

---

## 🧩 Stage Analysis
![Part 1 – Initial Design and Goal Setting](academic-monitor-stage1.png)
*Shows the initial basic tracker design and the transition to accepting new user input for score and goal analysis.*

**Core Features Added**
- **Goal Checking:** Compares current performance against set academic objectives.
- **Weakest Subject Area Identification:** Calculates and flags the course most likely to pull down the overall GPA.
- **User Input Validation:** Added safety checks to ensure correct data types (e.g., numbers for scores/weights) were entered during setup.

Each stage built upon the last, directly addressing the limitations and user pain points of the previous iteration (e.g., moving from static numbers to dynamic input).

---

## 🧱 Key System Upgrades
![Part 2 – Help Menu and Data Collection Logic](academic-monitor-stage2.png)
*Focuses on the integration of the built-in help guide and the structured, safety-checked data collection process.*

**1. Onboarding Pattern – Instant Help Guide**
- The built-in help menu provides immediate, context-sensitive instructions when the user types 'help'.
- Reduces the friction of new user adoption and ensures consistent program usage.
- Models an essential **user-centric design** component for complex tools.

**2. Data Safety Pattern – Organized Input**
- Uses distinct, organized sections and input safety checks to collect core planning data (Course Name, GPA, Weights).
- Prevents system errors from bad data and ensures the planning algorithm runs on reliable inputs.

---

## 🔁 Before & After Comparison
![Part 3 – Basic Tracker vs. Smart Planner](academic-monitor-stage3.png)
*Visual comparison showing how dynamic data input and smart analysis improve the user’s ability to monitor and achieve academic goals.*

### Before
The system provided static feedback ("Keep it up!") without accepting new data or performing goal analysis.

### After
The redesigned system integrates dynamic score updates, weak-subject identification, and a structured planning setup — maintaining continuous analysis toward the user's defined academic goal.

---

## 💻 Purpose
This project demonstrates how **iterative design and feature expansion** can be applied to a personal tool to enhance its utility, moving it from a passive tracker to an **active, goal-oriented monitoring system**.

---

## 🧠 About This Project
This system was developed as the "Academic Monitor 2.0" to directly support a personal academic goal.
It integrates **data analysis with a user-friendly interface** to show how custom Python scripts can be designed to self-regulate performance, identify areas for improvement, and automate critical monitoring tasks.

---

Compares GPA to target and generates advice:
- **On Track:** Meeting or exceeding goal
- **Warning:** Near the threshold
- **Review Needed:** Below goal, with weakest area highlighted

---
### 🎨 Sample Output
```
Current GPA: 3.8 Required GPA: 4.0...
STATUS: REVIEW NEEDED ADVICE: You are currently 0.20 points below your target...
```
---
## 🔄 Future Directions
- Add **data storage** (CSV or JSON) to track progress over time
- Visualize results through **matplotlib or Plotly graphs**
- Integrate with **AI-driven predictive modeling** for GPA forecasting
- Explore **ethical frameworks** for algorithmic evaluation and fairness

---
## 🔎 Research Context

This project aligns with my ongoing research on **surveillance, algorithmic systems, and social control**.
By translating self-monitoring into code, *Academic Monitor 2.0* illustrates how **digital systems quantify performance, identify “weakness,” and shape user behavior** through structured feedback loops.

It bridges **technical learning (Python logic)** and **sociological inquiry (algorithmic governance)** — showing how metrics, automation, and design can both **empower and discipline** individuals in pursuit of improvement.
---
## ▶️ Run Instructions
To run the program locally:
```bash
python main.py
