from random import randrange #Required for randomizing machine choice

from classes.round import Round
from functions.choice_functions import *

##### Executes from here
while(True):
	current_round = Round() #Creates a new round object

	# Asks for user to choose a move
	current_round.player_choice = prompt_user_choice()
	print(f'Your choice: {get_choice_name_From_idx(current_round.player_choice)}')


	#BOT CHOICE
	current_round.bot_choice = randrange(1,4,1)
	print(f'Adversary choice: {get_choice_name_From_idx(current_round.bot_choice)}')

	# EXECUTES ROUND
	print("...".center(48)) # First, prints a few dots to show the match is being calculated
	current_round.calc_result() #Calculates the round's result

	#ANNOUNCES RESULT
	print(f'\n{(current_round.get_result_str()).center(48)}')


	#TODO: Store amount of wins/losses and show them in the end of each round