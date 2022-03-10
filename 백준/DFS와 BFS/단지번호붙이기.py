import sys
input = sys.stdin.readline

n = int(input())
board = []
check = []
for _ in range(n):
  board_input = input()
  temp = [int(board_input[i]) for i in range(n)]
  temp_check = [False] * n
  board.append(temp)
  check.append(temp_check)

def bfs(x, y):
  global count
  if check[x][y] == True:
    return 0
  check[x][y] = True
  if board[x][y] == 1:
    count += 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
      new_x = x + dx[i]
      new_y = y + dy[i]
      if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
        continue

      bfs(new_x, new_y)
  return count

result_list = []
result = 0
for i in range(n):
  for j in range(n):
    count = 0
    num = bfs(i, j)
    if num != 0:
      result += 1
      result_list.append(num)

print(result)
result_list.sort()
for _result in result_list:
  print(_result)