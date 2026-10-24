
import csv
from pathlib import Path

FILE_NAME = Path(__file__).parent / "students.csv"


def load_students():
    students = []

    if FILE_NAME.exists():
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students = list(reader)

    return students


def save_students(students):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["roll_number", "name", "marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)


def add_student():
    roll_number = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    marks = input("Enter marks: ").strip()

    if not roll_number or not name or not marks:
        print("All fields are required.")
        return

    try:
        marks_value = float(marks)

        if marks_value < 0 or marks_value > 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter marks as a number.")
        return

    students = load_students()

    for student in students:
        if student["roll_number"] == roll_number:
            print("Roll number already exists.")
            return

    students.append({
        "roll_number": roll_number,
        "name": name,
        "marks": str(marks_value)
    })

    save_students(students)
    print("Student added successfully.")


def search_student():
    roll_number = input("Enter roll number to search: ").strip()
    students = load_students()

    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found")
            print("Roll Number:", student["roll_number"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def delete_student():
    roll_number = input("Enter roll number to delete: ").strip()
    students = load_students()

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def show_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(
            "Roll Number:", student["roll_number"],
            "| Name:", student["name"],
            "| Marks:", student["marks"]
        )


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Show All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        show_students()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
