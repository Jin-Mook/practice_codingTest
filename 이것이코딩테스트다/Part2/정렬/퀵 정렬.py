array =[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 내 풀이
def quick_sort(array):
  if len(array) <= 1:
    return array

  left_list = []
  right_list = []
  pivot = array[0]
  for i in range(1, len(array)):
    if array[i] <= pivot:
      left_list.append(array[i])
    else:
      right_list.append(array[i])
  return quick_sort(left_list) + [pivot] + quick_sort(right_list)

print(quick_sort(array))

# 책 풀이
def quick_sort1(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  return quick_sort1(left_side) + [pivot] + quick_sort1(right_side)

print(quick_sort1(array))
