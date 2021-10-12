from collections import deque

def bfs(graph, start, visited):
  # 큐 구현을 위해 덱 모듈 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True

  # 큐가 빌때까지 진행한다.
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True




graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited);