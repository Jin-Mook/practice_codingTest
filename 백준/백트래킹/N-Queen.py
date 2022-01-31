# # 백트래킹으로 문제를 풀 예정인데 n+1 크기를 갖는 2차원 리스트를 만들자.
# n = int(input())

# # 퀸이 위치할 수 없는 리스트
# located_index = []

# result = []
# # 해당 행의 인덱스를 받아 각각의 열에서 퀸 위치가 가능한지 확인하는 함수
# def find_count_queen(row_index):
#   # 기저조건
#   if row_index == n+1:
#     print(located_index)
#     result.append(1)
#     return

#   for j in range(1, n+1):
#     # 실행되는 행이 1인 경우 바로 located_index에 넣어준다.
#     if row_index == 1:
#       located_index.append([row_index, j])
#       find_count_queen(row_index + 1)
#       located_index.pop()
#     # 만약 실행되는 함수의 행이 1행이 아닌 경우는 체크를 해주어야 한다.
#     else:
#       flag = True
#       for locate in located_index:
#         diff = row_index - locate[0]
#         if j == locate[1] + diff or j == locate[1] - diff or j == locate[1]:
#           flag = False
#           break
      
#       if flag == True:
#         located_index.append([row_index, j])
#         find_count_queen(row_index + 1)
#         located_index.pop()


# find_count_queen(1)
# print(len(result))
        


# 백트래킹으로 문제를 풀 예정인데 n+1 크기를 갖는 2차원 리스트를 만들자.
n = int(input())

# 퀸이 위치할 수 없는 리스트
located_index = []

result = 0
# 해당 행의 인덱스를 받아 각각의 열에서 퀸 위치가 가능한지 확인하는 함수
def find_count_queen(row_index):
  # 기저조건
  global result
  if row_index == n+1:
    result += 1
    return

  for j in range(1, n+1):
    # 실행되는 행이 1인 경우 바로 located_index에 넣어준다.
    if row_index == 1:
      located_index.append([row_index, j])
      find_count_queen(row_index + 1)
      located_index.pop()
    # 만약 실행되는 함수의 행이 1행이 아닌 경우는 체크를 해주어야 한다.
    else:
      flag = True
      for locate in located_index:
        diff = row_index - locate[0]
        if j == locate[1] + diff or j == locate[1] - diff or j == locate[1]:
          flag = False
          break
      
      if flag == True:
        located_index.append([row_index, j])
        find_count_queen(row_index + 1)
        located_index.pop()


find_count_queen(1)
print(result)
        










