import numpy as np
import pandas as pd
import cv2
import oracledb

# ========== 1. NumPy Basics ==========
print("===== NumPy =====")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Std Dev:", np.std(arr))
print("Max:", np.max(arr), "| Min:", np.min(arr))

# ========== 2. Pandas Basics ==========
print("\n===== Pandas =====")
data = {
    "name": ["Ali", "Sara", "Zain"],
    "marks": [85, 92, 78]
}
df = pd.DataFrame(data)
print(df)
print("\nAverage marks:", df["marks"].mean())

# ========== 3. OpenCV - Image I/O ==========
print("\n===== OpenCV =====")
img = np.zeros((100, 100, 3), dtype=np.uint8)
img[:] = (0, 255, 0)  # green image
cv2.imwrite("test_image.png", img)
print("Test image saved as test_image.png")

loaded_img = cv2.imread("test_image.png")
avg_pixel_value = float(np.mean(loaded_img))
print("Average pixel value of image:", avg_pixel_value)

# ========== 4. Result ko Database mein save karo ==========
print("\n===== Saving results to Oracle DB =====")

connection = oracledb.connect(
    user="maham_intern",
    password="InternPass123",
    dsn="localhost:1521/FREEPDB1"
)
cursor = connection.cursor()

try:
    cursor.execute("""
        CREATE TABLE analysis_results (
            id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            description VARCHAR2(100),
            result_value NUMBER,
            created_at DATE DEFAULT SYSTIMESTAMP
        )
    """)
    print("Table 'analysis_results' created.")
except oracledb.DatabaseError as e:
    print("Table already exists, skipping creation.")

cursor.execute(
    "INSERT INTO analysis_results (description, result_value) VALUES (:descr, :val)",
    {"descr": "numpy_array_mean", "val": float(np.mean(arr))}
)

cursor.execute(
    "INSERT INTO analysis_results (description, result_value) VALUES (:descr, :val)",
    {"descr": "pandas_average_marks", "val": float(df["marks"].mean())}
)

cursor.execute(
    "INSERT INTO analysis_results (description, result_value) VALUES (:descr, :val)",
    {"descr": "opencv_avg_pixel_value", "val": avg_pixel_value}
)

connection.commit()
print("All results saved to database.")

cursor.execute("SELECT description, result_value, created_at FROM analysis_results")
print("\n===== Data in analysis_results table =====")
for row in cursor:
    print(row)

cursor.close()
connection.close()
print("\nConnection closed.")