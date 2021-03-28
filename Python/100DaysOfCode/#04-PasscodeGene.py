#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

picked_letters = []
picked_symbols = []
picked_numbers = []
base_work = []
easy_mode = []
pass1 = ""
hard_mode = []
pass2 = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

while nr_letters >= 1:
    r = random.randint(0, 51)
    picked_letters.append(letters[r])
    nr_letters -= 1

while nr_symbols >= 1:
    r = random.randint(0, 8)
    picked_symbols.append(symbols[r])
    nr_symbols -= 1

while nr_numbers >= 1:
    r = random.randint(0, 9)
    picked_numbers.append(numbers[r])
    nr_numbers -= 1

base_work = picked_letters + picked_symbols + picked_numbers
easy_mode = base_work
pass1 = "".join(easy_mode)
hard_mode = random.shuffle(base_work)
pass2 = "".join(base_work)

#pass2 = "".join(hard_mode)
#easy_mode = picked_letters + picked_symbols + picked_numbers
print(f"Your easy password is: {pass1}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print(f"Your secure password is: {pass2}")
