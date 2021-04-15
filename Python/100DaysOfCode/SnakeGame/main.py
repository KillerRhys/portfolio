from turtle import Screen
from snake import Snake
from time import sleep as zz
from food import Food
from scoreboard import ScoreBoard as pnts

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Sneks On a Plane')
game_over = False
score = 0

snake = Snake()
food = Food()
score = pnts()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while not game_over:
    screen.update()
    zz(0.1)
    snake.move()
    score

    if snake.head.distance(food) < 15: # Tweak, New Food Types / Effects
        food.refresh()
        snake.extend()
        score.pnt_up()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        score.game_over()

    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            game_over = True
            score.game_over()


screen.exitonclick()