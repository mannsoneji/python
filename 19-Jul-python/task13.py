#movie tickit 
price=0
discount=0
age= int(input("Enter the agae = "))
if age<=10 and age>=10:
    price=5
elif age>=12 and age<=18:
    price=7
elif age>=18 and age<=64:
    price=12
elif age>=65:
    price=7


day = input("Enter the day = ")
if day == "sun" or day == "sat":
    discount=10
else:
    print(price)

sum=price*discount/100
ans=price-sum

print(f"Base Price = ${ans}")