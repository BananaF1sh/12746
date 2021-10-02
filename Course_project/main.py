import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

bridges = pd.read_csv("Course_project\PittsburghBridges.csv")
bridge_geo = gpd.GeoDataFrame(bridges)

map = gpd.GeoDataFrame.from_file("Course_project\PittsburghBridges.csv")
print(map)

points = gpd.GeoDataFrame(bridges,geometry=gpd.points_from_xy(bridges.longitude, bridges.latitude))
print(points.head())
points.plot()
plt.show()