# without list comprehance

l1 = []
for i in range(1,6):
    l1.append(i*2)
print(l1)


l1 = [i*2 for i in range(1,8)]
print(l1)