# Write a Python program to append text to a file and display the text.

with open('example.txt', 'a') as file:
    file.write("\nThis is a new line appended to the file.")
    file.write("\nAppending is easy in Python!")

with open('example.txt', 'r') as file:
    content = file.read()

print(content)