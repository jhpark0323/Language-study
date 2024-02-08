import numpy as np

# 내 빙고
my_bingo = [list(map(int, input().split())) for _ in range(5)]

my_bingo = np.array(my_bingo)

print(my_bingo)

# 사회자가 부르는 순서
mc = [list(map(int, input().split())) for _ in range(5)]

mc = np.array(mc)

'''
이걸 어케 풀지..
1. 사회자가 부른걸 순회한다.
2. 그걸 내 빙고에서 찾는다.
3. 빙고는 어케 확인함?
-> 사회자가 부른걸 내위치에서 찾아서 그 위치를 기준으로 사방팔방 줄 만들어지는지 확인해야하나
'''

def find_num(num, bingo):
    # np.where으로 num의 index를 찾음
    index = np.where(bingo == num)
    # 행과 열을 찾음
    row_find = index[0]
    col_find = index[1]
    return [row_find, col_find]  # ex) [array([2], dtype=int64), array([2], dtype=int64)] -> 2행 2열이라는 뜻

# ls = find_num(5, my_bingo)
# print(ls)
# print(ls[0][0] == 2)

# print(my_bingo[ls[0], ls[1]][0])

cnt = 0
# 먼저 사회자 빙고 순회
for row in range(5):
    for col in range(5):
        # numpy의 array는 index이렇게 가져옴
        n = mc[row, col]
        # ls에 index를 찾음
        ls = find_num(n, my_bingo)
        # my_bingo에서 그 위치를 0으로 변경
        my_bingo[ls[0], ls[1]] = 0
        print(my_bingo)

        # 찾은 index가 y = -x 형태의 대각선 이면
        if ls[0][0] == ls[1][0]:
            # 그게 전부 0이면
            if my_bingo[0,0] == 0 and my_bingo[1,1] == 0 and my_bingo[2,2] == 0 and my_bingo[3,3] == 0 and my_bingo[4,4] == 0:
                cnt += 1
        # 찾은 index가 y = x 혀태의 대각선 이면
        elif ls[0][0] == 4-ls[1][0]:
            if my_bingo[0, 0] == 0 and my_bingo[1, 1] == 0 and my_bingo[2, 2] == 0 and my_bingo[3, 3] == 0 and my_bingo[4, 4] == 0:
                pass
                # 계속 풀기