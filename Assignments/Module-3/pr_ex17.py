#Write a Python program to show hybrid inheritance.

class Person:
    def display(self):
        print("This is a person.")

class Student(Person):
    def show(self):
        print("This is a student.")

class Teacher(Person):
    def print_data(self):
        print("This is a teacher.")

# Child class with multiple inheritance (Hybrid part)
class Result(Student, Teacher):
    def disp(self):
        print("This is the result of hybrid inheritance.")

r = Result()

r.display()    
r.show()   
r.print_data()  
r.disp()    
