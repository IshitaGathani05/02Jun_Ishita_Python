#Write a Python program to write multiple strings into a file. 
str=[
    "Hello Python!\n",
    "This is a multiple string\n",
    "This is a python's file handling"
]

x=open("program5.txt", "w")

x.writelines(str)

print("Multiple strings written into the program5.txt file successfully...")