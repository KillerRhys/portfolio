# import only system from os
from os import system, name
import art_book as art
import random
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


auctions = {}

def auction():
    print(art.auction_logo)
    name = input("Please enter your name.\n")
    bid = float(input("Please enter your bid.\n"))
    for key in auctions:
                if key in auctions:
                    name = name + random.randint(0,99)
                    auctions[name] = bid
                else:
                    auctions[name] = bid
    #TODO - infinite loop here please fix!!!
    again = input("Is there another bidder?\n")
    if again == "yes" or "y":
        auction()
        again = input("Is there another bidder?\n")
    elif again == "no" or "n":
        winner = ""
        high_bid = 0
        for key in auctions:
            if auctions[key] > high_bid:
                winner = key
                high_bid = auctions[key]
            else:
                winner = winner
                high_bid = high_bid
        print(f"{winner}, won with a bid of {auctions[key]}")   


auction()

