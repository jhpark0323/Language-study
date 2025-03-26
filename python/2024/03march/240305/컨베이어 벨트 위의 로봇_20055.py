import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

ls = list(map(int, sys.stdin.readline().strip().split()))
ls = deque(ls)
# print(ls)

# 로봇들의 위치를 담은 ls
robot = deque([0] * (n))

# 횟수세기
cnt = 1
while 1:
    # 1단계 벨트가 로봇과 함께 한칸 회전
    # 맨뒤에서 하나 pop, 앞에 append
    ls.appendleft(ls.pop())
    robot.appendleft(robot.pop())

    # 로봇이 내리는 위치 도착시 내림
    if robot[-1] == 1:
        robot[-1] = 0

    # 2단계
    # 로봇이 있으면 한칸씩 뒤로 밈 -> 이때 뒤 벨트가 0이 아니어야함
    if any(robot):
        # robot을 뒤에서부터 순회하며 움직일수있는지 찾음 -> (처음과 마지막에는 없겠지만 걍 헷갈려서 다 넣음)
        for i in range(n-1, -1, -1):
            # robot이 있다면
            if robot[i] == 1:
                # ls의 다음 칸 내구도가 1이상이고 로봇이 없으면 움직임
                # 이 때 robot의 마지막 칸에는 robot이 절대 없으므로 ls[i+1]에서는 index error 안뜰듯
                if ls[i+1] >= 1 and robot[i+1] == 0:
                    robot[i] = 0
                    robot[i+1] = 1
                    # 내구도 빼기
                    ls[i+1] -= 1

    # 로봇이 내리는 위치 도착시 내림
    if robot[-1] == 1:
        robot[-1] = 0

    # 3단계
    # 올리는 위치에 있는 칸의 내구도가 0보다 크면
    if ls[0] > 0:
        # 올리는 위치에 로봇 올리기
        robot[0] = 1
        ls[0] -= 1

    # 4단계
    if ls.count(0) >= k:
        break
    # 횟수 증가
    cnt += 1

print(cnt)