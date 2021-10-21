count = {1: 0, 2:1, 3:1}

def make_count(x):
  if x in count:
    return count[x]
  temp = []
  if x % 5 == 0:
    temp.append(1 + make_count(x//5))
  if x % 3 == 0:
    temp.append(1 + make_count(x//3))
  if x % 2 == 0:
    temp.append(1 + make_count(x//2))
  temp.append(1 + make_count(x-1))

  count[x] = min(temp)
  return count[x]

n = int(input())
print(make_count(n))