# ***************************  Function Arguments in Python  ***************************

# There are four types of arguments that we can provide in a function:

# 1.    Default Arguments
def avg1(a, b=5):  # b is default argument here
    print(1, (a + b) / 2)

avg1(5)  # b is optional here


# 2.    Keyword Arguments
def avg2(a , b):
    print(2, (a + b) / 2)

avg2(b = 5, a = 4)  # order is not important here


# 3.    Variable length Arguments
    # 3.1.   Arbitrary Arguments:
def avg3_1(*numbers):   # tuple of numbers is created
    sum = 0
    for number in numbers:
        sum += number
    print(3.1, sum / len(numbers))

avg3_1(10, 15, 20)

    # 3.2.   Keyword Arbitrary Arguments:
def avg3_2(**numbers):   # dictionary of numbers is created
    print(numbers["name"], "is", numbers["age"], "year old and got", numbers["marks"], "marks")
        
avg3_2(name = "Akshay", age = "21", marks = 100)


# 4.   Required Arguments
def avg4(a, b=5):  # a is required argument here
    print(4, (a + b) / 2)

avg4(5)
