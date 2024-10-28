from re import search

#    #    Functions for the treatment/validation of choices   #    #


#   General choice validation/treatment
#Used for user choices only
def treatChoice(c):
     #  checks first if user inputted it as number
     #if so, just get it printed
     if c.isnumeric():
          choice_echo(int(c))
          return int(c)

     # Otherwise, we proceed with the string treatment
     #TODO: Fix RegExps

     c = str.lower(c) # Lowercases it
     # Verifies the string via RegExp
     #Rock
     if not search("^r([ck]?o?[ck][ck]?)?#",c) == None:
          print("Rock")
          return 1
     #Paper
     elif not search("^p((ae?)?pp?e?r)?$",c) == None:
          print("Paper".center(2))
          return 2
     #Scissors
     elif not search("^s((([cs]?[cs]?i[sz][sz]?ors?)|((cr?s?|sr?s?)?)))$",c) == None:
          print("Scissors".center(2))
          return 3
     else: #Invalid choice case
          print("Choice could not be recognized".center(2))
          return -1

#   Prints choice result
#Used both for user and machine choices
def choice_echo(n): #For user choices, this is used after verified by treatChoice. As for machine choice, this is used directly, as machine choices are always numeric
     #Note that the interval check(as in, the check for it the input is between 1-3) is not done here, as this function is also intended for machine choices. they are already done in a fixed range. not only this avoids a small waste, but also much better then having to put 'return n-1' to each case or similar.
     match n:
          case 1: print("Rock".center(2))
          case 2: print("Paper".center(2))
          case 3: print("Scissors".center(2))
     # return n