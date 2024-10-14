# find a length of string without using len function 

def lenFun(str):
    count = 0
    for s in str:
        count+=1
    return count

str = input("Enter a string : ")

print(lenFun(str))
