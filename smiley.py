from turtle import *

hideturtle()  # Hides the turtle (triangle)

pensize(2)
begin_fill()
fillcolor("#E8BEAC")
circle(100)
end_fill()  # For outer circle

penup()  # stop drawing
goto(-40, 110)
pendown()  # start drawing
begin_fill()    # Left eye
fillcolor("white")
circle(20)
end_fill()
penup()

goto(-40, 110)  # For pupil
pendown()
begin_fill()
fillcolor("#0E27FF")
circle(10)
end_fill()
penup()

pensize(0)
goto(-40, 112.5)  # For iris
pendown()
begin_fill()
fillcolor("#061275")
circle(5)
end_fill()
penup()

pensize(2)  # For right eye
goto(40, 110)
pendown()
begin_fill()
fillcolor("white")
circle(20)
end_fill()

goto(40, 110)  # For pupil
pendown()
begin_fill()
fillcolor("#0E27FF")
circle(10)
end_fill()
penup()

pensize(0)  # For iris
goto(40, 112.5)
pendown()
begin_fill()
fillcolor("#061275")
circle(5)
end_fill()
penup()

"""
pensize(5)  # For Eyebrows
goto(-15, 140)
color("black")
pendown()
left(90)
circle(27, 180)
penup()
right(270)
"""

pensize(3)  # For Nose
color("black")
goto(0, 115)
pendown()
right(60)
forward(30)
right(120)
forward(30)
right(120)
forward(30)

pensize(3)  # For Smile
color("black")
fillcolor("#FF0253")
penup()
setpos(-60, 75)
pendown()
begin_fill()
right(150)
circle(60, 180)
left(90)
forward(120)
end_fill()
exitonclick()


