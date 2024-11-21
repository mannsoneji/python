# Write a Python program to find the second smallest number in a list.

l1 = [2,54,3,3,4,5,5,3,3,2,5,6,8]

unique_number = list(set(l1))

unique_number.sort()

second_smallest = unique_number[1]

print("Second Smallest Number is = ",second_smallest)