'''a=int((input("Enter the value of A:")))
b=int((input("Enter the value of B:")))
print("Add is:", a+b)
print("Sub is:", a-b)
print("Mul is:", a*b)
print("Div is:", a/b)'''

#Menu Driven Program of Calc
a=int(input("Enter number1:"))
b=int(input("Enter number2:"))

choice=int(input('''Enter a choice:
      1: Addition
      2:Subtraction
      3.Multiplication
      4.Division\n'''))

if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print("Invalid Choice")