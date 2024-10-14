#accept string from user and check its palandrome or not

name = input("Enter  name = ")
rev_string = name[::-1]

if rev_string == name:
    print("its palandrome ....")
else:
    print("its not palandrom.....")