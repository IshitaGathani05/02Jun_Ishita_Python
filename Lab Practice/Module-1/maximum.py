#wap to find the max between four num using nested if 
a=int(input("Enter no1:"))
b=int(input("Enter no2:"))
c=int(input("Enter no3:"))
d=int(input("Enter no4:"))
if a>b and a>c and a>d:
    print("A is maximum")
elif b>c and b>a and b>d:
    print("B is maximum")
elif c>d and c>a and c>b:
    print("C is maximum")
else:
    print("D is maximum")


# ------------------------------ #
# Taking 4 numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# Using nested if to directly print the maximum
if a > b:
    if a > c:
        if a > d:
            print("Maximum number is:", a)
        else:
            print("Maximum number is:", d)
    else:
        if c > d:
            print("Maximum number is:", c)
        else:
            print("Maximum number is:", d)
else:
    if b > c:
        if b > d:
            print("Maximum number is:", b)
        else:
            print("Maximum number is:", d)
    else:
        if c > d:
            print("Maximum number is:", c)
        else:
            print("Maximum number is:", d)
