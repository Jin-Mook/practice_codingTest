n = int(input())

nums = []
for i in range(n):
  nums.append(int(input()))

# 내림차순으로 정렬
nums.sort(reverse=True)
for num in nums:
  print(num, end=' ')