# change elements from the tuple

t = ("c","c++","java","python")
print(t)

# convert tuple into list

l = list(t)

l.remove("java")

# convert list into tuple

t = tuple(l)
print(t)