n = input()


half = len(n) // 2

left_half = n[:half]
right_half = n[half:]
sum1, sum2 = 0, 0
for left in left_half:
  sum1 += int(left)

for right in right_half:
  sum2 += int(right)

print(sum1, sum2)
if sum1 == sum2:
  print('LUCKY')
else:
  print('READY')