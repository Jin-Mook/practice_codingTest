import sys
input = sys.stdin.readline

n = int(input())
boards = []
for _ in range(n):
  boards.append(list(map(int, input().split())))

def solution(h_start, h_end, v_start, v_end):
  white = 0
  blue = 0

  # boards에서 start와 end의 위치에 맞게 새로운 new_boards를 만들어야 한다.
  new_board = []
  for i in range(v_start, v_end+1):
    append_board = []
    for j in range(h_start, h_end+1):
      append_board.append(boards[i][j])
    
    new_board.append(append_board)
  
  # 만약 n즉, 한 변의 길이가 1 인경우는 1을 리턴한다.
  if h_start == h_end and v_start == v_end:
    if new_board[0][0] == 0:
      white += 1
    else:
      blue += 1
    return [white, blue]

  # print(new_board)
  new_board_len = len(new_board)
  first = new_board[0][0]
  flag = True
  for x in range(new_board_len):
    for y in range(new_board_len):
      if first != new_board[x][y]:
        flag = False
        break

  # 만약 flag 가 그대로 True라면 모든 값이 같은 경우이다.
  # 이때는 1을 리턴한다.
  if flag == True:
    if first == 0:
      white += 1
    else:
      blue += 1
    return [white, blue]
  

  h_center = (h_start + h_end) // 2 + 1   # 가로 중간 인덱스
  v_center = (v_start + v_end) // 2 + 1   # 세로 중간 인덱스

  result1 = solution(h_start, h_center-1, v_start, v_center-1)
  result2 = solution(h_center, h_end, v_start, v_center-1)
  result3 = solution(h_start, h_center-1, v_center, v_end)
  result4 = solution(h_center, h_end, v_center, v_end)
  result = []
  for new in zip(result1, result2, result3, result4):
    result.append(sum(new))
    
  return result

sol = solution(0, n-1, 0, n-1)
print(sol[0])
print(sol[1])