from collections import deque

#n, m 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보를 입력받기
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

def bfs(y, x):
  queue = deque()
  queue.append((y, x))
  
  # 이동할 4 방향 정의 상 하 좌 우
  dy = [1, -1, 0, 0]
  dx = [0, 0, -1, 1]
  
  # queue가 0이 될 때까지 즉 맵의 모든 위치를 확인할때까지
  while len(queue) != 0:
    # 큐에서 첫번째 위치를 먼저 뺀다.
    y, x = queue.popleft()
    # 이후에 뺀 위치에서 가능한 4가지 경우를 모두 확인하고 가능한 위치만 큐에 추가해준다
    # 추가할때 이전 위치 값에서 1을 더해준다.
    for i in range(4):
      new_y = y + dy[i]
      new_x = x + dx[i]
      if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and graph[new_y][new_x] == 1:
        graph[new_y][new_x] = graph[y][x] + 1
        queue.append((new_y, new_x))

bfs(0, 0)
print(graph[n-1][m-1])
