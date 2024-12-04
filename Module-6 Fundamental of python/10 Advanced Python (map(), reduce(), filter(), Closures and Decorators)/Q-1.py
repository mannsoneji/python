# Write a Python program to apply the map() function to square a list of numbers.

def square(n):
    return n * n

l1 = [1,2,3,4,5,6,7,8,9,10]

squared = list(map(square,l1))

print(squared)
