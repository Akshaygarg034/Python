# ***************************  Introduction to Lists in Python  ***************************
 
ls = [1, 2, 3.0, "Akshay", True]

print(ls[3])
print(ls[-3])   # === ls[5 - 3] === ls[2]
print(ls)

if 3.0 in ls:
    print("Yes")

if "Ak" in "Akshay":  # Same for strings
    print("Yes")

# List Comprehension

ls2 = [i for i in range(1, 11) if i%2 == 0]
print(ls2)
