#Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

#Single Inheritance
'''class father:
    bal:int
    car:int

    def getdata(self):
        self.bal=input("Enter a bank balance details:")
        self.car=input("Enter a car details:")

class son(father):
    def printdata(self):
        print("Balance:", self.bal)
        print("Car:", self.car)

sn=son()
sn.getdata()
sn.printdata()'''

#Multiple Inheritance
'''class ishita:
    sid:int
    ssub:str

    def i_getdata(self):
        self.sid=input("Enter ishita's id:")
        self.ssub=input("Enter ishita's subject:")

class abc:
    aid:int
    asub:str

    def a_getdata(self):
        self.aid=input("Enter abc's id:")
        self.asub=input("Enter abc's subject:")

class xyz:
    xid:int
    xsub:str

    def x_getdata(self):
        self.xid=input("Enter xyz's id:")
        self.xsub=input("Enter xyz's subject:")

class demo(ishita, abc, xyz):
    def printdata(self):
        print("-----Ishita's info-----")
        print("Ishita's id:", self.sid)
        print("Ishita's subject:", self.ssub)
        print("-----abc's info-----")
        print("abc's id:", self.aid)
        print("abc's subject:", self.asub)
        print("-----xyz's info-----")
        print("xyz's id:", self.xid)
        print("xyz's subject:", self.xsub)

d=demo()
d.i_getdata()
d.a_getdata()
d.x_getdata()
d.printdata()'''

#Multilevel Inheritance
class ishita:
    sid:int
    ssub:str

    def i_getdata(self):
        self.sid=input("Enter ishita's id:")
        self.ssub=input("Enter ishita's subject:")

class abc(ishita):
    aid:int
    asub:str

    def a_getdata(self):
        self.aid=input("Enter abc's id:")
        self.asub=input("Enter abc's subject:")

class xyz(abc):
    xid:int
    xsub:str

    def x_getdata(self):
        self.xid=input("Enter xyz's id:")
        self.xsub=input("Enter xyz's subject:")

class demo(xyz):
    def printdata(self):
        print("-----Ishita's info-----")
        print("Ishita's id:", self.sid)
        print("Ishita's subject:", self.ssub)
        print("-----abc's info-----")
        print("abc's id:", self.aid)
        print("abc's subject:", self.asub)
        print("-----xyz's info-----")
        print("xyz's id:", self.xid)
        print("xyz's subject:", self.xsub)

d=demo()
d.i_getdata()
d.a_getdata()
d.x_getdata()
d.printdata()