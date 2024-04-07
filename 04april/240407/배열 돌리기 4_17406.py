import sys
from copy import deepcopy
from pprint import pprint
from itertools import permutations

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rotation_ls = [list(map(int, input().split())) for _ in range(k)]
# print(arr)
# print(rotation_ls)

def rotation(row, col, n, cp_arr):
    start = cp_arr[row][col]
    # print('row : ', row)
    # print('col : ', col)

    # 왼쪽
    for i in range(n-1):
        cp_arr[row+i][col] = cp_arr[row+1+i][col]
        # print('row : ', row+i)
        # print('col : ', col)

    # 아래쪽
    for i in range(n-1):
        cp_arr[row+n-1][col+i] = cp_arr[row+n-1][col+i+1]
        # print('row : ', row+n-1)
        # print('col : ', col+n-1-(i+1))
        # print('col : ', col+n-1-i)

    # 오른쪽
    for i in range(n-1):
        cp_arr[row+n-1-i][col+n-1] = cp_arr[row+n-1-(i+1)][col+n-1]

    # 위쪽
    for i in range(n-1):
        cp_arr[row][col+n-1-i] = cp_arr[row][col+n-1-(i+1)]

    # 마지막
    cp_arr[row][col+1] = start

    return cp_arr

p = [i for i in range(k)]

permu = permutations(p, k)

min_arr = float('inf')
for per in permu:
# for ls in rotation_ls:
    cp_arr = deepcopy(arr)
    for each in per:
        r, c, s = rotation_ls[each][0], rotation_ls[each][1], rotation_ls[each][2]
        standard_row, standard_col = r - s - 1, c - s - 1
        for length in range(s, 0, -1):
            # 길이가 홀수라서 무조건 마지막은 하나만 남음
            num = 2*length+1
            # print(num)

            # print('standard_row : ', standard_row)
            # print('standard_col : ', standard_col)
            # 회전
            cp_arr = rotation(standard_row, standard_col, num, cp_arr)
            # 넘어가기 전에 바꿔줌
            standard_row += 1
            standard_col += 1
            # pprint(cp_arr)


    for i in cp_arr:
        score = sum(i)
        if min_arr > score:
            min_arr = score

print(min_arr)