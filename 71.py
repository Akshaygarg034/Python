# ************************  dir, __dict__ and help method  ************************

# dir() is a powerful inbuilt function in Python3, which returns list of the attributes and methods of any object (say functions, modules, strings, lists, dictionaries etc.)

# __dict__ is a special attribute of a class which is a dictionary containing the class's namespace.

# help() method calls the built-in Python help system. It is used to display the documentation of modules, functions, classes, keywords etc.

# Example of dir, __dict__ and help method:

class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    
    def get_info(self):
        print(f"Name -> {self.name}, Age -> {self.age}")

p1 = Person("Akshay", "21")

arr = [1, 2, 3, 4, 5]

print(1, dir(arr), "\n")  # returns list of the attributes and methods of the list object
print(2, dir(p1), "\n")  # returns list of the attributes and methods of the Person object
print(3, p1.__dict__, "\n")  # returns dictionary containing the class's namespace
# print(4, help(p1), "\n")  # returns the documentation of the Person class
print(5, Person.__dict__, "\n")  # returns dictionary containing the class's namespace
