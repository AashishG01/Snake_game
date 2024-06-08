from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50,250)


    def add_score(self):
        self.score = self.score + 1
        self.clear()

    def print_score(self):
        self.write(arg=f"score : {self.score}", font=("Arial", 20, "normal"))


class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50, 0)
        self.write(arg="GAME OVER", font=("Arial", 30, "normal"))




