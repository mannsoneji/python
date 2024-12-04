# Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.


age = int(input("Enter your age :- "))
weight = int(input("Enter your age :- "))

if age>=18 or age<= 65:
    print("according to your age You are eligable to donate blood")
    if weight>= 50:
        print(" according to you are weight You are eligable to donate blood")
    else:
        print(" according to you are weight You are not eligable to donate blood")

else:
    print("according to your age You are not eligable to donate blood")


