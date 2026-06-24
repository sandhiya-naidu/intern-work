def create_account(name):
    """Create a bank account"""
    print(f"\nAccount created for {name}")
    return 0   # initial balance


def deposit(balance, amount):
    """Deposit money"""
    balance += amount
    print("Deposit successful")
    return balance


def withdraw(balance, amount):
    """Withdraw money"""
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawal successful")
    return balance


# Main program
name = input("Enter account holder name: ")
balance = create_account(name)

dep = float(input("Enter deposit amount: "))
balance = deposit(balance, dep)

wd = float(input("Enter withdraw amount: "))
balance = withdraw(balance, wd)

print("Final Balance:", balance)