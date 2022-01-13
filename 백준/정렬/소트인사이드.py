count_list = [0] * 10

n = input()

for num in n:
  count_list[int(num)] += 1

result = ''
for i in range(9, -1, -1):
  temp = str(i) * count_list[i]
  result += temp

print(int(result))

# 다른사람의 풀이
print(''.join(sorted(n)[::-1]))