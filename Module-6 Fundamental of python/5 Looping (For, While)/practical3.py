# Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

list1 = ['apple', 'banana', 'mango']

str1 = 'banana'

for fruit in list1:
    if fruit == str1:
        print(f"The {str1} is in a list")
        break

if str1 not in list1:
    print(f"The {str1} is not in a list")