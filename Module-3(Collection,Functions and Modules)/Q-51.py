# Write a Python function to check whether a number is perfect or not

num = int(input("Enter a num : "))

sum_divisor = 0

for i in range(1, num):
    if num % i == 0: 
        sum_divisor += i

if sum_divisor == num:
    print(f"{num} is perfect")

else:
    print(f"{num} is not perfect")