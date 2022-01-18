import sys
n = int(input())

def input():
  return sys.stdin.readline().strip()

lists = []
for _ in range(n):
  lists.append(input().split())

lists.sort(key=lambda x: int(x[0]))
for l in lists:
  print(' '.join(l))