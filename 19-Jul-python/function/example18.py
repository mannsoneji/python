l1 = ["one", "two", "three","four"]

result_list = list(filter(lambda name : len(name)>= 4,l1))

print(result_list)