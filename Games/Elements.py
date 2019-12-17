# Elements by Atomsk 2015.06.03 R1; 2015.06.03-15:30 R2; 2015.06.06-0:25 R3;

# ::Call Functions::
from random import choice
import random
import time

# ::Define Variables::
HP = 100
HP2 = 100
Score = 0
Wins = 0
Losses = 0
Potion = 1


# ::Define Play Again::
def playAgain():
        gameIsDone = True
        print('Want to try again young mage? (yes or no)')
        return input().lower().startswith('y')

# ::Intro::
print("Welcome young one! These old bones aren't what they once were....")
time.sleep(2)
print("I'm looking for a young apprentice. Would you be interested...Er what did you say your name was?")
print()
print('Please enter your name.')
myName = input()
time.sleep(2)  
print('Well '+ myName +' Would you like to be a mage someday?!')
print()
print('Press enter to continue.')
input()
print('Then listen well as I explain the way of the Elements.')
print('Fire -> Earth')
print('Earth -> Wind')
print('Wind -> Water')
print('Water -> Fire')
print()
print('Press enter to continue.')
input()
print('An effective attack will result in a critical hit doing double damage, However the same rules apply to you.')
print()
print('Ok let us begin your training. Defeat me if you can! eheheheheh')
print()
print('Press enter to continue.')
input()

# ::Game::
print('Elements')
gameIsDone = False

while True:
        print(myName+"'s Health:"+str(HP)+"    Wizard's Health:"+str(HP2))
        print('Wins:'+str(Wins)+' Losses:'+str(Losses))
        print()

        FIRE = 1
        EARTH = 2
        WIND = 3
        WATER = 4

        cpu = choice((FIRE, EARTH, WIND, WATER))
        player_one = input('-> FIRE, EARTH, WIND or WATER? ')

        if str(player_one).upper() == 'FIRE':
            player_one = 1
        elif str(player_one).upper() == 'EARTH':
            player_one = 2
        elif str(player_one).upper() == 'WIND':
            player_one = 3
        elif str(player_one).upper() == "WATER":
            player_one = 4    
        else:
            print('What the heck did you pick!?  Pick a valid option!')

        if(cpu == FIRE)and(player_one == FIRE):
            print('The flames consume each other!')
            print()
        elif(cpu == FIRE)and(player_one == EARTH):
            print("The Wizards fire razes your earth!")
            print()
            HP = HP - 20
        elif(cpu == FIRE)and(player_one == WIND):
            print('In a mass of flaming wind you both are hit!')
            print()
            HP = HP - 10
            HP2 = HP2 - 10
        elif(cpu == FIRE)and(player_one == WATER):
            print('Your waves douse the flames.. and the wizard!')
            print()
            HP2 = HP2 - 20
        elif(cpu == EARTH)and(player_one == FIRE):
            print('Your flames raize the wizards world!')
            print()
            HP2 = HP2 - 20
        elif(cpu == EARTH)and(player_one == EARTH):
            print('Boulders collide and a dust cloud envelopes both magi!')
            print()
        elif(cpu == EARTH)and(player_one == WIND):
            print('The conjured mountains stop your storm!')
            print()
            HP = HP - 20 
        elif(cpu == EARTH)and(player_one == WATER):
            print('Both magi are consumed!')
            print()
            HP = HP - 10
            HP2 = HP2 - 10
        elif(cpu == WIND)and(player_one == FIRE):
            print('A fiery storm forms around you both!')
            print()
            HP = HP - 10
            HP2 = HP2 - 10
        elif(cpu == WIND)and(player_one == EARTH):
            print("Your conjured mountains stop the wizard's storm")
            print()
            HP2 = HP2 - 20
        elif(cpu == WIND)and(player_one == WIND):
            print('A hurricane forms and fades!')
            print()
        elif(cpu == WIND)and(player_one == WATER):
            print('The gales turn your waves upon you!')
            print()
            HP = HP - 20
        elif(cpu == WATER)and(player_one == FIRE):
            print('The floods swallow your flames!')
            print()
            HP = HP - 20
        elif(cpu == WATER)and(player_one == EARTH):
            print('A mudslide forms and takes you both!')
            print()
            HP = HP - 10
            HP2 = HP2 - 10
        elif(cpu == WATER)and(player_one == WIND):
            print('You force the waves back on the wizard!')
            print()
            HP2 = HP2 - 20
        elif(cpu == WATER)and(player_one == WATER):
            print('The torrents collide leaving a heavy mist!')
            print()
            
        
        # Check if the player has won
        if HP2 <= 0:
                print('You have bested the wizard!')
                gameIsDone = True
                Wins = Wins + 1

        elif HP <= 0:
                print('You have been defeated!')
                gameIsDone = True
                Losses = Losses + 1

        # Ask if they want to play again.
        if gameIsDone:
           if playAgain():
                   HP = 100
                   HP2 = 100
                   gameIsDone = False
                   print()
           else:
                print('Thanks for playing!')
                print()
                break

        
