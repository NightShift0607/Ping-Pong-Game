from turtle import Screen, Turtle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong Game")
screen.tracer(0)


paddle = Turtle("square")
paddle.setheading(90)
paddle.penup()
paddle.color("white")
paddle.shapesize(stretch_len=5,stretch_wid=1)
paddle.goto(350,0)

def up():
    paddle.forward(20)

def down():
    paddle.backward(20)

screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")

flag = True
while flag:
    screen.update()

screen.exitonclick()