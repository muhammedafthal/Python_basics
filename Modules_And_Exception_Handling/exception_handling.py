# This is for exception handling in python.

b=0

try:
    a=10/b
    print(a)
    print("Try completed...")
except ZeroDivisionError: # This is the syntax.
    print("Can't divided by zero")

print("Program completed...")