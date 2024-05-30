import sys
from collections import deque

def bfs():
    # 0번째 칸 버림
    visited = [0] * 101
    # 시작
    visited[1] = 1
    # q에 시작값과 cnt할 0 넣기
    q = deque([[1, 0]])

    while q:
        current, cnt = q.popleft()

        # 기저조건
        if current >= 100:
            return cnt

        # 주사위 굴리기
        for i in range(1, 7):
            nxt = current + i

            # 방문 안했으면
            if 0 <= nxt <= 100 and not visited[nxt]:

                # 사다리 밟으면
                if nxt in ladder_dict:
                    nxt = ladder_dict[nxt]

                # 뱀 밟으면
                if nxt in snake_dict:
                    nxt = snake_dict[nxt]

                q.append([nxt, cnt+1])
                visited[nxt] = 1


ipt = sys.stdin.readline
ladder_n, snake_n = map(int, ipt().strip().split())
ladder = [list(map(int, ipt().strip().split())) for _ in range(ladder_n)]
snake = [list(map(int, ipt().strip().split())) for _ in range(snake_n)]
# print(ladder)
# print()
# print(snake)

ladder_dict = {}
for i in range(ladder_n):
    ladder_dict[ladder[i][0]] = ladder[i][1]

snake_dict = {}
for i in range(snake_n):
    snake_dict[snake[i][0]] = snake[i][1]

# print(ladder_dict)
# print(snake_dict)

count = bfs()
print(count)