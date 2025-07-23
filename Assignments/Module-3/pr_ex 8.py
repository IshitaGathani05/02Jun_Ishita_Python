#Write a Python program to handle multiple exceptions (e.g., file not found, division by zero). 
def example():
    try:
        print("Program to find the division of any number...")
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))

        result = a / b
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid integer numbers.")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

example()