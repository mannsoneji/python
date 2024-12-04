# Write a Python program that uses a custom iterator to iterate over a list of integers.

def custom_iterator(data):
    for item in data:
        yield item

data_list = [1,2,3,4,5,6,7,8,9,10]

for num in custom_iterator(data_list):
    print(num)