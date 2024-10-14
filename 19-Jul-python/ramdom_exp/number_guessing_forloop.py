import random

status = True

computer = random.randint(1,100) # it will generate randome number between 1 - 100


for i in range(1,6):
    user_choice = int(input("Enter your choice : "))
    if user_choice > computer:
        print("Hint : Guess Lower Number")
    elif user_choice < computer:
        print("Hint : Guess Upper Number")
    else:
        print("right answer")
        break
else:
    print("Game over")
