
n, m = map(int, input().split())

board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

count = 0

def dfs(board, y, x):
  board[y][x] = 1
  new_location = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
  for new_y, new_x in new_location:
    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and board[new_y][new_x] == 0:
      dfs(board, new_y, new_x)


for y in range(n):
  for x in range(m):
   # 얼음판을 돌아가며 0인 부분을 찾자
   # 0인 부분을 찾으면 거기서부터 DFS 를 적용해보자
   # 이때 0인 부분에서 다음 부분으로 일반적으로 상, 하, 좌, 우 4군데 진행
   # 끝부분 예외처리 신경
   if board[y][x] == 0:
     dfs(board, y, x)
     count += 1

print(count)