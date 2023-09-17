import random
import time
import getpass


# function determines and returns the winner.
def winner(choice1, choice2):
    try:
        if choice1.upper() == "S":
            if choice2.upper() == "R":
                return choice2
            elif choice2.upper() == "P":
                return choice1
            else:
                return 1
        elif choice1.upper() == "P":
            if choice2.upper() == "R":
                return choice1
            elif choice2.upper() == "S":
                return choice2
            else:
                return 1
        elif choice1.upper() == "R":
            if choice2.upper() == "S":
                return choice1
            elif choice2.upper() == "P":
                return choice2
            else:
                return 1
    except:
        print("Something went wrong at winner function!")


# function to covert letter choice to full name choice
def characterToLetter(choice):
    try:
        if choice.upper() == "R":
            return "Rock"
        elif choice.upper() == "S":
            return "Scissors"
        elif choice.upper() == "P":
            return "Paper"
        else:
            print("Invalid Value")
    except:
        print("Something went wrong at characterToLetter function.")


# function determines if a player choice is valid, and returns valid user input
def playerChoice(playerID):
    try:
        playerSelectionValid = False
        if playersInfo[0] == 1 and playerID == "Program":
            playerSelection = random.choice("RSP")
            print("Program selects: " + playerSelection)
        elif playersInfo[0] == 1 and playerID != "Program":
            printText = "{} selects:"
            print(printText.format(playerID))
            playerSelection = input()
            if playerSelection.upper() in "RSP":
                playerSelectionValid = True

            while playerSelectionValid is False:
                print("Invalid input, please enter a correct letter!")
                playerSelection = input("Player selects: ")
                if playerSelection.upper() in "RSP":
                    playerSelectionValid = True
        else:
            printText = "{} selects:"
            print(printText.format(playerID))
            playerSelection = getpass.getpass(prompt="")
            print("*")
            if playerSelection.upper() in "RSP":
                playerSelectionValid = True

            while playerSelectionValid is False:
                print("Invalid input, please enter a correct letter!")
                playerSelection = getpass.getpass(prompt="")
                print("*")
                if playerSelection.upper() in "RSP":
                    playerSelectionValid = True
    except:
        print("Something went wrong at playerChoice function.")
    return playerSelection


# function shows the result
def showResult(playerNum):
    try:
        player1ID = playersInfo[1]
        player2ID = playersInfo[2]
        player1Choice = playerChoice(player1ID)
        player2Choice = playerChoice(player2ID)
        result = winner(player1Choice, player2Choice)
        while result != 1:
            showResult = "\n{} selected {}, {} selected {}. {} Wins!\n"
            print(showResult.format(player1ID, characterToLetter(player1Choice), 
                                    player2ID, characterToLetter(player2Choice), 
                                    characterToLetter(result)))
            #scenario of computer winning.
            if playerNum == 1 and result != player1Choice:
                print("You lost! Good luck next time!")
            #scenario of player 1 winning.
            elif result == player1Choice:
                wins = "{} Won! Good job!"
                print(wins.format(player1ID))
            #scenario of player 2 wins when it's against each other. 
            else:
                wins = "{} Won! Good job!"
                print(wins.format(player2ID))
            break
        #when both selects the same.
        else:
            showResult = "\n{} selected {}, {} also selected {}.\n"
            print(showResult.format(player1ID, characterToLetter(player1Choice), 
                                    player2ID, characterToLetter(player2Choice)))
            print("It's a tie!!! You should try again to find out who wins!")   
    except:
        print("Something went wrong at showResult function.")



#function determines if players play against each other or against the program.
def determinePlayerNumber ():
    try:
        print("\nDo you want to play against each other?")
        playAgainstEachOther = input("Enter Y to play each other, enter any other key to play against program: ")
        if playAgainstEachOther.upper() == "Y":
            playerNumber = 2
            player1ID = input("Enter player 1 username: ")
            player2ID = input("Enter player 2 username: ")
        else:
            playerNumber = 1
            player1ID = input("Enter player username: ")
            player2ID = "Program"
        playerInfo = [playerNumber, player1ID, player2ID]
    except:
        print("Something went wrong at determinePlayerNumber function.")
    return playerInfo



intentionToPlay = True
playerNumber = 1
player1ID = ""
player2ID = ""
playersInfo = list()

#This is Welcome message.
welcome = """
************************************************************
*                                                          *
*        This is Rock, Paper, Scissors Game!               *
*                                                          *
*                      Have Fun!                           *
*                                                          *
************************************************************
"""
print(welcome)

#Game pauses for 1 second. 
time.sleep(1)

#Determine if it's player against the program or player against another player according to the user input.
playersInfo = determinePlayerNumber()

while intentionToPlay is True:

    #describes how the game is played.
    print("\nYou may enter R for rock, S for scissors, P for paper.")
    print("Press ENTER key after selecting your choice!\n")

    #Game pauses for 1 second.
    time.sleep(1)

    #Players make their selections and result is shown. Go to showResult function for details.
    showResult(playersInfo[0])

    #Game pauses for 2 seconds before asking for rematch or stop playing.
    time.sleep(2)

    #player chooses to play again or stop the game. 
    print("\nDo you want to play again?")
    rematchChoice = input("Enter Y for Yes, or any other key to exit the game. \nYes or No? ")
    
    if rematchChoice.upper() == "Y":
        playersInfo = determinePlayerNumber()
    else:
        intentionToPlay = False


