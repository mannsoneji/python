"""
string :- strinng is a biggest datatype in any programming language string is denoted by single ' and double quotes " 
"""

# len - length is an inbuilt function to find string length
name = input("Enter your name : ")
# print(len(name))


# find string length without using len

count = 0
for i in name:
    count+=1
print(count)