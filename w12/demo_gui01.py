# import all from tkinter
from tkinter import *

def say_hello():
    # get text from entry
    language = txt_name.get()
    # change the text of the label
    lbl_hello.config(text="Hello " + language + " World!")

# create a window
window = Tk()
# set title of window
window.title("Demo GUI 01")
# set size of window
window.geometry("400x300")


# add some widgets
lbl_hello = Label(window, text="Hello World!")  # create a label
lbl_hello.grid(row=0, column=0)         # add label to window using grid system

txt_name = Entry(window)
txt_name.grid(row=1, column=0)

btn_hello = Button(window, text="Say Hello", command=say_hello)
btn_hello.grid(row=2, column=0)

# run the window
window.mainloop()