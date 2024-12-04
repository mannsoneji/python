# Write a Python program that filters out even numbers using the filter() function

l1 = [1,2,3,4,5,6,7,8,9,10]

even_nums = list(filter(lambda x : x % 2 == 0,l1))
odd_nums = list(filter(lambda x : x % 2 != 0,l1))

print("even_nums =",even_nums)
print("odd_nums =",odd_nums)
