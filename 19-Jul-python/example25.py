status = True
while status:
    name = input("Enter student name : ")


    choice = int(input("do you want to continue perss 1 for yes and press 2 for no :"))
    if choice == 1:
        status = True
    elif choice == 2:
        status = False
    else:
        print("Invalid input")