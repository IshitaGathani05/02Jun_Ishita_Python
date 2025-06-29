#Write a Python program to calculate grades based on percentage using if-else ladder. 
s1=int(input("Enter Subject1 Mark:"))
s2=int(input("Enter Subject2 Mark:"))
s3=int(input("Enter Subject3 Mark:"))
s4=int(input("Enter Subject4 Mark:"))

total=s1+s2+s3+s4
print("Total is:", total)

pr=total/4
print("PR:", pr)

if pr>=90:
    print("A+ Grade")
elif pr>=80:
    print("A Grade")
elif pr>=70:
    print("B+ Grade")
elif pr>=60:
    print("B Grade")
elif pr>=50:
    print("C+ Grade")
elif pr>=40:
    print("C Grade")
else:
    print("Fail")
