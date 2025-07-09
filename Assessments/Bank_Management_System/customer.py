# Function to get all customer records
def load_customers():
    customers = []
    try:
        with open("Customer.txt", "r") as file:
            for line in file:
                acc_no, name, balance = line.strip().split(",")
                customers.append({
                    "acc_no": acc_no,
                    "name": name,
                    "balance": int(balance)
                })
    except FileNotFoundError:
        print("Customer file not found.")
    return customers

# Function to save all customer records
def save_customers(customers):
    with open("Customer.txt", "w") as file:
        for cust in customers:
            file.write(f"{cust['acc_no']},{cust['name']},{cust['balance']}\n")

#Current Balance
def current_balance():
    acc = input("Enter your account number: ")
    customers = load_customers()
    for cust in customers:
        if cust["acc_no"] == acc:
            print("Hello", cust["name"])
            print("Your current balance is:", cust["balance"])
            return
    print("Account not found.")

#Deposit Amount
def deposit():
    acc = input("Enter your account number: ")
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 500:
            print("Minimum deposit must be more than ₹500.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    customers = load_customers()
    updated = False
    for cust in customers:
        if cust["acc_no"] == acc:
            cust["balance"] += amount
            print("Amount deposited successfully.")
            updated = True
            break

    if updated:
        save_customers(customers)
    else:
        print("Account not found.")

#Withdraw Amount
def withdraw():
    acc = input("Enter your account number: ")
    try:
        amount = int(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount.")
        return

    customers = load_customers()
    updated = False
    for cust in customers:
        if cust["acc_no"] == acc:
            if cust["balance"] - amount >= 500:
                cust["balance"] -= amount
                print("Amount withdrawn successfully.")
                updated = True
            else:
                print("Insufficient balance! Minimum ₹500 must remain.")
            break

    if updated:
        save_customers(customers)
    else:
        print("Account not found.")

#Updated Balance
def updated_balance():
    acc = input("Enter your account number: ")
    customers = load_customers()
    for cust in customers:
        if cust["acc_no"] == acc:
            print("Updated balance for", cust["name"], "is ₹", cust["balance"])
            return
    print("Account not found.")

def menu():
    while True:
        print("\n==== Welcome to Customer's App ====")
        print("1. View Current Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Updated Balance")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            current_balance()

        elif choice=="2":
            deposit()

        elif choice=="3":
            withdraw()

        elif choice=="4":
            updated_balance()
        
        elif choice=="5":
            break

        else:
            print("Invalid choice. Try again.")

#menu()