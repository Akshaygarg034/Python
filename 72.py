# ************************  super keyword in Python  ************************

# super() is used to call the methods of the parent class. It returns a temporary object of the superclass which allows us to call the methods of the superclass.

# Example of super keyword:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        print(f"I am a parent class having name -> {self.name} and age -> {self.age}")

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language
    
    def get_info(self):
        print(f"I am a child class and I am a programmer having name -> {self.name}, age -> {self.age} and I know {self.language}")

p1 = Programmer("Akshay", "21", "Python")
p1.get_info()   #  by default it will call the child class method 
super(Programmer, p1).get_info()  # calling the parent class method using super() method
