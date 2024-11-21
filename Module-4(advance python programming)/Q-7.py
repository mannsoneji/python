# Write a Python program to read a file line by line store it into a variable.

def file_to_variable(file_name):
    content = ""
    with open(file_name, 'r') as file:
        for line in file:
            content += line
    return content

file_name = 'example.txt'

content = file_to_variable(file_name)
print(content)
