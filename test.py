import os
import tkinter as tk

from tkcalendar import Calendar
from tkinter import ttk, filedialog, messagebox
from tkinter import *
 
OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

def open_file():
    file_path = filedialog.askopenfilename()
    try:
        return file_path
    except:
        print("Open operation cancelled")
        return

    


root = tk.Tk()
root.title("My Text Editor")
root.option_add("*tearOff", False)
root.geometry("400x400")

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=(1), pady=(4, 0))

variable = StringVar(main)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(main, variable, *OPTIONS)
w.pack()

B = tk.Button(root, text ="Hello", command = open_file)
B.pack()

cal = Calendar(root, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
 
cal.pack(pady = 20)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
Button(root, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(root, text = "")
date.pack(pady = 20)

mainloop()