#Write a Python function to insert a string in the middle of a string.

original_string = input("Enter the original string: ")
insert_string = input(" Enter the string to insert at the middle: ")


middle_index = len(original_string) // 2


result = original_string[:middle_index] + insert_string + original_string[middle_index:]


print("Result:", result)