import matplotlib.pyplot as plt
import pandas as pd

data = {
    "name": ["Ali", "Sara", "Zain"],
    "marks": [85, 92, 78]
}
df = pd.DataFrame(data)

plt.bar(df["name"], df["marks"], color="skyblue")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.savefig("marks_chart.png")
print("Chart saved as marks_chart.png")