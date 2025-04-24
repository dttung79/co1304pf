from tkinter import *

##### EVENT HANDLER #####
def rd_gift_selected():
    value = gift_var.get()
    print(value)
    lbl_price.config(text=f'Price ${value}')

##### CREATE UI #####
window = Tk()
window.title("Select Gift")
window.geometry("400x300")

lbl_select = Label(window, text="Select a gift")
lbl_select.grid(row=0, column=0, padx=10, pady=10, sticky=W)

gift_var = IntVar()
gift_var.set(5)  # set the first option as default
rd_notebook = Radiobutton(window, text="Notebook", value=5, variable=gift_var, command=rd_gift_selected)
rd_notebook.grid(row=1, column=0, padx=10, pady=10, sticky=W)

rd_pen = Radiobutton(window, text="Color pen", value=3, variable=gift_var, command=rd_gift_selected )
rd_pen.grid(row=2, column=0, padx=10, pady=10, sticky=W)

rd_flower = Radiobutton(window, text="Paper flower", variable=gift_var, value=4, command=rd_gift_selected)
rd_flower.grid(row=3, column=0, padx=10, pady=10, sticky=W)

lbl_price = Label(window, text="Price :$5")
lbl_price.grid(row=4, column=0, padx=10, pady=10, sticky=W)

##### RUN THE WINDOW #####
window.mainloop()