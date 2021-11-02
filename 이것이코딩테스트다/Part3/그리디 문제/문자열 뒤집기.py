# 처음부터 차례대로 확인하며 0이 이어지는 갯수와
# 1이 이어지는 갯수를 따로 확인한다.
n = input()

count_zero = 0
count_one = 0

init = n[0]
if init == '0':
  count_zero += 1
else:
  count_one += 1

for i in range(1, len(n)):
  # 초기 값과 다르면 기존 개수를 늘려준다.
  if init != n[i]:
    if init == '0':
      count_one += 1
    else:
      count_zero += 1
  
  init = n[i]

print(min(count_zero, count_one))
