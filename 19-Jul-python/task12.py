# accept 5 subjects from user and check no. of group wise 
i=1 
java=0
flutter=0
react=0
while i<=5:
    subname = input("Enter the subject name = ")

    if subname == "java":
        java+=1
    elif subname == "react":
        react+=1
    elif subname == "flutter":
        flutter+=1

    i+=1
print(f"java = {java}")
print(f"react = {react}")
print(f"flutter = {flutter}")


