# ============================================================
# Gear Train Performance Analyzer
# Developed By : Aneesh Gopal (RA2311072010013)
# Language     : Python 3
# Libraries    : pandas, numpy, matplotlib
# ============================================================

# ------------------------------------------------------------
# Import Libraries
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ------------------------------------------------------------
# Program Title
# ------------------------------------------------------------

print("=" * 70)
print("        GEAR TRAIN PERFORMANCE ANALYZER")
print("=" * 70)

# ------------------------------------------------------------
# Check CSV File
# ------------------------------------------------------------

INPUT_FILE = "gear_input.csv"
OUTPUT_FILE = "gear_results.csv"

if not os.path.exists(INPUT_FILE):

    print("\nERROR : gear_input.csv not found.")
    print("Please keep the CSV file in the same folder.")
    exit()

# ------------------------------------------------------------
# Read CSV
# ------------------------------------------------------------

try:

    data = pd.read_csv(INPUT_FILE)

except Exception as e:

    print("Unable to read CSV File")
    print(e)
    exit()

# ------------------------------------------------------------
# Display Data
# ------------------------------------------------------------

print("\nINPUT DATA\n")

print(data)

print("\nNumber of Gear Sets :", len(data))

# ------------------------------------------------------------
# Required Columns
# ------------------------------------------------------------

required_columns = [

    "DriverTeeth",
    "DrivenTeeth",
    "InputRPM",
    "InputTorque",
    "Efficiency"

]

for column in required_columns:

    if column not in data.columns:

        print("\nMissing Column :", column)
        exit()

# ------------------------------------------------------------
# Empty Lists
# ------------------------------------------------------------

gear_ratio = []

output_speed = []

output_torque = []

power_input = []

power_output = []

status = []

print("\nStarting Calculations...\n")
# ============================================================
# Gear Calculations
# ============================================================

for index, row in data.iterrows():

    # Read Input Values

    driver_teeth = row["DriverTeeth"]
    driven_teeth = row["DrivenTeeth"]
    input_rpm = row["InputRPM"]
    input_torque = row["InputTorque"]
    efficiency = row["Efficiency"]

    # --------------------------------------------------------
    # Validate Data
    # --------------------------------------------------------

    if driver_teeth <= 0 or driven_teeth <= 0:

        print("Invalid Gear Teeth at Row", index + 1)

        continue

    if efficiency <= 0 or efficiency > 100:

        print("Invalid Efficiency at Row", index + 1)

        continue

    # --------------------------------------------------------
    # Gear Ratio
    # --------------------------------------------------------

    ratio = driven_teeth / driver_teeth

    gear_ratio.append(ratio)

    # --------------------------------------------------------
    # Output Speed
    # --------------------------------------------------------

    rpm = input_rpm / ratio

    output_speed.append(rpm)

    # --------------------------------------------------------
    # Output Torque
    # --------------------------------------------------------

    torque = input_torque * ratio * (efficiency / 100)

    output_torque.append(torque)

    # --------------------------------------------------------
    # Input Power
    #
    # P = (2πNT)/60
    # --------------------------------------------------------

    pin = (2 * np.pi * input_rpm * input_torque) / 60

    power_input.append(pin)

    # --------------------------------------------------------
    # Output Power
    # --------------------------------------------------------

    pout = pin * (efficiency / 100)

    power_output.append(pout)

    # --------------------------------------------------------
    # Performance Status
    # --------------------------------------------------------

    if efficiency >= 95:

        status.append("Excellent")

    elif efficiency >= 90:

        status.append("Good")

    elif efficiency >= 80:

        status.append("Average")

    else:

        status.append("Poor")

# ============================================================
# Add Results into DataFrame
# ============================================================

data["GearRatio"] = np.round(gear_ratio, 3)

data["OutputRPM"] = np.round(output_speed, 2)

data["OutputTorque"] = np.round(output_torque, 2)

data["InputPower(W)"] = np.round(power_input, 2)

data["OutputPower(W)"] = np.round(power_output, 2)

data["Performance"] = status

# ============================================================
# Display Results
# ============================================================

print("=" * 80)

print("FINAL RESULTS")

print("=" * 80)

print(data)

# ============================================================
# Save Results
# ============================================================

data.to_csv(OUTPUT_FILE, index=False)

print("\nResults saved successfully as:", OUTPUT_FILE)

# ============================================================
# Project Statistics
# ============================================================

print("\nPROJECT SUMMARY")

print("-" * 50)

print("Average Gear Ratio      :", round(data["GearRatio"].mean(), 2))

print("Maximum Output RPM      :", round(data["OutputRPM"].max(), 2))

print("Minimum Output RPM      :", round(data["OutputRPM"].min(), 2))

print("Average Output Torque   :", round(data["OutputTorque"].mean(), 2))

print("Maximum Output Torque   :", round(data["OutputTorque"].max(), 2))

print("Average Efficiency      :", round(data["Efficiency"].mean(), 2), "%")

print("-" * 50)
# ============================================================
# GRAPH GENERATION
# ============================================================

# Create folder for graphs if it does not exist
if not os.path.exists("graphs"):
    os.makedirs("graphs")

# ------------------------------------------------------------
# Graph 1 : Gear Ratio vs Output Speed
# ------------------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    data["GearRatio"],
    data["OutputRPM"],
    marker="o",
    linewidth=2,
    color="blue"
)

plt.title("Gear Ratio vs Output Speed")
plt.xlabel("Gear Ratio")
plt.ylabel("Output Speed (RPM)")
plt.grid(True)

plt.savefig("graphs/speed_vs_ratio.png")

# ------------------------------------------------------------
# Graph 2 : Gear Ratio vs Output Torque
# ------------------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    data["GearRatio"],
    data["OutputTorque"],
    marker="s",
    linewidth=2,
    color="green"
)

plt.title("Gear Ratio vs Output Torque")
plt.xlabel("Gear Ratio")
plt.ylabel("Output Torque (Nm)")
plt.grid(True)

plt.savefig("graphs/torque_vs_ratio.png")

# ------------------------------------------------------------
# Graph 3 : Efficiency Comparison
# ------------------------------------------------------------

plt.figure(figsize=(10,5))

plt.bar(
    range(len(data)),
    data["Efficiency"]
)

plt.title("Efficiency of Each Gear Set")
plt.xlabel("Gear Set Number")
plt.ylabel("Efficiency (%)")
plt.grid(axis="y")

plt.savefig("graphs/efficiency.png")

# ------------------------------------------------------------
# Graph 4 : Input Power vs Output Power
# ------------------------------------------------------------

plt.figure(figsize=(8,5))

plt.plot(
    data["InputPower(W)"],
    marker="o",
    label="Input Power"
)

plt.plot(
    data["OutputPower(W)"],
    marker="^",
    label="Output Power"
)

plt.title("Input Power vs Output Power")
plt.xlabel("Gear Set")
plt.ylabel("Power (W)")
plt.legend()
plt.grid(True)

plt.savefig("graphs/power_comparison.png")

# ------------------------------------------------------------
# Graph 5 : Output Speed Distribution
# ------------------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    data["OutputRPM"],
    bins=5
)

plt.title("Distribution of Output RPM")
plt.xlabel("Output RPM")
plt.ylabel("Frequency")

plt.savefig("graphs/output_speed_histogram.png")

# ------------------------------------------------------------
# Display all graphs
# ------------------------------------------------------------

plt.show()

# ============================================================
# FINAL ANALYSIS
# ============================================================

print("\n" + "="*60)
print("FINAL ANALYSIS")
print("="*60)

highest_speed = data.loc[data["OutputRPM"].idxmax()]
highest_torque = data.loc[data["OutputTorque"].idxmax()]
best_efficiency = data.loc[data["Efficiency"].idxmax()]

print("\nHighest Output Speed")
print("--------------------")
print(highest_speed)

print("\nHighest Output Torque")
print("---------------------")
print(highest_torque)

print("\nBest Efficiency")
print("----------------")
print(best_efficiency)

print("\nGraphs saved successfully inside the 'graphs' folder.")
print("Analysis completed successfully.")
