# Write a Python program to read last n lines of a file.

from collections import deque

def read_last_line(file_name, n):
    with open(file_name , 'r') as file:
        lines = deque(file, maxlen=n)
    return list(lines)

file_name = 'example.txt'
n = int(input("Enter a num to read line : "))

last_n_line = read_last_line(file_name,n)


for line in last_n_line:
    print(line,end=' ')