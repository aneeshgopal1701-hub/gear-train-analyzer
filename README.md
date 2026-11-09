<h1 align="center">⚙️ Gear Train Performance Analyzer</h1>

<p align="center">
  <i>A Python tool that turns raw gear data into speed, torque and power insights — with graphs.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pandas-data%20analysis-150458?logo=pandas&logoColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/NumPy-maths-013243?logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-plots-11557c" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Project-Individual-success" alt="Individual project">
</p>

| | |
|---|---|
| **Author** | Aneesh Gopal |
| **Registration No.** | RA2311072010013 |
| **Department** | Mechanical Engineering (Automation and Robotics) |
| **Course** | Python Programming – Individual Project |

---

## 📌 Table of Contents
1. [About the Project](#-about-the-project)
2. [Objectives](#-objectives)
3. [How It Works](#-how-it-works)
4. [Formulas](#-formulas)
5. [Project Structure](#-project-structure)
6. [Getting Started](#-getting-started)
7. [Input Format](#-input-format)
8. [Results](#-results)
9. [Graphs](#-graphs)
10. [Concepts Used](#-python-concepts-used)
11. [Limitations & Future Scope](#-limitations--future-scope)
12. [Report](#-report)

---

## 📖 About the Project
Gears change speed and torque in almost every machine, from robots to car gearboxes. Comparing many gear sets by hand is slow and error-prone.

The **Gear Train Performance Analyzer** reads gear specifications from a CSV file, validates them, calculates the main performance values, rates each gear set, saves the results and plots five graphs — all with a single command.

## 🎯 Objectives
- Read gear data (teeth, input RPM, input torque, efficiency) from a CSV file
- Validate the data before calculating
- Compute gear ratio, output speed, output torque, input power and output power
- Rate every gear set as **Excellent / Good / Average / Poor**
- Save results to `gear_results.csv` and generate graphs for comparison

## 🔄 How It Works
```
gear_input.csv ──► check file & columns ──► validate each row ──► calculate
                                                                     │
        graphs/*.png ◄── plots ◄── summary & analysis ◄── gear_results.csv
```

## 📐 Formulas
| Quantity | Formula |
|---|---|
| Gear ratio | `driven_teeth / driver_teeth` |
| Output speed (RPM) | `input_rpm / gear_ratio` |
| Output torque (Nm) | `input_torque × gear_ratio × efficiency/100` |
| Input power (W) | `2π × input_rpm × input_torque / 60` |
| Output power (W) | `input_power × efficiency/100` |

**Rating:** efficiency ≥ 95 → Excellent · ≥ 90 → Good · ≥ 80 → Average · otherwise Poor

## 🗂 Project Structure
```
gear-train-analyzer/
├── main.py                  # main program
├── gear_input.csv           # input dataset
├── gear_results.csv         # generated results
├── program_output.txt       # console output of a sample run
├── requirements.txt         # dependencies
├── graphs/                  # generated plots (5 PNG files)
├── Report/                  # final project report (PDF)
└── README.md
```

## 🚀 Getting Started

**Prerequisites:** Python 3.8 or newer.

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/gear-train-analyzer.git
cd gear-train-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python main.py
```

The program prints the results in the terminal, writes `gear_results.csv`, saves five graphs in `graphs/`, and finally opens the plot windows (close them to end the program).

> **Tip:** keep `gear_input.csv` in the same folder as `main.py`.

## 📥 Input Format
| Column | Meaning | Unit |
|---|---|---|
| `DriverTeeth` | Teeth on driver gear | – |
| `DrivenTeeth` | Teeth on driven gear | – |
| `InputRPM` | Input shaft speed | RPM |
| `InputTorque` | Input shaft torque | Nm |
| `Efficiency` | Efficiency, 0 < value ≤ 100 | % |

```csv
DriverTeeth,DrivenTeeth,InputRPM,InputTorque,Efficiency
20,40,1200,50,95
25,50,1500,45,94
```
Add your own rows to analyse other gear sets. Rows with invalid teeth counts or efficiency are skipped with a message.

## 📊 Results
| Set | Ratio | Output RPM | Output Torque (Nm) | Input Power (W) | Output Power (W) | Rating |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 2.0 | 600 | 95.0 | 6283.19 | 5969.03 | 🟢 Excellent |
| 1 | 2.0 | 750 | 84.6 | 7068.58 | 6644.47 | 🟡 Good |
| 2 | 3.0 | 600 | 96.6 | 6597.34 | 6069.56 | 🟡 Good |
| 3 | 2.0 | 500 | 115.2 | 6283.19 | 6031.86 | 🟢 Excellent |
| 4 | 2.0 | 700 | 74.4 | 5864.31 | 5453.80 | 🟡 Good |

**Key findings**
- 🏆 **Best efficiency & highest torque:** gear set 3 (96 %, 115.2 Nm)
- ⚡ **Highest output speed:** gear set 1 (750 RPM)
- 📉 **Average:** ratio 2.2 · output torque 93.16 Nm · efficiency 94 %
- Every set is a speed reducer: speed drops, torque rises.

## 📈 Graphs
<table>
  <tr>
    <td><img src="graphs/efficiency.png" alt="Efficiency of each gear set"></td>
    <td><img src="graphs/power_comparison.png" alt="Input vs output power"></td>
  </tr>
  <tr>
    <td><img src="graphs/speed_vs_ratio.png" alt="Gear ratio vs output speed"></td>
    <td><img src="graphs/torque_vs_ratio.png" alt="Gear ratio vs output torque"></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="graphs/output_speed_histogram.png" alt="Distribution of output RPM" width="50%"></td>
  </tr>
</table>

## 🧠 Python Concepts Used
File handling · exception handling · variables & data types · lists · `for` loops · `if/elif/else` · pandas DataFrames · NumPy maths · input validation · Matplotlib plotting

## 🔭 Limitations & Future Scope
- Small sample dataset (5 gear sets); single-stage gear pairs only
- Efficiency is a single given value per set (no friction/lubrication model)
- Ideas: multi-stage trains, helical/bevel/worm gears, scatter plots for ratio graphs, a GUI (Tkinter/Streamlit)

## 📄 Report
The complete project report is in [`Report/`](Report/).

---
<p align="center">Made by <b>Aneesh Gopal</b> · RA2311072010013</p>
