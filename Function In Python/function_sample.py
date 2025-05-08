# Function in python.
def hello () :
    print("Hai")

hello()

# Argument passing in function.
def x (name1) :
    print("My name is " + name1)

x("Muhammed Afthal K")

# Multiple argument passing in function.
def y (name2, age) :
    print("My name is " + name2 + " Iam " + str(age))

value = "Muhammed Afthal K"
y(value, 22)

# Another example for passing muliple argument in function(Arbitary Element).
# Here we can pass many arguments.
def z (*values) :
    print("First value: " + values[0] + " Second value: " + values[1])

z("hello", "hai")

# Example of keyword argument.
def sample (name, age) :
    print(name, age)

sample(age = 22, name = "Muhammed Afthal K")

# Here this is example for defualt argument.
def sample1 (name, age = 22) :
    print(name, age)

sample1(name = "Muhammed Afthal K")

# Return statement in function.
def sample3 (num1, num2) :
    sum = num1 + num2
    return sum

result = sample3(10, 20)
print(result)
