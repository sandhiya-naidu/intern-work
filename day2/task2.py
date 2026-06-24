# Day 2 - Employee Attendance Management System

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\n--- Employee", i + 1, "---")

    name = input("Enter employee name: ")
    working_days = int(input("Enter total working days: "))
    present_days = int(input("Enter present days: "))
    rating = float(input("Enter performance rating (0 to 5): "))
 
    if present_days > working_days:
        print("error")
    else:
        continue
    # Attendance calculation
    attendance_percentage = (present_days / working_days) * 100

    # Attendance status using conditions
    if attendance_percentage >= 90:
        attendance_status = "Excellent Attendance"
    elif attendance_percentage >= 75:
        attendance_status = "Good Attendance"
    elif attendance_percentage >= 50:
        attendance_status = "Average Attendance"
    else:
        attendance_status = "Poor Attendance"

    # Bonus eligibility
    if attendance_percentage >= 80 and rating >= 4:
        bonus = "Eligible for Bonus"
    else:
        bonus = "Not Eligible for Bonus"

    # Performance status
    if rating >= 4.5:
        performance = "Outstanding"
    elif rating >= 3.5:
        performance = "Good"
    elif rating >= 2.5:
        performance = "Average"
    else:
        performance = "Poor"

    # Output
    print("\n--- Employee Report ---")
    print("Name:", name)
    print("Attendance %:", round(attendance_percentage, 2))
    print("Attendance Status:", attendance_status)
    print("Bonus:", bonus)
    print("Performance:", performance)
    