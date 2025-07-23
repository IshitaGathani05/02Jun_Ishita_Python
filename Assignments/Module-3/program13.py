#Write a Python program to match a word in a string using re.match().
import re

text = input("Enter a string: ")
word = input("Enter the word to match: ")

# Use re.match() to check if the word is at the beginning of the string
# \b ensures it's a complete word match
pattern = r'\b' + re.escape(word) + r'\b'

match = re.match(pattern, text)

if match:
    print(f"The word '{word}' MATCHES the beginning of the string.")
else:
    print(f"The word '{word}' does NOT match the beginning of the string.")