from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
    
    
    def move_ball(self):
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.goto(x, y)