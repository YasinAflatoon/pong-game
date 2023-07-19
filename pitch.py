from turtle import Turtle


class Pitch(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.color("white")
        self.pensize(5)
        self.goto(0, -300)
        self.left(90)

        for _ in range(10):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
