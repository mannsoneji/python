import random

computer = random.randint(1,100)

status = True

while status:
    user = int(input("Enter your choice : "))

    if user > computer:
        print("Hint : Guess Lower Number")
    elif user < computer:
        print("Hint : Guess upper Number")
    else:
        print("Right guess")
        status = False