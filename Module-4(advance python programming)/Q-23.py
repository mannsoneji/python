# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w 

l = int(input("Enter a length of rectangle : "))       
w = int(input("Enter a width of rectangle : "))   

rect1 = rectangle(l,w)

print("The area of rectangle is = ",rect1.area())