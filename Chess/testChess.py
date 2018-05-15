import chess as c# This file is just for testing so it is allowed to violate abstraction

print("Checking setVars()")
c.setVars()

print("Checking isGameOver(board)")
assert(c.isGameOver(board) == False)

print("Checking isValidPos(board, start, finish)")
assert(c.isValidPos([8, 8]) == False) # Fence-post error check
assert(c.isValidPos([100298, 301847]) == False) # Normal error check

print("Checking isValidMove(board, piece, start, finish)")
assert(c.isValidMove(board, c.w6, [0, 7], [0, 6]) == True) # 1 Square move (pawn)
assert(c.isValidMove(board, c.w6, [0, 7], [0, 5]) == True) # 2 Square move (pawn)
