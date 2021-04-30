""" Turtle Crossings
    Coded by TechGYQ
    www.mythosworks.com
    OC:2021.04.14(2145) """

# Imports
from time import sleep as zz
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

# Vars
game_over = False
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossings')
screen.tracer(0)
screen.bgcolor('black')
player = Player()
car = Car()

score = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')
while not game_over:
    zz(0.1)
    screen.update()
    score.score_update()

    car.make_traffic()
    car.drive()

    for car.mob in car.mobs:
        if car.mob.distance(player) < 20:
            game_over = True
            score.go_msg()

    if player.ycor() >= 280:
        score.level_up()
        player.survive()
        car.go_fast()

screen.exitonclick()
