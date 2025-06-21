s1=int(input("Enter Subject1 Mark:"))
s2=int(input("Enter Subject2 Mark:"))
s3=int(input("Enter Subject3 Mark:"))
s4=int(input("Enter Subject4 Mark:"))

if s1>=40 and s2>=40 and s3>=40 and s4>=40:

 total=s1+s2+s3+s4
 print("Total is:", total)

 pr=total/4
 print("PR:", pr)

 if pr>=70:
    print("Distinctiopn")
 elif pr>=60:
    print("First Class")
 elif pr>=50:
    print("Second Class")
 elif pr>=40:
    print("Pass Class")
 else:
    print("Fail")


