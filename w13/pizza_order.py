from tkinter import *
from tkinter import messagebox

##### EVENT HANDLER #####
def btn_calculate_clicked():
    # get the pizza price
    pizza_price = pizza_var.get()

    # get the extras prices
    # if the extra is selected, add its price to the pizza price
    if water_var.get():
        pizza_price += 0.5
    if ice_cream_var.get():
        pizza_price += 1.5
    if coke_var.get():
        pizza_price += 1.0

    # show the total price in the entry box
    txt_bill.delete(0, END)
    txt_bill.insert(0, f"${pizza_price:.2f}")
    
##### CREATE UI #####
window = Tk()
window.title("Pizza Order")
window.geometry("300x300")

lbl_pizza = Label(window, text="Select a pizza:")
lbl_pizza.grid(row=0, column=0, padx=5, pady=10, sticky=W)

pizza_var = IntVar()
pizza_var.set(1)  # set the first option as default

rd_hawaiian = Radiobutton(window, text="Hawaiian", value=15, variable=pizza_var)
rd_hawaiian.grid(row=1, column=0, padx=5, pady=10, sticky=W)

rd_veggy = Radiobutton(window, text="Veggie", value=10, variable=pizza_var)
rd_veggy.grid(row=2, column=0, padx=5, pady=10, sticky=W)

rd_special = Radiobutton(window, text="Special", value=20, variable=pizza_var)
rd_special.grid(row=3, column=0, padx=5, pady=10, sticky=W)

lbl_extras = Label(window, text="Select extras:")
lbl_extras.grid(row=0, column=1, padx=5, pady=10, sticky=W)

water_var = BooleanVar()
water_var.set(False)  # set the first option as default
chk_water = Checkbutton(window, text="Water", variable=water_var)
chk_water.grid(row=1, column=1, padx=5, pady=10, sticky=W)

ice_cream_var = BooleanVar()
ice_cream_var.set(False)  # set the first option as default
chk_ice_cream = Checkbutton(window, text="Ice Cream", variable=ice_cream_var)
chk_ice_cream.grid(row=2, column=1, padx=5, pady=10, sticky=W)

coke_var = BooleanVar()
coke_var.set(False)  # set the first option as default
chk_coke = Checkbutton(window, text="Coke", variable=coke_var)
chk_coke.grid(row=3, column=1, padx=5, pady=10, sticky=W)

btn_calculate = Button(window, text="Calculate", command=btn_calculate_clicked)
btn_calculate.grid(row=4, column=0, padx=5, pady=10, sticky=W)

txt_bill = Entry(window, width=10)
txt_bill.grid(row=4, column=1, padx=5, pady=10, sticky=W)

##### RUN THE WINDOW #####
window.mainloop()