# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))

res = False

if num1==num2 or (num1 - num2) == 5 or (num1 + num2) == 5:
    res = True
    print(res)
else:
    print(res)