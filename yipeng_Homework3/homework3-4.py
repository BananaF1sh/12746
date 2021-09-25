'''
Name: Yi Peng AndrewID: yipeng Homework: 3-4 coursenumber: 12746 
''' 

import tkinter as tk
from tkinter.constants import BOTTOM


# initialize the size and background color
window = tk.Tk()
window.configure(bg='#FF7F50')
window.geometry("800x800")

# Insert the text entry box
entry1 = tk.StringVar()
tk.Entry(window, textvariable=entry1).pack()
entry1.set("Say something!")

# Insert the quit botton
button = tk.Button(text="quit", command=window.destroy)
button.pack()

# Insert the pull-down menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New")
OptionList = ["Hello", "This", "is", "Yi Peng"]
variable = tk.StringVar(window)
variable.set(OptionList[0])
opt = tk.OptionMenu(window, variable, *OptionList)
opt.pack()

# Insert the image
photo = tk.PhotoImage(file="amkat-jdx4w.gif")
tk.Label(window, image=photo).pack()

window.mainloop()

