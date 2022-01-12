# 666, 1666, 2666 3666 4666 5666 6661 6662 6663 6664 6665 6666 6667 6668 6669 7666 8666 9666 10666

# 노가다로 1부터 찾는다??

n = int(input())

count = 1

num = 666
while count < n:
  num += 1
  str_num = str(num)
  # 666이 있으면 count를 1 증가시키고 없으면 넘어간다.
  for i in range(len(str_num) - 2):
    if str_num[i:i+3] == '666':
      count += 1
      break

print(num)

# 다른 사람 풀이
N = int(input())
if N==1:
    print(666)
else:
    count = 1
    for i in range(2, N+1):
        base_title = "{0}666".format(i-1)
        num_of_extra_six_in_row = 0
        for k in range(len(base_title)-3):
            if base_title[-4-k]=='6':
                num_of_extra_six_in_row += 1
            else:
                break
        count += int(10**num_of_extra_six_in_row)
        if count >= N:
            break
            
    if num_of_extra_six_in_row > 0:
        base = int(10**num_of_extra_six_in_row)
        count -= base
        base_title = int(base_title) - int(base_title)%base + (N - count-1)
        
    print(base_title)