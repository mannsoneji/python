# Write a Python program to write a list to a file.

def list_to_file(file_name,data_list):
    with open(file_name, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

data_list = ['Mann', 'Darshan', 'Taha', 'Kunj']

file_name = 'Q-11.txt'

list_to_file(file_name, data_list)

print(f"List to file {file_name}")
