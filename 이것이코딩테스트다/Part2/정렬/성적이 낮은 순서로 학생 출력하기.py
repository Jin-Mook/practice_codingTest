n = int(input())

# 내가 푼 풀이
# 퀵정렬을 이용했지만 문제의 조건에 맞지 않다.
# 최악의 경우 퀵정렬은 O(n^2) 의 시간복잡도 이지만
# 문제의 경우 최소 O(nlogn) 의 시간 복잡도를 원한다.
name_list = []
score_list = []
for i in range(n):
  name, score = map(str, input().split())
  name_list.append(name)
  score_list.append(int(score))

def quick(names, scores):
  if len(scores) <= 1:
    return names
  
  left_scores = []
  left_names = []
  right_scores = []
  right_names = []
  pivot = scores[0]
  pivot_names = names[0]
  for i in range(1, len(scores)):
    if scores[i] <= pivot:
      left_scores.append(scores[i])
      left_names.append(names[i])
    else:
      right_scores.append(scores[i])
      right_names.append(names[i])

  return quick(left_names, left_scores) + [pivot_names] + quick(right_names, right_scores)

print(quick(name_list, score_list))


# 책 풀이 내장 정렬 라이브러리인 sort이용
n = int(input())
name_score_list = []
for i in range(n):
  input_data = input().split()
  name_score_list.append((input_data[0], input_data[1]))

result = sorted(name_score_list, key=lambda a: a[1])   # key값에는 함수의 지정한 결과에 따라 정렬할 수 있다.
for i in range(len(result)):
  print(result[i][0], end=' ')