# Write a Python program to print custom exceptions.

# Step 1: Define a custom exception class
class AgeTooSmallError(Exception):
    def __init__(self, message="Age is too small to proceed. Must be at least 18."):
        self.message = message
        super().__init__(self.message)

# Step 2: Use the custom exception in a program
def check_age(age):
    if age < 18:
        raise AgeTooSmallError()  # Raise the custom exception
    else:
        print("Access granted. Age is valid.")

# Step 3: Handle the exception using try-except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)

except AgeTooSmallError as e:
    print("Custom Exception Caught:", e)

except ValueError:
    print("Invalid input. Please enter a numeric value.")
