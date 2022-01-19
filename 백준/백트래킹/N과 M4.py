n, m = map(int, input().split())

stack = []

def input_stack():
  if len(stack) == m:
    print(' '.join(stack))
    return
  
  for i in range(1, n+1):
    
    if stack == []:
      stack.append(str(i))
      input_stack()
      stack.pop()
    
    else:
      flag = True
      for num in stack:
        if str(i) < num:
          flag = False
          break
      
      if flag:
        stack.append(str(i))
        input_stack()
        stack.pop()

input_stack()