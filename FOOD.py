from turtle import *
import random
x=random.randint(-250,250)
y=random.randint(-250,250)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.goto(x,y)

    def refresh(self):
        new_x = random.randint(-290, 290)
        new_y = random.randint(-290, 290)
        self.goto(new_x, new_y)

