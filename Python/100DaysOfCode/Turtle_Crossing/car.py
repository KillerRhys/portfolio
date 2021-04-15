from turtle import Turtle
from random import choice, randint
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'silver', 'pink']
speeds = [5, 10, 15, 20, 25]
INI_MOVE = 5
FASTER = 10


class Car:

    def __init__(self):
        self.mobs = []

    def make_traffic(self):
        build = randint(1, 6)
        if build == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            new_car.color(choice(colors))
            rando_y = randint(-250, 250)
            new_car.goto(300, rando_y)
            self.mobs.append(new_car)

    def drive(self):
        for mob in self.mobs:
            mob.bk(INI_MOVE)

    def go_fast(self):
        for mob in self.mobs:
            mob.bk(FASTER)
