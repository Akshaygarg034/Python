# ***************************  Local vs Global Variables in Python  ***************************

# Local variable -> Which is declared inside a function and has a local scope
# Global variable -> Which is declared outside a function and has a global scope

x = 5     # global variable

def func():
    global x     # to modify the global variable inside the function
    y = 6     # local variable
    print("y", y)
    print("before x", x)
    x = 10
    print("after x", x)

func()

print("outside x", x)
