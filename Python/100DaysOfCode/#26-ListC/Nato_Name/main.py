import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')

# TODO - Make dict
xlate = {row.letter: row.code for (index, row) in df.iterrows()}


# TODO - list of phonetics
word = input("Please enter your name: ").upper()
xfer = [xlate[letter] for letter in word]
print(xfer)
