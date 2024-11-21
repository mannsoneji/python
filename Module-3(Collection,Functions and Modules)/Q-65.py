# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num, min_num


numbers = list(map(float, input("Enter decimal numbers separated by spaces: ").split()))

maximum, minimum = find_max_min(numbers)

print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")