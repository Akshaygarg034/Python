# ***************************  For Loop with else in Python  ***************************

for i in range(11):
    print(i)
    if i == 5:
        break     # if due to such reasons loop breaks, then else will not execute
else:
    print("loop executed successfully")  # it is used to check whether loop executed fully or not
