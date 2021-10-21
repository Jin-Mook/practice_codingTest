# 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾는다.
# 금액 i를 만들 수 있는 최소한의 화폐 개수를 ai, 화폐의 단위를 k라고 했을 때
# 다음과 같은 점화식을 작성할 수 있다.
# ai-k 가 존재하는 경우 ai = min(ai, ai-k + 1)

# 책 풀이 바탕으로 내가 짠 코드
n, m = map(int, input().split())
moneys = [0] + [10001] * m
money_units = []
for _ in range(n):
  money_units.append(int(input()))

for unit in money_units:
  for i in range(len(moneys)):
    if i - unit >= 0 and moneys[i-unit] == 10001:
      pass
    if i - unit >= 0 and moneys[i-unit] != 10001:
      moneys[i] = min(moneys[i], moneys[i-unit] + 1)
if moneys[m] == 10001:
  print(-1)
else:
  print(moneys[m])


# 책 풀이
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
  array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행 (바텀업 방식)
d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    # (i - k)원을 만드는 방법이 존재하는 경우
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
  print(-1)
else:
  print(d[m])



