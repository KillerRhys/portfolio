"""Gandohar Adventures!
    Coded by TechGYQ
    OC 2019.12.15-18:00
"""
# Calls
import sys, random, os, time, json

# Vars
inv = []
Bonz = 0
cxp = 0
mxp = 100
bxp = 0
level = 1
maxhp = 20
hp = maxhp
maxmp = 5
mp = maxmp
strength = 5
vitality = 4
wisdom = 4
agility = 4
luck = 2


# Level Up
def levelup():
    global cxp
    global mxp
    global bxp
    global level
    global maxhp
    global hp
    global maxmp
    global mp
    global strength
    global vitality
    global wisdom
    global agility
    global luck

    if cxp >= mxp:
        level += 1
        cxp = 0 % bxp
        mxp += 100
        maxhp += random.randint(1, 9)
        hp = maxhp
        maxmp += random.randint(1, 9)
        mp = maxmp
        strength += random.randint(0, 3)
        vitality += random.randint(0, 3)
        wisdom += random.randint(0, 3)
        agility += random.randint(0, 3)
        luck += random.randint(0, 1)

    else:
        cxp = cxp + bxp


# item class
class items:
    def __init__(self, id, name, desc, tree, use, count, power, value):
        self.id = id
        self.name = name
        self.desc = desc
        self.tree = tree
        self.use = use
        self.count = count
        self.power = power
        self.value = value

        with open("items.txt", "r") as data_file:
            json_data = data_file.read()
            itemlist = json.loads(json_data)

    # def itemuse(self):


# Monster Class
class monsters():
    def __init_(self, id, name, hp, mp, atk, arm, move1, move2, move3, move4, rbonz, rxp, loottable):
        self.id = id
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.arm = arm
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.rbonz = rbonz
        self.rxp = rxp
        self.loottable = loottable


