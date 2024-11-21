# Write a Python function to check whether a number is in a given range

def is_range(num, starting, ending):
    if starting <= num <= ending:
        return True
    else:
        return False

num = int(input("Enter a num : "))
starting = int(input("Enter a starting point : "))
ending = int(input("Enter a ending point : "))

print(is_range(num, starting, ending))