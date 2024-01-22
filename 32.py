# ***************************  Set Methods  ***************************

# I. union() and update():

city1 = {"Delhi", "Mumbai", "Gurugram", "Noida"}
city2 = {"Chandigarh", "Mumbai", "Gurugram", "Noida", "Pune", "Chennai"}

city3 = city1.union(city2)
print(1, city3)

city1.update(city2)
print(2, city1)

# II. intersection and intersection_update():

city4 = {"Delhi", "Mumbai", "Gurugram", "Noida"}
city5 = {"Chandigarh", "Mumbai", "Gurugram", "Noida", "Pune", "Chennai"}

city6 = city4.intersection(city5)
print(3, city6)

city4.intersection_update(city5)
print(4, city4)

# III. symmetric_difference and symmetric_difference_update():     (A U B) - (A intersection B)

city7 = {"Delhi", "Mumbai", "Gurugram", "Noida"}
city8 = {"Chandigarh", "Mumbai", "Gurugram", "Noida", "Pune", "Chennai"}

city9 = city7.symmetric_difference(city8)
print(5, city9)

city7.symmetric_difference_update(city8)
print(6, city7)

# IV. difference() and difference_update():

city10 = {"Delhi", "Mumbai", "Gurugram", "Noida"}
city11 =  {"Chandigarh", "Mumbai", "Gurugram", "Noida", "Pune", "Chennai"}

city12 = city10.difference(city11)
print(7, city12)

city10.difference_update(city11)
print(8, city10)

city13 =  {"Chandigarh", "Mumbai", "Gurugram", "Noida", "Pune", "Chennai"}
city14 = {"Mumbai", "Gurugram", "Noida"}

print(9, city13.isdisjoint(city14))
print(10, city13.issuperset(city14))
print(11, city14.issubset(city13))

city13.add("Goa")
print(12, city13)

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

city13.remove("Goa")
print(13, city13)

city13.discard("Chandigarh")
print(14, city13)

print(15, city13.pop())  # random element gets popped

del city13   # delete the set
# print(16, city13)

city12.clear()
print(17, city12)
