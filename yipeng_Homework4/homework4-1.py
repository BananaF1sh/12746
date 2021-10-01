'''
Name: Yi Peng AndrewID: yipeng Homework: 4-1 coursenumber: 12746 
''' 

import time

# Create a new time class to print the time in format
class Mytime:
    
    def __init__(self):
        self.mytime = time.strftime("%H:%M:%S %d-%m-%Y", time.localtime())
    
    def printTime(self):
        print(self.mytime)

# get the time the program is run
myT = Mytime()
myT.printTime()