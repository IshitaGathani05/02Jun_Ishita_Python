#Write a Python program to insert elements into an empty list using a for loop and append().

list = []

# Number of elements to insert
n=int(input("How many elements you want to add in the list:"))

# Use a for loop to insert elements
for i in range(n):
    x= input(f"Enter element {i+1}: ")
    list.append(x)

# Print the final list
print("Final List:", list)