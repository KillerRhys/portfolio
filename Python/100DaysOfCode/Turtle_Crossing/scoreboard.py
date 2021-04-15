from turtle import Turtle
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.ht()
        self.pu()
        self.color('white')
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-200, 270)
        self.write('Level: ', align='left', font=FONT)
        self.goto(-90, 268)
        self.write(self.level, align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.score_update()

    def go_msg(self):
        self.goto(-200, 0)
        self.write('Game Over!', align='left', font=('Courier', 50, 'normal'))
