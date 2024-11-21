# Write a Python script to check if a given key already exists in a dictionary.


def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
    

d1 = {
        'fname': 'Mann', 
        'age': 21,
        'city': 'Ahmedabad'
}

key_check = 'city'

if check_key(d1,key_check):
    print(f"Key '{key_check}' exists in the dictionary.")
else:
    print(f"Key '{key_check}' does not exist in the dictionary.")



