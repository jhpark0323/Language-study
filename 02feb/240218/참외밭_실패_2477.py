import pprint

'''
어디든 기준으로 반시계 방향이라고 했으니 빈 밭을 크게 지어야 할듯
'''

# 넓이당 참외의 갯수
n = int(input())

# 참외 밭
melon_field = [list(map(int, input().split())) for _ in range(6)]

# 순서대로 동서남북(우좌하상) -> 1부터 4까지
di = [0, 0, 0, 1, -1]
dj = [0, 1, -1, 0, 0]

# 빈 밭 -> 크기가 가로세로 각각 두배는 되어야 할듯 -> 시작을 500, 500에서 해야할듯
field = [[0] * 21 for _ in range(21)]
# pprint.pprint(field)

ni = 10
nj = 10
for k in range(6):
    # 방향과 길이
    dij, length = melon_field[k][0], melon_field[k][1]
    for l in range(length):
        # if l == 0:
        #     field[ni][nj] = 1
        # else:
            ni += di[dij]
            nj += dj[dij]
            field[ni][nj] = 1

pprint.pprint(field)

'''
7
4 6
2 8
3 2
1 3
3 4
1 5
'''


answer = 0
# 처음과 끝에있는 1 찾기
for i in field:
    if 1 in i:
        # 시작 idx는 바로 찾기
        start_idx = i.index(1)
        # 끝 idx는 뒤집어서 찾기
        i = i[::-1]
        end_idx = 20 - i.index(1)
        # 끝 - 처음 + 1 이 그 행에서의 1이 채워진 갯수
        answer += end_idx - start_idx + 1
        # print(start_idx, end_idx)
print(answer)















#
# '''
# 1, 2, 3, 4중에서 한번만 나온거 -> 제일 큰 직사각형
#
# '''
#
# # 넓이당 참외의 갯수
# n = int(input())

# 참외 밭
# melon_field = [list(map(int, input().split())) for _ in range(6)]

