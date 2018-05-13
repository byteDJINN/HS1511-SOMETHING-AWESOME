import userChess as u

def decideMove():
  board = u.getBoard()
  start = list(input("Start: ")) # In format "x y"
  finish = list(input("Finish: ")) # In format "x y"
  return u.movePiece(board, start, finish)

