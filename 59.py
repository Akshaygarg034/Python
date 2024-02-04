# **************************  Decorators in Python  **************************

# Decorators are used to modify the behaviour of a function or a class. It takes a function or a class as an argument and returns a new function or a class. It is used to add some extra functionality to the existing function or a class.


# Example 1


def greet(func):
    def inner(*args, **kwargs):     # To accept any number of arguments
        print("Hello Everyone!")
        func(*args, **kwargs)
        print("Thanks for using this function")
    return inner

@greet
def add(a , b):
    print(a + b)

add(2 , 3)
