from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update()
        self.hideturtle()
    def update(self):
        self.write(f"Score: {self.score}",align="center",font=('Arial', 20, 'normal'))
    def increase(self):
        self.score +=1
        self.clear()
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Score: {self.score}",align="center",font=('Arial', 20, 'normal'))
