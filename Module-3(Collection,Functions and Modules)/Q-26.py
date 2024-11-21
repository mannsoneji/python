# Write a Python program to replace last value of tuples in a list.

l1 = [(1,2,3,4)]

new_val = 10

new_l1 = [t[:-1] + (new_val,) for t in l1]
print("replaces values : ",new_l1)