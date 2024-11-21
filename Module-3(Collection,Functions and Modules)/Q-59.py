# Write a Python program to read a random line from a file.

import random

def read_random(filename):
    with open(filename , 'r' ) as file:
        lines = file.readlines()

    if lines:
        return random.choice(lines).strip()
    else:
        return "The file is empty"
    
filename = input("Enter a file  name : ")
random_line  = read_random(filename)
print("random line from file is : ",random_line)