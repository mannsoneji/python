#string methods


name = input("Enter name ")
print(name.capitalize()) #capital first word
print(name.casefold()) #lower simmiler
print(name.center(10,"&")) # it make the words total len as a user type 
print(name.find("m"))


s1 = "python programing"
s2="mann"
s3="mann21"
print(s1.find("on",1,9))

print(s1.index("o"))
print(s1.count("o"))

#check alphabtes 
print(s1.isalpha()) #false
print(s2.isalpha())  #true
print(s3.isalpha()) #false

print(s3.isalnum())  #true it check string contains both number amd alphabatess