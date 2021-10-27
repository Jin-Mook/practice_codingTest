import sys
import heapq

input = sys.stdin.readline
# 도시의 개수 n, 통로의 개수 m 메시지를 보내고자 하는 도시 c
n, m ,c = map(int, input().split())

# 거리를 담을 리스트 초기화
inf = int(1e9)
distance = [inf] * (n + 1)

# 각 노드의 정보를 담을 리스트
graph = [[] for _ in range(n+1)]
# 각 노드에 대해 연결된 노드와 시간에 대한 정보 넣기
for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

q = []
def find_city_time(c):
  heapq.heappush(q, (0, c))
  distance[c] = 0

  while q:
    dist, city = heapq.heappop(q)
    
    if dist > distance[city]:
      continue

    for node in graph[city]:
      cost = dist + node[1]

      if cost < distance[node[0]]:
        distance[node[0]] = cost
        heapq.heappush(q, (cost, node[0]))

find_city_time(c)

city_count = 0
for i in range(0, n+1):
  if distance[i] != inf and distance[i] != 0:
    city_count += 1
  else:
    distance[i] = -1

print(city_count, max(distance))