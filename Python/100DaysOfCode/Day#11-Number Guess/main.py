""" Number Guess
    Coded by TechGYQ
    www.mythosworks.com
    OC:2021.04.03-1442 """

#imports
import random
from art_book import numgemu_logo as logo

#Vars
number = 0
guess = 0
lives = 5
game_over = False

#Funcs
def randonum():
    """Grabs a random int"""
    global number
    number = random.randint(1, 100)

def try_again():
    """Restarts game if true"""
    again = input("Want to play again? 'y' or 'n'? ")
    if again == 'y':
        randonum()
        game_loop()
    else:
        quit()


def game_loop():
    """Main game loop"""
    global lives
    global guess
    randonum()
    print(logo)
    print("I've got a number in mind try to guess it!")
    diff = input("Type 'e' for easy or 'h' for hard ")
    if diff == 'e':
        lives = 10
    elif diff == 'h':
        lives = 5
    else:
        print("Please select a valid choice!")

    while lives > 0 and game_over == False:
        guess = int(input("Pick a number: "))
        if guess == number:
            print(f"Wow it was {number}! Are you psychic?")
            try_again()

        else:
            if guess > number and lives > 1:
                lives -= 1
                print(f"Nope thats too high! Only {lives} attempts left!")
            elif guess < number and lives > 1:
                lives -= 1
                print(f"Nada thats too low! Only {lives} attempts left!")
            elif lives == 1:
                print("Uh-oh you've ran out of guesses!")
                try_again()



game_loop()
