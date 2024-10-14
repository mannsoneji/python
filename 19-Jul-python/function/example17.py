# without filter function

"""
l1 = [12,23,34,45,56]

l2 = []

for i in l1:
    if i%2==0
        l2.append(i)

        
print(l2)
"""

# with filter function

l1 = [12,23,34,45,56]

def findeven(num):
    if num%2==0:
        return num

myfilterlist = list(filter(findeven,l1))
print(myfilterlist)


# short trick 


l1 = [12,23,34,45,56]
l2 = list(filter(lambda num : num%2==0,l1))

print(l2)