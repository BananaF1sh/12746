import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import geoplot as gplt
import geoplot.crs as gcrs

#  In order to run the code correctly, the following modules are required:
#  tkinter, pandas, matploylib, geopandas, geoplot

class myGeoprocess:
    # Initialize the GUI
    def __init__(self):
        self.root = tk.Tk()
        self.file_path = ''
        self.file_name = ''
        self.df = None
        self.root.geometry("500x500")
        self.root.pack_propagate(False)
        self.root.resizable(0, 0)
        self.columns = ('id','name','year_built', \
                        'year_rehab','neighborhood', \
                        'latitude','longitude','DECK_COD_058', \
                        'SUPERSTRUCTURE_COD_059','SUBSTRUCTURE_COD_060','SCOUR_CRITICAL_113','Aggregated_Rating')

    # Visualize the vector data of bridges 
    def visualize(self):
        file_path = self.label_file['text']
        filename = r"{}".format(file_path)
        # points = gpd.read_file(filename)
        self.df = gpd.read_file(filename)
        # points_bridge = gpd.GeoDataFrame(points,geometry=gpd.points_from_xy(points.longitude, points.latitude),crs='EPSG:4326')
        points_bridge = gpd.GeoDataFrame(self.df,geometry=gpd.points_from_xy(self.df.longitude, self.df.latitude),crs='EPSG:4326')


        map = gpd.read_file("Course_project//2010_Census_Tracts.geojson")
        map_layer = gpd.GeoDataFrame(map, crs='EPSG:4326')

        ax = gplt.polyplot(df=map_layer,
                    projection=gcrs.AlbersEqualArea())
        
        ax = gplt.pointplot(df=points_bridge,
                        s=2,
                        color='blue',
                        alpha=0.8,
                        ax = ax)
        plt.show()
        return None
    
    def calculate(self):
                                     
        for index, row in self.df.iterrows():
            if row['SCOUR_CRITICAL_113'] > 0:
                row['Aggregated_Rating'] = 0.171*row['DECK_COD_058'] + 0.268*row['SUPERSTRUCTURE_COD_059'] + 0.291*row['SUBSTRUCTURE_COD_060'] + 0.27*row['SCOUR_CRITICAL_113']
                # return the value to the dataframe
                self.df.iloc[index] = row
            if row['SCOUR_CRITICAL_113'] == 0:
                row['Aggregated_Rating'] = 0.36*row['DECK_COD_058'] + 0.357*row['SUPERSTRUCTURE_COD_059'] + 0.283*row['SUBSTRUCTURE_COD_060']
                # return the value to the dataframe                
                self.df.iloc[index] = row            

        self.clear_data()
        self.tv1["column"] = list(self.df.columns)
        self.tv1["show"] = "headings"
        for col in self.tv1["columns"]:
            self.tv1.heading(col, text=col, command=lambda col_ = col: self.treeview_sort_column(self.tv1, col_, False))
        
        df_rows = self.df.to_numpy().tolist()
        for row in df_rows:
            self.tv1.insert("", "end", values=row)


    def File_dialog(self):
        self.file_name = filedialog.askopenfilename(initialdir="/", 
                                            title="Select A File", 
                                            filetypes=(("xlsx files", "*.xlsx"),("csv files","*.csv"),("All Files", ".")))
        self.label_file["text"] = self.file_name
        return None

    def Load_data(self):
        self.file_path = self.label_file['text']
        try:
            csv_filename = r"{}".format(self.file_path)
            self.df = pd.read_csv(csv_filename)
        except ValueError:
            messagebox.showerror("Information","The file you have chosen is invaild")
        except FileNotFoundError:
            messagebox.showerror("Information",f"No such as file as {self.file_path}" )
            return None
        
        self.clear_data()
        self.tv1["column"] = list(self.df.columns)
        self.tv1["show"] = "headings"
        for col in self.tv1["columns"]:
            self.tv1.heading(col, text=col, command=lambda col_ = col: self.treeview_sort_column(self.tv1, col_, False))
        
        df_rows = self.df.to_numpy().tolist()
        for row in df_rows:
            self.tv1.insert("", "end", values=row)
    
    def clear_data(self):
        self.tv1.delete(*self.tv1.get_children())


    def treeview_sort_column(self, tv,col, reverse_signal):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        # way of arrange; default value is True
        l.sort(reverse=reverse_signal)
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse_signal))
    
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

        self.button_calculate = tk.Button(self.data_frame, text='Calculate', command=lambda: self.calculate())
        self.button_calculate.pack()
        

        
        self.root.mainloop()
# import geo

process = myGeoprocess()
process.main()