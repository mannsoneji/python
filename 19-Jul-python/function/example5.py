"""
Fibbonaci series :

0  1

Enter a number : 5

0 1 1 2 3 

"""
# without function

# f = 1
# s = 1

# n=int(input("Enter a Number : "))
# print(f"{f}  {s}",end="  " )
# for i in range(2,n):
#     t = f + s
#     print(t,end=" ")
#     f , s = s, t


# with function


def findfibbo(n):
    f = 0
    s = 1
    print(f"{f}  {s}",end="  " )
    for i in range(2,n):
        t = f + s
        print(t,end=" ")
        f , s = s, t

n = int(input("Enter a Number : "))
findfibbo(n)