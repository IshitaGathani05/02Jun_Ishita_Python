# Add Customer
def add_customer():
    acc_no = input("Enter Account Number: ")
    customer_name = input("Enter Customer Name: ")
    try:
        opening_balance = int(input("Enter Opening Balance: "))
    except ValueError:
        print("Invalid balance amount.")
        return

    with open("Customer.txt", "a") as file:
        file.write(f"{acc_no },{customer_name},{opening_balance}\n")

    print("Customer added successfully!")

# Output a single customer
def out_add_customer(acc_no, customer_name, opening_balance):
    print("---Customer Details---")
    print("Account Number: ", acc_no)
    print("Customer Name: ", customer_name)
    print("Opening Balance: ", opening_balance)

# View Customer (Last Added)
def view_customer():
    try:
        with open("Customer.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last = lines[-1]
                acc_no, name, balance = last.strip().split(",")
                out_add_customer(acc_no, name, balance)
            else:
                print("No customers to view.")
    except FileNotFoundError:
        print("Customer file not found.")

# Search Customer by Account Number
def search_customer():
    search = input("Enter Account Number to Search: ")
    found = False
    try:
        with open("Customer.txt", "r") as file:
            for line in file:
                acc_no, name, balance = line.strip().split(",")
                if acc_no == search:
                    out_add_customer(acc_no, name, balance)
                    found = True
                    break
        if not found:
            print("Customer not found.")
    except FileNotFoundError:
        print("Customer file not found.")

# View All Customers
def view_all_customer():
    print("=== All Customers ===")
    try:
        with open("Customer.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No customers found.")
                return
            for line in lines:
                acc_no, name, balance = line.strip().split(",")
                out_add_customer(acc_no, name, balance)
                print("---------------------")
    except FileNotFoundError:
        print("Customer file not found.")

#Total Amount in Bank
def bank_accounts():
    total = 0
    try:
        with open("Customer.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    total += int(parts[2])
        print("Total amount in bank:", total)
    except FileNotFoundError:
        print("Customer file not found.")
    except ValueError:
        print("Invalid data format in file.")

# Sample menu to test all features
def menu():
    while True:
        print("\n==== Welcome to Banker's App ====")
        print("1. Add Customer")
        print("2. View Last Customer")
        print("3. Search Customer")
        print("4. View All Customers")
        print("5. Show Total Bank Balance")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customer()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            view_all_customer()
        elif choice == "5":
            bank_accounts()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
#menu()