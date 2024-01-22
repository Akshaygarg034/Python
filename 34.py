# ***************************  Dictionary Methods  ***************************

dict1 = {"name": "John", "age": 25, 1001: True}
dict2 = {"school": "international", "age": 29, 1002: True}

# #  If the key is in the dictionary, it updates the key with the new value. (Like age here)
# If the key is not in the dictionary, it adds the key-value pair to the dictionary.

dict1.update(dict2)
print(1, dict1)

dict2.clear()
print(2, dict2)

print(3, dict1.pop("age"))
print(4, dict1.popitem())

del dict1["name"]

print(5, dict1)
