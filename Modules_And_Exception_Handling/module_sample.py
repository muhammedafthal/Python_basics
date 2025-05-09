print(__name__) # This is for to get the module name or file name.
def check_neg_or_pos () :
    num = int(input("Enter a number"))

    if num < 0:
        print("Entered number is negative")
    elif num == 0:
        print("Entered number is zero")
    else:
        print("Entered number is positive")