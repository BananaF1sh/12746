'''
Name: Yi Peng AndrewID: yipeng Homework: 5-2 coursenumber: 12746 
''' 
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class file_opener:
    
    # Initialize the GUI
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x250')

    # Select the csv file
    def file_dialog(self):
        # Initial dir is current folder
        self.file_name = filedialog.askopenfilename(initialdir="./", 
                                            title="Select A File", 
                                            filetypes=(("csv files","*.csv"),("All Files", ".")))
        # update the text of label file to show the selected file path
        self.label_file['text'] = self.file_name


    # Load the file
    def load_data(self):
        # load the file path from the label file
        self.file_path = self.label_file['text']
        try:
            f = open(r'{}'.format(self.file_path), 'r')
            self.data_label['text'] = f.readline()
        except ValueError:
            messagebox.showerror("Information","The file you  have chosen is invaild")
        except FileNotFoundError:
            messagebox.showerror("Information",f"No such as file as {self.file_path}" )
        
        

    def main(self):
        
        # data frame
        self.data_frame = tk.LabelFrame(self.root, text='Load data')
        self.data_frame.place(height=100, width=400, rely=0.3, relx=0)
        # show data in data frame
        self.data_label = tk.Label(self.data_frame,text='No data')
        self.data_label.pack()        

        # file frame
        self.file_frame = tk.LabelFrame(self.root, text='Open File')
        self.file_frame.place(height=100, width=400, rely=0.6, relx=0)
        
        # Buttons for file frame

        # Browse the file
        self.button_browse = tk.Button(self.file_frame, text='Browse a file', command=lambda: self.file_dialog())
        self.button_browse.place(rely=0.4, relx=0.70)
        self.button_browse.pack()
        # Load the file
        self.button_load = tk.Button(self.file_frame,text='Load file', command=lambda: self.load_data())
        self.button_load.place(rely=0.9, relx=0.10)
        self.button_load.pack()
        
        # label to show the selected file
        self.label_file = ttk.Label(text='No File Selected')
        self.label_file.place(rely=0, relx=0)

        self.root.mainloop()


fo = file_opener()
fo.main()