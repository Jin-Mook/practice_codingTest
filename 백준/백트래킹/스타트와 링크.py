import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

member = int(n / 2)
min_val = int(1e9)
team1 = [0]
team2 = []

# team1이 member 길이가 된다면 기저조건이 발생한다.,
def findSolution(index):
  global min_val
  if len(team1) == member:
    team2 = []
    sum_team1 = 0
    sum_team2 = 0

    for i in range(n):
      if i not in team1:
        team2.append(i)
    
    # print('team1: ', team1)
    # print('team2: ', team2)

    for i in range(member):
      for j in range(member):
        sum_team1 += board[team1[i]][team1[j]]
        sum_team2 += board[team2[i]][team2[j]]
    min_val = min(min_val, abs(sum_team1 - sum_team2))
    # print('min_val: ',min_val)
    return

  # print('len: ', len(team1))
  for k in range(1, n):
    if index+k < n:
      # print('index: ',index+k)
      team1.append(index+k)
      findSolution(index+k)
      team1.pop()

findSolution(0)
print(min_val)