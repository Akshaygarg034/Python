# ***************************  File IO in Python  ***************************

# Reading a file

f = open("script.py", "r")   # open the file in read mode (default mode)
f = open("script.py")     # same as before

print(1, f)

f1 = open("script.py", "rb")  # open the file in read mode (binary mode)
print(2, f.read())


# Writing a file (it automatically creates a file if it doesn't exist)

# w = open("script.py", "w")   # open the file in write mode
# w.write("\"i am changed\"")
# w.close()   # changed takes place only after closing the file

with open("script.py", "w") as w1:     # with keyword automatically closes the file
    w1.write("\"I am changed again\"")

with open("script.py", "a") as a:  # open the file in append mode (it doesn't overwrite file)
    a.write("\n\"I am appended\"")
