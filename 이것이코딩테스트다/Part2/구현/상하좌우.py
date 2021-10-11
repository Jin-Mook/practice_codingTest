n = int(input())
plans = input().split();
print(plans)
x, y = 1, 1

# 내 풀이
for dir in plans:
  if dir == 'R':
    if x != n:
      x += 1
  elif dir == 'L':
    if x != 1:
      x -= 1
  elif dir == "U":
    if y != 1:
      y -= 1
  else:
    if y != n:
      y += 1

print(y, x)

# 책 풀이
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)