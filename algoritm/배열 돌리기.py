from pprint import pprint

# 시계방향 90도
def rotate(arr):
    return [list(row[::-1]) for row in zip(*arr)]

# 반시계방향 90도
def rotate_1(arr):
    return [list(row) for row in zip(*arr)]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(4):
    arr = rotate(arr)               # 각 depth 마다 배열을 4번 돌리면서(4번 돌리면 원위치)
    pprint(arr)

'''
10
1 1 1 0 0 0 0 2 2 2
1 1 1 1 0 0 0 0 2 2
1 0 1 1 0 0 0 0 2 2
0 0 1 1 1 0 0 0 0 2
0 0 0 1 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 0 0 0 0
0 0 0 0 3 3 3 0 0 0
0 0 0 0 0 0 0 0 0 0
'''