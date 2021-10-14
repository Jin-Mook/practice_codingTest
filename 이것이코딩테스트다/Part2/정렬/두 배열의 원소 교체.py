n, k = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
list_b.sort(reverse=True)

for i in range(k):
  if list_a[i] < list_b[i]:
    list_a[i] = list_b[i]
  else:
    break
print(sum(list_a))
