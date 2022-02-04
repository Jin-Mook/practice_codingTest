# 사전을 이용해 풀어보자
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

n_count = int(input())
want_find = list(map(int, input().split()))

new_dict = {}
for num in numbers:
  if num in new_dict:
    new_dict[num] += 1
  else:
    new_dict[num] = 1

result = []
for find in want_find:
  if find in new_dict:
    result.append(str(new_dict[find]))
  else:
    result.append('0')

print(' '.join(result))