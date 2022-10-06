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

    #do i need a parent class function of findMoves?

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

