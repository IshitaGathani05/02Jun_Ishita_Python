#Wap to make a simple calc with user choice, after one operation its ask for another operation.
#Use yes or no option for operation


while True:
    choice=int(input('''1.Addition
2:Subtraction
3.Multiplication
4.Division
Enter your choice:'''))

    a=int(input("Enter first number:"))
    b=int(input("Enter Second number:"))
    if choice==1:
        print("Addition:", a+b)
    elif choice==2:
        print("Subtraction:", a-b)
    elif choice==3:
         print("Multiplication:", a*b)
    elif choice==4:
        print("Division:", a/b)
    else:
        print("Invalid Choice...")
    var=(input("You wwant to perform another operation?"))
    if choice!='yes':
      print("Ending Operation")
    