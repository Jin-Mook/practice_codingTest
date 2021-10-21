memo_dict = {1:1, 2:1}

n = int(input())

for i in range(1, n+1):
  if i in memo_dict:
    pass
  else:
    memo_dict[i] = memo_dict[i-1] + memo_dict[i-2]
print(memo_dict[n])

