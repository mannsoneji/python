# Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

def addition(a,b):
    return a + b

l1 = [1,2,3,4,5,6,7,8,9,10]

product = reduce(addition,l1)

print(product)
