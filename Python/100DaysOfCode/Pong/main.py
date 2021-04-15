""" Pong
    Coded by: TechGYQ
    www.mythosworks.com
    OC:2021.04.13-2004 """


from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep as zz


# Vars
game_over = False
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.title('Paddle Ball')
screen.setup(width=800, height=600)

paddle = Paddle(player=1)
paddle2 = Paddle(player=2)
ball = Ball()
score_keeper = Scoreboard()

screen.listen()
screen.onkey(paddle.go_up, 'Up')
screen.onkey(paddle.go_down, 'Down')
screen.onkey(paddle2.go_up, 'w')
screen.onkey(paddle2.go_down, 's')

# Game Loop
while not game_over:
    screen.update()
    ball.move()
    zz(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score_keeper.p2_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score_keeper.p1_point()


screen.exitonclick()
