# 이진 탐색 이용
import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

num_count = int(input())
want_finds = list(map(int, input().split()))
def binary_search(start, end, target):
  if start > end:
    return 0
  
  mid = (start + end) // 2
  if num_list[mid] < target:
    start = mid + 1
    return binary_search(start, end, target)
  elif num_list[mid] > target:
    end = mid -1
    return binary_search(start, end, target)
  else:
    return 1

for num in want_finds:
  print(binary_search(0, n-1, num))
