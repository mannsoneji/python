# Write a Python script to sort (ascending and descending) a dictionary by value.


d1 = {"Banana": 20,"Apple": 10, "Watermelon" : 50,"Pineapple" : 30,"Orange" : 40}

ascending_dict = dict(sorted(d1.items(), key = lambda item: item[1]))

print("Dictionary in Ascending order : ",ascending_dict)


descending_dict = dict(sorted(d1.items(), key = lambda item: item[1], reverse=True))

print("Dictionary in Descending order : ",descending_dict)

