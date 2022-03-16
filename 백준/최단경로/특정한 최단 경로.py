import heapq
import sys
input = sys.stdin.readline


v, e = map(int, input().split())

direction = [[] for _ in range(v + 1)]
inf = int(1e9)

for _ in range(e):
  start, end, value = map(int, input().split())
  direction[start].append([end, value])
  direction[end].append([start, value])

v1, v2 = map(int, input().split())

def dijkstra(start, end):
  weights = [inf] * (v+1)
  weights[start] = 0
  q = []
  heapq.heappush(q, [0, start])
  while q:
    dist, now = heapq.heappop(q)
    if weights[now] < dist:
      continue
    
    for new, new_dist in direction[now]:
      cost = dist + new_dist
      if cost < weights[new]:
        weights[new] = cost
        heapq.heappush(q, [cost, new])
  return weights[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, v)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, v)

if path1 >= inf and path2 >= inf:
  print(-1)
else:
  print(min(path1, path2))