# **************************  Getters and Setters in Python  **************************

# Getters and Setters are used to get and set the values of the attributes of a class. They are used to protect the data from direct access. They are also known as accessors and mutators.


# Example of Getters and Setters:

class Person:
    def __init__(self, age):
        self.age = age

    @property                  # Getter 
    def ageFunc(self):
        return self.age
    
    @ageFunc.setter            # Setter
    def ageFunc(self, value):
        self.age = value

    def show(self):
        print(f"Age -> {self.age}")

p1 = Person(21)

print("getter", p1.ageFunc)
p1.ageFunc = 22
print("setter", p1.ageFunc)

# We can set different names for getter and setter functions but it is not a good practice. We should use the same name for both getter and setter functions to avoid any confusion.
