#Write a Python program that manipulates and prints strings using various string methods. 
str="Hello, World!"
var="Hii, Welcome to python!"

#String as arrays-----
print("String as arrays:", str[1])

#String Slicing---------
print("String Slicing:", str[2:5])

#String Length----------
print("String Length:", len(str))

#strip Method-------------
print("strip Method:", str.strip())

#lower method-----------
print("lower Method", str.lower())

#upper method-----------------
print("upper Method", str.upper())

#replace method----------------
print("replace Method", str.replace("!", "."))

#split method-------------
print("split Method:", str.split("e"))

#String concatenation-------------
str1="This is python..."
print("String Concatenation:", str + str1)

#string format--------------------
age= 50
str1= "My name is ishita, and I am {}" 
print(str1.format(age))

#capitalize Method-------------
print("capitalize Method:", str.capitalize())

#casefold Method-------------
print("casefold Method:", str.casefold())

#count Method---------
print("count Method:", str.count("Hello"))

#endswith Method-------------
print("endswith Method:", str.endswith("."))

#find and index method-----------
print("index Method:", var.index("Welcome"))
print("find Method:", var.find("Welcome"))

#isalnum Method------------------
print("isalnum Method:", str.isalnum())

#isalpha Method---------------
print("isalpha Method:", str.isalpha())

#isdigit Method-----------------------
print("isdigit Method:", str.isdigit())

#title Method-------------------
print("title Method:", str.title())