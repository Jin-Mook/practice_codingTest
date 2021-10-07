n , m = map(int, input().split())

# 내 풀이
min_num = min(list(map(int, input().split())))
for i in range(n-1):
  # data.append(list(map(int, input().split())))
  temp = min(list(map(int, input().split())))
  if min_num < temp:
    min_num = temp
    
print(min_num)

# 책 풀이 1, min() 이용
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)

# 책 풀이 2, 이중 for구문 이용
result = 0
for i in range(n):
  data = list(map(int, input().split()))
  min_value = data[0]
  for j in data:
    min_value = min(min_value, j)

  result = max(result, min_value)

print(result)