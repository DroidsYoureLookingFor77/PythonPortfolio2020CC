import turtle

from random import randint

#Sun turtle
u = turtle.Pen()
u.shape("turtle")
u.color("yellow")
u.hideturtle()
u.up()
u.left(90)
u.forward(300)
u.circle(80)



#Wall turtle
x = turtle.Pen()
x.shape("turtle")
x.color("blue")

#Walls
for i in range(4):
    x.forward(150)
    x.left(90)

#Roof turtle
z = turtle.Pen()
z.shape("turtle")
z.color("black")

#Roof
z.left(90)
z.up()
z.forward(150)
z.left(90)
z.forward(20)
z.right(180)
z.down()
z.forward(190)
z.left(135)
z.forward(135)
z.left(90)
z.forward(135)

#Door and window turtle
y = turtle.Pen()
y.shape("turtle")
y.color("green")

#Door
y.up()
y.forward(20)
y.down()
y.left(90)
y.forward(60)
y.right(90)
y.forward(40)
y.right(90)
y.forward(60)
y.up()
y.right(90)
y.forward(5)
y.right(90)
y.forward(30)
y.down()
y.dot(size = 5)
y.up()
y.right(180)
y.forward(30)
y.down()
y.left(90)
y.forward(5)
y.right(90)

#Windows
y.up()
y.left(90)
y.forward(30)
y.left(90)
y.forward(30)
y.down()
for i in range(4):
    y.forward(40)
    y.right(90)
y.up()
y.forward(70)
y.down()
for i in range(4):
    y.forward(40)
    y.right(90)
y.up()
y.left(90)
y.forward(70)
y.right(90)
y.down()
for i in range(4):
    y.forward(40)
    y.right(90)

#Move-in turtles
    
#Black
z.up()
z.left(135)
z.forward(60)
z.right(90)
z.forward(120)
z.hideturtle()
z.left(180)
z.forward(80)
z.showturtle()

#Blue
x.up()
x.forward(40)
x.left(90)
x.forward(30)
x.hideturtle()
x.right(90)
x.forward(70)
x.left(90)
x.forward(10)
x.showturtle()

#Green
y.up()
y.right(90)
y.forward(20)
y.right(90)
y.forward(60)
y.hideturtle()
y.left(180)
y.forward(70)
y.right(90)
y.forward(70)
y.left(90)
y.showturtle()
