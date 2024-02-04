# **************************  'is' vs '==' in Python  **************************

# 'is' is used to check if the two variables refer to the same object in memory
# '==' is used to check if the values of the two variables are the same

arr1 = [1, 2, 3]
arr2 = arr1   # arr2 refers to the same object as arr1, if arr2 is changed arr1 will also gets changed

arr3 = arr1.copy()

a = 4
b = 4  # In this case python make only one object in memory (because they are immutable) and both a and b refer to the same object. If we later changes b = 5, then python creates a new object in memory for b

print(arr1 is arr2)
print(arr1 == arr2)
print(arr1 is arr3)
print(a is b)
