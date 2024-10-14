#How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?


# --------> ANS

# The Pop() method is use to remove last object from a list.

l1 = [1,2,3,4,5]
l1.pop()
print(l1)

# what is list1 [-1]?

list1 = [2, 33, 222, 14, 25]
list1 = list1[:-1]
print(list1)