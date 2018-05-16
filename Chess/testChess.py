import chess as c # This file is just for testing so it is allowed to violate abstraction

def printCheck(status, check): # Status is True or False, Check is the test number
  if status:
    print("Test " + str(check) + ": succeeded.")
  else:
    print("Test " + str(check) + ": failed.")

print("Checking setVars()")
c.setVars()
printCheck(c.pieces["white"]["king"] == c.w1, 1)

print("\nChecking isGameOver(board)")
printCheck(not c.isGameOver(c.board), 1)

print("\nChecking isValidPos(board, start, finish)")
printCheck(not c.isValidPos([8, 8]), 1) # Fence-post error check
printCheck(not c.isValidPos([100298, 301847]), 2) # Normal error check

print("\nChecking isValidMove(board, piece, start, finish)")
printCheck(c.isValidMove(c.board, c.w6, [0, 7], [0, 6]), 1) # 1 Square move (pawn)
printCheck(c.isValidMove(c.board, c.w6, [0, 7], [0, 5]), 2) # 2 Square move (pawn)

print("\nChecking isObstruction(start, finish)")
printCheck(c.isObstruction([0, 6], [0, 5]), 1)

print("\nTesting Complete.")
