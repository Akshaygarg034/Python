# ************************  Regular Expressions in Python  ************************

# Regular expressions are a powerful tool for various kinds of string manipulation. They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python. They are useful for two main tasks:

# 1. verifying that strings match a pattern (for instance, that a string has the format of an email address),
# 2. performing substitutions in a string (such as changing all American spellings to British ones).

# Python has a built-in package called re, which can be used to work with regular expressions.

# Example:

import re

# The re.match function returns a match object on success, None on failure. We use group(num) or groups() function of match object to get matched expression.

# The re.match function can be used to determine whether it matches at the beginning of a string.

pattern = r"Cookie"  # r is used to indicate a raw string
sequence = "Cookie"
if re.match(pattern, sequence):
    print("Match!")

# The re.search function is used to search a string for a match. It returns a match object if there is a match anywhere in the string, otherwise it returns None.
    
if re.search(pattern, sequence):
    print("Match!")

# For more details, visit: https://regexr.com/ and https://docs.python.org/3/library/re.html
