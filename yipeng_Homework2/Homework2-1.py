'''
Name: Yi Peng AndrewID: yipeng Homework: 2-1 coursenumber: 12746 
''' 
 
import turtle
import keyword

def drawTriangle():
    length = int(input("please enter the length"))
    MyTurtle = turtle.Turtle()
    MyTurtle.fd(length)
    MyTurtle.rt(120)
    MyTurtle.fd(length)
    MyTurtle.rt(120)
    MyTurtle.fd(length)
    MyTurtle.rt(60)
    turtle.done()

drawTriangle()