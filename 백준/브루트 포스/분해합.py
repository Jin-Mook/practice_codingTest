n = input()

for i in range(1, int(n)+1):
  sum = i

  str_i = str(i)
  for num in str_i:
    sum += int(num)

  if sum == int(n):
    print(i)
    break

if i == int(n):
  print(0)


  


