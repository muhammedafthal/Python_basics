# This way we can create class in python
# Inside the class here we define a function. It is called "method" in python.
# When we create a class in python. By default an argument will be there that is here "self".
# In a "class" we can create many "object". Examples are below mentioned.
# And for both class value there is separate memory space.
class MySampleClass :
    # Here we set an variable through its object (self).
    def hello(self, n):
        self.name = n
    # Here we print that variable value which is a name.
    def print_name(self):
        print(self.name)

# A class can execute through an object. Below mention "x" and "y" are objects.
# Here we create an object called "x".
x = MySampleClass()
# Here we create a new object called "y".
y = MySampleClass()

name = "Muhammed Afthal K"
# Here i pass an argument called "name".
# And that object through we can call the "method" inside the class (MySampleClass) by this way.
# Through object we can only access any argument.

# Here in first method we set an variable through its object and pass a name value.
x.hello(name)
# Here we pass an new value to object we created which is also a name.
y.hello("Muhammed Aslam K A")
# Here we call that object to execute its object value.
x.print_name()
# Here also we call that new object to execute its object value.
y.print_name()