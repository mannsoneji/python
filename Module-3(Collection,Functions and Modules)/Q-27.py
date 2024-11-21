# Write a Python program to find the repeated items of a tuple.

def repeated_items(t1):
    repeating_items = []
    for i in range(len(t1)):
        if t1[i] in t1[i+1:] and t1[i] not in repeating_items:
            repeating_items.append(t1[i])
    return repeating_items

# Example usage
t1 = (1,2,3,4,5,6,7,8,5,4,3,2,1)
repeating_items = repeated_items(t1)

print("Repeated items:", repeating_items)
