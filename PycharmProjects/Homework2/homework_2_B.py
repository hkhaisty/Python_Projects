from graphics import *

win = GraphWin("Homework 2", 200, 200)

yAxis = Line(Point(100, 0), Point(100, 200))
xAxis = Line(Point(0, 100), Point(200, 100))

leftBound = Text(Point(7, 110),"-1")
rightBound = Text(Point(193, 110), "1")

leftBound.draw(win)
rightBound.draw(win)
xAxis.draw(win)
yAxis.draw(win)

x = 1.0
y = 1.0

for i in range(1, 200):
    x = (i - 100)/100
    y = (x*x)
    graph = Point(i, 200-(y*200)-100)
    graph.draw(win)

xAxis.setFill('blue')
yAxis.setFill('blue')

win.getMouse()
