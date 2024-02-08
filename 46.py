# ***************************  os Module in Python  ***************************

import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")

# folders = os.listdir("data")

# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))

print(os.listdir())

print(os.getcwd())

f = os.popen("echo 'hello world'")   # Write linux commands in the string

print(f.read())

os.system('notify-send -i face-wink "Smile please"') # This will execute this command on your system. i.e. it will display a notification on your desktop
