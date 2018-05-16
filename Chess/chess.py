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
  global board
  board = [[0 for x in range(8)] for y in range(8)]
  
  # Set up white pieces
  y = 0
  for piece in [w3, w5, w4, w2, w1, w4, w5, w3]: # Non-Pawns
    board[0][y] = piece
    y += 1
  for y in range(8): # Pawns
    board[1][y] = w6
    
  # Set up black pieces
  y = 0
  for piece in [b3, b5, b4, b2, b1, b4, b5, b3]: # Non-Pawns
    board[7][y] = piece
    y += 1
  for y in range(8): # Pawns
    board[6][y] = b6
  
  # Create game information
  global turnNumber
  turnNumber = 1
  

def showBoard(board):
  for x in range(8):
    
    print(str(x),'|',end='')
    for y in range(8):
      if board[x][y] == 0:
        print("\u2001",end='')
      else:
        print(board[x][y],end='')
    print()
  print("  |",end="")
  for c in '01234567':
    print(c+"\u200A",end="") # Note: Close but not 100% accurate
  print()

def isGameOver(board):
  wKing = False
  bKing = False
  for row in board:
    for square in row:
      if square == w1:
        wKing = True
      elif square == b1:
        bKing = True

  if not (wKing and bKing):
    return [wKing, bKing]
  return False

def movePiece(board, start, finish): # start and finish are [x, y] of piece to be moved
  board[finish[0]][finish[1]] = board[start[0]][start[1]]
  board[start[0]][start[1]] = 0 # Reset square
  return board

def isValid(board, start, finish):
  return isValidPos(start) and isValidPos(finish) and isValidPiece(board, start) and isValidMove(board, start, finish)

def isValidPiece(board, start):
  p = board[start[0]][start[1]]
  valid = False
  if turnNumber % 2 == 1 and p in [w1, w2, w3, w4, w5]:
    valid = True
  elif turnNumber % 2 == 0 and p in [b1, b2, b3, b4, b5]:
    valid = True
  return valid
    

def isValidPos(cords): # cords is a list of [x, y]
  return cords[0]>-1 and cords[0] < 8 and cords[1]>-1 and cords[1]<8

def isValidMove(board, start, finish):
  piece = board[start[0]][start[1]] # For ease of understanding
  valid = None

  if start == finish:
    valid = False
  elif piece == w1 or piece == b1: # King
    if isValidXMove(start, finish, distance=1) or isValidYMove(start, finish, distance=1) or isValidZMove(start, finish, distance=1):
      valid = True
    else:
      valid = False
  elif piece == w2 or piece == b2: # Queen
    if isValidXMove(start, finish) or isValidYMove(start, finish) or isValidZMove(start, finish):
      valid = True
    else:
      valid = False
  elif piece == w3 or piece == b3: # Rook
    if isValidXMove(start, finish) or isValidYMove(start, finish):
      valid = True
    else:
      valid = False
  elif piece == w4 or piece == b4: # Bishop
    if isValidZMove(start, finish):
      valid = True
    else:
      valid = False
  elif piece == w5 or piece == b5: # Knight
    xDiff = abs(start[0]-finish[0])
    yDiff = abs(start[1]-finish[1])
    if xDiff == 1 and yDiff == 2:
      valid = True
    elif xDiff == 2 and yDiff == 1:
      valid = True
    else:
      valid = False
  elif piece == w6 or piece == b6: # Pawn
    if start[1] == 1 and isValidYMove(start, finish, 2, forceForward=True): # If it is the first time the piece is being moved
      valid = True
    elif isValidYMove(start, finish, 1, forceForward=True):
      valid = True
    elif isValidZMove(start, finish, distance=1, forceForward=True) and board[finish[0]][finish[1]] != 0: # When the pawn is taking diagonally
      valid = True
    else:
      valid = False
  else:
    valid = False
  if valid and piece != w5 and piece != b5 and isObstruction(start, finish): # Check for obstructions
    valid = False
  return valid


def isValidXMove(start, finish, distance=-1): # Move along x-axis.
  if distance == -1:
    isValid = (abs(start[1] - finish[1]) == 0)
  else:
    isValid = (abs(start[0] - finish[0]) == distance and abs(start[1] - finish[1]) == 0)

def isValidYMove(start, finish, distance=-1, forceForward=False): # Move along y-axis
  if forceForward and distance != -1:
    return (start[0] - finish[0] == 0 and start[1] - finish[1] == -distance) # Since pawns can only go forward
  elif forceForward:
    return (start[0] - finish[0] == 0 and start[1] - finish[1])
  elif distance == -1:
    return (abs(start[0] - finish[0]) == 0)
  else:
    return (abs(start[0] - finish[0]) == 0 and abs(start[1] - finish[1]) == distance)

def isValidZMove(start, finish, distance=-1, forceForward=False): # Move along diagonal.
  if forceForward and distance != -1:
    return (abs(start[0] - finish[0]) == finish[1] - start[1] == distance)
  elif forceForward:
    return (abs(start[0] - finish[0]) == finish[1] - start[1])
  elif distance == -1:
    return (abs(start[0] - finish[0]) == abs(start[1] - finish[1]))
  else:
    return (abs(start[0] - finish[0]) == abs(start[1] - finish[1]) == distance)

def isObstruction(start, finish): 
  global board # Get the board
  inBetween = []
  biggerX = max(start[0], finish[0])
  smallerX = min(start[0], finish[0])
  biggerY = max(start[1], finish[1])
  smallerY = min(start[1], finish[1])
  if biggerX == smallerX: # Same y-axis
    for i in range(1, biggerY - smallerY+1):
      inBetween.append([biggerX, biggerY-i])
  elif biggerY == smallerY: # Same x-axis
    for i in range(1, biggerX - smallerX+1):
      inBetween.append([biggerX-i, biggerY])
  elif start[0] < finish[0] and start[1] < finish[1]: # A diagonal going upwards
    for i in range(1, biggerX - smallerX+1):
      inBetween.append([smallerX+i, smallerY+i])
  elif start[0] > finish[0] and start[1] > finish[1]: # A diagonal going downwards
    for i in range(1, biggerX - smallerX+1):
      inBetween.append([smallerX-i, biggerY-i])
  print(inBetween)
  for x, y in inBetween: # Check if pieces are on the squares
    if board[x][y] != 0:
      return True
  return False
    
def getBoard(): # Returns the board matrix
  global board # Gets the real board
  try: # Check if board exists
    assert(board)
  except:
    setVars()
  return board # Returns a copy

