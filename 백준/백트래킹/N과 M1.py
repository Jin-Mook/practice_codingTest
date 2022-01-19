# 최대 자연수 n
# 수열의 원소 수 m

n, m = map(int, input().split())

stack = []
# 첫번째 원소를 지정해주고 전부다 출력하는 함수
def input_stack():
  
  # 기저 조건 stack이 비어있으면 중지한다.
  if len(stack) == m:
    print(" ".join(map(str, stack)))
    return
  
  for i in range(1, n+1):
    if i not in stack:
      stack.append(i)
      input_stack()
      stack.pop()

input_stack()
