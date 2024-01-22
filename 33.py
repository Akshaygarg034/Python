# ***************************  Dictionaries in Python  ***************************

dict = {"name" : "Akshay", "age" : 21, "marks" : [90, 80, 70], "another_dict" : {"Akshay" : "Player"}}
print(1, dict)

print(2, dict["name"])  # Will throw error if key "name" not exist
print(3, dict.get("name"))  # returns None if key "name" not exist

print(4, dict.keys())
print(5, dict.values())

for key, value in dict.items():
    print(key, "--->", value)
