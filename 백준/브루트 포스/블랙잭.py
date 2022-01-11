# https://www.acmicpc.net/problem/2798

# 5 21
# 5 6 7 8 9

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

diff = int(1e9)
reult = 0
for i in range(len(num_list)-2):
  for j in range(i+1, len(num_list) - 1):
    for k in range(j+1, len(num_list)):
      new_result = num_list[i] + num_list[j] + num_list[k]
      new_diff = m - new_result
      if new_diff >= 0 and new_diff < diff:
        result = new_result
        diff = new_diff

print(result)
