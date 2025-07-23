#Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
def calculator(): 
    try:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print('''1. Addition
2. Subtraction
3. Multiplication
4. Division\n''')
        choice=int(input("Enter choice: "))
    
        if choice==1:
            result=a+b
        elif choice==2:
            result=a-b
        elif choice==3:
            result=a*b
        elif choice==4:
            result=a/b
        else:
            print("Invalid Choice...")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input! Please enter numeric values.")
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except Exception as e:
         print(f"An unexpected error occurred: {e}")


calculator()