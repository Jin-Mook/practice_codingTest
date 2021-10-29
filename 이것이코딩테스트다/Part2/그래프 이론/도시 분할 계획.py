# 신장트리 알고리즘으로 전체 마을이 이어지게 만들고
# 마지막에 유지비가 가장 큰 길을 뺀다.
import sys
input = sys.stdin.readline
# 마을과 길 입력받기
n, m = map(int,input().split())

# 마을 구조와 유지비 입력받기
graph = []
for _ in range(m):
  a, b, cost = map(int, input().split())
  graph.append((cost, a, b))

# 유지비가 작은 순으로 정렬
graph.sort()
result = 0  # 총 비용

# 부모 리스트
parent = [ i for i in range(n+1)]

# 부모가 같은지 확인하는 함수
def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

# 서로 합치는 함수
def union(parent, a, b):
  _a = find_parent(parent, a)
  _b = find_parent(parent, b)

  if _a < _b:
    parent[_b] = _a
  else:
    parent[_a] = _b

# 최소 신장트리에서 마지막에 가장 비용이 큰 부분을 빼준다.
for i in range(len(graph)):
  cost, a, b = graph[i]
  if find_parent(parent, a) != find_parent(parent, b):
    result += cost
    last = cost
    union(parent, a, b)

print(result - last)