# Employee Data Processing Tool

# Input
employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEmployee {i+1}")

    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    employees.append({
        "name": name,
        "salary": salary,
        "department": department
    })

# List Comprehension
employee_names = [emp["name"] for emp in employees]

print("\nEmployee Names")
print(employee_names)

# Lambda + map
updated_salary = list(map(lambda emp: emp["salary"] * 1.10, employees))

print("\nSalary after 10% increment")
print(updated_salary)

# Filter
high_salary = list(filter(lambda emp: emp["salary"] >= 50000, employees))

print("\nEmployees with salary >= 50000")
for emp in high_salary:
    print(emp)

# Decorator
def report_decorator(func):
    def wrapper():
        print("\n----- Employee Report -----")
        func()
        print("---------------------------")
    return wrapper

@report_decorator
def generate_report():
    for emp in employees:
        print(emp)

generate_report()

# Generator
def employee_generator():
    for emp in employees:
        yield emp

print("\nGenerator Output")

for emp in employee_generator():
    print(emp)