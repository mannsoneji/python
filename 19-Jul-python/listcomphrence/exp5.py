# without list comprehence

l1 = ['a','e','j','k','m']
vowel_list = ['a','e','i','o','u']

l2 = []

for c in l1:
    if c in vowel_list:
        l2.append(c)
print(l2)

# with list comprehence
l3 = [c for c in l1 if c in vowel_list]

print(l3)


l4 = [c for c in l1 if c in "aeiou"]

print(l4)

