# ************************  Generators in Python  ************************


# A generator function in Python is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a Python generator function. 

# Generators are a great way to produce data that is too large to fit in memory. They generate values on the fly and do not store all the values in memory, unlike lists or tuples. This makes them very memory efficient.

# Example:

def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator
gen = simple_generator()   # returns a iterable object

print(next(gen))   # when this is called, the generator starts executing the code until it reaches the first yield expression, which returns the value 1. The state of the generator function is saved right after the yield expression.

print(next(gen))   # when this is called, the generator resumes execution right after the last yield expression and continues until it reaches the next yield expression. This time, the value 2 is returned.

print(next(gen), "\n")   # similarly returns 3

# print(next(gen))   # StopIteration error is raised as there are no more values to be returned

### The generator object can be iterated through using a for loop.

# for value in gen:  # for loop will not execute as the generator has already been exhausted
#     print(value)

for value in simple_generator():
    print(value)
