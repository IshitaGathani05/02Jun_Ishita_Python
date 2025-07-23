#Write a Python program to show method overriding.

class studinfo:
    def getdata(self,id,name): #original
        print("ID:", id)
        print("Name:", name)

class home(studinfo): #reference
    def getdata(self, id, name): #Xerox
        return super().getdata(id, name)
    
class about(studinfo):
    def getdata(self, id, name):
        return super().getdata(id, name)
    
a=about()
a.getdata(101, "Ishita")
a.getdata(102, "abc")