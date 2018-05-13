'''
This is the file that the user is allowed to import when they make their own AI. To avoid violation of abstraction the user will not
use any functions from the chess.py file, and to easily avoid this they will only use the functions listed here.

NOTE: For simplification, to win you must take the opponents king.
'''

import chess as c
import sys

def getBoard():
  '''
  Returns a matrix in the form [[.., .., .., ...], [.., .., .., ...], ...] where the piece on (x, y) can be accessed by doing
  board[x-1][y-1] (assuming that x and y are between 1 and 8).
  '''
  return c.getBoard()
  
def isValid(board, start, finish):
  return c.isValid(board, start, finish)
  
def movePiece(board, start, finish):
  return c.movePiece(board, start, finish)

def getTurnNumber():
  return c.turnNumber

def isGameOver(board):
  return c.isGameOver(board)
    
def setBoard(board):
  '''
  AI is not allowed to use this function.
  '''
  assert(sys.argv[0][len(sys.argv[0])-12::] == "/runChess.py") # SECURITY
  c.board = board

