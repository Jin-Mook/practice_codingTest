import time
# 내 풀이
position = input()
time_start = time.time()
x, y = position[0], int(position[1])

x_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
x = x_dict[x]
count = 0
check_points = [[x-1, y+2], [x-1, y-2], [x+1, y+2], [x+1, y-2], [x-2, y+1], [x-2, y-1], [x+2, y+1], [x+2, y-1]]
result = []
for point in check_points:
  if point[0] >= 1 and point[0] <= 8 and point[1] >= 1 and point[1] <= 8:
    count += 1
time_end = time.time()
print(count, time_start-time_end)

# 책 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# ord함수는 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수이다.

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)
