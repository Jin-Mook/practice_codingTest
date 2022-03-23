import sys
from collections import deque
input = sys.stdin.readline

len_x, len_y = map(int, input().split())
board = []
for _ in range(len_y):
  line = list(map(int, input().split()))
  board.append(line)

# [[1,1], [5, 5]] 의 형태로 해당 날짜에 모두 체크해야되는 리스트를 묶어서 q에 넣자.
check = [[0 for _ in range(len_x)] for _ in range(len_y)]

start = []
for i in range(len_y):
  for j in range(len_x):
    if board[i][j] == 1:
      start.append([i, j])
      # check[i][j] = 1
    if board[i][j] == -1:
      check[i][j] = 1

# print(start)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque([])

q.append(start)
def bfs():
  day = -1
  # 다음날 모든 익은 토마토를 확인한다.
  while q:
    day += 1

    start = q.popleft()
    new_start = []
    for y, x in start:
      for i in range(4):
        new_y, new_x = y+dy[i], x+dx[i]
        if new_y >= 0 and new_y < len_y and new_x >= 0 and new_x < len_x:
          if board[new_y][new_x] == 0 and check[new_y][new_x] == 0:
            check[new_y][new_x] = 1
            board[new_y][new_x] = 1
            new_start.append([new_y, new_x])

    if new_start != []:
      q.append(new_start)

  # 모든 작업을 완료하고 하루라도 0이 있다면
  for i in range(len_y):
    for j in range(len_x):
      if board[i][j] == 0:
        return -1
  
  return day

print(bfs())