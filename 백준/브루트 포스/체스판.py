# 1018

# (1, 1)에서부터 전부 찾아보자
# W는 1, B는 0으로 표현
n, m = map(int, input().split())
board = []
for _ in range(n):
  new = []
  line = input()
  for el in line:
    if el == 'W':
      new.append(1)
    else:
      new.append(0)
  board.append(new)

# i, j 를 기준으로 8 x 8 체스판을 만들어주는 함수
def make_board(i, j, board):
  result = []
  for li in range(8):
    line = board[i+li][j:j+8]
    result.append(line)

  return result

# board의 0,0 부분부터 n-8, m-8 까지 new_board를 만들고 각각을 돌면서 확인한다.
# 이때 첫 부분이 흰 색인 경우와, 검은색인 경우로 나누어서 확인한다.
# 색칠한 횟수를 체크해서 작은 횟수를 가지고 간다.
answer = int(1e9)

for i in range(n-7):
  for j in range(m-7):
    new_board = make_board(i, j, board)
    count1 = 0   # 첫번째를 흰색으로 칠하는 경우
    count2 = 0   # 첫번째를 검은색으로 칠하는 경우
    
    for x in range(8):
      for y in range(8):
        # 첫번째를 흰색으로 칠하는 경우
        # x, y 둘다 짝수 혹은 둘다 홀수인 경우 흰색으로 칠함
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
          if new_board[x][y] == 0:
            count1 += 1
        else:
          if new_board[x][y] == 1:
            count1 += 1
        
        # 첫번째를 검은색으로 칠하는 경우
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
          if new_board[x][y] == 1:
            count2 += 1
        else:
          if new_board[x][y] == 0:
            count2 += 1
    
    answer = min(answer, count1, count2)

print(answer)


# 다른 사람 풀이
import sys
from itertools import accumulate
input = sys.stdin.readline

n, m = map(int, input().split())
f = lambda x: 1 if x == 'W' else 0
b = [[0 for _ in range(m+1)]]
print(b)
for i in range(n):
    cost = [0]
    cost.extend(accumulate([(f(s)+i+j) % 2 for j, s in enumerate(input().rstrip())]))
    b.append([k+j for k, j in zip(cost, b[-1])])

print(b)

result = 32
for i in range(8, n+1):
    for j in range(8, m+1):
        x = b[i][j] + b[i-8][j-8] - b[i][j-8] - b[i-8][j]
        result = min(result, x, 64-x)
print(result)
