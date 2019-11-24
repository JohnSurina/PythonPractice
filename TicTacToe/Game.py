# Tic Tac Toe Game script
# Written by John Surina

#-----------------------------------------------------------------------------------------#
from . import TicTacToeBoard as Tic

def play():
    x = Tic.TicTacToeBoard()

    print("Tic Tac Toe","\tWritten by John Surina",sep="\n",end="\n\n")

    sym1Invalid = True
    while(sym1Invalid):
        sym1 = input("Player 1, please select a symbol (enter nothing for default X): ")
        if sym1 == "":
            sym1Invalid = False
            continue
        sym1Invalid = not x.changeSym(1,sym1)


    sym2Invalid = True
    while(sym2Invalid):
        sym2 = input("Player 2, please select a symbol (enter nothing for default O): ")
        if sym2 == "":
            sym2Invalid = False
            continue
        sym2Invalid = not x.changeSym(2,sym2)

    x.print();print()

    playing = True
    while(playing):
        noWinner = True
        while(noWinner):

            p1SlotInvalid = True
            while(p1SlotInvalid):
                p1Slot = input("Player 1 move: ")
                p1SlotInvalid = not x.player1move(p1Slot)
                x.print();print()

            if x.isWon()[0]:
                noWinner = False
                break

            p2SlotInvalid = True
            while(p2SlotInvalid):
                p2Slot = input("Player 2 move: ")
                p2SlotInvalid = not x.player2move(p2Slot)
                x.print();print()

            if x.isWon()[0]:
                noWinner = False
                break

        print("\n")
        winner:str
        if x.isWon()[1] == 0:
            print("It's a draw")
        elif x.isWon()[1] == 1:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        x.resetBoard()
        playAgain = input("Play again? (y/n): ")
        if playAgain.lower() != "y":
            playing = False
        
