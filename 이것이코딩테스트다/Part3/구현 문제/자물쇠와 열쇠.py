import copy
# 90도 회전시키는 함수
def rotate90(matrix):
    temp = zip(*matrix[::-1])
    return [list(elem) for elem in temp]

# background를 만드는 함수
# background를 만들어야한다. 가운데는 lock이 존재하고 나머지는 0으로 만든다.
# background의 크기는 len(lock) + (len(key)-1) * 2 이다.
def make_back(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    back_n = len(lock) + (len(key)-1)*2
    # 0으로 이루어진 back만들기
    back = [[0] * back_n for _ in range(back_n)]

    for i in range(len_key-1, len_lock+len_key-1):
        for j in range(len_key-1, len_lock+len_key-1):
            back[i][j] = lock[i-(len_key-1)][j-(len_key-1)]
    return back

def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    
    back = make_back(key, lock)
    
    for _ in range(4):
        # print("back : " , back)
        for x in range(len_lock+len_key-1):
            for y in range(len_lock+len_key-1):
                answer = True
                temp = copy.deepcopy(back)
                # key와 back을 하나씩 더한다.
                # print(x, y)
                for key_x in range(len_key):
                    if answer==False:
                        break
                    for key_y in range(len_key):
                        if answer==False:
                            break
                        
                        if x+key_x >= len_key-1 and x+key_x< len_lock+len_key-1 and y+key_y >= len_key-1 and y+key_y< len_lock+len_key-1:
                            new_result = temp[x+key_x][y+key_y] + key[key_x][key_y]
                            temp[x+key_x][y+key_y] = new_result
                            if new_result == 0 or new_result == 2:
                                answer=False
                
                # 만약 더해지지 않은 부분이 lock에 있을 수 있기 때문에 x, y loop가 끝나고 lock부분을 체크한다.
                for _x in range(len_key-1, len_lock+len_key-1):
                    for _y in range(len_key-1, len_lock+len_key-1):
                        if temp[_x][_y] != 1:
                            answer = False
                
                if answer == True:
                    return True

        key = rotate90(key)
    return False