# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output: ac ad bc bd

import itertools

data = {'1': ['a','b'],
       '2': ['c','d']
}

val_of_list = data.values()

combinations = itertools.product(*val_of_list)

for combination in combinations:
    print(''.join(combination))






