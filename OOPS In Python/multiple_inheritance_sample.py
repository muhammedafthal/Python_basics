# This is called "Multiple Inheritance."
class First:
    def display_first(self):
        print("First")
class Second:
    def display_second(self):
        print("Second")
class Third(First, Second):
    def display_third(self):
        print("Third")

x = Third()
x.display_third()
x.display_second()
x.display_first()

# This is called "Multi-Level Inheritance."
class FirstClass:
    def display_1(self):
        print("First Class")
class SecondClass(FirstClass):
    def display_2(self):
        print("Second Class")
class ThirdClass(SecondClass):
    def display_3(self):
        print("Third Class")

z = ThirdClass()
z.display_3()
z.display_2()
z.display_1()
