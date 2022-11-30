from turtle import Turtle, Screen

POS = [(-40, 0), (-20, 0), (0, 0)]
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


class Snake:

    def __init__(self):
        self.s_body = []
        self.create_s()
        self.head = self.s_body[0]

    def add(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.s_body.append(segment)

    def create_s(self):
        for _ in POS:
            self.add(_)

    def grow(self):
        self.add(self.s_body[-1].position())

    def move(self):
        for _ in range(len(self.s_body) - 1, 0, -1):
            new_x = self.s_body[_ - 1].xcor()
            new_y = self.s_body[_ - 1].ycor()
            self.s_body[_].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset_s(self):
        for _ in self.s_body:
            _.goto(1000, 1000)
        self.s_body.clear()
        self.create_s()
        self.head = self.s_body[0]
