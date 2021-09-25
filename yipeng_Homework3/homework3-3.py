'''
Name: Yi Peng AndrewID: yipeng Homework: 3-3 coursenumber: 12746 
''' 

# Show the coordinates of bridges in the dictionary
def printMyGeo(GeoData):
    for key, value in GeoData.items():
        print(f"The No.{key} bridge is located in {value}")

# some samples of bridges
GeoID = {1:[-8898095.848, 4921740.399],
        2:[-8896177.146, 4926460.976],
        3:[-8895425.294, 4934083.524],
        4:[-8902593.49, 4932427.281],
        5:[-8900032.251,4928115.483]}

printMyGeo(GeoID)