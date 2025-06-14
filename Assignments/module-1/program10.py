# Write a Python program to check if a number is prime using if_else. 
i=1
no=int(input("Enter a number:"))
while i<=no:
    i+=1
    
    if no%i==0:
        print("Num is not prime")
        break
    else:
        print("Num is prime")
        break