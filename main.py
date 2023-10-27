from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


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


# Score Creation
scoreboard = Scoreboard()


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
    sleep(ball.ball_speed)
    ball.move_ball()
    
    # ball bouncing from top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # ball bounces off the right and left paddle
    if r_paddle.paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # misses right paddle
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
    
    # misses left paddle
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
    
    if scoreboard.r_score == 10:
        flag = False
        scoreboard.r_won()
    
    if scoreboard.l_score == 10:
        flag = False
        scoreboard.l_won()


screen.exitonclick()