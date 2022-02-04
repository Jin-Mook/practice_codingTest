import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()

result = []
count = 0
for time in times:
  count += time
  result.append(count)
print(sum(result))