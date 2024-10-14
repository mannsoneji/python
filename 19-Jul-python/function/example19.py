# filter vowel list

l1 = ['a','e','r','t','o','u']

l2 = list(filter(lambda char : char in "aeiou",l1))

print(l2)