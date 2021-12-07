from collections import deque

n = int(input())   # 보드의 크기
k = int(input())   # 사과의 개수
apple_loc = []     # 사과의 위치를 담은 리스트
for _a in range(k):
  apple_loc.append(list(map(int, input().split())))
  # temp = list(map(int, input().split()))
  # apple_loc.append([temp[0]-1, temp[0]-1])

l = int(input())   # 뱀의 방향 전환 횟수
direction_change = []

# 숫자인지 문자인지 체크하는 함수
def check(x):
  try:
    return int(x)
  except:
    return x

direction_change = {}
for _d in range(l):
  # direction_change.append(list(map(check, input().split())))
  temp = list(map(check, input().split()))
  direction_change[temp[0]] = temp[1]

# 게임판 행렬을 먼저 만든다.
game_board = [[0] * (n+1) for _ in range(n+1)]

# 게임판에서 사과 위치 1로 바꾸기
for loc in apple_loc:
  game_board[loc[0]][loc[1]] = 1

# deq의 앞쪽 인덱스는 뱀의 꼬리 부분이고 뒤쪽 인덱스가 뱀의 머리 부분이다.
deq = deque([[1, 1]])

# 뱀의 머리 방향에 따라 이동 후 deq 을 변화시키는 함수를 만들자
def move(direction):
  # 이동하는 위치에 사과가 있는지 없는지를 먼저 체크하자
  # 오른쪽으로 이동하는 경우
  head = deq[-1]
  if direction == 'right':
    next_head = [head[0], head[1]+1]
    # 뱀이 몸이 위치해 있거나 벽에 부딪치는 경우  
    if (next_head in deq) or (next_head[0] <= 0) or (next_head[0] > n) or (next_head[1] <= 0) or (next_head[1] > n):
      return False
    # 사과가 있는 경우
    elif game_board[next_head[0]][next_head[1]] == 1:
      deq.append(next_head)
      game_board[next_head[0]][next_head[1]] = 0
    # 이동하는 위치에 사과가 없는 경우
    else:
      deq.append(next_head)
      deq.popleft()
  # 왼쪽으로 이동하는 경우
  elif direction == 'left':
    next_head = [head[0], head[1]-1]
    # 뱀이 몸이 위치해 있거나 벽에 부딪치는 경우  
    if (next_head in deq) or (next_head[0] <= 0) or (next_head[0] > n) or (next_head[1] <= 0) or (next_head[1] > n):
      return False
    # 사과가 있는 경우
    elif game_board[next_head[0]][next_head[1]] == 1:
      deq.append(next_head)
      game_board[next_head[0]][next_head[1]] = 0
    # 이동하는 위치에 사과가 없는 경우
    else:
      deq.append(next_head)
      deq.popleft()
  # 아래로 이동하는 경우
  elif direction == 'down':
    next_head = [head[0]+1, head[1]]
    # 뱀이 몸이 위치해 있거나 벽에 부딪치는 경우  
    if (next_head in deq) or (next_head[0] <= 0) or (next_head[0] > n) or (next_head[1] <= 0) or (next_head[1] > n):
      return False
    # 사과가 있는 경우
    elif game_board[next_head[0]][next_head[1]] == 1:
      deq.append(next_head)
      game_board[next_head[0]][next_head[1]] = 0
    # 이동하는 위치에 사과가 없는 경우
    else:
      deq.append(next_head)
      deq.popleft()
  # 위로 이동하는 경우
  else:
    next_head = [head[0]-1, head[1]]
    # 뱀이 몸이 위치해 있거나 벽에 부딪치는 경우  
    if (next_head in deq) or (next_head[0] <= 0) or (next_head[0] > n) or (next_head[1] <= 0) or (next_head[1] > n):
      return False
    # 사과가 있는 경우
    elif game_board[next_head[0]][next_head[1]] == 1:
      deq.append(next_head)
      game_board[next_head[0]][next_head[1]] = 0
    # 이동하는 위치에 사과가 없는 경우
    else:
      deq.append(next_head)
      deq.popleft()
  return True

# 방향을 바꾸는 함수
def change_direction(direction, vector):
  if direction == 'right':
    if vector == 'D':
      return 'down'
    else:
      return 'up'
  elif direction == 'left':
    if vector == 'D':
      return 'up'
    else:
      return 'down'
  elif direction == 'down':
    if vector == 'D':
      return 'left'
    else:
      return 'right'
  else:
    if vector == 'D':
      return 'right'
    else:
      return 'left'

def main():
  print(game_board)
  result = 0
  direction = 'right'
  while True:
    result += 1
    if move(direction) == False:
      return result
    print(result, deq)
    
    # result초가 된 후 방향을 바꿔야 하는 경우
    if result in direction_change:
      direction = change_direction(direction, direction_change[result])


print(main())