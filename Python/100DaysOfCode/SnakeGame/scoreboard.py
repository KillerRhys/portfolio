from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('teal')
        self.pu()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scores()

    def update_scores(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align= 'center', font=('Arial', 30, 'bold'))

    def pnt_up(self):
        self.score += 1
        self.clear()
        self.update_scores()
