#  What is used to check whether an object o is an instance of class A?

class Perent:
    pass

class Child(Perent):
    pass

child = Child()

print(isinstance(child, Child))

print(isinstance(child,Perent))

