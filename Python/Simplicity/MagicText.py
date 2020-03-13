"""	Magic Text Editor
	Coded by TechGYQ
	2020.03.13 OC;
	DESC: Tool used to build words.json game dictionary with over 125K words in 25 mins. 
"""

import sys, time, os

def cuts():
    with open(r"/Users/Undea/Documents/words.txt") as f:
        string = f.read()
        print('Please select char number to cut!:')
        n=int(input())
        string2=[string[i:i+n] for i in range(0, len(string), n)]
        with open('/Users/Undea/Documents/words2.txt', 'w') as f:
            for item in string2:
                f.write("%s\n" % item)
    print("step 1 complete")



def xfer():
    with open(r"/Users/Undea/Documents/words2.txt") as f:
        content = f.read().upper().splitlines()
        string1 = '{"word": "'
        string2 = '"},'
        content2 = [string1 + x + string2 for x in content]
        with open('/Users/Undea/Documents/words3', 'w') as f:
            for item in content2:
                f.write("%s\n" % item)
    print('Finshed Tasks')
