from tkinter import *
from time import sleep as zz
from random import choice, randint
import py2exe
version = 1.0


# Vars
operand = ["+", "-", "*", "/"]
eqa = "="
answer = ""
life = "❤️"
hp = 2
for _ in range(hp):
    life += life
chain = 0
wins = 0
losses = 0
job = ""
game_over = False


# ----------------------- Question Machine -------------#
def quest_machine():
    global job
    global answer
    canvas.delete('problem')
    n1 = randint(0, 100)
    n2 = randint(0, 100)
    task = choice(operand)

    if task == "+":
        answer = n1 + n2
    elif task == "/":
        n2 = randint(0, 10)
        job = f"{n1} {task} {n2} {eqa}"
        answer = n1 / n2
        problem = canvas.create_text(340, 400, text=job, fill='blue', font=('Arial', 50, 'bold'), tags='problem')
        window.update()
    elif task == "-" and n2 > n1:
        n2 = randint(0, n1)
        job = f"{n1} {task} {n2} {eqa}"
        answer = n1 - n2
        problem = canvas.create_text(340, 400, text=job, fill='blue', font=('Arial', 50, 'bold'), tags='problem')
        window.update()
    else:
        job = f"{n1} {task} {n2} {eqa}"
        answer = n1 * n2
        problem = canvas.create_text(340, 400, text=job, fill='blue', font=('Arial', 50, 'bold'), tags='problem')
        window.update()


def judge():
    global answer
    global wins
    global losses
    global chain
    global hp
    guess = int(e1.get())
    if guess == answer:
        wins += 1
        chain += 1
        canvas.create_text(75, 30, text=f"{life}", fill='red', font=('Courier', 20, 'bold'))
        canvas.create_text(100, 700, text=f"Chain# {chain} \nWins: {wins} \nLosses: {losses}", fill='orange', font=('Courier', 20, 'normal'))
        quest_machine()
    else:
        hp -= 1
        losses += 1
        chain = 0
        canvas.create_text(75, 30, text=f"{life}", fill='red', font=('Courier', 20, 'bold'))
        canvas.create_text(100, 700, text=f"Chain# {chain} \nWins: {wins} \nLosses: {losses}", fill='orange', font=('Courier', 20, 'normal'))
        quest_machine()


# ------------------------ UI --------------------------#
window = Tk()
window.title("Dalton's Math Mania")

canvas = Canvas(width=800, height=800)
backdrop = PhotoImage(file='mathbg.png')
canvas.create_image(400, 400, image=backdrop)
e1 = Entry(canvas, width=10)
e1.focus()
b1 = Button(canvas, width=10, text='Submit', command=judge)
canvas.create_window(520, 500, window=b1)
canvas.create_window(520, 400, window=e1)
canvas.create_text(75, 30, text=f"{life}", fill='red', font=('Courier', 20, 'bold'))
canvas.create_text(100, 700, text=f"Chain# {chain} \nWins: {wins} \nLosses: {losses}", fill='orange', font=('Courier', 20, 'normal'))
canvas.create_text(730, 790, text=f"Version: {version}", fill='white', font=('Courier', 12, 'bold'))
canvas.grid(column=1, row=1)
quest_machine()


window.mainloop()
