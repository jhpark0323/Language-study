'''
1. 4개로 나누었을 때 어디 있는지 파악
1-1. 기준을 전체 크기의 절반으로 설정하여 절반보다 클때와 작을 때를 가지고 위치 찾기
2. 반복 (n번)
'''

import sys

n, r, c = map(int, sys.stdin.readline().strip().split())

# 기준
standard = (2 ** n) // 2
cnt = 0
for i in range(n-1, -1, -1):
    # row, col이 기준 미만 이면 -> 0번째 박스
    if r < standard and c < standard:
        pass
    # row : 기준 미만, col : 기준 이상 -> 1번째 박스
    elif r < standard and standard <= c:
        c -= standard
        cnt += (2**i)**2

    # row : 기준 이상, col : 기준 미만 -> 2번째 박스
    elif standard <= r and c < standard:
        r -= standard
        cnt += (2**i)**2 * 2

    # 3번째 박스
    else:
        r -= standard
        c -= standard
        cnt += (2**i)**2 * 3

    standard //= 2

print(cnt)