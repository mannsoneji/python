#accept 5 numbers from user and then find even odd
for i in range(1,6):
    num = int(input("Enter the number = ")) 
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")