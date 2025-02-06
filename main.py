from random import randrange #Required for randomizing machine choice
from choiceValTrtFuncs import *
from roundExecFuncs import *

# Choices are stored here ('-1' for empty)
player_choice = -1 #user choice
bot_choice = -1 #machine choice

##### Executes from here
while(True):
	# Asks for user to choose _a move
	# If choice is invalid, it will ask once again untill user inputs a valid choice
	while(player_choice==-1): player_choice = user_choice() #reminder that getChoice() already calls treatChoice() inside it (which already prints the user choice)

	#BOT CHOICE
	print("Adversary choice: ")
	bot_choice = randrange(1,4,1)
	choice_echo(bot_choice) # prints the bot's choice

	# EXECUTES ROUND AND ANNOUNCES RESULT
	print(f'\n{do_round(player_choice,bot_choice).center(48)}') #With a line break


	#TODO: Store amount of wins/losses and show them in the end of each round


	# RESETS CHOICES FOR NEXT ROUND
	player_choice=-1
	bot_choice=-1