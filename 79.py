# ************************  Multiple Inheritance in Python  ************************


# Multiple Inheritance : When a class inherits from more than one parent classes.

# Method Resolution Order (MRO) in Python is the order in which the base classes are searched when looking for a method.

# example:

class A:
    def show(self):
        print("Show of A")

class B:
    def show(self):
        print("Show of B")

class C(A, B):
    pass

c1 = C()
c1.show() # it will call the show method of class A because class A is inherited first.

print(C.mro()) # Method resolution order of class C ()


