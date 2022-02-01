sol = [0] * 101

sol[1] = 1
sol[2] = 1
sol[3] = 1
sol[4] = 2
sol[5] = 2
sol[6] = 3
sol[7] = 4
sol[8] = 5
sol[9] = 7
sol[10] = 9
sol[11] = 12

for i in range(1, 101):
  if sol[i] != 0:
    pass
  else:
    sol[i] = sol[i-1] + sol[i-5]

n = int(input())
for _ in range(n):
  print(sol[int(input())])
