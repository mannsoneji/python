# Write a Python program to check multiple keys exists in a dictionary

d1 = {'fname': 'mann','lname': 'soneji','age': 21,'city': 'ahmedabad'}

checking_keys = ['fname','lname','age']

if all(key in d1 for key in checking_keys):
    print("All the keys are exists in dictionary")

else:
    print("some of the keys are not exists in dictionary")

    
    