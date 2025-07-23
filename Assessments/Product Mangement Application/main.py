from register import register_window

print("1. Register as Product Manager")
print("2. Register as Customer")

choice = input("Enter your choice: ")
if choice == '1':
    register_window('manager')
elif choice == '2':
    register_window('customer')
else:
    print("Invalid choice")
