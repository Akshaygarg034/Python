# ***************************  break and continue in Python  ***************************

i = 1

# break
for i in range(1, 11):
    print("5 X", i, "=", 5 * i)
    if i == 5:
        print("ending iteration")
        break

# Continue
for i in range(1, 11):
    if i == 5:
        print("skipping iteration")
        continue
    print("5 X", i, "=", 5 * i)