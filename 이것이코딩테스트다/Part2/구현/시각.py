n = int(input())

# 1번째 내 풀이
count = 0
for hour in range(n+1):
  strHour = str(hour)
  for minute in range(0, 60):
    if "3" in strHour:
      count += 60
      continue
    strMinute = str(minute)
    for second in range(0, 60):
      if "3" in strMinute:
        count += 1
        continue
      
      strSecond = str(second)
      if "3" in strSecond:
        count += 1
print(count)

# 2번째 내 풀이
count = 0
for hour in range(n+1):
  strHour = str(hour)
  if "3" in strHour:
    count += 60*60
    continue
  for minute in range(0, 60):
    strMinute = str(minute)
    if "3" in strMinute:
      count += 60
      continue
    for second in range(0, 60):
      strSecond = str(second)
      if "3" in strSecond:
        count += 1
print(count)

# 책 풀이
h = int(input)

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if "3" in str(i) + str(j) + str(k):
        count += 1
print(count)