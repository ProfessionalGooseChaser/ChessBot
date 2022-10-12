#creating a Cole Chess Bot
# i ilike chess
#i have plenty of data
#and i can train it myself by having it make a move and seeing if i'd play said move
#from contextlib import nullcontext
#import tensorflow as tf
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
        if(board[RC[0]][RC[1]].piece != None):
            del board[RC[0]][RC[1]].piece # does this do what I think it does? - It defintely doesn't
        #board[RC[0], RC[1]] = Self
        board[self.tile.row][self.tile.col] = None
        self.tile = board[RC[0]][RC[1]]



    #do i need a parent class function of findMoves? no but a parent of Move is nice so I put one in

class Pawn(piece):
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
            if(not self.hasMoved and board[r + 2][c].piece == None and board[r + 1][c].piece == None):
                self.moves.append((r + 2, c)) #can it move two squares ahead
                self.moves.append((r+1, c)) #can it move one square ahead

            elif(board[r + 1][c].piece == None):
                self.moves.append((r, c+1)) #can it move one square ahead

            if(c-1 >= 0 and board[r + 1][c -1].piece != None and board[r + 1][c - 1].piece.color != self.color):
                self.moves.append((r + 1, c - 1)) #taking to the left

            if(c + 1 < 8 and board[r+1][c+1].piece != None and board[r+1][c+1].piece.color != self.color):
                self.moves.append((r+1, c+1)) #taking to the right

            if(c-1 >= 0 and board[r][c-1].piece != None and board[r][c-1].piece.color != self.color and type(board[r][c-1].piece) == Pawn and board[r][c-1].piece.enPassant):
                self.moves.append((r + 1, c - 1)) #taking en Passant to the left

            if(c+1 < 8 and board[r][c+1].piece != None and board[r][c+1].piece.color != self.color and type(board[r][c+1].piece) == Pawn and board[r][c+1].piece.enPassant):
                self.moves.append((r+1, c+1)) #taking to the right

        else:

            if(not self.hasMoved and board[r-2][c].piece == None and board[r-1][c].piece == None):
                self.moves.append((r-2, c)) #can it move two squares ahead
                self.moves.append((r - 1, c)) #can it move one square ahead

            elif(board[r - 1][c].piece == None):
                self.moves.append((r - 1, c)) #can it move one square ahead

            if(c-1 >= 0 and board[r - 1][c -1].piece != None and board[r - 1][c-1].piece.color != self.color):
                self.moves.append((r - 1, c - 1)) #taking to the left

            if(c + 1 < 8 and board[r-1][c+1].piece != None and board[r-1][c-1].piece.color != self.color):
                self.moves.append((r-1, c+1)) #taking to the right

            if(c-1 >= 0 and board[r][c-1].piece != None and board[r][c-1].piece.color != self.color and type(board[r][c-1].piece) == Pawn and board[r-1][c-1].piece.enPassant):
                self.moves.append((r-1, c - 1)) #taking en Passant to the left

            if(c+1 < 8 and board[r][c+1].piece != None and board[r][c+1].piece.color != self.color and type(board[r][c+1].piece) == Pawn and board[r-1][c+1].piece.enPassant):
                self.moves.append((r-1, c+1)) #taking to the right

    def Move(self, RC):
        #board[RC[0]][RC[1]] = Self
        if(self.color and RC[0] == 7):
            self.promote("Congrats on making it to the end of the board. ")
        if(not self.color and RC[0] == 0):
            self.promote("Congrarts on making it to the end of the board. ")
        board[self.tile.row][self.tile.col] = None
    
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
                if(board[r-2][c-1].piece == None or board[r-2][c-1].piece.color != self.color):
                    self.moves.append((r-2, c-1)) #(-2, -1)
                if(board[r-1][c-2].piece == None or board[r-1][c-2].piece.color != self.color):
                    self.moves.append((r-1, c-2)) #(-1, -2)
            elif(r-1 >=0):
                #Only (-1, -2) is on the board
                if(board[r-1][c-2].piece == None or board[r-1][c-2].piece.color != self.color):
                    self.moves.append((r-1, c-2))
            if(r+2 <8):
                # (+1, -2) and (+2, -1) are available
                if(board[r+2][c-1].piece == None or board[r+2][c-1].piece.color != self.color):
                    self.moves.append((r+2, c-1)) #(+2, -1)
                if(board[r+1][c-2].piece == None or board[r+1][c-2].piece.color != self.color):
                    self.moves.append((r+1, c-2)) #(+1, -2)
            elif(r+1<8):
                # Only (+1, -2) is there
                if(board[r+1][c-2].piece == None or board[r+1][c-2].piece.color != self.color):
                    self.moves.append((r+1, c-2))
        elif (c-1 >= 0):
            if(r-2 >= 0): #only need to look at when r is +- 2
                if(board[r-2][c-1].piece == None or board[r-2][c-1].piece.color != self.color):
                    self.moves.append((r-2, c-1)) #(-2, -1)
            if(r+2< 8):
                if(board[r+2][c-1].piece == None or board[r+2][c-1].piece.color != self.color):
                    self.moves.append((r+2, c-1)) #(+2, -1)  

        if (c+2 < 8):
            if(r - 2 >= 0):
                # (-2, +1) and (-1, +2) are on the board
                if(board[r-2][c+1].piece == None or board[r-2][c+1].piece.color != self.color):
                    self.moves.append((r-2, c+1)) #(-2, +1)
                if(board[r-1][c+2].piece == None or board[r-1][c+2].piece.color != self.color):
                    self.moves.append((r-1, c+2)) #(-1, +2)
            elif(r-1 >=0):
                #Only (-1, +2) is on the board
                if(board[r-1][c+2].piece == None or board[r-1][c+2].piece.color != self.color):
                    self.moves.append((r-1, c+2))
            if(r+2 <8):
                # (+1, +2) and (+2, +1) are available
                if(board[r+2][c+1].piece == None or board[r+2][c+1].piece.color != self.color):
                    self.moves.append((r+2, c+1)) #(+2, +1)
                if(board[r+1][c+2].piece == None or board[r+1, c+2].piece.color != self.color):
                    self.moves.append((r+1, c+2)) #(+1, +2)
            elif(r+1<8):
                # Only (+1, +2) is there
                if(board[r+1][c+2].piece == None or board[r+1][c+2].piece.color != self.color):
                    self.moves.append((r+1, c+2))
        elif (c + 1<8):
            if(r-2 >= 0): #only need to look at when r is +- 2
                if(board[r-2][c+1].piece == None or board[r-2][c+1].piece.color != self.color):
                    self.moves.append((r-2, c+1)) #(-2, +1)
            if(r+2< 8):
                if(board[r+2][c+1].piece == None or board[r+2][c+1].piece.color != self.color):
                    self.moves.append((r+2, c-1)) #(+2, +1)



class Bishop(piece):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.worth = 3
        self.name = "bishop"
    
    def find_Moves(self):
        r = self.tile.row
        c = self.tile.col
        N = 8 - c
        S = c + 1
        E = 8 - r
        W = r + 1

        #NE ++
        for NE in range(1, min(N, E)):
            if(board[r+NE][c+NE].piece == None):
                self.moves.append((r+NE, c+NE))
            elif(board[r+NE][c+NE].piece.color != self.color):
                self.moves.append((r+NE, c+NE))
                break
            else:
                break

        #NW -+
        for NW in range(1, min(N, W)):

            if(board[r-NW][c+NW].piece == None):
                self.moves.append((r-NW, c+NW))
            elif(board[r-NW][c+NW].piece.color != self.color):
                self.moves.append((r-NW, c+NW))
                break
            else:
                break

        #SW --
        for SW in range(1, min(S, W)):
            if(board[r-SW][c-SW].piece == None):
                self.moves.append((r-SW, c-SW))
            elif(board[r-SW][c-SW].piece.color != self.color):
                self.moves.append((r-SW, c-SW))
                break
            else:
                break

        #SE +-
        for SE in range(1, min(S, E)):
            
            if(board[r+SE][c-SE].piece == None):
                self.moves.append((r+SE, c-SE))
            elif(board[r+SE][c-SE].piece.color != self.color):
                self.moves.append((r+SE, c-SE))
                break
            else:
                break



class Rook(piece):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.worth = 5
        self.hasMoved = False
        self.name = "rook"

    def find_Moves(self):
        #castling is a function of the king, so when I use the this function with the queen, the queen doesn't castle with the queen)
        r = self.tile.row
        c = self.tile.col

        #N
        for N in range(1, 8-r):
            if(board[r+N][c].piece == None):
                self.moves.append((r+N, c))
            elif(board[r+N][c].piece.color != self.color):
                self.moves.append((r+N, c))
                break
            else:
                break
        
        for S in range(1, 1+ r):
            if(board[r-S][c].piece == None):
                self.moves.append((r-S, c))
            elif(board[r-S][c].piece.color != self.color):
                self.moves.append((r-S, c))
                break
            else:
                break

        for E in range(1, 8-c):
            if(board[r][c + E].piece == None):
                self.moves.append((r, c + E))
            elif(board[r][c+E].piece.color != self.color):
                self.moves.append((r, c+E))
                break
            else:
                break

        for W in range(1, 1+ c):
            if(board[r][c - W].piece == None):
                self.moves.append((r, c - W))
            elif(board[r][c-W].piece.color != self.color):
                self.moves.append((r, c-W))
                break
            else:
                break



class Queen(Bishop, Rook):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.worth = 9
        self.name = "queen"

    def find_Moves(self):
        return super().find_Moves()




class King(piece):
    def __init__(self, tile, color, moves):
        super().__init__(tile, color, moves)
        self.hasMoved = False
        self.inCheck = False
        self.name = "king"
    
    def in_check(self, tileXY):
        
        return False

    def find_Moves(self):
        r = self.tile.row
        c = self.tile.col

        #cardinal directions
        #E
        if(r + 1 < 8 and not self.in_check((r+1, c)) and board[r+1][c].piece == None or board[r+1][c].piece.color != self.color):
            self.moves.append((r+1, c)) 
        #W
        if(r - 1 >= 0 and not self.in_check((r-1, c)) and board[r-1][c].piece == None or board[r-1][c].piece.color != self.color):
            self.moves.append((r-1, c)) 
        #N
        if(c + 1 < 8 and not self.in_check((r, c+1)) and board[r][c+1].piece == None or board[r][c+1].piece.color != self.color):
            self.moves.append((r, c+1)) 
        #S
        if(c - 1 >= 0 and not self.in_check((r, c-1)) and board[r][c-1].piece == None or board[r][c-1].piece.color != self.color):
            self.moves.append((r, c-1)) 
        
        #corners
        #NE
        if(r + 1 < 8 and c + 1 < 8 and not self.in_check((r+1, c+1)) and board[r+1][c+1].piece == None or board[r+1][c+1].piece.color != self.color):
            self.moves.append((r+1, c+1))
        #SE
        if(r + 1 < 8 and c - 1 >=0 and not self.in_check((r+1, c-1)) and board[r+1][c-1].piece == None or board[r+1][c-1].piece.color != self.color):
            self.moves.append((r+1, c-1))
        #NW
        if(r - 1 >= 0 and c + 1 < 8 and not self.in_check((r-1, c+1)) and board[r-1][c+1].piece == None or board[r-1][c+1].piece.color != self.color):
            self.moves.append((r-1, c+1))
        #SW
        if(r - 1 >= 0 and c - 1 >= 0 and not self.in_check((r-1, c-1)) and board[r-1][c-1].piece == None or board[r-1][c-1].piece.color != self.color):
            self.moves.append((r-1, c-1))    
        
        


board = []

for i in range(8):
    row = []
    for j in range(8):
        temp = tile(None, i, j)
        row.append(temp)
    board.append(row)

#testing
board[6][3].piece = Knight(board[6][3], False, [])
board[3][1].piece = Pawn(board[3][1], True, [])
board[2][6].piece = Queen(board[2][6], False, [])
board[2][6].piece.find_Moves()
print("\n" * 5)
print(board[2][6].piece.moves)

#new game (creates all the pieces in they're correct spots)
#turn (recursive function called in play game)
#for the end each turn call in check for both sides, which will find moves for each piece on the other side

#will return string in same format as chess.com games
