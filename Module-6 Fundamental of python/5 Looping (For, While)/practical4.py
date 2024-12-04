"""
Practical Example 4: Print this pattern using nested for loop:
markdown
Copy code
*
**
***
****
*****

"""

n = int(input("Enter a num = "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ") 

    print()