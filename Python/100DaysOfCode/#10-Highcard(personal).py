""" High-Low Card
    Coded by TechGYQ
    www.mythosworks.com
    OC: 2021.04.03-1236 """

import random
from art_book import hl_logo as logo

# Vars
player_chips = 100
game_over = False


# Func
def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def game_loop(card):
    global player_chips
    bid = int(input(f"Care to make a wager? I see you have {player_chips} chips."))
    dealer_card = deal()
    print(f"House lays a {card} on the table")
    new_card = deal()
    guess = input("Type 'h' for high or type 'l' for low. ")
    if guess == "h":
        if new_card > dealer_card:
            player_chips += bid * 2
            print(f" {new_card} is higher than {dealer_card}, You win!")
        else:
            player_chips = player_chips - bid
            print(f" {new_card} was lower than {dealer_card}, You lost!")
        
    elif guess == "l":
            if new_card < dealer_card:
                player_chips = player_chips + bid * 2
                print(f" {new_card} is lower than {dealer_card}, You win!")
            else:
                player_chips = player_chips - bid
                print(f" {new_card} is higher than {dealer_card}, You lost!")

while game_over == False:
    game_loop(deal())

   
