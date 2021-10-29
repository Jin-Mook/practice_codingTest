import sys
input = sys.stdin.readline

# n, m 받기
n, m = map(int, input().split())

#부모 배열
parent = [i for i in range(n + 1)]

# 부모를 찾는 함수
# 따라서 부모가 같으면 같은 팀으로 간주할 수 있다.
def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

# 팀을 합치는 함수
def union(parent, a, b):
  # 부모가 같다면 합칠 필요가 없다.
  if find_parent(parent, a) == find_parent(parent, b):
    return "YES"
  # 다른 경우
  a_parent = find_parent(parent, a)
  b_parent = find_parent(parent, b)
  if a_parent < b_parent:
    parent[b_parent] = a_parent
  else:
    parent[a_parent] = b_parent 

for _ in range(m):
  x, a, b = map(int, input().split())
  if x == 0:
    union(parent, a, b)
  else:
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    else:
      print("NO")

