import random

def game(comp, plyr):
    if comp == plyr:
        print("Tie!!!")
    elif comp == 'r':
        if plyr == 'p':
            print("You win!!!")
        elif plyr == 's':
            print("You Lose!!!")
    elif comp == 'p':
            if plyr == 's':
                print("You win!!!")
            elif plyr == 'r':
                print("You Lose!!!")
    elif comp == 's':
            if plyr == 'r':
                print("You win!!!")
            elif plyr == 'p':
                print("You Lose!!!")

rand = random.randint(1,3)
if rand == 1:
    comp = 'r'
elif rand == 2:
    comp = 'p'
else:
    comp = 's'
plyr = input("Your Turn: ")
print("comp choose ", comp)
print("You choose ", plyr)
game(comp,plyr)
