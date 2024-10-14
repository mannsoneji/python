sum = 0

status = True

while status:
    num = int(input("Enter the number = "))
    sum += num

    choice = input("do you want to continue perss y for yes and press n for no :").lower()  # .lower() makes lower case
    if choice == 'y' or choice == 'yes':
        status = True
    else:
        status = False

print("sum = ",sum)