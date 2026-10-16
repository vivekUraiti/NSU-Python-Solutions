"""
NSU Python — Lab 12
NumPy and Pandas

Tasks 1–14 are core practice. Tasks 15–16 are optional bonus tasks.
Complete at least 10 core tasks, including Tasks 10–14 and at least
five tasks from Tasks 1–9. All 14 core tasks are recommended.
Use only Lecture 12 and earlier concepts. Python 3.10+.
Run from this directory. Preserve the supplied CSV files.
"""

import numpy as np
import pandas as pd


# ========================================================================
# Task 1 — Create and inspect an array
# ========================================================================
# Create np.array([12, 18, 24, 30], dtype=np.int64).
# Print the array, shape, ndim, size, and dtype.
# Expected metadata: (4,), 1, 4, int64.

# Write your code below:


import numpy as np

a = np.array([12, 18, 24, 30], dtype=np.int64)

print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)





# ========================================================================
# Task 2 — Array creation functions
# ========================================================================
# Create a 2-by-3 array of zeros, an integer array of four ones,
# and an array containing 2, 4, 6, 8 using np.arange().
# Use np.linspace() to create five evenly spaced values from 0 to 1, inclusive.
# Expected final values: [0.0, 0.25, 0.5, 0.75, 1.0].

# Write your code below:


import numpy as np

zeros = np.zeros((2, 3))
ones = np.ones(4, dtype=int)
numbers = np.arange(2, 10, 2)
values = np.linspace(0, 1, 5)

print(zeros)
print(ones)
print(numbers)
print(values)





# ========================================================================
# Task 3 — Indexing and slicing
# ========================================================================
# Given a = np.array([10, 20, 30, 40, 50, 60]),
# print the first element, last element, elements at positions 1 through 3,
# every second element starting at position 0, and the reversed array.
# Expected: 10; 60; [20, 30, 40]; [10, 30, 50]; [60, 50, 40, 30, 20, 10].

# Write your code below:

import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])

print(a[0])
print(a[-1])
print(a[1:4])
print(a[::2])
print(a[::-1])




# ========================================================================
# Task 4 — Reshape and select from a table
# ========================================================================
# Create np.arange(1, 13).reshape(3, 4).
# Print its shape, second row, third column, and element at row 2, column 3.
# Then print its transpose and the shape of the transpose.
# Indices are zero-based. Expected element: 12. Transposed shape: (4, 3).

# Write your code below:


import numpy as np

a = np.arange(1, 13).reshape(3, 4)

print(a.shape)
print(a[1])
print(a[:, 2])
print(a[2, 3])
print(a.T)
print(a.T.shape)





# ========================================================================
# Task 5 — Views and independent copies
# ========================================================================
# Create a = np.array([10, 20, 30, 40]).
# Create view = a[1:3] and assign view[0] = 99. Print a.
# Then create independent = a[1:3].copy(), assign independent[0] = -1,
# and print a again. Both outputs must be [10, 99, 30, 40].
# Explain the difference in a comment.

# Write your code below:

import numpy as np

a = np.array([10, 20, 30, 40])

view = a[1:3]
view[0] = 99

print(a)

independent = a[1:3].copy()
independent[0] = -1

print(a)






# ========================================================================
# Task 6 — Vectorized calculations and broadcasting
# ========================================================================
# Given a = np.array([2, 4, 6]), calculate a + 10, a * 3, and a ** 2
# without Python loops.
# Given m = np.array([[1, 2, 3], [4, 5, 6]]),
# add np.array([10, 20, 30]) to every row using broadcasting.
# Expected table: [[11, 22, 33], [14, 25, 36]].

# Write your code below:

import numpy as np

a = np.array([2, 4, 6])

print(a + 10)
print(a * 3)
print(a ** 2)

m = np.array([[1, 2, 3], [4, 5, 6]])
result = m + np.array([10, 20, 30])

print(result)





# ========================================================================
# Task 7 — Boolean filtering
# ========================================================================
# Given scores = np.array([35, 60, 75, 90, 100]),
# select scores >= 60, then scores >= 60 and < 90.
# Use Boolean masks, &, and parentheses. Do not use a Python loop.
# Expected results: [60, 75, 90, 100] and [60, 75].

# Write your code below:


import numpy as np

scores = np.array([35, 60, 75, 90, 100])

passing = scores[scores >= 60]
selected = scores[(scores >= 60) & (scores < 90)]

print(passing)
print(selected)





# ========================================================================
# Task 8 — Aggregations by axis
# ========================================================================
# Given scores = np.array([[70, 80], [90, 85], [50, 60]]),
# calculate the mean per student, mean per assignment, overall mean,
# and global minimum and maximum. Rows represent students.
# Expected student means: [75.0, 87.5, 55.0].
# Expected assignment means: [70.0, 75.0]. Overall mean: 72.5.
# Minimum: 50. Maximum: 90.

# Write your code below:


import numpy as np

scores = np.array([
    [70, 80],
    [90, 85],
    [50, 60]
])

print(np.mean(scores, axis=1))
print(np.mean(scores, axis=0))
print(np.mean(scores))
print(np.min(scores))
print(np.max(scores))





# ========================================================================
# Task 9 — Elementwise and matrix multiplication
# ========================================================================
# Given A = np.array([[1, 2], [3, 4]]) and
# B = np.array([[5, 6], [7, 8]]), calculate A * B and A @ B.
# Expected elementwise result: [[5, 12], [21, 32]].
# Expected matrix result: [[19, 22], [43, 50]].
# Explain in a comment why these results differ.

# Write your code below:

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A * B)
print(A @ B)






# ========================================================================
# Task 10 — Load and inspect a CSV
# ========================================================================
# Load students.csv with pd.read_csv() into df.
# Print head(), shape, column names, dtypes, info(), and describe().
# Expected shape: (8, 4). Expected columns: student_id, name, group, score.
# Call info() directly rather than print(df.info()).
# Do not modify the CSV file.

# Write your code below:


import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())





# ========================================================================
# Task 11 — Select and filter labelled data
# ========================================================================
# Reload students.csv so this task starts with the original data.
# Select name and score as a DataFrame.
# Select student_id=103 using a labelled index and loc. Expected name: Lena.
# Use iloc to select the first three rows.
# Convert a separate score Series with pd.to_numeric(errors="coerce")
# for numerical comparisons. The source includes the text "absent".
# Select names with scores >= 80 and <= 100.
# Expected names: Omar, Lena, Sara. Invalid scores must not pass.

# Write your code below:


import pandas as pd

df = pd.read_csv("students.csv")

print(df[["name", "score"]])

indexed = df.set_index("student_id")
print(indexed.loc[103])

print(df.iloc[:3])

numeric_scores = pd.to_numeric(df["score"], errors="coerce")

mask = (numeric_scores >= 80) & (numeric_scores <= 100)
print(df.loc[mask, "name"])





# ========================================================================
# Task 12 — Clean scores and identify invalid rows
# ========================================================================
# Reload students.csv. Convert score using pd.to_numeric(errors="coerce").
# Print the count of missing or non-numeric scores after conversion. Expected: 2.
# Mark any missing score or score outside [0, 100] as invalid.
# Expected invalid student IDs: 104, 106, 108.
# Create clean = df.loc[valid_mask].copy(). Expected number of rows: 5.
# Do not fill missing scores with zero. Explain why in a comment.

# Write your code below:


import pandas as pd

df = pd.read_csv("students.csv")

df["score"] = pd.to_numeric(df["score"], errors="coerce")

print(df["score"].isna().sum())

valid_mask = df["score"].notna() & df["score"].between(0, 100)

print(df.loc[~valid_mask, "student_id"].tolist())

clean = df.loc[valid_mask].copy()

print(len(clean))






# ========================================================================
# Task 13 — Create columns and summarize groups
# ========================================================================
# Reuse clean from Task 12. Add passed = score >= 60
# and score_fraction = score / 100. Sort by score descending.
# Print the overall mean, pass percentage, and group means.
# Expected overall mean: 76.0. Pass percentage: 80.0.
# Expected group means: A=77.5, B=90.0, C=67.5.
# Expected sorted names: Lena, Omar, Sara, Anna, Denis.
# Use groupby() for group means. No row-by-row Python loops.

# Write your code below:

clean["passed"] = clean["score"] >= 60
clean["score_fraction"] = clean["score"] / 100

clean = clean.sort_values("score", ascending=False)

print(clean["score"].mean())
print(clean["passed"].mean() * 100)
print(clean.groupby("group")["score"].mean())
print(clean["name"].tolist())





# ========================================================================
# Task 14 — Export an analysis report
# ========================================================================
# Using clean from Tasks 12–13, save cleaned_students.csv with index=False.
# Create a group report with group and mean_score columns.
# Save group_report.csv with index=False, then reload it to check its columns.
# Convert clean[["score"]] to a NumPy array with dtype=float.
# Expected array shape: (5, 1). Use NumPy to calculate its mean: 76.0.
# Keep all exports separate from the supplied students.csv.

# Write your code below:


import numpy as np

clean.to_csv("cleaned_students.csv", index=False)

group_report = (
    clean.groupby("group", as_index=False)["score"]
    .mean()
    .rename(columns={"score": "mean_score"})
)

group_report.to_csv("group_report.csv", index=False)

check = pd.read_csv("group_report.csv")
print(check.columns)

score_array = clean[["score"]].to_numpy(dtype=float)

print(score_array.shape)
print(np.mean(score_array))





# ========================================================================
# Task 15 — BONUS: weighted assignment scores
# ========================================================================
# Load assignments.csv. Convert test_1 and test_2 to a NumPy array.
# Calculate final scores with weights [0.4, 0.6] using matrix multiplication.
# Add the results as a final_score column in the DataFrame.
# Expected final scores in file order: [76.0, 87.0, 56.0, 84.0].
# Print names whose final score is at least 80: Omar and Sara.

# Write your code below:


import numpy as np
import pandas as pd

df = pd.read_csv("assignments.csv")

scores = df[["test_1", "test_2"]].to_numpy(dtype=float)
weights = np.array([0.4, 0.6])

df["final_score"] = scores @ weights

print(df["final_score"].tolist())
print(df.loc[df["final_score"] >= 80, "name"].tolist())





# ========================================================================
# Task 16 — BONUS: a reusable CSV-analysis function
# ========================================================================
# Define analyze_scores(input_path, output_path).
# Require columns student_id, name, group, score. Raise ValueError if missing.
# Convert and validate scores as in Task 12.
# Raise ValueError if no valid scores remain.
# Save the cleaned table to output_path and return a dictionary containing
# valid_count, invalid_count, mean_score, and pass_percentage.
# For students.csv, expect 5, 3, 76.0, and 80.0 respectively.
# Use a temporary or separate output file. Do not overwrite the input.

# Write your code below:


import pandas as pd


def analyze_scores(input_path, output_path):
    df = pd.read_csv(input_path)

    required = {"student_id", "name", "group", "score"}

    if not required.issubset(df.columns):
        raise ValueError("Required columns are missing")

    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    valid_mask = df["score"].notna() & df["score"].between(0, 100)

    clean = df.loc[valid_mask].copy()

    invalid_count = len(df) - len(clean)

    if clean.empty:
        raise ValueError("No valid scores remain")

    clean.to_csv(output_path, index=False)

    return {
        "valid_count": len(clean),
        "invalid_count": invalid_count,
        "mean_score": clean["score"].mean(),
        "pass_percentage": (clean["score"] >= 60).mean() * 100
    }


result = analyze_scores(
    "students.csv",
    "students_analysis.csv"
)

print(result)



