# Employee Salary Calculator

# Taking inputs
name = input("Enter Employee Name: ")
age = int(input("Enter Age: "))
salary = float(input("Enter Salary: "))
experience = int(input("Enter Experience (in years): "))
is_permanent = input("Is Permanent Employee (True/False): ")

# Convert string to boolean
is_permanent = is_permanent.lower() == "true"

# Calculate bonus
if experience > 5:
    bonus = salary * 0.20
else:
    bonus = salary * 0.10

# Extra bonus if permanent
if is_permanent:
    bonus += 1000

# Final salary
final_salary = salary + bonus

# Output
print("\n--- Employee Details ---")
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Experience:", experience)
print("Permanent:", is_permanent)

print("\nBonus:", bonus)
print("Final Salary:", final_salary)