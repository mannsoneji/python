"""
Dictionary : which is contain key and value pair 
syntax  : 

dict = {
    'key' : 'value'
}

"""

d = {}

for i in range(1,6):
    key = input("Enter a key : ")
    value = input("Enter a value : ")

    d[key] = value
    
print(d)