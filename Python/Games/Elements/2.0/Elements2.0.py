""" Elements 2.0
    Coded by TechGYQ
    MythosWorks(www.mythosworks.com)
    OC:2019.12.19:19:56
"""

# ::Calls::
import time, sys, os
from random import *

#:: Global Variables ::
mentor0 = "Old Man: "
mentor = "Merwin: "
char = ""

#:: Classes ::
class Player():
    def __init__(self, name, level, cxp, nxp, hp, maxhp, atk, arm, wins, losses, draws, bonz, potions, pcap, progress):
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
        self.progress = progress



class Monster():
    def __init__(self, name, hp, atk, arm, bonz, xp):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm
        self.bonz = bonz
        self.xp = xp


#:: Methods ::
def save():
    




def tuts():
    print(mentor + "Listen well young " + char + " I'll teach you a few base spells and their effectiveness.")
    time.sleep(2)
    print("")
    print(mentor + "Firstly I'll give you these four orbs. They contain the powers of Fire, Earth, Wind, and Water.")
    time.sleep(1)
    print("")
    print("Merwin hands over four multi-colored orbs")
    time.sleep(2)
    print(mentor + "The ebb and flow of nature is now at your command. Fire eats the Earth while the Earth bars the Winds. Wind rakes the Waters who douse the Fires..." + "\n")
    time.sleep(5)
    print(mentor + "If you remember the type effectiveness you can deal double damage to any foe you meet young one.\n")
    time.sleep(2)
    print(mentor + "Okay " + char + " Let's try this out... will you battle me?! (yes or no) \n")
    a = input().lower()
    if a == "yes":
        print("Code this fight idjit!")
    else:
        exit()



def playAgain():
    gameOver = True
    print("Want to try your luck again young mage? (yes or no) ")
    return input().lower().startswith("y")

def intro():
    global char
    print("You awake in a dark room. There is a slow drip of water in the distance. Before you in a gnarled old man." + '\n' + "Old man: Hello child. It's not oft one of your kind finds themselves here..")
    time.sleep(4)
    print("")
    print(mentor0 + "I dare say it's been a few millinea since I've had a visitor!" + '\n' + "You feel the ground beneath you tremble as the cavern calls out a hallowed moan")
    time.sleep(4)
    print("")
    print(mentor0 + "My name is Merwin lad. We haven't much time before the darkness consumes this place")
    time.sleep(2)
    print("")
    print(mentor + "Child in you flows the blood of the Magi. I can sense it!")
    time.sleep(1)
    print(mentor + "Time if of import here, but I shall teach you what I can will you answer the call young hero? (yes or no)")
    a = input().lower()
    time.sleep(2)
    if a == "yes":
        print(mentor + "Good I knew you would accept this quest! Now what is thy name young hero?")
        char = input()
        p1 = Player(char, 1, 0, 100, 50, 50, 5, 4, 0, 0, 0, 100, 1, 2, 1)
        time.sleep(2)
        print(mentor + "Ah " + char + ", Let us begin your training!")
        time.sleep (1)
        tuts()
    else:
        exit()

intro()