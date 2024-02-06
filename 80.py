# ************************  Multilevel Inheritance in Python  ************************

# Multilevel Inheritance : When a class inherits from a class which is already inherited from another class. or we can also say that when there are many levels of inheritance.

# e.g.

class A:
    def feature(self):
        print("Feature 1 is working")

class B(A):
    def feature(self):
        print("Feature 2 is working")

class C(B):
    def feature(self):
        print("Feature 3 is working")

c1 = C()
c1.feature() 
print(C.mro()) # Method resolution order of class C ()
