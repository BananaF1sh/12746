'''
Name: Yi Peng AndrewID: yipeng Homework: 5-1 coursenumber: 12746 
''' 
import tkinter as tk
from tkinter.constants import LEFT
from tkinter import messagebox

class file_opener:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x200')

    def open_file(self):
        self.file_path = self.entry_box.get()
        try:
            f = open(r'{}'.format(self.file_path), 'r')
            self.label_file['text'] = f.readline()
            print(f.readline())
        except ValueError:
            messagebox.showerror("Information","The file you  have chosen is invaild")
        except FileNotFoundError:
            messagebox.showerror("Information",f"No such as file as {self.file_path}" )

    def main(self):

        # creat a frame for file
        self.file_frame = tk.LabelFrame(self.root, text='Open file')
        self.file_frame.place(height=50, width=450, rely=0.7, relx=0)
        self.label_file = tk.Label(self.file_frame, text='No file selected')
        self.label_file.pack()
        
        # button to open the file
        self.button_open_file = tk.Button(self.root, text='load file', command=lambda: self.open_file())
        self.button_open_file.pack(side=LEFT)

        self.label_entry = tk.Label(self.root, text='Please enter the file path')
        self.label_entry.pack(side=LEFT)
        self.entry_box = tk.Entry(self.root, bd=5)
        self.entry_box.pack(side=LEFT)

        self.root.mainloop()


fo = file_opener()
fo.main()