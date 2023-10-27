from turtle import Screen
from paddle import Paddle


# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

# paddle creation
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

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


screen.exitonclick()