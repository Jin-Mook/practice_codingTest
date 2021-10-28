# parent는 부모 노드를 얘기하는 것이다.
# 부모노드와 루트 노드는 다르다. 즉 어떤 노드의 부모노드가 루트노드가 아닌경우
# 그 어떤 노드의 부모노드의 부모노드를 찾는 과정을 거쳐 최종적으로
# 자기가 루트인 노드를 찾아가는 것이다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a_parent = find_parent(parent, a)
  b_parent = find_parent(parent, b)
  if a_parent < b_parent:
    parent[b_parent] = a_parent
  else:
    parent[a_parent] = b_parent

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v + 1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(v + 1):
  parent[i] = i

# union 연산을 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v + 1):
  print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
  print(parent[i], end=' ')
