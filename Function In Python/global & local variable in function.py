value = 10 # This is global variable.

def sample () :
    value = 20 # This is local variable.
    print(value)

print(value)
sample()