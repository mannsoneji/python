# Write python program that swap two number with temp variable and without temp variable

# Swap two numbers with temp varialble

num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))

temp = num1
num1 = num2 
num2 = temp

print("After Swapping wth temp : ",num1,num2)

# swap two numbers without temp variables 

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping without temp : ", num1, num2)