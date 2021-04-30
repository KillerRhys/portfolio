from turtle import Turtle, Screen
from random import randint

winner = True
colors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple']
ninjas = []
screen = Screen()
screen.setup(width= 500, height= 400)
bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color: ")
start_x = -240
start_y = -175


def begin_setup():
    global start_x
    global start_y
    for item in colors:
        new_turtles = Turtle(shape = 'turtle')
        new_turtles.color(item)
        new_turtles.pu()
        new_turtles.goto(start_x, start_y)
        ninjas.append(new_turtles)
        start_y += 70


def race():
    global winner
    global ninjas
    global bet
    if bet:
        winner = False
    while not winner:
        for turtle in ninjas:
            if turtle.xcor() > 230:
                winner = True
                win_color = turtle.pencolor()
                if win_color == bet:
                    print(f"You've won!, The {win_color} is the winner!")
                else:
                    print(f"You didn't win, {win_color} took the gold!")
            rando = randint(0, 10)
            turtle.forward(rando)



begin_setup()
race()
screen.exitonclick()