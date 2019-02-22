from graphics import *

win = GraphWin("Homework 2", 200, 200)

yAxis = Line(Point(100, 0), Point(100, 200))
xAxis = Line(Point(0, 100), Point(200, 100))
c = Circle(Point(100, 0), 100)
c.draw(win)

xAxis.draw(win)
yAxis.draw(win)

x = 1.0
y = 1.0

for i in range(1, 50):
    x *= 2.0
    y *= 2.0
    graph = Point(x, y)
    graph.draw(win)

xAxis.setFill('blue')
yAxis.setFill('blue')
c.setOutline('orange')

win.getMouse()
