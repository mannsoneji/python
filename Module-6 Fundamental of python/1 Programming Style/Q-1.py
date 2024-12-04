# Write a Python program that demonstrates the correct use of indentation, comments, and variables following PEP 8 guidelines.


# Initialize numbers

num1 = int(input("Enter a number 1 :- "))
num2 = int(input("Enter a number 2 :- "))

# This code perform addition on num1 and num2 that taken by user

addition = num1 + num2
print(f"The Addition of {num1} and {num2} is {addition}")

# This code perform subtraction on num1 and num2 that taken by user

subtraction = num1 - num2
print(f"The subtraction between {num1} and {num2} is {subtraction}")

# This code perform Multiplication on num1 and num2 that taken by user

multiplication = num1 * num2
print(f"The Multiplication of {num1} and {num2} is {multiplication}")

# This code perform Division on num1 and num2 that taken by user

if num2 != 0:
    division = num1 / num2
    print(f"The Division of {num1} and {num2} is {division}")
else:
    print("Cannot divide by zero!")