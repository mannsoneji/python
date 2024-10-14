menu = """
                    jay Bhavani 

                    menu

                    vadapav : 30
                    dabeli : 25
                    bhel: 70

"""

menu_card = {
    "vadapav" : 30,
    "dabeli" : 25,
    "bhel" : 70

}
print(menu)

cart= {}
"""
        {

                "vadapav" : 
                    {
                        "qty" : 2,
                        "price" : 60
                    }
        }
"""

status = True

while status:
    sub_dictionary = {}
    item_name = input("Enter item here : ")
    qty = int(input("Enter qty"))
    price = menu_card[item_name]

    if item_name or cart:
        cart[item_name][qty] = cart[item_name]["qty"] + qty
        cart[item_name][qty] = cart[item_name]["qty"] * price
    else:
        sub_dictionary["qty"] = qty
        sub_dictionary["price"] = qty * price
    
        cart[item_name] = sub_dictionary
    print(cart)

