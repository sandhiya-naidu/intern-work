from datetime import datetime
import random
import math


class WrongPINError(Exception):
    pass


balance = 5000
correct_pin = 1234

try:

    pin = int(input("Enter PIN: "))

    if pin != correct_pin:
        raise WrongPINError("Wrong PIN")

    print("\nLogin Successful")

    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter choice: "))

    if choice == 1:

        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        balance += amount

        print("Deposit Successful")

    elif choice == 2:

        amount = float(input("Enter withdraw amount: "))

        if amount > balance:
            raise ValueError("Insufficient Balance")

        balance -= amount

        print("Withdrawal Successful")

    else:
        print("Invalid Choice")

    print("Updated Balance:", balance)

    print("Transaction Time:", datetime.now())

    transaction_id = random.randint(10000, 99999)
    print("Transaction ID:", transaction_id)

    print("Square Root of Balance:", math.sqrt(balance))

except WrongPINError as e:
    print(e)

except ValueError as e:
    print(e)

except Exception as e:
    print("Error:", e)

finally:
    print("Thank you for using ATM")