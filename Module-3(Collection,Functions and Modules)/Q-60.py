# Write a Python program to convert degree to radian

import math

def degree_to_radian(degree):
    radian = degree * (math.pi / 180)
    return radian

degree= float(input("Enter an angle in degree : "))

radian = degree_to_radian(degree)

print(f"{degree} degrees is equal to {radian} radians.")