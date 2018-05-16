# IMPORTS
import userChess as u
import random

# FUNCTIONS


  
def decideMove():
  checkSettings()
  if version == 0:
    start, finish = decideMove0()
  if version == 1:
    start, finish = decideMove1()

  return [start, finish] # start and finish are [x, y]
  
def setMode(mode):
  global version
  version = mode

def checkSettings():
  global version
  try:
    version += 0
  except:
    setMode(int(input("What AI Version For Black: ")))

# AI VERSION 0
def decideMove0():
  start = list(map(int, input("Start: ").split())) # In format "x y"
  finish = list(map(int, input("Finish: ").split())) # In format "x y"
  return start, finish # start and finish are [x, y]

# AI VERSION 1
def decideMove1():
  start = [random.randint(0, 8), random.randint(0, 8)]
  finish = [random.randint(0, 8), random.randint(0, 8)]
  while not u.isValid(u.getBoard(), start, finish):
    start = [random.randint(0, 8), random.randint(0, 8)]
    finish = [random.randint(0, 8), random.randint(0, 8)]
  return start, finish
