# dictionary as a parameter 

def myFun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} - {v}")

myFun(name="Mann",subject= "Python",score=90)