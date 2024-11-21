# Write a Python program to read a file line by line and store it into a list

def file_to_list(file_name):
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines


file_name = 'example.txt'

lines = file_to_list(file_name)

for line in lines:
    print(line)