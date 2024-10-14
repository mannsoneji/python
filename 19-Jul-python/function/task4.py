# with lambda function

l1 = [-12,23,-34,45,-56]
l2 = list(filter(lambda num : num>=0,l1))

print(l2)

# with normal function

l1 = [-12,23,-34,45,-56]

def findeven(num):
    if num>=0:
        return num

myfilterlist = list(filter(findeven,l1))
print(myfilterlist)