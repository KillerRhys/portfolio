""" Elements 2.0
    Coded by TechGYQ
    MythosWorks(www.mythosworks.com)
    OC:2019.12.19:19:56
"""

# Calls
import time, sys, os
from random import *

# Global Variables
mentor0 = "Old Man: "
mentor = "Merwin: "
char = ""
p1 = None
lootpool = ["Fang Necklace", "Shield Totem", "Coin-purse", "Tome of Ka'mor", "Giant's Goblet", "Hermit's Satchel"]
mobs = ["Merwin", "Young Magi", "Wizard", "Oracle", "Sketchy Caster", "Magic Grunt", "Anei The Fox", "Goose The Destroyer", "Avari The Ageless", "Rhys The Forsaken"]


# Classes
class Player:
    def __init__(self, name, level, cxp, nxp, hp, maxhp, atk, arm, wins, losses, draws, bonz, potions, pcap, loot, progress):
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
        self.loot = loot
        self.progress = progress


class Monster:
    def __init__(self, name, hp, atk, arm, bonz, xp, potion):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm
        self.bonz = bonz
        self.xp = xp
        self.potion = potion


# Methods
def save():
    file = open(p1.name + ".dat", "w+")
    content = [p1.name, p1.level, p1.cxp, p1.nxp, p1.hp, p1.maxhp, p1.atk, p1.arm, p1.wins, p1.losses, p1.draws, p1.bonz, p1.potions, p1.pcap, p1.progress, p1.loot, lootpool]
    for item in content:
        file.write("%s\n" % item)


def load():
    global p1
    global lootpool
    a = input("Please type your characters name...\n")
    try:
        file = open(a + ".dat", "r")
        content = file.readlines()
        p1 = Player(content[0], content[1], content[2], content[3], content[4], content[5], content[6], content[7], content[8], content[9], content[10], content[11], content[12], content[13], content[14], content[15])
        lootpool = content[16]
        time.sleep(1)
        if int(content[14]) == 0:
            stage0()
        elif int(content[14]) == 1:
            stage1()
        else:
            print("Um...we got a problem scotty!")
    except (OSError, IOError) as e:
        print("Couldn't locate that file. Please check your spelling and try again")
        load()


def battle():
    n = int(p1.progress)
    enemy = Monster(mobs[n], int(p1.map), int(p1.atk), int(p1.arm), 50, 50, 1)
    fire = 0
    earth = 1
    wind = 2
    water = 3
    potion = 4


def stage1():
    print(mentor + "Listen well young " + p1.name + " I'll teach you a few base spells and their effectiveness.")
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
    print(mentor + "Okay " + p1.name + " Let's try this out... will you battle me?! (yes or no) \n")
    a = input().lower()
    if a == "yes":
        print("Code this fight idjit!")
    else:
        save()
        exit()


def playAgain():
    gameover = True
    print("Want to try your luck again young mage? (yes or no) ")
    return input().lower().startswith("y")

def stage0():
    global char
    global p1
    global loot
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
        p1 = Player(char, 1, 0, 100, 50, 50, 5, 4, 0, 0, 0, 100, 1, 2, 0, [""])
        time.sleep(2)
        p1.progress = 1
        print(mentor + "Ah " + char + ", Let us begin your training!")
        time.sleep (1)
        save()
        stage1()
    else:
        exit()

load()