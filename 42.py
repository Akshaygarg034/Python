# ***************************  Enumerate Function in Python  ***************************

marks = [45, 78, 86, 77, 90, 99, 100]

# for i, mark in enumerate(marks):
#     if(i == 0):
#         print("First element")

#     print(mark)

#     if(i == len(marks)-1):
#         print("Last element")


for i, mark in enumerate(marks, start = 1):
    if(i == 0):
        print("First element")

    print(mark)

    if(i == len(marks)-1):
        print("Last element")
