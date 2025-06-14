#list
data=["python", "java", "php", "c++", "js"]
print(data)

print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:1])
print(data[:3])


print(len(data))
data[1]="ios"
print(data)

for i in data:
    print(i)

print(data.index("python"))

'''newdata=["html", "css", "html5"]
print(data+newdata)'''

'''if java in data:
    print("Yes...")
else:
    print("Nooo...")'''

#list methods

data.append("html")
#print(data)
data.insert(2, "css")
#print(data)
data.remove("c++")
print(data)