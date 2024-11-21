# Write a Python program to calculate surface volume and area of a cylinder

import math

def surface_area(r,h):
    return 2 * math.pi * r * (r + h)

def volume_area(r,h):
    return math.pi * (r ** 2) * h


r = float(input("Enter the radius of the base of the cylinder: "))

h = float(input("Enter the height of the cylinder: "))

surface = surface_area(r,h)
volume = volume_area(r,h)

print(f"The surface area of the cylinder is: {surface :.2f} square units.")
print(f"The volume of the cylinder is: {volume :.2f} cubic units.")