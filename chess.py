# IMPORTS



# FUNCTIONS

def setVars():
  
  # Create dictionary of pieces.
  print("SPONTANEOUSLY CREATING PIECES...")
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
  print("GIVING PIECES SHORT NAMES...")
  global w1,w2,w3,w4,w5,w6,b1,b2,b3,b4,b5,b6
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
  print("SPONTANEOUSLY CREATING A BOARD...")
  global board
  board = [['\u2001' for x in range(8)] for y in range(8)]
  
  # Set up white pieces
  print("SETTING UP WHITE PIECES...")
  y = 0
  for piece in [w3, w5, w4, w2, w1, w4, w5, w3]: # Non-Pawns
    board[0][y] = piece
    y += 1
  for y in range(8): # Pawns
    board[1][y] = w6
    
  # Set up black pieces
  print("SETTING UP BLACK PIECES...")
  y = 0
  for piece in [b3, b5, b4, b2, b1, b4, b5, b3]: # Non-Pawns
    board[7][y] = piece
    y += 1
  for y in range(8): # Pawns
    board[6][y] = b6
  
  # Create game information
  print("WRITING DOWN GAME INFORMATION...")
  turnNumber = 0
  
  # Done
  print("STARTING THE GAME...")
  

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
    print(c+"\u200A",end="") # Note: Close but not 100% accurate
  print()

def movePiece(start, finish): # start and finish are [x, y] of piece to be moved
  if isValidPos(start) and isValidPos(finish) and isValidMove(board[start[0]][start[1]], start, finish):
    
    return True
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
    if start[1] == 1 and isValidYMove(start, finish, 2, forceForward=True): # If it is the first turn
      return True
    elif isValidYMove(start, finish, 1, forceForward=True):
      return True
    # Add elif it goes diagonally

def isValidXMove(start, finish, distance=-1, obstructions=True): # Move along x-axis.
  if distance == -1:
    isValid = (abs(start[1] - finish[1]) == 0)
  else:
    isValid = (abs(start[0] - finish[0]) == distance and abs(start[1] - finish[1]) == 0)
  

def isValidYMove(start, finish, distance=-1, forceForward=False): # Move along y-axis
  if forceForward:
    return (start[0] - finish[0] == 0 and start[1] - finish[1] == -distance) # Since pawns can only go forward
  elif distance == -1:
    return (abs(start[0] - finish[0]) == 0)
  else:
    return (abs(start[0] - finish[0]) == 0 and abs(start[1] - finish[1]) == distance)

def isValidZMove(start, finish, distance=-1): # Move along diagonal.
  if distance == -1:
    return  (abs(start[0] - finish[0]) == abs(start[1] - finish[1]))
  else:
    return (abs(start[0] - finish[0]) == abs(start[1] - finish[1]) == distance)

def isObstruction(start, finish): # FINISH THIS!!!
  return False
  
# MAIN

setVars()
showBoard()
