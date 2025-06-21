#While Loop

'''i=1

while i<=10:
    print(i)
    i+=1'''

#Even Numbers
'''i=2
while i<=10:
    print(i)
    i+=2'''

#Odd Numbers
'''i=1
while i<=10:
    print(i)
    i+=2'''

#Table of 5
'''i=1
while i<=10:
    print(f"5*{i}={5*i}")
    i+=1'''

#for loop
'''for i in range(1, 11):
    print(f"5*{i}={5*i}")'''

#Nested for loop
'''table=int(input("How many tables you want?"))
for i in range(table):
    no1=int(input("Enter the table you want:"))
    for j in range(1, 11):
        print(f"{no1}*{j}={no1*j}")'''

#Factorial
'''n=int(input("Enter the factorial number you want:"))
fact=1
for i in range(1, n+1):
    fact=fact*i
    print(fact)
'''

#fibonacci series
'''n=int(input("Enter the number:"))
n1=0
n2=1
count=0
if n<=0:
    print("Please enter valid number!")
elif n==1:
    print(n1)
else:
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1'''

#leap year
'''n=int(input("Enter the year you want to check:"))
if(n%4==0):
    print("This year is leap year")
elif n%400==0:
    print("This year is leap year")
elif n%100==0:
    print("This year is leap year")
else:
    print("This year is not leap year")'''

#Armstrong number
'''n=int(input("Enter the number you wnat to check:"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp//=10

if n==sum:
    print("The number is armstrong number")
else:
    print("The number is not an armstrong number")'''

'''a=10
a=float(a)
print(type(a))'''

'''#sum of numbers
n=int(input("Enter number:"))
i=0
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print(sum)'''

#vowels and consonants in the string
'''str="asia"
vowels=0
consonants=0
for i in str:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1
    elif i.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)'''

#reverse string
'''str=input("Enter the string:")
print(str[::-1])'''

#palindrome checking
'''str=input("Enter the string:")
rev_string=str[::-1]
if str==rev_string:
    print("This string is palindrome")
else:
    print("This string is not palindrome")'''

#finding length of string without using len() function
'''str=input("Enter the string:")
count=0
for i in str:
    count=count+1
print("The length of your string is:", count)'''
