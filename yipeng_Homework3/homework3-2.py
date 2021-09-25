'''
Name: Yi Peng AndrewID: yipeng Homework: 3-2 coursenumber: 12746 
''' 
 
# add i numbers 0f 0 to the ith element
def stringOfList(integers):
    s = "["
    for i in range(len(integers)):
        s = s + str(integers[i]) + "." + "0" * (i+1) + ", "
        print(s)
    s = s.rstrip(", ")
    s += "]"
    return s

intgers = [1, 2, 3, 4]
string1 = stringOfList(intgers)
print(string1)
test1 = 1
test1 = float(test1)
print("%.5d", test1)
GeoId = {"1"}