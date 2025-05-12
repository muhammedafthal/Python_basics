
# By default if we run "SubClass". The constructor inside "BaseSample" class will execute.
# If there is no any other constructor.
# Through "super()" method we can call like override. Here both "Constructor" & "Method is override."
class BaseSample:
    # Here wwe just create a constructor.
    def __init__(self):
        print("Base init")

    def set_name(self, name):
        self.name = name
        print("BaseClass set_name")

# But if there is a constructor like below mention.
# Then the this constructor will be override previous one.
# This is called "Constructor Override".
# So here "Sub unit" will be execute.
# Also we write an example for method "override".
# So here the "set_name" method is override.

class SubClass(BaseSample):
    # If we also want "BaseClass" constructor.
    # Then we can write this way.
    def __init__(self):
        # Below mention "BaseSample.__init(self)" & "super().__init__()" are same.
        BaseSample.__init__(self)
        super().__init__() # This is "Standard way to call."
        print("Sub init")

    # Here we call the "set_name" from "BaseClass" through "super()" Method.
    def set_name(self, name):
        super().set_name(name)
        print("SubClass set_name")

    def welcome(self):
        print("Welcome")

    def display_name(self):
        print("Name: " + self.name)

y = SubClass()
y.welcome()
y.set_name("Muhammed Afthal K")
y.display_name()
