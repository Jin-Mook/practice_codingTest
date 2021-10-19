n = int(input())
array = [0] * 1000001
# n 의 최대값이 1000000 이기 때문에 계수 정렬로 크기가 n으로 만들어준다.
market_have = list(map(int, input().split()))

m = int(input())
person_want = list(map(int, input().split()))

for num in market_have:
  array[num] = 1

for menu in person_want:
  if array[menu] == 1:
    print('yes', end=' ')
  else:
    print('no', end=' ')
