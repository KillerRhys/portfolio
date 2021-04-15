from turtle import Turtle
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_AREA = [(0, 0), (0, -20), (0, -40)]

class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in START_AREA:
            self.shed_skin(position)

    def shed_skin(self, position):
        new_snek = Turtle(shape='square')
        new_snek.pu()
        new_snek.goto(position)
        new_snek.color('yellow')
        self.parts.append(new_snek)

    def extend(self):
        self.shed_skin(self.parts[-1].position())

    def move(self):
        for snake_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[snake_num - 1].xcor()
            new_y = self.parts[snake_num - 1].ycor()
            self.parts[snake_num].goto(new_x, new_y)
        self.parts[0].forward(DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)