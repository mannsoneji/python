"""
Function with parameters and function with return type
"""

def myfun(num1,num2):
    ans = num1 + num2 
    return ans


num1 = int(input("Enter a num1 : "))
num2 = int(input("Enter a num2 : "))

print(myfun(num1,num2))