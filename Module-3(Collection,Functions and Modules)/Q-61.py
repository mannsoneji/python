# Write a Python program to calculate the area of a trapezoid

def area_of_trapezoid(b1, b2 ,h):
    return 0.5 * (b1 + b2) * h

b1 = float(input("Enter the length of the first base b1: "))
b2 = float(input("Enter the length of the second base b2: "))
h = float(input("Enter the height h: "))

area = area_of_trapezoid(b1,b2,h)

print(f"The area of the trapezoid is: {area} square units.")