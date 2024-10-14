# Differentiate between append () and extend () methods?


#The main difference between the append() and extend() methods is 
#append() adds a single item to the end of a list, 
#while extend() adds multiple items from an iterable to the end of a list

# Append()

l1 = [1, 2, 3]
l1.append(4)
print(l1) 

# Extend()

l2 = [1, 2, 3]
l2.extend([4, 5])
print(l2) 

l2.extend('abc')
print(l2)



