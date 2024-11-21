# How can you pick a random item from a range?

import random

r1 = range(1,100)

random_item = random.choice(list(r1))

print(f"Random item from the range: {random_item}")