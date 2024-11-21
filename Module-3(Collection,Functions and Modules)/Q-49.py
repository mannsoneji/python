# Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(n):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

n = int(input("Enter a positive number : "))
fact = factorial(n)

print(f"Factorial of {n} is :", fact)