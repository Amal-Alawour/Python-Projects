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


# Add student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    while True:
        age = input("Enter student age: ")

        if age.isdigit():
            age = int(age)
            break
        else:
            print("Please enter a valid age.")

    major = input("Enter student major: ").strip()

    cursor.execute(
        "INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
        (name, age, major)
    )

    connection.commit()
    print("Student added successfully!")


# View students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\nID | Name | Age | Major")
    print("-" * 35)

    for student in students:
        print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")


# Update student
def update_student():
    student_id = input("Enter student ID: ").strip()

    new_name = input("Enter new name: ").strip()

    if not new_name:
        print("Name cannot be empty.")
        return

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    cursor.execute(
        "UPDATE students SET name=? WHERE id=?",
        (new_name, student_id)
    )

    connection.commit()
    print("Student updated successfully!")


# Delete student
def delete_student():
    student_id = input("Enter student ID: ").strip()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    connection.commit()
    print("Student deleted successfully!")


# Search student
def search_student():
    keyword = input("Enter student name to search: ").strip()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + keyword + '%',)
    )

    students = cursor.fetchall()

    if not students:
        print("No matching students found.")
        return

    print("\nID | Name | Age | Major")
    print("-" * 35)

    for student in students:
        print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")


# Main menu
while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

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
        search_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice")


connection.close()
