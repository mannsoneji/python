#accept name and password from user and chekc its validation

name = input("Enter your name : ")

if len(name) < 4:
    print("Enter 4 characters in name ")
elif name != name.isalpha():
    print("you have to use only aphabates")
else:
    print("Name : ",name)
password = input("Enter your password : ")
if len(password) < 8:
    print("Enter atleast 8 characters in password ")
elif password != password.isalnum():
    print("you have to use both alphabates and number")
else:
    print("Password : ",password)
