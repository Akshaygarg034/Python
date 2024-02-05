# **************************  Static Methods in Python  **************************


# Static methods are the methods which are bound to the class and not the object of the class. They do not require a class instance creation. So, they are not dependent on the state of the object.

# Example of Static Methods:

class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    @staticmethod   
    def show_count(): # Don't need self parameter, as they don't deal with instance of the class
        print(f"Total number of persons created -> {Person.count}")

p1 = Person("Akshay", "21")
p1.show_count()

p2 = Person("Abhay", "19")
Person.show_count()     # Can also be called using class name
