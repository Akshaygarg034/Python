# ************************  Shutil Module in Python  ************************

# The shutil module in Python provides many functions to perform high-level operations on files and collections of files.

# e.g.

import shutil
import os

# Copy a file
# shutil.copy("data.txt", "data2.txt")

# Copy a directory
# shutil.copytree("dir1", "dir2")

# Move a file
# shutil.move("data.txt", "file/data3.txt")

# Remove a directory
# shutil.rmtree("dir2")

# Remove a file
os.remove("data2.txt")   # shutil has no attribute to remove a file
