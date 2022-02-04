# 파라매트릭 서치의 기본 문제
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = []
for _ in range(k):
  lans.append(int(input()))
lans.sort()

start = 0
end = lans[-1] + 1

while True:
  mid = (start + end) // 2

  count = 0
  for lan in lans:
    count += lan // mid
  
  # print(count)
  # print(start, end)

  if count >= n:
    start = mid
  elif count < n:
    end = mid
  
  if abs(start - end) <= 1:
    print(start)
    break

