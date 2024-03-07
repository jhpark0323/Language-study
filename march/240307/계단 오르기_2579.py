
'''
DP로 다시풀자 그냥 DP이번에 마스터하자
'''

from collections import deque

def bfs(i):
    visited = set()
    visited.add(0)
    q = deque([0, i])
    # 점수
    score = 0
    # 오른 계단 수
    cnt_stair = 0

    while q:
        current, up_stair = q.popleft()
        score += current
        cnt_stair += up_stair

        if cnt_stair == n:

        for next in (current+1, current+2):


n = int(input())

stair = [0] + [int(input()) for _ in range(n)]
print(stair)


