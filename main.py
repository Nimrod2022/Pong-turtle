import turtle
from turtle import Turtle, Screen
from pad import Pad

STARTING_POSITIONS = [(350, 0), (-350, 0)]

r_pad = Pad(STARTING_POSITIONS[0])
l_pad = Pad(STARTING_POSITIONS[1])
# Setup screen

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")

game_on = True

while game_on:
    screen.update()



screen.exitonclick()

