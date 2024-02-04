# ***************************  String Methods in Python  ***************************

a = "!!!Harry!! !!!!!!!!! Harry!!!!"
print(1, len(a))
print(2, a)
print(3, a.upper())
print(4, a.lower())
print(5, a.rstrip("!"))
print(6, a.replace("Harry", "John"))
print(7, a.split(" "))
blogHeading = "introduction tO jS"
print(8, blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(9, len(str1))
print(10, str1.center(50))
print(11, a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(12, str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(13, str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(14, str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(15, str1.isalnum())
str1 = "Welcome"
print(16, str1.isalpha())

str1 = "hello world"
print(17, str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(18, str1.isprintable())
str1 = "         "       #using Spacebar
print(19, str1.isspace())
str2 = "  "       #using Tab
print(20, str2.isspace())

str1 = "World Health Organization" 
print(21, str1.istitle())

str2 = "To kill a Mocking bird"
print(22, str2.istitle())

str1 = "Python is a Interpreted Language" 
print(23, str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(24, str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(25, str1.title())

str2 = ["hello", "my", "name", "is", "Akshay"]
print(26, " ".join(str2))     # join the list of strings with a space
