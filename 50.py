# **************************  read(), readlines() and other methods  **************************


# Readlines method
f = open("data.txt", "r")
lines = f.readlines()   # read the whole file

f.seek(0)  # Reset the file pointer to the beginning of the file otherwise it will not read the file again

line1  = f.readline()   # read the first line
line2  = f.readline()   # read the second line
line3  = f.readline()   # read the third line

print("lines", lines)
print(line1, line2, line3, sep = "")

f.seek(0)

print("\nprinting using loop")

while True:
    line = f.readline()
    print(line, end = "")
    if not line:
        break


# Writelines method
w = open("data.txt", "w")
writeLines = ["My name is Akshay\n", "I am a software developer\n", "I am learning python\n"]
w.writelines(writeLines)
w.close()
