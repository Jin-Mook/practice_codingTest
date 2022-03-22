import sys
input = sys.stdin.readline

n, c = map(int, input().split())
loc = []
for _ in range(n):
  loc.append(int(input()))

loc.sort()
start = 1
end = loc[-1] - loc[0]

while start <= end:
  mid = (start+end) // 2
  now = loc[0]
  count = 1
  # 앞에서부터 공유기를 설치해서 mid보다 거리차이가 크거나 같으면 된다.
  # 공유기를 c개보다 많이 설치하면 start를 옮긴다.
  # 공유기를 c개보다 적게 설치하면 end를 옮긴다.
  for i in range(1, len(loc)):
    if loc[i] >= now + mid:
      count += 1
      now = loc[i]
  
  if count >= c:
    start = mid + 1
    result = mid
  else:
    end = mid - 1
print(result)