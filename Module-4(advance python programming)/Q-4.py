# Write a Python program to read first n lines of a file

def read_n_lines(file_name, n):
    with open('example.txt', 'r') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line, end=" ")

n = int(input("Enter a num to read line : "))
file_name = 'example.txt'
read_n_lines(file_name,n)