#Write a Python program to read the contents of a file and print them on the console.

x=open("program3.txt", "r")

contents = x.read()

print("Your file content is:")

print(contents)