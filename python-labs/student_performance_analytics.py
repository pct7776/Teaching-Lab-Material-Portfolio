"""
=========================================================================
COURSE LAB ACTIVITY: Exploratory Data Analysis & Visual Metrics
Target Student Level: Undergraduate Computer Applications (BCA / B.Sc IT)
Course Framework Alignment: UGC & NSDC Advanced Python Curriculum
Designer: Poornachandra Tejaswi (MBA - Information Systems, BCA)
=========================================================================
"""

import matplotlib.pyplot as plt
import pandas as pd

# 1. CORE LABORATORY EXERCISE: GENERATING DATA MATRICES
# Objective: Simulating an academic department matrix to clean and analyze student performance distributions.
data = {
    "StudentID":,
    "StudentName": ["Amit", "Neha", "Rohan", "Pooja", "Vikram", "Anjali"],
    "Python_Score":,
    "DBMS_Score":,
}

# Transform dictionary data into a structured Data Frame
df = pd.DataFrame(data)


# 2. ALGORITHMIC COMPUTATION SECTION
# Compute individual average benchmarks per row record
df["Final_Average"] = df[["Python_Score", "DBMS_Score"]].mean(axis=1)


# Establish logical categorical outcomes using conditional filters
def evaluate_outcome(score):
    if score >= 75:
        return "Distinction"
    elif score >= 50:
        return "Pass"
    else:
        return "Re-appear"


df["Academic_Standing"] = df["Final_Average"].apply(evaluate_outcome)

print("--- EXECUTED LABORATORY DATA ANALYSIS METRIC ---")
print(df)
print("\n--- AGGREGATE LAB COMPUTATION ---")
print(f"Overall Class Performance Average: {df['Final_Average'].mean():.2f}%")


# 3. ADVANCED VISUALIZATION EXERCISE
# Generate a comparative bar plot charting student execution distributions
plt.figure(figsize=(8, 5))
plt.bar(df["StudentName"], df["Python_Score"], color="skyblue", edgecolor="black")
plt.title("Student Computational Performance: Python Laboratory Assessment", fontsize=12, fontweight="bold")
plt.xlabel("Student Name", fontsize=10)
plt.ylabel("Score Secured (Out of 100)", fontsize=10)
plt.axhline(y=50, color="red", linestyle="--", label="Passing Threshold (50%)")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.legend()

# Save visual execution frame
plt.savefig("python-labs/student_performance_plot.png")
print("\nSuccess: Performance plot compiled and mapped to inventory.")
