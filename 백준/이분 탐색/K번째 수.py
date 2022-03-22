n = int(input())
k = int(input())

start = 1
end = n * n

while start <= end:
  mid = (start+end) // 2
  count = 0

  for i in range(1, n+1):
    count += min(mid // i, n)
  
  if count >= k:
    answer = mid
    end = mid - 1
  else: #count < k:
    start = mid + 1
print(answer)