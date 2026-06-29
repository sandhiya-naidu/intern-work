import csv
import json
import os

# User Input
name = input("Enter Name: ")
email = input("Enter Email: ")
skills = input("Enter Skills (comma separated): ").split(",")

student = {
    "Name": name,
    "Email": email,
    "Skills": skills
}

# ---------------- TXT FILE ----------------

with open("student.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Skills: {', '.join(skills)}\n")
    file.write("-" * 30 + "\n")

print("\nReading TXT File")
with open("student.txt", "r") as file:
    print(file.read())

# ---------------- CSV FILE ----------------

file_exists = os.path.exists("student.csv")

with open("student.csv", "a", newline="") as file:
    writer = csv.writer(file)

    # Write header only once
    if not file_exists or os.path.getsize("student.csv") == 0:
        writer.writerow(["Name", "Email", "Skills"])

    writer.writerow([name, email, ", ".join(skills)])

print("\nReading CSV File")
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ---------------- JSON FILE ----------------

if os.path.exists("student.json"):
    with open("student.json", "r") as file:
        try:
            students = json.load(file)
        except json.JSONDecodeError:
            students = []
else:
    students = []

students.append(student)

with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nReading JSON File")
with open("student.json", "r") as file:
    data = json.load(file)
    print(data)