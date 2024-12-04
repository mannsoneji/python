# Write a Python program that manipulates and prints strings using various string methods.

text = "Hello, Python Programming!"

# Convert the string to lowercase
lowercase_text = text.lower()
print("Lowercase:", lowercase_text)


# Convert the string to uppercase
uppercase_text = text.upper()
print("Uppercase:", uppercase_text)


# Capitalize the first letter of the string
capitalized_text = text.capitalize()
print("Capitalized:", capitalized_text)


# Replace 'Python' with 'Java'
replaced_text = text.replace("Python", "Java")
print("Replaced 'Python' with 'Java':", replaced_text)



# Check the string starts with 'Hello'
starts_with_hello = text.startswith('Hello')
print("Starts with 'Hello':", starts_with_hello)


# Check the string ends with 'Programming!'
ends_with_programming = text.endswith('Programming!')
print("Ends with 'Programming!':", ends_with_programming)


# Join a list of strings into single string
words = ['Mann', 'Soneji']
joined_text = ' '.join(words)
print("Joined text:", joined_text)


# Convert the string into list of characters
char_list = list(text)
print("List of characters:", char_list)


# Check string contains only letters
is_alpha = text.isalpha()
print("Is alphabetic:", is_alpha)

