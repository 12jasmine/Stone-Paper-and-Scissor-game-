import random

def gamewin(comp , you):
# If two values are equal , declare a tie .
    if comp == you :
        return None
 
 # Check for possibilities when computer chose 's ':
    elif comp == 's':
        if you == 'p':
            return True
        elif you =='sc':
            return False
# Check for possibilities when computer chose 'p' :          
    elif comp =='p':
        if you == 'sc':
            return True
        elif you == 's':
            return False
# Check for possibilities when computer chose 'sc' :           
    elif comp == 'sc':
        if you == 's':
            return True
        elif you =='p':
            return False
        
# Printing computer turn randomly.        
print("Computer turn : Stone(s) Paper(p) or Scissors(sc) : ")

# declaring a random variable which print random value between 1-3.
randomNo = random.randint(1 , 3)
if randomNo ==1:
    comp = 's'
elif randomNo ==2:
    comp = 'p'
elif randomNo ==3:
    comp = 'sc'

# Printing player turn .
you = input("your turn : Stone(s) Paper(p) or Scissors(sc) : ")

a = gamewin(comp , you)

# Choosed value of both.
print(f"Computer chose {comp}")
print(f"You chose {you}")

# Applying conditions and printing  who wins the game.
if a == None:
    print("Game tie!!")
elif a == True:
    print("You Win!!")
else :
    print("You Lose !!")
       
    #  !!!  finished !!!
    

