from choiceValTrtFuncs import treatChoice

#    #    Functions for the execution of the rounds themselves   #    #


#  Prompts user's choice
def getChoice():
    inp = input("""
     Pick your move by typing one of the following numbers:
                    [1] - Rock
                    [2] - Paper
                    [3] - Scissors

(Alternatively, you can simply type its name. Initials and abbreviations are also an option)
""")
    print("""
Your choice: """)
    return treatChoice(inp)


#  Checks if user has won the round or not
def doRound(p1,p2):
     #first, prints a few dots to indicate the match is being calculated
     print("                    ...")




     #gets the subtration of the choice indexes
     sbt = p1-p2

     #uses it to check who's the winner
     if sbt==0: return "                   Tied." # tie case
     elif sbt in [1, -2]: return "                  You won!" # victory cases
     else: return "                  You lost." # loss case