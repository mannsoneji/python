"""
arguments : tuple as a paramenter :
"""

#without tuple - without args

def myFun(a,b,c):
    print(a)
    print(b)
    print(c)

myFun(10,20,30)

# with args:

def myFun2(*args):
    print(args)

myFun2(10,20,12,23,12,33,4,56,8)