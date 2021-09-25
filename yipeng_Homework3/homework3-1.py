'''
Name: Yi Peng AndrewID: yipeng Homework: 3-1 coursenumber: 12746 
''' 
import math
# From polar coordinates to Cartesian coordinates
def transferCoordinate(r, theta):
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    return x,y

# create some interesting pairs of r and theta
r_list = [-10000,-100,-0.000000001,0.00000001,100,10000]
theta_list = [-10000, -100, -0.00000001, 0.00000001, 100, 10000]
theta = math.pi/3
for i in range(6):
    x,y = transferCoordinate(r_list[i], theta_list[i])
    print(x, y)



