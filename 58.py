# **************************  Constructors in Python  **************************


# Constructors are special methods which are automatically called when an object of a class is created. They are used to initialize the object's state.

# Types of Constructors:
# 1. Default Constructor: It has no parameters.
# 2. Parameterized Constructor: It has parameters.
# 3. Copy Constructor: It is used to copy the values of one object to another object.

# Example of Default Constructor:
class Student:
    def __init__(self):
        print("This is default constructor")

s1 = Student()

# Example of Parameterized Constructor:
class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"This is parameterized constructor with name {self.name} and age {self.age}")

s2 = Student2("Akshay", 21)

# Example of Copy Constructor:
class Student3:
    def __init__(self, obj):
        self.name = obj.name
        self.age = obj.age
        print(f"This is copy constructor with name {self.name} and age {self.age}")

s3 = Student3(s2)
