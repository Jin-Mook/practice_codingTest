import sys
input = sys.stdin.readline

node = int(input())
num_lines = int(input())

lines = [[] for _ in range(node+1)]
check = [False for _ in range(node+1)]
for _ in range(num_lines):
  first, second = map(int, input().split())
  lines[first].append(second)
  lines[second].append(first)

# print(lines, check)

count = 0
check[1] = True
def dfs(start):
  global count
  for new_node in lines[start]:
    if check[new_node] == False:
      count += 1
      check[new_node] = True
      dfs(new_node)
  return count

print(dfs(1))