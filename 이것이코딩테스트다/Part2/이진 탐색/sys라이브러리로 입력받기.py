import sys

# 하나의 문자열 데이터 입력받기
for i in range(2):
  input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
  print(input_data)

# sys 라이브러리를 사용할 때 한 줄 입력받고 나서 rstrip()함수를 반드시 작성해야한다.
# 이유로는 입력 후 엔터키를 누를 때 줄 바꿈 기호로 입력이 되는데
# 이 공백 문자를 제거하려면 rstrip()함수를 이용해야 한다.