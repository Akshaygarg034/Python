# **************************  seek(), tell() and other functions  **************************

f = open("data.txt", "r")

f.seek(3)  # move the file pointer to the 5th byte

print(f.read(4))  # only read next 4 bytes

print(f.tell())  # tell the current position of the file pointer

w = open("data.txt", "w")
w.write("My name is Akshay and i am from Himachal Pradesh")
w.truncate(17) # truncate the file to 5 bytes
