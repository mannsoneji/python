f = open("theory.txt","a")


for i in range(1,4):
    name = input("Enter your name : ")
    subject = input("Enter your subject : ")

    f.write("\n name : "+name)
    f.write("\n subject : "+subject)
    f.write("\n ----------------------------------------------")

f.close()