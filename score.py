from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 40, "normal"))

    def point(self):
        self.score += 1
        self.update_score()
