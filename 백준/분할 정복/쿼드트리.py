import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
  n_board = []
  for string in input().strip():
    n_board.append(string)
  board.append(n_board)  
print(board)

def solution(h_start, h_end, v_start, v_end):
  result = []
  h_center = (h_start+h_end) // 2 + 1
  v_center = (v_start+v_end) // 2 + 1

  new_board = []
  for i in range(v_start, v_end+1):
    append_board = []
    for j in range(h_start, h_end+1):
      # print(board, i, j)
      append_board.append(board[i][j])
    
    new_board.append(append_board)
  
  if h_start == h_end and v_start == v_end:
    if new_board[0][0] == '0':
      result.append('0')
      return result
    else:
      result.append('1')
      return result
  
  first = new_board[0][0]
  flag = True
  new_board_len = len(new_board)
  for x in range(new_board_len):
    for y in range(new_board_len):
      if new_board[x][y] != first:
        flag = False
        break
  
  if flag == True:
    if first == '0':
      result.append('0')
    else:
      result.append('1')
    return result

  result.append('(')
  result1 = solution(h_start, h_center-1, v_start, v_center-1)
  result2 = solution(h_center, h_end, v_start, v_center-1)
  result3 = solution(h_start, h_center-1, v_center, v_end)
  result4 = solution(h_center, h_end, v_center, v_end)
  result += result1
  result += result2
  result += result3
  result += result4
  result.append(')')
  return result

result = solution(0, n-1, 0, n-1)
print(result)
print(''.join(result))

    