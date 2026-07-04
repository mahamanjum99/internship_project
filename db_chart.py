import matplotlib.pyplot as plt
import oracledb

connection = oracledb.connect(
    user="maham_intern",
    password="InternPass123",
    dsn="localhost:1521/FREEPDB1"
)
cursor = connection.cursor()

cursor.execute("SELECT description, result_value FROM analysis_results")
rows = cursor.fetchall()

cursor.close()
connection.close()

descriptions = [row[0] for row in rows]
values = [row[1] for row in rows]

plt.figure(figsize=(8, 5))
plt.bar(descriptions, values, color=["orange", "green", "purple"])
plt.xlabel("Metric")
plt.ylabel("Value")
plt.title("Analysis Results from Database")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("analysis_results_chart.png")
print("Chart saved as analysis_results_chart.png")