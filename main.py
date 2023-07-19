import time
from turtle import Screen
from scoreboard import ScoreBoard
from ball import Ball
from stick import Stick
from pitch import Pitch

sc = Screen()

sc.bgcolor("black")
sc.setup(width=1000, height=600)
sc.title("Pong!")
sc.tracer(0)

pitch = Pitch()
board = ScoreBoard()
ball = Ball()
r_stick = Stick((480, 0))
l_stick = Stick((-490, 0))

sc.listen()
sc.onkeypress(r_stick.up, "Up")
sc.onkeypress(r_stick.down, "Down")
sc.onkeypress(l_stick.up, "q")
sc.onkeypress(l_stick.down, "a")

game_on = True

while game_on:
    ball.move()
    sc.update()
    time.sleep(ball.move_speed)

    if (ball.xcor() <= -465 and ball.distance(l_stick) < 50) or (ball.xcor() >= 460 and ball.distance(r_stick) < 50):
        ball.reflect()
        ball.move_speed *= 0.9
    elif ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    elif ball.xcor() >= 490 or ball.xcor() <= -490:
        if ball.xcor() > 0:
            board.update(0, 1)
        else:
            board.update(1, 0)
        ball.home()
        ball.move_speed = 0.1


sc.exitonclick()
