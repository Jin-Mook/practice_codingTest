n = int(input())

sort_list = []

for _ in range(n):
  sort_list.append(list(map(int, input().split())))

sort_list.sort(key=lambda x: (x[0], x[1]))

for el in sort_list:
  print(el[0], el[1])