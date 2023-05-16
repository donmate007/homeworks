from turtle import *


# house
shape("turtle")
speed(4)
width(7)
color("green")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

# door

forward(75)
left(90)
begin_fill()
color("blue")
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()

# roof

penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# first window

penup()
begin_fill()
color("yellow")
goto(30,150)
pendown()
left(30)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)


# second window

color("yellow")
penup()
goto(170,150)
pendown()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)

exitonclick()