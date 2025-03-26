
'''
최대와 최솟값을 찾아 기준을 잡고 모든칸을 다 비교해서 시간 제일 적게 걸릴 때를 찾기
'''

import sys

# n : 세로, m : 가로, b : 시작시 가진 블럭의 수
n, m, b = map(int, sys.stdin.readline().strip().split())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
# print(arr)

min_block = float('inf')
max_block = -float('inf')

for i in range(n):
    for j in range(m):
        # 최대 최솟값 찾기
        if arr[i][j] < min_block:
            min_block = arr[i][j]

        if max_block < arr[i][j]:
            max_block = arr[i][j]
# print(min_block, max_block)

min_time = float('inf')
height = arr[0][0]

# 처음부터 땅의 높이가 일정하면
if min_block == max_block:
    print(0, height)
    exit()

# 기준을 최솟값부터 최댓값까지 잡음
for standard in range(min_block, max_block+1):
    # 시간 초기화
    time = 0
    # 시작시 가진 블럭 수
    given_block = b
    # 모든 칸을 순회
    for i in range(n):
        for j in range(m):
            # 필요한 갯수를 현재 땅에서 기준을 뺸만큼으로 설정
            need = arr[i][j] - standard
            # 필요한 갯수가 양수면
            if need >= 0:
                # need크기만큼 제거 해야함
                time += 2 * need
                # 블럭 추가
                given_block += need
            # 필요한 갯수가 음수면
            else:
                # need 크기만큼 추가함
                need = abs(need)
                # 시간 추가
                time += need
                # 블럭 사용
                given_block -= need
    # 다 돌았을 때 블럭의 갯수가 음수면
    if given_block < 0:
        # 실패
        continue
    # 최소시간 초기화
    if min_time >= time:
        min_time = time
        height = standard

print(min_time, height)