from random import choice
from turtle import Turtle, Screen, colormode
crayon_box = [(229, 226, 221), (243, 236, 240), (209, 156, 103), (58, 98, 133), (157, 82, 52), (229, 241, 238), (139, 159, 191), (232, 201, 103), (52, 174, 122), (158, 167, 40), (202, 135, 153), (123, 189, 173), (66, 39, 32), (75, 113, 88), (128, 78, 87), (27, 47, 67), (133, 29, 47), (196, 93, 74), (179, 94, 110), (116, 37, 24), (5, 67, 50), (56, 31, 46), (75, 132, 197), (231, 203, 1), (162, 191, 223), (32, 65, 104), (25, 163, 169), (16, 84, 57), (151, 211, 193), (217, 180, 172), (217, 174, 182), (79, 80, 41), (165, 204, 209), (49, 68, 75)]

colormode(255)
leo = Turtle()
leo.shape('turtle')
leo.speed(0)
leo.pu()

def draw_art():
    x = -622
    y = -510
    for _ in range(10):
        leo.setpos(x, y)
        y += 115
        for _ in range(10):
            leo.dot(30, choice(crayon_box))
            leo.fd(135)
    leo.hideturtle()


draw_art()


screen = Screen()
screen.exitonclick()