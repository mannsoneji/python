# Write a Python program to find the highest 3 values in a dictionary

d1 = {'a': 100,'b': 200,'c': 300,'d': 15,'e': 400}

highest_3 = sorted(d1.items(), key = lambda x : x[1],reverse = True)[:3]

print("Highest 3 values: ")
for key,value in highest_3:
    print(f"{key}: {value}")