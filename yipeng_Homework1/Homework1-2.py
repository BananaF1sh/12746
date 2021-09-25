'''
Name: Yi Peng AndrewID: yipeng Homework: 1-2 coursenumber: 12746 
''' 
import math

# print the author's name 'Yi Peng'
def printMyname():
    name = 'Yi Peng'
    print(name)
    return name

#Test functoin
#True if output is Yi Peng
def testFunction():
    exceptName = 'Yi Peng'
    printName = printMyname()
    print(exceptName == printName)

# intialize a variable
a = 100

# Assign a built-in value to variable a
a = math.e

print(a)    

print(type(a))

a_new = math.exp(a)

# print origin value and new value
print(f'The new value is {a_new} and the origin value is {a}')

# Test function
testFunction()  