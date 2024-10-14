menu = {
    'Pizza' : 80,
    'Pasta' : 100,
    'Burger' : 70,
    'Sandwich' : 90,
    'Coffee' : 60
}

print("Welcom to PYTHON Restaurant")
print("Menu : ")
for item, price in menu.items():
    print(f"{item} : Rs.{price}")


order_total = 0


while True:
    item = input("Enter the Item you want to order: ").capitalize()
    if item in menu:
        quantity = int(input(f"How many {item} would you like to order? :  "))

        if quantity > 0:
            order_total += menu[item] * quantity
            print(f"{quantity} {item} has been added to your order")
        else:
            print("Enter a quantity Greater then 0")

    else:
        print(f"The {item} is not available at our Restaurant")

    another_order = input("Do you want to add another item ? (yes or no)").lower()
    if another_order != 'yes':
        break

print(f"The total amount is to pay is Rs.{order_total}")