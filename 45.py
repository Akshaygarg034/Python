# ***************************  __name__ == "__main__" in Python  ***************************

# If you import this in script file then even without calling welcome funciton here in the script, it will still run because when we import a module, python firstly run the imported module from top to bottom.

# So any funciton call will also be executed.

def welcome():
    print("Welcome to my module")
    print(__name__)


if(__name__ == "__main__"):   # __name__ is a special variable in python which is set to __main__ when we run the script directly from this file, otherwise gives this file name
    welcome()
