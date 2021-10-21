# 내 풀이
# 책 풀이와 아이디어는 동일하다
# 다만 코드가 다를 뿐이다.
n = int(input())
foods = list(map(int, input().split()))

def max_foods(foods):
  foods_list = [0] * (n+1)
  for i in range(1, n+1):
    if i == 1:
      foods_list[i] = foods[i-1]
    elif i == 2:
      foods_list[i] = max(foods[i-2], foods[i-1])
    else:
      foods_list[i] = max(foods_list[i-1], foods_list[i-2] + foods[i-1])
  
  return foods_list[-1]
    
print(max_foods(foods))


# 책 풀이
# 위 코드보다 훨씬 깔끔해 보인다.
n = int(input())
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(DP) 진행 -> 바텀업 방식 이용
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + array[i])
print(d[n-1])

  

