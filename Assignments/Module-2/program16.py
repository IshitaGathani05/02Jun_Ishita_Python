#Write a Python program to create a calculator using functions.
def add(a,b):
    print("Sum:", a+b)

def sub(a, b):
    print("Subtraction:", a-b)

def mul(a, b):
    print("Multiplication:", a*b)

def div(a, b):
    if b==0:
        print("Cannot divide by zero!")
    else:
        print("Division:", a/b)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

add(a, b)
sub(a, b)
mul(a, b)
div(a, b)