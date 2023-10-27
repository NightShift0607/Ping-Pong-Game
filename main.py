from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball


# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong Game")
screen.tracer(0)


# paddle creation
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)


# Ball creation
ball = Ball()


# paddle movement
screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")


# gameplay control
flag = True
while flag:
    screen.update()
    sleep(0.1)
    ball.move_ball()
    # ball bouncing from top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()