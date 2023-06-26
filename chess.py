import tkinter as tk
from tkinter import ttk

class game: 
  
  def __init__(self, initialPosition):

    self.root = tk.Tk()
    squareSize = 75
    squares = []
    isWhite = 1
    alphabet = 'abcdefgh'


    # creates board
    for y in range(1,9):

      # adds numbers down the side
      sideFrames = tk.Frame(self.root)
      sideFrames.grid(row=y, column=0)
      ttk.Label(sideFrames, text=str(abs(y-9))).grid()
      
      for x in range(1,9):
        
        # adds letters to the bottom
        if y == 1:
          bottomFrames = tk.Frame(self.root)
          bottomFrames.grid(row=9, column=x)
          ttk.Label(bottomFrames, text=alphabet[x-1]).grid()

        # creates the checker pattern
        if isWhite:
          squares.append(tk.Frame(self.root, bg="white", width=squareSize, height=squareSize))
          squares[len(squares)-1].grid(row=y, column=x)
        else:
          squares.append(tk.Frame(self.root, bg="black", width=squareSize, height=squareSize))
          squares[len(squares)-1].grid(row=y, column=x)

        isWhite = abs(isWhite-1)

      isWhite = abs(isWhite-1)

    pieces = {'r':rook, 'n':knight, 'b':bishop,
              'q':queen, 'k':king, 'p':pawn}

    FEN = initialPosition.split(' ')

    # initialize board position
    self.board = [[None for y in range(8)] for x in range(8)]
    x = 0
    y = 0
    for i in FEN[0]:
      if i in 'rnbkqp':
        self.board[y][x] = pieces[i]('black')
        x += 1
      elif i in 'RNBKQP':
        self.board[y][x] = pieces[i.lower()]('white')
        x += 1
      elif i in '12345678':
        for n in range(int(i)):
          self.board[y][x] = None
          x += 1
      else:
        y += 1
        x = 0

    # other FEN info
    self.colorToGo = FEN[1]
    self.castlingRights = FEN[2]
    self.enPassantTargets = FEN[3]
    self.halfMoves = int(FEN[4])
    self.fullMoves = int(FEN[5])
    
  def convertToFEN(self):
    string = ''
    empty = 0
    
    for y in range(8):
      
      for x in range(8):
        if not self.board[y][x]:
          empty += 1
        elif empty:
          string = string + str(empty) + str(self.board[y][x])
          empty = 0
        else: 
          string += str(self.board[y][x])
          
      if empty:
        string += str(empty)
        empty = 0
        
      string += '/'
    
    return(string[:-1])

  def __str__(self):
    otherFEN = [self.convertToFEN(), self.colorToGo, 
                self.castlingRights, self.enPassantTargets, 
                str(self.halfMoves), str(self.fullMoves)]
    return ' '.join(otherFEN)

class king(game):

  def __init__(self, color):
    self.color = color

  def __str__(self):
    if self.color == 'white':
      return 'K'
    else:
      return 'k'
      
class queen(game):
    
  def __init__(self, color):
    self.color = color

  def __str__(self):
    if self.color == 'white':
      return 'Q'
    else:
      return 'q'
    
class rook(game):
    
  def __init__(self, color):
    self.color = color

  def __str__(self):
    if self.color == 'white':
      return 'R'
    else:
      return 'r'
    
class bishop(game):
    
  def __init__(self, color):
    self.color = color

  def __str__(self):
    if self.color == 'white':
      return 'B'
    else:
      return 'b'
    
class knight(game):
    
  def __init__(self, color):
    self.color = color

  def __str__(self):
    if self.color == 'white':
      return 'N'
    else:
      return 'n'
    
class pawn(game):
    
  def __init__(self, color):
    self.color = color

  def __str__(self):
    if self.color == 'white':
      return 'P'
    else:
      return 'p'
    
position = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
g = game(position)
g.root.mainloop()
