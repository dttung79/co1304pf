from tkinter import *
from tkinter import messagebox

##### EVENT HANDLER #####
def rd_color_selected():
    # get the selected color via the value of the associated variable
    selected_color = color_var.get()
    
    if   selected_color == 1:   color = "Red"
    elif selected_color == 2:   color = "Green"
    else                    :   color = "Blue"
    # show a message box with the selected color 
    messagebox.showinfo("Selected Color", f"You selected: {color}")
    
##### CREATE UI #####
window = Tk()
window.title("Demo Radio Button")
window.geometry("400x300")

color_var = IntVar()
color_var.set(1) # set the Red option as default

lbl_question = Label(window, text="Select a color:")
lbl_question.grid(row=0, column=0, sticky=W, padx=10, pady=10)

rd_red = Radiobutton(window, text="Red", value=1, variable=color_var, command=rd_color_selected)
rd_red.grid(row=1, column=0, sticky=W, padx=10, pady=10)

rd_green = Radiobutton(window, text="Green", value=2, variable=color_var, command=rd_color_selected)
rd_green.grid(row=2, column=0, sticky=W, padx=10, pady=10)

rd_blue = Radiobutton(window, text="Blue", value=3, variable=color_var, command=rd_color_selected)
rd_blue.grid(row=3, column=0, sticky=W, padx=10, pady=10)

##### RUN THE WINDOW #####
window.mainloop()