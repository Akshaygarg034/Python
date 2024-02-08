# ************************  Multithreading in Python  ************************

# Multithreading is a technique in which multiple threads are created to execute tasks concurrently. Threads share the same memory space and can share data with each other. It is perfect for CPU-bound operations.

# Example:

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def print_numbers():
    for i in range(1, 6):
        time.sleep(2)
        print(i)

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(letter)

# t1 = threading.Thread(target = print_numbers)  # created a thread
# t2 = threading.Thread(target = print_letters)  # created another thread

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# The join method is used to wait for the threads to complete. If we do not use join, the main thread will not wait for the threads to complete and will exit, causing the threads to be terminated.

# Also due to gil (Global Interpreter Lock), Python threads are not suitable for CPU-bound operations. For CPU-bound operations, we should use the multiprocessing module.

# During certain blocking I/O operations, the GIL can also be released, allowing other threads to run while the thread is waiting for the I/O operation to complete.
        

### Using threadpool executer
        
def wrapper(func_name):
    if func_name == 'numbers':
        print_numbers()
    elif func_name == 'letters':
        print_letters()
        

with ThreadPoolExecutor() as executor:
    # executor.submit(print_numbers)
    # executor.submit(print_letters)

    executor.map(wrapper, ["numbers", "letters"])
    
