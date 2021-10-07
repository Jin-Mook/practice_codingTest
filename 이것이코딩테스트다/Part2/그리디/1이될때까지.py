n, k = map(int, input().split())

# 내 풀이
count = 0
while n != 1:
  if n % k == 0:
    count += 1
  else:
    count += n % k + 1
  n = n // k
  if n < k:
    count += n-1
    break
print(count)

# 책 풀이
result = 0
while True:
  # n 이 k 로 나누어 떨어지는 수가 될 때까지 1씩 빼기
  target = (n // k) * k
  result += n - target
  n = target

  if n < k:
    break
  result += 1
  n //= k

result += (n -1)
print(result)