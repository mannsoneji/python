f  = open("manual.txt","a")

for i in range(1,4):
    name = input("Enter your name : ")
    age = str(int(input("Enter your age : ")))
    gender = input("Enter your gender : ")
    email = input("Enter your email : ")

f.write("name : "+name)
f.write("\n age : "+age)
f.write("\n gender : "+gender)
f.write("\n email : "+email)


f.close()