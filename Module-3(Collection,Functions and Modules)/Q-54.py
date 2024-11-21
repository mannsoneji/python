# How can you pick a random item from a list or tuple?

import random

# list random 


l1 = [1,2,3,4,5,6,7,8,9,10]

random_item1 = random.choice(l1)

print(f"Random from list is : {random_item1}")

# tuple random

t1 = (1,2,3,4,5,6,7,8,9,10)

random_item2 = random.choice(t1)

print(f"Random from tuple is : {random_item2}")