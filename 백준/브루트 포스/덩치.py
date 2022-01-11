# 7568번 문제
# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

num = int(input())
people = []

for _ in range(num):
  new = list(map(int, input().split()))
  people.append(new)


races = [0] * len(people)

for i in range(num):
  record = num

  for j in range(num):
    if i == j:
      pass
    else:
      if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
        record -= 1
      elif (people[i][0] >= people[j][0] and people[i][1] <= people[j][1]) or (people[i][0] <= people[j][0] and people[i][1] >= people[j][1]):
        record -= 1

  races[i] = record

for ra in races:
  print(ra)



# print(new_people1, new_people2)
# races = []
# race = 0
# for i in range(len(people)-1):

#   if people[i][1] > people[i+1][1]:
#     race = i+1
#     races.append(race)
#     race += 1
#   else:
#     races.append(race)

# if people[-2][1] > people[-1][1]:
#   races.append(len(people))
# else:
#   races.append(race)

# for record in races:
#   print(record)