# Write a Python script to concatenate following dictionaries to create a new one.

# there are three method to concete dictonaries 

# 1. update method

d1 = {'a': 1,'b': 2,'c': 3}
d2 = {'d': 4,'e': 5, 'f': 6}
d3 = {'g': 7,'h': 8,'i': 9}

concate_d1 = d1.copy()
concate_d1.update(d2)
concate_d1.update(d3)

print("Concate Dictionaries using update method :",concate_d1)


# 2. using operator

concate_d2 = d1 | d2 | d3

print("Concate Dictionaries using | operator :",concate_d2)

# 3. using unpacking

concate_d3 = {**d1,**d2,**d3}
print("Concatenated Dictionaries using unpacking :",concate_d3)

