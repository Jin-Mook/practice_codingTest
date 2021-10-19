n = int(input())
market_have = set(map(int, input().split()))

m = int(input())
person_want = list(map(int, input().split()))

for menu in person_want:
  if menu in market_have:
    print('yes', end=' ')
  else:
    print('no', end=' ')