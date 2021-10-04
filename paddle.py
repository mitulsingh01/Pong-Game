from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def goUp(self):
        DirY = self.ycor() + 20
        self.goto(self.xcor(), DirY)

    def goDown(self):
        DirY = self.ycor() - 20
        self.goto(self.xcor(), DirY)