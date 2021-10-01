
# Visualization of Bridges in Pittsburgh
最终目的:

可交互的匹兹堡桥梁地图 可以体现哪些桥梁需要维修

TODO:
1. csv数据转成shapefile或者geojson
2. 找一个匹兹堡的地图
3. 需要一个GUI界面
4. 怎么算重要程度

## 1. Introduction

### problem definition 
Pittsburgh is also called the ‘The City of Bridge’. However, the current conditions of Pittsburgh’s bridges are not satisfactory. Overall, 29% of urban bridges are assessed as structurally deficient (SD), and 29% of bridges are in the condition of functionally obsolete (FO) [1]. The program will visualize the situation of bridges in Pittsburgh based on GIS(Geographic Information System) to help the decision-makers to intuitively observe the damage situation of bridges in different areas so as to optimize the maintenance plan of the bridges.

### solution methods
transform csv data to shapeflie data

use a GUI to process the bridge data

AHP method to evaluate the importance


### what I need to learn

1. how to process the preliminary data(csv to shapefile)
2. a GUI to interact with users
3. a method to calculate the importance of bridge system
4. Geopandas

## 2. Background

### 2.1 Pre-process the data
Compared with general data, GIS data combines the attributes and coordinate information of elements. One common type of GIS data is 'Vector Data'. It uses X, Y, and Z coordinates to represent map graphics (etc. river and lake) or geographic entity locations(etc. houses and bridges).

This project will contain two data sets, a data set showing a map of Pittsburgh and a data set showing Pittsburgh Bridges. The preliminary date set of Pittsburgh Bridges contains some useless information such as... , and the two date sets have different data fomrats. Thus, before we process the data, we need to use an uniform data type to clear and store the data.

### 2.2 Geopandas
Geopandas is an open-source project to help process the geographic data[2]. Geopandas provides excellent read and write support for shapefiles. It allows users direct manipulation of geometry data, making it easier to manipulate geographic data in Python.

Geopandas has an unique data sturcture called geopandas.GeoDataFrame, a subclass of pandas.DataFrame. A DataFrame is a tabular data structure that contains an ordered set of columns.It has both row and column indexes, and can be thought of as a dictionary of Series( an unique column in pandas) with a common index. GeoDataFrame can store geometry columns and perform spatial operations.

Therefore, your GeoDataFrame is a combination of Series with your data (numerical, boolean, text etc.) and GeoSeries with geometries (points, polygons etc.). You can have as many columns with geometries as you wish, there’s no limit typical for desktop GIS software.

### 2.2 Compute something using the data
Algorithm


Data Structures
GeoSeries

Flow/transformation of data


solution method (algorithm, data needs, ...)
what you need to learn in order to execute your project
what you plan to deliver in your final report 

## 3. Program Design
Show your preliminary design by creating a flow chart of the major modules with the corresponding data and logic flow.  You can generate this by hand or use one of the many charting applications that are available.


## Reference
[1] https://infobridge.fhwa.dot.gov/Page/infobridge_documentation

[2] https://geopandas.org/about.html
