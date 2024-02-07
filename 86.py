# ************************  Walrus Operator in Python  ************************

# The walrus operator := is a new operator in Python 3.8 that allows you to assign values to variables as part of a larger expression.

# e.g.

# # Without walrus operator

# while True:
#     food = input("Enter food name: ")
#     if food == "exit":
#         break

# # With walrus operator

while((food := input("Enter food name: ")) != "exit"):
    pass
