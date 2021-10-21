
# 내 풀이
# 잘못된 풀이이다.
n = int(input())
d = []
d.append(1)
d.append(3)
for i in range(2, n):
  d.append(d[i-2] * 3 + d[i-1] - 1)

print(d[-1] % 796796)

# 책 풀이
n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
  d[i] = d[i-1] + d[i-2] * 2
print(d[n])