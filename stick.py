from turtle import Turtle


class Stick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5)
        self.left(90)
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 30)
