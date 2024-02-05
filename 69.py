# **************************  Class Methods in Python  **************************


# Class methods are the methods which are bound to the class and not the object of the class. They are used to change the class variables.

# Example of Class Methods:

class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    # cls is reference to the class itself even if we pass class object as cls it will still take reference of the class itself     
    @classmethod
    def change_count(cls, value):   # used to change the class variable
        cls.count += value 
        cls.newcount = value    # if cls.newcount is not a class variable, then it will create a new class variable with the name newcount

p1 =  Person("Akshay", "21")
p2 =  Person("Abhay", "19")

print(1, Person.count)

p2.change_count(2)

print(2, Person.count)
print(3, Person.newcount)
