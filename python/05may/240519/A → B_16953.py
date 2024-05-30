from collections import deque

a, b = map(int, input().split())

def bfs():
    visited = set()
    visited.add(a)
    q = deque([[a, 1]])

    while q:
        now, cnt = q.popleft()

        if now == b:
            return cnt

        # x 2 (곱하기 2)의 경우
        nxt = now * 2
        # 방문하지 않았고 10^9이하이면
        if nxt not in visited and now <= 1000000000:
            visited.add(nxt)
            q.append([nxt, cnt+1])

        # 뒤에 1 추가하는 경우
        nxt = now*10 + 1
        # 방문하지 않았고 10^9이하이면
        if nxt not in visited and now <= 1000000000:
            visited.add(nxt)
            q.append([nxt, cnt+1])

    else:
        return -1

print(bfs())