# This "tkinder" library is for to create a window application in python.
# The "*" is for to get what are things is included in the "tkinder" library.
# After imported the library we should assign "Tk()" method into a variable. Here "window" is variable.
# Then we should use "mainloop()" method into that variable before we created.
# The "mainloop()" method is for to run the created window continuously.
# When ever we close the created "window app" then only the execution will end.
# After that if we run this program we will get a plane new "window application".
from tkinter import *

window = Tk()

# This is for to get width & height for created window.
window.geometry("500x500")
# This is for set a title for created window.
window.title("GUI Sample")
# This is for to set a background colour for created window.
window.configure(bg="yellow")

# Here we created this function for to take action when ever we clicked the button.
def hello():
    print("Button clicked")

# This is for create a button in created window.
# Here the last argument "command" is for execute what are the operation or action were define in that function "hello".
button = Button(window, text="ok", width=30, height=30,  command=hello)
# This is for to show any label text in created window.
label = Label(window, text="welcome", height=10)

# This "pack()" method is using for to attach those above things to created window.
button.pack()
label.pack()

window.mainloop()