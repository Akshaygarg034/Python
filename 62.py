# **************************  Access Modifiers in Python  **************************

# Access Modifiers are used to restrict the access of the attributes and methods of a class. There are three types of access modifiers in Python:

# 1. Public Access Modifier: The members of a class that are declared public are easily accessible from any part of the program. All the methods and attributes of a class are public by default.

# 2. Protected Access Modifier: The members of a class that are declared protected are only accessible to a class derived from it. Data members of a class are declared protected by adding a single underscore before the data member of that class. (e.g   _name)

# 3. Private Access Modifier: The members of a class that are declared private are only accessible within the class. Data members of a class are declared private by adding a double underscore before the data member of that class. (e.g   __name)

# Example of Access Modifiers:

class Person:
    def __init__(self, name, age, roll_no):
        self._name = name       # Protected attribute
        self.__age = age       # Private attribute, python do name mangling to access this attribute (changes its name to _Person__age)
        self.roll_no = roll_no  # public attribute
    
    def show_name(self):
        print(f"Name -> {self._name}")
    
    def show_age(self):
        print(f"Age -> {self.__age}")

class Student(Person):
    def show_info(self):
        print("This is a student class")

s1 = Student("Akshay", "21", "59")
print(s1.__dir__())
print(s1.roll_no)
print(s1._name)
print(s1._Person__age)

# Python doesn't enforce these access modifiers, it is just a convention. We can still access the private and protected attributes of a class from outside the class.
# and even both public and private attributes can be accessed in same way, but still it is up to programmer to respect these conventions on not.
