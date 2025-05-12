# Here we are learning Object Oriented Programming.
# This is class "Inheritance" in python.
class BaseClass:
    def display(self):
        print("Hello")

# Main class passing like an argument to another class.
# Here we can also access methods from "BaseClass" methods through "SubClass" object.
# Which means a copy of "BaseClass" will also in "SubClass" that's it.
class SubClass(BaseClass):
    def welcome(self):
        print("Welcome")

x=BaseClass()
x.display()


y=SubClass()
y.display()
y.welcome()

# If a variables is in a class. The Class Inheritance act like this way.
class MainClass:
    def set_name(self, name):
        self.name = name

# In this class we can also access "MainClass" from here.
# Because a copy of "MainClass" will here in "SecondClass".
# This is class Inheritance in python.
class SecondClass(MainClass):
    def display_name(self):
        print("Name is: " + self.name)

z = SecondClass()
z.set_name("Muhammed Bilal K A")
z.display_name()