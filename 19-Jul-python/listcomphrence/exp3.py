# without list comprehance

l1 = [2,3,4,5,6,5,3,]
l2 = []
for i in l1:
    l2.append(i*2)
print(l1)

l1 = [1,2,3,4,5,67,7]
l2 = [i*2 for i in l1]
print(l2)