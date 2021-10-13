array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)-1):
  head_value = array[i]
  min_value = array[i+1]
  index = i+1
  for j in range(i+1, len(array)):
    if array[j] < min_value:
      min_value = array[j]
      index = j   
  if head_value > min_value:
    array[i], array[index] = array[index], array[i]
print(array)


# 책 풀이
for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]
print(array)