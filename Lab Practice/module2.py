#list
'''data=["python", "java", "php", "c++", "js"]
print(data)'''

'''print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:1])
print(data[:3])
'''

'''print(len(data))
data[1]="ios"
print(data)'''

'''for i in data:
    print(i)'''

#print(data.index("python"))

'''newdata=["html", "css", "html5"]
print(data+newdata)'''

'''if java in data:
    print("Yes...")
else:
    print("Nooo...")'''

#data.append("html")
#print(data)
#data.insert(2, "css")
#print(data)
#data.remove("c++")
'''data.append("html")
print(data)
data.pop(1)
print(data)'''
#data.clear()
#data.sort()
#data.reverse()
#del data[0]
#del data
#newdata = data.copy()
'''newdata = ["html", "css", "html5"]
print(newdata)
data.extend(newdata)
print(data)'''

#dictionary
'''data={'id':1, 'name':'ishita', 'sub':'python'}
print(data)
print(data["name"])
print(data.get("sub"))
print(data.keys())
print(data.values())

data["id"]=102
data["city"]='Rajkot'
print(data)

for i in data.values():
    print(i)

for i in data.items():
    print(i)

for i,j in data.items():
    print(f"Key={i} and Value={j}")

print(data)
data["city"]="Rajkot" #add a new pair
data['name']="ashok"#update a pair'''

#dynamic dictionary
'''a={}
n=int(input("How many pairs you want to add?"))
for i in range(n):
    key=input("Enter the key:")
    no=int(input("Enter the value:"))
    a[key]=no
print(a)'''

#dynamic value
'''data={}
keys=['id', 'name', 'city']

for i in range(len(keys)):
    v=input(f"Enter value of {keys[i]}:")
    data[keys[i]]=v

print(data)

#nested dictionary
stdata=[{'id':101, 'name':'ishita'},
        {'id':102, 'name':'abc'}]

print(stdata)

for i in stdata:
    print(i["name"])'''


#function
'''def getdata(id, name):
    print("Id:", id)
    print("Name", name)

n=int(input("Enter number of students:"))
for i in range(n):
    stid=input("Enter an id:")
    stnm=input("Enter a name:")
    getdata(stid, stnm)'''

#arbit Function
'''def getdata(*data):
    print("Id:", data[0])
    print("Name:", data[1])
    print("City:", data[2])

#getdata(101, 'Ishita', 'Rajlot')
getdata([101, 'Ishita', 'Rajlot'])'''

'''def getdata(id, name):
    print("Id:", id)
    print("Name", name)
    
student=[]

n=int(input("Enter number of students:"))
for i in range(n):
    stid=input("Enter an id:")
    stnm=input("Enter a name:")
    student.append([stid, stnm])

print("Student Details:")
for j in student:
    getdata(stid, stnm)'''



'''def getdata(id, name):
    print("Id:", id)
    print("Name", name)

students = {} 

n = int(input("Enter number of students: "))
for i in range(n):
    stid = input("Enter an id: ")
    stnm = input("Enter a name: ")
    students[stid] = stnm 

print("Student Details:")
for id, name in students.items():
    getdata(id, name)'''

#Bank Management System
'''1) Account Opening- a/c number, a/c holder name, a/c type
2) Deposit- min 2000/-
3) Withdrawal
4) Statement- a/c number, a/c holder name, a/c type, balance'''

def open(no, name, type):
    print("Acc number:", no)
    print("Acc name:", name)
    print("Acc type:", type)

def deposit():
    d=int(input("Enter the amount for deposit:"))
    if d<2000:
        print("You cannot deposit less than 2000")
    else:
        print("deposited:", d)
        return d

def withdrawal(d):
    w=int(input("Enter the amount for withdrawal:"))
    if w<=d:
        print("Amount should be greater than the balance")
    else:
        print("Withdrawed:", w)

open(1566, 'ishita', 'saving')
deposit()
withdrawal(3000)