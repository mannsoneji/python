# Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.

str1 = input("Enter the name1 : ")
str2 = input("Enter the name2 : ")

# swapping first two characters both string

swap_str1 = str2[:2] + str1[2:]
swap_str2 = str1[:2] + str2[2:]

# combine both str after swapping 

combine = swap_str1 + " " + swap_str2
print(combine)