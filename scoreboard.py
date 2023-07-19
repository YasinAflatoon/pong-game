from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 210)
        self.l_score = -1
        self.r_score = -1
        self.update(1, 1)

    def update(self, r_scored, l_scored):

        if r_scored == 1:
            self.r_score += 1

        if l_scored == 1:
            self.l_score += 1

        self.clear()
        self.write(
                arg=f"{self.l_score}     {self.r_score}",
                move=False,
                align="center",
                font=("Digital-7", 70, "normal")
        )
