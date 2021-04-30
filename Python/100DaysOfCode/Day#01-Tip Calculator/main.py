def amt():
    print("Welcome to the tip calculator! ")
    bill = float(input("What is the bill amount? $"))
    party = int(input("How many people to split between? "))
    tip = int(input("How much tip would you like to give? 10, 12 or 15%? "))
    total = tip / 100 * bill + bill
    split = round(total / party, 2)
    print(f"Bill Total:${total} \nPer Person:${split}")

    aga = input("Calculate again? (y)es (n)o? ")

    if aga == 'y':
        amt()

    else:
        quit()


amt()
