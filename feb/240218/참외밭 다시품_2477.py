'''
큰 사각형에서 작은 사각형을 빼서 구하기
전체 중에서 제일 긴 두변이 큰 사각형의 가로 세로
큰 사각형의 가로 세로가 나온 전 후에 있는게 빼야할 길이
ex) 제일긴 두변 : 160, 50
큰 사각형의 가로 세로 전 후 길이 : 100, 30 -> 빼야함
작은 사각형의 가로 세로 : 160 - 100, 50 - 30
'''

# 넓이당 참외의 갯수
n = int(input())

# 참외 밭
melon_field = [list(map(int, input().split())) for _ in range(6)]

# 가로방향 인 것
max_j = 0
max_j_idx = 0
# 세로방향 인 것
max_i = 0
max_i_idx = 0

# 제일 긴 변 두개를 찾아 그게 제일 큰 사각형의 가로 세로임을 찾기
# 방향에 따라 긴변을 따로 구함
# 이 때 index도 같이 구함
for k in range(6):
    # 방향과 길이
    dij, length = melon_field[k][0], melon_field[k][1]
    # 가로
    if dij == 1 or dij == 2:
        if max_j < length:
            max_j = length
            max_j_idx = k
    # 세로
    if dij == 3 or dij == 4:
        if max_i < length:
            max_i = length
            max_i_idx = k

# print(max_j_idx, max_j)
# print(max_i_idx, max_i)

# 어떤 변이 꺾여 들어가는지 찾아야 할듯
# 둘중 index가 큰거보다 하나더 큰거, 작은거보다 1 작은거 -> 꺾여서 빼야함
# 이 때 1과 6이 나오는 경우만 빼고 -> 이때만 1보다 큰거, 6보다 작은거 구하기

# 세로의 index가 가로의 index보다 클 때
if max_i_idx < max_j_idx:
    # 1과 6이 나오면
    if max_i_idx == 0 and max_j_idx == 5:
        minus_j_idx = 1
        minus_i_idx = 4
    else:
        # 작은거보다 작고 큰거보다 크게
        minus_j_idx = max_i_idx - 1
        minus_i_idx = (max_j_idx + 1) % 6

else:
    # 1과 6이 나오면
    if max_j_idx == 0 and max_i_idx == 5:
        minus_i_idx = 1
        minus_j_idx = 4

    else:
        # 작은거보다 작고 큰거보다 크게
        minus_i_idx = max_j_idx - 1
        minus_j_idx = (max_i_idx + 1) % 6

# print(minus_i_idx, minus_j_idx)

len_minus_i = max_i - melon_field[minus_i_idx][1]
len_minus_j = max_j - melon_field[minus_j_idx][1]
# print(len_minus_i, len_minus_j)

answer = max_i * max_j - len_minus_i * len_minus_j
print(answer*n)