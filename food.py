from random import choice
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = choice(range(-280, 280, 20))
        random_y = choice(range(-280, 280, 20))
        self.goto(random_x, random_y)
