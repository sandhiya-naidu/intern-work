import csv
import json

# User Input
name = input("Enter Name: ")
email = input("Enter Email: ")
skills = input("Enter Skills (comma separated): ").split(",")

student = {
    "Name": name,
    "Email": email,
    "Skills": skills
}

# Write into TXT file
with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Skills: {', '.join(skills)}\n")

# Read TXT file
print("\nReading TXT File")
with open("student.txt", "r") as file:
    print(file.read())

# Write into CSV file
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email", "Skills"])
    writer.writerow([name, email, ", ".join(skills)])

# Read CSV file
print("\nReading CSV File")
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Write into JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read JSON file
print("\nReading JSON File")
with open("student.json", "r") as file:
    data = json.load(file)
    print(data)