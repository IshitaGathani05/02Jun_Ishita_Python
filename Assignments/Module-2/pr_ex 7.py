# Write a Python program to convert a list into a tuple.

city=[]

n=int(input("How many city you want to enter in the list:"))

for i in range(n):
    x=input(f"Enter city{i+1}:")
    city.append(x)

print(tuple(city))