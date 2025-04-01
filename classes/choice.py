class Choice:
    def __init__(self):
        self.idx:int #choice index. integer that represents the choice, and is used as a value for the subtraction in result calculation
        self.name = lambda: {1:'Rock',2:'Paper',3:'Scissors'}[self.idx]


class ChoiceUser(Choice):
    def __init__(self):
        super().__init__()

    def prompt_user_choice(self):
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

        # Gets the choice
        self.idx = int(input(prompt_dialogue))
        #TODO: input treatment


class ChoiceBot(Choice):
    def __init__(self):
        super().__init__()
        self.probabillity_modifiers = {1:.0,2:.0,3:.0} #these shall be summed to otherwise equally divided chances. Negative values can be used to reduce these probabillities instead of increasing them

    def choice_logic(self):
        from random import randrange #Required for randomizing the choice
        self.idx = randrange(1,4,1)

        #TODO: proper choice logic, which modifies each possible choices' probability based on the frequency of each user choice and on the last choice used