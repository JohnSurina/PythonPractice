# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# ----------------------------------------------------------- #

import random

print("Rock Paper Scissors")
playMode = input("Play with computer (C), or with player (P): ")

rockInput = (1,"r","R","rock","Rock","ROCK")
paperInput = (2,"p","P","paper","Paper","PAPER")
scissorsInput = (3,"s","S","scissors","Scissors","SCISSORS")

def whoWon(p1, p2):
    if p1 in rockInput:
        if p2 in rockInput:
            return(None)
        if p2 in paperInput:
            return(2)
        if p2 in scissorsInput:
            return(1)
    if p1 in paperInput:
        if p2 in rockInput:
            return(1)
        if p2 in paperInput:
            return(None)
        if p2 in scissorsInput:
            return(2)
    if p1 in scissorsInput:
        if p2 in rockInput:
            return(2)
        if p2 in paperInput:
            return(1)
        if p2 in scissorsInput:
            return(None)

winner = None

if playMode == "C" or playMode == "c":
    while winner != 1 and winner != 2:
        playerInput = input("Rock, paper, scissors...: ")
        computerInput = random.randint(1,3)
        winner = whoWon(playerInput,computerInput)
        if winner != 1 and winner != 2:
            print("It's a draw! try again. ", end="")
    if winner == 1:
        print("You win!")
    else:
        print("You lose.")
    
elif playMode == "P" or playMode == "p":
    while winner != 1 and winner != 2:
        player1Input = input("Player 1, Rock, paper, scissors...: ")
        player2Input = input("Player 2, Rock, paper, scissors...: ")
        winner = whoWon(player1Input,player2Input)
        if winner != 1 and winner != 2:
            print("It's a draw! try again. ")
    if winner == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")