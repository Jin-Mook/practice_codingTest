import time

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 내 풀이
data.sort(reverse=True)

count = 0
sum = 0
for i in range(M):
  if count != 3:
    sum += data[0]
    count += 1
  else:
    sum += data[1]
    count = 0

print(sum)

# 책 풀이 1
start_time = time.time()

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  
  if m == 0:
    break
  result += second
  m -= 1

end_time = time.time()

print(result)

print("time : ", end_time - start_time)

# 책 풀이 2
data.sort()
first = data[n-1]
second = data[n-2]

num_of_fisrt = int((m // (k+1)) * k + m % (k+1))
num_of_second = m - num_of_fisrt

result = first * num_of_fisrt + second * num_of_second
print(result)