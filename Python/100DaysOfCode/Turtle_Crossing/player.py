from turtle import Turtle
POLE_POSITION = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('dodgerblue1')
        self.setheading(90)
        self.pu()
        self.goto(POLE_POSITION)
        self.speed('fastest')

    def move(self):
        new_y = self.ycor() + 20
        self.goto(0, new_y)

    def survive(self):
        self.goto(POLE_POSITION)
