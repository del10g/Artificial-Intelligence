import turtle
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//200+1)
    t.forward(x)
    t.left(59)