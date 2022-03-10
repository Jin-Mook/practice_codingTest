import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
lines = [[] for _ in range(n+1)]
check1 = [False for _ in range(n+1)]
check2 = copy.deepcopy(check1)

for _ in range(m):
  first, second = map(int, input().split())
  lines[first].append(second)
  lines[second].append(first)

for line in lines:
  line.sort()

# DFS => 스택 이용
def dfs(start):
  check1[start] = True
  print(start, end=' ')
  for next in lines[start]:
    if check1[next] == True:
      continue
    check1[next] = True
    dfs(next)

dfs(v)
print()

# BFS => 덱 구조 이용
def bfs(start):
  bfs_list = deque([start])
  while bfs_list:
    # print(bfs_list)
    pop_node = bfs_list.popleft()
    if check2[pop_node] == True:
      continue
    print(pop_node, end=' ')
    check2[pop_node] = True
    for node in lines[pop_node]:
      if check2[node] == True:
        continue
      bfs_list.append(node)
bfs(v)
