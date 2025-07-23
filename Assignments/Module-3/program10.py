#Write Python programs to demonstrate method overloading and method overriding.

#Method Overloading
'''class studinfo:
    def getdata(self,id):
        print("ID:", id)

    def getdata(self,name):
        print("Name:", name)

st=studinfo()
st.getdata(101) # Python Does not support Method Overloading
st.getdata("Ishita")'''

#Method overriding
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