# IMPORTS



# FUNCTIONS

def setVars():
  # Create dictionary of pieces.

  global pieces
  pieces = {'white': {}, 'black': {}}
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

  # Create shorthand
  w1 = pieces['white']['king']
  w2 = pieces['white']['queen']
  w3 = pieces['white']['rook']
  w4 = pieces['white']['bishop']
  w5 = pieces['white']['knight']
  w6 = pieces['white']['pawn']
 
  b1 = pieces['black']['king']
  b2 = pieces['black']['queen']
  b3 = pieces['black']['rook']
  b4 = pieces['black']['bishop']
  b5 = pieces['black']['knight']
  b6 = pieces['black']['pawn']

  # Create the board
  global board
  board = [['\u2001' for x in range(8)] for y in range(8)]
  
  # Put on white pieces
  y = 0
  for piece in [w3, w5, w4, w2, w1, w4, w5, w3]: # Non-Pawns
    board[0][y] = piece
    y += 1
  for y in range(8): # Pawns
    board[1][y] = w6
    
  # Put on black pieces
  y = 0
  for piece in [b3, b5, b4, b2, b1, b4, b5, b3]: # Non-Pawns
    board[7][y] = piece
    y += 1
  for y in range(8): # Pawns
    board[6][y] = b6
  

def showBoard():
  global board
  for x in range(8):
    print()
    print(str(x+1),'|',end='')
    for y in range(8):
      print(board[x][y],end='')
  print()
  print("  |",end="")
  for c in 'abcdefgh':
    print(c+"\u200A",end="") # NOTE: Close but not 100% accurate
  print()

def movePiece(start, finish): # start and finish are [x, y] of piece to be moved
  if isValidPos(start) and isValid(finish):
    pass
  else:
    return False
  
def getRating(board):
  # Generate number based on how good each side is


def isValidPos(cords): # cords is a list of [x, y]
  return cords[0]>-1 and cords[0] < 8 and cords[1]>-1 and cords[1]<8

def isValidMove(piece, start, finish):
  if piece == w1 or piece == b1:
    if isValidXMove(start, finish, distance=1) or isValidYMove(start, finish, distance=1) or isValidZMove(start, finish, distance=1):
      return True
    else:
      return False
  elif piece == w2 or piece == b2:
    if isValidXMove(start, finish) or isValidYMove(start, finish) or isValidZMove(start, finish):
      return True
    else:
      return False
  elif piece == w3 or piece == b3:
    if isValidXMove(start, finish) or isValidYMove(start, finish):
      return True
    else:
      return False
  elif piece == w4 or piece == b4:
    if isValidZMove(start, finish):
      return True
    else:
      return False
  elif piece == w5 or piece == b5:
    pass # PUT STUFF HERE
  elif piece == w6 or piece == b6:
    pass # PUT STUFF HERE

def isValidXMove(start, finish, distance=-1): # Move along x-axis.
  if distance == -1:
    return (abs(start[1] - finish[1]) == 0)
  else:
    return (abs(start[0] - finish[0]) == distance and abs(start[1] - finish[1]) == 0)

def isValidYMove(start, finish, distance=-1): # Nove along y-axis.
  if distance == -1:
    return (abs(start[0] - finish[0]) == 0)
  else:
    return (abs(start[0] - finish[0]) == 0 and abs(start[1] - finish[1]) == distance)

def isValidZMove(start, finish, distance=-1): # Move along diagonal.
  if distance == -1:
    return  (abs(start[0] - finish[0]) == abs(start[1] - finish[1]))
  else:
    return (abs(start[0] - finish[0]) == abs(start[1] - finish[1]) == distance)

# MAIN

setVars()
showBoard()
