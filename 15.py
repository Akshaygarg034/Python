# ***************************  Greeting  ***************************
import time

print(time.strftime('%H: %M: %S'))

if int(time.strftime('%H')) < 12:
    print("Good morning")
elif int(time.strftime('%H')) < 17:
    print("Good afternoon")
else:
    print("Good evening")