# **************************  Classes and Objects in Python  **************************

# Class: A blueprint for creating objects. It is a logical entity that has some attributes and methods.
# Object: An instance of a class. It is a physical entity that has some attributes and methods.

class Person:
    name = "Some name"
    place = "Some place"

    def info(self):
        print(f"Name: {self.name}, Place: {self.place}")

p1 = Person()
p1.name = "Akshay"
p1.place = "Himachal Pradesh"

p2 = Person()
p2.name = "Akshay2"
p2.place = "Gurugram"

p1.info()
p2.info()
