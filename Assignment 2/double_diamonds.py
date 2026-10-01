# Program to create a graph of two diamonds by using the functions in Turtle graphics.

import turtle

SIDE_LENGTH = 150

COLOR = "Black"

turtle.setup(500,600)

turtle.hideturtle()
turtle.fillcolor(COLOR)

# Left-Side Diamond

turtle.begin_fill()
turtle.left(45)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.end_fill()

#Right-Side Diamond

turtle.begin_fill()
turtle.left(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.end_fill()

turtle.done()