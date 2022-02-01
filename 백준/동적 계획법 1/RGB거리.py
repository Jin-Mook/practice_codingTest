# n번째 가격은 n-1번째의 경우에서 각각 구한 후 가장 작은것을 선택한다.
# 이때 n이 3인 경우는 처음과 끝이 색이 달라도 되지만 4부터는 무조건 처음과 끝의 색이 같다.
import sys
import copy
input = sys.stdin.readline

n = int(input())
prices = []
for _ in range(n):
  prices.append(list(map(int, input().split())))

# print(prices)
cal = [0, 0, 0]
new_cal = [0, 0, 0]

for i in range(n):
  new_cal[0] = min(cal[1]+prices[i][0], cal[2]+prices[i][0])
  new_cal[1] = min(cal[0]+prices[i][1], cal[2]+prices[i][1])
  new_cal[2] = min(cal[0]+prices[i][2], cal[1]+prices[i][2])
  cal = copy.deepcopy(new_cal)

print(min(new_cal))
