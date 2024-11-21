# Write a Python program to copy the contents of a file to another file.

def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        with open(destination_path, 'w') as dest_file:
            dest_file.write(source_file.read())

source_path = 'source.txt'
destination_path = 'destination.txt' 

copy_file(source_path, destination_path)

print(f"Contents of {source_path} have been copied to {destination_path}")