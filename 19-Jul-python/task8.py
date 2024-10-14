#accept 5 numbers from user and then find even odd and calculate how many are even or odd
evensum=0
oddsum=0
for i in range(1,6):
    num = int(input("Enter the number = ")) 
    if num%2==0:
        evensum += 1
    else:
        oddsum += 1
        
print("Even sum =",evensum)
print("odd sum =",oddsum)