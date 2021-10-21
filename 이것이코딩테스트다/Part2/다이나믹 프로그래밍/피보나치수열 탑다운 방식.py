memo_dict = {1: 1, 2: 1}

def fibo(x):
  if x in memo_dict:
    return memo_dict[x]
  else:
    memo_dict[x] = fibo(x-1) + fibo(x-2)
    return memo_dict[x]

print(fibo(10))