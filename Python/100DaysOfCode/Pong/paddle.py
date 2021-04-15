from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.player = player
        if player == 1:
            self.goto(350, 0)
        else:
            self.goto(-350, 0)
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.pu()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
