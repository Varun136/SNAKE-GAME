from turtle import *

CO_ORDINATES = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for n in CO_ORDINATES:
            self.add_segment(n)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_cord = self.segments[segment - 1].xcor()
            y_cord = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cord, y_cord)
        self.head.forward(20)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def add_segment(self,position):
        snake = Turtle()
        snake.shape("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def reset(self):
        for n  in self.segments:
            n.goto(1000,1000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]