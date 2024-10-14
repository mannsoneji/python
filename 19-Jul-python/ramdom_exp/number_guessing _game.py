# import random

# status = True

# computer = random.randint(1,100) # it will generate randome number between 1 - 100


# while status:
#     user_choice = int(input("Enter your choice : "))
#     if user_choice > computer:
#         print("Hint : Guess Lower Number")
#     elif user_choice < computer:
#         print("Hint : Guess Upper Number")
#     else:
#         print("right answer")
#         status=False



import random

status = True
trials = 0
max_trials = 5

computer = random.randint(1, 100)  # Generate a random number between 1 and 100

while status and trials < max_trials:
        user_choice = int(input("Enter your choice : "))
        trials += 1
        
        if user_choice > computer:
            print("Hint: Guess Lower Number")
        elif user_choice < computer:
            print("Hint: Guess Higher Number")
        else:
            print("Right Answer")
            status = False

if status:
    print(f"Sorry, you've used all {max_trials} trials. The correct number was {computer}.")

