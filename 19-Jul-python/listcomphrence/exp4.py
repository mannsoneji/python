# without list comprehence

#que. filter even numbers from the list

l1 = [1,2,3,4,5,6,8]
l2 = []

for i in l1:
    if i%2 == 0:
        l2.append(i)

print(l2)

l1 = [1,2,3,4,5,6,8]
l3 = [i for i in l1 if i%2==0]

print(l3)