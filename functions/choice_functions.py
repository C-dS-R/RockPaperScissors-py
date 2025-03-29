## PROMPTS USER'S CHOICE
def prompt_user_choice():
    """
    Prompts user to choose a move.
    Returns the choice as an integer (1, 2 or 3).

    """
    # Dialogue
    prompt_dialogue = (
        "\nPick your move by typing one of the following numbers:\n"
        +"\n[1] - Rock".center(48)
        +"\n[2] - Paper".center(48)
        +"\n[3] - Scissors".center(48)
        +"\n"
        )

    # Gets and returns choice
    return int(input(prompt_dialogue))
    #TODO: input treatment


# Converts an index to the equivalent choice name
#TODO: remove this function once the choice class is implemented
def get_choice_name_From_idx(choice_idx):
	"""A temporary function while I havent implemented the choice class yet"""
	match choice_idx:
		case 1: return 'Rock'
		case 2: return 'Paper'
		case 3: return 'Scissors'
