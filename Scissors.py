import random

Program = None
# possiblities = None
possibilities = ["rock", "paper", "scissor"] # List of posibities
def programInput ():
    # possibilities = ["rock", "paper", "scissor"]  # List of posibities
    # Randomly choose an option
    global Program
    Program = random.choice(possibilities)
    return Program

def playerInput () :
    # Prompting the User for Input
    global player_choice
    player_choice = None
    while player_choice not in possibilities:
        player_choice = input("Pick one ! Rock , Paper , Scissors :  ").lower()  # lower care
        if player_choice not in possibilities:  # controing for input errors
            print("Please pick one of the three choices , try again ")
    return player_choice

def playAgain (): # Prompt for a second round and fetch input
    ans_key = ["N","Y","YES","NO"]
    ans = None
    while ans not in ans_key :
        ans = input("Do you want to play again ? Y/N : ").upper()
        if ans not in ans_key:  # controing for input errors
            print("Please reply by Yes or No . ")
    if ans in ["YES", "Y"]:
        programInput()
        playerInput()
        game()
    else:
        print("Thank you , See you next time ! ")
    return


def game():
    if Program == player_choice:
        print("You got : {}".format(player_choice))
        print("The Computer got : {}".format(Program))
        print("It's a Tie !")
        playAgain()

    elif Program == "rock":
        if player_choice == "paper":
            print("You got : {}".format(player_choice))
            print("The Computer got : {}".format(Program))
            print("You WON !!")
            playAgain()
        else:
            print("You got : {}".format(player_choice))
            print("The Computer got : {}".format(Program))
            print("You Lost !")
            playAgain()
    elif Program == "paper":
        if player_choice == "rock":
            print("You got : {}".format(player_choice))
            print("The Computer got : {}".format(Program))
            print("You Lost !")
            playAgain()
        else:
            print("You got : {}".format(player_choice))
            print("The Computer got : {}".format(Program))
            print("You Lost !")
            playAgain()
    else:
        if player_choice == "paper":
            print("You got : {}".format(player_choice))
            print("The Computer got : {}".format(Program))
            print("You Lost !")
            playAgain()
        else:
            print("You got : {}".format(player_choice))
            print("The Computer got : {}".format(Program))
            print("You Lost !")
            playAgain()


playerInput()
# Now let's play
game()



# print("You chose :"+ player_choice )


