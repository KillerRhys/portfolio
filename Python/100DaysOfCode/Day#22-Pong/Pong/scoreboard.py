from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.ht()
        self.rp_score = 0
        self.lp_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lp_score, align='center', font=('Arial', 70, 'normal'))
        self.goto(100, 200)
        self.write(self.rp_score, align='center', font=('Arial', 70, 'normal'))

    def p1_point(self):
        self.rp_score += 1
        self.update_scores()

    def p2_point(self):
        self.lp_score += 1
        self.update_scores()
