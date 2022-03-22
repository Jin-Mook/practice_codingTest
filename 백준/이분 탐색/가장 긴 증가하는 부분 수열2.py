import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

make_list = [0]
for i in range(n):
  if make_list[-1] < nums[i]:
    make_list.append(nums[i])
  else:
    start = 0
    end = len(make_list) - 1

    while start <= end:
      mid = (start+end)//2

      if make_list[mid] < nums[i]:
        start = mid + 1
      else: # mid >= nums[i]
        end = mid - 1
        result = mid
        # print(result)

    make_list[result] = nums[i]
  # print(make_list)
print(len(make_list) - 1)  