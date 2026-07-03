import oracledb

connection = oracledb.connect(
    user="maham_intern",
    password="InternPass123",
    dsn="localhost:1521/FREEPDB1"
)

print("Connected successfully!")

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students (name) VALUES (:name)",
    {"name": "Hamza"}
)
connection.commit()
print("New student inserted.")

cursor.execute("SELECT id, name, enrollment_date FROM students")
print("\nAll Students:")
for row in cursor:
    print(row)

cursor.execute("""
    SELECT s.name, c.course_name
    FROM students s
    JOIN courses c ON s.id = c.student_id
""")
print("\nStudents with Courses:")
for row in cursor:
    print(row)

cursor.close()
connection.close()
print("\nConnection closed.")