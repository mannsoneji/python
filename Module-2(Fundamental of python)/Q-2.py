#Write a Python program to get the Factorial number of given number.

num = int(input("Enter the num : "))
print(num)
fact = 1

# if num == 0:
#     print("The factorial of 0 is 1")
for i in range(1, num + 1):
        fact *= i
    
print(f"The factotial of {num} is {fact}")
