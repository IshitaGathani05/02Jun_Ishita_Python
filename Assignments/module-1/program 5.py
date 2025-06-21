# How does the Python code structure work? 
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print(a, "is maximum")
elif b>c and b>a:
    print(b, "is maximum")
else:
    print(c, "is maximum")