import userChess as u
import random as r
# Set up white and black
if r.randint(0, 1):
  import variableAi as ai1
  import variableAi as ai2
else:
  import variableAi as ai2
  import variableAi as ai1

while not u.isGameOver(u.getBoard()):
  u.showBoard(u.getBoard())
  if u.getTurnNumber() % 2 == 1: # If it is an odd number
    start, finish = ai1.decideMove()
    u.movePiece(start, finish)
  else:
    start, finish = ai2.decideMove()
    u.movePiece(start, finish)
  

wKing, bKing = u.isGameOver(u.getBoard())
if wKing:
  print("White Won!!!")
else:
  print("Black Won!!!")
