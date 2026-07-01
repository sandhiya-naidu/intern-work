import re

print("=== User Registration ===")

username = input("Enter Username: ")
email = input("Enter Email: ")
phone = input("Enter Phone Number: ")
password = input("Enter Password: ")

errors = []

# Username Validation 
if len(username) < 3:
    errors.append("Username must be at least 3 characters")

# Email Validation
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if not re.match(email_pattern, email):
    errors.append("Invalid Email format")

# Phone Validation
phone_pattern = r"^[0-9]{10}$"

if not re.match(phone_pattern, phone):
    errors.append("Phone must be exactly 10 digits")

# Password Validation
# At least 1 uppercase, 1 lowercase, 1 digit, min 6 chars
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$"

if not re.match(password_pattern, password):
    errors.append("Password must be 6+ chars with uppercase, lowercase, and number")

#  Final Output 
print("\n--- Result ---")

if len(errors) == 0:
    print("Registration Successful")
else:
    print("Registration Failed")
    for err in errors:
        print("-", err)