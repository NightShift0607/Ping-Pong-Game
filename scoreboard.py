from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()
    
    
    def score_update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    
    
    def r_point(self):
        self.r_score += 1
        self.score_update()
    
    
    def l_point(self):
        self.l_score += 1
        self.score_update()
    
    
    def r_won(self):
        self.goto(0,0)
        self.write("Right Player Won", align="center", font=("Courier", 40, "normal"))
    
    
    def l_won(self):
        self.goto(0,0)
        self.write("Left Player Won", align="center", font=("Courier", 40, "normal"))