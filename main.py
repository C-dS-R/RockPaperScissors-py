from classes.round import Round

##### Executes from here
while(True):
	this_round = Round() #Creates a new round object

	# Asks for user to choose a move
	this_round.player_choice.prompt_user_choice()
	print(f'Your choice: {this_round.player_choice.name()}')


	#BOT CHOICE
	this_round.bot_choice.choice_logic()
	print(f'Adversary choice: {this_round.bot_choice.name()}')

	# EXECUTES ROUND
	print("...".center(48)) # First, prints a few dots to show the match is being calculated
	this_round.calc_result() #Calculates the round's result

	#ANNOUNCES RESULT
	print(f'\n{(this_round.get_result_str()).center(48)}')


	#TODO: Store amount of wins/losses and show them in the end of each round