# result 가 1인 경우도 더해주어야 하는데 이를 생각 못한 풀이이다.
# 아래 풀이는 잘못된 풀이이다.

nums = input()

result = 0
for num in nums:
  # 첫번째 수만 더해준다.
  if result == 0:
    result += int(num)
    continue
  
  # 중간에 0이 나오는 경우 더해준다
  if int(num) <= 0 or int(num) == 1:   # 이 부분을 int(num) <= 1 or result <= 1로 바꿔주어야 맞는 답이다.
    result += int(num)
  else:
    result = result * int(num)
print(result)