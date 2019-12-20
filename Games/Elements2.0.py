""" Elements 2.0
    Coded by TechGYQ
    MythosWorks(www.mythosworks.com)
    OC:2019.12.19:19:56
"""

# ::Calls::
import time, sys, os
from random import *

#:: Global Variables ::

#:: Classes ::
class Player():
    def __init__(self, name, level, cxp, nxp, hp, maxhp, atk, arm, wins, losses, draws, bonz, potions, pcap):
        self.name = name
        self.level = level
        self.cxp = cxp
        self.nxp = nxp
        self.hp = hp
        self.maxhp = maxhp
        self.atk = atk
        self.arm = arm
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.bonz = bonz
        self.potions = potions
        self.pcap = pcap



class Monster():
    def __init__(self, name, hp, atk, arm, bonz, xp):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm
        self.bonz = bonz
        self.xp = xp


#:: Methods ::
def playAgain():
    gameOver = True
    print("Want to try your luck again young mage? (yes or no) ")
    return input().lower().startswith("y")

def intro():
    print("You awake in a dark room. There is a slow drip of water in the distance. Before you in a gnarled old man." + '\n' + "Old man: Hello child. It's not oft one of your kind finds themselves here..")
    time.sleep(4)
    print("")
    print("Old man: I dare say it's been a few millinea since I've had a visitor!" + '\n' + "You feel the ground beneath you tremble as the cavern calls out a hallowed moan")
    time.sleep(4)
    print("")
    print("Old man: My name is Merwin lad. We haven't much time before the darkness consumes this place")
    time.sleep(2)
    print("")
    print("Merwin: Child in you flows the blood of the Magi. I can sense it!")
    time.sleep(1)
    print("Merwin: Time if of import here, but I shall teach you what I can will you answer the call young hero? (yes or no)")
    a = input()
    if a == "Yes" or "yes" or "y" or "Y":
        print("Merwin: Good I knew you would accept this quest! Now what is thy name young hero?")
        char = input()
        p1 = Player(char, 1, 0, 100, 50, 50, 5, 4, 0, 0, 0, 100, 1, 2)
        print("Merwin: Ah " + p1.name + ", Let us begin your training!")
    else:
        exit()

intro()