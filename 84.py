# ************************  Time Module in Python  ************************

# The time module in Python provides many functions to manipulate time values.

# e.g.

import time

print("1 ->", time.time()) # returns the current time in seconds since the epoch (January 1, 1970)

t = time.localtime() # returns the current time in the form of a tuple
print("2 ->", t) 

formatted_time = time.strftime("%m-%d-%Y %H:%M:%S", t) # returns the current time in the form of a string

print("3 ->", formatted_time)

time.sleep(3) # suspends the execution of the current thread for a given number of seconds

print("\nI am printed after 3 seconds")
