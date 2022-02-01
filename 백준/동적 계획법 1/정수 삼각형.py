import sys
input = sys.stdin.readline

tri = []
n = int(input())
for _ in range(n):
  tri.append(list(map(int, input().split())))

# print(tri)

for i in range(1, len(tri)):
  for j in range(len(tri[i])):
    # j가 각 원소의 끝에 존재하는 경우
    if j == 0:
      tri[i][j] = tri[i-1][j] + tri[i][j]
    elif j == len(tri[i]) - 1:
      tri[i][j] = tri[i-1][j-1] + tri[i][j]
    else:
      tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]

print(max(tri[-1]))
