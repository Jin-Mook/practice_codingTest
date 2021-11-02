# 오름차순으로 정렬을 한다.
# 앞에서부터 하나씩 더할때 n번째 까지 더한 수가 n+1번째 수보다 2이상 작은경우
# n번째 까지 더한 수보다 1큰 수가 답이다.
# 단 처음이 1이 아니라면 1이 답이다.

n = int(input())
nums = list(map(int, input().split()))
# 오른차순 정렬
nums.sort()

# 처음 수가 1이 아니라면 답은 1이다.
def find_number(nums):  
  if nums[0] != 1:
    return 1
  
  # n번째 까지의 숫자의 합
  sum_now = nums[0]
  for i in range(1, len(nums)):
    # n번째 까지 더한 수보다 n+1이 2 이상 크다면
    # 예를 들어 n번째 까지 더한 수가 7이고 n+1 번째 수가 9이면 
    # 답은 8이 된다.
    if nums[i] - sum_now >= 2:
      return sum_now + 1
    else:
      sum_now += nums[i]
  # 만약 for문을 다 돌때까지 if문을 들어가는 경우가 없다면
  # 마지막 sum_now에서 1 더한 수가 최소 값이다.    
  return sum_now + 1

print(find_number(nums))





