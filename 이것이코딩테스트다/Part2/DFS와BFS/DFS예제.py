#DFS 메서드 정의

# graph는 노드가 연결된 정보를 리스트 자료형으로 표현
# v는 현재 위치한 노드
# visited 는 각 노드가 방문된 정보를 리스트 자료형으로 표현
def dfs(graph, v, visited):
  visited[v] = True  # v 위치는 방문한 것으로 체크
  print(v, end=' ')

  for i in graph[v]:   # v위치에서 연결된 각 노드를 확인할 때 재귀함수를 이용
    if visited[i] == False:
      dfs(graph, i, visited)


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

dfs(graph, 1, visited);