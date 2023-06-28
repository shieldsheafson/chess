import tkinter as tk, os
from tkinter import ttk
from PIL import ImageTk, Image

class game: 
  
  def __init__(self, root):
    
    self.root = root
    self.squareSize = 75
    self.initialPosition = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    self.squares = []
    self.board = [[[None, None] for y in range(8)] for x in range(8)]
    self.images = []

  def createGameInstance(self):

    isWhite = 1
    alphabet = 'abcdefgh'

    pieces = {'r':rook, 'n':knight, 'b':bishop,
              'q':queen, 'k':king, 'p':pawn}

    FEN = self.initialPosition.split(' ')

    # initialize board position

    for n in range(1,9):

      # adds numbers down the side
      sideFrames = tk.Frame(self.root)
      sideFrames.grid(row=n-1, column=0)
      ttk.Label(sideFrames, text=str(abs(n-9))).grid()

      # adds letters to the bottom
      bottomFrames = tk.Frame(self.root)
      bottomFrames.grid(row=8, column=n)
      ttk.Label(bottomFrames, text=alphabet[n-1]).grid()

    x = 0
    y = 0
    for i in FEN[0]:

      # add black pieces
      if i in 'rnbkqp':
        self.board[y][x][1] = pieces[i](self, 'black', x+y*8)
        createSquare(self, isWhite, x, y)
        isWhite = abs(isWhite-1)
        x += 1

      # add white pieces
      elif i in 'RNBKQP':
        self.board[y][x][1] = pieces[i.lower()](self, 'white',  x+y*8)
        createSquare(self, isWhite, x, y)
        isWhite = abs(isWhite-1)
        x += 1

      # add empty spaces
      elif i in '12345678':
        for n in range(int(i)):
          self.board[y][x][1] = None
          createSquare(self, isWhite, x, y)
          isWhite = abs(isWhite-1)
          x += 1

      else:
        y += 1
        x = 0
        isWhite = abs(isWhite-1)

    # other FEN info
    self.colorToGo = FEN[1]
    self.castlingRights = FEN[2]
    self.enPassantTargets = FEN[3]
    self.halfMoves = int(FEN[4])
    self.fullMoves = int(FEN[5])
    
    updateUI(self)
    
  def convertToFEN(self):
    string = ''
    empty = 0
    
    for y in range(8):
      
      for x in range(8):
        if not self.board[y][x][1]:
          empty += 1
        elif empty:
          string = string + str(empty) + returnPieceFEN(self, self.board[y][x][1])
          empty = 0
        else: 
          string += returnPieceFEN(self, self.board[y][x][1])
          
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
  
def updateUI(self):

  for y in self.board:

    for x in y:
      
      if x[1]:
        img = Image.open(returnPieceImagePath(self, x[1]))
        img = img.resize((self.squareSize, self.squareSize))
        img = ImageTk.PhotoImage(img)
        self.images.append(img)
        x[0].create_image(self.squareSize/2, self.squareSize/2, image=img)
        
def returnPieceFEN(self, pieceString: str):

  return pieceString.split(',', 1)[0]

def returnPieceImagePath(self, pieceString: str):

  return pieceString.split(',', 1)[1]

def createSquare(self, isWhite: bool, x: int, y: int):

  if isWhite:
    square_frames = tk.Frame(self.root, width= self.squareSize, height=self.squareSize)
    square_frames.grid(row=y, column=x+1) # x+1 to make room for notation marks
    self.board[y][x][0] = tk.Canvas(square_frames, background='light gray', width=self.squareSize, height=self.squareSize, borderwidth=0)
    self.board[y][x][0].grid()
  else:
    square_frames = tk.Frame(self.root, width= self.squareSize, height=self.squareSize)
    square_frames.grid(row=y, column=x+1) # x+1 to make room for notation marks
    self.board[y][x][0] = tk.Canvas(square_frames, background='dark gray', width=self.squareSize, height=self.squareSize, borderwidth=0)
    self.board[y][x][0].grid()

def king(self, color: str, initialPiecePosition: int):

    if color == 'white':
      FENInfo = 'K'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/white king.png'
    else:
      FENInfo = 'k'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/black king.png'
    return f'{FENInfo},{pathToImage}'
      
def queen(self, color: str, initialPiecePosition: int):

    if color == 'white':
      FENInfo = 'Q'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/white queen.png'
    else:
      FENInfo = 'q'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/black queen.png'
    return f'{FENInfo},{pathToImage}'

def rook(self, color: str, initialPiecePosition: int):

    if color == 'white':
      FENInfo = 'R'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/white rook.png'
    else:
      FENInfo = 'r'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/black rook.png'
    return f'{FENInfo},{pathToImage}'
    
def bishop(self, color: str, initialPiecePosition: int):

    if color == 'white':
      FENInfo = 'B'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/white bishop.png'
    else:
      FENInfo = 'b'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/black bishop.png'
    return f'{FENInfo},{pathToImage}'
    
def knight(self, color: str, initialPiecePosition: int):

    if color == 'white':
      FENInfo = 'N'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/white knight.png'
    else:
      FENInfo = 'n'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/black knight.png'
    return f'{FENInfo},{pathToImage}'
    
def pawn(self, color: str, initialPiecePosition: int):

    if color == 'white':
      FENInfo = 'P'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/white pawn.png'
    else:
      FENInfo = 'p'
      pathToImage = f'{os.path.dirname(__file__)}/pieces/black pawn.png'
    return f'{FENInfo},{pathToImage}'
    
root = tk.Tk()
g = game(root)
g.createGameInstance()
root.mainloop()
