import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("students.csv")

# Display dataset
print("Dataset:")
print(df)

# Calculating average score
df["Average"] = (df["Math"] + df["ComputerScience"]) / 2

print("\nWith Average:")
print(df)

# Finding top student
top_student = df.loc[df["Average"].idxmax()]
print("\nTop Student:")
print(top_student)

# Find lowest student
low_student = df.loc[df["Average"].idxmin()]
print("\nLowest Student:")
print(low_student)


# Creates the bar chart
plt.bar(df["Name"], df["Average"])

plt.title("Student Average Scores")
plt.xlabel("Students")
plt.ylabel("Average Score")

plt.show()
