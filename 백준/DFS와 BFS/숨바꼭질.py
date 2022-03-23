from collections import deque

n, k = map(int, input().split())
check = [0] * 100001
dn = [1, -1, 2]
q = deque([])
q.append([n])
def bfs():
  if n == k:
    return 0
  result = 0

  while q:
    result += 1
    locations = q.popleft()
    new_locations = []
    # print(locations)
    for location in locations:
      for i in range(3):
        if i == 2:
          new_location = location * dn[i]
        else:
          new_location = location + dn[i]

        # 만약 new_locaiton 이 k라면 멈춘다.
        if new_location == k:
          return result
        
        if new_location >= 0 and new_location <= 100000 and check[new_location] == 0:
          check[new_location] = 1
          new_locations.append(new_location)
    
    q.append(new_locations)
print(bfs())
# bfs()