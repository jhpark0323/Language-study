from collections import deque

start, end = map(int, input().split())

# 동생의 숫자가 수빈의 숫자보다 작으면
if start >= end:
    exit(print(start-end))

def bfs():
    visited = set()
    visited.add(start)
    # 시작점, 시간
    q = deque([[start, 0]])

    while q:
        current, time = q.popleft()

        if current == end:
            return time

        # 3개의 경우
        # 1번
        next_1 = current-1
        if next_1 not in visited:
            q.append([next_1, time+1])

        # 2번
        next_2 = 2*current
        if next_2 not in visited:
            q.append([next_2, time])

        # 3번
        next_3 = current+1
        if next_3 not in visited:
            q.append([next_3, time+1])

ans = bfs()
print(ans)