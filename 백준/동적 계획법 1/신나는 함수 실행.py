import sys
input = sys.stdin.readline

w_dict = {}

def w(a, b, c):
  if (a, b, c) in w_dict:
    return w_dict[(a, b, c)]
  else:
    if a <= 0 or b <= 0 or c <= 0:
      return 1
    elif a > 20 or b > 20 or c > 20:
      w_dict[(a, b, c)] = w(20, 20, 20)
    elif a < b and b < c:
      w_dict[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
      w_dict[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return w_dict[(a,b,c)]

check = []

while True:
  new_tuple = tuple(map(int, input().split()))
  if new_tuple == (-1, -1, -1):
    break
  check.append(new_tuple)


for value in check:
  a, b, c = value
  print(f"w({a}, {b}, {c}) = {w(*value)}")