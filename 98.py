# ************************  MultiProcessing in Python  ************************

# The multiprocessing module in Python is used to run multiple processes concurrently. It is used to avoid the GIL (Global Interpreter Lock) and take advantage of multiple cores.

# Example:

import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

def print_numbers(string):
    print(f"printing {string}")
    for i in range(1, 6):
        time.sleep(2)
        print(i)

def print_letters(string):
    print(f"printing {string}")
    for letter in "abcde":
        time.sleep(2)
        print(letter)

# p1 = multiprocessing.Process(target = print_numbers, args = ["numbers"])  # created a process
# p2 = multiprocessing.Process(target = print_letters, args = ["letters"])  # created another process

# p1.start()
# p2.start()

# p1.join()
# p2.join()


# GIL does not affect multiprocessing, so it is used for CPU-bound operations. It creates a separate memory space for each process.
        

### Using Process pool executer
        
def wrapper(func_name):
    if func_name == 'numbers':
        print_numbers("numbers")
    elif func_name == 'letters':
        print_letters("letters")
        
with ProcessPoolExecutor() as executor:
    executor.map(wrapper, ["numbers", "letters"])
