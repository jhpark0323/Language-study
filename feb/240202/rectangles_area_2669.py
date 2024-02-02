rec = [list(map(int, input().split())) for _ in range(4)]

# xy평면
xy_plane = [[0 for i in range(100)] for j in range(100)]

# 직사각형 좌표(i[0], i[1]) -> 왼쪽 아래 좌표, (i[2], i[3]) -> 오른쪽 위 좌표
for i in rec:
    # 가로의 좌표들 순회
    for j in range(i[0], i[2]):
        # 세로의 좌표들 순회
        for k in range(i[1], i[3]):
            # 만난좌표에 1대입
            xy_plane[j][k] = 1

ans = 0

for i in xy_plane:
    ans += sum(i)

print(ans)
