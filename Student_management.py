import json
import os

FILE_NAME = "Student_data.json"

# Load Data
def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []

# Save Data
def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add Student
def add_student(students):
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")

    students.append({
        "id": sid,
        "name": name,
        "grade": grade
    })

    save_data(students)
    print("Student Added Successfully!")

# View Students
def view_students(students):
    if not students:
        print("\nNo Student Records Found!")
        return

    print("\n------ Student Records ------")
    print("{:<10}{:<20}{:<10}".format("ID", "Name", "Grade"))

    for student in students:
        print("{:<10}{:<20}{:<10}".format(
            student["id"],
            student["name"],
            student["grade"]
        ))

# Update Student
def update_student(students):
    sid = input("Enter Student ID to Update: ")

    for student in students:
        if student["id"] == sid:
            student["name"] = input("Enter New Name: ")
            student["grade"] = input("Enter New Grade: ")
            save_data(students)
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")

# Delete Student
def delete_student(students):
    sid = input("Enter Student ID to Delete: ")

    for student in students:
        if student["id"] == sid:
            students.remove(student)
            save_data(students)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

# Main Menu
def main():
    students = load_data()

    while True:
        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please Try Again.")

if __name__ == "__main__":
    main()