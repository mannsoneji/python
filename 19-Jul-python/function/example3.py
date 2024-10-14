def addition():
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    ans = num1 + num2 
    print(ans)

addition()

def substraction():
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    ans = num1 + num2 
    print(ans)

substraction()

def division():
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    ans = num1 + num2 
    print(ans)

division()

def multipication():
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    ans = num1 + num2 
    print(ans)

multipication()


status = True 
menu = """
        press 1 for addition
        press 2 for substaction 
        press 3 for division
        press 4 for multipication

"""


while status:
    print(menu)
    choice = int(input("Enter the choice : "))
    if choice == 1:
        addition()
    elif choice == 2:
        substraction()
    elif choice == 1:
        division()
    elif choice == 1:
        multipication()

    user_exit = input("do you want to perform more opration : press y for yes and n for no").lower()
    if user_exit == 'y':
        status = True
    else:
        status = False
