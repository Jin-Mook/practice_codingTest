from collections import deque
import copy

# 과목 수 입력
n = int(input())

# 선수과목 즉, 간선정보를 담기 위한 리스트
# n번째 행에 선수과목에 대한 정보가 들어간다.
graph = [[] for _ in range(n+1) ]

# 선수과목의 개수를 담는 리스트
indegree = [0] * (n+1)

# 과목 시간을 담는 리스트
time = [0] * (n+1)

# 과목 입력받아서 graph와 indegree 채우기
for j in range(1, n+1):
  subject = list(map(int, input().split()))
  # 각 과목정보에서 처음은 시간이고 -1이 될때까지 선수과목에 대한 내용이다. 
  time[j] = subject[0]
  for i in subject[1:-1]:
    graph[i].append(j)
    indegree[j] += 1

# 과목당 결과 시간을 담을 리스트
result = copy.deepcopy(time)
# queue에서 과목을 하나씩 뺄때마다 print해서 출력을 한다.
# 위상 정렬 함수
def topology_sort():
  q = deque()
  q.append(1)

  while q:
    now = q.popleft()

    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1

      #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  
  for i in range(1, n + 1):
    print(result[i])

topology_sort()

