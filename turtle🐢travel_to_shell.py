import turtle

abhi = turtle.Turtle()
start = turtle.Turtle()

abhi.shape("turtle")
abhi.color("green")
abhi.shapesize(3)
abhi.pencolor("green")
abhi.pensize(8)
abhi.circle(-20)





start.shape("circle")
start.up()
start.color("red")
start.shapesize(3)
start.setposition(130,-390)


dist = 20

for _ in range(28):
  abhi.forward(dist)
  abhi.right(45)
  dist = dist + 10

exit()
