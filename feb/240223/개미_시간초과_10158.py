
'''
개미가 (+1, +1)씩 움직이다가 벽(0 or w or h)을 만나면 그 좌표(가로 or 세로)가 -1씩 증가로 바뀜
가로랑 세로를 따로 생각하면 될듯
'''

# w : 가로, h : 세로
w, h = map(int, input().split())

# 초기 개미 위치
start_w, start_h = map(int, input().split())

# 시간
t = int(input())

# 방향
di = [1, -1]

# 기본 방향 = 0 (증가)
direction_w = 0
direction_h = 0

# t시간만큼 순회
for i in range(t):
    # 가로를 가고있는 방향으로 1씩증가시킴
    start_w += di[direction_w]

    # 세로를 가고있는 방향으로 1씩 증가시킴
    start_h += di[direction_h]

    # 가로가 0이나 최댓값을 만나면 방향을 전환 시킨다
    if start_w == 0 or start_w == w:
        direction_w = 1 - direction_w

    # 세로가 0이나 최댓값을 만나면 방향을 전환 시킨다
    if start_h == 0 or start_h == h:
        direction_h = 1 - direction_h

    # print(start_w, start_h)

print(start_w, start_h)