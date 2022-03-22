import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
  mid = (start+end) // 2
  count_tree = 0
  total_tree = 0

  # for tree in trees:
  #   if tree > mid:
  #     count_tree += 1
  #     total_tree += tree
  result = [tree-mid for tree in trees if tree > mid]

  # total_tree -= count_tree * mid
  total_tree = sum(result)
  # 가져가는 길이가 원하는 양보다 작다면 end를 옮긴다.
  if total_tree < m:
    end = mid-1
  # 가져가는 길이가 원하는 양보다 크다면 start를 옮긴다.
  else:
    start = mid+1

print(end)