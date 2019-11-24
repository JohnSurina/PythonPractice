class TicTacToeBoard:

    _boardVals_init = {
        "p13":" ","p23":" ","p33":" ",
        "p12":" ","p22":" ","p32":" ",
        "p11":" ","p21":" ","p31":" ",
        }

    def __init__(self):
        self.p1_sym = "X"
        self.p2_sym = "O"
        self.boardVals = {
            "p13":" ","p23":" ","p33":" ",
            "p12":" ","p22":" ","p32":" ",
            "p11":" ","p21":" ","p31":" ",
            }    

    _topLeft = ("tl","topleft","p13")
    _topMiddle = ("tm","topmiddle","p23")
    _topRight = ("tr","topright","p33")
    _middleLeft = ("ml","middleleft","p12")
    _middleMiddle = ("mm","middlemiddle","p22")
    _middleRight = ("mr","middleright","p32")
    _bottomLeft = ("bl","bottomleft","p11")
    _bottomMiddle = ("bm","bottommiddle","p21")
    _bottomRight = ("br","bottomright","p31")
    
    def print(s):
        print("+-----------+")
        print("| {0} | {1} | {2} |".format(s.boardVals["p13"],s.boardVals["p23"],s.boardVals["p33"]))
        print("|---+---+---|")
        print("| {0} | {1} | {2} |".format(s.boardVals["p12"],s.boardVals["p22"],s.boardVals["p32"]))
        print("|---+---+---|")
        print("| {0} | {1} | {2} |".format(s.boardVals["p11"],s.boardVals["p21"],s.boardVals["p31"]))
        print("+-----------+")

    def resetBoard(s):
        s.boardVals = s._boardVals_init

    def changeSym(self, ref:int, sym:str) -> bool:
        ''' changes the symbol that a player uses for indicating their moves on
        the board'''
        if (ref != 1) and (ref != 2):
            print("The player reference is not a valid (must be one or two)")
            return(False)
        if len(sym) != 1:
            print("The desired symbol must be just one (non-space) character")
            return(False)
        if sym == " ":
            print("You cannot use a space for your symbol")
            return(False)
        
        if ref == 1:
            self.p1_sym = sym
            return(True)
        elif ref == 2:
            self.p2_sym = sym
            return(True)
    
    def player1move(self, preSlot:str) -> bool:
        ''' This Function takes the player 1 symbol and puts it into
        the slot given. If the slot is valid, the method returns true
        and puts the player 1 symbol into the table slot specified,
        if the slot is invalid, than the method prints a warning message
        and returns false '''
        slot = preSlot.lower()
        if (slot in self._topLeft) and (self.boardVals["p13"] == " "):
            self.boardVals["p13"] = self.p1_sym
            return(True)
        elif (slot in self._topMiddle) and (self.boardVals["p23"] == " "):
            self.boardVals["p23"] = self.p1_sym
            return(True)
        elif (slot in self._topRight) and (self.boardVals["p33"] == " "):
            self.boardVals["p33"] = self.p1_sym
            return(True)
        elif (slot in self._middleLeft) and (self.boardVals["p12"] == " "):
            self.boardVals["p12"] = self.p1_sym
            return(True)
        elif (slot in self._middleMiddle) and (self.boardVals["p22"] == " "):
            self.boardVals["p22"] = self.p1_sym
            return(True)
        elif (slot in self._middleRight) and (self.boardVals["p32"] == " "):
            self.boardVals["p32"] = self.p1_sym
            return(True)
        elif (slot in self._bottomLeft) and (self.boardVals["p11"] == " "):
            self.boardVals["p11"] = self.p1_sym
            return(True)
        elif (slot in self._bottomMiddle) and (self.boardVals["p21"] == " "):
            self.boardVals["p21"] = self.p1_sym
            return(True)
        elif (slot in self._bottomRight) and (self.boardVals["p31"] == " "):
            self.boardVals["p31"] = self.p1_sym
            return(True)
        else:
            print("Invalid position")
            return(False)

    def player2move(self, preSlot:str):
        ''' This Function takes the player 1 symbol and puts it into
        the slot given. If the slot is valid, the method returns true
        and puts the player 1 symbol into the table slot specified,
        if the slot is invalid, than the method prints a warning message
        and returns false '''
        slot = preSlot.lower()
        if (slot in self._topLeft) and (self.boardVals["p13"] == " "):
            self.boardVals["p13"] = self.p2_sym
            return(True)
        elif (slot in self._topMiddle) and (self.boardVals["p23"] == " "):
            self.boardVals["p23"] = self.p2_sym
            return(True)
        elif (slot in self._topRight) and (self.boardVals["p33"] == " "):
            self.boardVals["p33"] = self.p2_sym
            return(True)
        elif (slot in self._middleLeft) and (self.boardVals["p12"] == " "):
            self.boardVals["p12"] = self.p2_sym
            return(True)
        elif (slot in self._middleMiddle) and (self.boardVals["p22"] == " "):
            self.boardVals["p22"] = self.p2_sym
            return(True)
        elif (slot in self._middleRight) and (self.boardVals["p32"] == " "):
            self.boardVals["p32"] = self.p2_sym
            return(True)
        elif (slot in self._bottomLeft) and (self.boardVals["p11"] == " "):
            self.boardVals["p11"] = self.p2_sym
            return(True)
        elif (slot in self._bottomMiddle) and (self.boardVals["p21"] == " "):
            self.boardVals["p21"] = self.p2_sym
            return(True)
        elif (slot in self._bottomRight) and (self.boardVals["p13"] == " "):
            self.boardVals["p31"] = self.p2_sym
            return(True)
        else:
            print("Invalid position")
            return(False)

    def isWon(s):
        # Case: Draw
        if (s.boardVals["p11"] != " " and 
            s.boardVals["p12"] != " " and
            s.boardVals["p13"] != " " and
            s.boardVals["p21"] != " " and
            s.boardVals["p22"] != " " and
            s.boardVals["p23"] != " " and
            s.boardVals["p31"] != " " and
            s.boardVals["p32"] != " " and
            s.boardVals["p33"] != " "):
            return((True,0))
        # Case: vertical left
        elif s.boardVals["p13"] == s.boardVals["p12"] == s.boardVals["p11"] and s.boardVals["p13"] != " ":
            if s.boardVals["p13"] == s.p1_sym:
                playerWinner = 1
            else:
                playerWinner = 2
            return((True, playerWinner))
        # Case: vertical center
        elif s.boardVals["p23"] == s.boardVals["p22"] == s.boardVals["p21"] and s.boardVals["p23"] != " ":
            if s.boardVals["p23"] == s.p1_sym:
                playerWinner = 1
            else:
                playerWinner = 2
            return((True, playerWinner))
        # Case: vertical right
        elif s.boardVals["p33"] == s.boardVals["p32"] == s.boardVals["p31"] and s.boardVals["p33"] != " ":
            if s.boardVals["p33"] == s.p1_sym:
                playerWinner = 1
            else:
                playerWinner = 2
            return((True, playerWinner))
        # Case: horizontal top
        elif s.boardVals["p13"] == s.boardVals["p23"] == s.boardVals["p33"] and s.boardVals["p13"] != " ":
            if s.boardVals["p13"] == s.p1_sym:
                playerWinner = 1
            else:
                playerWinner = 2
            return((True, playerWinner))
        # Case: horizontal middle
        elif s.boardVals["p12"] == s.boardVals["p22"] == s.boardVals["p32"] and s.boardVals["p12"] != " ":
            if s.boardVals["p12"] == s.p1_sym:
                playerWinner = 1
            else:
                playerWinner = 2
            return((True, playerWinner))
        # Case: horizontal bottom
        elif s.boardVals["p11"] == s.boardVals["p21"] == s.boardVals["p31"] and s.boardVals["p11"] != " ":
            if s.boardVals["p11"] == s.p1_sym:
                playerWinner = 1
            else:
                playerWinner = 2
            return((True, playerWinner))
        # Case: backslash
        elif s.boardVals["p13"] == s.boardVals["p22"] == s.boardVals["p31"] and s.boardVals["p13"] != " ":
            if s.boardVals["p13"] == s.p1_sym:
                playerWinner = 1
            else:
                playerWinner = 2
            return((True, playerWinner))
        # Case: forwardslash
        elif s.boardVals["p11"] == s.boardVals["p22"] == s.boardVals["p33"] and s.boardVals["p11"] != " ":
            if s.boardVals["p11"] == s.p1_sym:
                playerWinner = 1
            else:
                playerWinner = 2
            return((True, playerWinner))
        else:
            return((False,None))