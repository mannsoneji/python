# Write a Python program to unzip a list of tuples into individual lists.

def unzip_tup(t1):
    return list(zip(*t1))

t1 = [(1, 2, 3),(4, 5, 6),(7, 8, 9),(10,11,12)]
result = unzip_tup(t1)

print("Unziped lists : ",result)
