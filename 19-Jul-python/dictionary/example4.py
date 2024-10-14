# dynamic dictionary

m = {}

status =  True

while status:
    key = input("Enter a key : ")
    value = input("Enter a value : ")

    m[key] = value

    choice = int(input("do you want to add more data : press 1 for yes and press 2 for no"))
    if choice == 1:
        status =True
    else:
        status = False

print(m)