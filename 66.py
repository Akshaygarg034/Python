# **************************  Instance variables vs Class variables  **************************


# Instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class.

# Example

class Employee:
    company = "Newgen"     # class variable

    def __init__(self, name, age):
        self.name = name     # instance variable
        self.age = age

    def show_info(self):
        print(f"The name of the employee is {self.name} and age is {self.age} and company is {self.company}")

print("Without creating any instance -> ", Employee.company)
# In python Whenever any class is created python by default create a object of that class and store all the class variables in that object. Thus we can access class variables even without creating any instance of the class.

e1 = Employee("Akshay", "21")
e2 = Employee("Abhay", "19")

print(1, e1.company)

e2.company = "Google"   # This will create a new instance variable for e2 and will not change the class variable

print(2, e2.company)
# Python first checks if there is an instance variable with the name company in e2, if not then it checks for class variable with the name company in Employee class.

print(3, e1.company)
Employee.company = "Microsoft"  # This will change the class variable for all instances

print(4, e1.company)

e1.roll_no = 59  # Here python doesn't finds both instance and class variable for this name. So it will create a new instance variable for e1

print(5, e1.roll_no)



