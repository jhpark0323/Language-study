import sys
from collections import deque
from pprint import pprint

'''
1. 방향을 설정
-> 가로방향 : 0, 대각선 방향 : 1, 세로방향 : 2
2. 방향과 끝점을 q에 넣어 bfs 돌림
'''

# 방향 가로 대각선 세로
di = [0, 1, 1]
dj = [1, 1, 0]


input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
# print(arr)

dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
pprint(dp)

