""" Higher/Lower
    Coded by TechGYQ
    www.mythosworks.com
    OC:2021.04.05-2044"""

import random
from art import *
from time import sleep as zz
from game_data import data as question
from replit import clear

#vars
a = {}
b = {}
wins = 0
winner = {}


#Funcs
def tryagain():
    """Asks the player if they want to play again."""
    global wins
    again = input("Want to play again? (y)es or (n)o ").lower()
    if again == "yes" or "y":
        wins = 0
        clear()
        game_loop()
    elif again == "no" or "n":
        exit()
    else:
        print("I'm sorry I don't understand that")
        tryagain()

def contestants():
    """Randomly selects our challengers"""
    global a
    global b
    global wins
    if wins > 0:
        a = winner
        b = random.choice(question)
        return a, b
    else:
        a = random.choice(question)
        b = random.choice(question)
        return a, b


def game_loop():
    game_over = False
    global a
    global b
    contestants()
    global winner
    global wins
    guess = ""
    while game_over != True:
        print(logo)
        print(f"Your current streak is {wins} long!")
        print(f"\n A:{a['name']}, is a {a['description']} from {a['country']}\n")
        print(vs)
        print("\n")
        print(f"B:{b['name']}, is a {b['description']} from {b['country']}\n \n")
        guess = input(f"Who is higher? A:{a['name']} or B:{b['name']}? ").lower()
        if guess == "a" and a['follower_count'] > b['follower_count']:
            wins += 1
            winner = a
            print(f"Thats correct {a['name']} has {a['follower_count']} followers!")
            zz(3)
            clear()
            game_loop()

        elif guess == "a" and a['follower_count'] < b['follower_count']:
            print(f"Nope! {a['name']} has {b['follower_count'] - a['follower_count']} million less than {b['name']} your final streak was {wins}")
            tryagain()

        elif guess == "b" and a['follower_count'] < b['follower_count']:
            wins += 1
            winner = b
            print(f"Thats correct {b['name']} has {b['follower_count']} followers!")
            zz(3)
            clear()
            game_loop()

        elif guess == "b" and a['follower_count'] > b['follower_count']:
            print(f"Nope! {b['name']} has {a['follower_count'] - b['follower_count']} million less than {a['name']} your final streak was {wins}")
            tryagain()

        else:
            print("I'm sorry I don't recognize that input... try again?")
            guessing()

game_loop()
