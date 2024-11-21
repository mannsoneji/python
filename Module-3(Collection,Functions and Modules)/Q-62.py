# Write a Python program to calculate the area of a parallelogram

def area_of_parallelogram(b,h):
    return b * h 

b = float(input("Enter the length of the base : "))
h = float(input("Enter the height of the parallelogram : "))

area = area_of_parallelogram(b,h)

print(f"The area of the parallelogram is: {area} square units.")
