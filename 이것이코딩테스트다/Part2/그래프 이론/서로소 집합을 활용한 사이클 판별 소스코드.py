# 이 알고리즘은 간선에 방향성이 없는 무향 그래프에서만 작동 가능하다.

# 특정 원소가 속한 집합을 찾기
# 경로 압축 기법 이용
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  _a = find_parent(parent, a)
  _b = find_parent(parent, b)
  
  if _a < _b:
    parent[_b] = _a
  else:
    parent[_a] = _b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)

# 부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(v + 1):
  parent[i] = i

# 사이클 발생 여부
cycle = False

for i in range(e):
  a, b = map(int, input().split())
  # 간선을 확인했을때 서로 루트 노드가 같다면 사이클이 발생한 경우이다.
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  # 사이클이 발생하지 않았다면 합집합 과정을 수행한다.
  else:
    union_parent(parent, a, b)

if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지 않았습니다.")