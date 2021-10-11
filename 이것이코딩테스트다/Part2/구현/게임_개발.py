n, m = map(int, input().split())
y, x, direction = map(int, input().split())
game_board = []
for i in range(n):
  game_board.append(list(map(int, input().split())))

count = 1

# 게임 시작

# while문을 통해 새로운 육지를 찾을 때까지 반복한다.
# 새로운 육지를 찾으면 새로운 땅으로 이동하고 이전 땅을 바다로 바꾼 후 새로운 위치, 방향, count를 반환한다.
# 새로운 육지를 찾지 못하면 False를 반환한다.

def checkGround(y, x, direction, count):
  first_direction = direction
  while True:
    position = [y, x]   # 처음 위치
    # 시계방향 회전시키기
    if direction == 0:
      new_direction = 3
    else:
      new_direction = direction - 1

    # 갈 곳 있는지 체크하기
    go_way = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    new_y, new_x = position[0] + go_way[new_direction][0], position[1] + go_way[new_direction][1]

    if game_board[new_y][new_x] == 1:
      direction = new_direction
      if direction == first_direction:
        return False, y, x, direction, count
    else:
      game_board[y][x] = 1
      count += 1
      return True, new_y, new_x, new_direction, count

while True:
  bool, new_y, new_x, new_direction , new_count = checkGround(y, x, direction, count)
  if bool == False:
    break
  else:
    y, x, direction, count = new_y, new_x, new_direction, new_count
  
print(count)

