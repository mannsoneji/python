# Write a Python program to remove an empty tuple(s) from a list of tuples


def remove_empty_tuple(t1):
    return [tup for tup in t1 if tup]

t1 = [(),(1,2),(),(3,4),(),(5,6),(),(7,8),(),(9,10)]

result = remove_empty_tuple(t1)

print("Removed empty tuples : ",result)