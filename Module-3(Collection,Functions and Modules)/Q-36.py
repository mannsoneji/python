# How Do You Check The Presence Of A Key In A Dictionary? 

d1 = {'fname': 'mann','lname': 'soneji','age': 21,'city': 'ahmedabad'}

# using in keyword

if 'fname' in d1:
    print("Key exists")
else:
    print("Key doesnot exists")

# using .get() method 

if d1.get('age'):
    print("Key exists")
else:
    print("Key doesnot exists")

# using dict.keys() method

if 'lname' in d1.keys():
    print("Key exists")
else:
    print("Key does not exist")


# Using dict.__contains__() method 

if d1.__contains__('city'):
    print("Key exists")
else:
    print("Key does not exist")