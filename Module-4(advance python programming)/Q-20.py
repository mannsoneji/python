# Write python program that user to enter only odd numbers, else will raise an exception

def get_odd_number():
    while True:
        try:
            user_input = input("Enter an odd number: ")

            number = int(user_input)

            if number % 2 != 1:
                raise ValueError("The number is not odd!")
            
            return number

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")

odd_number = get_odd_number()
print(f"You entered a valid odd number: {odd_number}")
