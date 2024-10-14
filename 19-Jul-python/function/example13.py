l1 = [23,22,34,54,67]

def checkEvenandOdd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
    
ans = list(map(checkEvenandOdd,l1))
print(ans)