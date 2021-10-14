array = [7, 6, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 내 풀이
list_num = [0] * (max(array) + 1)
sorted_list = []
for num in array:
  list_num[num] += 1

for i in range(len(list_num)):
  sorted_list = sorted_list + [i] * list_num[i]

print(sorted_list)

# 책 풀이

# 모든 범위를 포함하는 리스트 선언, 초기 값은 0으로 초기화
count = [0] * (max(array) + 1)

for i in range(len(array)):
  # 각 데이터에 해당하는 인덱스의 값 증가
  count[array[i]] += 1   

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
      print(i, end=' ')