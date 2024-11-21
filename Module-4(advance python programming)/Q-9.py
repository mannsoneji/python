# Write a Python program to count the number of lines in a text file.

def count_lines(file_name):
    with open(file_name, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

file_name = 'example.txt'

num_lines = count_lines(file_name)

print(num_lines)