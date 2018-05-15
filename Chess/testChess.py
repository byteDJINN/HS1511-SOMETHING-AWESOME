import chess as c # This file is just for testing so it is allowed to violate abstraction

print("Checking setVars()")
c.setVars()

print("Checking isGameOver(board)")
if not (c.isGameOver(board) == False):
  print("isGameOver failed.")

print("Checking isValidPos(board, start, finish)")
if not (c.isValidPos([8, 8]) == False): # Fence-post error check
  print("isValidPos failed.")
if not (c.isValidPos([100298, 301847]) == False): # Normal error check
  print("isValidPos failed.")

print("Checking isValidMove(board, piece, start, finish)")
if not (c.isValidMove(board, c.w6, [0, 7], [0, 6]) == True): # 1 Square move (pawn)
  print("isValidMove failed.")
if not (c.isValidMove(board, c.w6, [0, 7], [0, 5]) == True): # 2 Square move (pawn)
  print("isValidMove failed.")

print("All tests passed. You are AWESOME!!!")
