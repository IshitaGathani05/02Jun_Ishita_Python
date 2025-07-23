#Write a Python program to read a file and print the data on the console

x=open("pr_ex4.txt", "r")

contents = x.read()

print("Your file content is:")

print(contents)