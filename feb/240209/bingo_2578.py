import pprint

# 내 빙고
my_bingo = [list(map(int, input().split())) for _ in range(5)]

# print(my_bingo)

# 사회자가 부르는 순서
mc = [list(map(int, input().split())) for _ in range(5)]

'''
이걸 어케 풀지..
1. 사회자가 부른걸 순회한다.
2. 그걸 내 빙고에서 찾는다.
3. 빙고는 어케 확인함?
-> 사회자가 부른걸 내위치에서 찾아서 그 위치를 기준으로 사방팔방 줄 만들어지는지 확인해야하나
'''

# 빙고 위치 찾는 함수
def find_num(number, bingo):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                return i, j

ls = find_num(5, my_bingo)
# print(ls)

bingo_cnt = 0
cnt = 0
# 먼저 사회자 빙고 순회
for row in range(5):
    for col in range(5):
        # numpy의 array는 index이렇게 가져옴
        n = mc[row][col]
        # ls에 index를 찾음
        ls = find_num(n, my_bingo)
        # my_bingo에서 그 위치를 0으로 변경
        my_bingo[ls[0]][ls[1]] = 0
        # pprint.pprint(my_bingo)

        cnt += 1

        # 찾은 index가 y = -x 형태의 대각선 이면
        if ls[0] == ls[1]:
            # 그게 전부 0이면
            if my_bingo[0][0] == 0 and my_bingo[1][1] == 0 and my_bingo[2][2] == 0 and my_bingo[3][3] == 0 and my_bingo[4][4] == 0:
                bingo_cnt += 1
        # 찾은 index가 y = x 형태의 대각선 이면
        # 양쪽 대각선이 2,2의 index 빼고 다채워져있다가 마지막에 2,2가 채워지면 위의 경우와 지금경우가 다 적용되야함
        # 그래서 여기도 if
        if ls[0] == 4-ls[1]:
            if my_bingo[4][0] == 0 and my_bingo[3][1] == 0 and my_bingo[2][2] == 0 and my_bingo[1][3] == 0 and my_bingo[0][4] == 0:
                bingo_cnt += 1

        # 나머지의 경우 대각선을 생각할 필요 없음 -> 하지만 대각선에 들어갔던 경우도 여기서 다시 체크 할 필요는 있음
        # -> elif가 아니고 if인 이유
        # 채워졌을 때 그 행의 합이 0이면 bingo_cnt += 1
        if sum(my_bingo[ls[0]]) == 0:
            bingo_cnt += 1

        # 채워졌을 때 그 열의 합이 0이면 bingo_cnt += 1
        col_sum = 0
        for i in range(5):
            col_sum += my_bingo[i][ls[1]]

        if col_sum == 0:
            bingo_cnt += 1
            # pprint.pprint(my_bingo)

        if bingo_cnt >= 3:
            # print(cnt)
            break

        # print(bingo_cnt)

    if bingo_cnt >= 3:
        print(cnt)
        break
