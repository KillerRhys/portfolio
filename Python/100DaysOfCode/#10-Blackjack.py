""" Blackjack V1.0
    Coded by TechGYQ
    www.mythosworks.com
    2021.04.02-2331 """

# Ports
import random
import art_book as arts

# Vars

# Funcs
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(player_total, house_total):
    if player_total == house_total:
        return "Draw!"
    elif house_total == 0:
        return "House has blackjack!"
    elif player_total == 0:
        return "Blackjack!"
    elif player_total > 21:
        return "Bust! House wins!"
    elif house_total > 21:
        return "House busts you win!"
    elif player_total > house_total:
        return "You win!"
    else:
        return "You lose."
        
def play_game():
    print(arts.blackjack_logo)
    player_hand = []
    house_hand = []
    game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        house_hand.append(deal_card())

    while game_over != True:
        player_total = calculate_score(player_hand)
        house_total = calculate_score(house_hand)
        print(f"    Your cards: {player_hand}, current score: {player_total}. ")
        print(f"    House's first card: {house_hand[0]}")

        if player_total == 0 or house_hand == 0 or player_total > 21:
            game_over = True

        else:
            hit = input("Type 'y' for another card, type 'n' to pass: ")
            if hit == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

        while house_total != 0 and house_total <17:
            house_hand.append(deal_card())
            house_total = calculate_score(house_hand)

        print(f"    Your final hand: {player_hand}, final score: {player_total}")
        print(f"    House's final hand: {house_hand}, final score: {house_total}")
        print(compare(player_total, house_total))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
      play_game()

play_game()
