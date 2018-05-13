# IMPORTS
import userChess as u

# FUNCTIONS

def getRating():
  # Produces a rating of the position of a board
  return 0
  
def decideMove():
  checkSettings()
  if version == 0:
    start, finish = decideMove0()

  return [start, finish] # start and finish are [x, y]
  
def setMode(mode):
  global version
  version = mode

def checkSettings():
  global version
  try:
    version += 0
  except:
    setMode(int(input("What AI Version: ")))

def decideMove0():
  start = list(map(int, input("Start: ").split())) # In format "x y"
  finish = list(map(int, input("Finish: ").split())) # In format "x y"
  return start, finish # start and finish are [x, y]

