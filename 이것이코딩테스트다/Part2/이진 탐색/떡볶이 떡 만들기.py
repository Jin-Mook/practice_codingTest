# 내 풀이 수학적으로 풀었는데
# 답이 아닐 가능성이 높다
import math

n, m = map(int, input().split())
lengths = list(map(int, input().split()))
num_sum = 0
target_value = 0

lengths.sort()
for i in range(len(lengths)-1, -1, -1):
  print(i)
  num_sum += lengths[i]
  target = math.floor((num_sum - m) / (len(lengths)-i))
  if target >= lengths[i-1]:
    target_value = target
    break

print(target_value)

# 책의 풀이
# 이진탐색을 이용해 풀었다. 파라메트릭 서치 유형
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 이진 탑색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while start <= end:
  total = 0

  mid = (start + end) // 2
  for x in array:
    # 잘랐을때 떡의 양 계산
    if x > mid:
      total += x - mid

  # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
  if total < m:
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
  else:
    # result 값이 될수있는 한 가장 큰 값을 원하기 때문에 result에 대입하고
    # 계속 while문을 돌게 한다.
    result = mid
    start = mid + 1
print(result)
  
    