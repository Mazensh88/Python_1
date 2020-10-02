def esquare(x):
    # turtle.begin_fill()
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(x)
    # turtle.end_fill()
import turtle
i= int(input("Enter number of squares "))
a = float(input("Enter offset angle for the square "))
turtle.hideturtle()
turtle.speed('fastest')
while i>0:
    if i % 2 ==0:
        turtle.pencolor('#ff0000')
        turtle.fillcolor('#b22222')
        turtle.pensize(4)
    else:
        turtle.pencolor('#000000')
        turtle.fillcolor('#0000ff')
        turtle.pensize(2)
    esquare(a)
    i -= 1
turtle.exitonclick()   
