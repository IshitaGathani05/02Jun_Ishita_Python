#Write a Python program to create a class and access its properties using an object.
class student:
    def getdata(self):
        self.id=int(input("Enter id:"))
        self.name=input("Enter name:")

    def printdata(self):
        print("Id:", self.id)
        print("Name:", self.name)

st=student()
st.getdata()
st.printdata()