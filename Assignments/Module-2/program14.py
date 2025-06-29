#Write a Python program to merge two lists into one dictionary using a loop. 

keys = ['id', 'name', 'age']
values = [101, 'ishita', 18]

dict = {}

# Use a loop to merge the lists
for i in range(len(keys)):
    dict[keys[i]] = values[i]

print("Merged Dictionary:", dict)