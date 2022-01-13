n = int(input())

num_list = []

count_dict = {}

result_sum = 0
for _ in range(n):
  num = int(input())
  result_sum += num
  num_list.append(num)
  if num in count_dict:
    count_dict[num] += 1
  else:
    count_dict[num] = 1

num_list.sort()
print(round(result_sum/n))

index = int((n-1)/2)
print(num_list[index])

count_list = [k for k, v in count_dict.items() if max(count_dict.values()) == v ]
if len(count_list) == 1:
  print(count_list[0])
else:
  count_list.sort()
  print(count_list[1])

print(num_list[-1] - num_list[0])
