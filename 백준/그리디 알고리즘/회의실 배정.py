import sys
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
  times.append(list(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))

count = 0
rooms = []
for i in range(n):
  if i == 0:
    rooms.append(times[i])
    count += 1
  else:
    if rooms[-1][1] <= times[i][0]:
      rooms.append(times[i])
      count += 1
print(times)
# print(rooms)
print(count)