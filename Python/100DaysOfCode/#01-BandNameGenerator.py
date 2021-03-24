def bandgene():
    print("Welcome to my band name generator! \n")
    a = input("What city did you grow up in?\n")
    b = input("\nWhat's your pet's name?\n")
    print("\nYour band name could be " + a + " " + b + "!\n")
    c = input("Want to try agian? (y)es or (n)o? \n")
    if c == "y":
        bandgene()
    else:
        quit()
    

bandgene()

