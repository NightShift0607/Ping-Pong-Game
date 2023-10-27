from turtle import Turtle
DIST = 20


class Paddle:
    def __init__(self,xcor,ycor):
        self.xcor = xcor
        self.ycor = ycor
        self.paddle = Turtle("square")
        self.create_paddle()
    
    
    def create_paddle(self):
        self.paddle.setheading(90)
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_len=5,stretch_wid=1)
        self.paddle.goto(self.xcor,self.ycor)
    
    
    def up(self):
        self.paddle.forward(DIST)
    
    
    def down(self):
        self.paddle.backward(DIST)