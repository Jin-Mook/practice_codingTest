import sys
input = sys.stdin.readline

n, total = map(int, input().split())

moneys = []
for _ in range(n):
  moneys.append(int(input()))

moneys.sort(reverse=True)
result = 0
for money in moneys:
  result += total // money
  total = total % money

print(result)
