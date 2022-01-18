# 전체 입력을 리스트로 만든다음 정렬시킨다.
import sys
import copy
n = int(input())

num_origin = list(map(int, sys.stdin.readline().split()))

num_sorted = []

for i in range(len(num_origin)):
  num_sorted.append([num_origin[i], i]) 

num_sorted.sort(key=lambda x: x[0])

record = []
index = 0
for i in range(len(num_sorted)):
  if i == 0:
    record.append(index)
  else:
    if num_sorted[i][0] == num_sorted[i-1][0]:
      record.append(index)
    else:
      index += 1
      record.append(index)

result = [0] * n
for i in range(len(num_sorted)):
  result_index = num_sorted[i][1]
  result_value = str(record[i])
  result[result_index] = result_value


print(' '.join(result))


# 다른 사람 풀이
N = int(input())
S = list(map(int, input().split()))
s = set(S)
s = list(s)
s.sort()
sdic = {s[i] : i for i in range(len(s))}
print(' '.join((str(sdic[i])) for i in S))