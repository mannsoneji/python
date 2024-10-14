#  Write a Python function that takes two lists and returns true if they have at least one common member.


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7]

has_common_member = False

for item in list1:
    if item in list2:
        has_common_member = True

print("Common Members = ", has_common_member)