n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)


def findSolution(iter, num, add, sub, mul, div):
  global max_val, min_val
  if iter == n:
    max_val = max(max_val, num)
    min_val = min(min_val, num)
    return

  if add > 0:
    findSolution(iter+1, num+num_list[iter], add-1, sub, mul, div)
  if sub > 0:
    findSolution(iter+1, num-num_list[iter], add, sub-1, mul, div)
  if mul > 0:
    findSolution(iter+1, num*num_list[iter], add, sub, mul-1, div)
  if div > 0:
    findSolution(iter+1, int(num/num_list[iter]), add, sub, mul, div-1)

findSolution(1, num_list[0], add, sub, mul, div)
print(max_val)
print(min_val)
  
  

