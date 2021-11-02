# 책에서는 target 즉 앞에서부터 더한 값보다 1 큰것을 기준으로
# 문제를 풀었다.

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
  # 만들 수 없는 금액을 찾았을 때 반복 종료
  if x > target:
    break
  target += x

print(target)