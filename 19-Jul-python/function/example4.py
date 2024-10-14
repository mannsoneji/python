#factorial values 

# accept value from user and find it factorial value

def findfact(num):
    f=1
    for i in range(1,num+1):
        f*=i
    print(f)

num = int(input("Enter a number : "))
findfact(num)