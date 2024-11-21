# Write a Python function that checks whether a passed string is palindrome or not

def is_palindrome(s):
    return s == s[::-1]

str1 = input("Enter a string : ")

if is_palindrome(str1):
    print(f"{str1} is a pallindrome")

else:
    print(f"{str1} is a not a pallindrome")