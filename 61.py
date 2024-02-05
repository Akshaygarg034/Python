# **************************  Inheritance in Python  **************************

# Inheritance is a way of creating a new class for using details of an existing class and can add new features to it. This results in re-usability of code.

# Example of Inheritance:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print(f"Name -> {self.name}")
        print(f"Age -> {self.age}")

class Student(Person):
    def show_info(self):
        print("This is a student class")

s1 = Student("Akshay", "21")
s1.show_details()
s1.show_info()
