import turtle
from turtle import Turtle, Screen

# Setup screen

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


pad = Turtle(shape="square")
pad.color("white")
pad.penup()
pad.shapesize(stretch_wid=5, stretch_len=1)
pad.speed("fastest")
pad.setposition(x=350, y=0)

# Define Pad movement
def go_up():
    new_y = pad.ycor() + 20
    pad.goto(pad.xcor(), new_y)

def go_down():
    new_y = pad.ycor() - 20
    pad.goto(pad.xcor(), new_y)


screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_on = True

while game_on:
    screen.update()



screen.exitonclick()

