from choiceValTrtFuncs import treatChoice

#    #    Functions for the execution of the rounds themselves   #    #


#  Prompts user's choice
def user_choice():
    # Dialogue
    print("\nPick your move by typing one of the following numbers:")
    print("[1] - Rock".center(48))
    print("[2] - Paper".center(48))
    print("[3] - Scissors".center(48))
    # print("(Alternatively, you can simply type its name. Initials and abbreviations are also an option)")

    # Gets choice
    inp = input()
    print(f'\nYour choice:')
    return treatChoice(inp)


#  Checks if user has won the round or not
def do_round(player_choice,bot_choice):
    # First, prints a few dots to show the match is being calculated
    print("...".center(48))


    #CALCULATING MATCH RESULTS
    # Subtracts the choice indexes
    result = player_choice-bot_choice

    # Uses it to check who's the winner
    if result==0: return "Tied." # tie case
    elif result in [1, -2]: return "You won!" # victory cases
    else: return "You lost." # loss case