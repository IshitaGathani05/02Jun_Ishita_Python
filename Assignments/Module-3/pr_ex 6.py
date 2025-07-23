#Write a Python program to check the current position of the file cursor using tell().

file = open("pr_ex6.txt", "w")

file.write("Hello, Python File Handling!")

# Check the current position of the file cursor
position = file.tell()
print(f"Current file cursor position: {position}")

file.close()
