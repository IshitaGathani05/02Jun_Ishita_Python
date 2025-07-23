#Write a Python program to show method overloading.

class studinfo:
    def getdata(self,id):
        print("ID:", id)

    def getdata(self,name):
        print("Name:", name)

st=studinfo()
st.getdata(101) # Python Does not support method overloading
st.getdata("Ishita")