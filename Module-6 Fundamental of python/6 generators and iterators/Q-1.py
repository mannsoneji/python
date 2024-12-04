# Write a generator function that generates the first 10 even numbers.

def even_nums():
    num = 0
    for num in range(0,20,2):
        yield num

for even_num in even_nums():
    print(even_num)
