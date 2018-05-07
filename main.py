# IMPORTS

# FUNCTIONS
def setVars():
  # Create dictionary of pieces.
  global pieces = {}
  pieces['white']['king'] = '♔'
  pieces['white']['queen'] = '♕'
  pieces['white']['rook'] = '♖'
  pieces['white']['bishop'] = '♗'
  pieces['white']['knight'] = '♘'
  pieces['white']['pawn'] = '♙'
  
  pieces['black']['king'] = '♚'
  pieces['black']['queen'] = '♛'
  pieces['black']['rook'] = '♜'
  pieces['black']['bishop'] = '♝'
  pieces['black']['knight'] = '♞'
  pieces['black']['pawn'] = '♟'
  
  # Create the board
  global board = [['.' for x in range(8)] for y in range(8)]

def showBoard():
  global board
  for x in range(8):
    for y in range(8):
      print(str(x),"|",board[x][y])
  print(" | abcdefgh")
  

# MAIN
