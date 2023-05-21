import tkinter

class game: 
  
  def __init__(self, initialPosition):
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
print(g)