#enter four numbers from muser and check they are positive or negative

i=1
while i<=4:
    num = int(input("Enter your number = "))
    print(num)

    if num>=0:
        print("number is positive")
    else:
        print("number is negative")
    i+=1