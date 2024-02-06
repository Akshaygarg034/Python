# ************************  Magic/Dunder Methods in Python  ************************


# Magic methods are the special methods which have double underscores at the beginning and end of their names. They are also known as Dunder methods. These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

# Some of the most commonly used magic methods in Python.

# __init__ method
# The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor", we have discussed this method already

# __str__ and __repr__ methods
# The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.
# __repr__ is basically made for making debugging easier. Ideally, it is used to get the string which on passed to eval() should return the object with the same value. If no __str__ method is defined then __repr__ method is used as fallback method.

# __len__ method
# The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.

# __call__ method
# The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.

# and many more...

# Example of magic methods:

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):  
        return f"Book({self.title}, {self.author}, {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __call__(self, val):
        print(f"You called the object {self.title} and the square of val is {val*val}")

b1 = Book("Python", "Akshay", 300)  # creating an object of Book class using __init__ method

print(1, b1)   #  calling the __str__ method

print(2, repr(b1))   #  calling the __repr__ method

print(3, len(b1))    #  calling the __len__ method

b1(5)  #  calling the __call__ method
