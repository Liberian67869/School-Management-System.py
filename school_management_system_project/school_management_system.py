import json
import os

DATA_FILE = "school_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {"students": [], "teachers": [], "marks": {}}
    return {"students": [], "teachers": [], "marks": {}}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def login():
    print("===== SCHOOL SYSTEM LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "1234":
        print("Login successful!")
        return True
    print("Invalid login!")
    return False

def add_student(data):
    student = {
        "id": f"STU{len(data['students'])+1:03}",
        "name": input("Enter student name: "),
        "age": int(input("Enter age: ")),
        "phone": input("Enter phone: "),
        "email": input("Enter email: ")
    }
    data["students"].append(student)

def add_teacher(data):
    teacher = {
        "id": f"TCH{len(data['teachers'])+1:03}",
        "name": input("Enter teacher name: "),
        "age": int(input("Enter age: ")),
        "phone": input("Enter phone: "),
        "email": input("Enter email: ")
    }
    data["teachers"].append(teacher)

def view_students(data):
    for s in data["students"]:
        print(s)

def view_teachers(data):
    for t in data["teachers"]:
        print(t)

def menu():
    data = load_data()
    while True:
        print("\\n1.Add Student\\n2.Add Teacher\\n3.View Students\\n4.View Teachers\\n5.Save & Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_student(data)
        elif choice == "2":
            add_teacher(data)
        elif choice == "3":
            view_students(data)
        elif choice == "4":
            view_teachers(data)
        elif choice == "5":
            save_data(data)
            break

if __name__ == "__main__":
    if login():
        menu()
