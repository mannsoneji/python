# Practical Example 6: Write a Python program to check if a number is prime using if_else

n = int(input("Enter a num : "))

flag = 0

for i in range(1 , n):
    if n % i == 0:
        flag = 1
        break
    else:
        flag = 0

if flag == 0:
    print("Num is prime") 
else:
    print("Num is not a prime ")