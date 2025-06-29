#Write a Python program to convert two lists into one dictionary using a for loop. 

keys = ['id', 'name', 'age']
values = [101, 'Alice', 22]

dict = {}

# Use a for loop to combine the lists
for i in range(len(keys)):
    dict[keys[i]] = values[i]

print("Combined Dictionary:", dict)