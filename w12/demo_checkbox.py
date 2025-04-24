from tkinter import *
from tkinter import messagebox

##### EVENT HANDLER #####
def update_language():
    s = "I can speak: "
    if opt1_var.get() == True: s += "English "
    if opt2_var.get() == True: s += "Spanish "
    if opt3_var.get() == True: s += "French "
    if opt1_var.get() == False and opt2_var.get() == False and opt3_var.get() == False:
        s = "I can speak: None"
    
    lbl_languages.config(text=s)
##### CREATE UI #####
window = Tk()
window.title("Demo GUI 03")
window.geometry("400x300")

lbl_question = Label(window, text="Select an option:")
lbl_question.grid(row=0, column=0, sticky=W)

opt1_var = BooleanVar()
cb_option1 = Checkbutton(window, text="English", variable=opt1_var, command=update_language)
cb_option1.grid(row=1, column=0, sticky=W)
opt2_var = BooleanVar()
cb_option2 = Checkbutton(window, text="Spanish", variable=opt2_var, command=update_language)
cb_option2.grid(row=1, column=1, sticky=W)
opt3_var = BooleanVar()
cb_option3 = Checkbutton(window, text="French", variable=opt3_var, command=update_language)
cb_option3.grid(row=1, column=2, sticky=W)

lbl_languages = Label(window, text="I can speak: None")
lbl_languages.grid(row=2, column=0, columnspan=3, sticky=W)
##### RUN THE WINDOW #####
window.mainloop()