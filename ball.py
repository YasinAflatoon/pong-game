import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_speed = 0.09
        self.setheading(random.randint(150, 209))
        if self.heading() > 180:
            self.x_move = -15
            self.y_move = -15
        else:
            self.x_move = -15
            self.y_move = 15


    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= (-1)

    def reflect(self):
        self.x_move *= (-1)
