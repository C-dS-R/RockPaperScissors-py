from random import randrange #Required for randomizing machine choice
from choiceValTrtFuncs import *
from roundExecFuncs import *

#choices are stored here ('-1' for empty)
usrChoice = -1 #user choice
mchChoice = -1 #machine choice

# Executes from here
while(True):
    # Asks for user to choose a move
    # If choice is invalid, it will ask once again untill user inputs a valid choice
    while(usrChoice==-1): usrChoice = getChoice() #reminder that getChoice() already calls treatChoice() inside it (which already prints the user choice)

    print("Adversary choice: ")
    mchChoice = randrange(1,4,1)
    # Treats and prints the machine's choice
    mchChoice = checkNumChoice(mchChoice) 

    # EXECUTES ROUND AND ANNOUNCES WIN/LOSS
    print("""
""" + doRound(usrChoice,mchChoice)) #With a line break

    # RESETS CHOICES FOR NEXT ROUND
    usrChoice=-1
    mchChoice=-1