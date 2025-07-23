#Write a Python program to demonstrate the use of local and global variables in a class.

# Global variable
x = 100

class demo:
    def ex(self):
        # Local variable
        x = 50
        y = 20
        print("Inside class method:")
        print("Local variable x:", x)      # Local to this method
        print("Local variable y:", y)
        print("Global variable x (accessed using global name):", globals()['x'])

# Create object of the class
obj = demo()
obj.ex()

print("\nOutside class:")
print("Global variable x:", x)
