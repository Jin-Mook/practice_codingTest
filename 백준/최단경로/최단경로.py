import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
first = int(input())
direction = [[] for _ in range(v+1)]
for i in range(e):
  start, end, value = map(int, input().split())
  direction[start].append([end, value])


inf = int(1e9)
weights = [inf] * (v+1)

def dijkstra(start):
  q = []
  heapq.heappush(q, [0, start])
  weights[start] = 0
  while q:
    dist, now = heapq.heappop(q)

    if weights[now] < dist:
      continue
    
    for new, value in direction[now]:
      cost = dist + value
      if cost < weights[new]:
        weights[new] = cost
        heapq.heappush(q, [cost, new])

dijkstra(first)

for i in range(1, v+1):
  if weights[i] == inf:
    print('INF')
  else:
    print(weights[i])
    




