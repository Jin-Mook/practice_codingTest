# n번째 계단에 오르는 방법은 먼저 n-2번째 계단에서 2칸을 올라가는 방법이 있다.
import sys
input = sys.stdin.readline
stairs = [0]

n = int(input())
for _ in range(n):
  stairs.append(int(input()))


stair_sum_value = [0 for _ in range(301)]  

# count = 0  # 1칸 올라갈 경우 count를 1 증가시킨다.
for i in range(1, n+1):
  # 만약 stair_sum_value에 값이 있는 경우 그대로 사용하면 된다.
  if i == 1:
    stair_sum_value[i] = stairs[i]

  elif i == 2:
    stair_sum_value[i] = max(stairs[i], stairs[i-1] + stairs[i])
    
  elif i == 3:
    stair_sum_value[i] = max(stairs[i-2], stairs[i-1]) + stairs[i]
    # print(stair_sum_value[:7])

  else:
    stair_sum_value[i] = max(stair_sum_value[i-2], stair_sum_value[i-3] + stairs[i-1]) + stairs[i]
    # print(stair_sum_value[:7])
print(stair_sum_value[n])