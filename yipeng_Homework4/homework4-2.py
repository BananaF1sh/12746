'''
Name: Yi Peng AndrewID: yipeng Homework: 4-2 coursenumber: 12746 
''' 

# Receive an argument from the user and calculate the factorial
from tkinter import *

# calculate the factorial of number
# if the argument is not an integer, a prompt is given
def factorial():
    result = 1
    try:
        num = int(entry.get())
    except:
        errotext = "Oops... Please enter a number : )"
        clickText(errotext)
    else:
        for i in range(1, num+1):
            result = result * i
        clickText(result)

# set the text of label
def clickText(numtext):
    label.config(text= numtext)

# initialize the GUI
root = Tk()
root.title("Factorial")
root.geometry("350x200")

# initialize the label
label = Label(root, text="The answer is")

# initialzie the entry
entry = Entry(root,width = "5")
entry.bind('<Return>',factorial)
entry.pack(side = LEFT)

# initialize the button
button = Button(root, text="OK", command=lambda:factorial())
button.pack(side= BOTTOM)
label.pack(side= LEFT)
# enter the mainloop
root.mainloop()