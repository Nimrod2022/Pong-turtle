import turtle
from turtle import Turtle, Screen
from pad import Pad
from ball import Ball
import time

STARTING_POSITIONS = [(350, 0), (-350, 0)]

r_pad = Pad(STARTING_POSITIONS[0])
l_pad = Pad(STARTING_POSITIONS[1])

ball = Ball()

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with pad
    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < - 320:
        ball.bounce_x()
        print("contact")

    # When it misses the ball Right pad

    if ball.xcor() > 380:
        ball.reset_position()

    # When it misses the ball Right pad

    if ball.xcor() < - 380:
        ball.reset_position()





screen.exitonclick()
