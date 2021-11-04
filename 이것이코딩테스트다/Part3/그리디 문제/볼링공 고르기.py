# 무게가 다른 볼링공의 개수를 리스트로 만들어 준다.

n, m = map(int, input().split())
weights = list(map(int, input().split()))

# 볼링공 무게별 개수를 담을 리스트
# 인덱스 번호가 무게를 의미한다.
weight_list = [0] * (n + 1)

for weight in weights:
  weight_list[weight] += 1

result = 0
for i in range(1, len(weight_list)-1):
  # 무게가 i인 볼링공의 개수는 전체에서 제외한다.
  n -= weight_list[i]
  result += weight_list[i] * n

print(result)

