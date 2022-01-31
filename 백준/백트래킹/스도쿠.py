import sys

board = []

for i in range(9):
  board.append(list(map(int, sys.stdin.readline().split())))

print(board)