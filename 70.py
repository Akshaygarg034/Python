# ************************  Class Methods as Alternative Constructors  ************************

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    # cls is reference to the class itself even if we pass class object as cls it will still take reference of the class itself
    def from_str(cls, string):
        name, age = string.split(",")
        return cls(name, age)
    
string = "Akshay,21"
p1 = Person.from_str(string)  # this class method acts as a alternative constructor
print(p1.name, p1.age)
