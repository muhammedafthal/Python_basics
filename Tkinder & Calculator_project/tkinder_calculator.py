from tkinter import *

root = Tk()

root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

# Global variable to store the expression
expression = ""

# Result display label
label_result = Label(root, width=40, height=2, text="", font=("arial", 30), bg="white", anchor="e", padx=10)
label_result.pack()

# Function to update label_result
def update_result(value):
    global expression
    expression += str(value)
    label_result.config(text=expression)

# Function for '=' to evaluate the expression
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        label_result.config(text=result)
        expression = result  # Allow chaining operations
    except:
        label_result.config(text="Error")
        expression = ""

# Function to clear the result
def clear():
    global expression
    expression = ""
    label_result.config(text="")

# General button creator
def create_button(text, x, y, bg_color):
    btn = Label(root, text=text, width=5, height=2, font=("arial", 24, "bold"),
                bg=bg_color, fg="white", bd=0, padx=10, pady=10)
    btn.place(x=x, y=y)
    if text == "C":
        btn.bind("<Button-1>", lambda e: clear())
    elif text == "=":
        btn.bind("<Button-1>", lambda e: evaluate())
    else:
        btn.bind("<Button-1>", lambda e: update_result(text))

def create_button1(text, x, y, bg_color):
    btn = Label(root, text=text, width=5, height=6, font=("arial", 24, "bold"),
                bg=bg_color, fg="white", bd=0, padx=10, pady=10)
    btn.place(x=x, y=y)
    if text == "=":
        btn.bind("<Button-1>", lambda e: evaluate())
    else:
        btn.bind("<Button-1>", lambda e: update_result(text))

def create_button2(text, x, y, bg_color):
    btn = Label(root, text=text, width=15, height=2, font=("arial", 24, "bold"),
                bg=bg_color, fg="white", bd=0, padx=10, pady=10)
    btn.place(x=x, y=y)
    btn.bind("<Button-1>", lambda e: update_result(text))

# Create buttons
create_button("C", 10, 100, "#3697f5")
create_button("/", 150, 100, "#2a2d36")
create_button("%", 290, 100, "#2a2d36")
create_button("*", 430, 100, "#2a2d36")

create_button("7", 10, 200, "#2a2d36")
create_button("8", 150, 200, "#2a2d36")
create_button("9", 290, 200, "#2a2d36")
create_button("-", 430, 200, "#2a2d36")

create_button("4", 10, 300, "#2a2d36")
create_button("5", 150, 300, "#2a2d36")
create_button("6", 290, 300, "#2a2d36")
create_button("+", 430, 300, "#2a2d36")

create_button("1", 10, 400, "#2a2d36")
create_button("2", 150, 400, "#2a2d36")
create_button("3", 290, 400, "#2a2d36")
create_button1("=", 430, 400, "orange")

create_button(".", 290, 500, "#2a2d36")
create_button2("0", 10, 500, "#2a2d36")

root.mainloop()
