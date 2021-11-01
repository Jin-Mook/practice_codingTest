# 모험가 수
n = int(input())

scare = list(map(int, input().split()))

# 내림차순 정렬
# 첫번째 사람부터 확인해서 공포도에 맞게 그룹을 구성한다.
scare.sort(reverse=True)

i = 0
group_count = 0
while i < len(scare):
  # i번째 인덱스의 공포도가 x라면
  # 그 다음 그룹의 첫번째 인덱스는 i + x 이다.
  next_index = i + scare[i]
  # next_index가 범위 안에 있다면
  if next_index <= len(scare):
    group_count += 1
    i = next_index
  # scare[i]가 1이고 next_index가 범위를 벗어난다면
  # scare[i]가 마지막이라는 얘기이다.
  # 따라서 group_count 에 1을 더해주고 while을 빠져나가자
  elif scare[i] == 1:
    group_count += 1
    break
  
print(group_count)
  
  


