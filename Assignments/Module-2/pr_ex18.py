#Write a Python program to count how many times each character appears in a string.

# Input string
str = input("Enter a string: ")

# Create an empty dictionary to store character counts
count = {}

# Loop through each character in the string
for i in str:
    if i in count:
        count[i] += 1  # Increment count if character already exists
    else:
        count[i] = 1   # Initialize count if character is new

# Print the character counts
print("Character Frequencies:")
for i, count in count.items():
    print(f"'{i}': {count}")
