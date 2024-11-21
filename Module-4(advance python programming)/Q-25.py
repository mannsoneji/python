# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

# Inheritance is one of the key concepts of Object-Oriented Programming (OOP), which allows a class to inherit attributes and methods from another class. 

# In Python, inheritance allows you to create a new class by using details from an existing class. The new class, called a child class or subclass, inherits the properties and methods of the existing class, which is called the parent class or superclass.

# syntax of inheritance :
"""
class ParentClass:
    # Parent class code
    pass

class ChildClass(ParentClass):
    # Child class inherits from ParentClass
    pass

"""
class parent:
    def dis1(self):
        print("parent class is here")

class child(parent):
    def dis2(self):
        print("child class is here")

obj = child()
obj.dis1()
obj.dis2()



# What is init?

# The __init__ method in Python is a special method that is automatically called when a new object of a class is created. It is commonly known as the constructor. This method is used to initialize the object's attributes when the object is created.

# syntax of ___init___ method

"""

class MyClass:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

"""

# What Is A Constructor In Python?

# A constructor in Python is a special method that is automatically called when a new instance (object) of a class is created. It is used to initialize the object's attributes and set up the initial state of the object. In Python, the constructor is defined by the __init__() method.