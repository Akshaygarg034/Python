# ***************************  f strings  ***************************

name = "akshay"
country = "India"

# String formatting
letter = "My name is {} and I am from {}"
print(1, letter.format(name, country))

letter2 = "My name is {1} and I am from {0}"
print(2, letter2.format(name, country))

# F strings
letter3 = f"My name is {name} and I am from {country}"
print(3, letter3)

letter4 = f"My name is {{name}} and I am from {{country}}"
print(4, letter4)

price  = 49.3183213424
print(f"Price is {price:.2f}")
