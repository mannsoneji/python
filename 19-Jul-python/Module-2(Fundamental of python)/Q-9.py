# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))
num3 = int(input("Enter the num3 : "))
sum=0
if num1 == num2 or num2 == num3 or num3 == num1:
    print("sum is zero")
else:
    sum = num1 + num2 + num3
    print(sum)