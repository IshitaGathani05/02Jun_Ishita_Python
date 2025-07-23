#Write a Python program to search for a word in a string using re.search().
import re

text = input("Enter a string: ")
word = input("Enter the word to search: ")

# The pattern uses \b to ensure the word is matched exactly (not as a part of another word)
pattern = r'\b' + re.escape(word) + r'\b'

match = re.search(pattern, text)

if match:
    print(f"The word '{word}' was found in the string.")
else:
    print(f"The word '{word}' was NOT found in the string.")