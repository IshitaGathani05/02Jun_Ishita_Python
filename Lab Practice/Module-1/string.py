#string methods
#-------------------------#
#string as arrays
a = "Hello, World!" 
print(a[1]) 

#Slicing
b = "Hello, World!" 
print(b[2:5])

#String Length 
a = "Hello, World!" 
print(len(a)) 

#The strip() method removes any whitespace from the beginning or the end: 
a = " Hello, World! " 
print(a.strip()) 

# The lower() method returns the string in lower case: 
a = "Hello, World!" 
print(a.lower()) 

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The replace() method replaces a string with another string:
a = "Hi, Sanket!"
print(a.replace("J", "A"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String Format
age= 28
str= "My name is Sanket, and I am {}"
print(str.format(age))

#Python String capitalize()
str = "hello students, welcome to python world."
x = str.capitalize()
print (x)

#Python String casefold()
str = "hello students, welcome to python world."
x = str.casefold()
print (x)

#Python String count()
str = "I love apples, apple are my favorite fruit"
x = str.count("apple")
print(x)

#Python String endswith()
str = "Hello, welcome to Python."
x = str.endswith(".")
print(x)

#Python String find() - index()
str = "Hello, welcome to Python."
# x = str.find("welcome")
# x = str.index("welcome")
print(x)

#Python String isalnum()
txt = "Sanket123"
x = txt.isalnum()
print(x)

#Python String isalpha()
txt = "Sanket"
x = txt.isalpha()
print(x)

#Python String isdigit()
txt = "52500"
x = txt.isdigit()
print(x)

#Python String title()
txt = "welcome to python world"
x = txt.title()
print(x)
