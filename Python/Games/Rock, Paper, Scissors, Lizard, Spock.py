from random import randint

# RPS
rps = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# scores
w = 0
l = 0
g = 0

# player | cpu
cpu = rps[randint(0,4)]
player = False

# game loop
while player == False:
    player = input("Current score is %s W, %s L, of %s games. Please select a move Rock, Paper, Scissors, Lizard, Spock " % (w, l, g))
    if player == cpu:
        print("You have tied! That is imporbable...")
        g = g + 1
    elif player == "Rock":
        if cpu == "Paper":
            print("You have lost!", cpu, "covers", player)
            l = l + 1
            g = g + 1
        elif cpu == "Spock":
            print(cpu, "Blasted your", player)
            l = l + 1
            g = g + 1
        elif cpu == "Scissors":
            print("You have won! ", player, " smashes", cpu)
            w = w + 1
            g = g + 1
        elif cpu == "Lizard":
            print("You have smashed the", cpu)
            w = w + 1
            g = g + 1
    elif player == "Paper":
        if cpu == "Scissors":
            print("You have lost! ", cpu, " cuts", player)
            l = l + 1
            g = g + 1
        elif cpu == "Lizard":
            print("A ", cpu, " ate you...")
            l = l + 1
            g = g + 1
        elif cpu == "Spock":
            print(cpu, " couldn't handle the truth! ", player, " wins!")
            w = w + 1
            g = g + 1
        elif cpu == "Rock":
            print(cpu, " is covered up... ",)
            w = w + 1
            g = g + 1
    elif player == "Scissors":
        if cpu == "Rock":
            print("You have lost! ", cpu, " smashes ", player)
            l = l + 1
            g = g + 1
        elif cpu == "Spock":
            print("You have lost! ", cpu, "smashes ", player)
            l = l + 1
            g = g + 1
        elif cpu == "Paper":
            print("You have won!", player, "cuts", cpu)
            w = w + 1
            g = g + 1
        elif cpu == "Lizard":
            print("You have won!", player, "cuts", cpu)
            w = w + 1
            g = g + 1
    elif player == "Lizard":
        if cpu == "Rock":
            print("You got smashed by", cpu)
            l = l + 1
            g = g + 1
        elif cpu == "Scissors":
            print("You got snipped by", cpu)
            l = l + 1
            g = g + 1
        elif cpu == "Paper":
            print ("You chowed down on some", cpu)
            w = w + 1
            g = g + 1
        elif cput == "Spock":
            print ("You poisoned", cpu)
            w = w + 1
            g = g + 1
    elif player == "Spock":
        if cpu == "Paper":
            print ("You can't possibly exist", cpu, "says so!")
            l = l + 1
            g = g + 1
        elif cpu == "Lizard":
            print("Gah! a", cpu, "poisoned you!")
            l = l + 1
            g = g + 1
        elif cpu == "Rock":
            print("You blasted that pos", cpu)
            w = w + 1
            g = g + 1
        elif cpu == "Scissors":
            print("Smashed those", cpu)
            w = w + 1
            g = g + 1
    elif player == "Quit":
        exit()
    else:
        print("That is not valid choice! Please try again!")
    player = False
    cpu = rps[randint(0,4)]
