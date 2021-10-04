from turtle import Turtle, Screen, width
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen =  Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

rPaddle = Paddle((350, 0))
lPaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(lPaddle.goUp, "w")
screen.onkey(lPaddle.goDown, "s")
screen.onkey(rPaddle.goUp, "Up")
screen.onkey(rPaddle.goDown, "Down")

gameOn = True
while gameOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if ball.distance(rPaddle) < 50 and ball.xcor() > 320  or  ball.distance(lPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.lPoint()
    
    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.rPoint()

 
screen.exitonclick()