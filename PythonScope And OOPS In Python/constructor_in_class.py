# Like this way we can create "constructor" in python.
class TeamMember:
    # This variable (year) can only access through class. This is a class variable.
    # This variable (year) is for all of its "object" under this "class".
    year = 2025

    # Given below methods is for all "object" under this "class".
    # Here we create "constructor".
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1 # This method is for add age in separate years.

    def relocate(self, place):
        self.place = place

    # This method is for to display the already defined variables in constructor.
    def display(self):
        print("Year: " + str(TeamMember.year))
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Place: " + self.place)

    # This annotation method is using for when ever we are using class variable.
    @classmethod
    def add_year(cls):
        cls.year = cls.year+1

    # This annotation method is using for just print a static message in a class.
    @staticmethod
    def display_welcome():
        print("Welcome")

# By this way we can execute that "static" method inside the "TeamMember" class
TeamMember.display_welcome()

# Here we created the object for the class and pass the values for the created constructor.
x = TeamMember("Muhammed Afthal K", 22, "Mannarkkad")
y = TeamMember("Muhammed Aslam K A", 24, "UAE")

# Through created object we call the method inside the class (TeamMember).
x.display()
y.display()

print("-----------------------------------")

# This one is for add each year.
# And here this can only execute through class. Because "year" is a class variable.
TeamMember.year = TeamMember.year + 1

# This method we called for to add respective age for them.
x.add_age()
y.add_age()

# And after adding age and year. Then display it.
x.display()
y.display()

print("-----------------------------------")

# Here this is now a method under class.
# So it can execute through class.method class name is "TeamMember" and method name is "add_year".
TeamMember.add_year()

# This object method we called for to add respective age for them.
x.add_age()
y.add_age()

# This object method we called for to change their place.
x.relocate("Chennai")
y.relocate("Canada")

# And after adding age and year and change place value. Then display it.
x.display()
y.display()
