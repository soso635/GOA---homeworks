from turtle import *
#we want to paint a house

#step 1: draw a square
speed(30)
width(3)
color("red")
forward(200)

left(90)

forward (200)

left(90)
forward(200)
left(90)

forward(200)
left(90)
#end of square
#drawing a door

forward(70)
color("yellow")
left(90)

forward(120)
right(90)

forward(60)
right(90)
forward(120)


penup()
goto(200, 200)
pendown()
color("purple")
begin_fill()


right(150)
forward(200)
left(120)
forward(200)
end_fill()



color("red")

left(30)


forward(50)
color("purple")

left(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(25)
right(90)
forward(60)
penup()

goto(200, 150)
pendown()
right(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(25)
left(90)
forward(60)
exitonclick()
