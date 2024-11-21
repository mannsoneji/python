# What is Instantiation in terms of OOP terminology ?

# Instantiation is the process of creating an instance of a class. In object-oriented programming (OOP), classes are blueprints or templates, and objects are instances of those classes. When you create an object from a class, you're instantiating the class.

# Class: A blueprint or template for creating objects.

# Object: An instance of the class.

class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        return f"Bike : {self.brand} {self.model}"

my_bike = Bike("Kawasaki", "H2R")

print(my_bike.display_details())