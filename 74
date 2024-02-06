# ************************  Method Overriding in Python  ************************

# Method overriding is a concept of object-oriented programming that allows us to change the implementation of a method in the child class that is defined in the parent class. It is used to change the behaviour of the method in the child class.

# Example of method overriding:

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):   # area method gets override by child class Circle
        return 3.14 * self.radius * self.radius
    
s1 = Circle(10, 20, 5)
print(s1.area())  # 78.5
print(super(Circle, s1).area()) # 200
