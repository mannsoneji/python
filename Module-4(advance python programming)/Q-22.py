# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

# In Python, a class is a blueprint for creating objects.A class encapsulates data for the object and functions that operate on that data. It allows you to bundle data and functionality together. You define a class using the class keyword.

# What Is self?

# ---> The self keyword in Python is a reference to the current instance of the class. It allows the class methods to access and modify the instance's attributes and call other methods. In other words, self is used to represent the object itself.

class example:
    def display(self):
        print("Hello welcome to sample class")
    
    def show(self):
        print("This is class program")

obj = example()
obj.display()
obj.show()
