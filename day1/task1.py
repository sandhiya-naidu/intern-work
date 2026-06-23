# Employee Salary Calculator

# Taking inputs
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
salary = float(input("Enter Salary: "))
experience = int(input("Enter Experience (in years): "))
is_permanent = input("Is Permanent Employee (True/False): ")
department = input("Enter Department: ")

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
travel_allowance = salary*0.05
food_allowance = salary*0.03 # Example food allowance
# Final salary
allowance = travel_allowance + food_allowance
final_salary = salary + bonus + allowance

# Output
print("\n--- Employee Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Salary:", salary)
print("Experience:", experience)
print("Permanent:", is_permanent)
print("Department:", department)
print("\nBonus:", bonus)
print("Final Salary:", final_salary)