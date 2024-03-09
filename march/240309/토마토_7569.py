from collections import deque

# 6방향
di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

def bfs():
    visited = [[[0] * x for _ in range(y)] for _ in range(z)]
    # 익은 토마토가 있는 곳은 1
    for i in ls:
        visited[i[0]][i[1]][i[2]] = 1
    # 토마토가 없는 곳은 -1을 해줌 -> 이걸 하는 이유는 나중에 visited로 0이 있는지 확인하려고
    for i in no_tomato:
        visited[i[0]][i[1]][i[2]] = -1

    # print(visited)
    q = deque(ls)
    real_cnt = 0

    while q:
        current_z, current_y, current_x, cnt = q.popleft()
        if real_cnt < cnt:
            real_cnt = cnt
        # print(current_z, current_y, current_x, cnt)
        for next in range(6):
            # 범위안에 있고
            if 0 <= current_z+di[next] < z and 0 <= current_y+dj[next] < y and 0 <= current_x+dk[next] < x:
                # 방문하지 않았고
                if not visited[current_z+di[next]][current_y+dj[next]][current_x+dk[next]]:
                    # 안익은 토마토가 존재하면
                    if arr[current_z+di[next]][current_y+dj[next]][current_x+dk[next]] == 0:
                        # 방문표시
                        visited[current_z + di[next]][current_y + dj[next]][current_x + dk[next]] = 1
                        # append 이때 cnt 1증가
                        q.append([current_z + di[next], current_y + dj[next], current_x + dk[next], cnt+1])

    # print('visited :', visited)
    # print(real_cnt)
    a = 0
    for i in range(z):
        for j in range(y):
            # 하나라도 visited중에 0이있다면
            if not all(visited[i][j]):
                # 익지 못한 토마토가 있음
                print(-1)
                a = 1
                break
        if a == 1:
            break

    else:
        print(real_cnt)


x, y, z = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(y)] for _ in range(z)]
# print(arr)

# 익은 토마토 담을 ls
ls = []
# 없는칸
no_tomato = []

# arr순회하며 익은 토마토 찾아서 ls에 append
for i in range(z):
    for j in range(y):
        for k in range(x):
            if arr[i][j][k] == 1:
                # 0을 붙이는 이유는 bfs에서 횟수를 세워주기 위함
                ls.append([i, j, k, 0])
            if arr[i][j][k] == -1:
                no_tomato.append([i, j, k])
# print(ls)

bfs()