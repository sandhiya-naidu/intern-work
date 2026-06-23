# Input
name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

skills = input("Enter skills (comma separated): ").split(",")

marks = int(input("Enter marks: "))

# Create dictionary
student = {
    "name": name,
    "age": age,
    "course": course,
    "skills": skills,
    "marks": marks
}

# Update skills
new_skill = input("Enter a new skill to add: ")
student["skills"].append(new_skill)

# Unique student records
unique_students = set()
unique_students.add(name)

# Output
print("\nStudent Profile:")
print(student)

print("\nUpdated Skills:")
print(student["skills"])

print("\nUnique Students:")
print(unique_students)