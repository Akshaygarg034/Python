# **************************  Lambda functions in Python  **************************

# They are small anonymous functions which are defined using lambda keyword
# They are temporary functions and are used where we require a nameless function for a short period of time
# They can take any number of arguments but can only have one expression


# Syntax:
lambda x : x + 10

# The above lambda function is equivalent to:
def add(x):
    return x + 10


# Example
def exec(func, val):
    res = func(val)
    print(res)

exec(lambda x: x*2, 5)
