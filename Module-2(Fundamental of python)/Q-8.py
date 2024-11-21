# Write a Python program to test whether a passed letter is a vowel or not.

char = input("Enter a character: ")
if char.lower() in 'aeiou':
    print(f"{char} is a vowel.")
elif char.upper() in 'AEIOU':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel")