# How Do You Traverse Through A Dictionary Object In Python?

# in python you can traverse (iterate) through a dictionary object using several methods.

# dictionary is an unordered collection of key-values pairs and there are different ways to acess  and iterate on key-values pair or keys and values

# traverse == itreate 

d1 = {'a': 1, 'b': 2, 'c': 3}

# Traverse through dictionary keys

for key in d1:
    print(f"Key: {key}")

# Iterating through values: 

for value in d1.values():
    print(f"Value: {value}")


# Iterating through key-value pairs: 

for key, value in d1.items():
    print(f"Key: {key}, Value: {value}")

# List comprehensions:

even_keys = [key for key, value in d1.items() if value % 2 == 0]
print(even_keys)

# Using map():

modified_values = dict(map(lambda item: (item[0], item[1] * 2), d1.items()))
print(modified_values)




