import sys

n = int(input())
market_have = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
person_want = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
  if start > end:
    return 'no'
  mid = (start + end) // 2

  if target > array[mid]:
    return binary_search(array, target, mid+1, end)
  elif target < array[mid]:
    return binary_search(array, target, start, mid-1)
  else:
    return 'yes'

market_have.sort()
for menu in person_want:
  print(binary_search(market_have, menu, 0, len(market_have)-1), end=' ')