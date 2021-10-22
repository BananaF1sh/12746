import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import geoplot as gplt
import geoplot.crs as gcrs


class myGeoprocess:
    # Initialize the GUI
    def __init__(self):
        self.root = tk.Tk()
        self.file_path = ''
        self.file_name = ''
        self.root.geometry("500x500")
        self.root.pack_propagate(False)
        self.root.resizable(0, 0)

    # Visualize the vector data of bridges 
    def visualize(self):
        file_path = self.label_file['text']
        filename = r"{}".format(file_path)
        points = gpd.read_file(filename)
        points_bridge = gpd.GeoDataFrame(points,geometry=gpd.points_from_xy(points.longitude, points.latitude),crs='EPSG:4326')

        ax = gplt.polyplot(df=points_bridge,
                    projection=gcrs.AlbersEqualArea())

        plt.show()
        return None

    # browse the file and record the file path
    def File_dialog(self):
        self.file_name = filedialog.askopenfilename(initialdir="/", 
                                            title="Select A File", 
                                            filetypes=(("xlsx files", "*.xlsx"),("csv files","*.csv"),("All Files", ".")))
        self.label_file["text"] = self.file_name
        return None

    # load file 
    def Load_data(self):
        self.file_path = self.label_file['text']
        try:
            csv_filename = r"{}".format(self.file_path)
            df = pd.read_csv(csv_filename)
        except ValueError:
            messagebox.showerror("Information","The file you have chosen is invaild")
        except FileNotFoundError:
            messagebox.showerror("Information",f"No such as file as {self.file_path}" )
            return None
        
        self.clear_data()
        self.tv1["column"] = list(df.columns)
        self.tv1["show"] = "headings"
        for column in self.tv1["columns"]:
            self.tv1.heading(column, text=column)
        
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.tv1.insert("", "end", values=row)
    
    # when using the load_data function, clear the data in treeview
    def clear_data(self):
        self.tv1.delete(*self.tv1.get_children())

    def main(self):
        # frame for Treeview
        self.frame1 = tk.LabelFrame(self.root, text='CSV Data')
        self.frame1.place(height=250, width=500)
        # label
        self.label_file = ttk.Label(text='No File Selected')
        self.label_file.place(rely=0, relx=0)
        # Treeview widget
        self.tv1 = ttk.Treeview(self.frame1)
        self.tv1.place(relheight=1, relwidth=1)
        # add scroll for the Treeview
        self.treescrolly = tk.Scrollbar(self.frame1, orient='vertical', command=self.tv1.yview)
        self.treescrollx = tk.Scrollbar(self.frame1, orient='horizontal', command=self.tv1.xview)
        self.tv1.configure(xscrollcommand=self.treescrollx.set, yscrollcommand=self.treescrolly.set)
        self.treescrollx.pack(side='bottom', fill='x')
        self.treescrolly.pack(side='right', fill='y')
        
        # file frame
        self.file_frame = tk.LabelFrame(self.root, text='Open File')
        self.file_frame.place(height=100, width=400, rely=0.7, relx=0)
        # Buttons for file frame
        self.button_browse = tk.Button(self.file_frame, text='Browse a file', command=lambda: self.File_dialog())
        self.button_browse.place(rely=0.8, relx=0.60)
        self.button_browse.pack()

        self.button_load = tk.Button(self.file_frame,text='Load file', command=lambda: self.Load_data())
        self.button_load.place(rely=0.8, relx=0.20)
        self.button_load.pack()

        # data frame
        self.data_frame = tk.LabelFrame(self.root, text='Data')
        self.data_frame.place(height=80, width=400,rely=0.5,relx=0)
        # Button for visualize
        self.button_visualize = tk.Button(self.data_frame, text='Visualize data', command=lambda: self.visualize())
        self.button_visualize.pack()
      
        self.root.mainloop()


process = myGeoprocess()
process.main()