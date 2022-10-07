#creating a Cole Chess Bot
# i ilike chess
#i have plenty of data
#and i can train it myself by having it make a move and seeing if i'd play said move
from contextlib import nullcontext
from typing_extensions import Self
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#have to download my chess.com archive
#learn how to find file paths in drive

#create chess game
#filter data, what color am I? my moves, oponent's moves, winner, method of win etc

#creating the chess game
class tile():
    def __init__(self):
        self.piece = None
        self.row = 0
        self.col = 0

    def __init__(self, piece, row, col):
        self.piece = piece
        self.row = row
        self.col = col
    
    def __str__(self):
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return abc[self.row] + str(self.col) + "is occupied by a " + str(self.piece)

class piece():
    def __init__(self): #do I need this?
        self.tile = None
        self.color = True #bool value, true for white. false: black
        self.worth = 0
        self.moves = []
        self.name = ""


    def __init__(self, tile, color, moves):
        self.tile = tile
        self.color = color
        self.moves = moves
        self.name = "piece"

    def __str__(self):
        clr = ""
        if(self.color):
            clr = "white "
        else:
            clr = "black "
        return clr + self.name

    def find_Moves(self):
        return 0

    def Move(self, RC):
        if(board[RC[0], RC[1]].piece != None):
            del board[RC[0], RC[1]].piece # does this do what I think it does?
        board[RC[0], RC[1]] = Self
        board[self.tile.row, self.tile.col] = None
        self.tile = board[RC[0], RC[1]]



    #do i need a parent class function of findMoves? no but a parent of Move is nice so I put one in

class pawn(piece):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.worth = 1
        self.hasMoved = False
        self.enPassant = False
        self.name = "pawn"

    def find_Moves(self):
        r = self.tile.row
        c = self.tile.col
        if(self.color):
            if(not self.hasMoved and board[r + 2, c].piece == None and board[r + 1, c].piece == None):
                self.moves.append((r + 1, c)) #can it move two squares ahead

            if(board[r + 1, c].piece == None):
                self.moves.append((r, c+1)) #can it move one square ahead

            if(c-1 >= 0 and board[r + 1, c -1].piece != None and board[r + 1, c - 1].piece.color != self.color):
                self.moves.append((r + 1, c - 1)) #taking to the left

            if(c + 1 < 8 and board[r+1, c+1].piece != None and board[r+1, c+1].piece.color != self.color):
                self.moves.append((r+1, c+1)) #taking to the right

            if(c-1 >= 0 and board[r+1, c-1].piece.enPassant):
                self.moves.append((r + 1, c - 1)) #taking en Passant to the left

            if(c+1 < 8 and board[r+1, c+1].piece.enPassant):
                self.moves.append((r+1, c+1)) #taking to the right

        else:

            if(not self.hasMoved and board[r-2, c].piece == None and board[r-1, c].piece == None):
                self.moves.append((r-2, c)) #can it move two squares ahead

            if(board[r - 1, c].piece == None):
                self.moves.append((r - 1, c)) #can it move one square ahead

            if(c-1 >= 0 and board[r - 1, c -1].piece != None and board[r - 1, c-1].piece.color != self.color):
                self.moves.append((r - 1, c - 1)) #taking to the left

            if(c + 1 < 8 and board[r-1, c+1].piece != None and board[r-1, c-1].piece.color != self.color):
                self.moves.append((r-1, c+1)) #taking to the right

            if(c-1 >= 0 and board[r-1, c-1].piece.enPassant):
                self.moves.append((r-1, c - 1)) #taking en Passant to the left

            if(c+1 < 8 and board[r-1, c+1].piece.enPassant):
                self.moves.append((r-1, c+1)) #taking to the right

    def Move(self, RC):
        board[RC[0], RC[1]] = Self
        if(self.color and RC[0] == 7):
            self.promote("Congrats on making it to the end of the board. ")
        if(not self.color and RC[0] == 0):
            self.promote("Congrarts on making it to the end of the board. ")
        board[self.tile.row, self.tile.col] = None
    
    def promote(self, err):
        var = input(err + 'What would you like to promote your pawn to? (K, B, R, Q)')
        if(var == 'Q'):
            self.tile.piece = Queen(self.tile, self.color, moves := [])
        elif(var == 'K'):
            self.tile.piece = Knight(self.tile, self.color, moves := [])
        elif(var == 'R'):
            self.tile.piece = Rook(self.tile, self.color, moves := [])
        elif(var == 'B'):
            self.tile.piece = Bishop(self.tile, self.color, moves := [])
        else:
            self.promote("Looks like that's an invalid piece. Try again. ")
        
class Knight(piece):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.worth = 3
        self.name = "knight"

    def find_Moves(self):
        r = self.tile.row
        c = self.tile.col
        #none of the other pieces available moves are dependent on self.color
        if (c-2 >= 0):
            if(r - 2 >= 0):
                # (-2, -1) and (-1, -2) are on the board
                if(board[r-2, c-1].piece == None or board[r-2, c-1].piece.color != self.color):
                    self.moves.append((r-2, c-1)) #(-2, -1)
                if(board[r-1, c-2].piece == None or board[r-1, c-2].piece.color != self.color):
                    self.moves.append((r-1, c-2)) #(-1, -2)
            elif(r-1 >=0):
                #Only (-1, -2) is on the board
                if(board[r-1, c-2].piece == None or board[r-1, c-2].piece.color != self.color):
                    self.moves.append((r-1, c-2))
            if(r+2 <8):
                # (+1, -2) and (+2, -1) are available
                if(board[r+2, c-1].piece == None or board[r+2, c-1].piece.color != self.color):
                    self.moves.append((r+2, c-1)) #(+2, -1)
                if(board[r+1, c-2].piece == None or board[r+1, c-2].piece.color != self.color):
                    self.moves.append((r+1, c-2)) #(+1, -2)
            elif(r+1<8):
                # Only (+1, -2) is there
                if(board[r+1, c-2].piece == None or board[r+1, c-2].piece.color != self.color):
                    self.moves.append((r+1, c-2))
        elif (c-1 >= 0):
            if(r-2 >= 0): #only need to look at when r is +- 2
                if(board[r-2, c-1].piece == None or board[r-2, c-1].piece.color != self.color):
                    self.moves.append((r-2, c-1)) #(-2, -1)
            if(r+2< 8):
                if(board[r+2, c-1].piece == None or board[r+2, c-1].piece.color != self.color):
                    self.moves.append((r+2, c-1)) #(+2, -1)  

        if (c+2 < 8):
            if(r - 2 >= 0):
                # (-2, +1) and (-1, +2) are on the board
                if(board[r-2, c+1].piece == None or board[r-2, c+1].piece.color != self.color):
                    self.moves.append((r-2, c-1)) #(-2, +1)
                if(board[r-1, c+2].piece == None or board[r-1, c+2].piece.color != self.color):
                    self.moves.append((r-1, c+2)) #(-1, +2)
            elif(r-1 >=0):
                #Only (-1, +2) is on the board
                if(board[r-1, c+2].piece == None or board[r-1, c+2].piece.color != self.color):
                    self.moves.append((r-1, c+2))
            if(r+2 <8):
                # (+1, +2) and (+2, +1) are available
                if(board[r+2, c+1].piece == None or board[r+2, c+1].piece.color != self.color):
                    self.moves.append((r+2, c+1)) #(+2, +1)
                if(board[r+1, c+2].piece == None or board[r+1, c+2].piece.color != self.color):
                    self.moves.append((r+1, c+2)) #(+1, +2)
            elif(r+1<8):
                # Only (+1, +2) is there
                if(board[r+1, c+2].piece == None or board[r+1, c+2].piece.color != self.color):
                    self.moves.append((r+1, c+2))
        elif (c + 1<8):
            if(r-2 >= 0): #only need to look at when r is +- 2
                if(board[r-2, c+1].piece == None or board[r-2, c+1].piece.color != self.color):
                    self.moves.append((r-2, c+1)) #(-2, +1)
            if(r+2< 8):
                if(board[r+2, c+1].piece == None or board[r+2, c+1].piece.color != self.color):
                    self.moves.append((r+2, c-1)) #(+2, +1)



class Bishop(piece):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.worth = 3
        self.name = "bishop"

class Rook(piece):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.worth = 5
        self.hasMoved = False
        self.name = "rook"

class Queen(Bishop, Rook):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.worth = 9
        self.name = "queen"

class King(piece):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.hasMoved = False
        self.inCheck = False
        self.name = "king"
            
            

        


board = []

for i in range(8):
    row = []
    for j in range(8):
        temp = tile(None, j, i)
        row.append(temp)
    board.append(row)

#new game (creates all the pieces in they're correct spots)
#turn (recursive function called in play game)
#for the end each turn call in check for both sides, which will find moves for each piece on the other side

#will return string in same format as chess.com games
