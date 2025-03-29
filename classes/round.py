class Round:
    def __init__(self):
        #choices:
        self.player_choice:int
        self.bot_choice:int

        #results:
        self.is_player_winner:bool # if the player has won.
        self.is_tied = False # if it was a tie. False by default


    #Calculates the round's result
    def calc_result(self):
        """
        Calculates the round's result.
        After this, you can call get_result_str() to get the result as a string.

        (OBS: Requires player_choice and bot_choice to be set first!)
        """
        ###### CALCULATING MATCH RESULTS ######
        # Subtracts the choice indexes
        result = self.player_choice - self.bot_choice

        # Uses this subtraction to find the winner
        ## VICTORY
        if result in [1, -2]:
            self.is_player_winner = True
        ## TIE
        elif result == 0:
            self.is_tied = True
        ## LOSS
        else:
            self.is_player_winner = False

    ## GETS MATCH RESULT AS A STRING
    def get_result_str(self):
        """Returns match result as a string."""
        if self.is_tied: return 'Tied.' # tie case
        elif self.is_player_winner: return 'You won!' # victory cases
        else: return 'You lost.' # loss case


    #OBS: I currently plan on making a small interface for this in the future, hence why I'm not using one single function for this