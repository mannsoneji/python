# When will the else part of try-except-else be executed?

# The else block in a try-except-else statement is executed only if no exception is raised in try block

# If an exceptions raised in try block the code in else block will be skipped 

# example of else 

try:
    x = 10 / 2 
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("No exception occurred. The result is:", x)