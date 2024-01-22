# ***************************  Raising custom errors in Python  ***************************

a = int(input("Enter number bwteen 5 to 10: "))

if(a < 5 or a > 10):
    # raise Exception("Number is not in range")
    raise ValueError("Number is not in range")
