from tkinter import *

##### EVENT HANDLER #####
def add():
    calculate('+')

def subtract():
    calculate('-')

def multiply():
    calculate('*')

def divide():
    calculate('/')

def calculate(operation='+'):
    try:
        a = int(txt_a.get())
        b = int(txt_b.get())
        if operation == '+':
            c = a + b
        elif operation == '-':
            c = a - b
        elif operation == '*':
            c = a * b
        elif operation == '/':
            c = a / b
        lbl_result.config(text=str(c))
    except ValueError:
        lbl_result.config(text="Invalid input")
    except ZeroDivisionError:
        lbl_result.config(text="Cannot divide by zero")

##### CREATE UI #####
window = Tk()
window.title("Demo GUI 02")
window.geometry("400x300")

lbl_a = Label(window, text="a")
lbl_a.grid(row=0, column=0)
txt_a = Entry(window)
txt_a.grid(row=0, column=1, columnspan=4)

lbl_b = Label(window, text="b")
lbl_b.grid(row=1, column=0)
txt_b = Entry(window)
txt_b.grid(row=1, column=1, columnspan=4)

btn_add = Button(window, text='+', command=add)
btn_add.grid(row=2, column=1)

btn_sub = Button(window, text='-', command=subtract)
btn_sub.grid(row=2, column=2)

btn_mul = Button(window, text='*', command=multiply)
btn_mul.grid(row=2, column=3)

btn_div = Button(window, text='/', command=divide)
btn_div.grid(row=2, column=4)

lbl_result = Label(window, text="0")
lbl_result.grid(row=3, column=1)

##### RUN THE WINDOW #####
window.mainloop()