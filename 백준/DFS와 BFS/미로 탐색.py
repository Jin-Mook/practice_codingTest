from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
  nums = input()
  temp = []
  for i in range(m):
    temp.append(int(nums[i]))
  board.append(temp)
check = [[False] * m for _ in range(n)]
# print(board)
result = 1
flag = True
check[0][0] = True
d = deque([[0, 0, result]])
while flag:
  x, y, result = d.popleft()
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  # print('loc: ', x, y, result)
  for i in range(4):
    new_x = x + dx[i]
    new_y = y + dy[i]
    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or board[new_x][new_y] == 0 or check[new_x][new_y] == True:
      continue
    d.append([new_x, new_y, result+1])
    check[new_x][new_y] = True
    if new_x == n-1 and new_y == m-1:
      flag = False
      break

print(result+1)