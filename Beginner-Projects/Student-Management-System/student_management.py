import sqlite3

# Create database connection
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT
)
""")

connection.commit()


def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    major = input("Enter student major: ")

    cursor.execute(
        "INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
        (name, age, major)
    )

    connection.commit()
    print("Student added successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        print(student)


def update_student():
    student_id = input("Enter student ID: ")
    new_name = input("Enter new name: ")

    cursor.execute(
        "UPDATE students SET name=? WHERE id=?",
        (new_name, student_id)
    )

    connection.commit()
    print("Student updated successfully!")


def delete_student():
    student_id = input("Enter student ID: ")

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    connection.commit()
    print("Student deleted successfully!")


while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

    else:
        print("Invalid choice")


connection.close()
