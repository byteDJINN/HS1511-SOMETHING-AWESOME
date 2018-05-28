import userChess as u
import random as r
import variableAi1 as ai1
import variableAi2 as ai2
import sys, time

ai1.checkSettings()
ai2.checkSettings()
minSpeed = int(input("What is the minimum move delay [seconds]: "))


u.showBoard(u.getBoard()) # Show board starting state
while not u.isGameOver(u.getBoard()):
  print() # Create gap between turns
  print("Turn %s" % u.getTurnNumber())
  if u.getTurnNumber() % 2 == 0: # If it is an even number
    print("WHITE'S TURN")
    start, finish = ai1.decideMove()
    print(u.getBoard()[start[0]][start[1]],"was moved from",start,"to",finish)
    u.movePiece(u.getBoard(), start, finish)
    u.showBoard(u.getBoard())
  else: # It is black's turn
    print("BLACK'S TURN")
    start, finish = ai2.decideMove()
    print(u.getBoard()[start[0]][start[1]],"was moved from",start,"to",finish)
    u.movePiece(u.getBoard(), start, finish)
    u.showBoard(u.getBoard())

  time.sleep(minSpeed)
  
  
print()
wKing, bKing = u.isGameOver(u.getBoard())
if wKing:
  print("White Won!!!")
else:
  print("Black Won!!!")
