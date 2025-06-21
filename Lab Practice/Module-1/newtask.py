while True:
    a=int(input("Enter No1:"))
    b=int(input("Enter No2:"))

    print("1:Add")
    print("2:SUb")
    print("3:Mul")
    print("4:DIv")

    choice=int(input("Select your choice:"))

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

    x=input("DO you continue? Yes/No :")
    if x=="no" or "No":
        break