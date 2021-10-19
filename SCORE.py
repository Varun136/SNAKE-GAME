from turtle import *

with open("High score.txt") as file:
    high_score = int(file.read())

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.high_score = high_score
        self.write(f"SCORE : {self.score}  HIGH SCORE : {self.high_score}" , align="center" , font=("Aerial",20,"normal"))
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE : {self.score}  HIGH SCORE : {self.high_score}", align="center", font=("Aerial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER \nYOUR SCORE : {self.score}  HIGH SCORE : {self.high_score}", align="center", font=("Aerial", 20, "normal"))

    def update_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("High score.txt",mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0



