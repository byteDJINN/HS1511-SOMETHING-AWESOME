# IMPORTS
import userChess

# FUNCTIONS

def getRating():
  # Produces a rating of the position of a board
  
def decideMove():
  checkSettings()
  # Blah Blah Blah
  # Decide what to do...
  
  movePiece(piece, start, finish) # Make the move
  
def setMode(mode):
  global version
  version = mode

def checkSettings():
  global version
  try:
    version += 0
  except:
    setMode(int(input("What AI Version: ")))

