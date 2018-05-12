import sys
import userChess as u
import random as r
# Set up white and black
if r.randint(0, 1):
  import makesUSufferAi as ai1
  import opponentAi as ai2
else:
  import makesUSufferAi as ai2
  import opponentAi as ai1

while not u.isGameOver(u.getBoard):
  if u.getTurnNumber() % 2 == 1: # If it is an odd number
    setBoard(ai1.decideMove())
  else:
    setBoard(ai2.decideMove())

wKing, bKing = u.isGameOver(u.getBoard())
if wKing:
  print("White Won!!!")
else:
  print("Black Won!!!")
