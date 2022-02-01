# n번째 개수는 n-1번째 + n-2번째이다.
sol_dict = [0] * 1000001
sol_dict[1] = 1
sol_dict[2] = 2

# def findSolution(n):
#   if n in sol_dict:
#     return sol_dict[n]
#   else:
#     sol_dict[n] = findSolution(n-1) + findSolution(n-2)

#     return sol_dict[n]

# print(findSolution(int(input())))

n = int(input())
for i in range(1, n+1):
  if sol_dict[i] != 0:
    pass
  else:
    sol_dict[i] = (sol_dict[i-1] + sol_dict[i-2]) % 15746

print(sol_dict[n])
