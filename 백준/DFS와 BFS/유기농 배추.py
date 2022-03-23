import sys
import copy
input = sys.stdin.readline

test = int(input())

# 이미 확인한 부분인지 알기 위한 check = [[0,0,0...]...]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
count = 0

def dfs(vege_loc, x, y, check, len_x, len_y):
  global count

  if vege_loc[y][x] == 0 or check[y][x] == 1:
    return False
  
  if vege_loc[y][x] == 1 and check[y][x] == 0:
    check[y][x] = 1
    # count += 1
    for i in range(4):
      new_y = y+dy[i]
      new_x = x+dx[i]

      if new_y >= 0 and new_y < len_y and new_x >= 0 and new_x < len_x:
        dfs(vege_loc, new_x, new_y, check, len_x, len_y)
    return True


for _ in range(test):
  count = 0
  len_x, len_y, k = map(int, input().split())
  check = [[0 for _ in range(len_x)] for _ in range(len_y)]
  vege_loc = copy.deepcopy(check)
  for _ in range(k):
    x, y = map(int, input().split())
    vege_loc[y][x] = 1
  
  for y in range(len_y):
    for x in range(len_x):
      if dfs(vege_loc, x, y, check, len_x, len_y):
        count += 1
  print(count)

