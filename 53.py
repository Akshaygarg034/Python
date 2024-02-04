# **************************  Map, Filter and Reduce in Python  **************************

from functools import reduce

##### Map 
# map(function, list) -> It applies funciton to all the items in the list

numbers  = [1, 2, 3, 4, 5, 6, 7]

list2  = list(map(lambda x : x * 2, numbers))
print("list2 ->", list2)

##### Filter
# filter(function, list) -> It filters out the elements from the list for which the function returns True

list3 = list(filter(lambda x: x%2 == 0, numbers))
print("list3 ->", list3)

##### Reduce (needs to be imported from functools)
# reduce(function, list) -> It applies the function to all the elements in the list and returns a single value

res = reduce(lambda x, y : x + y, numbers)
print("res ->", res)
