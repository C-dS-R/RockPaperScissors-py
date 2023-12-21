from re import search

#    #    Functions for the treatment/validation of choices   #    #


#   General choice validation/treatment
#Used for user choices only
def treatChoice(c):
     #  checks first if user inputted it as number
     #if so, we go for checkNumChoice()'s treatment instead
     if c.isnumeric(): return checkNumChoice(int(c))

     # Otherwise, we proceed with the string treatment

     c = str.lower(c) # Lowercases it
     # Verifies the string via RegExp
     #Rock
     if not search("^r(((c|k|)(o|)(c|k)(c|k|))|$)",c) == None:
          print(" Rock")
          return 1
     #Paper
     elif not search("^p(((a(e|)|)p(p|)(e|)r)|$)",c) == None:
          print(" Paper")
          return 2
     #Scissors
     elif not search("^s(((c|s|)(c|s|)i(s|z)(s|z|)or(s|))|((c(r|)(s|)|s(r(s|)|)))|)$",c) == None:
          print(" Scissors")
          return 3
     else: #Invalid choice case
          print(" Choice could not be recognized")
          return -1
     

#   Treatment for when the choice is a number
#Used both for user and machine choices
def checkNumChoice(n): #For user choices, this is used after verified by treatChoice. As for machine choice, this is used directly, as machine choices are always numeric
     #Note that the interval check(as in, the check for it the input is between 1-3) is not done here, as this function is also intended for machine choices. they are already done in a fixed range. not only this avoids a small waste, but also much better then having to put 'return n-1' to each case or similar.
     match n:
          case 1: print(" Rock")
          case 2: print(" Paper")
          case 3: print(" Scissors")
     return n