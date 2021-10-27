import sys
input = sys.stdin.readline

# 도시의 개수 n, 경로의 개수 m
n, m = map(int, input().split())

# 초기값으로 가장 크게 설정해준다.
inf = int(1e9)
# 연결된 길을 나타내는 2차원 배열
graph = [[inf] * (n + 1) for _ in range(n+1)]

# 자기 자신에게 가는 길에 걸리는 시간은 0이다.
for i in range(1, n+1):
  graph[i][i] = 0

# 값이 1이라면 서로 연결된 상태이다.
for _ in range(m):
  i, j = map(int, input().split())
  graph[i][j] = 1
  graph[j][i] = 1

print(graph)
# 최종 목적지 x 와 소개팅 자리 k 값 받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for mid in range(1, n + 1):
  for start in range(1, n + 1):
    for last in range(1, n + 1):
      graph[start][last] = min(graph[start][last], graph[start][mid] + graph[mid][last])
print(graph)

# 최종 결과
distance = graph[1][k] + graph[k][x]

# 결과 출력
if distance >= inf:
  print(-1)
else:
  print(distance)
