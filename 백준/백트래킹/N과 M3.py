n, m = map(int, input().split())

stack = []

def input_stack():
  # 기저 조건
  if len(stack) == m:
    print(' '.join(stack))
    return
  
  for i in range(1, n+1):
    stack.append(str(i))
    input_stack()
    stack.pop()

input_stack()